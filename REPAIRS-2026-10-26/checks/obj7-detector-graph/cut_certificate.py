#!/usr/bin/env python3
"""Exact disjoint-cut certificate for the circuit-level distance (objection 7, item 3).

For any set S of detectors of the relevant type, the fault set
    K_S = { f : obs(f) xor |sig(f) ∩ S| is odd }
is crossed an odd number of times by every fault set with zero relevant syndrome and odd
observable. Indeed, the parity of |F ∩ K_S| is obs(F) plus the syndrome of F summed over S, which
is 1 + 0. So if S_1, ..., S_D give pairwise disjoint K_{S_m}, every logical error has at least D
faults.

Construction:
  1. gauge: find S0 with obs(f) = |sig(f) ∩ S0| mod 2 on every two-detector fault, by 2-colouring
     the interior graph (consistent when no interior cycle carries odd observable), so the
     re-gauged observable obs' lives on boundary faults only;
  2. phi(v) = 1 + graph distance from A = {detectors carrying an obs' = 1 boundary fault};
  3. S_m = S0 xor {v : phi(v) < m}, for m = 1..D.
Every fault's multiplicity, the number of m with f in K_{S_m}, is computed exactly; the
certificate holds when every multiplicity is at most 1 and D cuts exist.
"""
import itertools, json, sys
from collections import defaultdict, deque
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import detector_graph as DG
import merge_graph as MG

def memory_faults(d, rounds, basis, ox, oz):
    DG.FACE.clear()
    checks, dets, faults = DG.enumerate_faults(d, ox, oz, rounds, basis)
    types = [t for (t, _, _) in dets]
    coords = []
    for (t, ms, a) in dets:
        coords.append(DG.FACE[a])
    return faults, types, coords

def merge_faults(d, T, basis, ox, oz):
    ops, meas, dets, obs, nch, oprnd, rows, cols = MG.build_merge(d, T, basis, ox, oz)
    det_masks = []
    for (typ, ms, c) in dets:
        mm = 0
        for x in ms:
            mm |= 1 << x
        det_masks.append(mm)
    obs_mask = 0
    for x in obs:
        obs_mask |= 1 << x
    mb_list, m = [], 0
    for op, qs in ops:
        mb_list.append(m)
        if op == 'M':
            m += 1
    faults = []
    for n_, (op, qs) in enumerate(ops):
        if op in ('R', 'H', 'I'):
            cands = [{qs[0]: DG.PAULI1[p]} for p in 'XYZ']; start = n_ + 1
        elif op == 'CX':
            cands = []
            for p, q in itertools.product('IXYZ', repeat=2):
                if p == 'I' and q == 'I':
                    continue
                f = {}
                if p != 'I': f[qs[0]] = DG.PAULI1[p]
                if q != 'I': f[qs[1]] = DG.PAULI1[q]
                cands.append(f)
            start = n_ + 1
        elif op == 'M':
            cands = [{qs[0]: (1, 0)}]; start = n_
        else:
            continue
        mb = mb_list[start] if start < len(ops) else m
        for f in cands:
            flips = DG.propagate(ops, start, {q: v[0] for q, v in f.items()}, {q: v[1] for q, v in f.items()}, mb)
            sig = frozenset(k for k, mm in enumerate(det_masks) if bin(mm & flips).count('1') % 2)
            ob = bin(obs_mask & flips).count('1') % 2
            faults.append((n_, sig, ob))
    types = [t for (t, _, _) in dets]
    coords = [c for (_, _, c) in dets]
    return faults, types, coords

