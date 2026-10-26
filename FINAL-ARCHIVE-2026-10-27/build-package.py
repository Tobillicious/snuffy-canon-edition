#!/usr/bin/env python3
"""Build and verify a curated, self-contained-layout public deposit bundle."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT.parent/'UPT-FINAL-ARCHIVE-2026-10-27'
PREFIX = 'Snuffy-Canon-Edition-4.2'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit = json.loads((HERE/'FINAL-VERIFICATION.json').read_text())
    assert audit['all_final_checks_pass']
    OUT.mkdir(exist_ok=True)
    files = {}

    def include(path):
        if path.is_file() and path.name != '.DS_Store' and '__pycache__' not in path.parts:
            files[path.relative_to(ROOT).as_posix()] = path

    for path in (ROOT/'CANON-EDITION-V4.2-WORKING').rglob('*'):
        if path.suffix not in ['.log', '.aux', '.out', '.toc', '.olean', '.ilean']:
            include(path)
    for path in (ROOT/'LEDGER-FOUR-STROKE-2026-10-24').rglob('*'):
        include(path)
    bank = ROOT/'REPAIRS-2026-10-26'
    notes = ['G21-ENDPOINT-INSERT-2026-10-27.md', 'DELTA-JOINT-CERTIFICATES-PROOF-2026-10-27.md',
             'JOINT-ENDPOINT-KERNEL-CONSTRAINT-2026-10-27.md',
             'ENDPOINT-FAULT-MODEL-AND-CONTROLLER-COSTS-2026-10-27.md',
             'BOUNDED-PAULI-JUMP-ENDPOINT-2026-10-27.md', 'MICROSCOPIC-PRIVATE-ENDPOINT-2026-10-27.md',
             'NOISE-COMPENSATED-PREPARATION-2026-10-27.md', 'FT-PRIVATE-OUTPUT-BRIDGE-2026-10-27.md',
             'BDL-REFINEMENT-CIRCUIT-2026-10-27.md', 'COMPLETE-TRANSFER-COST-JOIN.md',
             'G21-SOURCE-APPLICATION-AUDIT.md', 'INITIAL-SYNDROME-SPARSITY.md',
             'PROSE-BATCH-09.json', 'MANUSCRIPT-BEFORE-AFTER-BATCH-09.md',
             'PROSE-BATCH-10.json', 'MANUSCRIPT-BEFORE-AFTER-BATCH-10.md', 'MANUSCRIPT-REVIEW-FINAL.diff']
    for name in notes:
        include(bank/name)
    # Preserve every current file explicitly covered by the Batch 10 receipt.
    batch = json.loads((bank/'PROSE-BATCH-10.json').read_text())
    for change in batch['changes']:
        include(ROOT/change['file'])
    for path in (bank/'checks').iterdir():
        if path.suffix in ['.py', '.json']:
            include(path)
    for relative in ['checks/snapshots/checkpoint-12-complete-transfer-bill',
                     'snapshots/before-endpoint-final-10',
                     'checks/development/noise-compensation', 'checks/development/pauli-interface',
                     'checks/endpoint-final-integration', 'checks/bdl-metacheck', 'candidates']:
        for path in (bank/relative).rglob('*'):
            include(path)
    include(bank/'inputs/AUTHOR-DELTA-JOINT-PROOF-2026-10-27.md')
    for name in ['HANDOFF.md', 'FINAL-VERIFICATION.json',
                 'audit-final.py', 'build-package.py', 'publish-zenodo.py', 'VISUAL-REVIEW.json']:
        include(HERE/name)
    for relative, path in files.items():
        assert not any(part.lower() in ['doors', 'companion'] for part in path.parts), relative
        if path.suffix in ['.md', '.html', '.tex']:
            assert not re.search(r'whakapapa|umuntu|ubuntu', path.read_text(errors='ignore'), re.I), relative
    # Verify that all immutable Checkpoint 12 files are in the public package.
    before = json.loads((bank/'snapshots/before-endpoint-final-10/BEFORE-MANIFEST.json').read_text())
    for relative, digest in before['checkpoint12_files'].items():
        assert relative in files and sha(files[relative]) == digest, relative
    manifest = {'date': '2026-10-27', 'core_commit': '551d385',
                'package_layout': PREFIX+'/<original project-relative paths>',
                'files': {name: {'sha256': sha(path), 'bytes': path.stat().st_size}
                          for name, path in sorted(files.items())},
                'manifest_self_hash': 'Excluded to avoid a recursive hash; the outer archive manifest seals this file.',
                'checkpoint12': '192 / 1158 unchanged', 'exact_certificate_decisions': 18130,
                'physical_installation_residual_certified': False,
                'held_material_included': False}
    manifest_path = HERE/'FILE-MANIFEST.json'
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')
    archive = OUT/'Snuffy-Canon-Edition-4.2-Deposit.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as package:
        for name, path in sorted(files.items()):
            package.write(path, PREFIX+'/'+name)
        package.write(manifest_path, PREFIX+'/FINAL-ARCHIVE-2026-10-27/FILE-MANIFEST.json')
        package.writestr(PREFIX+'/README.md',
                        '# Snuffy — Canon Edition 4.2\n\n'
                        'Start with FINAL-ARCHIVE-2026-10-27/HANDOFF.md and FINAL-VERIFICATION.json.\n'
                        'The master and PDF/EPUB/HTML are under CANON-EDITION-V4.2-WORKING/.\n'
                        'Checkpoint 12: 192 modules / 1,158 names, unchanged.\n'
                        'The residual checker records 18,130 exact certificate decisions.\n'
                        'The complete actual physical installation/model and parameter boundary remains explicit.\n')
    with zipfile.ZipFile(archive) as package:
        assert package.testzip() is None
        for name, item in manifest['files'].items():
            assert hashlib.sha256(package.read(PREFIX+'/'+name)).hexdigest() == item['sha256'], name
    digest = sha(archive)
    checksum = archive.with_suffix(archive.suffix+'.sha256')
    checksum.write_text(digest+'  '+archive.name+'\n')
    paths = [archive, checksum, ROOT/'CANON-EDITION-V4.2-WORKING/render/Snuffy-Canon-Edition-4.2.pdf',
             ROOT/'CANON-EDITION-V4.2-WORKING/render/Snuffy-Canon-Edition-4.2.epub',
             ROOT/'CANON-EDITION-V4.2-WORKING/render/Snuffy-Canon-Edition-4.2.html',
             HERE/'FINAL-VERIFICATION.json', manifest_path]
    upload = {'date': '2026-10-27', 'all_package_checks_pass': True,
              'files': [{'path': str(path), 'name': path.name, 'sha256': sha(path),
                         'md5': hashlib.md5(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
                        for path in paths],
              'metadata_path': str(ROOT/'CANON-EDITION-V4.2-WORKING/zenodo.json'),
              'metadata_sha256': sha(ROOT/'CANON-EDITION-V4.2-WORKING/zenodo.json')}
    (HERE/'UPLOAD-MANIFEST.json').write_text(json.dumps(upload, indent=2)+'\n')
    print(json.dumps({'package_pass': True, 'files': len(files), 'bytes': archive.stat().st_size,
                      'sha256': digest, 'archive': str(archive)}))


if __name__ == '__main__':
    main()
