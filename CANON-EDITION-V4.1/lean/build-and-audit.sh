#!/bin/zsh
# Rebuild every v4.1 summit module in dependency order, kernel-check, audit
# axioms, and write RECEIPT.txt. Needs: Lean 4.35.0 on PATH (or LEAN_BIN),
# MATHLIB_PROJECT = a Lake project pinned to Mathlib rev 56a005855ea1.
set -u
HERE=${0:A:h}
LEAN_BIN=${LEAN_BIN:-$HOME/.elan/toolchains/leanprover--lean4---v4.35.0/bin}
MATHLIB_PROJECT=${MATHLIB_PROJECT:?set MATHLIB_PROJECT to a Mathlib 56a005855ea1 Lake project}
BUILD=${BUILD:-$(mktemp -d)}
export PATH=$LEAN_BIN:$PATH
mkdir -p $BUILD/Snuffy
export LEAN_PATH="$(cd $MATHLIB_PROJECT && lake env printenv LEAN_PATH):$BUILD"
MODULES=(MathlibAnalyticBridge HalperinDecay OpialBridge CanonVonNeumann RecoveryWork E9SelfHealing H5Closure Greatestness ThermoLedger Composition PremiseFloor ReciprocityCeiling CyclicProjections GaussianTail DeductionBoundary ReflectionCertificate Trotter)
OUT=$HERE/RECEIPT.txt
{
  echo "# v4.1 summit modules — build receipt ($(date -u +%Y-%m-%dT%H:%MZ))"
  echo "# $(lean --version | head -1); Mathlib rev $(cd $MATHLIB_PROJECT/.lake/packages/mathlib && git rev-parse HEAD)"
  ok=1
  for m in $MODULES; do
    lean -R $HERE -o $BUILD/Snuffy/$m.olean $HERE/Snuffy/$m.lean > $BUILD/$m.out 2>&1
    ec=$?; b=$(wc -c < $BUILD/$m.out | tr -d ' ')
    echo "## $m: exit=$ec compiler-output-bytes=$b"
    [[ $ec -ne 0 || $b -ne 0 ]] && { ok=0; sed 's/^/##   /' $BUILD/$m.out; }
  done
  for m in $MODULES; do
    leanchecker Snuffy.$m > $BUILD/$m.check 2>&1; echo "## leanchecker Snuffy.$m: exit=$?"
  done
  hits=$(grep -n -E '(:=|by|^)[[:space:]]*(sorry|admit)([[:space:]]|$)|^axiom ' $HERE/Snuffy/*.lean)
  echo "## sorry/admit/axiom uses in sources: ${hits:-none}"
  echo "## axiom audit (SummitsAudit.lean):"
  lean $HERE/SummitsAudit.lean 2>&1 | sed 's/^/##   /'
  echo "## source sha256:"
  (cd $HERE && shasum -a 256 Snuffy/*.lean SummitsAudit.lean) | sed 's/^/##   /'
  echo "## overall: $([[ $ok -eq 1 ]] && echo PASS || echo FAIL)"
} > $OUT
cat $OUT
