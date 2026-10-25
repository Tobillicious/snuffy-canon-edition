#!/usr/bin/env python3
"""Fresh DAG compilation or independent kernel checks; preserve every result."""
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import time

phase, source_arg, build_arg, jobs_arg, *modules = sys.argv[1:]
source, build = Path(source_arg), Path(build_arg)
jobs = max(1, int(jobs_arg))
if phase not in ('compile', 'kernel') or len(set(modules)) != len(modules):
    raise SystemExit('Invalid phase or duplicate module manifest')
names = set(modules)
deps = {}
for name in modules:
    text = (source / 'Snuffy' / (name + '.lean')).read_text()
    imports = set(re.findall(r'^import Snuffy\.(\w+)\s*$', text, re.M))
    if imports - names:
        raise SystemExit('Unbuilt local imports: ' + repr((name, imports - names)))
    deps[name] = imports if phase == 'compile' else set()


def run(name):
    started = time.monotonic()
    src = source / 'Snuffy' / (name + '.lean')
    before = hashlib.sha256(src.read_bytes()).hexdigest()
    if phase == 'compile':
        command = ['lean', '-R', str(source), '-o', str(build / 'Snuffy' / (name + '.olean')),
                   str(src)]
        log = build / (name + '.out')
    else:
        command = ['leanchecker', 'Snuffy.' + name]
        log = build / (name + '.check')
    with log.open('wb') as out:
        result = subprocess.run(command, stdout=out, stderr=subprocess.STDOUT)
    after = hashlib.sha256(src.read_bytes()).hexdigest()
    return {'module': name, 'exit': result.returncode, 'output_bytes': log.stat().st_size,
            'elapsed_seconds': round(time.monotonic() - started, 3),
            'source_sha256': before, 'source_unchanged': before == after,
            'log': str(log)}


results = {}
pending = set(modules)
running = {}
phase_start = time.monotonic()
with ThreadPoolExecutor(max_workers=jobs) as pool:
    while pending or running:
        ready = [m for m in modules if m in pending and deps[m] <= results.keys()]
        for name in ready[:max(0, jobs - len(running))]:
            pending.remove(name)
            running[pool.submit(run, name)] = name
        if not running:
            raise SystemExit('Local dependency cycle: ' + repr(sorted(pending)))
        completed, _ = wait(running, return_when=FIRST_COMPLETED)
        for task in completed:
            name = running.pop(task)
            results[name] = task.result()
            (build / 'PROGRESS.json').write_text(json.dumps({
                'phase': phase, 'completed': len(results), 'total': len(modules),
                'last_module': name, 'last_exit': results[name]['exit'],
                'elapsed_seconds': round(time.monotonic() - phase_start, 3)
            }) + '\n')

ordered = [results[m] for m in modules]
(build / ('parallel-' + phase + '.json')).write_text(
    json.dumps({'jobs': jobs, 'phase': phase, 'results': ordered}, indent=2) + '\n')
bad = False
for r in ordered:
    if phase == 'compile':
        print('## {module}: exit={exit} compiler-output-bytes={output_bytes}'.format(**r))
    else:
        print('## leanchecker Snuffy.{module}: exit={exit}'.format(**r))
    if r['exit'] or r['output_bytes'] or not r['source_unchanged']:
        bad = True
        print('##   source-unchanged=' + str(r['source_unchanged']))
        for line in Path(r['log']).read_text(errors='replace').splitlines():
            print('##   ' + line)
raise SystemExit(1 if bad else 0)
