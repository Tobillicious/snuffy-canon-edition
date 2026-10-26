import sys
from collections import defaultdict
D = sys.argv[1]; sys.path.insert(0, D)
import cut_certificate as CC
std = (['NW','NE','SW','SE'], ['NW','SW','NE','SE'])
d = int(sys.argv[2]); basis = sys.argv[3]
f, t, c = CC.memory_faults(d, d, basis, *std)
adj = defaultdict(set)
for (loc, sig, ob) in f:
    part = sorted(k for k in sig if t[k] == basis)
    if len(part) == 2:
        a, b = part; adj[a].add(b); adj[b].add(a)
nodes = sorted(adj); idx = {v: i for i, v in enumerate(nodes)}
print(len(nodes))
for v in nodes:
    print(len(adj[v]), *[idx[u] for u in sorted(adj[v])])
