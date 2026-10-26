#!/usr/bin/env python3
"""Exact checks of the received reset/projector preparation proposal.

These test preservation of a reference correlation and whether commuting,
disjoint completions alone give a polynomial thermal density factor.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def main():
    # R,L basis: 00,01,10,11. The syndrome ancilla is initially |1>,
    # orthogonal to the proposed projector's accepted |0> sector.
    # On this branch the supplied channel replaces L,A by a fixed default.
    bell = [[F(0) for _ in range(4)] for _ in range(4)]
    for i in (0, 3):
        for j in (0, 3):
            bell[i][j] = F(1, 2)
    reset = [[F(0) for _ in range(4)] for _ in range(4)]
    reset[0][0] = reset[2][2] = F(1, 2)
    xx = [[F(int(j == (i ^ 3))) for j in range(4)] for i in range(4)]
    before = trace(matmul(bell, xx))
    after = trace(matmul(reset, xx))
    overlap = trace(matmul(bell, reset))
    assert trace(bell) == trace(reset) == 1
    assert before == 1 and after == 0 and overlap == F(1, 4)

    # H=sum_i syndrome_i, q=exp(-beta)=1/3. On disjoint ancilla patches,
    # Pi_i rho Pi_i + Tr((I-Pi_i)rho)|0><0| resets every bit to zero.
    # Logical data can be kept separate in this second example, so the
    # density obstruction remains even after that fidelity issue is fixed.
    q = F(1, 3)
    density_examples = []
    for n in (1, 8, 32, 64):
        pi_empty = (1 / (1 + q)) ** n
        ratio = 1 / pi_empty
        assert ratio == (1 + q) ** n
        density_examples.append({'checks': n, 'parallel_depth': 1,
                                  'pi_empty': str(pi_empty),
                                  'output_mass_at_empty': '1',
                                  'necessary_warm_start_factor': str(ratio)})
    result = {'reset_branch_reference_test': {
                  'input': 'Bell state of reference R and logical L, syndrome ancilla |1>',
                  'default': '|0>_L tensor |0>_ancilla',
                  'XX_before': str(before), 'XX_after': str(after),
                  'Bell_overlap_after': str(overlap)},
              'commuting_disjoint_completion_density_test': density_examples,
              'scope': 'checks the stated implications; not a no-go theorem for other feed-forward samplers'}
    Path('PROJECTOR-COMPLETION-EXACT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'exact_checks_pass': True, 'XX_before': str(before),
                      'XX_after_reset': str(after), 'density_factor': '(4/3)^n'}))


if __name__ == '__main__':
    main()
