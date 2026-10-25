# Next-proof register — 25 October 2026 (evening)

*Historical queue recorded against the then 113-module canon. Current 4.2 working state: 144 modules / 924 audited statements; the older entries below retain their dated context. Companion to `BANKS/2026-10-24-next-proof-register/REGISTER.md`.*

## Current 4.2 checkpoint

Solvent and affordable reciprocity are incorporated in the checked canon. `ErrorBudget.telescoping_delta` and `error_budget` now supply the compiled product-error engine. Their older waiting/registered labels below are superseded by this checkpoint.

The boundary/work/history continuation adds 28 checked statements in the existing late modules and Part III-G of the working master. Current work is the actual full-history source/capacity/physical handoff and complete charge correspondence, full G1 source/fault certificate, whole continuation/freedom G2 outcome, and the remaining semantic review. Shell counting, finite-code recovery, cumulative billing, operator flow and finite dual-kernel derivations are established component results. Verification evidence: `BANKS/2026-10-25-boundary-work-history-wiring/RESULT.json`.

## 1. Solvent reciprocity (from PĀTAI 2, P2b) — **FOLDED INTO THE CANON (25 Oct, late): `SolventReciprocity` module, §23.1**

The proof was banked with receipt (`BANKS/2026-10-25-solvent-reciprocity/`), then folded into the canon the same evening after the completeness gate correctly flagged the bank→canon gap. The canon is 113 modules; `solvent_keeps_everyone` and `reciprocity_dominance_solvent` are cited in §23.1. Original record:

**Closed.** `BANKS/2026-10-25-solvent-reciprocity/SolventReciprocity.lean` proves both targets — `solvent_keeps_everyone` and `reciprocity_dominance_solvent` — compiled clean (zero output, `leanchecker` exit 0) against Mathlib `56a005855ea1` with `Greatestness`/`PremiseFloor`/`UnionClosure` as dependencies; receipt in the bank. Awaiting fold-in to the next canon increment (Edition 4.1 seals at 113 modules with the restatement cited as banked). The original target statement is preserved below for the record.

**Status quo.** `ReciprocityCeiling.reciprocity_dominance` carries the union-closure hypothesis `hF : ∀ x ∈ F, ∀ y ∈ F, x ⊔ y ∈ F` and routes through `Greatestness.greatest_of_union_closed`. Under solvency this hypothesis is unnecessary.

**Target.** Two statements in `ReciprocityCeiling` (or a successor module):

1. `solvent_keeps_everyone`: under the resource model's solvency (`⊤ ∈ budgetFamily`, cost of `⊤` within budget) and an aligned canonical option `o`, the canonical outcome is `⊤` and keeps every particular — `o = ⊤` from `UnionClosure.greatest_of_solvent`; the keeps-everything property of `⊤` enters as the meaning of the top tuple (stage 1 = all existing particulars continue), stated as the module's `keeps` hypothesis. No union closure.
2. `reciprocity_dominance_solvent`: for any rival `q` (no closure assumption on the family), `keeps (q ⟨0, _⟩) m → keeps (o ⟨0, _⟩) m`, by monotonicity from 1.

**Note.** Gemini's P2b sketch (`MasterSolvency`, `ContinuationValue`) is not against the real module types; the target above is. The below-solvency branch keeps `hF` unchanged.

## 2. A1 register rows as an instance structure (optional, from PĀTAI 2, P4)

The nine rows of §24.1 are an inventory; an optional formalisation is a finite enumeration with per-row witness types, feeding `H5Closure`'s effect enforcement. Low priority; prose statement of record suffices for the edition.

---

*Dispositions of PĀTAI 2's other items: P1 folded (§15.2 restated around `ReasonsCompiled.reciprocity_expectation`; ensemble step marked prose). P2a/P2c folded (UnionRealizable already retired; §5.4 status note appended). P3 folded (§21.2 bosonic condition sentence). P4 folded (Section 24). P5 folded (doors register map, held).*

---

## Addendum (25 Oct, late — after PĀTAI 3 answers)

**2. Affordable reciprocity (PĀTAI 3 A2, honest form) — PROVED, RECEIPTED, BANKED post-seal (BANKS/2026-10-25-affordable-reciprocity/).** `reciprocity_dominance_affordable` (module text below) compiled clean against `Greatestness`/`PremiseFloor`/`UnionClosure` (zero output, leanchecker exit 0); the file is held at `/tmp/AffordableReciprocity.lean` until the running audit completes, then banks to `BANKS/2026-10-25-affordable-reciprocity/` and folds next cycle. Content: below full solvency, a rival whose union with the canonical option is realisable (`UnionRealizable`) and affordable is outcome-contained in it, so any mind the rival keeps, the canonical regime keeps — no family closure, no solvency.

**3. Product telescoping error budget (PĀTAI 3 A1's compilable half) — REGISTERED.** For contractions (unitaries) on a normed space: ‖∏Aⱼ − ∏Wⱼ‖ ≤ Σⱼ‖Aⱼ − Wⱼ‖, by the telescoping identity U − W = Σⱼ (∏ᵢ<ⱼ Uᵢ)(Uⱼ − Wⱼ)(∏ₘ>ⱼ Wₘ) and submultiplicativity. Gemini's prose derivation is correct; its offered Lean proved only the triangle inequality's neighbor and is rejected. With per-factor ε/K this is the error-budget engine of A1.

**4. Stone 2's residue — ROUTE SETTLED, honest status defined.** The gate-set clause reduces to the **Solovay–Kitaev theorem carried as a cited published theorem** (the DKLP precedent: §23.8 already carries published mathematics as cited inputs), plus item 3's compiled telescoping lemma, plus the already-compiled `TwoLevel.two_level_decomposition`. SK is not in Mathlib; compiling it is a real project and a 5.0-scale ambition, not an evening. Gemini's "terminal QED" module (circular: its typeclass hypothesis is the theorem) is rejected and will not enter the tree under any circumstances.

```lean
-- AffordableReciprocity.lean (verified; held for banking)
import Snuffy.UnionClosure
open Snuffy.Greatestness Snuffy.UnionClosure
namespace Snuffy.AffordableReciprocity
variable {n : ℕ} {L : Fin n → Type*} [∀ i, SemilatticeSup (L i)]
theorem reciprocity_dominance_affordable {P : Type*} (hn : 0 < n)
    (keeps : L ⟨0, hn⟩ → P → Prop) (hmono : ∀ x y, x ≤ y → ∀ m, keeps x m → keeps y m)
    {R : Set (∀ i, L i)} {c : (∀ i, L i) → ℝ} {B : ℝ} (hR : UnionRealizable R)
    {o : ∀ i, L i} (ho : Aligned (budgetFamily R c B) o) {q : ∀ i, L i}
    (hq : q ∈ R) (hcost : c (q ⊔ o) ≤ B) (m : P) (hm : keeps (q ⟨0, hn⟩) m) :
    keeps (o ⟨0, hn⟩) m :=
  hmono _ _ (dominates_of_affordable hR ho hq hcost ⟨0, hn⟩) m hm
end Snuffy.AffordableReciprocity
```
