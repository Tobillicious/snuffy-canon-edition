#!/usr/bin/env python3
"""A valid neutral move crossing single-defect hop regions in the finite BDL model."""
from collections import defaultdict, deque
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fastbuild


def bits(mask):
    while mask:
        bit = mask & -mask
        mask ^= bit
        yield bit.bit_length() - 1


def weight(mask):
    return bin(mask).count('1')


def main():
    if os.environ.get('PYTHONHASHSEED') != '0':
        raise SystemExit('Run with PYTHONHASHSEED=0 for reproducible indexing')
    (d0, d1), n = fastbuild.build(3, 2, 1)
    cols = defaultdict(int)
    for k, row in enumerate(d1):
        for q in bits(row):
            cols[q] |= 1 << k
    parent = list(range(len(d1)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for mask in cols.values():
        if weight(mask) == 2:
            a, b = bits(mask)
            parent[find(a)] = find(b)

    for jump, mask in sorted(cols.items()):
        if weight(mask) != 4:
            continue
        checks = list(bits(mask))
        regions = [find(k) for k in checks]
        if len(set(regions)) != 4:
            continue
        projected = {}
        for q, s in cols.items():
            v = sum(((s >> check) & 1) << i for i, check in enumerate(checks))
            if v:
                projected.setdefault(v, q)
        previous, queue, target = {0: None}, deque([0]), None
        while queue and target is None:
            value = queue.popleft()
            for v, q in projected.items():
                new = value ^ v
                if new not in previous:
                    previous[new] = (value, q)
                    queue.append(new)
                    if weight(new) == 2:
                        target = new
                        break
        if target is None:
            continue
        preimage, value = [], target
        while previous[value] is not None:
            old, q = previous[value]
            preimage.append(q)
            value = old
        before = 0
        for q in preimage:
            before ^= cols[q]
        after = before ^ mask
        after_preimage = sorted(set(preimage).symmetric_difference({jump}))
        after_check = 0
        for q in after_preimage:
            after_check ^= cols[q]
        assert after_check == after
        assert weight(before & mask) == 2
        assert weight(before) == weight(after)
        region_parity_changed = {
            region: sum(1 for k in checks if find(k) == region) % 2
            for region in regions
        }
        assert all(region_parity_changed.values())
        paths = [HERE / name for name in ['bdl.py', 'fastbuild.py', Path(__file__).name]]
        result = {
            'scope': 'finite algebraic BDL model at existing test subdivision; a counterexample to confinement in single-defect hop components, not a logical-failure or lifetime witness',
            'seed': [3, 2], 'level': 1, 'hash_seed': '0',
            'qubits': n, 'checks': len(d1),
            'jump_qubit': jump, 'jump_syndrome': checks,
            'four_distinct_one_defect_regions': regions,
            'before_preimage_qubits': preimage,
            'after_preimage_qubits': after_preimage,
            'before_syndrome': list(bits(before)),
            'after_syndrome': list(bits(after)),
            'before_weight': weight(before), 'after_weight': weight(after),
            'energy_change': 0,
            'both_syndromes_valid_by_explicit_preimage': True,
            'region_parity_changed_at_all_four_regions': True,
            'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        }
        HERE.joinpath('NEUTRAL-REGION-WITNESS.json').write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps(result), flush=True)
        return
    raise SystemExit('No witness found')


if __name__ == '__main__':
    main()
