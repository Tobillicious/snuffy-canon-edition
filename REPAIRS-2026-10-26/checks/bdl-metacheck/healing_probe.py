#!/usr/bin/env python3
"""Numerical probe for statement (R) of PATAI-NOISY-PREPARATION-2026-10-26.md (not a proof).

On the constructed BDL code at a given level, start the X-error configuration at a sparse random
fault layer (density p) and run single-site heat-bath (Glauber) dynamics at inverse temperature beta
with energy = number of violated Z-checks. Report the syndrome weight over time, the time at which
it first returns to zero, and whether the residual error is then an X-stabilizer (healed) or
a nontrivial logical (failure).
"""
import sys, json, math, random
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl

def build(a, b, level):
    T = bdl.seed_planar(a, b)
    for lev in range(level):
        if lev % 2 == 0:
            D0n, D1n, (n0, n1n, n2) = bdl.RX(T)
        else:
            S = bdl.swap(T); D0s, D1s, (n0s, n1s, n2s) = bdl.RX(S); D0n, D1n, n1n = D1s, D0s, n1s
        T, _ = bdl.to_TSC(D0n, D1n, n1n)
    return bdl.code_of(T), len(T.VQ)

def main(a, b, level, p, beta, sweeps, trials):
    (D0, D1), n = build(a, b, level)
    checks_of = [[] for _ in range(n)]
    for k, r in enumerate(D1):
        x = r
        while x:
            j = x.bit_length() - 1; x ^= 1 << j; checks_of[j].append(k)
    stab = bdl.rank_and_basis(D0)
    rng = random.Random(1)
    out = []
    for t in range(trials):
        err = [0] * n
        for j in range(n):
            if rng.random() < p: err[j] = 1
        syn = [0] * len(D1)
        for j in range(n):
            if err[j]:
                for k in checks_of[j]: syn[k] ^= 1
        w0 = sum(syn); w = w0; first_zero = 0 if w == 0 else None; trace = [w0]
        for s in range(sweeps):
            for _ in range(n):
                j = rng.randrange(n)
                dE = sum(1 - 2 * syn[k] for k in checks_of[j])
                if rng.random() < 1.0 / (1.0 + math.exp(beta * dE)):
                    err[j] ^= 1
                    for k in checks_of[j]: syn[k] ^= 1
                    w += dE
            trace.append(w)
            if w == 0 and first_zero is None:
                first_zero = s + 1
        e = sum(1 << j for j in range(n) if err[j])
        logical = None
        if w == 0:
            logical = bdl.reduce(e, stab) != 0
        out.append({'trial': t, 'initial_syndrome': w0,
                    'final_syndrome': w, 'first_zero_sweep': first_zero, 'logical_error_at_end': logical,
                    'trace_every_10': trace[::10]})
    print(json.dumps({'seed': [a, b], 'level': level, 'qubits': n, 'p': p, 'beta': beta,
                      'sweeps': sweeps, 'results': out}))

if __name__ == '__main__':
    a, b, level = map(int, sys.argv[1:4]); p, beta = map(float, sys.argv[4:6]); sweeps, trials = map(int, sys.argv[6:8])
    main(a, b, level, p, beta, sweeps, trials)
