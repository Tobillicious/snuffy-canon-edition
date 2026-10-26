#!/usr/bin/env python3
"""Exact matrix checks for the proposed norm, gap and killing steps."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def main():
    x, z = [[0, 1], [1, 0]], [[1, 0], [0, -1]]
    xzx = mul(mul(x, z), x)
    derivative = [[xzx[i][j] - z[i][j] for j in range(2)] for i in range(2)]
    assert derivative == [[-2, 0], [0, 2]]

    hopping = [[-1, 1], [1, -1]]
    assert [sum(row) for row in hopping] == [0, 0]
    assert hopping[0][0] * hopping[1][1] - hopping[0][1] * hopping[1][0] == 0

    e = F(1, 16)
    q0, qe = [[-1, 1], [0, -1]], [[-1, 1], [e, -1 - e]]
    assert all(sum(row) <= 0 for row in q0 + qe)
    assert all(q[i][j] >= 0 for q in [q0, qe] for i in range(2) for j in range(2) if i != j)
    trace = qe[0][0] + qe[1][1]
    determinant = qe[0][0] * qe[1][1] - qe[0][1] * qe[1][0]
    assert trace == -F(33, 16) and determinant == 1
    assert trace * trace - 4 * determinant == F(65, 256)
    assert 8 * 8 < 65
    assert 2 * e * e < F(1, 8) ** 2
    assert F(25, 32) < 1 - F(1, 8)

    qk = [[-1, 1], [1, -2]]
    assert qk[0][0] * qk[1][1] - qk[0][1] * qk[1][0] == 1
    poly = lambda r: r * r - 3 * r + 1
    assert poly(F(1, 4)) > 0 and poly(F(1, 2)) < 0
    assert poly(3) != 0
    killing = [[0, 0], [0, 1]]
    assert [[qk[i][j] + killing[i][j] for j in range(2)] for i in range(2)] == hopping

    source = Path(__file__)
    result = {
        'scope': 'exact finite counterchecks of proposed analytical steps; not a UPT no-go or a BDL holding certificate',
        'dissipator_factor_two_required': True,
        'unkilled_stationary_zero_mode': True,
        'nonnormal_gap_perturbation_counterexample': True,
        'boundary_killing_is_not_uniform_spectral_shift': True,
        'full_generator_reconstructed_as_killed_plus_exit_flux': True,
        'all_assertions_pass': True,
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    }
    source.with_name('TRANSIENT-RESOLVENT-CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
