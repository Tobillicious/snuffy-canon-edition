/-
Snuffy — Canon Edition 4.2 working: the doubling schedule's transfer bill has a
constant long-run rate (quantum-coherence branch; Codex handoff item 3, the
cost join).

  * poly_le_two_pow — every polynomial in `n` is at most `C · 2^n`, with `C`
    independent of `n`.
  * transfer_bill_le — per-stage transfer cost `(a + b j)^κ`, polynomial in the
    stage index (so polynomial in the stage code size `n_j`, since `n_j^η` grows
    linearly in `j`), sums over the first `J` stages to at most `C · 2^J`.
  * transfer_bill_linear_in_age — when the first `J` stages cover age `t`
    (`2^J ≤ 2 t`), the summed transfer bill is at most `C t` with the same `C`
    at every age: the transfers add an age-independent constant to the holding
    rate. Every transfer charge is included as supplied; nothing is averaged.

Zero `sorry`. Mathlib rev 56a005855ea1.
-/

import Snuffy.StageSchedule
import Mathlib.Analysis.SpecificLimits.Normed

open Finset Filter Topology

namespace Snuffy.TransferRate

/-- **A polynomial is at most a constant times `2^n`.** -/
theorem poly_le_two_pow (k : ℕ) : ∃ C : ℝ, ∀ n : ℕ, (n : ℝ) ^ k ≤ C * 2 ^ n := by
  have ht : Tendsto (fun n : ℕ => (n : ℝ) ^ k / (2 : ℝ) ^ n) atTop (𝓝 0) :=
    tendsto_pow_const_div_const_pow_of_one_lt k (by norm_num)
  obtain ⟨C, hC⟩ := ht.bddAbove_range
  refine ⟨C, fun n => ?_⟩
  have h2 : (0 : ℝ) < 2 ^ n := by positivity
  have hle : (n : ℝ) ^ k / 2 ^ n ≤ C := hC ⟨n, rfl⟩
  rwa [div_le_iff₀ h2] at hle

/-- **The summed transfer bill over `J` stages is at most `C · 2^J`.** -/
theorem transfer_bill_le (a b κ : ℕ) :
    ∃ C : ℝ, ∀ J : ℕ, ((∑ j ∈ range J, (a + b * j) ^ κ : ℕ) : ℝ) ≤ C * 2 ^ J := by
  obtain ⟨C, hC⟩ := poly_le_two_pow (κ + 1)
  refine ⟨2 * ((a + b : ℕ) : ℝ) ^ κ * C, fun J => ?_⟩
  have hsum := Snuffy.StageSchedule.stage_cost_le a b κ J
  have hlin : a + b * J ≤ (a + b) * (J + 1) := by nlinarith
  have hnat : J * (a + b * J) ^ κ ≤ (a + b) ^ κ * (J + 1) ^ (κ + 1) := by
    calc J * (a + b * J) ^ κ ≤ (J + 1) * ((a + b) * (J + 1)) ^ κ :=
          Nat.mul_le_mul (Nat.le_succ J) (Nat.pow_le_pow_left hlin κ)
      _ = (a + b) ^ κ * (J + 1) ^ (κ + 1) := by rw [mul_pow, pow_succ]; ring
  have hreal : ((∑ j ∈ range J, (a + b * j) ^ κ : ℕ) : ℝ)
      ≤ ((a + b : ℕ) : ℝ) ^ κ * ((J + 1 : ℕ) : ℝ) ^ (κ + 1) := by
    have := le_trans hsum hnat
    exact_mod_cast this
  have hpow := hC (J + 1)
  have hab : (0 : ℝ) ≤ ((a + b : ℕ) : ℝ) ^ κ := by positivity
  calc ((∑ j ∈ range J, (a + b * j) ^ κ : ℕ) : ℝ)
        ≤ ((a + b : ℕ) : ℝ) ^ κ * ((J + 1 : ℕ) : ℝ) ^ (κ + 1) := hreal
    _ ≤ ((a + b : ℕ) : ℝ) ^ κ * (C * 2 ^ (J + 1)) := mul_le_mul_of_nonneg_left hpow hab
    _ = 2 * ((a + b : ℕ) : ℝ) ^ κ * C * 2 ^ J := by rw [pow_succ]; ring

/-- **The transfer bill is linear in age with an age-independent constant.** -/
theorem transfer_bill_linear_in_age (a b κ : ℕ) :
    ∃ C : ℝ, ∀ (J : ℕ) (t : ℝ), (2 : ℝ) ^ J ≤ 2 * t →
      ((∑ j ∈ range J, (a + b * j) ^ κ : ℕ) : ℝ) ≤ C * t := by
  obtain ⟨C, hC⟩ := transfer_bill_le a b κ
  refine ⟨2 * max C 0, fun J t ht => ?_⟩
  have h1 := hC J
  have hm : C * 2 ^ J ≤ max C 0 * 2 ^ J :=
    mul_le_mul_of_nonneg_right (le_max_left C 0) (by positivity)
  have hm2 : max C 0 * 2 ^ J ≤ max C 0 * (2 * t) :=
    mul_le_mul_of_nonneg_left ht (le_max_right C 0)
  nlinarith

end Snuffy.TransferRate
