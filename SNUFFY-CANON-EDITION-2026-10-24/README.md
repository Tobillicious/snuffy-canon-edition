# Snuffy — Canon Edition (insert set, 24 October 2026)

## Assembled artifacts (same day)

- `SNUFFY-CANON-EDITION-MASTER.md` — the unified master manuscript (Parts I–IV: premise stack, retained core, the canon chapters, references). Assembly checks: `checks/check_master_assembly.py` → `.out`, **all_pass: true** (seven premises, guards, five rate components, verbatim ledger chain heads, DOI, canon sentence).
- `lean/Snuffy/PremiseStack.lean` — the seven premises as declarations; proves P-mon at the standard cost model. Compiles, Lean 4.35.0 core, no imports.
- `lean/Snuffy/MeetAlgebra.lean` — the H5 meet algebra: `anchor_preserved_over` (the tactic target `P_{T0 ∪ ΔΣ} = P_{T0}`), `contradiction_collapse`, `collapse_over`, consistency preservation, and a concrete predicate model discharging every lattice law. Compiles (cosmetic linter warnings only).
- `lean/COMPILE-RECEIPTS.txt` — exit-0 receipts, Lean 4.35.0 (arm64).
- `EVIDENCE-LINEAGE.md` — the published Zenodo core (DOI 10.5281/zenodo.23599528), local integrity (43/44; the single drift is a navigation file), and the Canon Edition's relationship and deposit recommendation.


Author-side canon manuscript inserts, drafted to the integration briefing and emitting the exact forms with their guards and evidence citations. This tree is the Canon Edition working set; it supersedes the 3.x candidate lineage by name and steps off its numbering. No prior edition, bank, or ledger is modified by this tree.

## Contents and placement

| Insert | Canon Edition section | Supersedes / extends (3.7 master argument) |
| --- | --- | --- |
| `inserts/00-header-premise-stack.md` | Header | §1.1 the relational given; new premise stack |
| `inserts/08-thermodynamic-core.md` | §8 Thermodynamic core | §10 joint readout and entropy accounting; Theorem 8 route |
| `inserts/11-identity-by-continuation.md` | §11 Identity layer | §4 continuation and records; Witness 2 |
| `inserts/12-e9-trichotomy.md` | §12 Adversarial containment | §6–7 timing and workload; E9 |
| `inserts/13-h5-meet-algebra.md` | §13 Logical extension | §8 generation and reflection; H5 (per the execution queue, alongside the briefing's five) |
| `inserts/14-canon-and-greatestness.md` | §14 Canon and greatestness | §13–14 complete-rival comparison and composition |

## Integration guards carried (from the review banks)

1. §8 uses the **unconditional** export bound \(\beta Q_B\ge I_M+D_{\mathrm{err}}\); the \(W_{\mathrm{on}}\)-form is a noted regime case only.
2. §12 carries the **full trichotomy** (A funded absorption, B syndrome, C per-site power); no single branch is cited as closing containment alone.
3. §14 states dominance with the **mirror-qualified quantifier**.
4. §14 uses P-slack in the **Landauer–Bennett form**; the variational-selection route is recorded as rejected.

## Evidence citations

Ledger (exact replay, hash-chained): `LEDGER-FOUR-STROKE-2026-10-24/` — chain heads and engine hash printed in the header insert; trace checksums in that directory's `SHA256SUMS`. Review banks (exact finite checks, provenance receipts): `BANKS/2026-10-24-glm-thermodynamic-route/` (`REVIEW.md`, `WITNESS-REVIEW.md`, `REPAIRS-AND-GREATESTNESS.md`, `CLOSURE.md`, `PREMISE-REDUCTION.md`, `GLOBAL-D-RELEASE.md`). The three evidence kinds — compiled, replayed, prose-at-premises — are distinguished in the header insert and never conflated. No Lean is claimed by this insert set; the Lean export queue is the next phase.

## Provenance and status

Drafted by GLM to the author's integration briefing of 24 October 2026, from the released theory (GLOBAL D: CLOSED-AT-DECLARED-PREMISES). Gemini's original identifiers are preserved (Theorem 8, E9, H5, X3, Witness 2/Theorem 2.3). This is the author's manuscript; assembly into the whole-edition source and the rendered book is the following task, and no publication is implied by this tree.
