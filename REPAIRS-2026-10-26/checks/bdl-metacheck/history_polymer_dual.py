#!/usr/bin/env python3
"""Opposite CSS sector of the same two-level code checked by history_polymer.

Duality turns R_Z(R_X(T)) into R_X(R_Z(dual(T))). This implementation uses
the same source matrices and checks the reversed sequence explicitly.
"""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import random

import bdl
import coarse as C
from history_polymer import History


class DualHistory(History):
    def __init__(self, a=3, b=2):
        seed = bdl.seed_planar(a, b)
        first = C.Level1(seed)
        T1, big = bdl.to_TSC(first.D0, first.D1, len(first.idx1))
        self.L = C.Level1(bdl.swap(T1))
        self.fine_rows = self.L.D1
        self.fine_columns = self.L.col
        self.nz = len(self.fine_rows)
        self.nq = len(self.L.idx1)
        self.nmid = len(first.D0)
        self.nbase = len(seed.VX)
        self.off1, self.off0 = self.nz, self.nz + self.nmid
        self.nvars = self.off0 + self.nbase
        self.dependencies = bdl.left_kernel(self.fine_rows)
        self.rx_order = list(self.L.T.VZ)
        self.groups = {}
        index = 0
        for k, x in enumerate(seed.VX):
            vertices = first.Yx[x][0]
            self.groups[k] = list(range(index, index + len(vertices)))
            index += len(vertices)
        assert index == self.nmid
        scopes = []
        T = self.L.T
        xs_for_q = defaultdict(set)
        for x, qs in T.adjXQ.items():
            for q in qs:
                xs_for_q[q].add(x)
        q_scopes = {}
        for mask in self.L.xmask.values():
            scopes.append(set(C.bits(mask)))
        for q in T.VQ:
            mask = self.L.qmask[q]
            for x in xs_for_q[q]:
                mask |= self.L.xmask[x]
            q_scopes[q] = mask
            scopes.append(set(C.bits(mask)))
        for zi, z in enumerate(self.rx_order):
            p0, p1 = self.L.pair[z]
            mask = (1 << p0) | (1 << p1)
            for q in T.VQ:
                if z in T.adjQZ[q]:
                    mask |= q_scopes[q]
            scopes.append(set(C.bits(mask)) | {self.off1 + zi})
        for k, group in self.groups.items():
            scopes.append({self.off1 + i for i in group} | {self.off0 + k})
        scopes.append(set(range(self.off0, self.nvars)))
        self.adj = [0] * self.nvars
        for scope in scopes:
            mask = sum(1 << i for i in scope)
            for i in scope:
                self.adj[i] |= mask ^ (1 << i)
        self.stats = {'variables': self.nvars, 'finest_checks': self.nz,
                      'intermediate_checks': self.nmid, 'seed_checks': self.nbase,
                      'constraint_scopes': len(scopes), 'max_scope': max(map(len, scopes)),
                      'max_degree': max(map(C.popc, self.adj)),
                      'T1_square_pairs_with_more_than_two_shared_qubits': big}

    def rx(self, sigma):
        sp, _ = self.L.coarse(sigma)
        return sum(int(sp[z]) << i for i, z in enumerate(self.rx_order))

    def check(self, fine):
        assert self.valid(fine)
        mid = self.rx(fine)
        assert 2 * C.popc(mid) <= C.popc(fine)
        base = self.rz(mid)
        assert C.popc(base) <= C.popc(mid)
        history = fine | (mid << self.off1) | (base << self.off0)
        count = 0
        for component in self.components(history):
            f = component & ((1 << self.nz) - 1)
            m = (component >> self.off1) & ((1 << self.nmid) - 1)
            b = component >> self.off0
            assert self.valid(f)
            assert self.rx(f) == m
            assert self.rz(m) == b
            assert C.popc(component) <= 4 * C.popc(f)
            count += 1
        return count, C.popc(history), C.popc(fine)


def main():
    H = DualHistory()
    rng = random.Random(20261027)
    components = 0
    max_ratio = 0
    for _ in range(500):
        fine = 0
        for j in rng.sample(range(H.nq), rng.choice([1, 2, 4, 8, 16, 32, 64])):
            fine ^= H.fine_columns[j]
        count, occupied, energy = H.check(fine)
        components += count
        if energy:
            max_ratio = max(max_ratio, occupied / energy)
    result = {'scope': 'finite source-correspondence check: opposite CSS sector of the same code',
              **H.stats, 'valid_histories_checked': 500,
              'standalone_components_checked': components,
              'max_observed_history_to_finest_weight': max_ratio,
              'all_assertions_pass': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path('HISTORY-POLYMER-DUAL-CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
