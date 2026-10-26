/-
Snuffy — Canon Edition 4.2 working: a warm start keeps the stationary failure
bound for all time (quantum-coherence holding branch; the initialisation
problem in its correct form).

For a CSS stabilizer Hamiltonian under Davies dynamics with Pauli jump
operators, the syndrome configuration evolves as a classical Markov chain
whose stationary law `π` is the thermal syndrome distribution. A prepared
initial law `μ` is a warm start with constant `C` when `μ ≤ C π` pointwise.
That is the max-divergence condition, `D_max(μ‖π) ≤ log C`.

  * warm_start — a warm start stays dominated: at every time
    `μ Kᵗ ≤ C π` pointwise.
  * warm_start_event — every event `A`, in particular "the syndrome is
    unstable under the decoder", has probability at most `C · π(A)` at every
    time. With `C = poly(n)` and `π(unstable) ≤ e^{−Θ(n^η)}`
    (arXiv:2605.10943, Theorem 2.6), the stationary bound survives intact.

The empty syndrome is not a warm start, since its constant is
`1/π(∅) = e^{Θ(n)}`. The remaining problem is to prepare a warm start with a
polynomial constant: to sample the metacheck-constrained thermal syndrome
distribution within a polynomial pointwise ratio. With independent
generators that distribution is a product, and exact preparation is a
classical sample followed by a layer of Pauli operators.

Zero `sorry`. Mathlib rev 56a005855ea1.
-/

import Snuffy.Threshold

open Finset

namespace Snuffy.WarmStart

variable {S : Type*} [Fintype S]

/-- One step of the chain with kernel `K`, acting on a law. -/
def step (K : S → S → ℝ) (μ : S → ℝ) : S → ℝ := fun y => ∑ x, μ x * K x y

/-- **A warm start stays dominated at every time.** -/
theorem warm_start (K : S → S → ℝ) (hK : ∀ x y, 0 ≤ K x y) (π μ : S → ℝ)
    (hπ : step K π = π) {C : ℝ} (hμ : ∀ x, μ x ≤ C * π x) :
    ∀ t y, (step K)^[t] μ y ≤ C * π y := by
  intro t
  induction t with
  | zero => exact hμ
  | succ t ih =>
      intro y
      rw [Function.iterate_succ_apply']
      calc step K ((step K)^[t] μ) y = ∑ x, (step K)^[t] μ x * K x y := rfl
        _ ≤ ∑ x, C * π x * K x y := sum_le_sum fun x _ => mul_le_mul_of_nonneg_right (ih x) (hK x y)
        _ = C * step K π y := by unfold step; rw [mul_sum]; refine sum_congr rfl fun x _ => by ring
        _ = C * π y := by rw [hπ]

/-- **Every event keeps the stationary bound up to the warm-start constant.** -/
theorem warm_start_event (K : S → S → ℝ) (hK : ∀ x y, 0 ≤ K x y) (π μ : S → ℝ)
    (hπ : step K π = π) {C : ℝ} (hμ : ∀ x, μ x ≤ C * π x) (A : Finset S) (t : ℕ) :
    ∑ y ∈ A, (step K)^[t] μ y ≤ C * ∑ y ∈ A, π y := by
  rw [mul_sum]
  exact sum_le_sum fun y _ => warm_start K hK π μ hπ hμ t y

end Snuffy.WarmStart
