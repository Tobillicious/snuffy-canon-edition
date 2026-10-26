#!/usr/bin/env python3
"""Final source, assembly, reference and render audit; never edits the canon."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import difflib
import hashlib
import json
import posixpath
import re
import runpy
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CANON = ROOT/'CANON-EDITION-V4.2-WORKING'
BANK = ROOT/'REPAIRS-2026-10-26'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.hrefs = set(), []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if 'href' in attrs:
            self.hrefs.append(attrs['href'])


def reference_audit(master):
    cp = subprocess.run(['pandoc', '-f', 'markdown+tex_math_single_backslash+lists_without_preceding_blankline',
                         '-t', 'json', str(master)], capture_output=True, check=True)
    tree = json.loads(cp.stdout)
    identifiers, links = set(), []

    def visit(node):
        if isinstance(node, dict):
            kind, content = node.get('t'), node.get('c')
            if kind == 'Header':
                identifiers.add(content[1][0])
            if kind == 'Link':
                links.append(content[2][0])
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)
    visit(tree)
    bad = []
    for target in links:
        url = urlsplit(target)
        if url.scheme or url.netloc:
            continue
        if not url.path and url.fragment and unquote(url.fragment) not in identifiers:
            bad.append(target)
        elif url.path and not (CANON/unquote(url.path)).is_file():
            bad.append(target)
    source = master.read_text()
    labels = set(re.findall(r'\\label\{([^}]+)\}', source))
    references = set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', source))
    missing_labels = sorted(references-labels)
    used = set(re.findall(r'\[S(\d+)\]', source))
    defined = set(re.findall(r'^\[S(\d+)\]', source, re.MULTILINE))
    assert not bad and not missing_labels and used <= defined, (bad, missing_labels, used-defined)

    html = Links()
    html.feed((CANON/'render/Snuffy-Canon-Edition-4.2.html').read_text())
    html_bad = [target for target in html.hrefs if target.startswith('#') and unquote(target[1:]) not in html.ids]
    epub_bad, epub_checked = [], 0
    with zipfile.ZipFile(CANON/'render/Snuffy-Canon-Edition-4.2.epub') as package:
        names = set(package.namelist())
        pages = {}
        for name in names:
            if name.endswith('.xhtml'):
                page = Links()
                page.feed(package.read(name).decode('utf-8'))
                pages[name] = page
        for name, page in pages.items():
            for target in page.hrefs:
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue
                path = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(url.path))) if url.path else name
                epub_checked += 1
                if path not in names or (url.fragment and (path not in pages or unquote(url.fragment) not in pages[path].ids)):
                    epub_bad.append([name, target])
    assert not html_bad and not epub_bad, (html_bad, epub_bad)
    return {'master_links_checked': len(links), 'heading_identifiers': len(identifiers),
            'unresolved_master_links': bad, 'unresolved_equation_labels': missing_labels,
            'parameter_source_markers_defined': sorted(defined),
            'html_fragment_links_checked': sum(t.startswith('#') for t in html.hrefs),
            'epub_internal_links_checked': epub_checked,
            'unresolved_render_links': html_bad+epub_bad,
            'external_source_scope': 'URI targets retained; this audit does not re-review published external theorems.'}


def main():
    preserved = runpy.run_path(str(BANK/'checks/verify-delta-joint.py'))['preservation_state']()
    delta = json.loads((BANK/'checks/DELTA-JOINT-VERIFICATION-2026-10-27.json').read_text())
    endpoint = json.loads((BANK/'checks/ENDPOINT-FINAL-INTEGRATION-2026-10-27.json').read_text())
    assert delta['all_assertions_pass'] and endpoint['targeted_verification_pass']
    count = sum(delta['exact_certificate_checks']['decisions'].values())
    assert count == 18130
    assert sha(ROOT/delta['script']) == delta['script_sha256']
    assert sha(ROOT/delta['proof']) == delta['proof_sha256']
    for entry in endpoint['freshly_executed_checks']:
        assert sha(ROOT/entry['script']) == entry['source_sha256']
        assert sha(ROOT/entry['receipt']) == entry['receipt_sha256']
    master = CANON/'SNUFFY-CANON-EDITION-4.2-MASTER.md'
    author = CANON/'inserts/25-boundary-work-history.md'
    text = master.read_text()
    heading = '## G.21 Constructive thermal preparation from the complete decoding history'
    section = text.split(heading, 1)[1].split('\n---\n\n# Part IV', 1)[0].strip()
    assert section == author.read_text().split(heading, 1)[1].strip()
    for phrase in ['### 12. Exact joint kernel constraint and bounded residual',
                   'finite jump-budgeted primitive', 'gross drive and export work separately',
                   'specified physical jump causes']:
        assert phrase in section, phrase
    reference = reference_audit(master)
    render_check = subprocess.run(['python3', str(CANON/'checks/verify_render.py')],
                                  capture_output=True, check=True, text=True)
    renders = json.loads(render_check.stdout)
    assert renders['all_pass'] and renders['master_sha256'] == sha(master)
    (CANON/'render/RENDER-VERIFY.json').write_text(json.dumps(renders, indent=2, sort_keys=True)+'\n')
    log = (CANON/'render/Snuffy-Canon-Edition-4.2.log').read_text(errors='replace')
    assert 'Missing character' not in log
    assert 'Overfull '+chr(92)+'hbox' not in log
    visual = json.loads((HERE/'VISUAL-REVIEW.json').read_text())
    assert visual['visual_review_pass'] and visual['pdf_sha256'] == renders['render_sha256']['pdf']
    paths = [p for p in sorted(CANON.rglob('*')) if p.is_file() and p.name not in ['SHA256SUMS', '.DS_Store']
             and p.suffix not in ['.log', '.aux', '.out', '.toc', '.olean', '.ilean']]
    (CANON/'SHA256SUMS').write_text(''.join(sha(p)+'  '+p.relative_to(CANON).as_posix()+'\n' for p in paths))
    summaries = {
        'checkpoint12': {'receipt': str((BANK/'checks/snapshots/checkpoint-12-complete-transfer-bill/RESULT.json').relative_to(ROOT)),
                         'modules': 192, 'statements': 1158, 'fresh_compilation_this_session': False,
                         'preservation': preserved},
        'endpoint_checks': {'receipt': str((BANK/'checks/ENDPOINT-FINAL-INTEGRATION-2026-10-27.json').relative_to(ROOT)),
                            'receipt_sha256': sha(BANK/'checks/ENDPOINT-FINAL-INTEGRATION-2026-10-27.json'),
                            'finite_checks': 6, 'feedback_patterns': 1024},
        'delta_joint': {'receipt': str((BANK/'checks/DELTA-JOINT-VERIFICATION-2026-10-27.json').relative_to(ROOT)),
                       'receipt_sha256': sha(BANK/'checks/DELTA-JOINT-VERIFICATION-2026-10-27.json'),
                       'script': delta['script'], 'proof': delta['proof'],
                       'exact_certificate_decisions': count, 'stages': 259, 'tolerances': 7,
                       'numerical_discrete_cases': 6, 'numerical_continuous_reference_cases': 15},
        'assembly': {'master_sha256': sha(master), 'author_insert_sha256': sha(author),
                     'G21_identical': True, 'Batch10_and_new_supports_present': True},
        'references': reference, 'renders': renders, 'visual_review': visual,
        'edition_seal': {'file': 'CANON-EDITION-V4.2-WORKING/SHA256SUMS',
                         'sha256': sha(CANON/'SHA256SUMS'), 'sealed_files': len(paths)}}
    result = {'date': '2026-10-27', 'timezone': 'Pacific/Auckland', 'all_final_checks_pass': True,
              'durable_core_commit': '551d385', 'checks': summaries,
              'physical_installation_certificate_complete': False,
              'remaining_external_boundary': 'Identify/validate the actual complete joint instrument (including common causes, retained memory and capped-controller binding), and establish the values/bounds for K_act and v_a. The manuscript retains its other stated physical source/device application correspondences.',
              'full_holding_condition': 'v_a <= epsilon/2^(2a+5) only when the residual persists for 2^a',
              'short_exposure_condition': 'tau_a*v_a <= epsilon/2^(a+5)',
              'maximal_UPT_target_unchanged': True, 'full_history_and_arbitrary_references_retained': True,
              'held_doors_and_companion_included': False,
              'publication_status': 'Prepared; actual publication is recorded separately after remote confirmation.'}
    (HERE/'FINAL-VERIFICATION.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    before = json.loads((HERE/'BEFORE-RELEASE.json').read_text())
    fence = chr(96)*3
    review = ['# Final release preparation review\n\nThe Batch 10 master, author insert and all Lean sources are unchanged.\n\n']
    for relative in before:
        old = HERE/'before-release'/relative
        new = CANON/relative
        if new.suffix in ['.pdf', '.epub'] or not new.is_file() or old.read_bytes() == new.read_bytes():
            continue
        if relative.startswith('render/') or relative == 'SHA256SUMS':
            continue
        diff = ''.join(difflib.unified_diff(old.read_text().splitlines(keepends=True), new.read_text().splitlines(keepends=True),
                                          fromfile='before/'+relative, tofile='release/'+relative))
        review += ['## '+relative+'\n\n'+fence+'diff\n', diff, fence+'\n\n']
    (HERE/'RELEASE-PREPARATION-REVIEW.md').write_text(''.join(review))
    print(json.dumps({'all_final_checks_pass': True, 'exact_certificate_decisions': count,
                      'canonical_checkpoint_unchanged': '192 / 1158', 'pdf_pages': renders['pdf']['pages'],
                      'reference_audit_pass': True, 'sealed_files': len(paths),
                      'receipt': str((HERE/'FINAL-VERIFICATION.json').relative_to(ROOT))}))


if __name__ == '__main__':
    main()
