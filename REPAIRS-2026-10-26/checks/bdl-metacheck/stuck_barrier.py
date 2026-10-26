#!/usr/bin/env python3
"""After the healing probe's dynamics, classify the residual excitations (not a proof).

Runs healing_probe-style heat-bath dynamics at beta from a fault layer of density p, then, for the
final configuration, asks for each connected residual syndrome cluster (Z-checks adjacent when they
share a qubit): is there a single flip that lowers the energy (not stuck), and otherwise how many zero-energy single flips
move it, and what is the smallest energy barrier of a path of up to K flips, within the cluster's qubit neighbourhood, that
annihilates the cluster's syndrome entirely?
"""
import sys, json, math, random, itertools
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl, healing_probe as hp

def main(a, b, level, p, beta, sweeps, K, seed):
    (D0, D1), n = hp.build(a, b, level)
    m = len(D1)
    checks_of = [[] for _ in range(n)]
    qubits_of = [[] for _ in range(m)]
    for k, r in enumerate(D1):
        x = r
        while x:
            j = x.bit_length() - 1; x ^= 1 << j; checks_of[j].append(k); qubits_of[k].append(j)
    rng = random.Random(seed)
    syn = [0] * m
    for j in range(n):
        if rng.random() < p:
            for k in checks_of[j]: syn[k] ^= 1
    for _ in range(sweeps * n):
        j = rng.randrange(n)
        dE = sum(1 - 2 * syn[k] for k in checks_of[j])
        if rng.random() < 1.0 / (1.0 + math.exp(beta * dE)):
            for k in checks_of[j]: syn[k] ^= 1
    on = {k for k in range(m) if syn[k]}
    seen, clusters = set(), []
    for k in on:
        if k in seen: continue
        comp, st = {k}, [k]; seen.add(k)
        while st:
            u = st.pop()
            for j in qubits_of[u]:
                for v in checks_of[j]:
                    if v in on and v not in seen: seen.add(v); comp.add(v); st.append(v)
        clusters.append(comp)
    out = []
    for comp in clusters:
        qs = sorted({j for k in comp for j in qubits_of[k]})
        nb = sorted(set(qs) | {j2 for j in qs for k in checks_of[j] for j2 in qubits_of[k]})
        def energy_delta(flips):
            d = {}
            for j in flips:
                for k in checks_of[j]: d[k] = d.get(k, 0) ^ 1
            return sum((1 - 2 * syn[k]) for k, v in d.items() if v)
        single_down = any(energy_delta([j]) < 0 for j in nb)
        neutral = sum(1 for j in nb if energy_delta([j]) == 0)
        best = None
        if not single_down:
            for r in range(2, K + 1):
                for S in itertools.combinations(nb, r):
                    if energy_delta(S) != -len(comp): continue
                    # check it annihilates exactly the cluster: all flipped checks are in comp
                    d = {}
                    for j in S:
                        for k in checks_of[j]: d[k] = d.get(k, 0) ^ 1
                    if {k for k, v in d.items() if v} != comp: continue
                    for order in itertools.permutations(S):
                        cur, peak = 0, 0
                        for i in range(1, len(order) + 1):
                            cur = energy_delta(order[:i]); peak = max(peak, cur)
                        best = peak if best is None else min(best, peak)
                if best is not None: break
        out.append({'size': len(comp), 'single_flip_downhill': single_down, 'zero_energy_single_flips': neutral, 'annihilation_barrier_upto_K': best})
    print(json.dumps({'level': level, 'qubits': n, 'p': p, 'beta': beta, 'sweeps': sweeps, 'K': K,
                      'residual_excitations': len(on), 'clusters': out}))

if __name__ == '__main__':
    a, b, level = map(int, sys.argv[1:4]); p, beta = map(float, sys.argv[4:6]); sweeps, K, seed = map(int, sys.argv[6:9])
    main(a, b, level, p, beta, sweeps, K, seed)
