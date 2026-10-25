# Claude handoff — UPT 4.2 repairs — 26 October 2026

Author explicitly requested wrap-up, banking and handoff because usage is
near its limit. Resume from this file, then AGENTS.md and the repair bank.
The maximal UPT target remains fixed. No X3/P1/P2 changes. No publication.
New branch `canon-v4.2-repairs`; draft PR only; merge on the author's word.
Existing manuscript prose must be shown before/after first.

## Where the work is

Working edition:
`/Users/admin/Documents/2026/Snuffy-Book/SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25`

Bank:
`/Users/admin/Documents/2026/Snuffy-Book/BANKS/2026-10-26-4.2-join-repairs`

Isolated branch checkout:
`/Users/admin/Documents/2026/Snuffy-Book/CODEX-4.2-REPAIR-CHECKOUT`

Base is merged PR #7, `d3f0c684a40a0d4dea167e73b9f16df2f8bc354d`,
169 modules / 1,042 names. Baseline backups: bank `snapshots/before/`.

## Implemented and verified

1. G1Held/G1E9 now quantify over unit-normalised physical states. Initial,
   step and run invariants are proved, with concrete zero-Hamiltonian,
   singleton decoder and inhabited-good-event witnesses. Fresh checkpoint 01
   has 169 zero-output compiles, 169 kernel passes and 1,048 standard-axiom
   audited names, strict gates PASS. Initial gate failures came from backup
   placement; original failures are preserved. Only gates were rerun after
   relocating snapshots; source hashes were checked unchanged. Do not say
   the failing initial receipt itself passed in one uninterrupted invocation.
2. TheoremEightLyapunov is integrated: actual clipped functional, exact
   saturated replenishment, solvent-cycle nonincrease, capacity-overflow
   energy balance and storage contraction. Targeted compile/kernel PASS.
   Source/index now 169 / 1,055. Its fresh full checkpoint 02 is **PASS**.
   Last observed progress: `{"phase": "kernel", "completed": 169, "total": 169, "last_module": "PureStateTraceNorm", "last_exit": 0, "elapsed_seconds": 891.061}`.
   Evidence: `checks/snapshots/checkpoint-02-lyapunov/RESULT.json` and
   `lean/RECEIPT.txt` there. Exec session 45466. The job copies the new receipt
   to the working edition only on full PASS and unchanged source hashes.
   Do not edit working Lean sources until that finishes. It uses four-worker
   fresh DAG compilation/kernel checking; all axiom and strict gates remain.
3. README/zenodo spelling Tobillicous -> Tobillicious corrected.

## Separately checked, not canon completion

- `drafts/Snuffy/BennettCounterpart.lean`: actual program
  (s,0,0)->(h(g(s)),0,s), trajectory, FULL ordered history, quantum permutation,
  complete lifecycle comparison and exact adiabatic feasibility iff.
  Compile/kernel PASS. The canon's main Bennett option model is still the
  older arbitrary-bijection/heat-only model. Repair 3 is NOT fully closed.
- `checks/snapshots/response/Snuffy/HoldingSpectralCriterion.lean`: FIVE
  checked helpers: real integral iff with integrability, null-support
  separation, ENNReal iff, quantitative bounded switching energy, and their
  conditional composition. Compile/kernel PASS, source hash in targeted
  receipt. Not in canon; do not add these to its 1,055 count.

## Manuscript and branch state

Master prose has NOT been rewritten. Proposed before/after batches 01 and
02 were shown to the author and are in the bank. Batch 02 qualifies Bennett
as an external checked candidate and scopes the physical claims honestly.
Do not apply count/PASS claims until checkpoint 02 genuinely passes. The
master and render/checksum metadata still require integration; do not claim
publication-ready. `REPAIR-STATUS.md` flags this staged state.

The isolated checkout contains the canon edits, generated 1,055-name index,
now-applicable 1,055-name full PASS receipt, selected reports and separate candidates
under `REPAIRS-2026-10-26/`. The status explicitly distinguishes these.
No push, PR creation, merge or Zenodo publication has been performed yet.
Create the requested DRAFT PR after finishing/checking the staged integration;
attach it to this chat if tools permit. Never merge/publish without author.

## Remaining support, exactly

Bennett: derive complete incremental work F(τ)<Q_actual within the SAME
required deadline for the full admitted family. For A/τ+H the missing
certificate is Q>H and A/(Q-H)<(T-T_other)/D_rev, with full retained history
and every lifecycle charge. Adiabatic and holographic proposals rearranged
or assumed this; they did not construct it. See BENNETT-ADIABATIC-DISPOSITION.md.

Holding: valid conditional mathematical wrappers are now checked. They do
not establish an actual bath gap, actual strictly separated system spectrum,
zero physical constraint power or complete lifecycle costs. Gap alone does
not suppress the ground-sector current correlation. Commutation conserves a
charge but permits energy exchange within a sector. Constant correlations
have a delta spectrum, not a zero spectrum. Generic current sums have cross
terms; preserved orthogonal blocks can eliminate them, but must be proved
for the full actual evolution. Latest DOS proposal has a decisive null-set
inference error; read LATEST-AUTHOR-SYMMETRY-DOS-PROPOSAL.md.

G1 actual guarded-source projection/transition and coupling-removal device;
G2 actual physical policy/outcome tuple and full freedom/R17 delivery for all
rivals/worlds; G3 physical patch/fence/capacity and complete pathwise charges;
external code/gadget/compiler certificates remain. Preserve the full target.

Objection 7 pātai: `/Users/admin/Documents/2026/Snuffy-Book/PATAI-GEMINI-OBJECTION-7-2026-10-26.md`.
All seven objection-7 attachments, G3 input, two trilemma attachments and
latest orthogonal attachment are preserved locally in inputs/ with hashes.
The latest in-chat proposals are assessed in the holding report and final
proposal note; the original chat also remains available to the author.
No messages were sent to Gemini or another chat. Do not treat another
conditional wrapper or a new typeclass hypothesis as a physical instance.

## First actions for Claude

Check checkpoint 02 RESULT/receipt and all source hashes; do not rerun the
50-minute serial audit unnecessarily if the immutable fresh run passed.
Read CHECKPOINT.md and the two disposition reports. Integrate only verified
source/prose claims, regenerate the master theorem index/counts, check claims
and render/seals, then commit/push a draft PR. Preserve the separate candidates
and unresolved physical constructions explicitly. Ask for the specific
missing device/source certificate if it cannot be derived from existing work.

Final audit update: checkpoint 02 completed PASS before banking ended. All
169 source hashes were checked against the working edition; the 1,055-name
receipt and parallel audit provenance are copied into the repair branch.
Do not rerun this completed full audit merely because the prose is pending.
Banking is local only; Claude should finish prose/render/seal integration and
create the requested draft PR.
