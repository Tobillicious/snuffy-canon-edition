#!/usr/bin/env python3
"""Exact finite witnesses for the G.21 residual allowance and gross reset cap.

These checks are separate from the all-level prose derivations, physical
source identification, and unchanged canonical Lean checkpoint.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def joint_kernel_check():
    p = F(1, 64)
    both = p*p/2
    kernel = [1-p+both, p/2-both, p/2-both, both]
    product = [(1-p/2)**2, (p/2)*(1-p/2), (p/2)*(1-p/2), (p/2)**2]
    assert sum(kernel) == sum(product) == 1 and min(kernel) >= 0
    assert both <= p*p and p/2 <= p
    discrepancy = sum(abs(a-b) for a, b in zip(kernel, product))
    assert discrepancy == p*p

    def convolution(a, b):
        return [sum(a[x]*b[x ^ y] for x in range(4)) for y in range(4)]

    # One shared X-X cause and distinct single-port causes. This is a
    # joint law with an exact inverse, rather than a marginal substitution.
    causes = [(1, F(1, 101)), (2, F(1, 211)), (3, F(1, 307))]
    forward, inverse = [F(1), F(0), F(0), F(0)], [F(1), F(0), F(0), F(0)]
    for shift, rate in causes:
        factor, inv = [F(0)]*4, [F(0)]*4
        factor[0], factor[shift] = 1-rate, rate
        inv[0], inv[shift] = (1-rate)/(1-2*rate), -rate/(1-2*rate)
        forward, inverse = convolution(forward, factor), convolution(inverse, inv)
    assert convolution(forward, inverse) == [1, 0, 0, 0]
    marginal_0, marginal_1 = forward[1]+forward[3], forward[2]+forward[3]
    assert forward[3] != marginal_0*marginal_1

    # Any following stochastic channel contracts the full signed l1
    # difference. Check a nontrivial common-cause suffix exactly.
    suffix = [F(5, 8), F(1, 8), F(1, 16), F(3, 16)]
    after = sum(abs(a-b) for a, b in zip(convolution(kernel, suffix),
                                       convolution(product, suffix)))
    assert after <= discrepancy

    # Identical data marginals can hide maximal record discrepancy.
    # These two distributions are the same prepared datum with opposite
    # deterministic retained flags, also for a Bell-correlated datum.
    recorded_0, recorded_1 = [F(1), F(0)], [F(0), F(1)]
    record_l1 = sum(abs(a-b) for a, b in zip(recorded_0, recorded_1))
    assert sum(recorded_0) == sum(recorded_1) and record_l1 == 2
    return {'shared_cause_law_local_stochastic': True,
            'product_marginal_substitution_error_l1': str(discrepancy),
            'joint_cause_inverse_exact': True,
            'suffix_contracts_residual': True,
            'data_only_comparison_misses_record_error': str(record_l1)}


def gross_reset_check():
    energy = F(13, 2)
    # Repeated thermal recrossings have zero signed heat and arbitrarily
    # increasing gross throughput: the old net estimate cannot price them.
    for recrossings in range(1, 33):
        transfers = [energy, -energy]*recrossings
        assert sum(transfers) == 0
        assert sum(abs(v) for v in transfers) == 2*recrossings*energy

    # Enumerate every allowed path of the three-jump reset star. Counter
    # increments are part of the generator, including on a flagged failure.
    paths_checked = 0
    for model in ['reset_star', 'activation_bridge']:
        for initial in range(3):
            frontier = [(initial, 0, 0, F(0))]
            for _ in range(3):
                new_frontier = []
                for state, count, up, gross in frontier:
                    if model == 'reset_star':
                        destinations = [1, 2] if state == 0 else [0]
                        upward = state == 0
                    else:
                        destinations = [0, 1] if state == 2 else [2]
                        upward = state != 2
                    for destination in destinations:
                        item = (destination, count+1, up+upward, gross+energy)
                        new_frontier.append(item)
                        paths_checked += 1
                        assert item[1] <= 3 and item[3] <= 3*energy
                        if item[1] == 3:
                            assert item[2] >= 1
                frontier = new_frontier

    # Uniformisation of the star at total rate 2 nu. Exact discrete
    # distributions verify the cap-event/upward-intensity domination for
    # every initial label; the continuous-time bound is proved in prose.
    fugacity = F(1, 1024)
    for initial in range(3):
        law = {(initial, 0): F(1)}
        expected_up = F(0)
        for tick in range(1, 17):
            next_law = {}
            for (state, count), mass in law.items():
                if count == 3:
                    transitions = [(state, count, F(1), False)]
                elif state == 0:
                    transitions = [(0, count, 1-2*fugacity, False),
                                   (1, count+1, fugacity, True),
                                   (2, count+1, fugacity, True)]
                else:
                    transitions = [(state, count, F(1, 2), False),
                                   (0, count+1, F(1, 2), False)]
                for out, new_count, probability, upward in transitions:
                    key = (out, new_count)
                    next_law[key] = next_law.get(key, F(0))+mass*probability
                    if upward:
                        expected_up += mass*probability
            law = next_law
            cap_mass = sum(mass for (_, count), mass in law.items() if count == 3)
            assert sum(law.values()) == 1
            assert cap_mass <= expected_up <= 2*fugacity*tick
    return {'capped_paths_enumerated': paths_checked,
            'reset_and_activation_caps_checked': True,
            'cap_requires_upward_jump': True,
            'gross_heat_bound_all_capped_paths': '3 E',
            'zero_net_unbounded_recrossing_witnesses': 32,
            'exact_uniformisation_initial_states': 3,
            'exact_uniformisation_steps_per_state': 16}


def allocation_and_translation_check():
    epsilon = F(1, 10**6)
    total = F(0)
    for age in range(65):
        budget = epsilon/F(2**(age+2))
        component = epsilon/F(2**(age+5))
        assert 8*component == budget
        # TV contributes twice its value, inside the same eighth.
        assert 2*(epsilon/F(2**(age+6))) == component
        total += budget
        assert total <= epsilon/2
    witnesses = 0
    for occupied, translation, required in itertools.product(range(16), repeat=3):
        if required & ~(occupied ^ translation) == 0:
            outside_translation = required & ~translation
            assert outside_translation & ~occupied == 0
            witnesses += 1
    # A fixed bounded translation costs a fixed occupation factor.
    R = F(1, 32)
    for size in range(21):
        for footprint in range(4):
            assert R**max(0, size-footprint) <= R**(-footprint)*R**size
    return {'age_allocations_checked': 65, 'eight_terms_equal_original_ceiling': True,
            'residual_TV_allocation_has_factor_two': True,
            'translation_necessary_occupation_cases': witnesses,
            'fixed_translation_prefactor_verified': True}


def main():
    result = {'scope': 'Exact finite residual, record, reset-cap and stage-allocation checks; no installed kernel, all-level proof or Lean compilation.',
              'joint_kernel': joint_kernel_check(),
              'gross_reset': gross_reset_check(),
              'allocation_and_translation': allocation_and_translation_check(),
              'all_exact_checks_pass': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'ENDPOINT-RESIDUAL-EXACT.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
