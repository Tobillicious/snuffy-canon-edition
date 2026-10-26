#!/usr/bin/env python3
"""Resume Claude's unexecuted Dec/Ext test; finite evidence, not an induction.

D[y] contains all valid weight-two syndromes coarse-grained to {y}.  For an
adjacent pair y,z, Z0[y,z] contains weight-four syndromes with coarse support
{y,z}.  Dec asks that each member contain a member of D[y] and one of D[z].
Ext asks that every member of either D set extend to a member of Z0[y,z].

The default enumerates *all* valid weight-four syndromes.  --windows restricts
each pair to the union of the D supports and their one-step check neighbours,
as in Claude's original command, and reports that restriction explicitly.
Witnesses use cell labels as well as run-specific bit indices.
"""
import argparse
from collections import defaultdict
import hashlib
import itertools
import json
import os
from pathlib import Path
import time

import bdl
import coarse as C


def valid_four(cells, signatures):
    """Each increasing quadruple occurs once, via its first and last pairs."""
    bysig = defaultdict(list)
    for i, j in itertools.combinations(cells, 2):
        bysig[signatures[i] ^ signatures[j]].append((i, j))
    for pairs in bysig.values():
        for (i, j), (k, l) in itertools.combinations(pairs, 2):
            if j < k:
                yield (1 << i) | (1 << j) | (1 << k) | (1 << l)


def main(a, b, windows=False):
    start = time.monotonic()
    T = bdl.seed_planar(a, b)
    L = C.Level1(T)
    labels = {i: repr(cell) for cell, i in L.idx2.items()}
    n2 = len(L.idx2)
    signatures = [0] * n2
    for t, dependency in enumerate(bdl.left_kernel(L.D1)):
        for k in C.bits(dependency):
            signatures[k] |= 1 << t

    def support(s):
        return frozenset(z for z, on in L.coarse(s)[0].items() if on)

    def witness(s):
        return {'indices': sorted(C.bits(s)),
                'cells': sorted(labels[k] for k in C.bits(s))}

    D = defaultdict(set)
    for i, j in itertools.combinations(range(n2), 2):
        if signatures[i] != signatures[j]:
            continue
        s = (1 << i) | (1 << j)
        supp = support(s)
        if len(supp) == 1:
            D[next(iter(supp))].add(s)

    adjacent = set()
    for zs in T.adjQZ.values():
        adjacent.update(frozenset(pair) for pair in itertools.combinations(zs, 2))
    targets = sorted(adjacent, key=lambda zs: sorted(map(repr, zs)))
    Z0 = {pair: set() for pair in targets}
    tested = 0
    max_window = n2
    if windows:
        neighbours = bdl.check_graph(L.D1)
        max_window = 0
        for pair in targets:
            seeds = {k for y in pair for s in D[y] for k in C.bits(s)}
            win = sorted(seeds | {j for k in seeds for j in neighbours[k]})
            max_window = max(max_window, len(win))
            for s in valid_four(win, signatures):
                tested += 1
                if support(s) == pair:
                    Z0[pair].add(s)
    else:
        for s in valid_four(range(n2), signatures):
            tested += 1
            supp = support(s)
            if supp in Z0:
                Z0[supp].add(s)
            if tested % 50000 == 0:
                print(json.dumps({'progress_valid_four': tested,
                                  'seconds': round(time.monotonic() - start, 2)}),
                      flush=True)

    pairs_out = []
    examples = {'dec': [], 'ext': [], 'decomposition': [], 'product': []}
    totals = defaultdict(int)
    for pair in targets:
        y, z = sorted(pair, key=repr)
        fibres = Z0[pair]
        products = {A | B for A in D[y] for B in D[z] if not A & B}
        product_fail = products - fibres
        decomp_fail = fibres - products
        dec_fail = []
        for s in sorted(fibres):
            missing = [repr(v) for v in (y, z)
                       if not any(B & s == B for B in D[v])]
            if missing:
                dec_fail.append((s, missing))
        ext_fail = [(v, B) for v in (y, z) for B in sorted(D[v])
                    if not any(B & s == B for s in fibres)]
        counts = {'zero_excess': len(fibres), 'dec_fail': len(dec_fail),
                  'ext_fail': len(ext_fail), 'decomposition_fail': len(decomp_fail),
                  'product_fail': len(product_fail)}
        for k, v in counts.items():
            totals[k] += v
        pairs_out.append({'coarse_pair': [repr(y), repr(z)], **counts})
        for s, missing in dec_fail[:1]:
            if len(examples['dec']) < 4:
                examples['dec'].append({'pair': [repr(y), repr(z)],
                                        'missing_single_defect_subset': missing,
                                        'syndrome': witness(s)})
        for v, B in ext_fail[:1]:
            if len(examples['ext']) < 4:
                examples['ext'].append({'pair': [repr(y), repr(z)],
                                        'unextendible_block_for': repr(v),
                                        'syndrome': witness(B)})
        for kind, failures in [('decomposition', decomp_fail), ('product', product_fail)]:
            if failures and len(examples[kind]) < 4:
                examples[kind].append({'pair': [repr(y), repr(z)],
                                       'syndrome': witness(min(failures))})

    return {'seed': [a, b], 'scope': 'one-step windows' if windows else 'global weight-four',
            'level1_2cells': n2, 'valid_four_tested': tested, 'adjacent_pairs': len(targets),
            'max_window': max_window, 'degenerate_blocks_per_z': {
                repr(z): len(D[z]) for z in sorted(D, key=repr)},
            'totals': dict(totals), 'pairs': pairs_out, 'examples': examples,
            'seconds': round(time.monotonic() - start, 3),
            'pythonhashseed': os.environ.get('PYTHONHASHSEED', 'unset'),
            'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in [Path(__file__), Path(bdl.__file__), Path(C.__file__)]}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    parser.add_argument('--windows', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = main(args.a, args.b, args.windows)
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.output:
        args.output.write_text(encoded)
    print(json.dumps({k: v for k, v in result.items() if k not in ('pairs', 'examples')},
                     ensure_ascii=False), flush=True)
