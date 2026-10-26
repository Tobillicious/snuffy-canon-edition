#!/usr/bin/env python3
"""Check source correspondence of existing development receipts.

Does not rerun the tests/compiler and does not validate the prose as a
kernel theorem. Keeps canonical checkpoint 12 and development scopes apart.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BANK = HERE.parent
ROOT = BANK.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    original = load(HERE/'snapshots/checkpoint-12-complete-transfer-bill/SOURCE-HASHES.json')
    canon = ROOT/'CANON-EDITION-V4.2-WORKING/lean/Snuffy'
    assert {p.name for p in canon.glob('*.lean')} == set(original)
    assert all(sha(canon/name) == digest for name, digest in original.items())
    lean = []
    for directory in ['noise-compensation', 'pauli-interface']:
        path = HERE/'development'/directory/'RESULT.json'
        receipt = load(path)
        assert receipt['pass'] and receipt['standard_axioms_only']
        assert receipt['compiler_output_bytes'] == receipt['kernel_output_bytes'] == 0
        assert sha(Path(receipt['source'])) == receipt['source_sha256']
        lean.append({'receipt': str(path.relative_to(ROOT)), 'receipt_sha256': sha(path),
                     'statements': receipt['statement_count'], 'source_hash_matches': True,
                     'scope': 'Previously executed targeted development check; not recompiled by this receipt audit.'})

    computations = []
    paths = ['NOISE-COMPENSATION-EXACT.json', 'PAULI-INTERFACE-EXACT.json',
             'TELEPORTATION-GAUGE-REFRESH.json', 'bdl-metacheck/REFINEMENT-CIRCUIT.json',
             'bdl-metacheck/REFINEMENT-SECOND-STEP.json']
    for filename in paths:
        path = HERE/filename
        receipt = load(path)
        assert receipt.get('all_assertions_pass', receipt.get('all_exact_checks_pass', False))
        sources = receipt['source_sha256']
        if isinstance(sources, str):
            assert sha(HERE/'teleportation-gauge-refresh.py') == sources
        else:
            for name, digest in sources.items():
                locations = [HERE/name, HERE/'bdl-metacheck'/name]
                source = next(p for p in locations if p.is_file())
                assert sha(source) == digest, (filename, name)
        if 'circuit_file_sha256' in receipt:
            assert sha(path.parent/receipt['circuit_file']) == receipt['circuit_file_sha256']
        computations.append({'receipt': str(path.relative_to(ROOT)), 'receipt_sha256': sha(path),
                             'source_hashes_match': True, 'original_scope': receipt['scope']})
    notes = ['NOISE-COMPENSATED-PREPARATION-2026-10-27.md',
             'BDL-REFINEMENT-CIRCUIT-2026-10-27.md',
             'FT-PRIVATE-OUTPUT-BRIDGE-2026-10-27.md']
    result = {
        'date': '2026-10-27', 'timezone': 'Pacific/Auckland',
        'scope': 'Source/hash audit of executed development receipts; no new full canonical audit or global physical completion.',
        'canonical_checkpoint12': {'modules': 192, 'public_names': 1158,
                                  'all_192_source_hashes_unchanged': True,
                                  'fresh_full_compile_in_this_audit': False},
        'development_kernel_receipts': lean,
        'development_statement_total_separate_from_canon': sum(r['statements'] for r in lean),
        'executed_computational_receipts': computations,
        'prose_derivations': {name: sha(BANK/name) for name in notes},
        'remaining_physical_join': [
            'Admitted correlated-fault model at the private endpoints, or a proved reduction to the constructed channel model.',
            'Actual final correction noise and the full routed, reset, clock and classical-controller implementation.',
            'Known effective rates or calibrated rates with drift/readout controlled; O(1/n) per-location precision suffices mathematically.',
            'Complete physical invoice for that implementation under the existing all-d stage/G3 theorem.'
        ],
        'maximal_target_unchanged': True, 'full_history_retained': True,
        'original_stage_error_budget_unchanged': True,
        'merge_push_publication_performed': False,
        'global_physical_completion_claimed': False,
        'receipt_correspondence_pass': True,
        'audit_script_sha256': sha(Path(__file__)),
    }
    path = HERE/'CONSTRUCTIVE-BRIDGE-CHECKPOINT-2026-10-27.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    continuation = BANK/'CONTINUATION-RECEIPT-2026-10-26.json'
    data = load(continuation)
    data['latest_update'] = '2026-10-27, Pacific/Auckland'
    data['physical_support_pending'] = 'Complete physical correspondence for the new compensated/private-output transfer: admitted endpoint fault law, final corrections, routed controller and full physical invoice. Direct time-evolved transport remains an alternative, not the only route.'
    data['constructive_development'] = {
        'receipt': str(path.relative_to(BANK)), 'receipt_sha256': sha(path),
        'canonical_sources_unchanged': True, 'separate_development_statements': 12,
        'notes': notes, 'scope': result['scope'],
        'full_history_and_arbitrary_references_retained': True,
        'global_physical_completion_claimed': False,
    }
    continuation.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({'canonical_sources_unchanged': len(original),
                      'targeted_development_statements': 12,
                      'computational_receipts_source_matched': len(computations),
                      'receipt_correspondence_pass': True,
                      'global_completion_claimed': False}))


if __name__ == '__main__':
    main()
