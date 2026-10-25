#!/usr/bin/env python3
"""Completeness gate: every Lean module built in the author's BANKS/ must be in
the canon (lean/Snuffy/) or listed in EXCLUDED-MODULES.txt with a
reason. Writes PROOF-STATE.md and exits 1 if anything is missing.

Usage: CORPUS_ROOT=/path/to/Snuffy-Book python3 check-complete.py

Only BANKS/ is scanned. The WHOLE-EDITION 3.x trees are superseded by the Canon
Edition and UPT-4.1-working-candidate is quarantined (00-START-HERE-CURRENT-STATE.md),
so neither counts. Received inputs, snapshots and canon mirrors are skipped.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SNUFFY = os.path.join(HERE, "Snuffy")
EXCL = os.path.join(HERE, "EXCLUDED-MODULES.txt")
OUT = os.path.join(HERE, "PROOF-STATE.md")
SKIP_DIRS = ("/.lake", "/build", "/.git", "/inputs", "/snapshots", "/prior",
             "pre-foldin-snapshot", "pre-consolidation-snapshot", "pre-law-snapshot",
             "pre-landauer-snapshot", "pre-speedlimit-snapshot", "claude-summit-1-von-neumann")


def corpus_modules(root):
    found = {}
    for dp, dn, fn in os.walk(root):
        if any(s in dp for s in SKIP_DIRS):
            continue
        for f in fn:
            if f.endswith(".lean") and f != "lakefile.lean":
                found.setdefault(f[:-5], []).append(os.path.relpath(os.path.join(dp, f), root))
    return found


def main():
    root = os.environ.get("CORPUS_ROOT")
    if not root:
        print("## completeness: not run (CORPUS_ROOT unset)")
        return 0
    canon = {f[:-5] for f in os.listdir(SNUFFY) if f.endswith(".lean")}
    excluded = {}
    if os.path.exists(EXCL):
        for line in open(EXCL):
            line = line.strip()
            if line and not line.startswith("#"):
                name, _, reason = line.partition(" ")
                excluded[name] = reason.strip()
    found = corpus_modules(os.path.join(root, "BANKS"))
    missing = sorted(n for n in found if n not in canon and n not in excluded
                     and not n.endswith("Audit"))
    with open(OUT, "w") as o:
        o.write("# Proof state\n\n")
        o.write(f"Canon modules: {len(canon)}. Corpus module names: {len(found)}. "
                f"Excluded with reason: {len(excluded)}. Missing: {len(missing)}.\n\n")
        o.write("| Module | In canon | Corpus copies (first) |\n| --- | --- | --- |\n")
        for n in sorted(set(found) | canon):
            state = "yes" if n in canon else ("excluded: " + excluded[n] if n in excluded else "**MISSING**")
            first = found.get(n, ["(canon only)"])[0]
            o.write(f"| `{n}` | {state} | `{first}` |\n")
    print(f"## completeness: canon {len(canon)}, corpus names {len(found)}, "
          f"excluded {len(excluded)}, missing {len(missing)}")
    for n in missing:
        print(f"##   MISSING {n}  ({found[n][0]})")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
