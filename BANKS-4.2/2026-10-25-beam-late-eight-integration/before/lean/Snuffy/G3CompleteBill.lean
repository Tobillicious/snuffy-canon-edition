namespace Snuffy.G3CompleteBill

structure WorkBill where
  timeSteps : Nat
  waveCount : Nat
  dimensionalFactor : Nat
  allocatedWork : Nat
  scalingConstant : Nat
  tiwaSuccess : Bool
  isBoundaryClosed : Bool
  decoderSuccess : Bool
  deriving Repr, DecidableEq

def G3_ValidWorkBill (bill : WorkBill) : Prop :=
  bill.tiwaSuccess = true →
  bill.allocatedWork <= bill.scalingConstant * (bill.waveCount ^ bill.dimensionalFactor)

abbrev WorkBillSequence := List WorkBill

def G3_SequenceValid (seq : WorkBillSequence) : Prop :=
  ∀ bill ∈ seq, G3_ValidWorkBill bill

theorem g3_success_implies_bound (bill : WorkBill) (h : G3_ValidWorkBill bill)
    (h_success : bill.tiwaSuccess = true) :
    bill.allocatedWork <= bill.scalingConstant * (bill.waveCount ^ bill.dimensionalFactor) := by
  exact h h_success

theorem g3_compose_valid (seq : WorkBillSequence) (bill : WorkBill)
    (h_seq : G3_SequenceValid seq)
    (h_bill : G3_ValidWorkBill bill) :
    G3_SequenceValid (seq ++ [bill]) := by
  intro x hx
  rw [List.mem_append, List.mem_singleton] at hx
  rcases hx with h_in | h_eq
  · exact h_seq x h_in
  · subst h_eq
    exact h_bill

theorem g3_wave_count_nonnegative (bill : WorkBill) :
    bill.waveCount >= 0 := by
  exact Nat.zero_le bill.waveCount

end Snuffy.G3CompleteBill
