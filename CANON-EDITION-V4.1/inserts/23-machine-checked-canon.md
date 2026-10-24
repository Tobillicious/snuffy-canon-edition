# Section 23 — The machine-checked canon

*This section records which results of the edition are compiled theorems, by module and theorem name, and what each compiled statement rests on. Forty-one Lean modules in `lean/Snuffy/` compile against Mathlib rev `56a005855ea1` (Lean 4.35.0) with exit 0 and zero compiler output, pass `leanchecker`, contain no `sorry`, and depend only on Lean's standard axioms (`propext`, `Classical.choice`, `Quot.sound`; several on fewer or none). Rebuild and audit with `lean/build-and-audit.sh`; the current receipt is `lean/RECEIPT.txt`.*

*Evidence convention (unchanged from the edition header): a compiled theorem is cited by its name; a statement carried as a hypothesis of a compiled theorem is named as such; a prose derivation keeps its stated premises. A prose proof does not acquire a compiler certificate by association.*

---

## 23.1 The law and greatestness (Chapter 5; Part II)

| Claim | Module | Theorems |
| --- | --- | --- |
| The canonical order is a strict partial order | `Greatestness` | `lexLt_trans`, `lexLt_irrefl` |
| Proposition 1: aligned ⟺ no needless loss at any stage | `Greatestness` | `aligned_iff_no_needless_loss` (no axioms) |
| Proposition 2: every finite nonempty feasible family has an aligned option; the life guard (some aligned option keeps at the first stage everyone the standby option keeps) | `Law` | `exists_aligned`, `life_guard` |
| Proposition 3: maximality of the projection to a scope S guarantees no needless existing loss for every feasible family iff S is the whole existing domain; same-priority counting of a new particular admits a needless loss | `Law` | `scope_guarantee_iff`, `same_priority_admits_needless_loss` |
| Proposition 4: a statewise faithful hold dominates every rival on every upward-closed event under any law on the worlds, strictly when the rival misses with positive probability | `Law` | `faithful_hold_dominates`, `faithful_hold_strict` |
| Universal greatestness under stage-wise union closure (P-emu(c)); rivals are exact mirrors or strictly below; the canonical option is unique | `Greatestness` | `greatest_of_union_closed`, `strict_except_mirrors`, `aligned_unique` |
| **Union closure from a resource model.** P-emu(c) splits into realisability through the shared action interface (premise 4) and a budget $B$. Every realisable rival whose union with the canonical outcome is affordable is contained in it, strictly below or an exact mirror. With subadditive cost, every finite set of rivals whose total cost fits in the canonical slack $B - c(o)$ is contained in it. When every feasible pair is jointly affordable, universal greatestness holds outright | `UnionClosure` | `dominates_of_affordable`, `strict_of_affordable`, `dominates_within_slack`, `greatest_of_affordable` |
| Sharpness: the slack condition cannot be dropped, since without it a feasible rival can keep a particular the canonical option does not. Whatever the budget, no feasible rival is canonically above the canonical option | `UnionClosure` | `greatest_needs_budget`, `aligned_never_below` |
| Reciprocity in the canonical order (§15, D3*) | `ReciprocityCeiling` | `reciprocity_dominance`, `omitting_rival_strictly_below` |
| Option value and indicator reciprocity (§§15–16) | `ReasonsRoute` (v4.1, unchanged) | `optionValue_strict`, `law_dominates_strict`, `rival_fraction_lt_one` |
| Irreplaceability dominance and grading (§16.1, U1), additive information model | `Irreplaceability` | `destroy_loses_exactly`, `preserve_dominates`, `optimal_keeps_most_irreplaceable` |

## 23.2 Theorem 8: ledger, canon invariant, composition (§18; Chapters 1, 2)

