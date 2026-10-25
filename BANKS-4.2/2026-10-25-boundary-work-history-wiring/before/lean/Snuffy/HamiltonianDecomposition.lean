namespace Snuffy.HamiltonianDecomposition

structure Hamiltonian where
  bulkTerm : Nat
  boundaryTerm : Nat
  interactionTerm : Nat

def totalHamiltonian (H : Hamiltonian) : Nat :=
  H.bulkTerm + H.boundaryTerm + H.interactionTerm

def confinementWell (boundaryPotential : Nat) : Nat :=
  boundaryPotential

theorem total_is_sum (H : Hamiltonian) :
    totalHamiltonian H = H.bulkTerm + H.boundaryTerm + H.interactionTerm := by
  rfl

theorem boundary_confinement_positive (V : Nat) (h : V > 0) :
    confinementWell V > 0 := h

end Snuffy.HamiltonianDecomposition