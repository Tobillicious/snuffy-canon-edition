import Snuffy.Bridge

namespace Snuffy.DecoderRetraction

universe u v

structure DecoderPair (A : Type u) (B : Type v) where
  encode : A → B
  decode : B → A
  retraction : ∀ a, decode (encode a) = a

theorem decode_encode {A : Type u} {B : Type v} (D : DecoderPair A B) (a : A) :
    D.decode (D.encode a) = a :=
  D.retraction a

/-- The existing finite nearest-codeword construction populates the retraction
interface and corrects every received state within the unique-decoding radius.
The retraction and radius guarantee are derived from `Bridge`; neither is
assumed as a field of an unspecified decoder. The physical source still has
to establish that its perturbations meet this same radius bound. -/
theorem finite_code_recovery {X : Type u} [MetricSpace X]
    (Code : Set X) (hfin : Code.Finite) (hne : Code.Nonempty)
    {dmin radius : ℝ}
    (hsep : ∀ c ∈ Code, ∀ c' ∈ Code, c ≠ c' → dmin ≤ dist c c')
    (hrad : 2 * radius < dmin) :
    ∃ D : DecoderPair Code X,
      (∀ c, D.encode c = (c : X)) ∧
      ∀ (c : Code) (y : X), dist y (c : X) ≤ radius → D.decode y = c := by
  obtain ⟨dec, hdec, hnear⟩ := Snuffy.Bridge.exists_nearest_decoder Code hfin hne
  let D : DecoderPair Code X := {
    encode := fun c => c.val
    decode := fun y => ⟨dec y, hdec y⟩
    retraction := by
      intro c
      apply Subtype.ext
      change dec (c : X) = (c : X)
      have hdist : dist (c : X) (dec (c : X)) ≤ 0 := by
        simpa only [dist_self] using hnear (c : X) (c : X) c.property
      exact (dist_eq_zero.mp (le_antisymm hdist dist_nonneg)).symm }
  refine ⟨D, fun _ => rfl, ?_⟩
  intro c y hy
  apply Subtype.ext
  change dec y = (c : X)
  exact Snuffy.Bridge.nearest_decodes hsep hrad hdec hnear c.property hy

/-- A continuation witness remains nonzero when its certified error is
strictly smaller than the record's distance from zero. The funded holding
construction supplies continuation; a work ceiling alone is not used as
a substitute for that witness. -/
theorem nonvanishing_of_continuation {X : Type u} [MetricSpace X] [Zero X]
    {Part : Type v} (rec : Part → X) (ε : ℝ) (state : Part → X) (x : Part)
    (hcontinues : Snuffy.Bridge.Continues rec ε state x)
    (hgap : ε < dist (rec x) 0) : state x ≠ 0 := by
  intro hzero
  change dist (state x) (rec x) ≤ ε at hcontinues
  rw [hzero, dist_comm] at hcontinues
  exact (not_le_of_gt hgap) hcontinues

/-- The finite-code recovery construction supplies a non-bottom fixed point
for its evaluation/transducer `encode ∘ decode` whenever the maintained code
contains a non-bottom record. This is a derived witness for the proposed
self-grounding equation; it introduces no new axiom and does not infer
existence from a work ceiling or from homology alone. -/
theorem finite_code_self_grounding {X : Type u} [MetricSpace X] [Bot X]
    (Code : Set X) (hfin : Code.Finite) (hne : Code.Nonempty)
    {dmin radius : ℝ}
    (hsep : ∀ c ∈ Code, ∀ c' ∈ Code, c ≠ c' → dmin ≤ dist c c')
    (hrad : 2 * radius < dmin) (record : Code) (hnonbot : (record : X) ≠ ⊥) :
    ∃ D : DecoderPair Code X,
      (∀ c, D.encode c = (c : X)) ∧
      (∀ (c : Code) (y : X), dist y (c : X) ≤ radius → D.decode y = c) ∧
      ∃ e : X, D.encode (D.decode e) = e ∧ D.encode (D.decode e) ≠ ⊥ := by
  obtain ⟨D, hencode, hcorrect⟩ := finite_code_recovery Code hfin hne hsep hrad
  have hfixed : D.encode (D.decode (record : X)) = (record : X) := by
    rw [← hencode record, D.retraction record]
  refine ⟨D, hencode, hcorrect, (record : X), hfixed, ?_⟩
  rw [hfixed]
  exact hnonbot

end Snuffy.DecoderRetraction
