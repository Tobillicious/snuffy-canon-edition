/-
Axiom audit for the v4.1 summit modules. Prints the axioms each headline
result depends on.
-/
import Snuffy.CanonVonNeumann
import Snuffy.RecoveryWork
import Snuffy.E9SelfHealing
import Snuffy.H5Closure
import Snuffy.Greatestness
import Snuffy.ThermoLedger
import Snuffy.Composition
import Snuffy.PremiseFloor
import Snuffy.ReciprocityCeiling
import Snuffy.CyclicProjections
import Snuffy.GaussianTail
import Snuffy.DeductionBoundary
import Snuffy.ReflectionCertificate
import Snuffy.Trotter
import Snuffy.Irreplaceability
import Snuffy.DataProcessing

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
#print axioms Snuffy.ThermoLedger.stroke_identity
#print axioms Snuffy.ThermoLedger.cycle_work_floor
#print axioms Snuffy.ThermoLedger.funded_repair_certificate
#print axioms Snuffy.ThermoLedger.quarantine_zero_debt
#print axioms Snuffy.ThermoLedger.tower_bound
#print axioms Snuffy.ThermoLedger.canon_invariant
#print axioms Snuffy.ThermoLedger.tracking_envelope
#print axioms Snuffy.ThermoLedger.tracking_within_resolution
#print axioms Snuffy.Composition.reactive_lockstep
#print axioms Snuffy.Composition.reactive_lockstep₂
#print axioms Snuffy.Composition.invariant_transfer
#print axioms Snuffy.Composition.theorem8_composition
#print axioms Snuffy.PremiseFloor.income_or_irrelevance
#print axioms Snuffy.PremiseFloor.forced_breach
#print axioms Snuffy.PremiseFloor.breach_strictly_below
#print axioms Snuffy.PremiseFloor.reversible_administration_forced
#print axioms Snuffy.ReciprocityCeiling.reciprocity_dominance
#print axioms Snuffy.ReciprocityCeiling.omitting_rival_strictly_below
#print axioms Snuffy.ReciprocityCeiling.ceiling_achievable
#print axioms Snuffy.Cyclic.energy
#print axioms Snuffy.Cyclic.mem_of_norm_adj_eq
#print axioms Snuffy.Cyclic.tendsto_cyc_iter
#print axioms Snuffy.Cyclic.presentation_detector
#print axioms Snuffy.GaussianTail.gaussian_lower_tail
#print axioms Snuffy.GaussianTail.carrier_tail
#print axioms Snuffy.GaussianTail.necessary_radius_of_decoder
#print axioms Snuffy.GaussianTail.x3_work_from_decoder
#print axioms Snuffy.DeductionBoundary.rank_criterion
#print axioms Snuffy.DeductionBoundary.boundary_mem_image
#print axioms Snuffy.DeductionBoundary.anchor_untouched
#print axioms Snuffy.Reflection.residual_certificate
#print axioms Snuffy.Reflection.apriori_error
#print axioms Snuffy.Reflection.stopping_count
#print axioms Snuffy.Reflection.zero_constant_fixed
#print axioms Snuffy.Trotter.norm_exp_le
#print axioms Snuffy.Trotter.norm_exp_sub_one_sub_le
#print axioms Snuffy.Trotter.norm_exp_mul_exp_sub
#print axioms Snuffy.Trotter.norm_exp_sum_sub_prod
#print axioms Snuffy.Trotter.trotter_bound
#print axioms Snuffy.Trotter.trotter_tendsto
#print axioms Snuffy.Trotter.lloyd_simulation
#print axioms Snuffy.Irreplaceability.destroy_loses_exactly
#print axioms Snuffy.Irreplaceability.preserve_dominates
#print axioms Snuffy.Irreplaceability.optimal_keeps_most_irreplaceable
#print axioms Snuffy.Information.fst_process
#print axioms Snuffy.Information.snd_process
#print axioms Snuffy.Information.data_processing
#print axioms Snuffy.Information.data_processing_map
