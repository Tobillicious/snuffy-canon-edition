#!/usr/bin/env python3
"""Numerical complete-channel checks for the explicit local generators.
No cross-device isolation or generic local-stochastic reduction is inferred.
"""
import hashlib
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def supermatrix(channel, d):
    columns = []
    for j in range(d):
        for i in range(d):
            unit = np.zeros((d, d), dtype=complex)
            unit[i, j] = 1
            columns.append(channel(unit).reshape(-1, order='F'))
    return np.column_stack(columns)


def exponential(matrix):
    values, vectors = np.linalg.eig(matrix)
    return (vectors*np.exp(values)) @ np.linalg.inv(vectors)


def main():
    records = []
    for axis, name, gamma in [(X, 'X', 0.07), (Z, 'Z', 0.11)]:
        duration = 0.6
        p = (1-np.exp(-2*gamma*duration))/2
        for request in [0, 1]:
            H = request*np.pi*axis/(2*duration)
            generator = supermatrix(lambda r: -1j*(H@r-r@H)+gamma*(axis@r@axis-r), 2)
            actual = exponential(duration*generator)
            U = I if request == 0 else axis
            predicted = supermatrix(lambda r: (1-p)*(U@r@U)+p*(axis@U@r@U@axis), 2)
            error = float(np.max(np.abs(actual-predicted)))
            assert error < 1e-13
            assert p <= gamma*duration
            records.append({'axis': name, 'request': request,
                            'all_matrix_units_max_error': error,
                            'rate_times_duration_bound': True})

    target = np.diag([0.81, 0.19]).astype(complex)
    jumps = [np.sqrt(0.3*target[u, u])*np.eye(2, dtype=complex)[:, [u]]
             @np.eye(2, dtype=complex)[[v], :] for u in range(2) for v in range(2)]
    def dissipator(r):
        return sum((L@r@L.conj().T-(L.conj().T@L@r+r@L.conj().T@L)/2 for L in jumps))
    reset_error = float(np.max(np.abs(supermatrix(dissipator, 2)-
                                     supermatrix(lambda r: 0.3*(target*np.trace(r)-r), 2))))
    assert reset_error < 1e-14
    t = 2.0
    reset = exponential(t*supermatrix(dissipator, 2))
    exact_reset = supermatrix(lambda r: np.exp(-0.3*t)*r+(1-np.exp(-0.3*t))*target*np.trace(r), 2)
    reset_semigroup_error = float(np.max(np.abs(reset-exact_reset)))
    assert reset_semigroup_error < 1e-13

    # A single-use flag gives the same reduced replacement channel with
    # at most one jump. Check every label matrix unit, including coherences.
    # Use a convergent matrix series: the absorbing generator can have
    # repeated eigenvalues, so diagonalisation is unnecessary here.
    def exp_series(matrix):
        scale = max(0, int(np.ceil(np.log2(max(1.0, np.linalg.norm(matrix, np.inf))))))
        reduced = matrix/(2**scale)
        answer = term = np.eye(len(matrix), dtype=complex)
        for k in range(1, 60):
            term = term@reduced/k
            answer = answer+term
        for _ in range(scale):
            answer = answer@answer
        return answer

    latch_jumps = []
    for u in range(2):
        for v in range(2):
            jump = np.zeros((4, 4), dtype=complex)
            jump[2*u+1, 2*v] = np.sqrt(0.3*target[u, u])
            latch_jumps.append(jump)

    def latch_generator(r):
        return sum(L@r@L.conj().T-(L.conj().T@L@r+r@L.conj().T@L)/2
                   for L in latch_jumps)

    latch_channel = exp_series(t*supermatrix(latch_generator, 4))
    latch_error = latch_record_error = 0.0
    zero_flag = np.diag([1, 0]).astype(complex)
    one_flag = np.diag([0, 1]).astype(complex)
    for i in range(2):
        for j in range(2):
            unit = np.zeros((2, 2), dtype=complex)
            unit[i, j] = 1
            actual = (latch_channel@np.kron(unit, zero_flag).reshape(-1, order='F')).reshape((4, 4), order='F')
            predicted = (np.exp(-0.3*t)*np.kron(unit, zero_flag)
                         +(1-np.exp(-0.3*t))*np.kron(target*np.trace(unit), one_flag))
            latch_record_error = max(latch_record_error, float(np.max(np.abs(actual-predicted))))
            marginal = np.trace(actual.reshape(2, 2, 2, 2), axis1=1, axis2=3)
            expected = np.exp(-0.3*t)*unit+(1-np.exp(-0.3*t))*target*np.trace(unit)
            latch_error = max(latch_error, float(np.max(np.abs(marginal-expected))))
    assert latch_error < 1e-13 and latch_record_error < 1e-13
    assert all(np.count_nonzero(L[:, [1, 3]]) == 0 for L in latch_jumps)
    result = {'scope': 'Finite numerical generator identities only; not a physical isolation certificate or Lean theorem.',
              'commuting_feedback_cases': records,
              'reset_Lindblad_identity_error': reset_error,
              'reset_semigroup_identity_error': reset_semigroup_error,
              'single_use_latch_matrix_units': 4,
              'single_use_latch_reduced_channel_error': latch_error,
              'single_use_latch_full_flag_channel_error': latch_record_error,
              'latch_absorbing_after_one_jump': True,
              'all_assertions_pass': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'MICROSCOPIC-ENDPOINT.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
