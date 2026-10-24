/-
Axiom audit for the v4.1 summit modules. Prints the axioms each headline
result depends on.
-/
import Snuffy.CanonVonNeumann
import Snuffy.RecoveryWork
import Snuffy.E9SelfHealing
import Snuffy.H5Closure
import Snuffy.Greatestness

#print axioms Snuffy.CanonVonNeumann.canon_von_neumann_convergence
#print axioms Snuffy.CanonVonNeumann.canon_opial_convergence
#print axioms Snuffy.CanonVonNeumann.opial_route_closes
#print axioms Snuffy.RecoveryWork.frontier_work_bound
#print axioms Snuffy.RecoveryWork.Wmin_lower_bound
#print axioms Snuffy.RecoveryWork.necessary_radius
#print axioms Snuffy.RecoveryWork.carrier_radius
#print axioms Snuffy.RecoveryWork.x3_delayed_recovery_work
#print axioms Snuffy.RecoveryWork.delayed_work_diverges
#print axioms Snuffy.E9.robust_between_honest
#print axioms Snuffy.E9.exists_robust
#print axioms Snuffy.E9.syndrome_detects
#print axioms Snuffy.E9.code_headroom
#print axioms Snuffy.E9.e9_timely_self_healing
#print axioms Snuffy.H5.step_inv
#print axioms Snuffy.H5.authority_attenuation
#print axioms Snuffy.H5.reserve_before_activation
#print axioms Snuffy.H5.no_unfunded_work
#print axioms Snuffy.H5.no_harmful_effect
#print axioms Snuffy.H5.consistency_detector
#print axioms Snuffy.Greatestness.lexLt_trans
#print axioms Snuffy.Greatestness.aligned_iff_no_needless_loss
#print axioms Snuffy.Greatestness.greatest_of_union_closed
#print axioms Snuffy.Greatestness.strict_except_mirrors
#print axioms Snuffy.Greatestness.aligned_unique
