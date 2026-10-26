#!/usr/bin/env python3
"""Exact finite checks of the sampler estimates used in the received proposals.

These calculations distinguish stationarity, TV convergence and pointwise
domination. They do not assert an all-level BDL mixing theorem.
"""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path

import bdl
import coarse as C


def main():
    states = list(itertools.product(range(2), repeat=2))
    pi = {(x, y): F(3 if x == y else 1, 8) for x, y in states}
    cond = lambda x, y: F(3 if x == y else 1, 4)
    # One systematic sweep: update x and then y, starting from (0,0).
    mu = {(x, y): cond(x, 0) * cond(y, x) for x, y in states}
    ratios = {s: mu[s] / pi[s] for s in states}
    assert sum(mu.values()) == sum(pi.values()) == 1
    assert max(ratios.values()) == F(3, 2)
    influence = abs(cond(0, 0) - cond(0, 1))
    assert influence == F(1, 2)
    # Independent dimers multiply both laws and the pointwise ratios.
    dimers = [{'sites': 2 * m, 'max_density_after_one_sweep': str(F(3, 2) ** m)}
              for m in (1, 8, 32, 64)]

    # A polynomially small TV error can put too much mass on an exponentially
    # rare state, even for H=0 and a product target.
    tv_examples = []
    for n in (8, 16, 32, 64):
        eps = F(1, n * n)
        pmin = F(1, 2 ** n)
        tv = eps * (1 - pmin)
        ratio = 1 - eps + eps / pmin
        assert tv <= eps
        tv_examples.append({'bits': n, 'TV': str(tv), 'TV_ceiling': str(eps),
                            'max_density': str(ratio)})

    # Globally valid syndromes can be updated by local qubit-error cochains.
    # For the one-qubit heat bath, this computes a lower bound on each
    # influence row using only two explicit outside configurations.
    L = C.Level1(bdl.seed_planar(3, 2))
    q = F(1, 3)  # beta = log(3), H(error) = |delta(error)|
    probability = lambda delta_energy: q ** delta_energy / (1 + q ** delta_energy)
    rows = []
    for i, col_i in L.col.items():
        degree = C.popc(col_i)
        changes = []
        for j, col_j in L.col.items():
            if i == j:
                continue
            shared = C.popc(col_i & col_j)
            if shared:
                change = abs(probability(degree - 2 * shared) - probability(degree))
                changes.append((j, shared, change))
        rows.append((sum((v for _, _, v in changes), F(0)), i, degree, changes))
    lower, i, degree, changes = max(rows, key=lambda r: r[0])
    assert lower > 1
    label = {j: repr(cell) for cell, j in L.idx1.items()}[i]
    result = {
        'one_sweep_dimer': {'Dobrushin_row_sum': str(influence),
                            'one_pair_max_density': str(max(ratios.values())),
                            'independent_products': dimers},
        'TV_does_not_imply_pointwise_without_floor': tv_examples,
        'BDL_one_qubit_error_cochain_kernel': {
            'seed': [3, 2], 'beta': 'log(3)', 'selected_qubit': label,
            'incident_checks': degree, 'influence_row_lower_bound': str(lower),
            'changed_outside_qubits': len(changes),
            'scope': 'this explicit one-qubit kernel; a different block cover needs its own certificate'}}
    Path('SAMPLER-BOUNDS-EXACT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'exact_checks_pass': True, 'dimer_row_sum': str(influence),
                      'BDL_one_qubit_row_lower_bound': str(lower)}))


if __name__ == '__main__':
    main()
