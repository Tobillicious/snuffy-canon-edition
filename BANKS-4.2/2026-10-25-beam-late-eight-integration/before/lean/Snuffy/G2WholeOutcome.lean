namespace Snuffy.G2WholeOutcome

structure OutcomeTuple where
  preStateHash : UInt64
  postStateHash : UInt64
  workExpenditure : Nat
  isAuthorized : Bool
  isClosed : Bool
  deriving Repr, DecidableEq

def G2_ValidOutcome (o : OutcomeTuple) : Prop :=
  o.isAuthorized = true → (o.isClosed = true ∧ o.workExpenditure > 0)

abbrev OutcomeSequence := List OutcomeTuple

def G2_SequenceValid (seq : OutcomeSequence) : Prop :=
  ∀ o ∈ seq, G2_ValidOutcome o

theorem g2_authorized_implies_closed (o : OutcomeTuple) (h : G2_ValidOutcome o)
    (h_auth : o.isAuthorized = true) : o.isClosed = true := by
  have := h h_auth
  exact this.1

theorem g2_authorized_implies_positive_work (o : OutcomeTuple) (h : G2_ValidOutcome o)
    (h_auth : o.isAuthorized = true) : o.workExpenditure > 0 := by
  have := h h_auth
  exact this.2

theorem g2_compose_valid (seq : OutcomeSequence) (o : OutcomeTuple)
    (h_seq : G2_SequenceValid seq)
    (h_o : G2_ValidOutcome o) :
    G2_SequenceValid (seq ++ [o]) := by
  intro x hx
  rw [List.mem_append, List.mem_singleton] at hx
  rcases hx with h_in | h_eq
  · exact h_seq x h_in
  · subst h_eq
    exact h_o

end Snuffy.G2WholeOutcome
