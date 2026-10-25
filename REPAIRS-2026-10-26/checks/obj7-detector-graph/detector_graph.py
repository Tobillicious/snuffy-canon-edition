#!/usr/bin/env python3
"""Circuit-level detector graph of the distance-d rotated surface code memory (objection 7.2/7.3).

Dependency-free Pauli-frame enumeration. For a memory experiment in the Z basis (logical Z
observable) and the X basis (logical X observable), every single circuit fault is inserted:
  * after each CNOT: each of the 15 non-identity two-qubit Paulis;
  * after each reset, Hadamard and idle: X, Y, Z;
  * before each measurement: a measurement flip (X before a Z measurement).
Each fault is propagated to the end of the circuit. Its signature is the set of flipped
detectors, and its observable bit is whether it flips the logical measurement.

Reported, for each CNOT ordering:
  * circuit distance >= 2 iff no single fault has empty signature and flips the observable;
  * circuit distance >= 3 iff in addition no two faults have equal signatures and different
    observable bits;
  * graphlike: every fault flips at most two detectors of each check type;
  * the maximum degree of the per-type detector graph (boundary node included);
  * the multiplicity c: the maximum number of distinct fault locations producing one edge.
"""
import itertools, json, sys
from collections import defaultdict

def build(d, order_x, order_z, rounds, basis):
    data = {(i, j): i * d + j for i in range(d) for j in range(d)}
    checks = []  # (type, ancilla, [data in CNOT order])
    nq = d * d
    for i in range(-1, d):
        for j in range(-1, d):
            corners = {'NW': (i, j), 'NE': (i, j + 1), 'SW': (i + 1, j), 'SE': (i + 1, j + 1)}
            present = {k: v for k, v in corners.items() if v in data}
            typ = 'X' if (i + j) % 2 == 0 else 'Z'
            inner = 0 <= i < d - 1 and 0 <= j < d - 1
            if len(present) == 4 and inner:
                pass
            elif len(present) == 2:
                # X-type checks on the top and bottom boundaries, Z-type on the left and right
                if typ == 'X' and not (i == -1 or i == d - 1):
                    continue
                if typ == 'Z' and not (j == -1 or j == d - 1):
                    continue
            else:
                continue
            order = order_x if typ == 'X' else order_z
            qs = [data[present[k]] for k in order if k in present]
            slots = [k in present for k in order]
            checks.append((typ, nq, qs, slots))
            nq += 1
    ops = []  # (op, qubits)
    meas = []  # measurement record: (kind, label)
    allq = list(range(d * d))
    # initialisation of data
    for q in allq:
        ops.append(('R', (q,)))
        if basis == 'X':
            ops.append(('H', (q,)))
    for r in range(rounds):
        for (typ, a, qs, slots) in checks:
            ops.append(('R', (a,)))
            if typ == 'X':
                ops.append(('H', (a,)))
        for layer in range(4):
            busy = set()
            for (typ, a, qs, slots) in checks:
                if not slots[layer]:
                    continue
                q = qs[sum(slots[:layer])]
                busy.add(q)
                ops.append(('CX', (a, q)) if typ == 'X' else ('CX', (q, a)))
            for q in allq:
                if q not in busy:
                    ops.append(('I', (q,)))
        for (typ, a, qs, slots) in checks:
            if typ == 'X':
                ops.append(('H', (a,)))
            ops.append(('M', (a,)))
            meas.append(('anc', (r, a)))
    for q in allq:
        if basis == 'X':
            ops.append(('H', (q,)))
        ops.append(('M', (q,)))
        meas.append(('data', q))
    return checks, ops, meas

def detectors(d, checks, meas, rounds, basis):
    idx = {lab: n for n, (_, lab) in enumerate(meas)}
    dets = []  # (type, list of measurement indices)
    det_type = 'Z' if basis == 'Z' else 'X'  # check type deterministic in round 0
    for (typ, a, qs, slots) in checks:
        if typ == det_type:
            dets.append((typ, [idx[(0, a)]]))
        for r in range(1, rounds):
            dets.append((typ, [idx[(r, a)], idx[(r - 1, a)]]))
        if typ == det_type:
            dets.append((typ, [idx[q] for q in qs] + [idx[(rounds - 1, a)]]))
    return dets

def logical_support(d, checks, basis):
    # logical Z = Z on a line commuting with every X check; logical X likewise for Z checks
    lines = [[i * d + j for j in range(d)] for i in range(d)] + [[i * d + j for i in range(d)] for j in range(d)]
    other = 'X' if basis == 'Z' else 'Z'
    for line in lines:
        if all(len(set(line) & set(qs)) % 2 == 0 for (typ, a, qs, s) in checks if typ == other):
            return line
    raise RuntimeError('no logical line')

def propagate(ops, start, frame_x, frame_z, nmeas):
    """Propagate a Pauli frame from op index `start` onward; return the flipped measurement set."""
    flips = 0
    m = nmeas
    fx, fz = dict(frame_x), dict(frame_z)
    for op, qs in ops[start:]:
        if op == 'R':
            q, = qs; fx[q] = 0; fz[q] = 0
        elif op == 'H':
            q, = qs; fx[q], fz[q] = fz.get(q, 0), fx.get(q, 0)
        elif op == 'CX':
            c, t = qs
            fx[t] = fx.get(t, 0) ^ fx.get(c, 0)
            fz[c] = fz.get(c, 0) ^ fz.get(t, 0)
        elif op == 'M':
            q, = qs
            if fx.get(q, 0):
                flips |= 1 << m
            m += 1
    return flips

PAULI1 = {'X': (1, 0), 'Y': (1, 1), 'Z': (0, 1)}

