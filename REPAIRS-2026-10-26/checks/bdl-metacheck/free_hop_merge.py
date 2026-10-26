#!/usr/bin/env python3
"""Do zero-energy hops change history polymers? (finite check of a claim in the pasted Lemma P)

Uses the full-history representation of history_polymer.py (one R_X / R_Z pair on the 3x2 seed).
For random valid fine syndromes, apply every zero-energy single flip (a qubit whose fine Z-syndrome
has weight 2 with exactly one of the two checks violated), recompute the complete history, and record
how the largest history-polymer size changes. Energy (fine syndrome weight) is unchanged by each move.
"""
import json, random
import coarse as C
from history_polymer import History

def comps(H, fine):
    mid = H.rz(fine); base = H.rx(mid)
    hist = fine | (mid << H.off1) | (base << H.off0)
    return sorted((C.popc(c) for c in H.components(hist)), reverse=True)

def main():
    H = History(3, 2)
    rng = random.Random(7)
    tests = grew = 0; max_jump = 0; example = None; merges = 0
    for _ in range(300):
        sigma = 0
        for j in rng.sample(range(H.nq), rng.choice([2, 4, 8, 16])):
            sigma ^= H.fine_columns[j]
        if not sigma: continue
        before = comps(H, sigma)
        for j, colmask in H.fine_columns.items():
            if C.popc(colmask) != 2 or C.popc(colmask & sigma) != 1: continue
            after_sigma = sigma ^ colmask
            assert C.popc(after_sigma) == C.popc(sigma)
            after = comps(H, after_sigma)
            tests += 1
            if after[0] > before[0]:
                grew += 1
                jump = after[0] - before[0]
                if len(after) < len(before): merges += 1
                if jump > max_jump:
                    max_jump = jump; example = {'before_largest': before[0], 'after_largest': after[0],
                                                'components_before': len(before), 'components_after': len(after)}
    out = {'zero_energy_moves_tested': tests, 'moves_growing_largest_polymer': grew,
           'of_which_merge_components': merges, 'largest_growth_in_one_move': max_jump, 'example': example}
    json.dump(out, open('FREE-HOP-MERGE.json', 'w'), indent=2); print(json.dumps(out))

if __name__ == '__main__':
    main()
