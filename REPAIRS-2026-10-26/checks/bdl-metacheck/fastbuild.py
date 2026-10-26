#!/usr/bin/env python3
"""Faster level construction for the BDL codes: the same complexes as bdl.py, with code_of and the
per-x star scan done from adjacency instead of all-pairs loops (needed at level 3)."""
import sys
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import bdl

def code_of(T):
    qi = {q: j for j, q in enumerate(T.VQ)}
    zi = {z: k for k, z in enumerate(T.VZ)}
    D0 = []
    for x in T.VX:
        r = 0
        for q in T.adjXQ[x]: r |= 1 << qi[q]
        D0.append(r)
    D1 = [0] * len(T.VZ)
    for q, zs in T.adjQZ.items():
        for z in zs: D1[zi[z]] |= 1 << qi[q]
    return D0, D1

def patch_star_scan():
    """bdl.cells_of_star_x scans every square for each x; index squares by x once per complex."""
    cache = {'T': None, 'by': None}
    def fast(T, x):
        if cache['T'] is not T:          # identity of the live object, never a reused id
            by = defaultdict(list)
            for s in T.squares: by[s[0]].append(s)
            cache['T'], cache['by'] = T, by
        by = cache['by']
        verts, edges, faces = set(), set(), []
        for s in by[x]:
            xx, q, z, q2 = s
            verts |= {xx, q, z, q2}
            es = [frozenset((xx, q)), frozenset((q, z)), frozenset((z, q2)), frozenset((q2, xx))]
            edges |= set(es); faces.append((s, es))
        bedges = {e for e in edges if x not in e}
        bverts = set().union(*bedges) if bedges else set()
        return verts, edges, faces, bverts, bedges
    bdl.cells_of_star_x = fast

def build(a, b, level):
    patch_star_scan()
    T = bdl.seed_planar(a, b)
    for lev in range(level):
        if lev % 2 == 0:
            D0n, D1n, (n0, n1n, n2) = bdl.RX(T)
        else:
            S = bdl.swap(T); D0s, D1s, (n0s, n1s, n2s) = bdl.RX(S); D0n, D1n, n1n = D1s, D0s, n1s
        T, _ = bdl.to_TSC(D0n, D1n, n1n)
    return code_of(T), len(T.VQ)
