/-
Snuffy — Canon Edition 4.2 working: premise 5 with the Bennett counterpart
constructed (Part I premise 5; §17; §23.8).

An option is a policy together with the implementation of its administration.
The administration is either irreversible — a joint register–bath dynamics
that leaves the register in the law of an overwrite `f` — or reversible — a
bijection of the register alone, such as Bennett's compute–copy–uncompute
cycle (`Bennett.bennettEquiv`), which writes `f x` into a clean output and
returns the workspace exactly (`Bennett.bennett_compute_uncompute`).

The cost of an option is the base cost of its policy plus the energy its
administration delivers to the bath (`Landauer.heat`). The outcome stages
before the resource stage are the policy's outcomes; the resource stage
records the residual slack `B − cost` through a strictly monotone reading.
The Bennett counterpart of an option runs the same policy with reversible
administration.

  * counterpart_heat_zero — reversible administration delivers exactly zero
    heat (`Bennett.heat_reversible`).
  * merging_heat_pos — merging irreversible administration delivers strictly
    positive heat (`Bennett.heat_irreversible`).
  * counterpart_feasible, counterpart_same, counterpart_more_slack — the
    counterpart is realisable whenever the option is, has the same outcomes
    before the resource stage, the same base cost, and strictly more slack.
  * premise5_constructed — no canonical option has merging irreversible
    administration. Every hypothesis on the counterpart is derived above.
  * bennett_counterpart_computes — the reversible counterpart instantiated
    by the Bennett cycle computes the same administration result, with a
    clean workspace.

Zero `sorry`. Mathlib rev 56a005855ea1.
-/

import Snuffy.Bennett
import Snuffy.Greatestness

open Finset

namespace Snuffy.BennettCounterpart

open Snuffy.Landauer Snuffy.Bennett Snuffy.Greatestness

/-- How an option's administration is implemented. -/
inductive Mode (Reg Bath : Type*)
  | irreversible (σ : Reg × Bath ≃ Reg × Bath) (f : Reg → Reg)
  | reversible (e : Reg ≃ Reg)

variable {Reg Bath Pol : Type*} [Fintype Reg] [Fintype Bath] [Nonempty Bath] [DecidableEq Reg]

/-- The energy the administration delivers to the bath. -/
noncomputable def heatOf (p : Reg → ℝ) (kT : ℝ) (E : Bath → ℝ) : Mode Reg Bath → ℝ
  | .irreversible σ _ => heat p (1 / kT) E σ
  | .reversible e => heat p (1 / kT) E (e.prodCongr (Equiv.refl Bath))

/-- Irreversible administration that leaves the register in the law of `f`,
where `f` merges two register states of positive probability. -/
def Merging (p : Reg → ℝ) (kT : ℝ) (E : Bath → ℝ) : Mode Reg Bath → Prop
  | .irreversible σ f => margA (evolve p (1 / kT) E σ) = push p f ∧
      ∃ x₁ x₂, x₁ ≠ x₂ ∧ f x₁ = f x₂ ∧ 0 < p x₁ ∧ 0 < p x₂
  | .reversible _ => False

omit [DecidableEq Reg] [Nonempty Bath] in
theorem counterpart_heat_zero (p : Reg → ℝ) (hp1 : ∑ x, p x = 1) (kT : ℝ) (E : Bath → ℝ)
    (e : Reg ≃ Reg) : heatOf p kT E (.reversible e) = 0 :=
  heat_reversible p hp1 (1 / kT) E e

theorem merging_heat_pos (p : Reg → ℝ) (hp : ∀ x, 0 ≤ p x) (hp1 : ∑ x, p x = 1)
    {kT : ℝ} (hkT : 0 < kT) (E : Bath → ℝ) (m : Mode Reg Bath) (hm : Merging p kT E m) :
    0 < heatOf p kT E m := by
  cases m with
  | reversible e => exact hm.elim
  | irreversible σ f =>
      obtain ⟨himpl, x₁, x₂, hne, hf, h₁, h₂⟩ := hm
      obtain ⟨hpos, hle⟩ := heat_irreversible p hp hp1 hkT E σ f himpl hne hf h₁ h₂
      exact lt_of_lt_of_le hpos hle

variable {n : ℕ} {L : Fin n → Type*} [∀ i, SemilatticeSup (L i)]

/-- The outcome tuple of an option: the policy's outcomes, with the resource
stage `j` reading the residual slack. -/
noncomputable def tuple (out : Pol → ∀ i, L i) (j : Fin n) (stage : ℝ → L j)
    (base : Pol → ℝ) (B : ℝ) (p : Reg → ℝ) (kT : ℝ) (E : Bath → ℝ)
    (x : Pol × Mode Reg Bath) : ∀ i, L i :=
  Function.update (out x.1) j (stage (B - (base x.1 + heatOf p kT E x.2)))