def enumerate_faults(d, order_x, order_z, rounds, basis):
    checks, ops, meas = build(d, order_x, order_z, rounds, basis)
    dets = detectors(d, checks, meas, rounds, basis)
    obs = logical_support(d, checks, basis)
    obs_meas = [n for n, (k, lab) in enumerate(meas) if k == 'data' and lab in obs]
    det_masks = []
    for (typ, ms) in dets:
        mm = 0
        for x in ms:
            mm |= 1 << x
        det_masks.append(mm)
    obs_mask = 0
    for x in obs_meas:
        obs_mask |= 1 << x
    mcount = [0]
    meas_before = []
    for op, qs in ops:
        meas_before.append(mcount[0])
        if op == 'M':
            mcount[0] += 1
    faults = []  # (location, signature frozenset, obs bit)
    for n, (op, qs) in enumerate(ops):
        if op in ('R', 'H', 'I'):
            cands = [{qs[0]: PAULI1[p]} for p in 'XYZ']
            start = n + 1
            mb = meas_before[n + 1] if n + 1 < len(ops) else mcount[0]
        elif op == 'CX':
            cands = []
            for p, q in itertools.product('IXYZ', repeat=2):
                if p == 'I' and q == 'I':
                    continue
                f = {}
                if p != 'I': f[qs[0]] = PAULI1[p]
                if q != 'I': f[qs[1]] = PAULI1[q]
                cands.append(f)
            start = n + 1
            mb = meas_before[n + 1] if n + 1 < len(ops) else mcount[0]
        elif op == 'M':
            cands = [{qs[0]: (1, 0)}]
            start = n
            mb = meas_before[n]
        else:
            continue
        for f in cands:
            fx = {q: v[0] for q, v in f.items()}
            fz = {q: v[1] for q, v in f.items()}
            flips = propagate(ops, start, fx, fz, mb)
            sig = frozenset(k for k, mm in enumerate(det_masks) if bin(mm & flips).count('1') % 2)
            ob = bin(obs_mask & flips).count('1') % 2
            faults.append((n, sig, ob))
    return checks, dets, faults

def analyse(d, order_x, order_z, rounds, basis):
    checks, dets, faults = enumerate_faults(d, order_x, order_z, rounds, basis)
    single_logical = [f for f in faults if not f[1] and f[2]]
    by_sig = defaultdict(set)
    for (_, sig, ob) in faults:
        by_sig[sig].add(ob)
    pair_logical = [s for s, obs in by_sig.items() if len(obs) == 2]
    dist = 1 if single_logical else (2 if pair_logical else 3)
    types = [t for (t, _) in dets]
    graphlike = all(sum(1 for k in sig if types[k] == t) <= 2 for (_, sig, _) in faults for t in 'XZ')
    edges = defaultdict(set)
    rel_t = 'Z' if basis == 'Z' else 'X'
    pairs_per_edge = defaultdict(int)
    for (loc, sig, _) in faults:
        part = tuple(sorted(k for k in sig if types[k] == rel_t))
        if part:
            pairs_per_edge[part] += 1
    for (loc, sig, _) in faults:
        for t in 'XZ':
            part = tuple(sorted(k for k in sig if types[k] == t))
            if len(part) == 1:
                edges[(t, part[0], 'B')].add(loc)
            elif len(part) == 2:
                edges[(t, part[0], part[1])].add(loc)
    nbrs = defaultdict(set)
    for (t, a, b) in edges:
        nbrs[(t, a)].add(b)
        if b != 'B':
            nbrs[(t, b)].add(a)
    maxdeg = max(len(v) for v in nbrs.values())
    c = max(len(v) for v in edges.values())
    # exact circuit distance: in the graph of the check type that detects observable-flipping
    # errors, every fault contributes at most one edge (graphlike), so the fewest faults giving
    # an undetected logical is the shortest boundary-to-boundary walk of odd observable parity.
    rel = 'Z' if basis == 'Z' else 'X'
    eobs = defaultdict(set)
    for (loc, sig, ob) in faults:
        part = tuple(sorted(k for k in sig if types[k] == rel))
        if len(part) == 1:
            eobs[(part[0], 'B')].add(ob)
        elif len(part) == 2:
            eobs[part].add(ob)
    adj = defaultdict(list)
    ambiguous = False
    for (a, b), obs in eobs.items():
        if len(obs) == 2:
            ambiguous = True
        for ob in obs:
            adj[a].append((b, ob)); adj[b].append((a, ob))
    from collections import deque
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
    if single_logical:
        exact = 1
    return {'d': d, 'rounds': rounds, 'basis': basis, 'order_x': order_x, 'order_z': order_z,
            'faults': len(faults), 'detectors': len(dets), 'circuit_distance_pairwise_test': dist,
            'circuit_distance_exact': exact, 'ambiguous_edge_observable': ambiguous,
            'single_fault_logicals': len(single_logical), 'equal_signature_logical_pairs': len(pair_logical),
            'graphlike_per_type': graphlike,
            'pauli_resolved_multiplicity_relevant_type': max(pairs_per_edge.values()), 'max_detector_degree': maxdeg, 'edge_multiplicity_c': c,
            'edges': len(edges)}

if __name__ == '__main__':
    d = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    rounds = int(sys.argv[2]) if len(sys.argv) > 2 else d
    out = []
    for name, ox, oz in [('standard (X: Z-shape, Z: N-shape)', ['NW', 'NE', 'SW', 'SE'], ['NW', 'SW', 'NE', 'SE']),
                         ('swapped (X: N-shape, Z: Z-shape)', ['NW', 'SW', 'NE', 'SE'], ['NW', 'NE', 'SW', 'SE'])]:
        for basis in 'ZX':
            r = analyse(d, ox, oz, rounds, basis)
            r['schedule'] = name
            out.append(r)
    print(json.dumps(out, indent=1))
