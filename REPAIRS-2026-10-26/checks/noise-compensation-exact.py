#!/usr/bin/env python3
"""Exact residual-noise compensation on existing finite BDL seed matrices.

This checks a specified independent depolarizing output-channel model. It
does not identify the noise of the full physical preparation circuit.
"""
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
MODEL = HERE / "bdl-metacheck"
sys.path.insert(0, str(MODEL))
import fastbuild
import bdl


def weight(value):
    return bin(value).count("1")


def span(generators):
    result = {0}
    for generator in generators:
        result.update([value ^ generator for value in tuple(result)])
    return sorted(result)


def noise_step(law, a, b, rate):
    third = rate / 3
    return {
        s: (1 - rate) * law[s]
        + third * (law[s ^ a] + law[s ^ b] + law[s ^ a ^ b])
        for s in law
    }


def inverse_step(law, a, b, rate):
    denominator = 1 - 4 * rate / 3
    assert denominator > 0
    return {
        s: ((1 - rate / 3) * law[s]
            - (rate / 3) * (law[s ^ a] + law[s ^ b] + law[s ^ a ^ b]))
        / denominator
        for s in law
    }


def swap_channel_check(rate):
    """All 16^3 independent Pauli fault patterns of the actual 3-CNOT swap."""
    def cnot(pauli, control, target):
        x = pauli & 3
        z = pauli >> 2
        if x & (1 << control):
            x ^= 1 << target
        if z & (1 << target):
            z ^= 1 << control
        return x | (z << 2)

    probabilities = [1 - rate] + [rate / 15] * 15
    output = [Fraction(0) for _ in range(4)]
    counts = [[0 for _ in range(4)] for _ in range(4)]
    patterns = 0
    for first in range(16):
        for second in range(16):
            for third in range(16):
                final = cnot(cnot(first, 1, 0) ^ second, 0, 1) ^ third
                target = ((final >> 1) & 1) | (((final >> 3) & 1) << 1)
                output[target] += probabilities[first] * probabilities[second] * probabilities[third]
                counts[target][sum(value != 0 for value in [first, second, third])] += 1
                patterns += 1
    effective = Fraction(3, 4) * (1 - (1 - Fraction(16, 15) * rate) ** 3)
    assert output == [1 - effective, effective / 3, effective / 3, effective / 3]
    assert counts == [[1, 9, 171, 843], [0, 12, 168, 844],
                      [0, 12, 168, 844], [0, 12, 168, 844]]
    return {
        "circuit": "CNOT(0,1), CNOT(1,0), CNOT(0,1)",
        "noise": "independent two-qubit Pauli depolarization after each CNOT",
        "fault_patterns_enumerated": patterns,
        "fault_weight_counts_by_target_Pauli": counts,
        "per_CNOT_nonidentity_rate": str(rate),
        "target_output_Pauli_probabilities": [str(value) for value in output],
        "effective_single_qubit_rate": str(effective),
        "effective_rate_formula": "(3/4)*(1-(1-16*p/15)^3)",
        "exact_formula_verified": True,
    }


def logical_reference_check(xchecks, zchecks, columns, compensated, target, rate, qubits):
    """Track the induced logical Pauli channel, rather than just its syndrome."""
    def parity(value):
        return weight(value) % 2

    def logical_vector(commutes, stabilizers):
        basis = bdl.rank_and_basis(stabilizers)
        candidates = sorted(range(1, 1 << qubits), key=lambda value: (weight(value), value))
        return next(value for value in candidates
                    if all(parity(value & row) == 0 for row in commutes)
                    and bdl.reduce(value, basis) != 0)

    logical_z = logical_vector(xchecks, zchecks)
    logical_x = logical_vector(zchecks, xchecks)
    assert parity(logical_x & logical_z) == 1

    def correction_bits(checks, logical):
        result = {}
        for error in sorted(range(1 << qubits), key=lambda value: (weight(value), value)):
            syndrome = sum(parity(error & row) << k for k, row in enumerate(checks))
            result.setdefault(syndrome, parity(error & logical))
        return result

    correct_x = correction_bits(zchecks, logical_z)
    correct_z = correction_bits(xchecks, logical_x)
    m = len(xchecks) + len(zchecks)
    lower_mask = (1 << len(zchecks)) - 1

    def decoder_label(syndrome):
        return correct_x[syndrome & lower_mask] | (correct_z[syndrome >> len(zchecks)] << 1)

    jumps = []
    for qubit, (a, b) in enumerate(columns):
        jumps.append((a | (parity((1 << qubit) & logical_z) << m),
                      b | (parity((1 << qubit) & logical_x) << (m + 1))))
    bad = {s for s in target if any(
        decoder_label(s) ^ decoder_label(s ^ shift) ^ logical
        for (a, b), (la, lb) in zip(columns, jumps)
        for shift, logical in [(a, la >> m), (b, lb >> m), (a ^ b, (la ^ lb) >> m)])}
    initial = {s | (logical << m): Fraction(0) for s in target for logical in range(4)}
    for s, probability in compensated.items():
        initial[s | (decoder_label(s) << m)] = probability
    current = dict(initial)
    syndrome_law = dict(compensated)
    union_bound = Fraction(0)
    for (a, b), (la, lb) in zip(columns, jumps):
        union_bound += rate * sum(syndrome_law[s] for s in bad)
        current = noise_step(current, la, lb, rate)
        syndrome_law = noise_step(syndrome_law, a, b, rate)
        assert all(value >= 0 for value in syndrome_law.values())
    marginal = {s: sum(current[s | (logical << m)] for logical in range(4)) for s in target}
    assert marginal == target
    logical_law = [Fraction(0) for _ in range(4)]
    for label, probability in current.items():
        syndrome = label & ((1 << m) - 1)
        error = (label >> m) ^ decoder_label(syndrome)
        logical_law[error] += probability
    assert sum(logical_law) == 1
    assert all(value >= 0 for value in logical_law)
    failure = sum(logical_law[1:])
    assert failure > 0
    assert failure <= union_bound
    return {
        "logical_Pauli_weights": [str(value) for value in logical_law],
        "initial_logical_error_probability": str(failure),
        "bad_transition_union_bound": str(union_bound),
        "logical_error_bounded_by_actual_intermediate_bad_weights": True,
        "Bell_reference_trace_distance": str(2 * failure),
        "thermal_syndrome_does_not_alone_make_initial_logical_error_zero": True,
    }


