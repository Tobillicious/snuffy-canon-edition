#!/usr/bin/env python3
"""The coarse-graining map of BDL Theorem 4.7 (arXiv:2605.10943 §4.3) for one R_X step, implemented
exactly as Lemmas 4.8, 4.12 and 4.14 describe, with subdivision parameter m = 1 (ℓ = 3). With m = 1
each piece Y_{x,j} (j = a square s at x) has four one-cell regions: ('L',s,0), ('L',s,1) and the two
side cells ('C',(q,z)), ('C',(z,q')).

Fixed deterministic choices (the paper allows any): α is solved on each component of the link graph
from its least vertex with value 0; the layer is 0 on ties; a (1,1,0,0) piece is paired through its
first side cell; the all-ones flip of Lemma 4.12 is not applied on ties.

Every conclusion the paper proves is asserted at run time: δ_x f_x = σ_x and Lemma 4.8(2); δ_q f_q =
σ_q and Lemma 4.12(2); σ₂ ∈ C_Z² with equal pair values; |σ₂| ≤ |σ₁| ≤ |σ|; σ = δf + F(σ′).

Usage: coarse.py a b W samples  (seed planar(a,b); local tests up to size W; random tests)
"""
import sys, json, random
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl

def popc(v): return bin(v).count('1')

def bits(v):
    while v:
        j = v.bit_length() - 1; v ^= 1 << j; yield j

class Level1:
    def __init__(self, T):
        self.T = T
        idx0, idx1, idx2 = {}, {}, {}
        def ix(d, key):
            if key not in d: d[key] = len(d)
            return d[key]
        self.Yx = {x: bdl.build_Yx(T, x) for x in T.VX}
        self.Yq = {q: bdl.build_Yq(T, q) for q in T.VQ}
        for x, (V, E, Fc, Ebd, Fbd) in self.Yx.items():
            for v in V: ix(idx0, ('x', x, v))
            for e in E: ix(idx1, ('x', x, e))
            for f in Fc: ix(idx2, ('x', x, f))
        for q, (V, E, Ebd) in self.Yq.items():
            for v in V: ix(idx1, ('q', q, v))
            for e in E: ix(idx2, ('q', q, e))
        for z in T.VZ:
            for t in (0, 1): ix(idx2, ('z', z, t))
        self.idx1, self.idx2 = idx1, idx2
        self.D0, self.D1, _ = bdl.RX(T)
        assert bdl.check_complex(self.D0, self.D1)
        self.col = defaultdict(int)              # qubit -> its δ¹ over 2-cells
        for k, r in enumerate(self.D1):
            for j in bits(r): self.col[j] |= 1 << k
        self.pair = {z: (idx2[('z', z, 0)], idx2[('z', z, 1)]) for z in T.VZ}
        self.zmask = 0
        for a, b in self.pair.values(): self.zmask |= (1 << a) | (1 << b)
        # the local coboundary δ_x restricted to Y_x 2-cells, and δ_q restricted to Y_q 2-cells
        self.xmask = {x: sum(1 << idx2[('x', x, f)] for f in self.Yx[x][2]) for x in T.VX}
        self.qmask = {q: sum(1 << idx2[('q', q, e)] for e in self.Yq[q][1]) for q in T.VQ}
        # level-0 coboundary (Z-check rows over level-0 qubits) for validity of σ′
        self.D0_0, self.D1_0 = bdl.code_of(T)

    def delta(self, f):
        d = 0
        for j in bits(f): d ^= self.col[j]
        return d

    def F(self, sp):
        """F(σ′): each coarse Z-check z lifts to the pair (z,0),(z,1)."""
        v = 0
        for z, on in sp.items():
            if on:
                a, b = self.pair[z]; v |= (1 << a) | (1 << b)
        return v

    def clean_x(self, x, sigma):
        T, i1, i2 = self.T, self.idx1, self.idx2
        val = lambda cell: (sigma >> i2[('x', x, cell)]) & 1
        sq = [s for s in T.squares if s[0] == x]
        side = {}
        for s in sq:
            _, q, z, q2 = s
            side[s] = (frozenset((q, z)), frozenset((z, q2)))
        # link graph G: vertices = q adjacent to x (edges (x,q)), edges = squares
        par = {s: (val(('L', s, 0)) + val(('L', s, 1)) + val(('C', side[s][0])) + val(('C', side[s][1]))) & 1
               for s in sq}
        adj = defaultdict(list)
        for s in sq:
            _, q, z, q2 = s
            adj[q].append((q2, s)); adj[q2].append((q, s))
        alpha = {}
        for root in sorted(adj, key=str):
            if root in alpha: continue
            alpha[root] = 0; stack = [root]
            while stack:
                u = stack.pop()
                for w, s in adj[u]:
                    need = alpha[u] ^ par[s]
                    if w in alpha:
                        assert alpha[w] == need, 'σ̃ not in Im δ_G'
                    else:
                        alpha[w] = need; stack.append(w)
        s1 = sum(val(('L', s, 1)) for s in sq); s0 = sum(val(('L', s, 0)) for s in sq)
        layer = 0 if s1 <= s0 else 1
        f = 0
        for q, a in alpha.items():
            if a: f ^= 1 << i1[('x', x, ('L', frozenset((x, q)), layer))]
        tau = (sigma & self.xmask[x]) ^ (self.delta(f) & self.xmask[x])
        tv = lambda cell: (tau >> i2[('x', x, cell)]) & 1
        for s in sq:
            eL, eR = side[s]; z = s[2]
            t0, t1, tL, tR = tv(('L', s, 0)), tv(('L', s, 1)), tv(('C', eL)), tv(('C', eR))
            assert (t0 + t1 + tL + tR) % 2 == 0
            E = lambda e, t: 1 << i1[('x', x, ('L', e, t))]
            Cz = 1 << i1[('x', x, ('C', z))]
            if t0 and t1: f ^= E(eL, 0) ^ E(eL, 1)
            if tL and tR: f ^= Cz
            if t0 ^ t1:                      # b = 1: one layer cell and one side cell
                t = 0 if t0 else 1
                f ^= E(eL if tL else eR, t)
        assert self.delta(f) & self.xmask[x] == sigma & self.xmask[x], 'Lemma 4.8(1)'
        gx = popc(self.delta(f) & ~self.xmask[x])
        assert gx <= popc(sigma & self.xmask[x]), 'Lemma 4.8(2)'
        return f

    def clean_q(self, q, sigma1):
        i1, i2 = self.idx1, self.idx2
        V, E, Ebd = self.Yq[q]
        sval = {e: (sigma1 >> i2[('q', q, e)]) & 1 for e in E}
        nb = defaultdict(list)
        for e, (u, w) in Ebd.items():
            nb[u].append((w, e)); nb[w].append((u, e))
        h = {V[0]: 0}; stack = [V[0]]
        while stack:
            u = stack.pop()
            for w, e in nb[u]:
                need = h[u] ^ sval[e]
                if w in h: assert h[w] == need, 'σ_q not in B²_q'
                else: h[w] = need; stack.append(w)
        zs = sorted(self.T.adjQZ[q], key=str)
        ones = sum(1 for z in zs if not sval[('C', z)] and h[('L', z, 0)])
        zeros = sum(1 for z in zs if not sval[('C', z)] and not h[('L', z, 0)])
        flip = ones > zeros
        f = 0
        for v, a in h.items():
            if a ^ flip: f ^= 1 << i1[('q', q, v)]
        assert self.delta(f) & self.qmask[q] == sigma1 & self.qmask[q], 'Lemma 4.12(1)'
        assert popc(self.delta(f) & ~self.qmask[q]) <= popc(sigma1 & self.qmask[q]), 'Lemma 4.12(2)'
        return f

    def coarse(self, sigma):
        fX = 0
        for x in self.T.VX: fX ^= self.clean_x(x, sigma)
        s1 = sigma ^ self.delta(fX)
        assert popc(s1) <= popc(sigma), 'Corollary 4.9'
        fQ = 0
        for q in self.T.VQ: fQ ^= self.clean_q(q, s1)
        s2 = s1 ^ self.delta(fQ)
        assert popc(s2) <= popc(s1), 'Corollary 4.13'
        assert s2 & ~self.zmask == 0, 'σ₂ ∉ C_Z²'
        sp = {}
        for z, (a, b) in self.pair.items():
            va, vb = (s2 >> a) & 1, (s2 >> b) & 1
            assert va == vb, 'σ₂ ∉ Im F'
            sp[z] = va
        assert sigma ^ self.delta(fX ^ fQ) == self.F(sp), 'σ = δf + F(σ′)'
        return sp, fX ^ fQ

