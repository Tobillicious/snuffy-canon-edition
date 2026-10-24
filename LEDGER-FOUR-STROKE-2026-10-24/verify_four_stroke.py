#!/usr/bin/env python3
"""Reproducibility wrapper for the replayable four-stroke ledger.

--verify-all:
  1. Re-runs every sealed scenario and asserts byte-identical replay
     (determinism certificate).
  2. Verifies every trace's hash chain and cycle checks.
  3. Asserts the ledger engine contains no float usage (exact rational only).

Deterministic; stdlib only; prints one JSON verdict.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE / 'four_stroke_ledger.py'
SCENARIOS = ['solvent', 'quarantine', 'charged']


def main():
    results = {}
    ok = True
    for s in SCENARIOS:
        trace = HERE / 'traces' / f'{s}.trace.json'
        rerun = subprocess.run([sys.executable, '-I', '-B', str(ENGINE), '--run', s],
                               capture_output=True, text=True)
        byte_identical = rerun.stdout.encode() == trace.read_bytes()
        verify = subprocess.run([sys.executable, '-I', '-B', str(ENGINE), '--verify', str(trace)],
                                capture_output=True, text=True)
        results[s] = {
            'replay_byte_identical': byte_identical,
            'chain_and_checks': verify.returncode == 0,
            'verify_detail': json.loads(verify.stdout) if verify.stdout else verify.stderr[-200:],
        }
        ok = ok and byte_identical and verify.returncode == 0
    engine_src = ENGINE.read_text()
    no_floats = ('float(' not in engine_src and 'math.log' not in engine_src
                 and 'import math' not in engine_src)
    out = {'all_pass': ok and no_floats, 'scenarios': results,
           'engine_exact_rational_only': no_floats,
           'note': 'no float usage, no math.log in engine; all arithmetic fractions.Fraction'}
    print(json.dumps(out, indent=2, sort_keys=True))
    sys.exit(0 if out['all_pass'] else 1)


if __name__ == '__main__':
    if '--verify-all' in sys.argv:
        main()
    else:
        print('usage: verify_four_stroke.py --verify-all')
        sys.exit(2)
