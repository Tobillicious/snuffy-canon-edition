/-
Anisotropic Pauli-channel compensation. Development candidate only.
This checks the exact four-character inverse and one-sided composition;
positivity and physical interface hypotheses are proved separately in prose.
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

open Finset

namespace PauliInterfacePrototype

noncomputable section

variable {S : Type*}

def weightedPauli (a b c d : ℝ) (A B : S → S) (f : S → ℝ) (x : S) : ℝ :=
  a * f x + b * f (A x) + c * f (B x) + d * f (A (B x))

def inverseI (a b c d : ℝ) : ℝ :=
  ((a + b + c + d)⁻¹ + (a + b - c - d)⁻¹ +
    (a - b + c - d)⁻¹ + (a - b - c + d)⁻¹) / 4

def inverseX (a b c d : ℝ) : ℝ :=
  ((a + b + c + d)⁻¹ + (a + b - c - d)⁻¹ -
    (a - b + c - d)⁻¹ - (a - b - c + d)⁻¹) / 4

def inverseZ (a b c d : ℝ) : ℝ :=
  ((a + b + c + d)⁻¹ - (a + b - c - d)⁻¹ +
    (a - b + c - d)⁻¹ - (a - b - c + d)⁻¹) / 4

def inverseY (a b c d : ℝ) : ℝ :=
  ((a + b + c + d)⁻¹ - (a + b - c - d)⁻¹ -
    (a - b + c - d)⁻¹ + (a - b - c + d)⁻¹) / 4

theorem fourier_inverse_coefficients (a b c d : ℝ)
    (h0 : a + b + c + d ≠ 0) (h1 : a + b - c - d ≠ 0)
    (h2 : a - b + c - d ≠ 0) (h3 : a - b - c + d ≠ 0) :
    a * inverseI a b c d + b * inverseX a b c d +
        c * inverseZ a b c d + d * inverseY a b c d = 1 ∧
    a * inverseX a b c d + b * inverseI a b c d +
        c * inverseY a b c d + d * inverseZ a b c d = 0 ∧
    a * inverseZ a b c d + b * inverseY a b c d +
        c * inverseI a b c d + d * inverseX a b c d = 0 ∧
    a * inverseY a b c d + b * inverseZ a b c d +
        c * inverseX a b c d + d * inverseI a b c d = 0 := by
  dsimp [inverseI, inverseX, inverseZ, inverseY]
  and_intros <;> field_simp [h0, h1, h2, h3] <;> ring

theorem weighted_pauli_compose (a b c d e f g h : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B)
    (hAB : ∀ x, A (B x) = B (A x)) (v : S → ℝ) (x : S) :
    weightedPauli a b c d A B (weightedPauli e f g h A B v) x =
      weightedPauli (a*e+b*f+c*g+d*h) (a*f+b*e+c*h+d*g)
        (a*g+b*h+c*e+d*f) (a*h+b*g+c*f+d*e) A B v x := by
  have ha (y : S) : A (A y) = y := hA y
  have hb (y : S) : B (B y) = y := hB y
  simp only [weightedPauli, hAB, ha, hb]
  ring

theorem weighted_pauli_inverse (a b c d : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B)
    (hAB : ∀ x, A (B x) = B (A x))
    (h0 : a + b + c + d ≠ 0) (h1 : a + b - c - d ≠ 0)
    (h2 : a - b + c - d ≠ 0) (h3 : a - b - c + d ≠ 0)
    (v : S → ℝ) (x : S) :
    weightedPauli a b c d A B
      (weightedPauli (inverseI a b c d) (inverseX a b c d)
        (inverseZ a b c d) (inverseY a b c d) A B v) x = v x := by
  rw [weighted_pauli_compose a b c d _ _ _ _ A B hA hB hAB]
  obtain ⟨hi, hx, hz, hy⟩ := fourier_inverse_coefficients a b c d h0 h1 h2 h3
  rw [hi, hx, hz, hy]
  simp only [weightedPauli, one_mul, zero_mul, add_zero]

theorem weighted_pauli_sum [Fintype S] (a b c d : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B) (v : S → ℝ) :
    ∑ x, weightedPauli a b c d A B v x = (a+b+c+d) * ∑ x, v x := by
  classical
  have ha := hA.bijective.sum_comp v
  have hb := hB.bijective.sum_comp v
  have hab : (∑ x, v (A (B x))) = ∑ x, v x := by
    simpa only [Function.comp_apply] using (hA.bijective.comp hB.bijective).sum_comp v
  simp only [weightedPauli, sum_add_distrib, ← mul_sum]
  rw [ha, hb, hab]
  ring

theorem weighted_pauli_upper (a b c d K : ℝ) (A B : S → S)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (v w : S → ℝ) (hvw : ∀ x, v x ≤ K * w x) (x : S) :
    weightedPauli a b c d A B v x ≤ K * weightedPauli a b c d A B w x := by
  have h := add_le_add (add_le_add (add_le_add
    (mul_le_mul_of_nonneg_left (hvw x) ha)
    (mul_le_mul_of_nonneg_left (hvw (A x)) hb))
    (mul_le_mul_of_nonneg_left (hvw (B x)) hc))
    (mul_le_mul_of_nonneg_left (hvw (A (B x))) hd)
  dsimp [weightedPauli] at h ⊢
  calc
    _ ≤ a*(K*w x)+b*(K*w (A x))+c*(K*w (B x))+d*(K*w (A (B x))) := h
    _ = _ := by ring

theorem anisotropic_compensated_output (a b c d K : ℝ) (A B : S → S)
    (hA : Function.Involutive A) (hB : Function.Involutive B)
    (hAB : ∀ x, A (B x) = B (A x))
    (h0 : a + b + c + d ≠ 0) (h1 : a + b - c - d ≠ 0)
    (h2 : a - b + c - d ≠ 0) (h3 : a - b - c + d ≠ 0)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (μ π : S → ℝ)
    (hμ : ∀ x, μ x ≤ K * weightedPauli (inverseI a b c d) (inverseX a b c d)
      (inverseZ a b c d) (inverseY a b c d) A B π x) (x : S) :
    weightedPauli a b c d A B μ x ≤ K * π x := by
  have h := weighted_pauli_upper a b c d K A B ha hb hc hd μ _ hμ x
  rwa [weighted_pauli_inverse a b c d A B hA hB hAB h0 h1 h2 h3 π x] at h

end

end PauliInterfacePrototype
