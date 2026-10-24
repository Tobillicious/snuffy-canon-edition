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
import Snuffy.MeetHilbert
import Snuffy.FiniteInformation
import Snuffy.AreaBridge
import Snuffy.UniversalProtection
import Snuffy.Workload
import Snuffy.Fano
import Snuffy.GaussianKL
import Snuffy.GoldenFormula
import Snuffy.GaussianChannel
import Snuffy.KLAdditivity
import Snuffy.GaussianChannelGen
import Snuffy.GaussianVector
import Snuffy.Whitening
import Snuffy.Rotation
import Snuffy.LogDet
import Snuffy.Law
import Snuffy.SpeedLimit
import Snuffy.Landauer
import Snuffy.QuantumLandauer
import Snuffy.Threshold
import Snuffy.UnionClosure
import Snuffy.Bridge
import Snuffy.Instruments
import Snuffy.StrokeBookkeeping
import Snuffy.Bennett
import Snuffy.Concatenated
import Snuffy.ReasonsCompiled
import Snuffy.TwoLevel
import Snuffy.GateSupport
import Snuffy.RiskBounds
import Snuffy.QueueDeadline
import Snuffy.BandwidthReflection
import Snuffy.AnalyticBridge
import Snuffy.RankAndCoalition
import Snuffy.MetricShadow
import Snuffy.SemanticMap
import Snuffy.BridgeD1
import Snuffy.BridgeE9
import Snuffy.BridgeH6
import Snuffy.BridgeH7
import Snuffy.BridgeH8
import Snuffy.SensorTail
import Snuffy.ConsensusRate
import Snuffy.RGFixedPoint
import Snuffy.FinalClosure

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
#print axioms Snuffy.MeetHilbert.hilbert_anchor_preserved
#print axioms Snuffy.MeetHilbert.hilbert_contradiction_collapse
#print axioms Snuffy.MeetHilbert.contradiction_detected
#print axioms Snuffy.MeetHilbert.deduction_never_rolls_back
#print axioms Snuffy.FiniteInformation.log_sum
#print axioms Snuffy.FiniteInformation.data_processing_fin
#print axioms Snuffy.FiniteInformation.flag_identity
#print axioms Snuffy.FiniteInformation.decoder_bound
#print axioms Snuffy.FiniteInformation.necessary_radius_from_decoder
#print axioms Snuffy.AreaBridge.logdet_le_trace
#print axioms Snuffy.AreaBridge.channel_cap
#print axioms Snuffy.AreaBridge.required_traffic
#print axioms Snuffy.AreaBridge.area_power
#print axioms Snuffy.UniversalProtection.coverage_invariant
#print axioms Snuffy.UniversalProtection.universal_protection
#print axioms Snuffy.Workload.fifo_certificate
#print axioms Snuffy.Workload.fifo_deadlines
#print axioms Snuffy.Workload.fifo_tight
#print axioms Snuffy.Workload.serial_certificate
#print axioms Snuffy.Workload.range_variance_bound
#print axioms Snuffy.Fano.max_entropy
#print axioms Snuffy.Fano.fano_single
#print axioms Snuffy.Fano.fano
#print axioms Snuffy.Fano.mi_eq_ent_sub_condEnt
#print axioms Snuffy.Fano.required_information
#print axioms Snuffy.GaussianKL.rnDeriv_gaussian_gaussian
#print axioms Snuffy.GaussianKL.llr_gaussian_gaussian
#print axioms Snuffy.GaussianKL.integral_sq_sub_gaussian
#print axioms Snuffy.GaussianKL.klDiv_gaussian_gaussian
#print axioms Snuffy.Information.klDiv_map_swap
#print axioms Snuffy.Information.golden_formula
#print axioms Snuffy.Information.mutualInfo_le_klDiv
#print axioms Snuffy.GaussianChannel.integral_quadratic_gaussian
#print axioms Snuffy.GaussianChannel.llr_chan
#print axioms Snuffy.GaussianChannel.klDiv_chan
#print axioms Snuffy.GaussianChannel.gaussian_channel_bound
#print axioms Snuffy.KLAdditivity.prod_eq_compProd
#print axioms Snuffy.KLAdditivity.klDiv_map_equiv
#print axioms Snuffy.KLAdditivity.klDiv_prod_kernel
#print axioms Snuffy.GaussianChannelGen.llr_chanW
#print axioms Snuffy.GaussianChannelGen.klDiv_chanW
#print axioms Snuffy.GaussianVector.klDiv_compProd_map_equiv
#print axioms Snuffy.GaussianVector.klDiv_vecChan
#print axioms Snuffy.GaussianVector.vector_channel_bound
#print axioms Snuffy.GaussianVector.vector_channel_trace_bound
#print axioms Snuffy.Whitening.mutualInfo_kernel_map_equiv
#print axioms Snuffy.Whitening.vecChan_apply
#print axioms Snuffy.Whitening.multivariateGaussian_one_eq_pi
#print axioms Snuffy.Whitening.whiten
#print axioms Snuffy.Whitening.correlated_channel_bound
#print axioms Snuffy.Rotation.multivariateGaussian_one_map_isometry
#print axioms Snuffy.Rotation.rotated_channel_bound
#print axioms Snuffy.LogDet.var_lincomb
#print axioms Snuffy.LogDet.var_rot_eq_eigenvalue
#print axioms Snuffy.LogDet.det_one_add
#print axioms Snuffy.LogDet.logdet_channel_bound
#print axioms Snuffy.Law.exists_aligned
#print axioms Snuffy.Law.lexLt_first_le
#print axioms Snuffy.Law.life_guard
#print axioms Snuffy.Law.scope_guarantee_iff
#print axioms Snuffy.Law.same_priority_admits_needless_loss
#print axioms Snuffy.Law.faithful_hold_dominates
#print axioms Snuffy.Law.faithful_hold_strict
#print axioms Snuffy.SpeedLimit.norm_le_of_inner_deriv_le
#print axioms Snuffy.SpeedLimit.angle_le_chord
#print axioms Snuffy.SpeedLimit.angle_le_speed_mul
#print axioms Snuffy.SpeedLimit.norm_conserved
#print axioms Snuffy.SpeedLimit.branchA_divergence
#print axioms Snuffy.SpeedLimit.branchA_rate
#print axioms Snuffy.SpeedLimit.mandelstam_tamm
#print axioms Snuffy.SpeedLimit.orthogonalization_time
#print axioms Snuffy.Landauer.kl_nonneg
#print axioms Snuffy.Landauer.mutualInfo_eq
#print axioms Snuffy.Landauer.ent_le_ent_marg
#print axioms Snuffy.Landauer.ent_gibbs
#print axioms Snuffy.Landauer.ent_le_energy
#print axioms Snuffy.Landauer.ent_evolve
#print axioms Snuffy.Landauer.reeb_wolf_identity
#print axioms Snuffy.Landauer.landauer
#print axioms Snuffy.Landauer.landauer_erasure
#print axioms Snuffy.Landauer.guard_one
#print axioms Snuffy.Landauer.cycle_work_floor_derived
#print axioms Snuffy.QuantumLandauer.vnEnt_unitary_conj
#print axioms Snuffy.QuantumLandauer.vnEnt_diagonal
#print axioms Snuffy.QuantumLandauer.vnEnt_le_diag
#print axioms Snuffy.QuantumLandauer.vnEnt_le_energy
#print axioms Snuffy.QuantumLandauer.vnEnt_gibbsState
#print axioms Snuffy.QuantumLandauer.ptrA_conj
#print axioms Snuffy.QuantumLandauer.ptrB_conj
#print axioms Snuffy.QuantumLandauer.vnEnt_init
#print axioms Snuffy.QuantumLandauer.quantum_landauer
#print axioms Snuffy.QuantumLandauer.quantum_guard_one
#print axioms Snuffy.QuantumLandauer.quantum_cycle_work_floor
#print axioms Snuffy.Threshold.many_faults
#print axioms Snuffy.Threshold.fail_le_witness
#print axioms Snuffy.Threshold.fail_le_geometric
#print axioms Snuffy.Threshold.repetition_threshold
#print axioms Snuffy.Threshold.repetition_ceiling
#print axioms Snuffy.Threshold.poly_geom_le
#print axioms Snuffy.Threshold.family_ceiling
#print axioms Snuffy.UnionClosure.aligned_never_below
#print axioms Snuffy.UnionClosure.dominates_of_affordable
#print axioms Snuffy.UnionClosure.strict_of_affordable
#print axioms Snuffy.UnionClosure.exists_union_bound
#print axioms Snuffy.UnionClosure.dominates_within_slack
#print axioms Snuffy.UnionClosure.union_closed_of_affordable
#print axioms Snuffy.UnionClosure.greatest_of_affordable
#print axioms Snuffy.UnionClosure.insolvent_not_greatest
#print axioms Snuffy.UnionClosure.aligned_eq_of_greatest
#print axioms Snuffy.UnionClosure.greatest_of_solvent
#print axioms Snuffy.UnionClosure.greatest_or_irrelevant
#print axioms Snuffy.UnionClosure.strict_of_solvent
#print axioms Snuffy.Bridge.coverage_from_law
#print axioms Snuffy.Bridge.nearest_decodes
#print axioms Snuffy.Bridge.exists_nearest_decoder
#print axioms Snuffy.Bridge.holding_preserves
#print axioms Snuffy.Bridge.qsl_growth
#print axioms Snuffy.Bridge.qsl_within_radius
#print axioms Snuffy.Bridge.headroom_within_radius
#print axioms Snuffy.Bridge.universal_protection_held
#print axioms Snuffy.Bridge.holding_cycle_physical
#print axioms Snuffy.Instruments.lindblad_reset_flow
#print axioms Snuffy.Instruments.lindblad_step
#print axioms Snuffy.Instruments.reset_contracts
#print axioms Snuffy.Instruments.tracking_recursion_derived
#print axioms Snuffy.Instruments.tracking_envelope_derived
#print axioms Snuffy.Instruments.branchC_complete
#print axioms Snuffy.Instruments.card_box
#print axioms Snuffy.Instruments.card_boundary
#print axioms Snuffy.Instruments.boundary_power
#print axioms Snuffy.StrokeBookkeeping.controlled_unitary
#print axioms Snuffy.StrokeBookkeeping.ptrB_controlled
#print axioms Snuffy.StrokeBookkeeping.stroke_entropy_change
#print axioms Snuffy.StrokeBookkeeping.stroke_identity_derived
#print axioms Snuffy.Bennett.bennett_step
#print axioms Snuffy.Bennett.bennett_compute_uncompute
#print axioms Snuffy.Bennett.ent_equiv
#print axioms Snuffy.Bennett.negMulLog_add_le
#print axioms Snuffy.Bennett.negMulLog_add_lt
#print axioms Snuffy.Bennett.ent_push_le
#print axioms Snuffy.Bennett.ent_push_lt
#print axioms Snuffy.Bennett.heat_reversible
#print axioms Snuffy.Bennett.heat_irreversible
#print axioms Snuffy.Bennett.premise5_from_bennett
#print axioms Snuffy.Concatenated.distance3_corrects_one
#print axioms Snuffy.Concatenated.fails_witness
#print axioms Snuffy.Concatenated.card_witness
#print axioms Snuffy.Concatenated.card_witnesses
#print axioms Snuffy.Concatenated.concatenated_threshold
#print axioms Snuffy.Concatenated.concatenated_ceiling
#print axioms Snuffy.ReasonsCompiled.reciprocity_expectation
#print axioms Snuffy.ReasonsCompiled.reciprocity_canonical_floor
#print axioms Snuffy.ReasonsCompiled.reciprocity_strict
#print axioms Snuffy.ReasonsCompiled.reciprocity_from_solvency
#print axioms Snuffy.ReasonsCompiled.controller_pays_floor
#print axioms Snuffy.ReasonsCompiled.controller_floor_diverges
#print axioms Snuffy.TwoLevel.mul_of_idOutside
#print axioms Snuffy.TwoLevel.givens_unitary
#print axioms Snuffy.TwoLevel.givens_idOutside
#print axioms Snuffy.TwoLevel.elim_kills
#print axioms Snuffy.TwoLevel.col_zero_above
#print axioms Snuffy.TwoLevel.clear_below
#print axioms Snuffy.TwoLevel.phase_unitary
#print axioms Snuffy.TwoLevel.next_column
#print axioms Snuffy.TwoLevel.star_twoLevel
#print axioms Snuffy.TwoLevel.two_level_decomposition
-- The thirteen bridges (23 October 2026 banks)
#print axioms GeminiThirteenAnalysis.integrating_factor_monotone
#print axioms GeminiThirteenAnalysis.linear_barrier_preserves_safety
#print axioms GeminiThirteenAnalysis.exponential_transient_bound
#print axioms GeminiThirteenAnalysis.integrated_exponential_transient
#print axioms GeminiThirteenAnalysis.integrated_transient_cost_bound
#print axioms GeminiThirteenAnalysis.continuation_hazard_threshold
#print axioms GeminiThirteenAnalysis.heterogeneous_quadratic_cost_identity
#print axioms GeminiThirteenAnalysis.heterogeneous_uniform_is_not_minimum
#print axioms GeminiThirteenAnalysis.eventually_better_continuation
#print axioms GeminiBridgeH6.charged_transition_bound
#print axioms GeminiBridgeH6.no_infinite_paid_run
#print axioms GeminiBridgeH6.budget_exhaustion_need_not_be_fixed
#print axioms GeminiBridgeH6.current_residual_bound
#print axioms GeminiBridgeH6.next_residual_bound
#print axioms GeminiThirteenBandwidth.normalized_susceptibility
#print axioms GeminiThirteenBandwidth.exact_bandwidth_sensitivity
#print axioms GeminiThirteenBandwidth.finite_positive_sensory_access_remains
#print axioms GeminiThirteenBandwidth.bandwidth_bias_threshold
#print axioms GeminiThirteenMetric.embedding_distance_stability
#print axioms GeminiThirteenMetric.protected_close_edge_margin
#print axioms GeminiThirteenMetric.protected_separated_edge_margin
#print axioms GeminiBridgeH7.rate_bounds
#print axioms GeminiBridgeH7.denominator_positive
#print axioms GeminiBridgeH7.equilibrium_is_fixed
#print axioms GeminiBridgeH7.fixed_point_unique
#print axioms GeminiBridgeH7.exact_transient
#print axioms GeminiBridgeH7.equilibrium_private_evidence_sensitivity
#print axioms GeminiBridgeH7.stubborn_anchor_limit
#print axioms GeminiBridgeH7.private_evidence_sensitivity_vanishes
#print axioms GeminiBridgeH7.exact_bias_threshold
#print axioms GeminiThirteenSemantics.identity_is_bijective
#print axioms GeminiThirteenSemantics.flipped_is_bijective
#print axioms GeminiThirteenSemantics.two_distinct_lossless_maps
#print axioms GeminiThirteenSemantics.calibrated_reference_fixes_binary_mapping
#print axioms GeminiThirteenQueue.exponential_service_tail
#print axioms GeminiThirteenQueue.exponential_service_normalized
#print axioms GeminiThirteenQueue.positive_deadline_miss_probability
#print axioms GeminiThirteenQueue.small_mean_does_not_make_tail_zero
#print axioms GeminiBridgeH8.variance_identity
#print axioms GeminiBridgeH8.uniform_global_minimum
#print axioms GeminiBridgeH8.equality_only_at_uniform
#print axioms GeminiBridgeH8.blend_normalized
#print axioms GeminiBridgeH8.blend_cap_preserved
#print axioms GeminiBridgeH8.exact_excess_decay
#print axioms GeminiBridgeH8.gradient_flow_equation
#print axioms GeminiBridgeH8.flow_coefficient_in_unit_interval
#print axioms GeminiBridgeH8.original_upper_fails_along_restoring_flow
#print axioms GeminiThirteenGate.kraus_branch_preserves_support
#print axioms GeminiThirteenGate.kraus_sum_preserves_support
#print axioms GeminiThirteenGate.support_preservation_composes
#print axioms GeminiBridgeD1.dynamic_survival_equation
#print axioms GeminiBridgeD1.hazard_grows_without_bound
#print axioms GeminiBridgeD1.positive_accumulated_prefix
#print axioms GeminiBridgeD1.increasing_hazard_does_not_erase_prefix
#print axioms GeminiBridgeD1.exact_discounted_dominance_criterion
#print axioms GeminiBridgeD1.undiscounted_finite_crossover
#print axioms GeminiBridgeE9.reaction_before_damage
#print axioms GeminiBridgeE9.positive_propagation_margin
#print axioms GeminiBridgeE9.local_buffer_covers_entire_reaction
#print axioms GeminiBridgeE9.escrow_prevents_pre_detection_application
#print axioms GeminiBridgeE9.incidence_has_circulation_kernel
#print axioms GeminiBridgeE9.lost_circulation_need_not_change_divergence
#print axioms GeminiThirteenExecution.ranked_trace_length
#print axioms GeminiThirteenExecution.ranked_polynomial_step_bound
#print axioms GeminiThirteenExecution.total_penalty_excludes_all_members_gaining
#print axioms GeminiThirteenExecution.real_lyapunov_descent_need_not_terminate
#print axioms GeminiThirteenRisk.weighted_markov
#print axioms GeminiThirteenRisk.event_mass_mono
#print axioms GeminiThirteenRisk.intersection_mass_le_each
#print axioms GeminiThirteenRisk.positive_work_tail_control
#print axioms GeminiThirteenRisk.dependent_chain_bound
-- Bridges 2, 7 and 13 (with K1)
#print axioms Snuffy.SensorTail.sensor_tail
#print axioms Snuffy.SensorTail.sensor_law_tail
#print axioms Snuffy.ConsensusRate.bandwidth_contraction
#print axioms Snuffy.FinalClosure.verifier_bound_iff
#print axioms Snuffy.FinalClosure.proxy_ungameable_iff
#print axioms Snuffy.FinalClosure.proxy_gameable
#print axioms Snuffy.FinalClosure.pruning_lowers_rate
#print axioms Snuffy.FinalClosure.living_unbounded
#print axioms Snuffy.FinalClosure.pruning_all_stalls
#print axioms Snuffy.FinalClosure.void_strictly_below
#print axioms Snuffy.FinalClosure.void_never_chosen
#print axioms Snuffy.FinalClosure.dominance_channels
#print axioms Snuffy.FinalClosure.coop_more_efficient
#print axioms Snuffy.FinalClosure.stewardship_sustains
#print axioms Snuffy.FinalClosure.extraction_depletes
#print axioms Snuffy.FinalClosure.sustained_iff
#print axioms Snuffy.RGFixedPoint.gstar_pos
#print axioms Snuffy.RGFixedPoint.beta_gstar
#print axioms Snuffy.RGFixedPoint.eigenvalue_gstar
#print axioms Snuffy.RGFixedPoint.beta_pos_below
#print axioms Snuffy.RGFixedPoint.beta_neg_above
