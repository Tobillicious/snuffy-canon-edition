#!/usr/bin/env python3
"""Code distance for accounts 1-4 from the measured surface-code scaling of [S6].

[S6]: distance-7 logical error per cycle eps7 = 0.143 % and suppression factor
Lambda = 2.14 +/- 0.02 per distance step of two (eps_{d+2} = eps_d / Lambda).
Target per cycle per logical qubit (section 22.5.2): delta = 4e-8 shared over 9 logical
qubits and N = 1e9 s / 1.1 us cycles. Extrapolation assumes the measured Lambda
continues to hold (the correlated-burst accounts are treated separately, §22.3).
"""
from fractions import Fraction
import math
N = 1e9 / 1.1e-6
target = 4e-8 / (9 * N)
eps7 = 1.43e-3
rows = []
for lam in (2.12, 2.14, 2.16):
    d = 7
    while eps7 / lam ** ((d - 7) / 2) > target:
        d += 2
    rows.append((lam, d, (2 * d - 1) ** 2, 9 * (2 * d - 1) ** 2, eps7 / lam ** ((d - 7) / 2)))
print(f"cycles N = {N:.4e}; per-cycle target per logical qubit = {target:.3e}")
for lam, d, q1, q9, e in rows:
    print(f"Lambda = {lam:.2f}: d = {d}, eps_d = {e:.2e}, physical qubits per logical = {q1}, for 9 logical = {q9}")
