/-
Snuffy — Canon Edition: the Mathlib analytic bridge (H5, operator level).

Bridges the discrete meet algebra of `MeetAlgebra.lean` to continuous Hilbert
space projections. Everything here compiles with zero `sorry` and no vacuous
self-equality theorems. Content:

  * starProjection_fixed_iff_mem — P v = v ↔ v ∈ K (fixed points = the subspace).
  * starProjection_idem        — P ∘ P = P, the operator algebraic identity.
  * altIterate_succ_eq_self    — intersection points are fixed by every
                                 nonempty alternating iterate (P_A ∘ P_B)^(n+1).
  * VonNeumannConvergence      — the SOT limit statement as an explicit
                                 hypothesis structure (per the integrity
                                 briefing: no `sorry`; the topological limit is
                                 declared, not faked).
  * convergence_inf_le        — GENUINE conditional theorem: given the SOT
                                 convergence hypothesis, the limit subspace
                                 contains the intersection: A ⊓ B ≤ AB.

Remaining target, honestly declared: the reverse inclusion AB ≤ A ⊓ B (hence
AB = A ⊓ B) is the analytic half of von Neumann's theorem. Its standard routes
are the norm-decay/Halperin argument or the mean-ergodic theorem — Mathlib
already carries the related machinery
(`ContinuousLinearMap.tendsto_birkhoffAverage_orthogonalProjection` in
`Mathlib.Analysis.InnerProductSpace.MeanErgodic`); deriving the alternating-
projection case from it is the next formalization step and is NOT claimed here.
-/

import Mathlib.Analysis.InnerProductSpace.Projection.Basic

open Submodule Filter

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]

namespace Snuffy.AnalyticBridge

/-! ## Operator algebraic identities (proved unconditionally) -/

/-- The fixed points of the orthogonal projection endomorphism are exactly the
subspace: `P v = v ↔ v ∈ K`. -/
theorem starProjection_fixed_iff_mem {K : Submodule ℂ E} [K.HasOrthogonalProjection] {v : E} :
    K.starProjection v = v ↔ v ∈ K :=
  starProjection_eq_self_iff

/-- Idempotence: composing the projection endomorphism with itself changes
nothing. -/
theorem starProjection_idem (K : Submodule ℂ E) [K.HasOrthogonalProjection] :
    K.starProjection.comp K.starProjection = K.starProjection := by
  ext x
  show K.starProjection (K.starProjection x) = K.starProjection x
  exact starProjection_fixed_iff_mem.mpr (starProjection_apply_mem K x)

/-! ## The alternating iteration -/

/-- Pointwise alternating iterate: x, then (P_A ∘ P_B) applied n times. -/
noncomputable def altIterate (A B : Submodule ℂ E)
    [A.HasOrthogonalProjection] [B.HasOrthogonalProjection] (x : E) : ℕ → E
  | 0 => x
  | n + 1 => A.starProjection (B.starProjection (altIterate A B x n))

/-- Every point of the intersection is fixed by every nonempty alternating
iterate — the discrete half of the bridge. -/
theorem altIterate_succ_eq_self (A B : Submodule ℂ E)
    [A.HasOrthogonalProjection] [B.HasOrthogonalProjection]
    (x : E) (hx : x ∈ A ⊓ B) (n : ℕ) :
    altIterate A B x (n + 1) = x := by
  have hA : x ∈ A := (mem_inf.mp hx).1
  have hB : x ∈ B := (mem_inf.mp hx).2
  induction n with
  | zero =>
      show A.starProjection (B.starProjection x) = x
      rw [starProjection_fixed_iff_mem.mpr hB]
      exact starProjection_fixed_iff_mem.mpr hA
  | succ k ih =>
      show A.starProjection (B.starProjection (altIterate A B x (k + 1))) = x
      rw [ih, starProjection_fixed_iff_mem.mpr hB]
      exact starProjection_fixed_iff_mem.mpr hA

/-! ## The SOT convergence hypothesis (declared, not faked) -/

/-- Von Neumann convergence as an explicit hypothesis structure: the alternating
iterates converge pointwise to the projection onto `AB`. This is the statement
of von Neumann's theorem; it is supplied as a hypothesis, never `sorry`ed. -/
structure VonNeumannConvergence (A B AB : Submodule ℂ E)
    [A.HasOrthogonalProjection] [B.HasOrthogonalProjection]
    [AB.HasOrthogonalProjection] where
  /-- Pointwise (strong operator topology) convergence to `AB.starProjection`. -/
  limit : ∀ x : E, Tendsto (fun n => altIterate A B x n) atTop (nhds (AB.starProjection x))

/-! ## A genuine conditional theorem -/

/-- Given the SOT convergence hypothesis, the limit subspace contains the
intersection: `A ⊓ B ≤ AB`. Proof: intersection points are fixed by every
nonempty iterate, so their iterate sequence is eventually constant with value
`x`; the limit is therefore `x` by uniqueness of limits in a T2 space, and the
fixed-point characterization gives `x ∈ AB`. -/
theorem convergence_inf_le (A B AB : Submodule ℂ E)
    [A.HasOrthogonalProjection] [B.HasOrthogonalProjection]
    [AB.HasOrthogonalProjection] (h : VonNeumannConvergence A B AB) :
    A ⊓ B ≤ AB := by
  intro x hx
  have hconst : ∀ n, altIterate A B x (n + 1) = x := altIterate_succ_eq_self A B x hx
  have hev : (fun n => altIterate A B x n) =ᶠ[atTop] (fun _ => x) := by
    filter_upwards [eventually_ge_atTop 1] with n hn
    obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hn
    rw [Nat.add_comm]
    exact hconst k
  have hlimitxisx : AB.starProjection x = x :=
    tendsto_nhds_unique (h.limit x) (tendsto_const_nhds.congr' hev.symm)
  exact starProjection_fixed_iff_mem.mp hlimitxisx

end Snuffy.AnalyticBridge
