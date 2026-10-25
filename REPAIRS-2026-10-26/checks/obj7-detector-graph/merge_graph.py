#!/usr/bin/env python3
"""Circuit-level distance of a lattice-surgery merge (objection 7, item 3).

Two d x d rotated patches, A (columns 0..d-1) and B (columns d+1..2d), with a seam column d.
During the merge, the stabilizers of the d x (2d+1) patch are measured for T rounds, using the
same CNOT schedule as detector_graph.py. In basis b, the patch data start in the b-eigenstate
and the seam data in the conjugate eigenstate. The type-b checks touching the seam are then
random in round 0. The measured joint logical is the GF(2) combination of them whose seam
support cancels; its round-0 outcome is the observable. Detectors:
  * type-b checks not touching the seam, in round 0;
  * every check between consecutive rounds;
  * after the split (seam data measured in the conjugate basis, patch data in basis b), the
    final readout against the last round for the type-b checks not touching the seam.
The joint outcome therefore rests on the T merged rounds, as in a real merge.
Every single circuit fault is enumerated as in detector_graph.py. The exact distance is the
shortest odd-observable walk in the type-b detector graph; the boundary node includes the time
boundary of the merge's first round.
"""
import itertools, json, sys
from collections import defaultdict, deque
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from detector_graph import propagate, PAULI1

def build_merge(d, T, basis, order_x, order_z):
    rows, cols = d, 2 * d + 1
    seam = d
    data = {(i, j): i * cols + j for i in range(rows) for j in range(cols)}
    nq = rows * cols
    checks = []
    for i in range(-1, rows):
        for j in range(-1, cols):
            corners = {'NW': (i, j), 'NE': (i, j + 1), 'SW': (i + 1, j), 'SE': (i + 1, j + 1)}
            present = {k: v for k, v in corners.items() if v in data}
            typ = 'X' if (i + j) % 2 == 0 else 'Z'
            inner = 0 <= i < rows - 1 and 0 <= j < cols - 1
            if len(present) == 4 and inner:
                pass
            elif len(present) == 2:
                if typ == 'X' and not (i == -1 or i == rows - 1):
                    continue
                if typ == 'Z' and not (j == -1 or j == cols - 1):
                    continue
            else:
                continue
            order = order_x if typ == 'X' else order_z
            qs = [data[present[k]] for k in order if k in present]
            slots = [k in present for k in order]
            touches = any(v[1] == seam for v in present.values())
            checks.append((typ, nq, qs, slots, touches))
            nq += 1
    seamq = {data[(i, seam)] for i in range(rows)}
    other = 'X' if basis == 'Z' else 'Z'
    ops, meas = [], []
    allq = list(range(rows * cols))
    for q in allq:
        ops.append(('R', (q,)))
        conj = q in seamq
        if (basis == 'X') != conj:  # X-eigenstate for basis X off the seam, or for basis Z on it
            ops.append(('H', (q,)))
    for r in range(T):
        for (typ, a, qs, slots, _) in checks:
            ops.append(('R', (a,)))
            if typ == 'X':
                ops.append(('H', (a,)))
        for layer in range(4):
            busy = set()
            for (typ, a, qs, slots, _) in checks:
                if not slots[layer]:
                    continue
                q = qs[sum(slots[:layer])]
                busy.add(q)
                ops.append(('CX', (a, q)) if typ == 'X' else ('CX', (q, a)))
            for q in allq:
                if q not in busy:
                    ops.append(('I', (q,)))
        for (typ, a, qs, slots, _) in checks:
            if typ == 'X':
                ops.append(('H', (a,)))
            ops.append(('M', (a,)))
            meas.append(('anc', (r, a)))
    # split: the seam data are measured in the conjugate basis, the patch data in basis b
    for q in allq:
        conj = q in seamq
        if (basis == 'X') != conj:
            ops.append(('H', (q,)))
        ops.append(('M', (q,)))
        meas.append(('data', q))
    idx = {lab: n for n, (_, lab) in enumerate(meas)}
    dets = []
    for (typ, a, qs, slots, touches) in checks:
        if typ == basis and not touches:
            dets.append((typ, [idx[(0, a)]]))
        for r in range(1, T):
            dets.append((typ, [idx[(r, a)], idx[(r - 1, a)]]))
        if typ == basis and not touches:
            dets.append((typ, [idx[q] for q in qs] + [idx[(T - 1, a)]]))
    # joint logical: GF(2) combination of random type-b checks whose seam support cancels
    rnd = [(a, qs) for (typ, a, qs, s, touches) in checks if typ == basis and touches]
    vecs = []
    for (a, qs) in rnd:
        v = 0
        for q in qs:
            if q in seamq:
                v |= 1 << q
        vecs.append(v)
    # find a nonzero combination with zero seam support (null vector) by elimination
    n = len(vecs)
    rows_ = [(vecs[k], 1 << k) for k in range(n)]
    basis_rows = []
    combo = None
    for v, c in rows_:
        for bv, bc in basis_rows:
            if v ^ bv < v:
                v ^= bv; c ^= bc
        if v == 0:
            combo = c; break
        basis_rows.append((v, c))
        basis_rows.sort(reverse=True)
    if combo is None:
        raise RuntimeError('no joint logical for this basis')
    chosen = [rnd[k][0] for k in range(n) if combo >> k & 1]
    obs = [idx[(0, a)] for a in chosen]
    return ops, meas, dets, obs, len(chosen)

