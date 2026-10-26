#!/usr/bin/env python3
"""Construct a local CNOT reduction of one actual BDL replacement step.

The inverse circuit encodes coarse data and fixed X/Z ancillas into the fine
CSS code. This is a circuit primitive, not the full noisy thermal transfer.
"""
from collections import defaultdict
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bdl
import fastbuild


def bits(mask):
    while mask:
        bit = mask & -mask
        mask ^= bit
        yield bit.bit_length() - 1


def weight(mask):
    return bin(mask).count("1")


def equal_span(left, right):
    lb, rb = bdl.rank_and_basis(left), bdl.rank_and_basis(right)
    return len(lb) == len(rb) and all(bdl.reduce(row, rb) == 0 for row in left)


def replacement(T):
    xs, zs, shape = bdl.RX(T)
    xrows, xqubits, zfaces, qrows, qqubits, roots = {}, {}, {}, {}, {}, {}
    qindex = xindex = zindex = 0
    for x in T.VX:
        vertices, edges, faces, _, _ = bdl.build_Yx(T, x)
        xrows[x] = list(range(xindex, xindex + len(vertices)))
        xindex += len(vertices)
        xqubits[x] = set(range(qindex, qindex + len(edges)))
        qindex += len(edges)
        zfaces[x] = list(range(zindex, zindex + len(faces)))
        zindex += len(faces)
    for q in T.VQ:
        vertices, edges, _ = bdl.build_Yq(T, q)
        qqubits[q] = set(range(qindex, qindex + len(vertices)))
        roots[q] = qindex + vertices.index(('L', q, 0))
        qindex += len(vertices)
        qrows[q] = list(range(zindex, zindex + len(edges)))
        zindex += len(edges)
    assert qindex == shape[1] and xindex == shape[0]
    return xs, zs, shape[1], (xrows, xqubits, zfaces, qrows, qqubits, roots)


def construct(T):
    original_x, original_z, n, data = replacement(T)
    xrows, xqubits, zfaces, qrows, qqubits, roots = data
    x, z = list(original_x), list(original_z)
    active = set(range(n))
    available_x, available_z = set(range(len(x))), set(range(len(z)))
    plus, zero, gates, programs = set(), set(), [], defaultdict(list)

    def cnot(control, target, owner):
        assert control in active and target in active and control != target
        for i, row in enumerate(x):
            if row & (1 << control):
                x[i] ^= 1 << target
        for i, row in enumerate(z):
            if row & (1 << target):
                z[i] ^= 1 << control
        gates.append((control, target))
        programs[owner].append((control, target))

    def eliminate_x(row, pivot, owner):
        assert row in available_x
        for target in list(bits(x[row] & ~(1 << pivot))):
            cnot(pivot, target, owner)
        assert x[row] == 1 << pivot
        for i in range(len(x)):
            if i != row and x[i] & (1 << pivot):
                x[i] ^= x[row]
        assert all(not (value & (1 << pivot)) for value in z)
        available_x.remove(row)
        active.remove(pivot)
        plus.add(pivot)

    def eliminate_z(row, pivot, owner):
        assert row in available_z
        for control in list(bits(z[row] & ~(1 << pivot))):
            cnot(control, pivot, owner)
        assert z[row] == 1 << pivot
        for i in range(len(z)):
            if i != row and z[i] & (1 << pivot):
                z[i] ^= z[row]
        assert all(not (value & (1 << pivot)) for value in x)
        available_z.remove(row)
        active.remove(pivot)
        zero.add(pivot)

    q_all = set().union(*qqubits.values())
    for cell in T.VX:
        internal = xqubits[cell]
        owner = ('x', cell)
        while True:
            choice = next(((row, next(bits(x[row] & sum(1 << q for q in internal & active))))
                           for row in xrows[cell] if row in available_x
                           and x[row] & sum(1 << q for q in internal & active)), None)
            if choice is None:
                break
            eliminate_x(*choice, owner)
        while internal & active:
            mask = sum(1 << q for q in internal & active)
            choice = next(((row, next(bits(z[row] & mask)))
                           for row in zfaces[cell] if row in available_z and z[row] & mask), None)
            assert choice is not None, ('unremoved local homology', cell, len(internal & active))
            row, pivot = choice
            assert set(bits(z[row])) <= internal
            eliminate_z(row, pivot, owner)
        assert all(control in internal and target in internal | q_all
                   for control, target in programs[owner])

    for cell in T.VQ:
        internal, root = qqubits[cell], roots[cell]
        owner = ('q', cell)
        while (internal - {root}) & active:
            mask = sum(1 << q for q in (internal - {root}) & active)
            choice = next(((row, next(bits(z[row] & mask)))
                           for row in qrows[cell] if row in available_z and z[row] & mask), None)
            assert choice is not None, ('disconnected q block', cell)
            row, pivot = choice
            assert set(bits(z[row])) <= internal
            eliminate_z(row, pivot, owner)

    coarse_positions = [roots[q] for q in T.VQ]
    assert active == set(coarse_positions)
    assert len(plus) + len(zero) + len(active) == n
    def compress(row):
        return sum(((row >> physical) & 1) << logical for logical, physical in enumerate(coarse_positions))
    coarse_x, coarse_z = fastbuild.code_of(T)
    assert equal_span([compress(row) for row in x], coarse_x)
    assert equal_span([compress(row) for row in z], coarse_z)

    touched = {owner: {q for gate in program for q in gate}
               for owner, program in programs.items() if owner[0] == 'x'}
    colours = {}
    for owner in touched:
        forbidden = {colours[old] for old in colours if touched[old] & touched[owner]}
        colours[owner] = next(c for c in range(len(forbidden) + 1) if c not in forbidden)
    x_colours = 1 + max(colours.values(), default=-1)
    x_max = max((len(program) for owner, program in programs.items() if owner[0] == 'x'), default=0)
    q_max = max((len(program) for owner, program in programs.items() if owner[0] == 'q'), default=0)
    return {
        'fine_x': original_x, 'fine_z': original_z, 'qubits': n,
        'coarse_qubits': len(coarse_positions), 'gates': gates,
        'coarse_positions': coarse_positions, 'coarse_x': coarse_x, 'coarse_z': coarse_z,
        'plus_ancillas': sorted(plus), 'zero_ancillas': sorted(zero),
        'x_cell_colours': x_colours, 'x_cell_max_CNOTs': x_max,
        'q_cell_max_CNOTs': q_max, 'depth_upper_bound': x_colours * x_max + q_max,
        'exact_coarse_stabilizer_spans': True,
    }