/-- The feasible family: realisable policies, any implementation, cost within
budget. -/
def feasible (Rpol : Set Pol) (out : Pol → ∀ i, L i) (j : Fin n) (stage : ℝ → L j)
    (base : Pol → ℝ) (B : ℝ) (p : Reg → ℝ) (kT : ℝ) (E : Bath → ℝ) : Set (∀ i, L i) :=
  {t | ∃ x : Pol × Mode Reg Bath, x.1 ∈ Rpol ∧ base x.1 + heatOf p kT E x.2 ≤ B ∧
    tuple out j stage base B p kT E x = t}

omit [Nonempty Bath] [DecidableEq Reg] [∀ i, SemilatticeSup (L i)] in
theorem counterpart_same (out : Pol → ∀ i, L i) (j : Fin n) (stage : ℝ → L j)
    (base : Pol → ℝ) (B : ℝ) (p : Reg → ℝ) (kT : ℝ) (E : Bath → ℝ)
    (x : Pol × Mode Reg Bath) (e : Reg ≃ Reg) :
    ∀ i, i < j → tuple out j stage base B p kT E x i =
      tuple out j stage base B p kT E (x.1, .reversible e) i := by
  intro i hi
  simp [tuple, Function.update_of_ne (ne_of_lt hi)]

theorem counterpart_feasible (base : Pol → ℝ) (B : ℝ) (p : Reg → ℝ)
    (hp : ∀ x, 0 ≤ p x) (hp1 : ∑ x, p x = 1) {kT : ℝ} (hkT : 0 < kT) (E : Bath → ℝ)
    (x : Pol × Mode Reg Bath) (hxB : base x.1 + heatOf p kT E x.2 ≤ B)
    (hm : Merging p kT E x.2) (e : Reg ≃ Reg) :
    base x.1 + heatOf p kT E (.reversible e) ≤ B := by
  have h0 := counterpart_heat_zero p hp1 kT E e
  have hpos := merging_heat_pos p hp hp1 hkT E x.2 hm
  linarith

theorem counterpart_more_slack (j : Fin n) (stage : ℝ → L j) (hstage : StrictMono stage)
    (out : Pol → ∀ i, L i) (base : Pol → ℝ) (B : ℝ) (p : Reg → ℝ)
    (hp : ∀ x, 0 ≤ p x) (hp1 : ∑ x, p x = 1) {kT : ℝ} (hkT : 0 < kT) (E : Bath → ℝ)
    (x : Pol × Mode Reg Bath) (hm : Merging p kT E x.2) (e : Reg ≃ Reg) :
    tuple out j stage base B p kT E x j <
      tuple out j stage base B p kT E (x.1, .reversible e) j := by
  have h0 := counterpart_heat_zero p hp1 kT E e
  have hpos := merging_heat_pos p hp hp1 hkT E x.2 hm
  simp only [tuple, Function.update_self]
  apply hstage
  rw [h0]
  linarith

/-- **Premise 5, with the counterpart constructed.** No canonical option has
merging irreversible administration. -/
theorem premise5_constructed (Rpol : Set Pol) (out : Pol → ∀ i, L i) (j : Fin n)
    (stage : ℝ → L j) (hstage : StrictMono stage) (base : Pol → ℝ) (B : ℝ)
    (p : Reg → ℝ) (hp : ∀ x, 0 ≤ p x) (hp1 : ∑ x, p x = 1) {kT : ℝ} (hkT : 0 < kT)
    (E : Bath → ℝ) (e : Reg ≃ Reg) (x : Pol × Mode Reg Bath) (hxR : x.1 ∈ Rpol)
    (hxB : base x.1 + heatOf p kT E x.2 ≤ B)
    (ho : Aligned (feasible Rpol out j stage base B p kT E) (tuple out j stage base B p kT E x)) :
    ¬ Merging p kT E x.2 := by
  intro hm
  refine ho.2 (tuple out j stage base B p kT E (x.1, .reversible e))
    ⟨(x.1, .reversible e), hxR, counterpart_feasible base B p hp hp1 hkT E x hxB hm e, rfl⟩
    ⟨j, counterpart_same out j stage base B p kT E x e, ?_⟩
  exact counterpart_more_slack j stage hstage out base B p hp hp1 hkT E x hm e

/-- **The counterpart computes the same administration result.** Instantiated
by the Bennett cycle for `f = h ∘ g`, the reversible administration writes
`h (g a)` into a clean output and returns the workspace to zero. -/
theorem bennett_counterpart_computes {α γ β : Type*} [AddGroup γ] [AddGroup β]
    (g : α → γ) (h : γ → β) (a : α) :
    bennettEquiv g h (a, 0, 0) = (a, 0, h (g a)) :=
  bennett_compute_uncompute g h a

end Snuffy.BennettCounterpart
