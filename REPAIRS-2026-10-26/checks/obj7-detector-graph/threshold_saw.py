import sys, json
from collections import defaultdict
D = sys.argv[1]; sys.path.insert(0, D)
import cut_certificate as CC
std = (['NW','NE','SW','SE'], ['NW','SW','NE','SE'])
d = int(sys.argv[2]); basis = sys.argv[3]; mall = int(sys.argv[4]); mbulk = int(sys.argv[5])
f, t, c = CC.memory_faults(d, d, basis, *std)
adj = defaultdict(set)
for (loc, sig, ob) in f:
    part = sorted(k for k in sig if t[k] == basis)
    if len(part) == 2:
        a, b = part; adj[a].add(b); adj[b].add(a)
nodes = sorted(adj)
nb = {v: sorted(adj[v]) for v in nodes}
def count(v, m):
    tot = 0
    stack = [(v, 0, iter(nb[v]))]; onpath = {v}
    while stack:
        u, depth, it = stack[-1]
        if depth == m:
            tot += 1; stack.pop(); onpath.discard(u); continue
        nxt = next(it, None)
        if nxt is None:
            stack.pop(); onpath.discard(u); continue
        if nxt in onpath:
            continue
        onpath.add(nxt); stack.append((nxt, depth + 1, iter(nb[nxt])))
    return tot
maxdeg = max(len(nb[v]) for v in nodes)
cm = max(count(v, mall) for v in nodes)
centre = max(nodes, key=lambda v: len(nb[v]))
bulk = {m: count(centre, m) for m in range(1, mbulk + 1)}
print(json.dumps({'d': d, 'basis': basis, 'vertices': len(nodes), 'max_interior_degree': maxdeg,
                  'm_all': mall, 'c_m_all_vertices': cm, 'Delta_rigorous': cm ** (1 / mall),
                  'bulk_counts': bulk, 'bulk_Delta': {m: bulk[m] ** (1 / m) for m in bulk}}))
