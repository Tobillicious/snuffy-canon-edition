/-
Mathematical criterion for a proposed nonnegative spectral power integral.
This does not identify the integral with an actual device's complete power,
nor infer spectral nullification from a gap or charge commutator.
-/
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

namespace Snuffy.HoldingSpectralCriterion

open MeasureTheory
open scoped ENNReal

variable {Ω : Type*} [MeasurableSpace Ω] {μ : Measure Ω}

/-- With a positive kernel, zero finite spectral power is equivalent to
vanishing of the nonnegative spectrum under the actual bath measure. -/
theorem zero_power_iff_spectrum_ae_zero {K f : Ω → ℝ}
    (hK : ∀ᵐ ω ∂μ, 0 < K ω) (hf : ∀ᵐ ω ∂μ, 0 ≤ f ω)
    (hint : Integrable (fun ω => K ω * f ω) μ) :
    (∫ ω, K ω * f ω ∂μ) = 0 ↔ ∀ᵐ ω ∂μ, f ω = 0 := by
  have hn : ∀ᵐ ω ∂μ, 0 ≤ K ω * f ω := by
    filter_upwards [hK, hf] with ω hk hfω
    exact mul_nonneg hk.le hfω
  rw [integral_eq_zero_iff_of_nonneg_ae hn hint]
  constructor
  · intro hz
    filter_upwards [hK, hz] with ω hk hzω
    exact (mul_eq_zero.mp hzω).resolve_left hk.ne'
  · intro hz
    filter_upwards [hz] with ω hzω
    simp [hzω]

/-- Exact separation under the bath measure is a sufficient zero-power
certificate. A physical application must construct the null set and the
actual spectral support; their names alone do not supply this certificate. -/
theorem zero_power_of_spectral_separation {K f : Ω → ℝ} {A : Set Ω}
    (hgap : μ A = 0) (hsupport : ∀ ω ∉ A, f ω = 0) :
    (∫ ω, K ω * f ω ∂μ) = 0 := by
  have ha : ∀ᵐ ω ∂μ, ω ∉ A := by
    simpa [ae_iff] using hgap
  apply integral_eq_zero_of_ae
  filter_upwards [ha] with ω hω
  simp [hsupport ω hω]

/-- The nonnegative extended integral needs measurability, but no finite
integrability premise. -/
theorem zero_extended_power_iff_spectrum_ae_zero {K f : Ω → ENNReal}
    (hK : Measurable K) (hf : Measurable f) (hpos : ∀ᵐ ω ∂μ, 0 < K ω) :
    (∫⁻ ω, K ω * f ω ∂μ) = 0 ↔ ∀ᵐ ω ∂μ, f ω = 0 := by
  have hprod : Measurable (fun ω => K ω * f ω) := hK.mul hf
  refine (lintegral_eq_zero_iff (μ := μ) hprod).trans ?_
  constructor
  · intro hz
    filter_upwards [hpos, hz] with ω hk hzω
    exact (mul_eq_zero.mp hzω).resolve_left hk.ne'
  · intro hz
    filter_upwards [hz] with ω hzω
    simp [hzω]

/-- A measurable nonnegative control waveform with an actual amplitude cap
has a quantitative finite-duration energy bound. This is one waveform's
charge, not a bound on all lifecycle costs or the number of attempts. -/
theorem switching_energy_bound {a b peak : ℝ} {P : ℝ → ℝ}
    (hab : a ≤ b) (hP : Measurable P) (hbound : ∀ t, 0 ≤ P t ∧ P t ≤ peak) :
    0 ≤ (∫ t in a..b, P t) ∧ (∫ t in a..b, P t) ≤ peak * (b - a) := by
  have hc : IntervalIntegrable (fun _ : ℝ => peak) MeasureTheory.volume a b :=
    intervalIntegrable_const
  have hi : IntervalIntegrable P MeasureTheory.volume a b := by
    apply hc.mono_fun' hP.aestronglyMeasurable.restrict
    exact ae_of_all _ fun t => by
      simpa only [Real.norm_eq_abs, abs_of_nonneg (hbound t).1] using (hbound t).2
  refine ⟨intervalIntegral.integral_nonneg_of_forall hab (fun t => (hbound t).1), ?_⟩
  have hm := intervalIntegral.integral_mono hab hi hc (fun t => (hbound t).2)
  simpa only [intervalIntegral.integral_const, smul_eq_mul, mul_comm] using hm

/-- The exact conditional model certificate: a constructed null spectral
support eliminates this modeled holding term; the control pulse keeps its
explicit finite charge. A hardware application still needs the physical
power identity, actual support and amplitude certificates, and full ledger. -/
theorem conditional_model_certificate {K f : Ω → ℝ} {A : Set Ω}
    (hgap : μ A = 0) (hsupport : ∀ ω ∉ A, f ω = 0)
    {a b peak : ℝ} {P : ℝ → ℝ} (hab : a ≤ b) (hP : Measurable P)
    (hbound : ∀ t, 0 ≤ P t ∧ P t ≤ peak) :
    (∫ ω, K ω * f ω ∂μ) = 0 ∧
      0 ≤ (∫ t in a..b, P t) ∧ (∫ t in a..b, P t) ≤ peak * (b - a) :=
  ⟨zero_power_of_spectral_separation hgap hsupport,
    switching_energy_bound hab hP hbound⟩

end Snuffy.HoldingSpectralCriterion
