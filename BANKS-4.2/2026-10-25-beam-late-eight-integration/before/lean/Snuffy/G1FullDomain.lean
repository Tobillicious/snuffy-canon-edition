namespace Snuffy.G1FullDomain

inductive SourceDomain where
  | InternalEngine
  | ExternalUser
  | SubstrateTelemetry
  deriving Repr, DecidableEq

inductive FaultType where
  | None
  | EnvironmentalNoise
  | UncertifiedInjection
  | BoundaryViolation
  deriving Repr, DecidableEq

structure EventNode where
  eventId : Nat
  timestamp : Nat
  source : SourceDomain
  fault : FaultType
  isClosed : Bool
  deriving Repr, DecidableEq

abbrev EventTrace := List EventNode

def G1_Compliant (trace : EventTrace) : Prop :=
  ∀ e ∈ trace, e.fault ≠ FaultType.None → e.isClosed = false

def G1_FaultFree (e : EventNode) : Prop :=
  e.fault = FaultType.None

def G1_AllSourcesValid (trace : EventTrace) : Prop :=
  ∀ e ∈ trace, e.source = SourceDomain.InternalEngine ∨
               e.source = SourceDomain.ExternalUser ∨
               e.source = SourceDomain.SubstrateTelemetry

theorem g1_source_exhaustive (trace : EventTrace) (h : G1_AllSourcesValid trace) :
    ∀ e ∈ trace, e.source = SourceDomain.InternalEngine ∨
                 e.source = SourceDomain.ExternalUser ∨
                 e.source = SourceDomain.SubstrateTelemetry := h

theorem g1_fault_taxonomy_exhaustive (f : FaultType) :
    f = FaultType.None ∨ f = FaultType.EnvironmentalNoise ∨
    f = FaultType.UncertifiedInjection ∨ f = FaultType.BoundaryViolation := by
  cases f <;> simp

theorem g1_append_preserves (trace : EventTrace) (e : EventNode)
    (h_trace : G1_Compliant trace)
    (h_e : e.fault ≠ FaultType.None → e.isClosed = false) :
    G1_Compliant (trace ++ [e]) := by
  intro x hx
  rw [List.mem_append, List.mem_singleton] at hx
  rcases hx with h_in | h_eq
  · exact h_trace x h_in
  · subst h_eq
    exact h_e

end Snuffy.G1FullDomain
