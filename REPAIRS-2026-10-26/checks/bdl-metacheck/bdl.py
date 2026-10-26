#!/usr/bin/env python3
"""Algebraic construction of the Balasubramanian–Davydova–Lin codes C(i) (arXiv:2605.10943 §3.2.2),
and a metacheck-soundness test (pātai 2⁵).

The geometric embedding into R³ does not change the abstract cochain complex, so it is omitted.
A Tanner square complex is (VX, VQ, VZ, edges, squares) with squares (x, q, z, q').
R_X follows §3.2.2 with subdivision parameter m = (ℓ−1)/2 = 1 (ℓ = 3):
  Y_x = X_x×{0} ⊔ X_x×{1} ⊔ ∂X_x×[0,1],  C_x = C•(Y_x);
  Y_q = X_q×{0} ⊔ X_q×{1} ⊔ ∂X_q×[0,1],  C_q = C•(Y_q)[−1];
  Y_z = two points,                       C_z = C•(Y_z)[−2];
  g_xq, g_qz = restriction along Y_q ↪ Y_x and Y_z ↪ Y_q; δ = δ_loc + g (total complex).
R_Z is the dual iteration: swap the X and Z roles, apply R_X, and swap back.
Linear algebra over F₂ uses Python integers as bit rows.
"""
import sys, json, itertools
from collections import defaultdict

# ---------- F2 linear algebra on rows stored as ints ----------
def rank_and_basis(rows):
    basis = {}  # pivot bit -> row
    for r in rows:
        while r:
            p = r.bit_length() - 1
            if p in basis:
                r ^= basis[p]
            else:
                basis[p] = r; break
    return basis

def reduce(r, basis):
    while r:
        p = r.bit_length() - 1
        if p in basis:
            r ^= basis[p]
        else:
            return r
    return 0

def left_kernel(rows, ncols_unused=None):
    """Vectors v (over row indices) with sum_i v_i rows[i] = 0; returns a basis as ints over rows."""
    basis = {}  # pivot -> (row value, combination)
    kern = []
    for i, r in enumerate(rows):
        comb = 1 << i
        while r:
            p = r.bit_length() - 1
            if p in basis:
                br, bc = basis[p]; r ^= br; comb ^= bc
            else:
                basis[p] = (r, comb); break
        if r == 0:
            kern.append(comb)
    return kern

# ---------- complexes ----------
class TSC:
    def __init__(self, VX, VQ, VZ, squares):
        self.VX, self.VQ, self.VZ, self.squares = list(VX), list(VQ), list(VZ), list(squares)
        self.adjXQ = defaultdict(set); self.adjQZ = defaultdict(set)
        for (x, q, z, q2) in self.squares:
            for qq in (q, q2):
                self.adjXQ[x].add(qq); self.adjQZ[qq].add(z)

def seed_planar(a, b):
    """Planar surface code: X-checks = vertices off the rough columns, qubits = edges (vertical edges
    on columns 0 and a removed), Z-checks = all faces. Squares: (vertex, edge, face, edge) corners."""
    V = [(i, j) for i in range(1, a) for j in range(b + 1)]
    Vs = set(V)
    E = []
    for i in range(a):
        for j in range(b + 1):
            E.append(('h', i, j))
    for i in range(1, a):
        for j in range(b):
            E.append(('v', i, j))
    Es = set(E)
    F = [(i, j) for i in range(a) for j in range(b)]
    def ends(e):
        t, i, j = e
        return [(i, j), (i + 1, j)] if t == 'h' else [(i, j), (i, j + 1)]
    def fedges(f):
        i, j = f
        return [('h', i, j), ('h', i, j + 1), ('v', i, j), ('v', i + 1, j)]
    squares = []
    for f in F:
        fe = [e for e in fedges(f) if e in Es]
        for v in Vs:
            sh = [e for e in fe if v in ends(e)]
            if len(sh) == 2:
                squares.append((('X', v), ('Q', sh[0]), ('Z', f), ('Q', sh[1])))
            assert len(sh) in (0, 2), (v, f, sh)
    return TSC([('X', v) for v in V], [('Q', e) for e in E], [('Z', f) for f in F], squares)

def cells_of_star_x(T, x):
    """X_x: closure of squares containing x; returns vertices, edges, faces of X_x and ∂X_x."""
    sq = [s for s in T.squares if s[0] == x]
    verts, edges, faces = set(), set(), []
    for s in sq:
        xx, q, z, q2 = s
        verts |= {xx, q, z, q2}
        es = [frozenset((xx, q)), frozenset((q, z)), frozenset((z, q2)), frozenset((q2, xx))]
        edges |= set(es)
        faces.append((s, es))
    bedges = {e for e in edges if x not in e}
    bverts = set().union(*bedges) if bedges else set()
    return verts, edges, faces, bverts, bedges

