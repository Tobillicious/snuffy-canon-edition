#!/usr/bin/env python3
"""Run targeted endpoint checks and verify the final prose/source receipt.

Reuses hash-matched canonical and development Lean receipts explicitly.
Never modifies or recompiles canonical Checkpoint 12.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
BANK = HERE.parent
ROOT = BANK.parent
CANON = ROOT/'CANON-EDITION-V4.2-WORKING'
SNAPSHOT = BANK/'snapshots/before-endpoint-final-10'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def verify_recorded_sources(receipt, fallback_script):
    sources = receipt['source_sha256']
    if isinstance(sources, str):
        assert sha(fallback_script) == sources, fallback_script
    else:
        for name, digest in sources.items():
            choices = [HERE/name, HERE/'bdl-metacheck'/name]
            path = next(p for p in choices if p.is_file())
            assert sha(path) == digest, path


def verify_unchanged():
    before = read_json(SNAPSHOT/'BEFORE-MANIFEST.json')
    for group in ['checkpoint12_files', 'canonical_lean_sources', 'preserved_batch09']:
        for relative, digest in before[group].items():
            assert sha(ROOT/relative) == digest, relative
    assert {p.relative_to(ROOT).as_posix() for p in (CANON/'lean').rglob('*.lean')} == set(before['canonical_lean_sources'])
    checkpoint = HERE/'snapshots/checkpoint-12-complete-transfer-bill'
    hashes = read_json(checkpoint/'SOURCE-HASHES.json')
    assert len(hashes) == 192
    sources = CANON/'lean/Snuffy'
    assert {p.name for p in sources.glob('*.lean')} == set(hashes)
    assert all(sha(sources/name) == digest for name, digest in hashes.items())
    assert read_json(checkpoint/'RESULT.json')['overall_pass']
    audit = (CANON/'lean/SummitsAudit.lean').read_text()
    assert len(re.findall(r'^#print axioms ', audit, flags=re.MULTILINE)) == 1158
    return {'modules': 192, 'public_names': 1158,
            'all_module_source_hashes_match': True,
            'entire_checkpoint_snapshot_unchanged_files': len(before['checkpoint12_files']),
            'all_canonical_lean_source_files_unchanged': len(before['canonical_lean_sources']),
            'batch09_artifacts_unchanged': True,
            'fresh_lean_compilation_in_this_run': False}


def verify_prose():
    batch = read_json(BANK/'PROSE-BATCH-10.json')
    assert batch['maximal_target_unchanged'] and not batch['canonical_lean_modified']
    for entry in batch['changes']:
        assert sha(ROOT/entry['file']) == entry['after_sha256'], entry['file']
        assert sha(SNAPSHOT/'working'/entry['file']) == entry['working_before_sha256']
        if 'batch09_index_sha256' in entry:
            assert sha(SNAPSHOT/'batch09-index'/entry['file']) == entry['batch09_index_sha256']
    for field in ['review_diff', 'review_markdown', 'new_derivation']:
        assert sha(BANK/batch[field]) == batch[field+'_sha256']
    master = (CANON/'SNUFFY-CANON-EDITION-4.2-MASTER.md').read_text()
    author = (CANON/'inserts/25-boundary-work-history.md').read_text()
    heading = '## G.21 Constructive thermal preparation from the complete decoding history'
    end = '\n---\n\n# Part IV'
    main_section = master.split(heading, 1)[1].split(end, 1)[0].strip()
    author_section = author.split(heading, 1)[1].strip()
    assert main_section == author_section
    endpoint = (BANK/'G21-ENDPOINT-INSERT-2026-10-27.md').read_text().strip()
    assert main_section.count(endpoint) == 1
    baseline = (SNAPSHOT/'batch09-index/CANON-EDITION-V4.2-WORKING/SNUFFY-CANON-EDITION-4.2-MASTER.md').read_text()
    assert master.split(heading, 1)[0] == baseline.split(heading, 1)[0]
    assert master.split(end, 1)[1] == baseline.split(end, 1)[1]
    return {'master_author_G21_identical': True,
            'endpoint_source_insert_identical': True,
            'master_outside_G21_unchanged_from_batch09': True,
            'review_diff_sha256': batch['review_diff_sha256'],
            'review_markdown_sha256': batch['review_markdown_sha256'],
            'physical_joint_kernel_identified': False,
            'actual_residual_value_certified': False,
            'residual_allocation': batch['residual_allocation']}


def main():
    canonical = verify_unchanged()
    prose = verify_prose()
    records = []
    out = HERE/'endpoint-final-integration'
    out.mkdir(exist_ok=True)
    tests = [('endpoint-controller-exact.py', 'ENDPOINT-CONTROLLER-EXACT.json'),
             ('noise-compensation-exact.py', 'NOISE-COMPENSATION-EXACT.json'),
             ('pauli-interface-exact.py', 'PAULI-INTERFACE-EXACT.json'),
             ('microscopic-endpoint.py', 'MICROSCOPIC-ENDPOINT.json'),
             ('correlated-pauli-jump.py', 'CORRELATED-PAULI-JUMP.json'),
             ('endpoint-residual-exact.py', 'ENDPOINT-RESIDUAL-EXACT.json')]
    env = dict(os.environ, PYTHONHASHSEED='0')
    for script, output in tests:
        started = time.monotonic()
        cp = subprocess.run([sys.executable, str(HERE/script)], cwd=ROOT,
                            capture_output=True, timeout=180, env=env)
        log = out/(Path(script).stem+'.log')
        log.write_bytes(cp.stdout+cp.stderr)
        assert cp.returncode == 0, (script, cp.returncode, log.read_text())
        receipt = read_json(HERE/output)
        assert receipt.get('all_assertions_pass', receipt.get('all_exact_checks_pass', False)), script
        verify_recorded_sources(receipt, HERE/script)
        records.append({'script': str((HERE/script).relative_to(ROOT)),
                        'source_sha256': sha(HERE/script),
                        'receipt': str((HERE/output).relative_to(ROOT)),
                        'receipt_sha256': sha(HERE/output),
                        'log': str(log.relative_to(ROOT)), 'log_sha256': sha(log),
                        'exit': cp.returncode, 'freshly_executed': True,
                        'scope': receipt['scope']})
        print(json.dumps({'check': script, 'pass': True,
                          'seconds': round(time.monotonic()-started, 2)}), flush=True)

    reused = []
    for label in ['noise-compensation', 'pauli-interface']:
        path = HERE/'development'/label/'RESULT.json'
        receipt = read_json(path)
        assert receipt['pass'] and receipt['standard_axioms_only']
        assert receipt['compiler_output_bytes'] == receipt['kernel_output_bytes'] == 0
        assert sha(Path(receipt['source'])) == receipt['source_sha256']
        reused.append({'receipt': str(path.relative_to(ROOT)), 'receipt_sha256': sha(path),
                       'statements': receipt['statement_count'],
                       'source_hash_matches': True, 'freshly_recompiled': False})

    # Check preservation again after executing scripts, and validate the
    # original feedback count separately from numerical generator checks.
    assert verify_unchanged() == canonical
    assert verify_prose() == prose
    assert read_json(HERE/'ENDPOINT-CONTROLLER-EXACT.json')['feedback']['fault_patterns_checked'] == 1024
    cp = subprocess.run(['git', 'diff', '--check', '--',
                         'CANON-EDITION-V4.2-WORKING',
                         '00-HANDOFF-CURRENT-2026-10-26.md',
                         'REPAIRS-2026-10-26/G21-ENDPOINT-INSERT-2026-10-27.md',
                         'REPAIRS-2026-10-26/ENDPOINT-FAULT-MODEL-AND-CONTROLLER-COSTS-2026-10-27.md'],
                        cwd=ROOT, capture_output=True)
    assert cp.returncode == 0, cp.stdout.decode()+cp.stderr.decode()
    result = {'date': '2026-10-27', 'timezone': 'Pacific/Auckland',
              'scope': 'Fresh targeted finite endpoint tests plus prose/source/hash audit; no new full Lean run or installed-kernel certificate.',
              'targeted_verification_pass': True,
              'canonical_checkpoint12': canonical, 'manuscript': prose,
              'freshly_executed_checks': records,
              'reused_development_kernel_receipts': reused,
              'controller_degree': '3 K_c + 5',
              'original_stage_ceiling': 'epsilon/2^(a+2)',
              'joint_residual_allocation': 'epsilon/2^(a+5)',
              'generic_unidentified_channel_residual_bound': 2,
              'installation_joint_residual_value_certified': False,
              'maximal_target_unchanged': True, 'full_history_retained': True,
              'arbitrary_reference_tests_retained': True,
              'global_physical_completion_claimed': False,
              'merge_push_publication_performed': False,
              'prose_batch_sha256': sha(BANK/'PROSE-BATCH-10.json'),
              'verification_script_sha256': sha(Path(__file__))}
    path = HERE/'ENDPOINT-FINAL-INTEGRATION-2026-10-27.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'targeted_verification_pass': True,
                      'fresh_checks': len(records),
                      'canonical_modules_unchanged': 192,
                      'canonical_statements_unchanged': 1158,
                      'physical_installation_residual_certified': False,
                      'receipt': str(path.relative_to(ROOT))}), flush=True)


if __name__ == '__main__':
    main()
