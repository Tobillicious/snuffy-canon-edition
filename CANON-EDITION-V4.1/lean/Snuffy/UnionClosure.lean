/-
Snuffy — Canon Edition v4.1: union closure from a resource model — when
universal greatestness holds, and exactly what holds when it does not
(Chapter 5, §5.3–5.4; P-emu(c)).

`Greatestness.greatest_of_union_closed` takes union closure of the whole
feasible family as its hypothesis. Here P-emu(c) is split into its two
ingredients:

  * realisability — concurrent emulation through the shared action interface
    (premise 4) realises the stage-wise union of any two realisable outcome
    tuples (`UnionRealizable`, a modelling premise);
  * resources — the canonical regime's feasible family is the realisable
    tuples of cost at most its budget `B` (`budgetFamily`), so the budget is a
    checkable inequality, like the income condition.

Results:

  * aligned_never_below — whatever the budget, no feasible rival is canonically
    above the canonical option.
  * dominates_of_affordable — every realisable rival whose union with the
    canonical outcome is affordable is contained in it stage by stage, and is
    strictly below it or an exact mirror.
  * dominates_within_slack — with subadditive cost, every finite set of
    realisable rivals whose total cost fits in the canonical slack `B − c(o)`
    is contained in the canonical outcome.
  * union_closed_of_affordable — when every pair of feasible tuples is jointly
    affordable, the budget family is union-closed, and universal greatestness
    holds outright (via `Greatestness.greatest_of_union_closed`).
  * greatest_needs_budget — sharpness: without the budget condition a feasible
    rival can keep a particular the canonical option does not.

Zero `sorry`. Mathlib rev 56a005855ea1.
-/

import Snuffy.Greatestness
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Card
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith

open Snuffy.Greatestness Finset

namespace Snuffy.UnionClosure

variable {n : ℕ} {L : Fin n → Type*} [∀ i, SemilatticeSup (L i)]

/-- The canonical regime's feasible family within budget `B`: realisable
outcome tuples of cost at most `B`. -/
def budgetFamily (R : Set (∀ i, L i)) (c : (∀ i, L i) → ℝ) (B : ℝ) : Set (∀ i, L i) :=
  {x | x ∈ R ∧ c x ≤ B}

/-- Realisability is union-closed: concurrent emulation through the shared
action interface realises the stage-wise union of any two realisable outcome
tuples. Resources are accounted for separately, by the cost. -/
def UnionRealizable (R : Set (∀ i, L i)) : Prop := ∀ x ∈ R, ∀ y ∈ R, x ⊔ y ∈ R

/-- **Never canonically below.** Whatever the budget, no feasible rival lies
strictly above the canonical option in the canonical order. -/
theorem aligned_never_below {F : Set (∀ i, L i)} {o : ∀ i, L i} (ho : Aligned F o) :
    ∀ q ∈ F, ¬ LexLt o q := ho.2

/-- **Dominance of affordable rivals.** If realisability is union-closed, every
realisable rival `q` whose union with the canonical outcome fits in the budget
is contained in the canonical outcome, stage by stage. -/
theorem dominates_of_affordable {R : Set (∀ i, L i)} {c : (∀ i, L i) → ℝ} {B : ℝ}
    (hR : UnionRealizable R) {o : ∀ i, L i} (ho : Aligned (budgetFamily R c B) o)
    {q : ∀ i, L i} (hq : q ∈ R) (hcost : c (q ⊔ o) ≤ B) : q ≤ o := by
  have hu : q ⊔ o ∈ budgetFamily R c B := ⟨hR q hq o ho.1.1, hcost⟩
  rcases lexLe_of_le (le_sup_right : o ≤ q ⊔ o) with heq | hlt
  · rw [heq]
    exact le_sup_left
  · exact absurd hlt (ho.2 _ hu)

/-- Affordable rivals are strictly below the canonical option or exact mirrors. -/
theorem strict_of_affordable {R : Set (∀ i, L i)} {c : (∀ i, L i) → ℝ} {B : ℝ}
    (hR : UnionRealizable R) {o : ∀ i, L i} (ho : Aligned (budgetFamily R c B) o)
    {q : ∀ i, L i} (hq : q ∈ R) (hcost : c (q ⊔ o) ≤ B) : q = o ∨ LexLt q o :=
  lexLe_of_le (dominates_of_affordable hR ho hq hcost)

