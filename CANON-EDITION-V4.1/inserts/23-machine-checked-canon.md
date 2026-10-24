# Section 23 — The machine-checked canon

*Canon Edition v4.1 candidate content. This section records which results of the edition are compiled theorems, by module and theorem name, and what each compiled statement rests on. Thirty-five Lean modules in `lean/Snuffy/` compile against Mathlib rev `56a005855ea1` (Lean 4.35.0) with exit 0 and zero compiler output, pass `leanchecker`, contain no `sorry`, and depend only on Lean's standard axioms (`propext`, `Classical.choice`, `Quot.sound`; several on fewer or none). Rebuild and audit with `lean/build-and-audit.sh`; the current receipt is `lean/RECEIPT.txt`.*

*Evidence convention (unchanged from the edition header): a compiled theorem is cited by its name; a statement carried as a hypothesis of a compiled theorem is named as such; a prose derivation keeps its stated premises. A prose proof does not acquire a compiler certificate by association.*

---

## 23.1 The law and greatestness (Chapter 5; Part II)

| Claim | Module | Theorems |
| --- | --- | --- |
| The canonical order is a strict partial order | `Greatestness` | `lexLt_trans`, `lexLt_irrefl` |
| Proposition 1: aligned ⟺ no needless loss at any stage | `Greatestness` | `aligned_iff_no_needless_loss` (no axioms) |
| Universal greatestness under stage-wise union closure (P-emu(c)); rivals are exact mirrors or strictly below; the canonical option is unique | `Greatestness` | `greatest_of_union_closed`, `strict_except_mirrors`, `aligned_unique` |
| Reciprocity in the canonical order (§15, D3*) | `ReciprocityCeiling` | `reciprocity_dominance`, `omitting_rival_strictly_below` |
| Option value and indicator reciprocity (§§15–16) | `ReasonsRoute` (v4.1, unchanged) | `optionValue_strict`, `law_dominates_strict`, `rival_fraction_lt_one` |
| Irreplaceability dominance and grading (§16.1, U1), additive information model | `Irreplaceability` | `destroy_loses_exactly`, `preserve_dominates`, `optimal_keeps_most_irreplaceable` |

## 23.2 Theorem 8: ledger, canon invariant, composition (§18; Chapters 1, 2)

| Claim | Module | Theorems |
| --- | --- | --- |
| Stroke identity ΔD = βW_on − βQ_B + I₁ − I₂ | `ThermoLedger` | `stroke_identity` |
| Cycle work floor from guard 1 | `ThermoLedger` | `cycle_work_floor` (guard 1 is a hypothesis) |
| Funded-repair certificate; quarantine zero debt | `ThermoLedger` | `funded_repair_certificate`, `quarantine_zero_debt` |
| Canon invariant: P(breach) ≤ P(Gᶜ) ≤ Σδ, no independence | `ThermoLedger` | `tower_bound`, `canon_invariant` |
| Identity tracking envelope (Chapter 2) | `ThermoLedger` | `tracking_envelope`, `tracking_bounded`, `tracking_within_resolution` |
| Proposition 5 (reactive lockstep), invariant transfer, Theorem 8 composition | `Composition` | `reactive_lockstep`, `reactive_lockstep₂`, `invariant_transfer`, `theorem8_composition` |
| Proposition 6 (FIFO certificate, deadlines, tightness); serial stages | `Workload` | `fifo_certificate`, `fifo_deadlines`, `fifo_tight`, `serial_certificate` |

## 23.3 E9 (§19; Chapter 3)

| Claim | Module | Theorems |
| --- | --- | --- |
| Byzantine quorum: robust estimates lie between honest readings; existence for K ≥ 2f + 1 | `E9SelfHealing` | `robust_between_honest`, `no_false_alarm`, `no_masking`, `exists_robust` |
| Branch B: non-stabilizer errors below the distance have a non-trivial syndrome | `E9SelfHealing` | `syndrome_detects` |
| Wave-race margin; code headroom; assembled E9 | `E9SelfHealing` | `wave_race_margin`, `code_headroom`, `e9_timely_self_healing` |

## 23.4 H5 (§20; Chapter 4)