def build_Yx(T, x):
    verts, edges, faces, bverts, bedges = cells_of_star_x(T, x)
    V = [('L', v, t) for v in verts for t in (0, 1)] 
    E = [('L', e, t) for e in edges for t in (0, 1)] + [('C', v) for v in bverts]
    Fc = [('L', s, t) for (s, es) in faces for t in (0, 1)] + [('C', e) for e in bedges]
    Ebd = {}
    for e in edges:
        u, w = tuple(e)
        for t in (0, 1):
            Ebd[('L', e, t)] = [('L', u, t), ('L', w, t)]
    for v in bverts:
        Ebd[('C', v)] = [('L', v, 0), ('L', v, 1)]
    Fbd = {}
    for (s, es) in faces:
        for t in (0, 1):
            Fbd[('L', s, t)] = [('L', e, t) for e in es]
    for e in bedges:
        u, w = tuple(e)
        Fbd[('C', e)] = [('L', e, 0), ('L', e, 1), ('C', u), ('C', w)]
    return V, E, Fc, Ebd, Fbd

def build_Yq(T, q):
    zs = sorted(T.adjQZ[q])
    V = [('L', q, t) for t in (0, 1)] + [('L', z, t) for z in zs for t in (0, 1)]
    E = [('L', frozenset((q, z)), t) for z in zs for t in (0, 1)] + [('C', z) for z in zs]
    Ebd = {}
    for z in zs:
        for t in (0, 1):
            Ebd[('L', frozenset((q, z)), t)] = [('L', q, t), ('L', z, t)]
        Ebd[('C', z)] = [('L', z, 0), ('L', z, 1)]
    return V, E, Ebd

def RX(T):
    idx0, idx1, idx2 = {}, {}, {}
    def ix(d, key):
        if key not in d:
            d[key] = len(d)
        return d[key]
    d0 = defaultdict(int)  # column (C^0 index) -> bits over C^1  (we store δ0 as rows over C^1 indexed by C^0 element)
    d1rows = defaultdict(int)  # C^2 index -> bits over C^1
    Yx = {x: build_Yx(T, x) for x in T.VX}
    Yq = {q: build_Yq(T, q) for q in T.VQ}
    # register cells
    for x, (V, E, Fc, Ebd, Fbd) in Yx.items():
        for v in V: ix(idx0, ('x', x, v))
        for e in E: ix(idx1, ('x', x, e))
        for f in Fc: ix(idx2, ('x', x, f))
    for q, (V, E, Ebd) in Yq.items():
        for v in V: ix(idx1, ('q', q, v))
        for e in E: ix(idx2, ('q', q, e))
    for z in T.VZ:
        for t in (0, 1): ix(idx2, ('z', z, t))
    # δ_X^0, δ_X^1 (local coboundaries in Y_x)
    for x, (V, E, Fc, Ebd, Fbd) in Yx.items():
        for e, bd in Ebd.items():
            for v in bd:
                d0[idx0[('x', x, v)]] ^= 1 << idx1[('x', x, e)]
        for f, bd in Fbd.items():
            for e in bd:
                d1rows[idx2[('x', x, f)]] ^= 1 << idx1[('x', x, e)]
    # δ_Q^1 (Y_q vertices -> edges, shifted)
    for q, (V, E, Ebd) in Yq.items():
        for e, bd in Ebd.items():
            for v in bd:
                d1rows[idx2[('q', q, e)]] ^= 1 << idx1[('q', q, v)]
    # g_XQ: restriction along Y_q ⊂ Y_x for adjacent x, q
    for x, (V, E, Fc, Ebd, Fbd) in Yx.items():
        Vset, Eset = set(V), set(E)
        for q in T.adjXQ[x]:
            Vq, Eq, _ = Yq[q]
            for c in Vq:
                assert c in Vset, ('Y_q not in Y_x (vertex)', x, q, c)
                d0[idx0[('x', x, c)]] ^= 1 << idx1[('q', q, c)]
            for c in Eq:
                assert c in Eset, ('Y_q not in Y_x (edge)', x, q, c)
                d1rows[idx2[('q', q, c)]] ^= 1 << idx1[('x', x, c)]
    # g_QZ: restriction to the two copies of z
    for q, (V, E, Ebd) in Yq.items():
        for z in T.adjQZ[q]:
            for t in (0, 1):
                d1rows[idx2[('z', z, t)]] ^= 1 << idx1[('q', q, ('L', z, t))]
    n0, n1, n2 = len(idx0), len(idx1), len(idx2)
    D0 = [d0[i] for i in range(n0)]          # X-check rows over qubits (support of δ0 e_x)
    D1 = [d1rows[i] for i in range(n2)]      # Z-check rows over qubits
    return D0, D1, (n0, n1, n2)

def check_complex(D0, D1):
    # δ1∘δ0 = 0: every Z-row has even overlap with every X-row
    bad = 0
    for zr in D1:
        for xr in D0:
            if bin(zr & xr).count('1') % 2:
                bad += 1
                if bad > 3: return False
    return bad == 0

