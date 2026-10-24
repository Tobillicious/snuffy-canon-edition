#!/usr/bin/env bash
# Snuffy — Canon Edition: reproducibility entrypoint.
# Zero-warning, zero-float, zero-tolerance execution assertion.
set -euo pipefail
cd /work

echo "== [1/3] Lean verification =="
# Core modules: no imports, no Mathlib. Fail on ANY output (zero warnings).
for f in PremiseStack MeetAlgebra; do
  out=$(lean SNUFFY-CANON-EDITION-2026-10-24/lean/Snuffy/$f.lean) && [ -z "$out" ] \
    || { echo "FAIL: $f.lean produced output:"; echo "$out"; exit 1; }
  echo "PASS: $f.lean (zero warnings)"
done
# Mathlib bridge: compiled through the pinned lake project.
cd /work/mathlib-bridge
out=$(lake env lean /work/SNUFFY-CANON-EDITION-2026-10-24/lean/Snuffy/MathlibAnalyticBridge.lean) && [ -z "$out" ] \
  || { echo "FAIL: MathlibAnalyticBridge.lean produced output:"; echo "$out"; exit 1; }
echo "PASS: MathlibAnalyticBridge.lean (zero warnings)"
cd /work

echo "== [2/3] Ledger replay =="
python3 -I -B LEDGER-FOUR-STROKE-2026-10-24/verify_four_stroke.py --verify-all | tee /tmp/ledger.json
jq -e '.all_pass == true' /tmp/ledger.json > /dev/null || { echo "FAIL: ledger verify-all"; exit 1; }
jq -e '.engine_exact_rational_only == true' /tmp/ledger.json > /dev/null || { echo "FAIL: float usage detected"; exit 1; }
echo "PASS: byte-identical replay, chains intact, exact rational only"

echo "== [3/3] Manuscript assembly checks =="
python3 -I -B SNUFFY-CANON-EDITION-2026-10-24/checks/check_master_assembly.py | tee /tmp/assembly.json
jq -e '.all_pass == true' /tmp/assembly.json > /dev/null || { echo "FAIL: assembly checks"; exit 1; }
echo "PASS: premises, guards, rate components, chain heads, DOI, canon sentence"

echo "== ALL REPRODUCIBILITY CHECKS PASSED =="
