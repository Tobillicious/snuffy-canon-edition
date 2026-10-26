#!/usr/bin/env python3
"""Range of the E1 product failures: on a larger seed, D_z is computed exhaustively over valid
weight-2 syndromes, and every disjoint pair B₁ ∈ D_{y₁}, B₂ ∈ D_{y₂} is tested for
coarse(B₁ ⊔ B₂) = e_{y₁} + e_{y₂}, tagged by the level-0 distance between y₁ and y₂ (Z-checks
adjacent when they share a level-0 qubit)."""
import sys, json, itertools
from collections import defaultdict, deque
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl, coarse as C

def main(a, b):
    T = bdl.seed_planar(a, b)
    L = C.Level1(T)
    n2 = len(L.idx2)
    deps = bdl.left_kernel(L.D1)
    sig = [0] * n2
    for t, d in enumerate(deps):
        for k in C.bits(d): sig[k] |= 1 << t
    D = defaultdict(list)
    for S in itertools.combinations(range(n2), 2):
        if sig[S[0]] ^ sig[S[1]]: continue
        s = (1 << S[0]) | (1 << S[1])
        sp, _ = L.coarse(s)
        supp = [z for z, v in sp.items() if v]
        if len(supp) == 1: D[supp[0]].append(s)
    zadj = defaultdict(set)
    for q in T.VQ:
        zs = list(T.adjQZ[q])
        for u in zs:
            for w in zs:
                if u != w: zadj[u].add(w)
    def dist(u):
        d = {u: 0}; Q = deque([u])
        while Q:
            v = Q.popleft()
            for w in zadj[v]:
                if w not in d: d[w] = d[v] + 1; Q.append(w)
        return d
    res = defaultdict(lambda: [0, 0])
    zs = sorted(L.pair, key=str)
    for y1, y2 in itertools.combinations(zs, 2):
        dd = dist(y1).get(y2, 99)
        for B1 in D[y1]:
            for B2 in D[y2]:
                if B1 & B2: continue
                sp, _ = L.coarse(B1 | B2)
                ok = {z for z, v in sp.items() if v} == {y1, y2}
                res[dd][0] += 1; res[dd][1] += 0 if ok else 1
    print(json.dumps({'seed': [a, b], 'level1_2cells': n2,
                      'block_sizes': sorted({len(v) for v in D.values()}),
                      'product_by_distance_[tested,failures]': {str(k): v for k, v in sorted(res.items())}}))

if __name__ == '__main__':
    main(*map(int, sys.argv[1:3]))