| Claim | Module | Theorems |
| --- | --- | --- |
| Reserve-before-activation machine: conservation, zero debt, strict authority attenuation, funding before activation, no unfunded work, no harmful effect | `H5Closure` | `step_inv`, `authority_attenuation`, `reserve_before_activation`, `zero_debt`, `no_unfunded_work`, `no_harmful_effect`, `effect_preserves_care` |
| Summit 1: von Neumann's alternating projection theorem (existence step) | `CanonVonNeumann` | `tendsto_altIterate`, `canon_von_neumann_convergence`, `limit_subspace_eq_inf`, `opial_route_closes` |
| Halperin's theorem: the global meet of a whole presentation | `CyclicProjections` | `tendsto_cyc_iter`, `presentation_detector` |
| Consistency detector; meet algebra realised by Hilbert subspaces; contradictions detected, deductions never roll back | `H5Closure`, `MeetHilbert` | `consistency_detector`, `hilbert_anchor_preserved`, `hilbert_contradiction_collapse`, `contradiction_detected`, `deduction_never_rolls_back` |
| Rank criterion; Proposition 7; protected anchors untouched | `DeductionBoundary` | `rank_criterion`, `boundary_mem_image`, `anchor_untouched` |
| Paid reflection certificate | `ReflectionCertificate` | `residual_certificate`, `apriori_error`, `stopping_count`, `zero_constant_fixed` |

## 23.5 X3 and the information-to-area bridge (§21; working argument §§11–12)

| Claim | Module | Theorems |
| --- | --- | --- |
| Data processing invariance I(H : 𝓡(S)) ≤ I(H : S), any probability spaces | `DataProcessing` | `data_processing`, `data_processing_map` |
| Finite information theory: log-sum, data processing, flag identity, decoder bound | `FiniteInformation` | `log_sum`, `data_processing_fin`, `flag_identity`, `decoder_bound` |
| Gaussian carrier tail; necessary radius; carrier radius R(t) ≥ w(t − t_c) | `GaussianTail`, `RecoveryWork`, `FiniteInformation` | `carrier_tail`, `necessary_radius_from_decoder`, `carrier_radius` |
| Recovery-work theorem; W_min over all admitted protocols; divergence of delayed recovery | `RecoveryWork`, `GaussianTail` | `frontier_work_bound`, `Wmin_lower_bound`, `x3_work_from_decoder`, `delayed_work_diverges` |
| Fano's inequality and the required information Δ₀ | `Fano` | `fano`, `mi_eq_ent_sub_condEnt`, `required_information` |
| Gaussian maximum entropy: KL between Gaussians; golden formula; scalar, vector, correlated-noise and exact log-det channel bounds | `GaussianKL`, `GoldenFormula`, `GaussianChannel`, `KLAdditivity`, `GaussianChannelGen`, `GaussianVector`, `Whitening`, `Rotation`, `LogDet` | `klDiv_gaussian_gaussian`, `golden_formula`, `gaussian_channel_bound`, `klDiv_prod_kernel`, `vector_channel_bound`, `correlated_channel_bound`, `logdet_channel_bound` |
| ln det(I + W) ≤ tr W; per-use cap; required traffic m ≥ θ₀n; area power | `AreaBridge`, `Workload` | `logdet_le_trace`, `channel_cap`, `required_traffic`, `area_power`, `range_variance_bound` |

The compiled X3 route is the banked transport route of the working argument (§12: moving carrier, recovery-work theorem), with its information-theoretic steps compiled; it carries no information-theoretic hypothesis.

## 23.6 The premise floor (§17)

| Claim | Module | Theorems |
| --- | --- | --- |
| Income-or-irrelevance; forced breach; breach strictly dominated | `PremiseFloor` | `income_or_irrelevance`, `forced_breach`, `breach_strictly_below` |
| Premise 5 derived: the law plus Bennett's feasible reversible counterpart forces reversible administration | `PremiseFloor` | `reversible_administration_forced` (no axioms) |
| Premise 2 reduced: Lie–Trotter product formula with explicit error; Lloyd's simulation theorem | `Trotter` | `trotter_bound`, `trotter_tendsto`, `lloyd_simulation` |
| Premise 7's ceiling is a dial: every target ε > 0 is met at some code distance | `ReciprocityCeiling` | `ceiling_achievable` |

