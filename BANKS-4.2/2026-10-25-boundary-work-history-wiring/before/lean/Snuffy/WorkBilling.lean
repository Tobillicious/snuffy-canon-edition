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

end Snuffy.WorkBilling