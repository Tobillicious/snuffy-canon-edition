#!/usr/bin/env python3
"""Reproducible targeted check of the development candidate, outside the canon."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess

HERE = Path(__file__).resolve().parent
WORKTREE = HERE.parents[1]
PROJECT = WORKTREE.parent / "BEAM-UPT-2026-10-22/mathlib-probe"
BIN = Path("/Users/admin/.elan/toolchains/leanprover--lean4---v4.35.0/bin")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', choices=['NoiseCompensation', 'PauliInterface'],
                        default='NoiseCompensation')
    args = parser.parse_args()
    module = args.candidate
    namespace = module+'Prototype'
    SOURCE = WORKTREE / ('REPAIRS-2026-10-26/candidates/'+module+'.lean')
    BUILD = HERE / ('development/'+('noise-compensation' if module == 'NoiseCompensation' else 'pauli-interface'))
    BUILD.mkdir(parents=True, exist_ok=True)
    libraries = [BUILD, PROJECT / ".lake/build/lib/lean",
                 *sorted(PROJECT.glob(".lake/packages/*/.lake/build/lib/lean"))]
    env = os.environ.copy()
    env["PATH"] = str(BIN) + ":" + env.get("PATH", "")
    env["LEAN_PATH"] = ":".join(str(path) for path in libraries if path.is_dir())
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    names = re.findall(r"^theorem ([A-Za-z0-9_]+)", SOURCE.read_text(), flags=re.M)
    result = {
        "scope": "Development candidate only; not part of the canonical checkpoint 12 receipt.",
        "source": str(SOURCE), "source_sha256": digest,
        "statements": names, "statement_count": len(names),
    }
    compile_result = subprocess.run(
        [str(BIN / "lean"), "-R", str(SOURCE.parent), "-o",
         str(BUILD / (module+".olean")), str(SOURCE)], capture_output=True, env=env)
    log = compile_result.stdout + compile_result.stderr
    (BUILD / "compile.log").write_bytes(log)
    result.update(compile_exit=compile_result.returncode, compiler_output_bytes=len(log))
    print(json.dumps({"compile_exit": compile_result.returncode, "output_bytes": len(log)}), flush=True)
    if compile_result.returncode == 0 and not log:
        kernel = subprocess.run([str(BIN / "leanchecker"), module], capture_output=True, env=env)
        klog = kernel.stdout + kernel.stderr
        (BUILD / "kernel.log").write_bytes(klog)
        result.update(kernel_exit=kernel.returncode, kernel_output_bytes=len(klog))
        print(json.dumps({"kernel_exit": kernel.returncode, "output_bytes": len(klog)}), flush=True)
        audit = BUILD / "AxiomAudit.lean"
        audit.write_text('import '+module+'\n' + "".join(
            '#print axioms '+namespace+'.' + name + "\n" for name in names))
        ax = subprocess.run([str(BIN / "lean"), str(audit)], capture_output=True, env=env)
        alog = ax.stdout + ax.stderr
        (BUILD / "axioms.log").write_bytes(alog)
        printed = re.findall(r"(?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",
                             alog.decode(), flags=re.S)
        permitted = {"propext", "Classical.choice", "Quot.sound"}
        standard = len(printed) == len(names) and all(
            set(part.strip() for part in values.split(",") if part.strip()) <= permitted
            for values in printed)
        result.update(axiom_audit_exit=ax.returncode, axioms_audited=len(printed),
                      standard_axioms_only=standard)
    result["source_unchanged"] = hashlib.sha256(SOURCE.read_bytes()).hexdigest() == digest
    result["pass"] = (result["compile_exit"] == 0 and result["compiler_output_bytes"] == 0
                      and result.get("kernel_exit") == 0 and result.get("kernel_output_bytes") == 0
                      and result.get("axiom_audit_exit") == 0
                      and result.get("standard_axioms_only") is True and result["source_unchanged"])
    (BUILD / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)
    if not result["pass"]:
        if log:
            print(log.decode(errors="replace"), flush=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
