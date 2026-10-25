#!/usr/bin/env python3
"""Complete checkpoint 01 after correcting only its corpus-scan location."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
working = root / 'SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25'
snapshot = Path(__file__).resolve().parent / 'snapshots/checkpoint-01-normalised'
lean = snapshot / 'lean'
receipt_path = lean / 'RECEIPT.txt'
initial = snapshot / 'INITIAL-RECEIPT-FAIL.txt'
if initial.exists() and sys.argv[1:] != ['--retry']:
    raise SystemExit('Reconciliation already attempted; preserve the evidence')
if not initial.exists():
    shutil.copy2(receipt_path, initial)
    shutil.copy2(snapshot / 'RESULT.json', snapshot / 'INITIAL-RESULT.json')
receipt = initial.read_text()
source_manifest = json.loads((snapshot / 'SOURCE-HASHES.json').read_text())
modules = {Path(n).stem for n in source_manifest}
compiles = re.findall(r'^## (\w+): exit=(\d+) compiler-output-bytes=(\d+)$', receipt, re.M)
kernels = re.findall(r'^## leanchecker Snuffy\.(\w+): exit=(\d+)$', receipt, re.M)
assert len(compiles) == len(modules) == len(kernels) == 169
assert {n for n, _, _ in compiles} == {n for n, _ in kernels} == modules
assert all(ec == '0' and size == '0' for _, ec, size in compiles)
assert all(ec == '0' for _, ec in kernels)
assert '## axiom audit exit=0\n' in receipt
assert '## theorems audited: 1048; non-standard axiom dependencies: none\n' in receipt
assert '## expected audited statements: 1048\n' in receipt
assert '## sorry/admit/axiom uses in sources: none\n' in receipt
for name, digest in source_manifest.items():
    for base in (lean, working / 'lean'):
        assert hashlib.sha256((base / 'Snuffy' / name).read_bytes()).hexdigest() == digest
assert (lean / 'SummitsAudit.lean').read_bytes() == (working / 'lean/SummitsAudit.lean').read_bytes()
receipt_hashes = re.findall(r'^##   ([0-9a-f]{64})  ((?:Snuffy/\w+|SummitsAudit)\.lean)$',
                            receipt, re.M)
assert len(receipt_hashes) == 170
for digest, name in receipt_hashes:
    assert hashlib.sha256((lean / name).read_bytes()).hexdigest() == digest
env = os.environ.copy()
env['CORPUS_ROOT'] = str(root)
gates = []
for script in ('check-complete.py', 'check-claims.py'):
    result = subprocess.run([sys.executable, str(lean / script)], env=env,
                            capture_output=True, text=True)
    gates.append({'script': script, 'exit': result.returncode,
                  'output': result.stdout + result.stderr})
passed = all(r['exit'] == 0 for r in gates)
header = ('# Checkpoint 01 completion after correcting snapshot placement\n'
          '# Fresh compile, kernel and axiom results below are retained from the initial run.\n'
          '# Only the strict completeness and claims gates were rerun; no proof sources changed.\n'
          '# Initial FAIL receipt is preserved as INITIAL-RECEIPT-FAIL.txt.\n')
prefix = receipt.split('## gates (completeness:', 1)[0]
source_block = receipt.split('## source sha256:\n', 1)[1].split('## overall:', 1)[0]
gate_block = '## gates rerun after snapshot relocation:\n' + ''.join(
    '##   ' + line + '\n' for r in gates for line in r['output'].splitlines())
receipt_path.write_text(header + prefix + gate_block + '## source sha256:\n' + source_block +
                        '## overall: ' + ('PASS' if passed else 'FAIL') + '\n')
summary = {'label': '01-normalised', 'overall_pass': passed,
           'working_sources_unchanged': True, 'fresh_compile_count': len(compiles),
           'fresh_kernel_count': len(kernels), 'axiom_count': 1048,
           'initial_run_retained': str(initial), 'gates_rerun': gates,
           'receipt': str(receipt_path)}
(snapshot / 'RESULT.json').write_text(json.dumps(summary, indent=2) + '\n')
if passed:
    for name in ('RECEIPT.txt', 'PROOF-STATE.md'):
        shutil.copy2(lean / name, working / 'lean' / name)
print(json.dumps(summary), flush=True)
raise SystemExit(0 if passed else 1)
