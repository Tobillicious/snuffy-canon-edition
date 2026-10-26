#!/usr/bin/env python3
"""Build review batch 10 against the preserved staged batch-09 postimage."""
from pathlib import Path
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
BANK = HERE.parent
ROOT = BANK.parent
SNAPSHOT = BANK/'snapshots/before-endpoint-final-10'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    before = json.loads((SNAPSHOT/'BEFORE-MANIFEST.json').read_text())
    for relative, digest in before['preserved_batch09'].items():
        assert sha((ROOT/relative).read_bytes()) == digest, relative
    canonical = 'CANON-EDITION-V4.2-WORKING/'
    review_files = [canonical+'SNUFFY-CANON-EDITION-4.2-MASTER.md',
                    canonical+'inserts/25-boundary-work-history.md',
                    canonical+'REPAIR-STATUS.md']
    diffs, changes = [], []
    for relative in before['working']:
        prior = SNAPSHOT/'working'/relative
        current = ROOT/relative
        if prior.read_bytes() == current.read_bytes():
            continue
        change = {'file': relative, 'working_before_sha256': sha(prior.read_bytes()),
                  'after_sha256': sha(current.read_bytes())}
        baseline = SNAPSHOT/'batch09-index'/relative
        if baseline.is_file():
            change['batch09_index_sha256'] = sha(baseline.read_bytes())
        changes.append(change)
    for relative in review_files:
        baseline = SNAPSHOT/'batch09-index'/relative
        diff = ''.join(difflib.unified_diff(baseline.read_text().splitlines(keepends=True),
                                          (ROOT/relative).read_text().splitlines(keepends=True),
                                          fromfile='batch09/'+relative,
                                          tofile='final/'+relative))
        assert diff, relative
        diffs.append((relative, diff))
    raw = ''.join(diff for _, diff in diffs)
    raw_path = BANK/'MANUSCRIPT-REVIEW-FINAL.diff'
    raw_path.write_text(raw)
    fence = chr(96)*3
    review = ['# Manuscript before/after batch 10\n\n',
              '27 October 2026, Pacific/Auckland. Local author review. The before images are ',
              'the hash-matched staged Batch 09 postimages; the separate working-entry ',
              'snapshot preserves the incoming partial sub-agent integration as well. ',
              'Batches 07–09 and canonical Checkpoint 12 remain unchanged.\n\n',
              'This batch integrates bounded Pauli common causes, the gross reset/export ',
              'invoice and the full-instrument residual constraint. The controller stage ',
              'degree remains 3 K_c+5. The residual allocation is epsilon/2^(a+5) inside ',
              'the original epsilon/2^(a+2) stage ceiling. Its actual installation value ',
              'is still unverified; no global completion or publication is asserted.\n\n']
    for relative, diff in diffs:
        review += ['## '+relative+'\n\n', fence+'diff\n', diff, fence+'\n\n']
    review_path = BANK/'MANUSCRIPT-BEFORE-AFTER-BATCH-10.md'
    review_path.write_text(''.join(review))
    manifest = {'date': '2026-10-27', 'timezone': 'Pacific/Auckland',
                'status': 'Local integration complete; installation joint-kernel residual not certified.',
                'scope': 'Prose and finite-check integration; no canonical Lean modification or new full compilation.',
                'canonical_modules': 192, 'canonical_public_names': 1158,
                'canonical_lean_modified': False,
                'before_images': str(SNAPSHOT.relative_to(BANK)),
                'review_baseline': 'Preserved index matching the exact Batch 09 postimage hashes.',
                'changes': changes,
                'new_derivation': 'JOINT-ENDPOINT-KERNEL-CONSTRAINT-2026-10-27.md',
                'new_derivation_sha256': sha((BANK/'JOINT-ENDPOINT-KERNEL-CONSTRAINT-2026-10-27.md').read_bytes()),
                'review_diff': raw_path.name, 'review_diff_sha256': sha(raw_path.read_bytes()),
                'review_markdown': review_path.name, 'review_markdown_sha256': sha(review_path.read_bytes()),
                'controller_degree': '3 K_c + 5',
                'K_c': 'max(2g kappa+nu+4,3g+nu,3g+4nu+1)',
                'residual_allocation': 'delta_joint <= epsilon/2^(a+5)',
                'original_stage_ceiling': 'epsilon/2^(a+2)',
                'joint_kernel_identified_for_installation': False,
                'installation_residual_value_certified': False,
                'maximal_target_unchanged': True, 'full_history_retained': True,
                'global_physical_completion_claimed': False,
                'merge_push_publication_performed': False,
                'review_builder_sha256': sha(Path(__file__).read_bytes())}
    (BANK/'PROSE-BATCH-10.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'review': str(review_path.relative_to(ROOT)),
                      'raw_diff': str(raw_path.relative_to(ROOT)),
                      'changed_preserved_files': len(changes)}))


if __name__ == '__main__':
    main()