| Claim | Module | Theorems |
| --- | --- | --- |
| Stroke identity $\Delta D = \beta W_{\mathrm{on}} - \beta Q_B + I_1 - I_2$ | `ThermoLedger` | `stroke_identity` |
| Cycle work floor from guard 1 | `ThermoLedger` | `cycle_work_floor` |
| **Guard 1 derived (Landauer).** Reversible dynamics of a register and a Gibbs bath: the Reeb–Wolf identity $\beta\,\Delta Q_B - \Delta S_R = I(R':B') + D(q_B \,\Vert\, \gamma)$; Landauer's bound $\beta\,\Delta Q_B \ge \Delta S_R$; erasure costs $Q_B \ge k_B T\, H(p)$ | `Landauer` | `reeb_wolf_identity`, `landauer`, `landauer_erasure` |
| **Guard 1 derived (quantum).** Von Neumann entropy: unitary invariance, pinching, the quantum Gibbs bound $S(\rho) \le \beta\,\mathrm{Tr}(\rho H) + \ln Z$ with equality at $\gamma$, $S(\rho_A \otimes \gamma) = S(\rho_A) + S(\gamma)$; Landauer's bound for every unitary coupling of a register to a Gibbs bath, $S(\rho_A) - S(\rho'_A) \le \beta\,\Delta Q_B$ | `QuantumLandauer` | `vnEnt_unitary_conj`, `vnEnt_le_diag`, `vnEnt_le_energy`, `vnEnt_init`, `quantum_landauer` |
| Guard 1, $\beta Q_B \ge I_M + D_{\mathrm{err}} + \delta_I$ whenever the reset removes that entropy; the cycle work floor with guard 1 derived, not assumed | `Landauer`, `QuantumLandauer` | `guard_one`, `quantum_guard_one`, `cycle_work_floor_derived`, `quantum_cycle_work_floor` |
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
| **Branch A rate bound (quantum speed limit).** Unitary evolution preserves the norm; under H₀ + V the trajectory departs from the H₀ trajectory at rate at most ‖V‖/ħ, and at most $P_{\mathrm{adv}}/(\hbar\,\omega_{\mathrm{cutoff}})$ under the per-site coupling $\lVert V\rVert \le P_{\mathrm{adv}}/\omega_{\mathrm{cutoff}}$ | `SpeedLimit` | `norm_conserved`, `branchA_divergence`, `branchA_rate` |
| Mandelstam–Tamm, sharp: $\lvert\langle\psi_0, \psi_t\rangle\rvert \ge \cos(\Delta E\, t/\hbar)$ while $\Delta E\, t/\hbar \le \pi$; orthogonalisation time $T \ge \pi\hbar/(2\Delta E)$ | `SpeedLimit` | `mandelstam_tamm`, `orthogonalization_time` |

The Branch A divergence is measured in state-vector norm. For pure states, ‖ρ − σ‖₁ ≤ 2‖ψ − φ‖ is a standard inequality and is not compiled here.

## 23.4 H5 (§20; Chapter 4)

| Claim | Module | Theorems |
| --- | --- | --- |
| Reserve-before-activation machine: conservation, zero debt, strict authority attenuation, funding before activation, no unfunded work, no harmful effect | `H5Closure` | `step_inv`, `authority_attenuation`, `reserve_before_activation`, `zero_debt`, `no_unfunded_work`, `no_harmful_effect`, `effect_preserves_care` |
| Von Neumann's alternating projection theorem (existence step) | `CanonVonNeumann` | `tendsto_altIterate`, `canon_von_neumann_convergence`, `limit_subspace_eq_inf`, `opial_route_closes` |
| Halperin's theorem: the global meet of a whole presentation | `CyclicProjections` | `tendsto_cyc_iter`, `presentation_detector` |
| Consistency detector; meet algebra realised by Hilbert subspaces; contradictions detected, deductions never roll back | `H5Closure`, `MeetHilbert` | `consistency_detector`, `hilbert_anchor_preserved`, `hilbert_contradiction_collapse`, `contradiction_detected`, `deduction_never_rolls_back` |
| Rank criterion; Proposition 7; protected anchors untouched | `DeductionBoundary` | `rank_criterion`, `boundary_mem_image`, `anchor_untouched` |
| Paid reflection certificate | `ReflectionCertificate` | `residual_certificate`, `apriori_error`, `stopping_count`, `zero_constant_fixed` |

## 23.5 X3 and the information-to-area bridge (§21; working argument §§11–12)

