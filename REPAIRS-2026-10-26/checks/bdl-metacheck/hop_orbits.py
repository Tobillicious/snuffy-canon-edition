#!/usr/bin/env python3
"""Zero-energy hopping orbits of a single point defect (not a proof).

A single violated Z-check k moves to k' at zero energy by flipping a qubit with δq = {k, k'}, and is
annihilated downhill by flipping a qubit with δq = {k}. Components of the hop graph (Z-checks,
edges = weight-2 qubits) are the regions a lone defect explores for free; a component containing a
weight-1 qubit has a sink. Reports component sizes, sinks, and the largest sink-free component.
"""
import sys, json
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl, fastbuild as hp

def main(a, b, level):
    (D0, D1), n = hp.build(a, b, level)
    m = len(D1)
    col = defaultdict(list)
    for k, r in enumerate(D1):
        x = r
        while x:
            j = x.bit_length() - 1; x ^= 1 << j; col[j].append(k)
    adj = defaultdict(set); sink = set()
    for j, ks in col.items():
        if len(ks) == 2: adj[ks[0]].add(ks[1]); adj[ks[1]].add(ks[0])
        if len(ks) == 1: sink.add(ks[0])
    seen = set(); comps = []
    for k in range(m):
        if k in seen: continue
        comp, st = {k}, [k]; seen.add(k)
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in seen: seen.add(v); comp.add(v); st.append(v)
        comps.append((len(comp), bool(comp & sink)))
    sizes = sorted((s for s, _ in comps), reverse=True)
    free = sorted((s for s, h in comps if not h), reverse=True)
    print(json.dumps({'seed': [a, b], 'level': level, 'qubits': n, 'zchecks': m,
                      'components': len(comps), 'largest': sizes[:8],
                      'sink_free_components': len(free), 'largest_sink_free': free[:8],
                      'checks_in_sink_free': sum(free)}))

if __name__ == '__main__':
    main(*map(int, sys.argv[1:4]))