def parity_constraint_check():
    """Exercise a global syndrome constraint absent from the independent seed checks."""
    checks = 8
    columns = [((1 << i) | (1 << ((i + 1) % checks)), 0) for i in range(checks)]
    states = span([a for a, _ in columns])
    assert states == [s for s in range(1 << checks) if weight(s) % 2 == 0]
    fugacity, rate = Fraction(1, 8), Fraction(1, 2**24)
    raw = {s: fugacity ** weight(s) for s in states}
    partition = sum(raw.values())
    target = {s: value / partition for s, value in raw.items()}
    compensated = dict(target)
    for a, b in reversed(columns):
        compensated = inverse_step(compensated, a, b, rate)
    assert all(value > 0 for value in compensated.values())
    assert sum(compensated.values()) == 1
    for a, b in columns:
        compensated = noise_step(compensated, a, b, rate)
    assert compensated == target
    return {
        "scope": "Eight-check even-parity syndrome control, not a BDL lifetime test.",
        "valid_syndromes": len(states), "global_parity_constraint_preserved": True,
        "inverse_nonnegative": True, "exact_noise_inverse_identity": True,
    }


def run_case(seed, fugacity, rate, expected_positive, label):
    (xchecks, zchecks), qubits = fastbuild.build(*seed, 0)
    columns = []
    for qubit in range(qubits):
        xerror = sum(((row >> qubit) & 1) << k for k, row in enumerate(zchecks))
        zerror = sum(((row >> qubit) & 1) << (k + len(zchecks))
                     for k, row in enumerate(xchecks))
        columns.append((xerror, zerror))
    states = span([column for pair in columns for column in pair])
    raw = {s: fugacity ** weight(s) for s in states}
    partition = sum(raw.values())
    target = {s: value / partition for s, value in raw.items()}
    compensated = dict(target)
    for a, b in reversed(columns):
        compensated = inverse_step(compensated, a, b, rate)
    recovered = dict(compensated)
    for a, b in columns:
        recovered = noise_step(recovered, a, b, rate)
    positive = all(value >= 0 for value in compensated.values())
    assert positive == expected_positive, label
    assert sum(compensated.values()) == 1
    assert recovered == target
    result = {
        "label": label, "seed": list(seed), "construction_level": 0,
        "physical_qubits": qubits, "joint_valid_CSS_syndromes": len(states),
        "fugacity": str(fugacity), "depolarizing_rate": str(rate),
        "inverse_mass_exactly_one": True,
        "inverse_nonnegative": positive,
        "exact_noise_inverse_identity": True,
        "negative_entries": sum(value < 0 for value in compensated.values()),
    }
    if positive:
        kept = [s for s in states if not s & 1]
        mass = sum(compensated[s] for s in kept)
        assert mass >= Fraction(1, 2)
        approximate = {s: compensated[s] / mass if s in kept else Fraction(0)
                       for s in states}
        assert sum(approximate.values()) == 1
        assert all(approximate[s] <= 2 * compensated[s] for s in states)
        for a, b in columns:
            approximate = noise_step(approximate, a, b, rate)
        assert all(approximate[s] <= 2 * target[s] for s in states)
        result["conditioned_input_mass_at_least_half"] = True
        result["one_sided_factor_two_survives_physical_noise"] = True
        if label == "five-qubit seed":
            result["logical_reference_check"] = logical_reference_check(
                xchecks, zchecks, columns, compensated, target, rate, qubits)
    return result


def main():
    assert os.environ.get("PYTHONHASHSEED") == "0", "Use PYTHONHASHSEED=0"
    cases = [
        ((2, 1), Fraction(1, 8), Fraction(1, 2**18), True, "five-qubit seed"),
        ((3, 2), Fraction(1, 8), Fraction(1, 2**18), True, "thirteen-qubit seed"),
        ((2, 1), Fraction(1, 2**128), Fraction(1, 2**1024), True,
         "very small fugacity and noise"),
        ((2, 1), Fraction(1, 8), Fraction(1, 4), False,
         "inverse positivity must be proved, not assumed"),
    ]
    results = []
    for args in cases:
        result = run_case(*args)
        results.append(result)
        print(json.dumps({"case": result["label"], "states": result["joint_valid_CSS_syndromes"],
                          "nonnegative": result["inverse_nonnegative"],
                          "exact_Nq_equals_target": True}), flush=True)
    receipt = {
        "scope": "Exact finite checks for a specified independent local Pauli output channel; not full circuit identification or all-level verification.",
        "cases": results, "all_assertions_pass": True,
        "actual_three_CNOT_handoff_channel": swap_channel_check(Fraction(1, 2**18)),
        "global_constraint_control": parity_constraint_check(),
        "source_sha256": {str(p.relative_to(HERE)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in [Path(__file__), MODEL / "bdl.py", MODEL / "fastbuild.py"]},
    }
    (HERE / "NOISE-COMPENSATION-EXACT.json").write_text(json.dumps(receipt, indent=2) + "\n")


if __name__ == "__main__":
    main()