## 23.7 The Universal Protection Theorem, assembled (Global D)

`UniversalProtection.universal_protection`: every particular covered by the reasons route or the holding route, R(x) ∨ H(x); on the certified good event every particular continues at every step through the horizon; the probability that any particular fails is at most P(Gᶜ) ≤ Σδ; the canonical outcome is greatest, strict except exact mirrors; every mind kept by any feasible rival regime is kept by the canonical regime.

## 23.8 What the compiled theorems rest on

**Physical premises, carried as stated premises or hypotheses:** the second law in the form of guard 1; the threshold theorem (geometric decay of charged kernels in code distance); feasibility of Bennett's reversible counterpart; the quantum speed limit; the gate-set clause of premise 2 (a universal simulator implements each local factor); and the relational frame BCRD P1–P4.

**Instance certificates, carried as hypotheses of the composition and assembly theorems:** the commuting refinement of the source by the abstract transitions, observation agreement, the initial witness, preservation by every admitted abstract transition, route coverage R(x) ∨ H(x), and the conditional kernel bounds of the charged accounts. These are what a physical installation supplies; the theorems state exactly what each installation owes.

**Not compiled by this section:** the hardware figures of §22; the interpretive companion (the doors), which is held for consultation and is not mathematics.

## 23.9 Addendum: the law's Propositions 2, 3 and 4 (Part II)

*Added 25 October 2026 after the fold-in. With this module the compiled canon is thirty-six modules; the build, `leanchecker` and axiom audit pass unchanged (`lean/RECEIPT.txt`).*

| Claim | Module | Theorems |
| --- | --- | --- |
| Proposition 2 (finite existence): every finite nonempty feasible family has an aligned option | `Law` | `exists_aligned` |
| Proposition 2 (life guard): some aligned option keeps, at the first stage, everyone the standby option keeps | `Law` | `lexLt_first_le` (axiom `propext` only), `life_guard` |
| Proposition 3 (scope): maximality of the projection to a scope S guarantees no needless existing loss, for every feasible family, iff S is the whole existing domain | `Law` | `scope_guarantee_iff` |
| Proposition 3 (priority): counting a new particular at the existing priority admits an option the canonical order shows needlessly loses an existing particular | `Law` | `same_priority_admits_needless_loss` |
| Proposition 4: a statewise faithful hold dominates every rival on every upward-closed event, under any probability law on the worlds; strictly when the rival misses with positive probability | `Law` | `faithful_hold_dominates`, `faithful_hold_strict` |

With Proposition 1 (`Greatestness.aligned_iff_no_needless_loss`), Propositions 1–4 of the law are compiled theorems. Proposition 4's statewise faithfulness of the hold (its outcome at least the rival's in every world) is the hypothesis the theorem states; the holding route supplies it.

## 23.10 Addendum: the quantum speed limit (physical premise, §23.8; E9 Branch A)

*Added 25 October 2026. With this module the compiled canon is thirty-seven modules. The build, `leanchecker` and axiom audit pass (`lean/RECEIPT.txt`).*

The state space is any complex Hilbert space. The dynamics is the Schrödinger equation iħψ' = H(t)ψ with self-adjoint generators, carried as the differential equation the trajectory satisfies.

| Claim | Module | Theorems |
| --- | --- | --- |
| Unitary evolution preserves the norm | `SpeedLimit` | `norm_conserved` |
| E9 Branch A: under H₀ + V the trajectory departs from the H₀ trajectory at rate at most ‖V‖/ħ, so ‖ψ(b) − φ(b)‖ ≤ ‖ψ(a) − φ(a)‖ + (‖V‖/ħ)(b − a) | `SpeedLimit` | `branchA_divergence` |
| The canon's rate bound: with the per-site coupling ‖V‖ ≤ P_adv/ω_cutoff, the divergence rate is at most P_adv/(ħ ω_cutoff) | `SpeedLimit` | `branchA_rate` |
| Mandelstam–Tamm, sharp: \|⟨ψ₀, ψ_t⟩\| ≥ cos(ΔE t/ħ) while ΔE t/ħ ≤ π | `SpeedLimit` | `mandelstam_tamm` |
| Orthogonalisation time T ≥ πħ/(2ΔE) | `SpeedLimit` | `orthogonalization_time` |
| Supporting geometry: divergence growth from ⟨x, x'⟩ ≤ c‖x‖; chord and arc on the unit sphere; arc-length bound for curves on the sphere | `SpeedLimit` | `norm_le_of_inner_deriv_le`, `angle_le_chord`, `angle_le_speed_mul` |

