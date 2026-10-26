#!/usr/bin/env python3
"""Exact anisotropic output-channel compensation and rate-error bound.

Uses the actual BDL seed matrices in both CSS sectors jointly. No physical
FT compiler or long-time transport is inferred from these finite checks.
"""
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE/'bdl-metacheck'))
import bdl
import fastbuild


def weight(value):
    return bin(value).count('1')


def span(generators):
    states = {0}
    for generator in generators:
        states.update([s ^ generator for s in tuple(states)])
    return sorted(states)


def inverse_weights(q):
    # Characters ordered I,X,Z,Y, matching syndrome shifts 0,a,b,a+b.
    characters = [[1, 1, 1, 1], [1, 1, -1, -1],
                  [1, -1, 1, -1], [1, -1, -1, 1]]
    eigenvalues = [sum(sign*value for sign, value in zip(row, q))
                   for row in characters]
    assert all(value != 0 for value in eigenvalues)
    inverse = [sum(F(characters[j][i], 4)/eigenvalues[j] for j in range(4))
               for i in range(4)]
    assert sum(inverse) == 1
    assert [sum(q[i]*inverse[i ^ k] for i in range(4)) for k in range(4)] == [1, 0, 0, 0]
    return inverse


def apply_channel(law, a, b, coefficients):
    shifts = [0, a, b, a ^ b]
    return {s: sum(c*law[s ^ shift] for c, shift in zip(coefficients, shifts))
            for s in law}


def run_case(seed):
    (x, z), n = fastbuild.build(*seed, 0)
    columns = [(sum(((row >> q) & 1) << k for k, row in enumerate(z)),
                sum(((row >> q) & 1) << (k+len(z)) for k, row in enumerate(x)))
               for q in range(n)]
    states = span([column for pair in columns for column in pair])
    fugacity = F(1, 8)
    raw = {s: fugacity**weight(s) for s in states}
    partition = sum(raw.values())
    target = {s: value/partition for s, value in raw.items()}
    channels = []
    for q in range(n):
        scale = F(1+q % 3, 2**24)
        channels.append([1-6*scale, scale, 2*scale, 3*scale])
    compensated = dict(target)
    for (a, b), channel in reversed(list(zip(columns, channels))):
        compensated = apply_channel(compensated, a, b, inverse_weights(channel))
    assert sum(compensated.values()) == 1
    assert min(compensated.values()) > 0
    recovered = dict(compensated)
    for (a, b), channel in zip(columns, channels):
        recovered = apply_channel(recovered, a, b, channel)
    assert recovered == target

    # Rate perturbations have both signs. The exact weighted sup-norm bound
    # controls their whole-system effect without using pi_min.
    varied = dict(compensated)
    bound = F(1)
    for j, ((a, b), nominal) in enumerate(zip(columns, channels)):
        delta = F((-1)**j, n*2**30)
        actual = [nominal[0]-delta, nominal[1]+delta, nominal[2], nominal[3]]
        assert min(actual) >= 0 and sum(actual) == 1
        w = max(weight(a), weight(b), weight(a ^ b))
        translation_bound = fugacity**(-w)
        nominal_error = (1-nominal[0])*(1+translation_bound)
        assert nominal_error < 1
        difference_bound = sum(abs(v-u) for u, v in zip(nominal, actual))*translation_bound
        bound *= 1+difference_bound/(1-nominal_error)
        varied = apply_channel(varied, a, b, actual)
    ratio = max(varied[s]/target[s] for s in states)
    assert all(value >= 0 for value in varied.values())
    assert sum(varied.values()) == 1
    assert ratio <= bound
    return {
        'seed': list(seed), 'physical_qubits': n, 'valid_joint_syndromes': len(states),
        'unequal_X_Z_Y_rates': True, 'spatially_varying_channels': True,
        'exact_inverse_nonnegative': True, 'exact_inverse_mass_one': True,
        'exact_noise_inverse_identity': True,
        'perturbed_output_mass_one': True,
        'pointwise_rate_perturbation_bound_verified_exactly': True,
        'max_perturbed_density_ratio_decimal': float(ratio),
        'proved_finite_product_bound_decimal': float(bound),
        'all_assertions_pass': True,
    }


def joint_occupation_control():
    # A global even-parity check is kept exactly. This finite control uses
    # a conservative complete augmented graph, not an observed all-level
    # BDL graph degree. K_0=1 because its history consists of the fine bits.
    checks = 8
    columns = [((1 << j) | (1 << ((j+1) % checks)), 0) for j in range(checks)]
    states = span([a for a, _ in columns])
    z, scale = F(1, 2**128), F(1, 2**1024)
    channel = [1-6*scale, scale, 2*scale, 3*scale]
    raw = {s: z**weight(s) for s in states}
    partition = sum(raw.values())
    current = {s: value/partition for s, value in raw.items()}
    for a, b in reversed(columns):
        current = apply_channel(current, a, b, inverse_weights(channel))
    augmented_vertices = checks+6*len(columns)
    B = augmented_vertices**2
    inverse_ratio_bound = 2*(6*scale)/(1-2*(6*scale))
    forward_ratio_bound = 6*scale/(1-6*scale)
    b = max(z, inverse_ratio_bound*z**(-2), forward_ratio_bound*z**(-2))
    R = 6*B*b  # e<3, so this exceeds 2 B e b.
    assert R < 1
    tests = 0
    for prefix in range(len(columns)+1):
        assert min(current.values()) >= 0 and sum(current.values()) == 1
        occupation = [current.get(s, F(0)) for s in range(1 << checks)]
        for j in range(checks):
            for mask in range(1 << checks):
                if not mask & (1 << j):
                    occupation[mask] += occupation[mask | (1 << j)]
        for marks, probability in enumerate(occupation):
            assert probability <= R**weight(marks)
            tests += 1
        if prefix < len(columns):
            current = apply_channel(current, *columns[prefix], channel)
    assert current == {s: value/partition for s, value in raw.items()}
    return {
        'scope': 'Exact eight-check global-parity control of the covering bound; not an all-level BDL verification.',
        'valid_syndromes': len(states), 'partial_output_layers': len(columns)+1,
        'joint_subset_occupation_checks': tests,
        'conservative_complete_augmented_graph_vertices': augmented_vertices,
        'occupation_parameter_upper_bound_decimal': float(R),
        'all_assertions_pass': True,
    }


def main():
    assert os.environ.get('PYTHONHASHSEED') == '0', 'Use PYTHONHASHSEED=0'
    fastbuild.patch_star_scan()
    records = [run_case(seed) for seed in [(2, 1), (3, 2)]]
    result = {
        'scope': 'Exact finite algebra and syndrome-law tests, not a physical FT application or lifetime certificate.',
        'cases': records, 'joint_occupation_control': joint_occupation_control(),
        'all_assertions_pass': True,
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in [Path(__file__), HERE/'bdl-metacheck/bdl.py',
                                    HERE/'bdl-metacheck/fastbuild.py']},
    }
    (HERE/'PAULI-INTERFACE-EXACT.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
