#!/usr/bin/env python3
"""Hypothesis E, part E1 (pātai 2⁹, step 2): is the lifted coarse defect F(e_z) locally unique
among weight-nonincreasing moves?

Level 1 is R_X(level 0) (bdl.RX). Its 2-cells include the pairs (z,0),(z,1) for every Z-check z of
level 0, and F(e_z) = (z,0)+(z,1) (BDL Lemma 4.14). For each z, this enumerates every connected set
f of level-1 qubits of size ≤ W that touches the pair (qubits are adjacent when they share a Z-check;
the two pair bits count as one hub), and records min |F(e_z)+δf| over δf ≠ 0 and the number of
moves with |F(e_z)+δf| ≤ 2. Components of f not touching the pair only add weight, so connected sets
touching the pair are exhaustive for moves that do not increase the weight, up to size W.
"""
import sys, json
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl

def RX_idx(T):
    """bdl.RX, also returning the 2-cell index (needed to locate the pairs (z,t))."""
    idx0, idx1, idx2 = {}, {}, {}
    def ix(d, key):
        if key not in d: d[key] = len(d)
        return d[key]
    Yx = {x: bdl.build_Yx(T, x) for x in T.VX}
    Yq = {q: bdl.build_Yq(T, q) for q in T.VQ}
    for x, (V, E, Fc, Ebd, Fbd) in Yx.items():
        for v in V: ix(idx0, ('x', x, v))
        for e in E: ix(idx1, ('x', x, e))
        for f in Fc: ix(idx2, ('x', x, f))
    for q, (V, E, Ebd) in Yq.items():
        for v in V: ix(idx1, ('q', q, v))
        for e in E: ix(idx2, ('q', q, e))
    for z in T.VZ:
        for t in (0, 1): ix(idx2, ('z', z, t))
    D0, D1, dims = bdl.RX(T)          # same insertion order, so the indices agree
    return D0, D1, dims, idx2

def main(a, b, W):
    T0 = bdl.seed_planar(a, b)
    D0, D1, (n0, n1, n2), idx2 = RX_idx(T0)
    assert bdl.check_complex(D0, D1)
    col = defaultdict(int)            # qubit -> Z-check bits (its δ)
    for k, r in enumerate(D1):
        bb = r
        while bb:
            j = bb.bit_length() - 1; bb ^= 1 << j; col[j] |= 1 << k
    byz = defaultdict(set)
    for j, c in col.items():
        bb = c
        while bb:
            k = bb.bit_length() - 1; bb ^= 1 << k; byz[k].add(j)
    colw = sorted({bin(c).count('1') for c in col.values()})
    out = []
    for z in T0.VZ:
        p0, p1 = idx2[('z', z, 0)], idx2[('z', z, 1)]
        P = (1 << p0) | (1 << p1)
        hub = byz[p0] | byz[p1]
        def nbrs(j):
            s = set(); c = col[j]
            while c:
                k = c.bit_length() - 1; c ^= 1 << k
                s |= byz[k]
            if j in hub: s |= hub
            return s - {j}
        seen = set(); best = None; nle2 = 0; examples = []
        stack = [frozenset([j]) for j in hub]
        while stack:
            S = stack.pop()
            if S in seen: continue
            seen.add(S)
            d = 0
            for j in S: d ^= col[j]
            if d:
                w = bin(P ^ d).count('1')
                best = w if best is None else min(best, w)
                if w <= 2:
                    nle2 += 1
                    if len(examples) < 3: examples.append({'f': sorted(S), 'weight': w})
            if len(S) < W:
                ext = set().union(*(nbrs(j) for j in S)) - S
                for u in ext: stack.append(S | {u})
        out.append({'z': str(z), 'min_weight_after_move': best, 'moves_weight_le_2': nle2,
                    'sets_enumerated': len(seen), 'examples': examples})
    summ = {'seed': [a, b], 'W': W, 'level1_qubits': n1, 'level1_zchecks': n2,
            'qubit_delta_weights': colw,
            'z_with_nonincreasing_move': sum(1 for r in out if r['moves_weight_le_2']),
            'z_total': len(out), 'min_over_z': min(r['min_weight_after_move'] for r in out)}
    for r in out: print(json.dumps(r))
    print(json.dumps({'summary': summ}))

if __name__ == '__main__':
    main(*map(int, sys.argv[1:4]))
