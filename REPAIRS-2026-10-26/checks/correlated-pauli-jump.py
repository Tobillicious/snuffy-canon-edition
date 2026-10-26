#!/usr/bin/env python3
"""Actual bounded correlated Pauli-jump channel: finite generator/inverse checks."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE/'bdl-metacheck'))
import bdl
import fastbuild


def main():
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.diag([1, -1]).astype(complex)
    paul = [np.kron(X, I), np.kron(X, X), np.kron(Z, Z)]
    rates = [0.03, 0.05, 0.07]
    conjugations = [np.kron(P.conj(), P) for P in paul]
    generator = sum(g*(C-np.eye(16)) for g, C in zip(rates, conjugations))
    eigenvalues, vectors = np.linalg.eigh(generator)
    actual = (vectors*np.exp(eigenvalues)) @ vectors.conj().T
    predicted = np.eye(16, dtype=complex)
    for gamma, C in zip(rates, conjugations):
        p = (1-np.exp(-2*gamma))/2
        predicted = ((1-p)*np.eye(16)+p*C) @ predicted
    error = float(np.max(np.abs(actual-predicted)))
    assert error < 1e-13
    (x, z), n = fastbuild.build(2, 1, 0)
    def syndrome(px, pz):
        return (sum((bin(row & px).count('1') % 2) << j for j, row in enumerate(z)) |
                sum((bin(row & pz).count('1') % 2) << (j+len(z)) for j, row in enumerate(x)))
    causes = [(1 << q, 0) for q in range(n)]+[(0, 1 << q) for q in range(n)]
    causes += [(3, 0), (0, 12), (5, 10)]
    shifts = [syndrome(*p) for p in causes]
    states = {0}
    for a in shifts:
        states.update([s ^ a for s in tuple(states)])
    raw = {s: F(1, 8)**bin(s).count('1') for s in states}
    total = sum(raw.values())
    target = {s: v/total for s, v in raw.items()}
    p = F(1, 2**24)
    q = dict(target)
    for shift in reversed(shifts):
        q = {s: ((1-p)*q[s]-p*q[s ^ shift])/(1-2*p) for s in q}
    assert sum(q.values()) == 1 and min(q.values()) > 0
    recovered = dict(q)
    for shift in shifts:
        recovered = {s: (1-p)*recovered[s]+p*recovered[s ^ shift] for s in recovered}
    assert recovered == target
    result = {'scope': 'Finite joint Pauli-jump generator and exact BDL seed inverse; no arbitrary correlated-fault reduction.',
              'noncommuting_underlying_Paulis_included': True,
              'commuting_conjugation_generator_max_error': error,
              'physical_output_qubits': n, 'joint_cause_count': len(causes),
              'multiqubit_correlated_causes': 3, 'valid_joint_syndromes': len(states),
              'exact_positive_inverse': True, 'exact_Nq_equals_pi': True,
              'all_assertions_pass': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'CORRELATED-PAULI-JUMP.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
