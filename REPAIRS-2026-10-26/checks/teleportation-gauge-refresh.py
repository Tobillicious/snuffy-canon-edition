#!/usr/bin/env python3
"""Finite channel check for the private-output gauge-refresh construction.

Checks every matrix unit of the logical-plus-input-gauge space, so it checks
the complete finite channel, including its arbitrary-reference extension.
This is floating-point validation of the displayed channel identity, not a
kernel proof or a full fault-tolerant physical implementation certificate.
"""
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = [I, X, Y, Z]
PHI = np.array([1, 0, 0, 1], dtype=complex)/np.sqrt(2)
BELL = np.outer(PHI, PHI.conj())


def partial_trace(matrix, dims, keep):
    tensor = matrix.reshape(tuple(dims)+tuple(dims))
    dimensions = list(dims)
    for index in reversed(range(len(dims))):
        if index not in keep:
            tensor = np.trace(tensor, axis1=index, axis2=index+len(dimensions))
            dimensions.pop(index)
    size = int(np.prod(dimensions))
    return tensor.reshape(size, size)


def bell_branches(rho, resource_gauge):
    # Register order S,G_S,A,B,G_A,G_B. The resource logical Bell pair is
    # independent of its joint gauge; G_A,G_B may be entangled.
    total = np.kron(np.kron(rho, BELL), resource_gauge).reshape([2]*12)
    for pauli in PAULIS:
        bell = (np.kron(I, pauli) @ PHI).reshape(2, 2)
        branch = np.einsum(
            total, [0, 1, 2, 3, 4, 5, 6, 1, 8, 9, 4, 11],
            bell.conj(), [0, 2], bell, [6, 8], [3, 5, 9, 11], optimize=True)
        yield pauli, branch.reshape(4, 4)


def max_error(left, right):
    return float(np.max(np.abs(left-right)))


def main():
    # A coherent, non-Pauli private decoder, controlled by the receiving gauge.
    # Teleportation outcomes twirl its effective channel only when the final
    # Pauli corrections are implemented covariantly, as assumed in this check.
    u0 = (3*I-4j*X)/5
    u1 = (5*I-12j*(3*X+4*Z)/5)/13
    p0, p1 = np.diag([1, 0]), np.diag([0, 1])
    unitary = np.kron(u0, p0)+np.kron(u1, p1)
    assert max_error(unitary.conj().T @ unitary, np.eye(4)) < 1e-14

    def private_decoder(state):
        return partial_trace(unitary @ state @ unitary.conj().T, [2, 2], [0])

    entangled_gauge = np.array([1, 1j, 2, -1], dtype=complex)/np.sqrt(7)
    gauges = {
        'entangled_Bell_gauge': BELL,
        'unequal_coherent_gauge': np.outer(entangled_gauge, entangled_gauge.conj()),
        'classically_correlated_gauge': np.diag([0.7, 0.0, 0.0, 0.3]).astype(complex),
    }
    records = []
    for label, gauge in gauges.items():
        tau = partial_trace(gauge, [2, 2], [1])

        def effective(rho):
            return private_decoder(np.kron(rho, tau))

        def twirled(rho):
            return sum((p @ effective(p @ rho @ p) @ p for p in PAULIS))/4

        refresh_error = decoder_error = branch_error = 0.0
        for a in range(4):
            for b in range(4):
                rho = np.zeros((4, 4), dtype=complex)
                rho[a, b] = 1
                logical = partial_trace(rho, [2, 2], [0])
                refreshed = np.zeros((4, 4), dtype=complex)
                decoded = np.zeros((2, 2), dtype=complex)
                for pauli, branch in bell_branches(rho, gauge):
                    expected_branch = np.kron(pauli @ logical @ pauli, tau)/4
                    branch_error = max(branch_error, max_error(branch, expected_branch))
                    correction = np.kron(pauli, I)
                    refreshed += correction @ branch @ correction
                    decoded += pauli @ private_decoder(branch) @ pauli
                refresh_error = max(refresh_error, max_error(refreshed, np.kron(logical, tau)))
                decoder_error = max(decoder_error, max_error(decoded, twirled(logical)))

        # Normalized Choi state checks positivity, trace preservation and
        # Pauli diagonality of the effective twirled output channel.
        choi = np.zeros((4, 4), dtype=complex)
        for a in range(2):
            for b in range(2):
                unit = np.zeros((2, 2), dtype=complex)
                unit[a, b] = 1
                choi += np.kron(unit, twirled(unit))/2
        bell_basis = np.column_stack([np.kron(I, p) @ PHI for p in PAULIS])
        bell_choi = bell_basis.conj().T @ choi @ bell_basis
        probabilities = np.real(np.diag(bell_choi))
        diagonal_error = max_error(bell_choi, np.diag(np.diag(bell_choi)))
        assert min(probabilities) >= -1e-14
        assert abs(sum(probabilities)-1) < 1e-14
        assert max(refresh_error, decoder_error, branch_error, diagonal_error) < 1e-13
        records.append({
            'resource_gauge': label, 'matrix_units_checked': 16,
            'max_branch_identity_error': branch_error,
            'max_refresh_identity_error': refresh_error,
            'max_private_decoder_identity_error': decoder_error,
            'max_Pauli_Choi_off_diagonal': diagonal_error,
            'effective_Pauli_probabilities_I_X_Y_Z': probabilities.tolist(),
            'all_assertions_pass': True,
        })

    # Control: private decoders applied to a correlated joint gauge need not
    # give independent output noise. This distinguishes the refresh argument
    # from simply assuming that private decoders always yield product noise.
    ket00 = np.array([1, 0, 0, 0], dtype=complex)
    ket11 = np.array([0, 0, 0, 1], dtype=complex)
    correlated = (np.outer(ket00, ket00)+np.outer(ket11, ket11))/2
    independent = np.eye(4)/4
    control_distance = float(np.sum(np.abs(np.linalg.eigvalsh(correlated-independent))))
    assert abs(control_distance-1) < 1e-14
    result = {
        'scope': 'Finite complete-channel validation; not the physical FT compiler, a general noise-model reduction, or a Lean receipt.',
        'cases': records,
        'unrefreshed_correlated_gauge_control_trace_distance': control_distance,
        'arbitrary_reference_basis_coverage': 'All matrix units of the full S tensor G_S input; equality extends linearly and completely.',
        'final_Pauli_correction_assumption': 'Ideal or independent Pauli-covariant correction noise. Arbitrary label-dependent faulty corrections are not certified.',
        'floating_point_tolerance': 1e-13,
        'numpy_version': np.__version__,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'all_assertions_pass': True,
    }
    (HERE/'TELEPORTATION-GAUGE-REFRESH.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