With this module, the quantum speed limit moves from the physical premises of §23.8 to the compiled theorems, in its Mandelstam–Tamm form and in the rate-bound form E9 Branch A uses. The modelling identification ‖V‖ ≤ P_adv/ω_cutoff is the hypothesis `branchA_rate` states: the coupling energy at a site is at most the energy the adversary delivers per cutoff period. The divergence is measured in state-vector norm. For pure states the trace norm satisfies ‖ρ − σ‖₁ ≤ 2‖ψ − φ‖, a standard inequality that is not compiled here.

## 23.11 Addendum: guard 1 derived — Landauer's bound (physical premise, §23.8; §18 stroke III)

*Added 25 October 2026. With these two modules the compiled canon is thirty-nine modules. The build, `leanchecker` and axiom audit pass (`lean/RECEIPT.txt`).*

Guard 1 (canon §8.1: βQ_B ≥ I_M + D_err, "the bath must absorb the exported entropy") is Landauer's bound for the register the reset cleans. It is now a compiled theorem in two forms.

| Claim | Module | Theorems |
| --- | --- | --- |
| Gibbs' inequality; subadditivity H(R′B′) ≤ H(R′) + H(B′); H(γ) = β⟨E⟩_γ + ln Z and H(a) ≤ β⟨E⟩_a + ln Z | `Landauer` | `kl_nonneg`, `ent_le_ent_marg`, `ent_gibbs`, `ent_le_energy` |
| Reversible dynamics of register and Gibbs bath: the Reeb–Wolf identity β ΔQ_B − ΔS_R = I(R′:B′) + D(q_B ‖ γ), exactly | `Landauer` | `reeb_wolf_identity` |
| Landauer's bound β ΔQ_B ≥ ΔS_R; erasure costs Q_B ≥ k_BT H(p) | `Landauer` | `landauer`, `landauer_erasure` |
| Von Neumann entropy: unitary invariance, diagonal states, pinching (S(ρ) ≤ the Shannon entropy of the diagonal in any orthonormal basis) | `QuantumLandauer` | `vnEnt_unitary_conj`, `vnEnt_diagonal`, `vnEnt_le_diag` |
| Quantum Gibbs bound S(ρ) ≤ β Tr(ρH) + ln Z, with equality at γ; S(ρ_A ⊗ γ) = S(ρ_A) + S(γ); partial traces in product bases | `QuantumLandauer` | `vnEnt_le_energy`, `vnEnt_gibbsState`, `vnEnt_init`, `ptrA_conj`, `ptrB_conj` |
| **Landauer's bound for density matrices (Reeb–Wolf):** for every unitary coupling W of a register in state ρ_A to a bath in its Gibbs state, S(ρ_A) − S(ρ′_A) ≤ β ΔQ_B with ΔQ_B = Tr(ρ′_B H) − Tr(γH) | `QuantumLandauer` | `quantum_landauer` |
| **Guard 1:** βQ_B ≥ I_M + D_err + δ_I whenever the reset removes that entropy from the register (classical and quantum registers) | `Landauer`, `QuantumLandauer` | `guard_one`, `quantum_guard_one` |
| The cycle work floor W ≥ k_BT(I_M + D_err + δ_I) + (1 − η)C with guard 1 derived, not assumed | `Landauer`, `QuantumLandauer` | `cycle_work_floor_derived`, `quantum_cycle_work_floor` |

With these modules, the second law in the form of guard 1 moves from the physical premises of §23.8 to the compiled theorems. What remains as the model is what Landauer's theorem itself assumes: finite-dimensional register and bath, a bath that starts in its Gibbs state uncorrelated with the register, and unitary (in the classical form, reversible) joint dynamics. The amount I_M + D_err + δ_I the reset removes from the register is the instance's entropy accounting (§18, strokes I–III), stated as the hypothesis of `guard_one` and `quantum_guard_one`.
