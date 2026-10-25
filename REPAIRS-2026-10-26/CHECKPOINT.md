# UPT 4.2 repair checkpoint — 26 October 2026

Full maximal target fixed. No Zenodo publication. Branch `canon-v4.2-repairs`;
draft PR only; merge requires the author's word. No X3/P1/P2 changes.

Base: PR #7 merged at `d3f0c684a40a0d4dea167e73b9f16df2f8bc354d`,
169 modules / 1,042 names. Exact baseline backups are in `snapshots/before/`.
Repair checkout: `/Users/admin/Documents/2026/Snuffy-Book/CODEX-4.2-REPAIR-CHECKOUT`.

## Actual canon changes

- G1Held/G1E9 use unit-normalised physical states. Initialisation, step and
  run invariants and concrete trajectory/decoder/good-event witnesses are proved.
  Fresh checkpoint 01: 169 clean compiles, 169 kernel passes, 1,048 names on
  standard axioms, strict completeness/claims gates PASS. Initial gate failures
  were audit-snapshot placement mistakes; original failures are preserved.
  Only those gates were rerun after relocation, with all source hashes checked.
  Evidence: `checks/snapshots/checkpoint-01-normalised/RESULT.json`.
- The exact checked TheoremEightLyapunov candidate is now integrated: clipped
  functional, saturated replenishment, solvent nonincrease, overflow energy
  account and actual storage contraction. Targeted compile/kernel PASS.
  Current source/index: 169 modules / 1,055 names. Full checkpoint 02 is running
  at `checks/snapshots/checkpoint-02-lyapunov/`; do not describe it as PASS until
  its RESULT.json and receipt confirm it. Exec session 45466.
- README/zenodo spelling corrected to Tobillicious. Master prose has not yet
  been rewritten. Reviewable batches 01 and 02 are prepared; apply counts/PASS
  claims only after checkpoint 02 passes. Batch 02 clarifies that Bennett is
  a separately checked candidate, not a completed physical counterpart.

## Separate checked candidates

- `drafts/Snuffy/BennettCounterpart.lean`: actual `(s,0,0) -> (h(g(s)),0,s)`
  program, trajectory and full ordered history, quantum permutation, lifecycle
  comparison and necessary/sufficient adiabatic window. Compile/kernel PASS.
  The old heat-only main model remains; the full physical repair is NOT closed.
- `checks/snapshots/response/Snuffy/HoldingSpectralCriterion.lean`: five helpers
  for positive-kernel real/extended integrals, spectral support separation,
  bounded switching and their conditional composition. Compile/kernel PASS.
  This candidate is not in the canon and does not increase its name count.

## Exact remaining supports

Bennett needs an actual complete extra-work function F(τ) below saved heat while
meeting the same deadline for the intended family. For A/τ+H, derive Q>H and
A/(Q-H)<(T-T_other)/D_rev. The adiabatic replies rearrange this condition but do
not construct the device satisfying it; the full-history capacity/bill remains.
See BENNETT-ADIABATIC-DISPOSITION.md.

The holding proposals now have valid conditional measure-theory lemmas, but
zero physical holding/constraint power is not derived from a gap, commutation,
a constant correlation, an asserted spectrum, or a newly named hypothesis.
See HOLDING-POWER-DISPOSITION.md, including the latest decomposition assessment.

Original G1 guarded-source/device refinement, G2 full physical policy/outcome
correspondence and R17 delivery, G3 patch/fence/capacity/full pathwise bill, and
external code/gadget/compiler certificates remain construction work. Detailed
Gemini pātai are in the root PATAI-GEMINI-OBJECTION-7-2026-10-26.md and the
submission-07 disposition. No messages were sent to Gemini or another chat.

## Audit execution

Full checkpoint 02 uses a scratch parallel driver: fresh dependency-ordered
compilation and independent kernel checks, four jobs. Canon build-and-audit.sh,
axiom audit and strict gates are unchanged. It copies the receipt back only
on full PASS and unchanged working sources. Do not mutate working Lean sources
until it completes. Preserve all receipts and failed attempts. No new axioms,
no sorry, no publication or merge.

Final bank: both concrete repairs now have passing full checkpoints. The
current 1,055-name receipt is copied into the repair branch. Prose/count
integration, render/seals and draft PR remain for Claude; no push or merge.