| Claim | Module | Theorems |
| --- | --- | --- |
| Data processing invariance I(H : 𝓡(S)) ≤ I(H : S), any probability spaces | `DataProcessing` | `data_processing`, `data_processing_map` |
| Finite information theory: log-sum, data processing, flag identity, decoder bound | `FiniteInformation` | `log_sum`, `data_processing_fin`, `flag_identity`, `decoder_bound` |
| Gaussian carrier tail; necessary radius; carrier radius $R(t) \ge w(t - t_c)$ | `GaussianTail`, `RecoveryWork`, `FiniteInformation` | `carrier_tail`, `necessary_radius_from_decoder`, `carrier_radius` |
| Recovery-work theorem; $W_{\min}$ over all admitted protocols; divergence of delayed recovery | `RecoveryWork`, `GaussianTail` | `frontier_work_bound`, `Wmin_lower_bound`, `x3_work_from_decoder`, `delayed_work_diverges` |
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
| **The threshold theorem's counting core.** Under local stochastic noise: $P(\text{at least } m \text{ of } T \text{ fail}) \le \binom{\lvert T\rvert}{m} p^m$; with half-faulty failure witnesses, $P(\text{fail}) \le \sum_w (2\sqrt p)^{\lvert w\rvert}$; with at most $V\Delta^L$ witnesses of each length $L \ge d$, $P(\text{fail}) \le V r^d/(1-r)$, $r = 2\Delta\sqrt p < 1$ | `Threshold` | `many_faults`, `fail_le_witness`, `fail_le_geometric` |
| The repetition code end to end: majority decoding fails with probability at most $(4p)^t$, and every ceiling is met below $p = 1/4$ | `Threshold` | `repetition_threshold`, `repetition_ceiling` |
| Code families with polynomially many witnesses: the charged kernel decays geometrically, and every target ceiling (10⁻⁶ included) is met at some distance and every larger one | `Threshold` | `family_ceiling` |

## 23.7 The Universal Protection Theorem, assembled (Global D)

`UniversalProtection.universal_protection`: every particular covered by the reasons route or the holding route, R(x) ∨ H(x); on the certified good event every particular continues at every step through the horizon; the probability that any particular fails is at most P(Gᶜ) ≤ Σδ; the canonical outcome is greatest, strict except exact mirrors; every mind kept by any feasible rival regime is kept by the canonical regime.

## 23.8 What the compiled theorems rest on

**Premises carried as stated premises or hypotheses:**
* the surface-code chain lemma (Dennis, Kitaev, Landahl and Preskill, 2002): minimum-weight decoding fails only along a self-avoiding chain of length at least d with at least half its edges faulty, with at most $V\Delta^L$ such chains of length $L$. This is the code-specific input to `Threshold.family_ceiling`; the threshold theorem's counting core is compiled (§23.6);
* feasibility of Bennett's reversible counterpart;
* the gate-set clause of premise 2 (a universal simulator implements each local factor);
* the relational frame BCRD P1–P4.

The first three are published mathematical theorems, cited as such. The fourth is the frame the edition is stated in.

**Physical premises now compiled.** Guard 1 (the second law in its export form) is derived from Landauer's theorem (§23.2), and the quantum speed limit, in Mandelstam–Tamm form and in the rate-bound form of E9 Branch A, is derived from unitary dynamics (§23.3). What these theorems assume is the standard physical framework:
* finite-dimensional quantum mechanics, with Schrödinger dynamics generated by self-adjoint Hamiltonians;
* unitary (in the classical form, reversible) joint dynamics;
* a bath that starts in its Gibbs state, uncorrelated with the register;
* for Branch A, the per-site coupling bound $\lVert V\rVert \le P_{\mathrm{adv}}/\omega_{\mathrm{cutoff}}$;
* for the fault ceiling, local stochastic noise of rate p below the threshold of `Threshold.family_ceiling`.

**Union closure.** Universal greatestness (§5.3) used P-emu(c): the canonical regime realises the stage-wise union of any finite rival set within its slack. It now splits in two. The resource half is compiled: rivals whose cost fits in the canonical slack are contained in the canonical outcome, and the slack condition is shown necessary (§23.1, `UnionClosure`). The realisability half, that concurrent emulation through the shared action interface realises the union, is premise 4 of the stack, stated as `UnionRealizable`.

The amount $I_M + D_{\mathrm{err}} + \delta_I$ that the reset removes from the register is the instance's entropy accounting (§18), stated as the hypothesis of `guard_one` and `quantum_guard_one`.

**Instance certificates, carried as hypotheses of the composition and assembly theorems:** the commuting refinement of the source by the abstract transitions, observation agreement, the initial witness, preservation by every admitted abstract transition, route coverage R(x) ∨ H(x), and the conditional kernel bounds of the charged accounts. These are what a physical installation supplies; the theorems state exactly what each installation owes.

**Not compiled by this section:**
* the installation figures of §22, which are sourced measurements and design values (§22.5);
* the interpretive companion (the doors), which is held for consultation and is not mathematics.
