#!/usr/bin/env python3
"""Compile and kernel-check selected repair modules against the sealed 169 baseline."""
from pathlib import Path
import os,subprocess,sys,json,shutil,hashlib,time
root=Path(__file__).resolve().parents[3]
leanroot=Path(os.environ.get('REPAIR_SOURCE_ROOT',str(root/'SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25/lean')))
checks=Path(__file__).resolve().parent
build=checks/os.environ.get('REPAIR_BUILD','targeted-build')
base=Path('/Users/admin/.claude/jobs/9d293ee6/tmp/build169/Snuffy')
if not (build/'Snuffy').exists():
    shutil.copytree(base,build/'Snuffy')
project=root/'BEAM-UPT-2026-10-22/mathlib-probe'
lib=[project/'.lake/build/lib/lean',*sorted(project.glob('.lake/packages/*/.lake/build/lib/lean')),build]
env=os.environ.copy()
env['PATH']='/Users/admin/.elan/toolchains/leanprover--lean4---v4.35.0/bin:'+env.get('PATH','')
env['LEAN_PATH']=':'.join(str(p) for p in lib if p.is_dir())
bin=Path('/Users/admin/.elan/toolchains/leanprover--lean4---v4.35.0/bin')
results=[]
for name in sys.argv[1:]:
    src=leanroot/'Snuffy'/f'{name}.lean'
    cp=subprocess.run([str(bin/'lean'),'-R',str(leanroot),'-o',str(build/'Snuffy'/f'{name}.olean'),str(src)],capture_output=True,env=env)
    output=cp.stdout+cp.stderr
    (checks/f'{name}.compile.log').write_bytes(output)
    result={'module':name,'compile_exit':cp.returncode,'compiler_output_bytes':len(output),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
    print(json.dumps(result),flush=True)
    if cp.returncode or output:
        print(output.decode(errors='replace'),flush=True)
        sys.exit(1)
    kc=subprocess.run([str(bin/'leanchecker'),f'Snuffy.{name}'],capture_output=True,env=env)
    (checks/f'{name}.kernel.log').write_bytes(kc.stdout+kc.stderr)
    result['kernel_exit']=kc.returncode
    result['kernel_output_bytes']=len(kc.stdout+kc.stderr)
    results.append(result)
    print(json.dumps({'module':name,'kernel_exit':kc.returncode,'kernel_output_bytes':result['kernel_output_bytes']}),flush=True)
    if kc.returncode:
        print((kc.stdout+kc.stderr).decode(errors='replace'),flush=True)
        sys.exit(1)
(checks/('TARGETED-'+ '-'.join(sys.argv[1:])+'.json')).write_text(json.dumps(results,indent=2)+'\n')
