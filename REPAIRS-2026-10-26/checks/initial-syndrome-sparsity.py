#!/usr/bin/env python3
"""Exact finite cross-check of the new initial-syndrome bound, not dynamics."""
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


def subspaces(m):
    spaces = {frozenset({0})}
    frontier = list(spaces)
    while frontier:
        current = frontier.pop()
        for v in range(1 << m):
            if v in current:
                continue
            extended = current | frozenset(x ^ v for x in current)
            if extended not in spaces:
                spaces.add(extended)
                frontier.append(extended)
    return sorted(spaces, key=lambda s: (len(s), sorted(s)))


def main():
    fugacities = [Fraction(0), Fraction(1, 16), Fraction(1, 4), Fraction(1, 2), Fraction(1)]
    cosets_checked = occupation_checks = spaces_checked = 0
    dimension_counts = {}
    for m in range(6):
        spaces = subspaces(m)
        dimension_counts[str(m)] = len(spaces)
        spaces_checked += len(spaces)
        for space in spaces:
            for z in fugacities:
                weights = {s: z ** bin(s).count('1') for s in space}
                partition = sum(weights.values())
                for v in range(1 << m):
                    coset = sum(z ** bin(s ^ v).count('1') for s in space)
                    assert coset <= partition, (m, space, z, v)
                    cosets_checked += 1
                for mask in range(1 << m):
                    mass = sum(w for s, w in weights.items() if s & mask == mask)
                    assert mass <= z ** bin(mask).count('1') * partition, (m, space, z, mask)
                    occupation_checks += 1

    # Two independent physical faults, each with a two-check footprint.
    # The syndrome space includes their images. Thermal coordinates retain
    # a global parity relation. The output law is computed, not assigned.
    code = frozenset({0, 3, 5, 6})
    z, p = Fraction(1, 16), Fraction(1, 256)
    q = Fraction(1, 8)  # ell=2, w=2, hence ell*sqrt(p)=1/8.
    partition = sum(z ** bin(s).count('1') for s in code)
    output = {s: Fraction(0) for s in code}
    footprint_checks = 0
    for f0, f1 in itertools.product([0, 1], repeat=2):
        probability = p ** (f0 + f1) * (1 - p) ** (2 - f0 - f1)
        fault_syndrome = (3 if f0 else 0) ^ (6 if f1 else 0)
        for s in code:
            output[s ^ fault_syndrome] += probability * z ** bin(s).count('1') / partition
    assert sum(output.values()) == 1
    for mask in range(8):
        mass = sum(w for s, w in output.items() if s & mask == mask)
        assert mass <= (z + q) ** bin(mask).count('1')
        footprint_checks += 1

    here = Path(__file__)
    result = {
        'scope': 'exact finite initial-law cross-check; not a dynamics or logical-recovery certificate',
        'ambient_dimensions': [0, 1, 2, 3, 4, 5],
        'subspace_counts': dimension_counts,
        'subspaces_checked': spaces_checked,
        'coset_maximum_checks': cosets_checked,
        'joint_occupation_checks': occupation_checks,
        'correlated_fault_footprint_convolution_checks': footprint_checks,
        'fugacities': [str(z) for z in fugacities],
        'all_assertions_pass': True,
        'source_sha256': hashlib.sha256(here.read_bytes()).hexdigest(),
    }
    here.with_name('INITIAL-SYNDROME-SPARSITY.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
