#!/usr/bin/env python3
"""Exact counterchecks for the newly supplied G3 arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def main():
    # d=1, alpha=beta=1, t=10.
    actual = 20
    proposed = 10 + 2
    assert actual > proposed

    # One realised reset need not be bounded by its expected cost.
    reset_cost, failure_probability = F(7), F(1, 4)
    assert reset_cost > reset_cost * failure_probability

    # Exact tail identity sum_{k>=1} k^3 q^k.
    q = F(1, 2)
    exact_series = q * (1 + 4*q + q*q) / (1-q)**4
    assert exact_series == 26
    # ln2=2 sum_{r>=0} 1/[(2r+1)3^(2r+1)]; positive omitted tail.
    log2_lower = sum(F(2, (2*r+1)*3**(2*r+1)) for r in range(5))
    assert log2_lower**4 > F(3, 13)
    assert 6 / log2_lower**4 < exact_series

    box, boundary = 5**3, 5**3 - 3**3
    assert box == 125 and boundary == 98 and boundary != box
    source = Path(__file__)
    result = {
        'scope': 'exact arithmetic checks of candidate G3 draft; not a physical completion verdict',
        'd1_active_sum_counterexample': {'actual':actual,'proposed_bound':proposed},
        'realised_reset_vs_expectation': {'realised':str(reset_cost),'expected':str(reset_cost*failure_probability)},
        'integral_only_series_bound_counterexample': {
            'dimension':4,'lambda':'ln 2','exact_series':str(exact_series),
            'ln2_strict_rational_lower_bound':str(log2_lower),
            'six_over_lower_bound_fourth_is_less_than_26':True,
        },
        'box_and_boundary_distinguished': {'box':box,'boundary':boundary},
        'all_assertions_pass': True,
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    }
    source.with_name('G3-HOSTILE-ARITHMETIC.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__ == '__main__':
    main()