def circuit_artifact(result, dual):
    fine_x, fine_z = (result['fine_z'], result['fine_x']) if dual else (result['fine_x'], result['fine_z'])
    coarse_x, coarse_z = (result['coarse_z'], result['coarse_x']) if dual else (result['coarse_x'], result['coarse_z'])
    plus = result['zero_ancillas'] if dual else result['plus_ancillas']
    zero = result['plus_ancillas'] if dual else result['zero_ancillas']
    gates = [(target, control) for control, target in result['gates']] if dual else result['gates']
    x, z = list(fine_x), list(fine_z)
    for control, target in gates:
        x = [row ^ (1 << target) if row & (1 << control) else row for row in x]
        z = [row ^ (1 << control) if row & (1 << target) else row for row in z]
    def embed(row):
        return sum(((row >> i) & 1) << physical
                   for i, physical in enumerate(result['coarse_positions']))
    expected_x = [embed(row) for row in coarse_x] + [1 << q for q in plus]
    expected_z = [embed(row) for row in coarse_z] + [1 << q for q in zero]
    assert equal_span(x, expected_x)
    assert equal_span(z, expected_z)
    return {
        'qubits': result['qubits'], 'coarse_positions': result['coarse_positions'],
        'plus_ancillas': plus, 'zero_ancillas': zero,
        'decoder_CNOTs': gates, 'encoder_CNOTs': list(reversed(gates)),
        'fine_X_checks_hex': [hex(row) for row in fine_x],
        'fine_Z_checks_hex': [hex(row) for row in fine_z],
        'coarse_X_checks_hex': [hex(row) for row in coarse_x],
        'coarse_Z_checks_hex': [hex(row) for row in coarse_z],
        'full_stabilizer_replay_verified': True,
        'scope': 'Exact Clifford code refinement primitive; physical placement and full noisy gauge transfer remain separate.',
    }


