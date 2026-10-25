import Snuffy.ThermoLedger
import Snuffy.QuantumLandauer

open scoped ComplexOrder

namespace Snuffy.WorkBilling

structure WorkBill where
  timeSteps : Nat
  allocatedWork : Nat
  scalingConstant : Nat
  dimFactor : Nat

def workBound (bill : WorkBill) : Prop :=
  bill.allocatedWork <= bill.scalingConstant * (bill.timeSteps ^ bill.dimFactor)

def workAdditive (w1 w2 : Nat) : Nat := w1 + w2

theorem work_nonnegative (w : Nat) : w >= 0 := Nat.zero_le w

theorem work_bound_preserved (bill : WorkBill) (h : workBound bill) :
    workBound bill := h

/-- At a fixed Hamiltonian and Gibbs reference, the complete first-law
ledger gives beta*work = relative-free-energy change + entropy production.
Historical degrees of freedom are included in U and S. -/
theorem decoder_work_balance {β lnZ S₁ S₂ U₁ U₂ W Q : ℝ}
    (hfirst : U₂ - U₁ = W - Q) :
    β * W =
      ((-S₂ + β * U₂ + lnZ) - (-S₁ + β * U₁ + lnZ)) +
      (S₂ - S₁ + β * Q) := by
  have h := Snuffy.ThermoLedger.stroke_identity
    (β := β) (lnZ := lnZ) (I₁ := S₁) (I₂ := S₂) hfirst rfl
  linarith

/-- The work floor uses output minus input relative free energy. -/
theorem decoder_work_floor {β lnZ S₁ S₂ U₁ U₂ W Q : ℝ}
    (hβ : 0 < β) (hfirst : U₂ - U₁ = W - Q)
    (hsecond : 0 ≤ S₂ - S₁ + β * Q) :
    ((-S₂ + β * U₂ + lnZ) - (-S₁ + β * U₁ + lnZ)) / β ≤ W := by
  apply (div_le_iff₀ hβ).mpr
  have h := decoder_work_balance (β := β) (lnZ := lnZ) (S₁ := S₁) (S₂ := S₂) hfirst
  nlinarith

/-- Saturation of that floor is exactly zero entropy production in this
ledger. Joint unitarity alone is not substituted for this condition. -/
theorem decoder_work_floor_saturation {β lnZ S₁ S₂ U₁ U₂ W Q : ℝ}
    (hβ : 0 < β) (hfirst : U₂ - U₁ = W - Q) :
    W = ((-S₂ + β * U₂ + lnZ) - (-S₁ + β * U₁ + lnZ)) / β ↔
      S₂ - S₁ + β * Q = 0 := by
  have h := decoder_work_balance (β := β) (lnZ := lnZ) (S₁ := S₁) (S₂ := S₂) hfirst
  rw [eq_div_iff hβ.ne']
  constructor <;> intro heq <;> nlinarith

/-- A Gibbs entropy bound joined to the decoder's metered energy budget.
The partition term is retained; entropy is measured per prepared state,
not silently equated with a channel rate. -/
theorem funded_decoder_entropy_bound {n : Type*} [Fintype n] [DecidableEq n] [Nonempty n]
    {H ρ : Matrix n n ℂ} (hH : H.IsHermitian) (hρ : ρ.PosSemidef)
    (htr : (Matrix.trace ρ).re = 1) {β E₀ budget : ℝ}
    (hβ : 0 ≤ β) (henergy : (Matrix.trace (ρ * H)).re ≤ E₀ + budget) :
    Snuffy.QuantumLandauer.vnEnt hρ.1 ≤
      β * (E₀ + budget) + Real.log (Snuffy.Landauer.partition β hH.eigenvalues) := by
  have h := Snuffy.QuantumLandauer.vnEnt_le_energy hH β hρ htr
  have hm := mul_le_mul_of_nonneg_left henergy hβ
  linarith

/-- Local income covering the complete decoder demand supplies the existing
escrow theorem at every cycle, including the minimal-hold account. -/
theorem funded_decoder_cycles {E₀ : ℝ} {r w h : ℕ → ℝ}
    (hE : 0 ≤ E₀) (hcover : ∀ k, w k ≤ r k) :
    ∀ k, Snuffy.ThermoLedger.escrow E₀ r w h k =
        E₀ + ∑ j ∈ Finset.range k, (r j - w j) ∧
      0 ≤ Snuffy.ThermoLedger.escrow E₀ r w h k ∧
      w k ≤ Snuffy.ThermoLedger.escrow E₀ r w h k + r k := by
  apply Snuffy.ThermoLedger.funded_repair_certificate hE
  intro k
  exact add_nonneg hE (Finset.sum_nonneg fun j _ => sub_nonneg.mpr (hcover j))

end Snuffy.WorkBilling