/-- The union of the canonical outcome with any finite set of realisable rivals
is realisable and costs at most the sum, under subadditive cost. -/
theorem exists_union_bound {R : Set (∀ i, L i)} {c : (∀ i, L i) → ℝ} (hR : UnionRealizable R)
    (hsub : ∀ x y, c (x ⊔ y) ≤ c x + c y) {o : ∀ i, L i} (ho : o ∈ R) {ι : Type*}
    (q : ι → ∀ i, L i) (s : Finset ι) (hq : ∀ j ∈ s, q j ∈ R) :
    ∃ u ∈ R, o ≤ u ∧ (∀ j ∈ s, q j ≤ u) ∧ c u ≤ c o + ∑ j ∈ s, c (q j) := by
  classical
  induction s using Finset.induction_on with
  | empty => exact ⟨o, ho, le_rfl, by simp, by simp⟩
  | insert a s ha ih =>
    obtain ⟨u, hu, hou, hqu, hcu⟩ := ih fun j hj => hq j (mem_insert_of_mem hj)
    refine ⟨u ⊔ q a, hR u hu (q a) (hq a (mem_insert_self a s)), hou.trans le_sup_left,
      fun j hj => ?_, ?_⟩
    · rcases mem_insert.mp hj with rfl | hj
      · exact le_sup_right
      · exact (hqu j hj).trans le_sup_left
    · rw [sum_insert ha]
      linarith [hsub u (q a)]

/-- **Dominance within slack.** With subadditive cost, every finite set of
realisable rivals whose total cost fits in the canonical slack `B − c(o)` is
contained in the canonical outcome, stage by stage: the canonical regime keeps
everything any of them keeps. -/
theorem dominates_within_slack {R : Set (∀ i, L i)} {c : (∀ i, L i) → ℝ} {B : ℝ}
    (hR : UnionRealizable R) (hsub : ∀ x y, c (x ⊔ y) ≤ c x + c y) {o : ∀ i, L i}
    (ho : Aligned (budgetFamily R c B) o) {ι : Type*} (q : ι → ∀ i, L i) (s : Finset ι)
    (hq : ∀ j ∈ s, q j ∈ R) (hslack : ∑ j ∈ s, c (q j) ≤ B - c o) : ∀ j ∈ s, q j ≤ o := by
  obtain ⟨u, hu, hou, hqu, hcu⟩ := exists_union_bound hR hsub ho.1.1 q s hq
  have huF : u ∈ budgetFamily R c B := ⟨hu, by linarith⟩
  rcases lexLe_of_le hou with heq | hlt
  · intro j hj
    rw [heq]
    exact hqu j hj
  · exact absurd hlt (ho.2 _ huF)

/-- **Universal greatestness from the budget.** If realisability is
union-closed and every pair of feasible tuples is jointly affordable, the
budget family is union-closed, so every canonical option contains every
feasible option. -/
theorem union_closed_of_affordable {R : Set (∀ i, L i)} {c : (∀ i, L i) → ℝ} {B : ℝ}
    (hR : UnionRealizable R)
    (hjoint : ∀ x ∈ budgetFamily R c B, ∀ y ∈ budgetFamily R c B, c (x ⊔ y) ≤ B) :
    ∀ x ∈ budgetFamily R c B, ∀ y ∈ budgetFamily R c B, x ⊔ y ∈ budgetFamily R c B :=
  fun x hx y hy => ⟨hR x hx.1 y hy.1, hjoint x hx y hy⟩

theorem greatest_of_affordable {R : Set (∀ i, L i)} {c : (∀ i, L i) → ℝ} {B : ℝ}
    (hR : UnionRealizable R)
    (hjoint : ∀ x ∈ budgetFamily R c B, ∀ y ∈ budgetFamily R c B, c (x ⊔ y) ≤ B)
    {o : ∀ i, L i} (ho : Aligned (budgetFamily R c B) o) :
    ∀ q ∈ budgetFamily R c B, q ≤ o :=
  greatest_of_union_closed (union_closed_of_affordable hR hjoint) ho

/-- **Sharpness.** The budget condition cannot be dropped: with one stage, two
particulars, each kept at unit cost, and budget one, the option keeping the
first particular is canonical, yet the feasible option keeping the second is not
contained in it. -/
theorem greatest_needs_budget :
    ∃ (R : Set (Fin 1 → Finset Bool)) (c : (Fin 1 → Finset Bool) → ℝ) (B : ℝ)
      (o q : Fin 1 → Finset Bool),
      UnionRealizable (L := fun _ => Finset Bool) R ∧
      Aligned (L := fun _ => Finset Bool) (budgetFamily (L := fun _ => Finset Bool) R c B) o ∧
      q ∈ budgetFamily (L := fun _ => Finset Bool) R c B ∧ ¬ q ≤ o := by
  refine ⟨Set.univ, fun x => ((x 0).card : ℝ), 1, fun _ => {true}, fun _ => {false},
    fun _ _ _ _ => trivial, ⟨⟨trivial, by simp⟩, ?_⟩, ⟨trivial, by simp⟩, ?_⟩
  · rintro q' ⟨-, hc⟩ ⟨j, -, hlt⟩
    have hj : j = 0 := Subsingleton.elim j 0
    subst hj
    have hcard : ({true} : Finset Bool).card < (q' 0).card := Finset.card_lt_card hlt
    simp only [Finset.card_singleton] at hcard
    have : (2 : ℝ) ≤ ((q' 0).card : ℝ) := by exact_mod_cast hcard
    simp only at hc
    linarith
  · intro h
    have h0 := h 0
    simp at h0

end Snuffy.UnionClosure
