/-
Snuffy — Canon Edition: formalization prelude for the reduced premise stack.

These declarations mirror the seven declared premises of the Canon Edition
header (SNUFFY-CANON-EDITION-2026-10-24, inserts/00). They are structure and
class mirrors: the premises are declared, not derived (Gödel/Tarski honesty
line), and no physical content is claimed as proven here. The one theorem this
file proves is the standard cost model's budget monotonicity with free
disposal — the P-mon of the greatestness proof, at its declared cost model.

Pure Lean 4 core; no imports; no Mathlib.
-/

namespace Snuffy

/- 1. BCRD P1–P4: the relational given. -/
class RelationalArena (Ω : Type) where
  related : Ω → Ω → Prop
  /- P1: one relational structure; no second substance or outside. -/
  one_structure : Prop
  /- P2: identity is constituted through relations within the structure. -/
  identity_by_relations : Prop
  /- P3: real differences of organisation; historically continuous processes. -/
  continuous_processes : Prop
  /- P4: local interactions; effects propagate at finite speed. -/
  finite_propagation : Prop

/- 2. The Church–Turing–Deutsch principle (declared). -/
class UniversalSimulator (Sys Sim : Type) where
  simulate : Sys → Sim → Prop
  /- Simulation to arbitrary precision with bounded overhead. -/
  arbitrary_precision_bounded_overhead : Prop

/- 3. The standard cost model: options are trajectories with energy costs;
     feasibility is budget-gated; unused energy is unspent (free disposal). -/
structure Costed (A : Type) where
  trajectory : A
  energy : Nat

def Affordable (budget : Nat) {A : Type} (o : Costed A) : Prop := o.energy ≤ budget

/- Free disposal: what is affordable at a budget stays affordable at any
   larger budget. -/
theorem free_disposal {A : Type} (o : Costed A) {b c : Nat}
    (h : b ≤ c) (ha : Affordable b o) : Affordable c o :=
  Nat.le_trans ha h

/- P-mon, proved at the declared cost model: residual resources weakly
   enlarge the feasible family. -/
theorem resource_monotonicity {A : Type} (b c : Nat) (h : b ≤ c) :
    ∀ o : Costed A, Affordable b o → Affordable c o :=
  fun _ ha => free_disposal _ h ha

/- 4. The shared action interface (from P1/P4): rival and lattice act through
     the same repertoire of local interactions. -/
class SharedActionInterface (Act Rival Lattice : Type) where
  actionOfRival : Rival → Act
  actionOfLattice : Lattice → Act
  /- Every rival action channel is available to the lattice. -/
  same_repertoire : Prop

/- 5. The reversible-administration commitment (Landauer floor, declared). -/
class ReversibleAdmin (Adm : Type) where
  cost : Adm → Nat
  erasedNats : Adm → Nat
  /- Bennett: dissipation is bounded by the Landauer floor of erasures
     actually performed. -/
  landauer_floor : ∀ a, erasedNats a ≤ cost a

/- 6. The income flux and the Master Solvency Condition (five rate components). -/
structure Rates where
  maint : Nat    -- boundary maintenance ω₀ R^(d_G−1)
  damage : Nat   -- Landauer-charged damage repair incl. controller export
  admin : Nat    -- reversible administration at the floor, plus emulation overhead
  advsub : Nat   -- adversarial sub-threshold absorption
  hold : Nat     -- the minimal-hold drain that quarantine requires

def Solvent (income : Nat) (r : Rates) : Prop :=
  income ≥ r.maint + r.damage + r.admin + r.advsub + r.hold

/- 7. Code, sensing, Π, and the twenty-one charged accounts with the ceiling. -/
structure Account where
  /- Conditional kernel weight in units of 10⁻¹². -/
  deltaPico : Nat

/- The ratified ceiling: Σδ ≤ 10⁻⁶ per declared horizon. -/
def CEILING : Nat := 10 ^ 6

def withinCeiling (accs : List Account) : Prop :=
  (accs.map Account.deltaPico).sum ≤ CEILING

end Snuffy
