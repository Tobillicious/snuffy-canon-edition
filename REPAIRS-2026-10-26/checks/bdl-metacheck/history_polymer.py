#!/usr/bin/env python3
"""Check the full-history constraint graph on actual R_X then R_Z codes.

R_X is the inherited Theorem 4.7 implementation. R_Z is exactly the parity
map of Theorem 4.6, Eq. (131). Constraints retain every intermediate
syndrome. Connected support components must themselves be valid complete
histories. This uses a constraint-scope graph, not the failed D_y products.
"""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import random

import bdl
import coarse as C


class History:
    def __init__(self, a, b):
        self.T0 = bdl.seed_planar(a, b)
        self.L = C.Level1(self.T0)
        T1, big = bdl.to_TSC(self.L.D0, self.L.D1, len(self.L.idx1))
        dual = bdl.swap(T1)
        D0dual, D1dual, dims = bdl.RX(dual)
        self.fine_rows = D0dual  # R_Z swaps the dual R_X checks back.
        self.fine_columns = defaultdict(int)
        for k, row in enumerate(self.fine_rows):
            for j in C.bits(row):
                self.fine_columns[j] |= 1 << k
        self.nz, self.nq = dims[0], dims[1]
        self.nmid = len(self.L.idx2)
        self.base_z = sorted(self.T0.VZ, key=repr)
        self.nbase = len(self.base_z)
        self.off1, self.off0 = self.nz, self.nz + self.nmid
        self.nvars = self.off0 + self.nbase
        self.groups = {}
        index = 0
        for x in dual.VX:
            vertices = bdl.build_Yx(dual, x)[0]
            self.groups[x[1]] = list(range(index, index + len(vertices)))
            index += len(vertices)
        assert index == self.nz
        assert set(self.groups) == set(range(self.nmid))
        self.dependencies = bdl.left_kernel(self.fine_rows)
        self.mid_dependencies = bdl.left_kernel(self.L.D1)
        scopes = []
        # R_Z output is parity on one whole local complex.
        for k, group in self.groups.items():
            scopes.append(set(group) | {self.off1 + k})
        # R_X L1 and L2: each q reads its own region and adjacent x regions.
        xs_for_q = defaultdict(set)
        for x, qs in self.T0.adjXQ.items():
            for q in qs:
                xs_for_q[q].add(x)
        q_scopes = {}
        for mask in self.L.xmask.values():
            scopes.append({self.off1 + i for i in C.bits(mask)})
        for q in self.T0.VQ:
            mask = self.L.qmask[q]
            for x in xs_for_q[q]:
                mask |= self.L.xmask[x]
            q_scopes[q] = mask
            scopes.append({self.off1 + i for i in C.bits(mask)})
        # R_X L3: each z pair reads its two fine bits and incident q scopes.
        for zi, z in enumerate(self.base_z):
            p0, p1 = self.L.pair[z]
            mask = (1 << p0) | (1 << p1)
            for q in self.T0.VQ:
                if z in self.T0.adjQZ[q]:
                    mask |= q_scopes[q]
            scopes.append({self.off1 + i for i in C.bits(mask)} | {self.off0 + zi})
        # The seed validity table has constant scope, even when it is full rank.
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

    def valid(self, sigma):
        return all(C.popc(sigma & d) % 2 == 0 for d in self.dependencies)

    def rz(self, sigma):
        return sum((C.popc(sigma & sum(1 << j for j in group)) % 2) << k
                   for k, group in self.groups.items())

    def rx(self, sigma):
        sp, _ = self.L.coarse(sigma)
        return sum(int(sp[z]) << i for i, z in enumerate(self.base_z))

    def components(self, occupied):
        while occupied:
            first = occupied & -occupied
            occupied ^= first
            frontier, component = first, first
            while frontier:
                neighbours = 0
                for i in C.bits(frontier):
                    neighbours |= self.adj[i]
                frontier = neighbours & occupied
                occupied ^= frontier
                component |= frontier
            yield component

    def check(self, fine):
        assert self.valid(fine)
        mid = self.rz(fine)
        assert C.popc(mid) <= C.popc(fine)
        base = self.rx(mid)
        assert 2 * C.popc(base) <= C.popc(mid)
        history = fine | (mid << self.off1) | (base << self.off0)
        count = 0
        for component in self.components(history):
            f = component & ((1 << self.nz) - 1)
            m = (component >> self.off1) & ((1 << self.nmid) - 1)
            b = component >> self.off0
            assert self.valid(f), 'component must retain all global metachecks'
            assert self.rz(f) == m
            assert self.rx(m) == b
            assert C.popc(component) <= 4 * C.popc(f)
            count += 1
        return count, C.popc(history), C.popc(fine)


def main():
    H = History(3, 2)
    rng = random.Random(20261026)
    cases = components = 0
    max_ratio = 0
    for _ in range(500):
        error_size = rng.choice([1, 2, 4, 8, 16, 32, 64])
        sigma = 0
        for j in rng.sample(range(H.nq), error_size):
            sigma ^= H.fine_columns[j]
        count, occupied, energy = H.check(sigma)
        cases += 1
        components += count
        if energy:
            max_ratio = max(max_ratio, occupied / energy)
    # The original non-product witness remains valid and becomes one or
    # more coupled history polymers, without requiring a D_y decomposition.
    old = json.loads(Path('TRANSPORT-3x2-GLOBAL.json').read_text())
    witnesses = 0
    for example in old['examples']['dec']:
        mid = sum(1 << i for i in example['syndrome']['indices'])
        fine = sum(1 << H.groups[k][0] for k in C.bits(mid))
        H.check(fine)
        witnesses += 1
    # Check that local reduction plus seed validity characterizes the full
    # syndrome space, including randomly generated invalid assignments.
    arbitrary = invalid = 0
    for _ in range(500):
        fine = sum(1 << i for i in rng.sample(range(H.nz), rng.choice([1, 2, 4, 8, 16])))
        mid = H.rz(fine)
        try:
            H.rx(mid)
            accepted = True
        except AssertionError:
            accepted = False
        assert accepted == H.valid(fine)
        arbitrary += 1
        invalid += not accepted
    result = {'scope': 'finite source-correspondence check: one R_X / R_Z pair',
              **H.stats, 'valid_histories_checked': cases,
              'standalone_components_checked': components,
              'max_observed_history_to_finest_weight': max_ratio,
              'old_Dec_witnesses_checked': witnesses,
              'arbitrary_assignments_checked': arbitrary,
              'arbitrary_invalid_rejected': invalid,
              'all_assertions_pass': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path('HISTORY-POLYMER-PAIR-CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
