#!/usr/bin/env python3
"""Source inventory for human semantic review; extraction is not a proof audit."""
from pathlib import Path
from collections import defaultdict
import hashlib
import json
import re
import difflib

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CANON = ROOT / "SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25/lean"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def uncomment(s):
    out, i, depth, quoted = [], 0, 0, False
    while i < len(s):
        if depth:
            if s.startswith("/-", i):
                depth += 1
                out.extend("  ")
                i += 2
            elif s.startswith("-/", i):
                depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if s[i] == "\n" else " ")
                i += 1
        elif quoted:
            out.append(s[i])
            if s[i] == "\\" and i + 1 < len(s):
                i += 1
                out.append(s[i])
            elif s[i] == '"':
                quoted = False
            i += 1
        elif s.startswith("/-", i):
            depth = 1
            out.extend("  ")
            i += 2
        elif s.startswith("--", i):
            j = s.find("\n", i)
            if j < 0:
                j = len(s)
            out.extend(" " * (j - i))
            i = j
        else:
            if s[i] == '"':
                quoted = True
            out.append(s[i])
            i += 1
    return "".join(out)

def code_tokens(s):
    s = uncomment(s)
    s = re.sub(r"^import\s+.*$", "", s, flags=re.M)
    return re.sub(r"\s+", "", s)

DECL = re.compile(r"^(?:(?:@\[[^\n]*\])\s*)?(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma|def|abbrev|structure|inductive|class)\s+([^\s(:{]+)", re.M)

def header_end(s, start):
    depth = 0
    i = start
    quoted = False
    pending_let = 0
    while i < len(s):
        c = s[i]
        if quoted:
            if c == "\\":
                i += 2
                continue
            if c == '"':
                quoted = False
        elif c == '"':
            quoted = True
        elif depth == 0 and re.match(r"\blet\b", s[i:]) and (i == 0 or not (s[i-1].isalnum() or s[i-1] == "_")):
            pending_let += 1
            i += 3
            continue
        elif depth == 0 and c == "\n" and re.match(r"\n[ \t]*\|[^\n]*=>", s[i:]):
            return i
        elif c in "({[":
            depth += 1
        elif c in ")}]":
            depth -= 1
        elif depth == 0 and s.startswith(":=", i):
            if pending_let:
                pending_let -= 1
                i += 2
                continue
            return i
        i += 1
    return len(s)

def declarations(path):
    s = uncomment(path.read_text())
    result = []
    blocks = list(re.finditer(r"^(namespace|section|end)(?:\s+([^\s]+))?\s*$", s, re.M))
    stack, pos = [], 0
    for m in DECL.finditer(s):
        while pos < len(blocks) and blocks[pos].start() < m.start():
            kind, name = blocks[pos].group(1), blocks[pos].group(2)
            if kind == "end":
                if stack:
                    stack.pop()
            else:
                stack.append((kind, name))
            pos += 1
        prefix = ".".join(name for kind, name in stack if kind == "namespace" and name)
        full = (prefix + "." if prefix else "") + m.group(2)
        stop = header_end(s, m.end()) if m.group(1) in ("theorem", "lemma") else None
        result.append({
            "kind": m.group(1), "name": m.group(2),
            "qualified_name": full,
            "private": "private" in s[m.start():m.start(1)].split(),
            "line": s.count("\n", 0, m.start()) + 1,
            "signature": s[m.start():stop].strip() if stop is not None else None,
        })
    return result

def compact_view(path):
    s = uncomment(path.read_text())
    ms = list(DECL.finditer(s))
    cuts = []
    for idx, m in enumerate(ms):
        if m.group(1) not in ("theorem", "lemma"):
            continue
        body = header_end(s, m.end())
        next_start = ms[idx + 1].start() if idx + 1 < len(ms) else len(s)
        # Retain global section/namespace/variable context following the proof.
        tail = re.search(r"^(?:end(?:\s.*)?|namespace\s.*|section(?:\s.*)?|variable\s.*|omit\s.*|include\s.*|open\s.*|attribute\s.*|#print.*|#check.*)$", s[body:next_start], re.M)
        stop = body + tail.start() if tail else next_start
        cuts.append((body, stop))
    for a, b in reversed(cuts):
        s = s[:a] + " := [proof body omitted in statement view]\n\n" + s[b:]
    return re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", s).strip() + "\n"

def main():
    for name in ("statements", "skip-diffs"):
        (HERE / name).mkdir(exist_ok=True)
    audit_names = re.findall(r"^#print axioms (\S+)", (CANON / "SummitsAudit.lean").read_text(), re.M)
    canon = sorted((CANON / "Snuffy").glob("*.lean"))
    chash, ccode, cname = defaultdict(list), defaultdict(list), {}
    modules = []
    for p in canon:
        chash[sha(p)].append(p)
        ccode[code_tokens(p.read_text())].append(p)
        cname[p.stem] = p
        ds = declarations(p)
        modules.append({"module": p.stem, "path": str(p.relative_to(ROOT)),
                        "sha256": sha(p), "declarations": ds, "review": "pending"})
        (HERE / "statements" / (p.stem + ".txt")).write_text(compact_view(p))
    skips = re.findall(r"^- `([^`]+\.lean)`", (CANON / "PROOF-STATE.md").read_text(), re.M)
    groups = defaultdict(list)
    for rel in skips:
        groups[sha(ROOT / "BANKS" / rel)].append(rel)
    skipped = []
    for value, paths in groups.items():
        p = ROOT / "BANKS" / paths[0]
        exact = chash[value]
        token = ccode[code_tokens(p.read_text())]
        candidate = token or ([cname[p.stem]] if p.stem in cname else [])
        entry = {"sha256": value, "paths": paths,
                 "byte_identical_canon": [x.stem for x in exact],
                 "code_identical_ignoring_comments_whitespace_imports": [x.stem for x in token],
                 "declarations": declarations(p), "review": "pending"}
        if candidate and not exact:
            diff = difflib.unified_diff(p.read_text().splitlines(keepends=True),
                    candidate[0].read_text().splitlines(keepends=True),
                    fromfile=paths[0], tofile=str(candidate[0].relative_to(ROOT)))
            (HERE / "skip-diffs" / (value[:12] + ".diff")).write_text("".join(diff))
        skipped.append(entry)
    inventory = {"method": "Machine inventory only; human semantic review remains explicit.",
                 "audited_names": audit_names, "modules": modules, "skipped_groups": skipped}
    (HERE / "INVENTORY.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n")
    summary = {"modules": len(modules), "audited_names": len(audit_names),
               "source_theorems": sum(d["kind"] in ("theorem", "lemma") for m in modules for d in m["declarations"]),
               "skipped_files": len(skips), "skipped_unique_contents": len(skipped),
               "skipped_byte_identical_to_canon": sum(len(e["paths"]) for e in skipped if e["byte_identical_canon"]),
               "skipped_code_identical_after_lexical_normalisation": sum(len(e["paths"]) for e in skipped if e["code_identical_ignoring_comments_whitespace_imports"]),
               "compact_statement_bytes": sum(p.stat().st_size for p in (HERE / "statements").glob("*.txt"))}
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