def certificate(faults, types, rel, phi_fn=None, S0_fn=None, D_target=None, coords=None):
    rf = []
    for (loc, sig, ob) in faults:
        part = tuple(sorted(k for k in sig if types[k] == rel))
        rf.append((part, ob))
    if any(len(p) > 2 for p, _ in rf):
        return {'graphlike': False}
    if any(len(p) == 0 and ob for p, ob in rf):
        return {'graphlike': True, 'D': 1, 'certificate': 'single undetected logical fault'}
    # 1. gauge by 2-colouring the interior graph
    adj = defaultdict(list)
    for p, ob in rf:
        if len(p) == 2:
            adj[p[0]].append((p[1], ob)); adj[p[1]].append((p[0], ob))
    nodes = sorted({k for p, _ in rf for k in p})
    colour = {}
    for s in nodes:
        if s in colour:
            continue
        colour[s] = 0; dq = deque([s])
        while dq:
            u = dq.popleft()
            for v, ob in adj[u]:
                c = colour[u] ^ ob
                if v not in colour:
                    colour[v] = c; dq.append(v)
                elif colour[v] != c:
                    return {'graphlike': True, 'gauge': 'inconsistent (odd interior cycle)'}
    S0 = {v for v in nodes if colour[v]}
    if S0_fn is not None:
        S0 = {v for v in nodes if S0_fn(coords[v])}
    obsp = []
    for p, ob in rf:
        obsp.append((p, ob ^ (sum(1 for k in p if k in S0) % 2)))
    A = {p[0] for p, o in obsp if len(p) == 1 and o == 1}
    # 2. phi = 1 + graph distance from A over interior edges
    phi = {v: None for v in nodes}
    dq = deque()
    for v in A:
        phi[v] = 1; dq.append(v)
    while dq:
        u = dq.popleft()
        for v, _ in adj[u]:
            if phi[v] is None:
                phi[v] = phi[u] + 1; dq.append(v)
    BIG = 10 ** 9
    ph = {v: (phi[v] if phi[v] is not None else BIG) for v in nodes}
    if phi_fn is not None:
        ph = {v: phi_fn(coords[v]) for v in nodes}
    # D = shortest odd walk = min over other-side boundary detectors of phi + 1, and over A-pairs
    other = [p[0] for p, o in obsp if len(p) == 1 and o == 0]
    D = min([ph[v] + 1 for v in other] + [2 * 1 if any(len(p) == 1 and o == 1 and p[0] in other for p, o in obsp) else BIG])
    if D_target is not None:
        D = D_target
    # 3. multiplicities
    worst = 0; bad = 0
    for p, o in obsp:
        mult = 0
        for m in range(1, D + 1):
            inS = sum(1 for k in p if ph[k] < m) % 2
            if (o ^ inS) == 1:
                mult += 1
        worst = max(worst, mult)
        if mult > 1:
            bad += 1
    return {'graphlike': True, 'D': D, 'max_multiplicity': worst, 'faults_in_two_or_more_cuts': bad,
            'certificate_holds': worst <= 1, 'phi': ph, 'A': sorted(A), 'S0': sorted(S0), 'obsp': obsp}

def phi_memory(basis):
    """Closed-form memory potential: the crossing face coordinate plus one."""
    k = 0 if basis == 'Z' else 1
    return lambda x: x[k] + 1

def phi_merge(d, T):
    """Closed-form merge potential max(tau(r), sigma(j)): tau(r) = max(1, r) is the time part;
    sigma is 1 on the two seam face columns d-1 and d, d-1-j to their left, j-d to their right."""
    def f(x):
        r, i, j = x
        tau = max(1, r)
        sig = d - 1 - j if j <= d - 2 else (j - d if j >= d + 1 else 1)
        return max(tau, sig)
    return f

def formula_run(ds):
    std = (['NW', 'NE', 'SW', 'SE'], ['NW', 'SW', 'NE', 'SE'])
    out = []
    for d in ds:
        for basis in 'ZX':
            f, t, c = memory_faults(d, d, basis, *std)
            r = certificate(f, t, basis, phi_fn=phi_memory(basis), S0_fn=lambda x: False, D_target=d, coords=c)
            out.append(dict(kind='memory', d=d, T=d, basis=basis, D=d, faults=len(f),
                            max_multiplicity=r['max_multiplicity'], certificate_holds=r['certificate_holds']))
        for T in (d - 2, d, d + 2):
            if T < 2:
                continue
            f, t, c = merge_faults(d, T, 'X', *std)
            Dt = min(d, T)
            r = certificate(f, t, 'X', phi_fn=phi_merge(d, T), S0_fn=lambda x: False, D_target=Dt, coords=c)
            out.append(dict(kind='merge', d=d, T=T, basis='X', D=Dt, faults=len(f),
                            max_multiplicity=r['max_multiplicity'], certificate_holds=r['certificate_holds']))
    return out

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'formula':
    print(json.dumps(formula_run(list(map(int, sys.argv[2:] or ['3', '5', '7']))), indent=1))
    sys.exit(0)

if __name__ == '__main__':
    std = (['NW', 'NE', 'SW', 'SE'], ['NW', 'SW', 'NE', 'SE'])
    swp = (['NW', 'SW', 'NE', 'SE'], ['NW', 'NE', 'SW', 'SE'])
    out = []
    for d in map(int, sys.argv[1:] or ['3', '5']):
        for name, sch in (('standard', std), ('swapped', swp)):
            for basis in 'ZX':
                f, t, c = memory_faults(d, d, basis, *sch)
                r = certificate(f, t, basis); r.pop('phi', None); r.pop('A', None)
                out.append(dict(kind='memory', d=d, T=d, basis=basis, schedule=name, **r))
        for T in (d - 2, d, d + 2):
            if T < 1:
                continue
            f, t, c = merge_faults(d, T, 'X', *std)
            r = certificate(f, t, 'X'); r.pop('phi', None); r.pop('A', None)
            out.append(dict(kind='merge', d=d, T=T, basis='X', schedule='standard', **r))
    print(json.dumps(out, indent=1))
