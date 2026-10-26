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
    result = {'scope': 'Finite numerical generator identities only; not a physical isolation certificate or Lean theorem.',
              'commuting_feedback_cases': records,
              'reset_Lindblad_identity_error': reset_error,
              'reset_semigroup_identity_error': reset_semigroup_error,
              'all_assertions_pass': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'MICROSCOPIC-ENDPOINT.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
