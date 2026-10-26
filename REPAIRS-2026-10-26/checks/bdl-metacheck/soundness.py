#!/usr/bin/env python3
"""Metacheck soundness test on the BDL codes built by bdl.py.

For a check family (rows) and a radius r:
  D     = all dependencies (left kernel);
  D_loc = span of the dependencies supported in radius-r balls of the check graph.
A syndrome s is valid iff s·d = 0 for every d in D. It passes the local metachecks iff s·d = 0 for
every d in D_loc. A dangerous cluster is a connected set of checks that passes every local metacheck
but is invalid. This reports the smallest dangerous cluster found by exhaustive enumeration of
connected sets up to size wmax, for each radius.
"""
import sys, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl

def dot(a, b): return bin(a & b).count('1') & 1

def connected_sets(adj, n, wmax):
    """Connected vertex sets of size ≤ wmax (each once), by canonical extension from the minimum vertex."""
    for v in range(n):
        stack = [(frozenset([v]), frozenset(u for u in adj[v] if u > v))]
        while stack:
            S, ext = stack.pop()
            yield S
            if len(S) == wmax: continue
            ext = set(ext)
            while ext:
                u = ext.pop()
                newext = ext | {w for w in adj[u] if w > v and w not in S and w not in ext}
                stack.append((S | {u}, frozenset(newext)))

def analyse(rows, radius, wmax):
    nd, nl, allk, loc = bdl.metacheck_profile(rows, radius)
    if nd == nl:
        return {'radius': radius, 'deps': nd, 'deps_local': nl, 'all_locally_generated': True}
    D = allk; L = list(loc.values())
    adj = bdl.check_graph(rows)
    best = None; count = 0
    for S in connected_sets(adj, len(rows), wmax):
        s = 0
        for c in S: s |= 1 << c
        if any(dot(s, d) for d in L): continue
        if any(dot(s, d) for d in D):
            count += 1
            if best is None or len(S) < len(best):
                best = sorted(S)
                if len(best) == 1: break
    return {'radius': radius, 'deps': nd, 'deps_local': nl, 'all_locally_generated': False,
            'smallest_dangerous': len(best) if best else None, 'example': best[:12] if best else None}

if __name__ == '__main__':
    a, b, level, wmax = map(int, sys.argv[1:5]); radii = list(map(int, sys.argv[5:]))
    T = bdl.seed_planar(a, b)
    for lev in range(level):
        if lev % 2 == 0:
            D0n, D1n, (n0, n1n, n2) = bdl.RX(T)
        else:
            S = bdl.swap(T); D0s, D1s, (n0s, n1s, n2s) = bdl.RX(S); D0n, D1n, n1n = D1s, D0s, n1s
        T, _ = bdl.to_TSC(D0n, D1n, n1n)
    D0, D1 = bdl.code_of(T)
    for name, rows in (('Zchecks', D1), ('Xchecks', D0)):
        for r in radii:
            print(json.dumps({'level': level, 'family': name, **analyse(rows, r, wmax)}), flush=True)
