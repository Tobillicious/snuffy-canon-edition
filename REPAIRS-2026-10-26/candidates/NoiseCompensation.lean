/-
Exact inverse algebra for a specified local Pauli syndrome channel.
This development candidate is outside the canon. It does not assert positivity
of the inverse law or identify the physical preparation circuit with the model.
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

open Finset

namespace NoiseCompensationPrototype

noncomputable section

variable {S : Type*}

def pauliNoise (p : ℝ) (A B : S → S) (f : S → ℝ) (x : S) : ℝ :=
  (1 - p) * f x + (p / 3) * (f (A x) + f (B x) + f (A (B x)))

def pauliInverse (p : ℝ) (A B : S → S) (f : S → ℝ) (x : S) : ℝ :=
  ((1 - p / 3) * f x - (p / 3) * (f (A x) + f (B x) + f (A (B x)))) /
    (1 - 4 * p / 3)

theorem pauli_noise_inverse (p : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B)
    (hAB : ∀ x, A (B x) = B (A x)) (hp : 1 - 4 * p / 3 ≠ 0)
    (f : S → ℝ) (x : S) :
    pauliNoise p A B (pauliInverse p A B f) x = f x := by
  have ha (y : S) : A (A y) = y := hA y
  have hb (y : S) : B (B y) = y := hB y
  have hd : (3 : ℝ) - p * 4 ≠ 0 := by
    intro hz
    apply hp
    linarith
  simp only [pauliNoise, pauliInverse, hAB, ha, hb]
  field_simp [hd]
  ring

theorem pauli_noise_sum [Fintype S] (p : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B) (f : S → ℝ) :
    ∑ x, pauliNoise p A B f x = ∑ x, f x := by
  classical
  have ha := hA.bijective.sum_comp f
  have hb := hB.bijective.sum_comp f
  have hab : (∑ x, f (A (B x))) = ∑ x, f x := by
    simpa only [Function.comp_apply] using (hA.bijective.comp hB.bijective).sum_comp f
  simp only [pauliNoise, sum_add_distrib, ← mul_sum]
  rw [ha, hb, hab]
  ring

theorem pauli_inverse_sum [Fintype S] (p : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B)
    (hAB : ∀ x, A (B x) = B (A x)) (hp : 1 - 4 * p / 3 ≠ 0) (f : S → ℝ) :
    ∑ x, pauliInverse p A B f x = ∑ x, f x := by
  have h := pauli_noise_sum p A B hA hB (pauliInverse p A B f)
  have hi : pauliNoise p A B (pauliInverse p A B f) = f :=
    funext (pauli_noise_inverse p A B hA hB hAB hp f)
  rw [hi] at h
  exact h.symm

theorem pauli_noise_upper (p C : ℝ) (A B : S → S) (f g : S → ℝ)
    (hp0 : 0 ≤ p) (hp1 : p ≤ 1) (hfg : ∀ x, f x ≤ C * g x) (x : S) :
    pauliNoise p A B f x ≤ C * pauliNoise p A B g x := by
  have hfirst := mul_le_mul_of_nonneg_left (hfg x) (sub_nonneg.mpr hp1)
  have hsum := add_le_add (add_le_add (hfg (A x)) (hfg (B x))) (hfg (A (B x)))
  have hrest := mul_le_mul_of_nonneg_left hsum (div_nonneg hp0 (by norm_num : (0 : ℝ) ≤ 3))
  dsimp [pauliNoise]
  calc
    (1 - p) * f x + (p / 3) * (f (A x) + f (B x) + f (A (B x)))
        ≤ (1 - p) * (C * g x) + (p / 3) * (C * g (A x) + C * g (B x) + C * g (A (B x))) :=
      add_le_add hfirst hrest
    _ = C * ((1 - p) * g x + (p / 3) * (g (A x) + g (B x) + g (A (B x)))) := by ring

theorem compensated_output (p C : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B)
    (hAB : ∀ x, A (B x) = B (A x)) (hp : 1 - 4 * p / 3 ≠ 0)
    (hp0 : 0 ≤ p) (hp1 : p ≤ 1) (μ π : S → ℝ)
    (hμ : ∀ x, μ x ≤ C * pauliInverse p A B π x) (x : S) :
    pauliNoise p A B μ x ≤ C * π x := by
  have h := pauli_noise_upper p C A B μ (pauliInverse p A B π) hp0 hp1 hμ x
  rwa [pauli_noise_inverse p A B hA hB hAB hp π x] at h

/-- Polynomial resulting from the separately enumerated 16^3 fault paths
of three CNOTs. The enumeration-to-circuit correspondence is not asserted
by this scalar identity. -/
theorem swap_target_rate (p : ℝ) :
    12 * (1 - p) ^ 2 * (p / 15) + 168 * (1 - p) * (p / 15) ^ 2 +
        844 * (p / 15) ^ 3 = (1 - (1 - 16 * p / 15) ^ 3) / 4 := by
  ring

end

end NoiseCompensationPrototype
