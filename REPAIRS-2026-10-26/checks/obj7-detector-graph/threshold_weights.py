import sys, json
from collections import defaultdict
D = sys.argv[1]; sys.path.insert(0, D)
import detector_graph as DG, cut_certificate as CC, merge_graph as MG
std = (['NW','NE','SW','SE'], ['NW','SW','NE','SE'])
W = {'CX': 1/15, 'R': 1/3, 'H': 1/3, 'I': 1/3, 'M': 1.0}
def weighted(faults, types, ops, rel):
    q = defaultdict(float); cnt = defaultdict(int)
    for (loc, sig, ob) in faults:
        part = tuple(sorted(k for k in sig if types[k] == rel))
        if part:
            q[part] += W[ops[loc][0]]; cnt[part] += 1
    return max(q.values()), max(cnt.values())
out = []
for d in map(int, sys.argv[2:]):
    for basis in 'ZX':
        f, t, c = CC.memory_faults(d, d, basis, *std)
        checks, ops, meas = DG.build(d, *std, d, basis)
        qm, cm = weighted(f, t, ops, basis)
        out.append(dict(kind='memory', d=d, basis=basis, c_weighted=qm, c_count=cm))
    ops2 = MG.build_merge(d, d, 'X', *std)[0]
    f, t, c = CC.merge_faults(d, d, 'X', *std)
    qm, cm = weighted(f, t, ops2, 'X')
    out.append(dict(kind='merge', d=d, T=d, basis='X', c_weighted=qm, c_count=cm))
print(json.dumps(out))