def analyse_merge(d, T, basis, order_x, order_z):
    ops, meas, dets, obs, nch = build_merge(d, T, basis, order_x, order_z)
    det_masks = []
    for (typ, ms) in dets:
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
            cands = [{qs[0]: PAULI1[p]} for p in 'XYZ']; start = n_ + 1
        elif op == 'CX':
            cands = []
            for p, q in itertools.product('IXYZ', repeat=2):
                if p == 'I' and q == 'I':
                    continue
                f = {}
                if p != 'I': f[qs[0]] = PAULI1[p]
                if q != 'I': f[qs[1]] = PAULI1[q]
                cands.append(f)
            start = n_ + 1
        elif op == 'M':
            cands = [{qs[0]: (1, 0)}]; start = n_
        else:
            continue
        mb = mb_list[start] if start < len(ops) else m
        for f in cands:
            flips = propagate(ops, start, {q: v[0] for q, v in f.items()}, {q: v[1] for q, v in f.items()}, mb)
            sig = frozenset(k for k, mm in enumerate(det_masks) if bin(mm & flips).count('1') % 2)
            ob = bin(obs_mask & flips).count('1') % 2
            faults.append((n_, sig, ob))
    types = [t for (t, _) in dets]
    single = any((not sig) and ob for (_, sig, ob) in faults)
    graphlike = all(sum(1 for k in sig if types[k] == t) <= 2 for (_, sig, _) in faults for t in 'XZ')
    eobs = defaultdict(set)
    for (_, sig, ob) in faults:
        part = tuple(sorted(k for k in sig if types[k] == basis))
        if len(part) == 1:
            eobs[(part[0], 'B')].add(ob)
        elif len(part) == 2:
            eobs[part].add(ob)
        elif len(part) == 0 and ob:
            pass
    adj = defaultdict(list)
    for (a, b), obset in eobs.items():
        for ob in obset:
            adj[a].append((b, ob)); adj[b].append((a, ob))
    start, goal = ('B', 0), ('B', 1)
    seen = {start: 0}; dq = deque([start]); exact = None
    while dq:
        u = dq.popleft()
        if u == goal:
            exact = seen[u]; break
        for (v, ob) in adj[u[0]]:
            w = (v, u[1] ^ ob)
            if w not in seen:
                seen[w] = seen[u] + 1; dq.append(w)
    if single:
        exact = 1
    return {'d': d, 'T': T, 'basis': basis, 'joint_logical_checks': nch, 'faults': len(faults),
            'graphlike_per_type': graphlike, 'circuit_distance_exact': exact}

if __name__ == '__main__':
    std = (['NW', 'NE', 'SW', 'SE'], ['NW', 'SW', 'NE', 'SE'])
    out = []
    for d in map(int, sys.argv[1:] or ['3', '5']):
        for T in sorted({d, max(1, d - 2), d + 2}):
            for basis in 'ZX':
                try:
                    out.append(analyse_merge(d, T, basis, *std))
                except RuntimeError as e:
                    out.append({'d': d, 'T': T, 'basis': basis, 'note': str(e)})
    print(json.dumps(out, indent=1))
