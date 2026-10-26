#!/usr/bin/env python3
"""Check a Dec counterexample with an explicit qubit-error preimage.

Also test the exact F-translation identity on this witness.  The validity
check here solves delta(error) = syndrome, independently of the left-kernel
enumeration in transport.py.  Run with PYTHONHASHSEED=0.
"""
import itertools
import json
from pathlib import Path

import bdl
import coarse as C


def preimage(L, syndrome):
    basis = {}
    for j, column in L.col.items():
        value, error = column, 1 << j
        while value:
            k = value.bit_length() - 1
            if k not in basis:
                basis[k] = value, error
                break
            row, err = basis[k]
            value ^= row
            error ^= err
    value, error = syndrome, 0
    while value:
        row, err = basis[value.bit_length() - 1]
        value ^= row
        error ^= err
    assert L.delta(error) == syndrome
    return error


def main():
    record = json.loads(Path('TRANSPORT-3x2-GLOBAL.json').read_text())
    example = record['examples']['dec'][0]
    L = C.Level1(bdl.seed_planar(3, 2))
    byindex = {i: repr(cell) for cell, i in L.idx2.items()}
    indices = example['syndrome']['indices']
    assert sorted(byindex[i] for i in indices) == example['syndrome']['cells']
    sigma = sum(1 << i for i in indices)

    def supp(s):
        return sorted(repr(z) for z, on in L.coarse(s)[0].items() if on)

    assert supp(sigma) == example['pair']
    error = preimage(L, sigma)
    subsets = []
    for pair in itertools.combinations(indices, 2):
        s = sum(1 << i for i in pair)
        try:
            e = preimage(L, s)
        except KeyError:
            subsets.append({'indices': list(pair), 'valid': False})
            continue
        coarse_support = supp(s)
        assert coarse_support not in [[v] for v in example['pair']]
        subsets.append({'indices': list(pair), 'valid': True,
                        'coarse_support': coarse_support})
    translations = []
    for z in sorted(L.pair, key=repr):
        lift = L.F({z: 1})
        expected = set(example['pair']) ^ {repr(z)}
        assert set(supp(sigma ^ lift)) == expected
        translations.append({'toggle': repr(z), 'coarse_support': supp(sigma ^ lift),
                             'fine_weight': C.popc(sigma ^ lift)})
    qubits = {i: repr(cell) for cell, i in L.idx1.items()}
    result = {'scope': 'one explicit globally valid Dec counterexample',
              'syndrome': example['syndrome'], 'coarse_support': supp(sigma),
              'fine_weight': C.popc(sigma),
              'qubit_error_preimage': {'indices': sorted(C.bits(error)),
                                        'cells': sorted(qubits[i] for i in C.bits(error))},
              'all_two_cell_subsets': subsets, 'F_translations': translations}
    Path('TRANSPORT-WITNESS-CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'preimage_verified': True, 'subsets_checked': len(subsets),
                      'Dec_counterexample_verified': True, 'F_translations_checked': len(translations)}))


if __name__ == '__main__':
    main()
