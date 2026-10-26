#!/usr/bin/env python3
"""Verify the stated delta_joint certificates without touching Checkpoint 12.

General analytical proofs are in DELTA-JOINT-CERTIFICATES-PROOF-2026-10-27.md.
Fraction checks certify finite threshold arithmetic; complete matrix-unit
checks use floating point and are not formal diamond-norm computations.
No installation path law or generator bound is supplied by these examples.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import numpy as np

HERE = Path(__file__).resolve().parent
BANK = HERE.parent
ROOT = BANK.parent
CANON = ROOT/'CANON-EDITION-V4.2-WORKING'
PROOF = BANK/'DELTA-JOINT-CERTIFICATES-PROOF-2026-10-27.md'
RECEIPT = HERE/'DELTA-JOINT-VERIFICATION-2026-10-27.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stage_budget(age, epsilon):
    if type(age) is not int or age < 0:
        raise ValueError('age must be a nonnegative integer')
    if not isinstance(epsilon, F) or not 0 < epsilon <= 1:
        raise ValueError('epsilon must be an exact Fraction in (0,1]')
    return epsilon/F(2**(age+5))


def kernel_variation(actual, nominal):
    if not actual or len(actual) != len(nominal):
        raise ValueError('joint laws must have the same nonempty path set')
    for law in [actual, nominal]:
        if not all(isinstance(value, F) and value >= 0 for value in law):
            raise ValueError('path masses must be nonnegative exact Fractions')
        if sum(law) != 1:
            raise ValueError('each complete joint path law must sum to one')
    return sum(abs(p-q) for p, q in zip(actual, nominal))/2


def discrete_certificate(actual, nominal, age, epsilon):
    """Sufficient predicate, conditional on common input-independent branches."""
    return 2*kernel_variation(actual, nominal) <= stage_budget(age, epsilon)


def continuous_certificate(rate_bound, exposure, age, epsilon):
    """Sufficient predicate for a verified uniform joint generator norm bound."""
    if not isinstance(rate_bound, F) or rate_bound < 0:
        raise ValueError('rate_bound must be a nonnegative exact Fraction')
    if not isinstance(exposure, F) or exposure < 0:
        raise ValueError('exposure must be a nonnegative exact Fraction')
    return exposure*rate_bound <= stage_budget(age, epsilon)


def exact_threshold_checks():
    ages = list(range(257))+[512, 1024]
    tolerances = [F(1), F(1, 2), F(1, 10**6), F(1, 10**12),
                  F(1, 10**30), F(1, 2**100), F(1, 10**100)]
    scales = [F(0), F(1, 2), F(1), F(1)+F(1, 2**20), F(2)]
    decisions = {'discrete_accept': 0, 'discrete_reject': 0,
                 'continuous_accept': 0, 'continuous_reject': 0}
    short_exposure_cases = 0
    for age in ages:
        exposure = F(2**age)
        for epsilon in tolerances:
            budget = stage_budget(age, epsilon)
            threshold = epsilon/F(2**(2*age+5))
            assert exposure*threshold == budget
            for scale in scales:
                shift = scale*budget/2
                nominal = [F(1, 4)]*4
                actual = [F(1, 4)+shift, F(1, 4)-shift, F(1, 4), F(1, 4)]
                variation = kernel_variation(actual, nominal)
                assert variation == shift
                accepted = discrete_certificate(actual, nominal, age, epsilon)
                assert accepted == (scale <= 1)
                assert accepted == (variation <= epsilon/F(2**(age+6)))
                decisions['discrete_accept' if accepted else 'discrete_reject'] += 1

                rate = scale*threshold
                accepted = continuous_certificate(rate, exposure, age, epsilon)
                assert accepted == (rate <= epsilon/F(2**(2*age+5)))
                assert accepted == (scale <= 1)
                assert exposure*rate == scale*budget
                decisions['continuous_accept' if accepted else 'continuous_reject'] += 1

            # The full holding duration is not imposed on a short endpoint.
            short = F((age+1)**2)
            short_rate = budget/short
            assert continuous_certificate(short_rate, short, age, epsilon)
            if exposure > short:
                assert short_rate > threshold
                assert not continuous_certificate(short_rate, exposure, age, epsilon)
            short_exposure_cases += 1

    invalid = [lambda: stage_budget(-1, F(1)),
               lambda: stage_budget(True, F(1)),
               lambda: stage_budget(1, F(0)),
               lambda: stage_budget(1, F(2)),
               lambda: stage_budget(1, 0.5),
               lambda: kernel_variation([], []),
               lambda: kernel_variation([F(1)], [F(1), F(0)]),
               lambda: kernel_variation([F(-1), F(2)], [F(1), F(0)]),
               lambda: kernel_variation([F(1, 2)], [F(1)]),
               lambda: continuous_certificate(F(-1), F(1), 0, F(1)),
               lambda: continuous_certificate(F(1), F(-1), 0, F(1))]
    for call in invalid:
        try:
            call()
        except ValueError:
            continue
        raise AssertionError('invalid certificate input was accepted')
    return {'arithmetic': 'exact fractions; no floating-point budget comparisons',
            'stages': {'consecutive_min': 0, 'consecutive_max': 256,
                       'additional': [512, 1024], 'total': len(ages)},
            'epsilon_values': [str(value) for value in tolerances],
            'relative_threshold_values': [str(value) for value in scales],
            'decisions': decisions, 'short_exposure_cases': short_exposure_cases,
            'invalid_inputs_rejected': len(invalid),
            'full_holding_equivalence_verified': True,
            'equality_at_threshold_accepted': True,
            'exceeded_certificate_bounds_rejected': True}


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def trace_norm_hermitian(matrix):
    assert np.max(np.abs(matrix-matrix.conj().T)) < 2e-12
    return float(np.sum(np.abs(np.linalg.eigvalsh(matrix))))


def supermatrix(channel):
    columns = []
    for col in range(2):
        for row in range(2):
            unit = np.zeros((2, 2), dtype=complex)
            unit[row, col] = 1
            columns.append(channel(unit).reshape(-1, order='F'))
    return np.column_stack(columns)


def exp_series(matrix):
    scale = max(0, int(np.ceil(np.log2(max(1.0, np.linalg.norm(matrix, np.inf))))))
    reduced = matrix/(2**scale)
    answer = term = np.eye(len(matrix), dtype=complex)
    for order in range(1, 60):
        term = term@reduced/order
        answer = answer+term
    for _ in range(scale):
        answer = answer@answer
    return answer


def apply_reference(channel, state):
    answer = np.zeros_like(state, dtype=complex)
    for row in range(2):
        for col in range(2):
            unit = np.zeros((2, 2), dtype=complex)
            unit[row, col] = 1
            image = (channel@unit.reshape(-1, order='F')).reshape((2, 2), order='F')
            reference_block = state[2*row:2*row+2, 2*col:2*col+2]
            answer += np.kron(image, reference_block)
    return answer


def reference_states():
    vectors = [np.array([1, 0, 0, 1], dtype=complex)/np.sqrt(2),
               np.array([np.sqrt(0.2), 0, 0, np.sqrt(0.8)], dtype=complex),
               np.array([1, 1j, 1, -1], dtype=complex)/2]
    return [np.outer(v, v.conj()) for v in vectors]


def discrete_quantum_checks():
    nominal = [F(1, 2), F(1, 5), F(1, 5), F(1, 10)]
    actual = [F(9, 20), F(1, 4), F(3, 20), F(3, 20)]
    bound = float(2*kernel_variation(actual, nominal))
    max_violation = saturation_error = 0.0
    cases = 0
    for keep_distinguishable_paths in [False, True]:
        for state in reference_states():
            outputs = []
            for law in [nominal, actual]:
                output = np.zeros((16, 16), dtype=complex)
                for label, (probability, pauli) in enumerate(zip(law, [I, X, Z, Y])):
                    operation = np.kron(pauli, I)
                    transformed = operation@state@operation.conj().T
                    record = np.zeros((4, 4), dtype=complex)
                    record[label if keep_distinguishable_paths else 0,
                           label if keep_distinguishable_paths else 0] = 1
                    output += float(probability)*np.kron(transformed, record)
                assert abs(np.trace(output)-1) < 1e-13
                assert np.min(np.linalg.eigvalsh(output)) >= -1e-13
                outputs.append(output)
            error = trace_norm_hermitian(outputs[1]-outputs[0])
            max_violation = max(max_violation, error-bound)
            assert error <= bound+2e-13
            if keep_distinguishable_paths:
                saturation_error = max(saturation_error, abs(error-bound))
                assert abs(error-bound) < 2e-13
            cases += 1
    return {'scope': 'Finite recorded CPTP mixtures on entangled inputs; no general diamond-norm optimisation.',
            'joint_reference_record_cases': cases,
            'TV_diamond_upper_bound': str(2*kernel_variation(actual, nominal)),
            'max_sampled_bound_violation': max_violation,
            'orthogonal_record_saturation_max_error': saturation_error,
            'all_numerical_checks_pass': True}


def generator(hamiltonian, jumps):
    def action(state):
        answer = -1j*(hamiltonian@state-state@hamiltonian)
        for rate, operator in jumps:
            square = operator.conj().T@operator
            answer += rate*(operator@state@operator.conj().T-(square@state+state@square)/2)
        return answer
    return supermatrix(action)


def continuous_quantum_checks():
    nominal = generator(0.21*Z, [(0.03, X)])
    actual = generator(0.21*Z+0.017*X, [(0.03, X), (0.011, Z)])
    perturbation = actual-nominal
    assert np.linalg.norm(nominal@perturbation-perturbation@nominal) > 1e-6
    norm_bound = 2*0.017+2*0.011
    identity_errors = []
    state_cases = 0
    for duration in [0.0, 0.125, 0.5, 1.5]:
        ideal, real = exp_series(duration*nominal), exp_series(duration*actual)
        intervals = 128
        integral = np.zeros((4, 4), dtype=complex)
        for point in range(intervals+1):
            u = duration*point/intervals
            coefficient = 1 if point in [0, intervals] else (4 if point % 2 else 2)
            integral += coefficient*(exp_series((duration-u)*actual)@perturbation@exp_series(u*nominal))
        integral *= duration/(3*intervals)
        error = float(np.max(np.abs(real-ideal-integral)))
        identity_errors.append(error)
        assert error < 1e-11
        for state in reference_states():
            output_ideal = apply_reference(ideal, state)
            output_real = apply_reference(real, state)
            for output in [output_ideal, output_real]:
                assert abs(np.trace(output)-1) < 2e-12
                assert np.min(np.linalg.eigvalsh(output)) >= -2e-12
            assert trace_norm_hermitian(output_real-output_ideal) <= duration*norm_bound+2e-12
            state_cases += 1

    # Noncommuting consecutive intervals: verify the telescoping join on
    # every matrix unit, as required for a piecewise generator.
    nominal_2 = generator(-0.13*X, [(0.02, Z)])
    actual_2 = generator(-0.13*X+0.009*Y, [(0.02, Z), (0.007, X)])
    u01, ua1 = exp_series(0.4*nominal), exp_series(0.4*actual)
    u02, ua2 = exp_series(0.7*nominal_2), exp_series(0.7*actual_2)
    difference = ua2@ua1-u02@u01
    telescope = (ua2-u02)@u01+ua2@(ua1-u01)
    piecewise_error = float(np.max(np.abs(difference-telescope)))
    assert piecewise_error < 1e-13
    bound = 0.4*norm_bound+0.7*(2*0.009+2*0.007)
    for state in reference_states():
        assert trace_norm_hermitian(apply_reference(ua2@ua1, state)-apply_reference(u02@u01, state)) <= bound+2e-12
        state_cases += 1
    return {'scope': 'Floating-point complete matrix-unit Duhamel identities and specified reference-state bounds; general norm theorem is the separate analytical proof.',
            'single_interval_durations': [0.0, 0.125, 0.5, 1.5],
            'noncommuting_nominal_and_perturbation': True,
            'matrix_units_per_channel': 4,
            'Duhamel_integral_max_entry_error': max(identity_errors),
            'Simpson_subintervals': 128,
            'piecewise_telescoping_max_entry_error': piecewise_error,
            'reference_state_bound_cases': state_cases,
            'all_numerical_checks_pass': True}


def preservation_state():
    before_path = BANK/'snapshots/before-endpoint-final-10/BEFORE-MANIFEST.json'
    before = json.loads(before_path.read_text())
    preserved = {}
    for group in ['checkpoint12_files', 'canonical_lean_sources', 'preserved_batch09']:
        for relative, digest in before[group].items():
            assert sha(ROOT/relative) == digest, relative
            preserved[relative] = digest
    checkpoint = HERE/'snapshots/checkpoint-12-complete-transfer-bill'
    assert {path.relative_to(ROOT).as_posix() for path in checkpoint.rglob('*') if path.is_file()} == set(before['checkpoint12_files'])
    assert {path.relative_to(ROOT).as_posix() for path in (CANON/'lean').rglob('*.lean')} == set(before['canonical_lean_sources'])
    source_hashes = json.loads((checkpoint/'SOURCE-HASHES.json').read_text())
    assert len(source_hashes) == 192
    current = CANON/'lean/Snuffy'
    assert {path.name for path in current.glob('*.lean')} == set(source_hashes)
    assert all(sha(current/name) == digest for name, digest in source_hashes.items())
    assert len(re.findall(r'^#print axioms ', (CANON/'lean/SummitsAudit.lean').read_text(), re.MULTILINE)) == 1158
    batch_path = BANK/'PROSE-BATCH-10.json'
    batch = json.loads(batch_path.read_text())
    for change in batch['changes']:
        assert sha(ROOT/change['file']) == change['after_sha256'], change['file']
        preserved[change['file']] = change['after_sha256']
    for field in ['review_diff', 'review_markdown', 'new_derivation']:
        path = BANK/batch[field]
        assert sha(path) == batch[field+'_sha256']
        preserved[path.relative_to(ROOT).as_posix()] = sha(path)
    prior_path = HERE/'ENDPOINT-FINAL-INTEGRATION-2026-10-27.json'
    assert json.loads(prior_path.read_text())['targeted_verification_pass']
    preserved[batch_path.relative_to(ROOT).as_posix()] = sha(batch_path)
    preserved[prior_path.relative_to(ROOT).as_posix()] = sha(prior_path)
    return {'canonical_modules': 192, 'canonical_public_names': 1158,
            'checkpoint12_snapshot_files_unchanged': len(before['checkpoint12_files']),
            'canonical_lean_source_files_unchanged': len(before['canonical_lean_sources']),
            'all_192_module_hashes_match_checkpoint12': True,
            'batch09_and_batch10_preserved': True,
            'previous_endpoint_receipt_preserved_sha256': sha(prior_path),
            'preserved_file_set_sha256': hashlib.sha256(json.dumps(preserved, sort_keys=True).encode()).hexdigest()}


def main():
    before = preservation_state()
    exact = exact_threshold_checks()
    discrete = discrete_quantum_checks()
    continuous = continuous_quantum_checks()
    after = preservation_state()
    assert before == after
    result = {'date': '2026-10-27', 'timezone': 'Pacific/Auckland',
              'scope': 'Exact finite certificate arithmetic plus numerical finite-channel checks of the separately written analytical proofs.',
              'all_assertions_pass': True,
              'exact_certificate_checks': exact,
              'numerical_discrete_checks': discrete,
              'numerical_continuous_checks': continuous,
              'preservation': after,
              'proof': str(PROOF.relative_to(ROOT)), 'proof_sha256': sha(PROOF),
              'author_input': 'REPAIRS-2026-10-26/inputs/AUTHOR-DELTA-JOINT-PROOF-2026-10-27.md',
              'author_input_sha256': sha(BANK/'inputs/AUTHOR-DELTA-JOINT-PROOF-2026-10-27.md'),
              'script': str(Path(__file__).relative_to(ROOT)), 'script_sha256': sha(Path(__file__)),
              'full_holding_rate_requirement': 'v_a <= epsilon/2^(2a+5) when tau_a=2^a',
              'general_exposure_requirement': 'tau_a*v_a <= epsilon/2^(a+5)',
              'discrete_requirement': '2*TV(K_act,K_0) <= epsilon/2^(a+5)',
              'canonical_lean_modified': False, 'fresh_lean_compilation': False,
              'analytical_proofs_kernel_formalized': False,
              'actual_installation_residual_certified': False,
              'maximal_target_unchanged': True, 'full_history_retained': True,
              'merge_push_publication_performed': False}
    RECEIPT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'all_assertions_pass': True,
                      'stage_values': exact['stages']['total'],
                      'epsilon_values': len(exact['epsilon_values']),
                      'certificate_decisions': sum(exact['decisions'].values()),
                      'checkpoint12_unchanged': True,
                      'actual_installation_residual_certified': False,
                      'receipt': str(RECEIPT.relative_to(ROOT))}), flush=True)


if __name__ == '__main__':
    main()
