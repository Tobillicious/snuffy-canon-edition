#!/usr/bin/env python3
"""Exact checks of claims in the current noisy-holding submission.

These verify arithmetic and delimit a model-specific obstruction. They do
not assert a BDL physical holding theorem.
"""
from fractions import Fraction as F
import json
from pathlib import Path

errors = {1: F(1, 4)}
for j in range(1, 20):
    errors[j + 1] = errors[j] / 2 + F(1, 2 ** (j + 2))
for j, value in errors.items():
    assert value == F(j, 2 ** (j + 1))
assert errors[2] > F(1, 2 ** 3)

repaired = {1: F(1, 4)}
for j in range(1, 20):
    repaired[j + 1] = repaired[j] / 4 + F(1, 2 ** (j + 3))
    assert repaired[j + 1] <= F(1, 2 ** (j + 2))

work = []
for depth in (4, 8, 16):
    n = 2 ** depth
    total = sum((n // 2 ** k) * (depth - k) for k in range(depth))
    assert total == (depth - 1) * 2 ** (depth + 1) + 2
    work.append({'n': n, 'depth': depth, 'work': total,
                 'work_per_fine_node': str(F(total, n))})

# Known independent bit-flip noise can be compensated in a product model
# with fixed parameters. This does not supply the unknown/correlated BDL
# device certificate, nor refute a theorem with p above its stated threshold.
p, q = F(1, 16), F(1, 4)
r = (q - p) / (1 - 2 * p)
assert 0 < r < 1
actual = r * (1 - p) + (1 - r) * p
assert actual == q

# One fault can occupy w checks at once. An input occupation estimate must
# retain the fault footprint; a uniform power p^|A| is not automatic.
fault, thermal, footprint = F(1, 100), F(1, 1000), 3
all_occupied = (1 - fault) * thermal ** footprint + fault * (1 - thermal) ** footprint
naive = (fault + thermal) ** footprint
assert all_occupied > naive

result = {
    'recurrence_submission': {'first_failing_level': 2, 'actual_error': str(errors[2]),
                              'claimed_bound': str(F(1, 8)),
                              'exact_solution': 'e_j = j epsilon / 2^(j+1)'},
    'conditional_repaired_budget': 'K<=1/4 and delta_j<=epsilon/2^(j+3) preserve the claimed bound; physical estimates still required',
    'geometric_work_examples': work,
    'known_product_noise_example': {'noise_p': str(p), 'target_q': str(q),
                                    'input_r': str(r), 'output_q': str(actual),
                                    'density_factor': '1 for every product size'},
    'fault_footprint_example': {'footprint': footprint, 'probability_all_occupied': str(all_occupied),
                               'naive_rate_to_footprint_power': str(naive)},
    'all_exact_checks_pass': True,
    'scope': 'finite arithmetic and examples; no physical BDL closure claimed'}
out = Path(__file__).with_name('NOISY-JOIN-ARITHMETIC.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'all_exact_checks_pass': True, 'result': str(out)}))