def connected_sets(nbrs, starts, W):
    seen = set(); stack = [frozenset([j]) for j in starts]
    while stack:
        S = stack.pop()
        if S in seen: continue
        seen.add(S); yield S
        if len(S) < W:
            for u in set().union(*(nbrs[j] for j in S)) - S: stack.append(S | {u})

def main(a, b, W, samples):
    L = Level1(bdl.seed_planar(a, b))
    nq = len(L.idx1)
    byk = defaultdict(set)
    for j, c in L.col.items():
        for k in bits(c): byk[k].add(j)
    nbrs = {j: set().union(*(byk[k] for k in bits(L.col[j]))) - {j} for j in range(nq)}
    stats = defaultdict(int); worst = None; degenerate = []
    def record(sigma, tag):
        nonlocal worst
        sp, f = L.coarse(sigma)
        lift = L.F(sp)
        exc = popc(sigma) - 2 * sum(sp.values())
        d = popc(sigma ^ lift)
        assert exc >= 0
        stats[tag + '_tested'] += 1
        if d and exc == 0:
            stats[tag + '_zero_excess_off_lift'] += 1
            if len(degenerate) < 5:
                degenerate.append({'sigma': sorted(bits(sigma)), 'coarse': sorted(str(z) for z, v in sp.items() if v)})
        if d and exc:
            r = exc / d
            if worst is None or r < worst[0]: worst = (r, exc, d, tag)
    # (A) every valid syndrome δg with g a connected qubit set of size ≤ W
    for S in connected_sets(nbrs, range(nq), W):
        g = 0
        for j in S: g |= 1 << j
        s = L.delta(g)
        if s: record(s, 'local')
    # (B) F(e_z) + δg near each z
    for z, (p0, p1) in L.pair.items():
        base = L.F({z: 1})
        for S in connected_sets(nbrs, byk[p0] | byk[p1], W):
            g = 0
            for j in S: g |= 1 << j
            record(base ^ L.delta(g), 'lifted')
    # (C) random valid syndromes δg, g Bernoulli(p)
    rng = random.Random(20261026)
    for _ in range(samples):
        p = rng.choice([0.01, 0.03, 0.06, 0.1])
        g = 0
        for j in range(nq):
            if rng.random() < p: g |= 1 << j
        s = L.delta(g)
        if s: record(s, 'random')
    print(json.dumps({'seed': [a, b], 'W': W, 'samples': samples, 'level1_qubits': nq,
                      'level1_2cells': len(L.idx2), 'stats': dict(stats),
                      'min_excess_ratio': worst, 'zero_excess_examples': degenerate}))

if __name__ == '__main__':
    main(*map(int, sys.argv[1:5]))
