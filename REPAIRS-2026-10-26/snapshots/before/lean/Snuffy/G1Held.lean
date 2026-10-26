/-
Snuffy — Canon Edition 4.2 working: the held source and its full certificate
(G1). The five components of `Bridge.universal_protection_held`'s `hcert` are
derived here, not supplied.

The held source keeps, for every particular, its record frame. One step: the
world — environment and any agent, a pure optimiser included — perturbs the
frame; the nearest-codeword decoder returns a codeword; funded repair prepares
that codeword. The good event is the complement of the named charged
accounts.

  * goodEvent, good_cover — the good event and its exact cover by the named
    accounts (`hG`).
  * held_source_protection — every particular continues at every step through
    the horizon on the good event, and the probability that any particular
    fails is at most `Σ δ`, with no independence. The five `hcert` components
    are proved: refinement and observation agreement by construction, initial
    continuation from the records, the decoding-radius bound from the per-step
    drift bound and the continuation radius, repair precision from exact
    repair.
  * held_source_qsl — the per-step drift bound derived from the quantum speed
    limit (`Bridge.qsl_growth`): an arbitrary perturbing agent whose coupling
    is bounded by `W` off the named accounts moves a stationary record frame by
    at most `(W/ħ)Δ` per step. The remaining physical inputs are that coupling
    bound off the named events and the account probabilities.

Zero `sorry`. Mathlib rev 56a005855ea1.
-/

import Snuffy.Bridge

open MeasureTheory

namespace Snuffy.G1Held

open Snuffy.Bridge

variable {X Part Ω ι C Ev O : Type*} [MetricSpace X] [MeasurableSpace Ω]