def noise_supports(result, dual=False):
    n = result['qubits']
    x, z = (result['fine_z'], result['fine_x']) if dual else (result['fine_x'], result['fine_z'])
    decoder = [(target, control) for control, target in result['gates']] if dual else result['gates']
    encoder = list(reversed(decoder))
    images_x, images_z = [1 << i for i in range(n)], [1 << (n+i) for i in range(n)]
    support_max, syndrome_max = 0, 0
    incidence = [0] * (len(x) + len(z))
    mask = (1 << n) - 1
    def syndrome(pauli):
        px, pz = pauli & mask, pauli >> n
        return (sum((weight(row & px) % 2) << i for i, row in enumerate(z)) |
                sum((weight(row & pz) % 2) << (len(z)+i) for i, row in enumerate(x)))
    for control, target in reversed(encoder):
        basis = [images_x[control], images_x[target], images_z[control], images_z[target]]
        touched = 0
        for pattern in range(1, 16):
            pauli = 0
            for i in range(4):
                if pattern & (1 << i):
                    pauli ^= basis[i]
            footprint = syndrome(pauli)
            support_max = max(support_max, weight((pauli & mask) | (pauli >> n)))
            syndrome_max = max(syndrome_max, weight(footprint))
            touched |= footprint
        for check in bits(touched):
            incidence[check] += 1
        images_x[control] ^= images_x[target]
        images_z[target] ^= images_z[control]
    return {
        'CNOT_fault_channels': len(encoder), 'Pauli_patterns_per_channel': 15,
        'max_output_Pauli_weight': support_max,
        'max_output_joint_syndrome_weight': syndrome_max,
        'max_check_to_CNOT_fault_channel_incidence': max(incidence, default=0),
        'scope': 'Independent Pauli faults after CNOTs in this one-step encoder; placement, resets, idles and full transfer are separate.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--second-step', action='store_true',
                        help='Also replay the alternating 206-to-5116-qubit replacement.')
    args = parser.parse_args()
    assert os.environ.get('PYTHONHASHSEED') == '0', 'Use PYTHONHASHSEED=0'
    fastbuild.patch_star_scan()
    records = []
    for seed in [(2, 1), (3, 2), (3, 3)]:
        old = bdl.seed_planar(*seed)
        for dual in [False, True]:
            T = bdl.swap(old) if dual else old
            result = construct(T)
            artifact = circuit_artifact(result, dual)
            artifact_path = HERE / 'refinement-circuits' / ('%sx%s-%s.json' % (*seed, 'RZ' if dual else 'RX'))
            artifact_path.parent.mkdir(exist_ok=True)
            artifact_path.write_text(json.dumps(artifact, indent=2)+'\n')
            support = noise_supports(result, dual)
            record = {key: value for key, value in result.items()
                      if key not in ['fine_x', 'fine_z', 'gates', 'plus_ancillas', 'zero_ancillas',
                                     'coarse_positions', 'coarse_x', 'coarse_z']}
            record.update(seed=list(seed), replacement='R_Z' if dual else 'R_X',
                          plus_ancilla_count=len(result['zero_ancillas'] if dual else result['plus_ancillas']),
                          zero_ancilla_count=len(result['plus_ancillas'] if dual else result['zero_ancillas']),
                          circuit_file=str(artifact_path.relative_to(HERE)),
                          full_stabilizer_replay_verified=True,
                          gate_list_sha256=hashlib.sha256(json.dumps(artifact['decoder_CNOTs']).encode()).hexdigest(),
                          noise_support=support)
            records.append(record)
            print(json.dumps(record), flush=True)
    receipt = {'scope': 'Explicit finite one-step refinement circuits and fault supports; not full noisy thermal preparation or all-level kernel verification.',
               'cases': records, 'all_assertions_pass': True,
               'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in [Path(__file__), HERE/'bdl.py', HERE/'fastbuild.py']}}
    (HERE/'REFINEMENT-CIRCUIT.json').write_text(json.dumps(receipt, indent=2)+'\n')
    if args.second_step:
        started = time.monotonic()
        first_x, first_z, first_shape = bdl.RX(bdl.seed_planar(3, 2))
        previous, _ = bdl.to_TSC(first_x, first_z, first_shape[1])
        result = construct(bdl.swap(previous))
        artifact = circuit_artifact(result, True)
        path = HERE/'refinement-circuits/3x2-RX-then-RZ.json'
        path.write_text(json.dumps(artifact, indent=2)+'\n')
        second = {
            'scope': 'Exact finite second replacement replay; no all-level or full noisy-preparation claim.',
            'coarse_qubits': result['coarse_qubits'], 'fine_qubits': result['qubits'],
            'CNOTs': len(result['gates']),
            'x_cell_colours': result['x_cell_colours'],
            'x_cell_max_CNOTs': result['x_cell_max_CNOTs'],
            'q_cell_max_CNOTs': result['q_cell_max_CNOTs'],
            'depth_upper_bound': result['depth_upper_bound'],
            'full_stabilizer_replay_verified': True,
            'circuit_file': str(path.relative_to(HERE)),
            'circuit_file_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'source_sha256': receipt['source_sha256'],
            'elapsed_seconds': time.monotonic()-started,
            'all_assertions_pass': True,
        }
        (HERE/'REFINEMENT-SECOND-STEP.json').write_text(json.dumps(second, indent=2)+'\n')
        print(json.dumps(second), flush=True)


if __name__ == '__main__':
    main()
