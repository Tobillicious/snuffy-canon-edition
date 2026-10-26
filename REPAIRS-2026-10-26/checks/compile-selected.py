#!/usr/bin/env python3
"""Targeted development checks, explicitly reusing checkpoint-09 dependencies.

The separate full-checkpoint.py run is required for a new combined receipt.
"""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys

checks = Path(__file__).resolve().parent
worktree = checks.parents[1]
corpus = worktree.parent
source = Path(os.environ.get('REPAIR_SOURCE_ROOT', str(worktree / 'CANON-EDITION-V4.2-WORKING/lean')))
baseline = corpus / 'BANKS/2026-10-26-4.2-join-repairs/checks/snapshots/checkpoint-09-warmstart-walk9'
build = checks / 'warmstart-development-build'
if not (build / 'Snuffy').exists():
    shutil.copytree(baseline / 'objects/Snuffy', build / 'Snuffy')
project = corpus / 'BEAM-UPT-2026-10-22/mathlib-probe'
libraries = [build, project / '.lake/build/lib/lean',
             *sorted(project.glob('.lake/packages/*/.lake/build/lib/lean'))]
env = os.environ.copy()
env['LEAN_PATH'] = ':'.join(str(p) for p in libraries if p.is_dir())
bin_dir = Path('/Users/admin/.elan/toolchains/leanprover--lean4---v4.35.0/bin')
env['PATH'] = str(bin_dir) + ':' + env.get('PATH', '')

for module in sys.argv[1:]:
    src = source / 'Snuffy' / (module + '.lean')
    digest = hashlib.sha256(src.read_bytes()).hexdigest()
    output = checks / 'development' / (module + '-' + digest[:12])
    output.mkdir(parents=True, exist_ok=True)
    result = {'module': module, 'source_sha256': digest,
              'dependency_reuse': str(baseline / 'objects/Snuffy'),
              'scope': 'targeted compilation and kernel check; not full canon verification'}
    compile_result = subprocess.run(
        [str(bin_dir / 'lean'), '-R', str(source), '-o', str(build / 'Snuffy' / (module + '.olean')), str(src)],
        capture_output=True, env=env)
    compile_log = compile_result.stdout + compile_result.stderr
    (output / 'compile.log').write_bytes(compile_log)
    result.update(compile_exit=compile_result.returncode, compiler_output_bytes=len(compile_log))
    if compile_result.returncode == 0 and not compile_log:
        kernel = subprocess.run([str(bin_dir / 'leanchecker'), 'Snuffy.' + module],
                                capture_output=True, env=env)
        (output / 'kernel.log').write_bytes(kernel.stdout + kernel.stderr)
        result.update(kernel_exit=kernel.returncode,
                      kernel_output_bytes=len(kernel.stdout + kernel.stderr))
    result['source_unchanged'] = hashlib.sha256(src.read_bytes()).hexdigest() == digest
    result['pass'] = (result['compile_exit'] == 0 and result['compiler_output_bytes'] == 0
                      and result.get('kernel_exit') == 0 and result['source_unchanged'])
    (output / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)
    if not result['pass']:
        print(compile_log.decode(errors='replace'), flush=True)
        sys.exit(1)