/-- The good event: no named charged account fires. -/
def goodEvent (accounts : Finset ι) (Ev' : ι → Set Ω) : Set Ω :=
  {ω | ∀ i ∈ accounts, ω ∉ Ev' i}

omit [MeasurableSpace Ω] in
theorem good_cover (accounts : Finset ι) (Ev' : ι → Set Ω) :
    (goodEvent accounts Ev')ᶜ ⊆ ⋃ i ∈ accounts, Ev' i := by
  intro ω hω
  simp only [goodEvent, Set.mem_compl_iff, Set.mem_ofPred_eq, not_forall, not_not] at hω
  obtain ⟨i, hi, hωi⟩ := hω
  exact Set.mem_biUnion hi hωi

/-- The held step: the world's perturbation, nearest-codeword decoding and
exact repair of the decoded codeword. -/
def heldStep (dec : X → X) (pre : Ω → (Part → X) → C → Ev → Part → X)
    (ω : Ω) (a : Part → X) (c : C) (e : Ev) : Part → X :=
  fun x => dec (pre ω a c e x)

/-- **The held source and its full certificate.** -/
theorem held_source_protection (μ : Measure Ω) (accounts : Finset ι) (Ev' : ι → Set Ω)
    (δ : ι → ENNReal) (hδ : ∀ i ∈ accounts, μ (Ev' i) ≤ δ i)
    {rec : Part → X} {ε ρ t dmin : ℝ} {Code : Set X} (hrec : ∀ x, rec x ∈ Code)
    (hsep : ∀ c ∈ Code, ∀ c' ∈ Code, c ≠ c' → dmin ≤ dist c c') (ht : 2 * t < dmin)
    {dec : X → X} (hdecC : ∀ y, dec y ∈ Code)
    (hnear : ∀ y, ∀ c ∈ Code, dist y (dec y) ≤ dist y c) (hε : 0 ≤ ε)
    (scope : Set Part)
    (hlaw : ∀ (F : Set (Set Part)) (o : Set Part),
      Snuffy.Law.ProjMax scope F o → ¬ Snuffy.Law.NeedlessLoss₁ F o)
    (pre : Ω → (Part → X) → C → Ev → Part → X)
    (hdrift : ∀ ω ∈ goodEvent accounts Ev', ∀ a c e x,
      dist (pre ω a c e x) (rec x) ≤ dist (a x) (rec x) + ρ)
    (hbudget : ε + ρ ≤ t)
    (obs : (Part → X) → O) (ctrl : Ω → List O → C) (env : Ω → List O → C → Ev)
    (horizon : ℕ) :
    (∀ ω ∈ goodEvent accounts Ev', ∀ k ≤ horizon, ∀ x,
      Continues rec ε
        (Snuffy.Composition.run (heldStep dec pre ω) obs (ctrl ω) (env ω) rec k).1 x) ∧
    μ {ω | ∃ k ≤ horizon, ¬ ∀ x,
      Continues rec ε
        (Snuffy.Composition.run (heldStep dec pre ω) obs (ctrl ω) (env ω) rec k).1 x}
      ≤ ∑ i ∈ accounts, δ i := by
  have h := universal_protection_held μ accounts Ev' δ (goodEvent accounts Ev')
    (good_cover accounts Ev') hδ (fun s : Part → X => s) (heldStep dec pre)
    (heldStep dec pre) obs obs ctrl env (fun _ => rec) hrec hsep ht hdecC hnear
    (εf := 0) hε scope hlaw pre
    (fun ω hω => ⟨fun _ _ _ => rfl, fun _ => rfl,
      fun x => by simp [Continues, hε],
      fun a c e x _ hc => by
        have := hdrift ω hω a c e x
        unfold Continues at hc
        linarith,
      fun a c e x _ => by simp [heldStep]⟩)
    horizon
  exact h

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]

/-- **The per-step drift from the speed limit.** If, off the named accounts,
each step of each particular's frame is a Schrödinger evolution of duration
`Δ` under `H₀ + V`, with the record stationary under `H₀` and the perturbing
coupling bounded by `W` — whatever agent applies `V` — then the frame moves
toward or away from its record by at most `(W/ħ)Δ`, and every particular is
held. -/
theorem held_source_qsl (μ : Measure Ω) (accounts : Finset ι) (Ev' : ι → Set Ω)
    (δ : ι → ENNReal) (hδ : ∀ i ∈ accounts, μ (Ev' i) ≤ δ i)
    {rec : Part → E} {ε t dmin : ℝ} {Code : Set E} (hrec : ∀ x, rec x ∈ Code)
    (hsep : ∀ c ∈ Code, ∀ c' ∈ Code, c ≠ c' → dmin ≤ dist c c') (ht : 2 * t < dmin)
    {dec : E → E} (hdecC : ∀ y, dec y ∈ Code)
    (hnear : ∀ y, ∀ c ∈ Code, dist y (dec y) ≤ dist y c) (hε : 0 ≤ ε)
    (scope : Set Part)
    (hlaw : ∀ (F : Set (Set Part)) (o : Set Part),
      Snuffy.Law.ProjMax scope F o → ¬ Snuffy.Law.NeedlessLoss₁ F o)
    (pre : Ω → (Part → E) → C → Ev → Part → E)
    {ħ W Δ : ℝ} (hħ : 0 < ħ) (hΔ : 0 ≤ Δ)
    (htraj : ∀ ω ∈ goodEvent accounts Ev', ∀ a c e x,
      ∃ (H₀ V : ℝ → E →L[ℂ] E) (ψ : ℝ → E) (s₁ : ℝ),
        (∀ s, IsSelfAdjoint (H₀ s)) ∧ (∀ s, IsSelfAdjoint (H₀ s + V s)) ∧
        (∀ s, ‖V s‖ ≤ W) ∧ (∀ s, H₀ s (rec x) = 0) ∧
        Snuffy.SpeedLimit.Solves ħ (fun s => H₀ s + V s) ψ ∧ ‖ψ 0‖ = 1 ∧
        ψ s₁ = a x ∧ ψ (s₁ + Δ) = pre ω a c e x)
    (hbudget : ε + W / ħ * Δ ≤ t)
    (obs : (Part → E) → O) (ctrl : Ω → List O → C) (env : Ω → List O → C → Ev)
    (horizon : ℕ) :
    (∀ ω ∈ goodEvent accounts Ev', ∀ k ≤ horizon, ∀ x,
      Continues rec ε
        (Snuffy.Composition.run (heldStep dec pre ω) obs (ctrl ω) (env ω) rec k).1 x) ∧
    μ {ω | ∃ k ≤ horizon, ¬ ∀ x,
      Continues rec ε
        (Snuffy.Composition.run (heldStep dec pre ω) obs (ctrl ω) (env ω) rec k).1 x}
      ≤ ∑ i ∈ accounts, δ i := by
  refine held_source_protection μ accounts Ev' δ hδ hrec hsep ht hdecC hnear hε scope hlaw
    pre (ρ := W / ħ * Δ) (fun ω hω a c e x => ?_) hbudget obs ctrl env horizon
  obtain ⟨H₀, V, ψ, s₁, hH₀, hHV, hW, hzero, hψ, hψ1, hstart, hend⟩ := htraj ω hω a c e x
  have hg := qsl_growth hħ hH₀ hHV hW hzero hψ hψ1 (s₁ := s₁) (s₂ := s₁ + Δ) (by linarith)
  rw [dist_eq_norm, dist_eq_norm, ← hstart, ← hend]
  have : s₁ + Δ - s₁ = Δ := by ring
  rw [this] at hg
  exact hg

end Snuffy.G1Held
