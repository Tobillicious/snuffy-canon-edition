#!/usr/bin/env python3
"""Exact finite checks for physical Pauli feedback and controller counting.

No installation independence, microscopic primitive or global UPT closure
is inferred from these finite algebra/counting checks.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent


def convolution(a, b):
    return [sum(a[x]*b[x ^ y] for x in range(4)) for y in range(4)]


def feedback_check():
    p = F(1, 2**16)
    decoder = [1-6*p, p, 2*p, 3*p]
    control = []
    slots_x, slots_z = [], []
    for bit in range(2):
        rates = [p*F(1+bit, 6), p*F(2-bit, 6), p*F(3, 6)]
        slots_x.append([1-sum(rates)]+rates)
        slots_z.append([1-sum(rates)]+list(reversed(rates)))
    for m in range(4):
        a, b = p*F(1+(m & 1), 2), p*F(1+(m >> 1), 2)
        control.append([(1-a)*(1-b), a*(1-b), (1-a)*b, a*b])
    endpoint = [F(0)]*4
    patterns = 0
    for m, e, eta, u, v in itertools.product(range(4), repeat=5):
        requested = m ^ eta
        probability = (F(1, 4)*decoder[e]*control[m][eta]
                       *slots_x[requested & 1][u]*slots_z[requested >> 1][v])
        # Actual Pauli propagation: decoder error plus teleportation frame,
        # actual requested correction, and both physical post-slot errors.
        raw_label = e ^ m
        after_x = raw_label ^ (requested & 1) ^ u
        after_z = after_x ^ (requested & 2) ^ v
        assert after_z == e ^ eta ^ u ^ v
        endpoint[after_z] += probability
        patterns += 1
    formula = [F(0)]*4
    for m, e, eta in itertools.product(range(4), repeat=3):
        r = convolution(slots_x[(m ^ eta) & 1], slots_z[(m ^ eta) >> 1])
        for f in range(4):
            formula[e ^ eta ^ f] += F(1, 4)*decoder[e]*control[m][eta]*r[f]
    assert formula == endpoint and sum(endpoint) == 1 and min(endpoint) >= 0
    bound = (1-decoder[0])+max(1-c[0] for c in control)+2*p
    assert 1-endpoint[0] <= bound
    # Shared-cause control: this law is local stochastic at p but is not
    # the product of its marginals. The raw physical witness is two ports.
    marginal, both = p/2, p*p/2
    assert both <= p*p and both != marginal*marginal
    # Check the derived inverse/forward activity threshold exactly.
    t = F(1, 1000)
    pstar = t/(2*(1+t))
    assert 2*pstar/(1-2*pstar) == t
    assert pstar/(1-pstar) <= t
    return {'fault_patterns_checked': patterns,
            'endpoint_I_X_Z_Y': [str(v) for v in endpoint],
            'exact_feedback_formula': True, 'union_rate_bound': True,
            'threshold_inverse_and_forward_bounds': True,
            'shared_cause_local_stochastic_does_not_factor': True}


def connected(mask, n):
    if mask == 0:
        return False
    reached = mask & -mask
    while True:
        expanded = reached | (((reached << 1) | (reached >> 1)) & mask)
        if expanded == reached:
            return reached == mask
        reached = expanded


def log_series(poly, order):
    a = poly+[F(0)]*max(0, order+1-len(poly))
    result = [F(0)]*(order+1)
    for k in range(1, order+1):
        result[k] = a[k]-sum(F(j, k)*result[j]*a[k-j] for j in range(1, k))
    return result


def coefficient_check(n):
    # Signed hard-core singleton polymer gas on a path. This tests the
    # connected-support Mobius/log-coefficient identity used by the bound.
    order = n
    values = {}
    for available in range(1 << n):
        polynomial = [F(0)]*(n+1)
        for occupied in range(1 << n):
            if occupied & ~available or occupied & (occupied << 1):
                continue
            weight = F(1)
            for j in range(n):
                if occupied & (1 << j):
                    weight *= F((-1)**j*(j+1), 256)
            polynomial[bin(occupied).count('1')] += weight
        values[available] = log_series(polynomial, order)
    recovered = [F(0)]*(order+1)
    terms = 0
    for support in range(1, 1 << n):
        if not connected(support, n):
            continue
        size = bin(support).count('1')
        for subset in range(1 << n):
            if subset & ~support:
                continue
            sign = (-1)**(size-bin(subset).count('1'))
            for k in range(size, order+1):
                recovered[k] += sign*values[subset][k]
                terms += 1
    assert recovered == values[(1 << n)-1]
    return {'vertices': n, 'Taylor_order': order,
            'exact_Mobius_terms': terms, 'log_coefficients_match': True}


def main():
    result = {
        'scope': 'Exact finite endpoint algebra and connected-support coefficient checks; no full physical model or canonical Lean audit.',
        'feedback': feedback_check(),
        'counting': [coefficient_check(n) for n in range(2, 7)],
        'all_assertions_pass': True,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE/'ENDPOINT-CONTROLLER-EXACT.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
