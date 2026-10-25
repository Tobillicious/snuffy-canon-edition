import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Basic.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

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

/-- A concrete boundary/reservoir exchange on the ordered basis
|00>, |01>, |10>, |11>. The off-diagonal coupling transfers one charge. -/
def exchangeHamiltonian : Matrix (Fin 4) (Fin 4) ℂ :=
  !![0, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 0]

def boundaryCharge : Matrix (Fin 4) (Fin 4) ℂ :=
  !![0, 0, 0, 0; 0, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1]

def reservoirCharge : Matrix (Fin 4) (Fin 4) ℂ :=
  !![0, 0, 0, 0; 0, 1, 0, 0; 0, 0, 0, 0; 0, 0, 0, 1]

def exchangeSwap : Matrix (Fin 4) (Fin 4) ℂ :=
  !![1, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 1]

theorem exchange_hamiltonian_hermitian : exchangeHamiltonian.IsHermitian := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [exchangeHamiltonian]

theorem exchange_conserves_total_charge :
    exchangeHamiltonian * (boundaryCharge + reservoirCharge) =
      (boundaryCharge + reservoirCharge) * exchangeHamiltonian := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [exchangeHamiltonian, boundaryCharge, reservoirCharge,
      Matrix.mul_apply, Fin.sum_univ_succ]

theorem exchange_pumps_boundary :
    boundaryCharge * exchangeHamiltonian ≠ exchangeHamiltonian * boundaryCharge := by
  intro heq
  have h := congrArg (fun M : Matrix (Fin 4) (Fin 4) ℂ => M 1 2) heq
  norm_num [exchangeHamiltonian, boundaryCharge, Matrix.mul_apply, Fin.sum_univ_succ] at h

theorem exchange_swap_unitary : star exchangeSwap * exchangeSwap = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [exchangeSwap, Matrix.mul_apply, Fin.sum_univ_succ]

theorem exchange_swap_charge :
    star exchangeSwap * boundaryCharge * exchangeSwap = reservoirCharge := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [exchangeSwap, boundaryCharge, reservoirCharge,
      Matrix.mul_apply, Fin.sum_univ_succ]

theorem exchange_swap_total :
    star exchangeSwap * (boundaryCharge + reservoirCharge) * exchangeSwap =
      boundaryCharge + reservoirCharge := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [exchangeSwap, boundaryCharge, reservoirCharge,
      Matrix.mul_apply, Fin.sum_univ_succ]

end Snuffy.HamiltonianDecomposition
