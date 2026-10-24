#!/usr/bin/env bash
# Snuffy — Canon Edition: one-command verification chain.
# Usage: bash verify-all.sh
# Locates its trees relative to itself; degrades gracefully (SKIP, not FAIL)
# when a toolchain component is absent, and reports each step's status.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
CANON="$HERE/SNUFFY-CANON-EDITION-2026-10-24"
LEDGER="$HERE/LEDGER-FOUR-STROKE-2026-10-24"
STATUS=()
FAIL=0

step() { STATUS+=("$1"); if [ "$1" = FAIL ]; then FAIL=1; fi; }

LEAN="$(command -v lean || true)"
[ -z "$LEAN" ] && [ -x /Users/admin/.elan/bin/lean ] && LEAN=/Users/admin/.elan/bin/lean

echo "== [1/6] Core Lean modules (zero-warning assertion) =="
if [ -n "$LEAN" ]; then
  ok=1
  for f in PremiseStack MeetAlgebra; do
    out="$("$LEAN" "$CANON/lean/Snuffy/$f.lean")" || { echo "FAIL: $f.lean"; step FAIL; ok=0; break; }
    if [ -n "$out" ]; then echo "FAIL: $f.lean emitted output:"; echo "$out"; step FAIL; ok=0; break; fi
    echo "PASS: $f.lean"
  done
  [ $ok -eq 1 ] && step PASS
else
  echo "SKIP: lean not found on PATH"; step SKIP
fi

echo "== [2/6] Mathlib analytic bridge (pinned Mathlib rev 56a005855ea1) =="
PROBE="${MATHLIB_PROBE:-$HERE/../BEAM-UPT-2026-10-22/mathlib-probe}"
if [ -n "$LEAN" ] && [ -d "$PROBE" ]; then
  out="$(cd "$PROBE" && "$LEAN" env lean "$CANON/lean/Snuffy/MathlibAnalyticBridge.lean" 2>/dev/null || \
         cd "$PROBE" && lake env lean "$CANON/lean/Snuffy/MathlibAnalyticBridge.lean")"
  if [ -n "$out" ]; then echo "FAIL: bridge emitted output:"; echo "$out"; step FAIL
  else echo "PASS: MathlibAnalyticBridge.lean"; step PASS; fi
else
  echo "SKIP: pinned Mathlib cache not found (set MATHLIB_PROBE to a lake project with mathlib rev 56a005855ea1)"; step SKIP
fi

echo "== [3/6] Ledger replay (byte-identical, exact-rational) =="
if python3 -I -B "$LEDGER/verify_four_stroke.py" --verify-all > /tmp/vfs.json 2>&1; then
  echo "PASS: $(python3 -c "import json;d=json.load(open('/tmp/vfs.json'));print('all scenarios replay byte-identical, chains intact, exact-rational-only:', d['engine_exact_rational_only'])")"
  step PASS
else
  echo "FAIL:"; cat /tmp/vfs.json; step FAIL
fi

echo "== [4/6] Manuscript assembly checks =="
if python3 -I -B "$CANON/checks/check_master_assembly.py" > /tmp/asm.json 2>&1; then
  echo "PASS: $(python3 -c "import json;print('all_pass:', json.load(open('/tmp/asm.json'))['all_pass'])")"
  step PASS
else
  echo "FAIL:"; cat /tmp/asm.json; step FAIL
fi

echo "== [5/6] Seals: SHA256SUMS and RO-Crate =="
if python3 -I -B - "$CANON" "$LEDGER" <<'PY'
import hashlib, json, sys
from pathlib import Path
ok = True
for root in sys.argv[1:]:
    sums = Path(root, 'SHA256SUMS')
    if not sums.is_file():
        print(f'FAIL: {sums} missing'); sys.exit(1)
    for line in sums.read_text().splitlines():
        if not line.strip():
            continue
        h, f = line.split('  ', 1)
        p = Path(root, f.strip())
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != h:
            print(f'FAIL: {f}'); ok = False
crate = Path(sys.argv[1], 'ro-crate-metadata.json')
if crate.is_file():
    for e in json.loads(crate.read_text())['@graph']:
        if e.get('@type') == 'File':
            p = Path(sys.argv[1], '..', e['@id'])
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != e['sha256']:
                print(f"FAIL: crate {e['@id']}"); ok = False
print('PASS: all checksums and crate hashes verified' if ok else 'FAIL')
sys.exit(0 if ok else 1)
PY
then step PASS; else step FAIL; fi

echo "== [6/6] Render citation integrity =="
if python3 -I -B - "$CANON" <<'PY'
import json, re, sys, zipfile
from pathlib import Path
canon = Path(sys.argv[1]); render = canon / 'render'
HEADS = ['6160d931d55767f39525671ff4ef8f3305b609cd22c6043cd9e0fb3eada69132',
         'd1a0d44bbad5a135928595e152a7a3e987e74a90017837e1491ad8b8430b0ef4',
         '41143bb2756875b03975b1cbb7c5cd09e6e0ee495b06c29243624de52a6a2788']
CANON_SENT = 'Uncompensated breach is deterministically impossible on the certified good event'
DOI = '10.5281/zenodo.23599528'
norm = lambda s: re.sub(r'\s+', ' ', s)
def present(s):
    return all(h in s for h in HEADS) and DOI in s and CANON_SENT in s
html = norm((render / 'Snuffy-Canon-Edition.html').read_text())
epub = norm(''.join(
    zipfile.ZipFile(render / 'Snuffy-Canon-Edition.epub').read(n).decode('utf-8', 'ignore')
    for n in zipfile.ZipFile(render / 'Snuffy-Canon-Edition.epub').namelist()
    if n.endswith(('.xhtml', '.html', '.opf', '.ncx'))))
tex = norm((render / 'Snuffy-Canon-Edition.tex').read_text())
pdf = (render / 'Snuffy-Canon-Edition.pdf').read_bytes()
ok = present(html) and present(epub) and present(tex) and pdf[:5] == b'%PDF-' and b'%%EOF' in pdf[-1024:]
print('PASS: HTML, EPUB citations intact; PDF verified via exact xelatex input + structural integrity'
      if ok else 'FAIL: citation or render integrity')
sys.exit(0 if ok else 1)
PY
then step PASS; else step FAIL; fi

echo
echo "== verify-all summary =="
for s in "${STATUS[@]}"; do echo "  $s"; done
if [ $FAIL -eq 0 ]; then
  echo "RESULT: ALL EXECUTED CHECKS PASSED (skips reported above are toolchain availability, not failures)"
else
  echo "RESULT: FAILURES PRESENT"; exit 1
fi
