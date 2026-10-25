/-
Snuffy — Canon Edition 4.2 working: the storage functional of Theorem 8
contracts on every cycle containing an error (§18.3–18.4).

The functional `Φ = E_code + max(0, W_target − E_escrow)/W₀` changes over one
cycle by the sum of the drift interval and the four strokes. With the stroke
bounds of §18.3 — drift at most `λτ`, measurement at most `W_meas/W₀`,
feedback exactly `−ηC`, reset at most `W_reset/W₀`, replenishment at most
`−W_income/W₀` — and solvency `W_meas + W_reset ≤ W_income`:

  * cycle_contracts — the cycle change is at most `−(ηC − λτ)`;
  * margin_pos — timeliness `τ < ηC/λ` makes the margin `σ₀ = ηC − λτ`
    positive;
  * lyapunov_iterate — over `n` such cycles `Φ` falls by at least `nσ₀`.

Zero `sorry`. Mathlib rev 56a005855ea1.
-/

import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

namespace Snuffy.TheoremEightLyapunov

/-- **One cycle contracts.** -/
theorem cycle_contracts {dDrift dI dII dIII dIV lam tau eta C W0 Wm Wr Winc : ℝ}
    (hW0 : 0 < W0) (hdrift : dDrift ≤ lam * tau) (hI : dI ≤ Wm / W0)
    (hII : dII = -(eta * C)) (hIII : dIII ≤ Wr / W0) (hIV : dIV ≤ -(Winc / W0))
    (hsolv : Wm + Wr ≤ Winc) :
    dDrift + dI + dII + dIII + dIV ≤ -(eta * C - lam * tau) := by
  have hdiv : Wm / W0 + Wr / W0 ≤ Winc / W0 := by
    rw [← add_div]
    exact div_le_div_of_nonneg_right hsolv hW0.le
  linarith

/-- **Timeliness gives a positive margin.** -/
theorem margin_pos {lam tau eta C : ℝ} (hlam : 0 < lam) (htime : tau < eta * C / lam) :
    0 < eta * C - lam * tau := by
  rw [lt_div_iff₀ hlam] at htime
  linarith

/-- **Iterated contraction.** -/
theorem lyapunov_iterate (Φ : ℕ → ℝ) {σ : ℝ} (h : ∀ k, Φ (k + 1) ≤ Φ k - σ) :
    ∀ n : ℕ, Φ n ≤ Φ 0 - n * σ := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
      have := h n
      push_cast
      linarith

end Snuffy.TheoremEightLyapunov
