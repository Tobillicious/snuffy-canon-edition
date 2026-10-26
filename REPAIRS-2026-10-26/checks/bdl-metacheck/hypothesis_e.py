#!/usr/bin/env python3
"""Hypothesis E on the level-1 BDL code, with the exact Theorem 4.7 map of coarse.py.

1. Every valid level-1 syndrome of weight ≤ 4 is enumerated exhaustively (validity = orthogonality
   to all dependencies of the Z-checks, tested by XOR of per-cell dependency signatures).
2. D_z := {σ : |σ| = 2, coarse(σ) = e_z}: the zero-excess (degenerate) lifts of one coarse defect.
3. Product structure (E1): every zero-excess σ with |coarse(σ)| = 2 is checked to be B₁ ⊔ B₂ with
   B_i ∈ D_{y_i}; conversely every disjoint B₁ ⊔ B₂ is checked to map to e_{y₁} + e_{y₂}.
4. Excess gap (E2): for random valid syndromes, η = σ ⊕ (nearest product lift, chosen per defect)
   and the ratio exc(σ)/|η| is recorded (an upper bound on |η|, so a lower bound on the ratio).
"""
import sys, json, random, itertools
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl, coarse as C

def main(a, b, samples):
    L = C.Level1(bdl.seed_planar(a, b))
    n2 = len(L.idx2)
    deps = bdl.left_kernel(L.D1)                      # dependencies among Z-checks (rows = 2-cells)
    sig = [0] * n2
    for t, d in enumerate(deps):
        for k in C.bits(d): sig[k] |= 1 << t
    valid = defaultdict(list)
    for w in (1, 2):
        for S in itertools.combinations(range(n2), w):
            s = 0
            for k in S: s ^= sig[k]
            if s == 0: valid[w].append(S)
    bysig = defaultdict(list)
    for S in itertools.combinations(range(n2), 2):
        bysig[sig[S[0]] ^ sig[S[1]]].append(S)
    w3 = set()
    for k in range(n2):
        for S in bysig.get(sig[k], ()):
            if k not in S: w3.add(tuple(sorted(S + (k,))))
    valid[3] = sorted(w3)
    w4 = set()
    for s, lst in bysig.items():
        for P, Q in itertools.combinations(lst, 2):
            if not set(P) & set(Q): w4.add(tuple(sorted(P + Q)))
    valid[4] = sorted(w4)
    mask = lambda S: sum(1 << k for k in S)
    D = defaultdict(list); table = defaultdict(int); zero4 = []
    for w in (1, 2, 3, 4):
        for S in valid[w]:
            sp, _ = L.coarse(mask(S))
            supp = sorted((z for z, v in sp.items() if v), key=str)
            exc = w - 2 * len(supp)
            table[(w, len(supp), exc)] += 1
            if w == 2 and len(supp) == 1: D[supp[0]].append(mask(S))
            if w == 4 and len(supp) == 2: zero4.append((mask(S), supp))
    # E1 product structure
    fail_decomp = 0
    for s, (y1, y2) in zero4:
        if not any(B1 & s == B1 and (s ^ B1) in set(D[y2]) for B1 in D[y1]): fail_decomp += 1
    fail_product = 0; tested_product = 0; overlap_skipped = 0
    zs = sorted(L.pair, key=str)
    for y1, y2 in itertools.combinations(zs, 2):
        for B1 in D[y1]:
            for B2 in D[y2]:
                if B1 & B2: overlap_skipped += 1; continue
                tested_product += 1
                sp, _ = L.coarse(B1 | B2)
                if {z for z, v in sp.items() if v} != {y1, y2}: fail_product += 1
    # E2 on random valid syndromes
    rng = random.Random(26102026); nq = len(L.idx1); worst = None; hist = defaultdict(int)
    for _ in range(samples):
        p = rng.choice([0.005, 0.01, 0.02, 0.04, 0.08])
        g = 0
        for j in range(nq):
            if rng.random() < p: g |= 1 << j
        s = L.delta(g)
        if not s: continue
        sp, _ = L.coarse(s)
        supp = [z for z, v in sp.items() if v]
        exc = C.popc(s) - 2 * len(supp)
        lift = 0
        for y in supp:
            cands = D[y] + [L.F({y: 1})]
            lift |= max(cands, key=lambda B: C.popc(B & s))
        eta = C.popc(s ^ lift)
        if eta:
            r = exc / eta; hist[round(r, 2)] += 1
            if worst is None or r < worst[0]: worst = (r, exc, eta, C.popc(s), len(supp))
        else:
            hist['exact_lift'] += 1
    m = {str(z): len(D[z]) for z in zs}
    print(json.dumps({'seed': [a, b], 'valid_counts': {w: len(valid[w]) for w in valid},
                      'table_(weight,|coarse|,exc)': {str(k): v for k, v in sorted(table.items())},
                      'degenerate_lifts_per_z': m,
                      'E1_zero_excess_weight4': len(zero4), 'E1_decomposition_failures': fail_decomp,
                      'E1_product_tested': tested_product, 'E1_product_failures': fail_product,
                      'E1_overlapping_block_pairs': overlap_skipped,
                      'E2_min_ratio': worst, 'E2_ratio_histogram_low': {str(k): v for k, v in sorted(hist.items(), key=lambda kv: (isinstance(kv[0], str), kv[0]))[:12]}}))

if __name__ == '__main__':
    main(*map(int, sys.argv[1:4]))
