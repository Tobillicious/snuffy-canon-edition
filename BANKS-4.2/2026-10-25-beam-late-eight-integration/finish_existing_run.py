#!/usr/bin/env python3
"""Finish Beam's preserved 136-module run without repeating unchanged checks.

This is a combined receipt: 136 compilation/kernel results are reused only
after source and object hash checks; eight are fresh. The full axiom audit,
module coverage, corpus completeness and claims gates are fresh.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

BANK = Path(__file__).resolve().parent
ROOT = BANK.parent.parent
EDITION = ROOT / "SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25"
HERE = EDITION / "lean"
OLD = json.loads((BANK / "BEAM-RUN.json").read_text())
BUILD = Path(OLD["build_directory"])
BIN = Path.home() / ".elan/toolchains/leanprover--lean4---v4.35.0/bin"
MATHLIB = ROOT / "BEAM-UPT-2026-10-22/mathlib-probe"
LOGS = BANK / "checks"
LOGS.mkdir(exist_ok=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(label, command, env, cwd=HERE):
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (LOGS / f"{label}.txt").write_text(result.stdout)
    return result


def main():
    prior_receipt = BANK / "before/lean/RECEIPT.txt"
    assert sha(prior_receipt) == OLD["source_receipt_sha256"], "Prior receipt changed"
    reused = OLD["completed_compile_modules"]
    assert reused == OLD["completed_kernel_modules"], "Incomplete prior kernel checks"
    for module in reused:
        assert sha(HERE / "Snuffy" / f"{module}.lean") == OLD["source_sha256"][module], module
        assert sha(BUILD / "Snuffy" / f"{module}.olean") == OLD["olean_sha256"][module], module

    script = (HERE / "build-and-audit.sh").read_text()
    modules = re.search(r"^MODULES=\((.*)\)$", script, re.M).group(1).split()
    late = OLD["late_modules"]
    assert len(modules) == len(set(modules))
    assert set(modules) == set(reused) | set(late)
    assert set(modules) == {p.stem for p in (HERE / "Snuffy").glob("*.lean")}
    sources = sorted((HERE / "Snuffy").glob("*.lean")) + [HERE / "SummitsAudit.lean"]
    initial_hashes = {str(p.relative_to(HERE)): sha(p) for p in sources}

    env = os.environ.copy()
    env["PATH"] = str(BIN) + os.pathsep + env.get("PATH", "")
    paths = subprocess.run([str(BIN / "lake"), "env", "printenv", "LEAN_PATH"],
                           cwd=MATHLIB, env=env, check=True, text=True,
                           stdout=subprocess.PIPE).stdout.strip()
    env["LEAN_PATH"] = paths + os.pathsep + str(BUILD)
    env["CORPUS_ROOT"] = str(ROOT)
    records = {}
    for module in late:
        command = [str(BIN / "lean"), "-R", str(HERE), "-o",
                   str(BUILD / "Snuffy" / f"{module}.olean"),
                   str(HERE / "Snuffy" / f"{module}.lean")]
        result = run(f"compile-{module}", command, env)
        records[module] = {"compile_exit": result.returncode,
                           "compiler_output_bytes": len(result.stdout.encode())}
        print(f"compile {module}: exit={result.returncode}, output={len(result.stdout.encode())}", flush=True)
        if result.returncode or result.stdout:
            print(result.stdout)
            (BANK / "FRESH-CHECKS.json").write_text(json.dumps(records, indent=2) + "\n")
            return 1
        result = run(f"kernel-{module}", [str(BIN / "leanchecker"), f"Snuffy.{module}"], env)
        records[module]["kernel_exit"] = result.returncode
        print(f"kernel {module}: exit={result.returncode}", flush=True)
        if result.returncode:
            print(result.stdout)
            (BANK / "FRESH-CHECKS.json").write_text(json.dumps(records, indent=2) + "\n")
            return 1

    audit = run("axioms", [str(BIN / "lean"), str(HERE / "SummitsAudit.lean")], env)
    expected = re.findall(r"^#print axioms (\S+)", (HERE / "SummitsAudit.lean").read_text(), re.M)
    joined = re.sub(r",\n\s+", ", ", audit.stdout)
    printed = re.findall(r"^'(.+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", joined, re.M)
    bad = [(name, axioms) for name, axioms in printed
           if set(filter(None, map(str.strip, axioms.split(","))))
           - {"propext", "Classical.choice", "Quot.sound"}]
    audit_ok = (audit.returncode == 0 and len(printed) == len(expected)
                and {name for name, _ in printed} == set(expected) and not bad)
    print(f"axioms: exit={audit.returncode}, printed={len(printed)}/{len(expected)}, bad={len(bad)}", flush=True)
    gates = {}
    for label, filename in (("completeness", "check-complete.py"), ("claims", "check-claims.py")):
        result = run(label, [sys.executable, str(HERE / filename)], env)
        gates[label] = result.returncode
        print(result.stdout, end="", flush=True)

    changed = [name for name, digest in initial_hashes.items() if sha(HERE / name) != digest]
    source_hits = []
    for path in sources:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if re.search(r"(^\s*|(:=|by)\s*)(sorry|admit)\s*$|^axiom ", line):
                source_hits.append(f"{path.relative_to(HERE)}:{number}: {line}")
    passed = audit_ok and not any(gates.values()) and not changed and not source_hits
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    receipt = [f"# Canon Edition 4.2 — combined verification receipt ({stamp})",
               "# 136 compilation/kernel results reused from the preserved Beam run; eight fresh.",
               f"# Prior receipt sha256: {OLD['source_receipt_sha256']}",
               "# Reuse checked against recorded source and .olean hashes.",
               "# Full axiom audit and completeness/claims gates are fresh.",
               "# Lean 4.35.0; Mathlib rev 56a005855ea17e0b0958f73ec801ae140b0a1679",
               f"## modules: {len(modules)}; reused compile/kernel: {len(reused)}; fresh compile/kernel: {len(late)}"]
    for module in modules:
        receipt.append(f"## {module}: exit=0 compiler-output-bytes=0")
    for module in modules:
        receipt.append(f"## leanchecker Snuffy.{module}: exit=0")
    receipt += [f"## sorry/admit/axiom uses in sources: {source_hits or 'none'}",
                "## axiom audit (SummitsAudit.lean):"]
    receipt += ["##   " + line for line in audit.stdout.splitlines()]
    receipt += [f"## axiom audit exit={audit.returncode}",
                f"## theorems/lemmas audited: {len(printed)}; expected: {len(expected)}; non-standard axiom dependencies: {bad or 'none'}"]
    for label in gates:
        receipt += ["##   " + line for line in (LOGS / f"{label}.txt").read_text().splitlines()]
    receipt += [f"## source changes during verification: {changed or 'none'}", "## source sha256:"]
    receipt += [f"##   {digest}  {name}" for name, digest in initial_hashes.items()]
    receipt += ["## overall: " + ("PASS" if passed else "FAIL")]
    result_text = "\n".join(receipt) + "\n"
    (BANK / "COMBINED-RECEIPT.txt").write_text(result_text)
    result_record = {"overall": "PASS" if passed else "FAIL", "modules": len(modules),
                     "reused_compile_kernel": len(reused), "fresh_compile_kernel": len(late),
                     "fresh_axiom_statements": len(printed), "expected_axiom_statements": len(expected),
                     "nonstandard_axioms": bad, "gates": gates, "source_changes": changed,
                     "fresh_checks": records, "source_sha256": initial_hashes,
                     "combined_receipt_sha256": sha(BANK / "COMBINED-RECEIPT.txt")}
    (BANK / "RESULT.json").write_text(json.dumps(result_record, indent=2) + "\n")
    if passed:
        (HERE / "RECEIPT.txt").write_text(result_text)
    print("overall: " + result_record["overall"], flush=True)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
