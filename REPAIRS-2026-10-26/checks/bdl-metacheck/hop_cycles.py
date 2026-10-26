#!/usr/bin/env python3
"""(R1) within components and the (R2) escape cost, on the constructed code (finite check).

Hop graph: Z-checks as vertices, an edge per qubit of Z-syndrome weight 2. Its cycle space consists
of X errors with zero Z-syndrome. A fundamental cycle of every non-tree edge is tested for
membership in the X-stabilizer row space (rows of D0); a cycle outside it would be a logical
operator reachable by zero-energy defect motion. Also reports, for a lone defect at each Z-check,
the least energy change of a single flip that moves it out of its hop component
(|δq| − 2 for a qubit q of weight ≥ 3 containing the check).
"""
import sys, json
from collections import defaultdict, deque
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
    adj = defaultdict(list)
    for j, ks in col.items():
        if len(ks) == 2: adj[ks[0]].append((ks[1], j)); adj[ks[1]].append((ks[0], j))
    parent = {}; depth = {}; comp = {}
    for root in range(m):
        if root in parent: continue
        parent[root] = (None, None); depth[root] = 0; comp[root] = root; Q = deque([root])
        while Q:
            u = Q.popleft()
            for v, j in adj[u]:
                if v not in parent:
                    parent[v] = (u, j); depth[v] = depth[u] + 1; comp[v] = root; Q.append(v)
    tree = {j for v, (u, j) in parent.items() if j is not None}
    stab = bdl.rank_and_basis(D0)
    def path_bits(u, v):
        bits = 0
        while u != v:
            if depth[u] < depth[v]: u, v = v, u
            pu, j = parent[u]; bits ^= 1 << j; u = pu
        return bits
    cycles = nontrivial = 0
    for j, ks in col.items():
        if len(ks) != 2 or j in tree: continue
        c = (1 << j) ^ path_bits(ks[0], ks[1])
        cycles += 1
        if bdl.reduce(c, stab): nontrivial += 1
    escape = defaultdict(int)
    for k in range(m):
        costs = [len(col[j]) - 2 for j in range(n) if k in col[j] and len(col[j]) >= 3]
        escape[min(costs) if costs else None] += 1
    print(json.dumps({'seed': [a, b], 'level': level, 'qubits': n, 'zchecks': m,
                      'fundamental_cycles': cycles, 'cycles_not_stabilizers': nontrivial,
                      'least_escape_cost_histogram': {str(k): v for k, v in sorted(escape.items(), key=lambda kv: (kv[0] is None, kv[0]))}}))

if __name__ == '__main__':
    main(*map(int, sys.argv[1:4]))
