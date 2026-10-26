#!/usr/bin/env python3
"""Run the required full build on an immutable snapshot of one repair step."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import shlex
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
working = Path(os.environ.get('REPAIR_WORKING_ROOT',
                            str(root / 'SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25')))
checks = Path(__file__).resolve().parent
label = sys.argv[1]
snapshot = checks / 'snapshots' / ('checkpoint-' + label)
if snapshot.exists():
    raise SystemExit('Checkpoint exists; choose a new label to preserve its evidence')


def hashes():
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted((working / 'lean/Snuffy').glob('*.lean'))}


before = hashes()
indexed = subprocess.run([sys.executable, 'gen-index.py'], cwd=working / 'lean',
                         capture_output=True, text=True, check=True)
snapshot.mkdir(parents=True)
shutil.copytree(working / 'lean', snapshot / 'lean')
shutil.copytree(working / 'inserts', snapshot / 'inserts')
(snapshot / 'SOURCE-HASHES.json').write_text(json.dumps(before, indent=2) + '\n')
# Only the scratch execution driver is parallelised. The canon's published
# command, manifest, theorem audit and gates are preserved unchanged.
jobs = int(os.environ.get('REPAIR_AUDIT_JOBS', '4'))
driver = snapshot / 'lean/build-and-audit.sh'
original_driver = driver.read_text()
compile_start = original_driver.index('  for m in $MODULES; do\n')
kernel_start = original_driver.index('  for m in $MODULES; do\n', compile_start + 1)
kernel_end = original_driver.index('  hits=$(', kernel_start)
helper = shlex.quote(str(checks / 'parallel-modules.py'))
replacement = ''.join(
    f'  {shlex.quote(sys.executable)} {helper} {phase} "$HERE" "$BUILD" {jobs} "${{MODULES[@]}}"\n'
    '  [[ $? -ne 0 ]] && ok=0\n'
    for phase in ('compile', 'kernel'))
driver.write_text(original_driver[:compile_start] + replacement + original_driver[kernel_end:])
(snapshot / 'CANONICAL-BUILD-AND-AUDIT.sh').write_text(original_driver)
(snapshot / 'AUDIT-DRIVER.json').write_text(json.dumps({
    'jobs': jobs, 'canonical_driver_sha256': hashlib.sha256(original_driver.encode()).hexdigest(),
    'executed_driver_sha256': hashlib.sha256(driver.read_bytes()).hexdigest(),
    'orchestration': 'fresh DAG compilation; independent kernel checks; unchanged axiom audit and gates'
}, indent=2) + '\n')
env = os.environ.copy()
env['PATH'] = '/Users/admin/.elan/toolchains/leanprover--lean4---v4.35.0/bin:' + env.get('PATH', '')
env['MATHLIB_PROJECT'] = str(root / 'BEAM-UPT-2026-10-22/mathlib-probe')
env['CORPUS_ROOT'] = str(root)
env['BUILD'] = str(snapshot / 'objects')
print(indexed.stdout.strip(), flush=True)
print('Fresh full build: ' + str(snapshot), flush=True)
with (snapshot / 'console.log').open('w') as output:
    result = subprocess.run(['/bin/zsh', str(snapshot / 'lean/build-and-audit.sh')],
                            env=env, stdout=output, stderr=subprocess.STDOUT)
receipt = (snapshot / 'lean/RECEIPT.txt').read_text()
passed = result.returncode == 0 and '\n## overall: PASS\n' in receipt
unchanged = before == hashes()
summary = {'label': label, 'process_exit': result.returncode, 'overall_pass': passed,
           'working_sources_unchanged': unchanged,
           'receipt': str(snapshot / 'lean/RECEIPT.txt')}
(snapshot / 'RESULT.json').write_text(json.dumps(summary, indent=2) + '\n')
if passed and unchanged:
    for name in ('RECEIPT.txt', 'PROOF-STATE.md'):
        shutil.copy2(snapshot / 'lean' / name, working / 'lean' / name)
print(json.dumps(summary), flush=True)
raise SystemExit(0 if passed and unchanged else 1)