def to_TSC(D0, D1, n1):
    """Tanner square complex of the code: squares pair the qubits shared by each (X-check, Z-check)."""
    VX = [('X', i) for i in range(len(D0))]; VQ = [('Q', j) for j in range(n1)]; VZ = [('Z', k) for k in range(len(D1))]
    qx = defaultdict(list)
    for i, r in enumerate(D0):
        b = r
        while b:
            j = b.bit_length() - 1; qx[j].append(i); b ^= 1 << j
    squares = []; big = 0
    for k, zr in enumerate(D1):
        shared = defaultdict(list)
        b = zr
        while b:
            j = b.bit_length() - 1; b ^= 1 << j
            for i in qx[j]:
                shared[i].append(j)
        for i, qs in shared.items():
            assert len(qs) % 2 == 0
            if len(qs) > 2: big += 1
            qs = sorted(qs)
            for a in range(0, len(qs), 2):
                squares.append((('X', i), ('Q', qs[a]), ('Z', k), ('Q', qs[a + 1])))
    return TSC(VX, VQ, VZ, squares), big

def swap(T):
    sq = [(('X', z[1]) if True else None, q, ('Z', x[1]), q2) for (x, q, z, q2) in T.squares]
    return TSC([('X', z[1]) for z in T.VZ], T.VQ, [('Z', x[1]) for x in T.VX], sq)

def code_of(T):
    qi = {q: j for j, q in enumerate(T.VQ)}
    D0 = []
    for x in T.VX:
        r = 0
        for q in T.adjXQ[x]: r |= 1 << qi[q]
        D0.append(r)
    D1 = []
    for z in T.VZ:
        r = 0
        for q in T.VQ:
            if z in T.adjQZ[q]: r |= 1 << qi[q]
        D1.append(r)
    return D0, D1

def logical_count(D0, D1, n1):
    return n1 - len(rank_and_basis(D0)) - len(rank_and_basis(D1))

def check_graph(rows):
    """Checks adjacent when they share a qubit."""
    byq = defaultdict(list)
    for i, r in enumerate(rows):
        b = r
        while b:
            j = b.bit_length() - 1; b ^= 1 << j; byq[j].append(i)
    adj = defaultdict(set)
    for j, cs in byq.items():
        for a in cs:
            for b2 in cs:
                if a != b2: adj[a].add(b2)
    return adj

def metacheck_profile(rows, radius):
    """dim of all dependencies vs dim of the span of dependencies supported in radius-r check balls."""
    allk = left_kernel(rows)
    adj = check_graph(rows)
    loc_basis = {}
    for c in range(len(rows)):
        ball = {c}; frontier = {c}
        for _ in range(radius):
            frontier = {b for a in frontier for b in adj[a]} - ball
            ball |= frontier
        ball = sorted(ball)
        sub = [rows[i] for i in ball]
        for kv in left_kernel(sub):
            v = 0; b = kv
            while b:
                t = b.bit_length() - 1; b ^= 1 << t; v |= 1 << ball[t]
            r = reduce(v, loc_basis)
            if r:
                loc_basis[r.bit_length() - 1] = r
    return len(allk), len(loc_basis), allk, loc_basis

if __name__ == '__main__':
    a, b, levels, radius = map(int, sys.argv[1:5])
    T = seed_planar(a, b)
    out = []
    for lev in range(levels + 1):
        D0, D1 = code_of(T)
        n1 = len(T.VQ)
        rec = {'level': lev, 'qubits': n1, 'xchecks': len(D0), 'zchecks': len(D1),
               'logical': logical_count(D0, D1, n1)}
        if n1 <= 60000:
            dz, dzl, _, _ = metacheck_profile(D1, radius)     # dependencies among Z-checks (X-error syndromes)
            # X-check rows as rows over qubits: dependencies among X-checks (Z-error syndromes)
            dx, dxl, _, _ = metacheck_profile(D0, radius)
            rec.update({'Zcheck_deps': dz, 'Zcheck_deps_local': dzl, 'Xcheck_deps': dx, 'Xcheck_deps_local': dxl})
        out.append(rec); print(json.dumps(rec), flush=True)
        if lev == levels: break
        if lev % 2 == 0:
            D0n, D1n, (n0, n1n, n2) = RX(T)
        else:
            S = swap(T); D0s, D1s, (n0s, n1s, n2s) = RX(S)
            # swap back: the new X-checks are the dual's Z-checks
            D0n, D1n, n1n = D1s, D0s, n1s
        assert check_complex(D0n, D1n), 'd1 d0 != 0'
        T, big = to_TSC(D0n, D1n, n1n)
        if big: print(json.dumps({'warning': 'X/Z pairs sharing >2 qubits', 'count': big}), flush=True)
