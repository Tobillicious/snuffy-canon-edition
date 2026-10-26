# Before/after batch 07 — full decoding history and reference-preserving preparation

Local draft only. The compiled core, proposed source application, and unfinished physical certificate are distinguished.

### SNUFFY-CANON-EDITION-4.2-MASTER.md

```diff
--- SNUFFY-CANON-EDITION-4.2-MASTER.md (before)
+++ SNUFFY-CANON-EDITION-4.2-MASTER.md (draft after)
@@ -8,7 +8,13 @@
 
 The three joined supports retain their full targets: the full-domain physical certificate (G1), realisability of the whole continuation-and-freedom tuple (G2), and recovery success with a complete pathwise work certificate (G3). This repair checkpoint corrects the normalised quantum-state domain and the clipped-reserve contraction, and develops the actual Bennett implementation. The physical source, whole-outcome, device-cost and external-theorem application correspondences remain explicit construction work; the component theorems do not by themselves declare the maximal argument complete.
 
-The current Lean tree contains 189 modules and 1133 audited public theorem/lemma names. All 189 modules were freshly compiled and kernel-checked in one run, and the full axiom audit over all 1133 names and the completeness and claims gates were freshly run, overall PASS. The earlier receipts, including the 924-name combined receipt that reused Beam's 136 results, are preserved with their banks. Seven previously omitted public helper lemmas are included. The original published 115-module/831-name baseline remains preserved. The architecture interfaces and their construction links are distinguished in Section 23.9.
+The current draft Lean tree contains 191 modules and 1150 public theorem/lemma names.
+Checkpoint 10 freshly compiled and kernel-checked all 189 modules then present and passed the
+1140-name axiom audit, completeness and claims gates. The two further modules, HistoryPolymer
+and ThermalEncoding (10 public names), passed targeted compilation and kernel checking with
+zero output. Checkpoint 11 is the fresh full 191-module audit; its result must be read before
+claiming that the expanded tree has a combined PASS. Earlier receipts are preserved for exactly
+the sources they cover. The original published 115-module/831-name baseline is unchanged.
 
 **Structure.** Part I states the frame and premise stack. Part II supplies the law, the derived holding bridge and the retained instruments. Part III retains the five-chapter synthesis; Sections 15–24 develop the reasons, physical and compiled arguments. Part III-C records the three joined supports and their constructions. Part IV gives references and provenance. Theorem and proposition numbers follow the programme's proof register.
 
@@ -1454,7 +1460,13 @@
 
 ## Section 23 — The machine-checked canon
 
-*This section maps the edition's compiled results and their actual hypotheses. The current source contains 189 modules and 1133 audited public theorem/lemma names. The receipt records a fresh compilation and kernel check of every module, a fresh full axiom audit with only `propext`, `Classical.choice` and `Quot.sound`, and fresh completeness/claims gates with overall PASS. Section 23.9 gives the new interfaces and derived adapters; their verification does not substitute their names for the full source construction.*
+*This section maps the edition's compiled results and their actual hypotheses. The current draft Lean tree contains 191 modules and 1150 public theorem/lemma names.
+Checkpoint 10 freshly compiled and kernel-checked all 189 modules then present and passed the
+1140-name axiom audit, completeness and claims gates. The two further modules, HistoryPolymer
+and ThermalEncoding (10 public names), passed targeted compilation and kernel checking with
+zero output. Checkpoint 11 is the fresh full 191-module audit; its result must be read before
+claiming that the expanded tree has a combined PASS. Earlier receipts are preserved for exactly
+the sources they cover. The original published 115-module/831-name baseline is unchanged. Section 23.9 distinguishes the interfaces, derived adapters and remaining physical applications.*
 
 *Evidence convention (unchanged from the edition header): a compiled theorem is cited by its name; a statement carried as a hypothesis of a compiled theorem is named as such; a prose derivation keeps its stated premises. A prose proof does not acquire a compiler certificate by association.*
 
@@ -1645,6 +1657,8 @@
 | `WeightedEdgeLaw` | Weighted fault rates push forward to edge rates; with the enumerated edge rate 94/15·p and walk bound 9.87, the explicit threshold exceeds 4×10⁻⁴ (G.19) |
 | `WarmStart` | A warm start, a prepared syndrome law at most C times the thermal law pointwise, stays dominated at every time, so every event keeps the stationary bound up to C (G.20) |
 | `WalkBound9` | The length-9 walk bound c₉ = 763,504,745 ≤ 9.71⁹ gives an explicit threshold above 4.2×10⁻⁴ (G.20) |
+| `HistoryPolymer` | Deterministic history support budget, component restriction, truncation factors and finite sampling-path bounds (G.21) |
+| `ThermalEncoding` | Orthogonal syndrome-mixture recovery, including arbitrary reference correlations (G.21) |
 
 The earlier `G1Certificate.universal_protection_held` has conclusion `True`; it is a placeholder and is not the protection theorem `Bridge.universal_protection_held`. The latter's full source certificate is constructed in G.10 (`G1Held.held_source_protection`). The exact integration history and dependency trace accompany this working edition.
 
@@ -1842,8 +1856,10 @@
 | `BennettBatch` | `batched_window`, `premise5_batched` |
 | `WeightedEdgeLaw` | `push_weighted`, `push_uniform`, `rate_iff`, `tightened_threshold`, `walk_bound`, `threshold_value` |
 | `StageSchedule` | `total_with_transfers`, `stage_cost_le` |
-| `WarmStart` | `warm_start`, `warm_start_event` |
+| `WarmStart` | `warm_start`, `warm_start_event`, `fibre_mass_pos`, `fibre_reassembly`, `reverse_sampler_bound`, `heat_bath_normalized`, `heat_bath_stationary`, `pointwise_from_absolute`, `warm_start_from_mixing` |
 | `WalkBound9` | `walk_bound_9`, `threshold_9`, `threshold_9_value` |
+| `HistoryPolymer` | `halving_prefix`, `paired_history_bound`, `component_valid`, `truncation_bound`, `sampled_truncation_bound`, `branch_path_bound` |
+| `ThermalEncoding` | `branch_compression`, `recovers`, `kron_orthogonal`, `recovers_reference` |
 <!-- END THEOREM INDEX -->
 
 ---
@@ -3368,13 +3384,285 @@
 level 2, with \(\ell=3\). Hence for every fixed range a single violated check passes all local
 metachecks yet is invalid.
 
-The remaining problem is a multiscale, recursive cluster expansion of the code's syndrome Gibbs law
-that treats level-\(j\) metachecks at scale \(\ell^j\), together with a sampler built from it,
-yielding a warm start with polynomial constant. This is the technique Balasubramanian, Davydova,
-Lin and Thorngren apply to the classical two-dimensional model (arXiv:2610.22548). Given it, the
-quantum branch closes through `StageSchedule.total_with_transfers`. Until then, indefinite holding
-of full quantum coherence is proved conditional on this one stated problem, while the objective
-classical record and its relations are held unconditionally (`PassiveReference`).
+Section G.21 develops a constructive full-history polymer sampler for the ideal thermal
+syndrome law, with its counting theorem and source correspondence stated explicitly. It avoids
+the failed product/deletion hypothesis and does not require a preparation mixing estimate.
+`WarmStart.fibre_reassembly` and `reverse_sampler_bound` give the exact probability-composition
+algebra. `pointwise_from_absolute` retains the probability floor whenever an absolute-error
+estimate is used. The actual noisy preparation/handoff and complete-cost application remain
+unfinished; the maximal quantum-coherence target is retained in full.
+
+---
+
+## G.21 Constructive thermal preparation from the complete decoding history
+
+Working derivation for author review, 26 October 2026. The generic support lemmas are compiled; the source application and physical join retain their separate verification statuses. The target is the actual
+BDL thermal syndrome law with a polynomial, preferably constant, one-sided
+pointwise factor. This does not assume product zero-excess fibres, a local
+mixing gap, an initially warm raw state or a reset of protected quantum data.
+
+### 1. Retain the full deterministic history
+
+For one syndrome sector of C(2k), introduce one binary variable for every
+syndrome coordinate at every level:
+
+    h = (s_2k, s_(2k-1), ..., s_0).
+
+Fix all local tie-breaks in the published coarse-graining maps, with the
+zero input producing zero corrections. A valid finest syndrome determines
+exactly one history. Conversely, the following finite local constraints
+characterize such histories:
+
+* For an R_X step, use (L1), (L2), (L3) of STEP2-FINE-CONDITIONAL.md, with
+  the coarse output stored as the next layer's variables.
+* For an R_Z step, use the local cohomology-class reduction in Theorem 4.6.
+  The difference from the lifted coarse value is a local coboundary.
+* The constant-sized seed syndrome s_0 must belong to its actual image(delta).
+
+Backward induction using s_i=delta(f_i)+F_i(s_(i-1)) proves global validity
+at every level. Forward evaluation of the fixed local rules proves
+uniqueness. These are constraints on syndrome variables; f_i is computed,
+not summed over as an additional freely degenerate variable.
+
+Each constraint has bounded scope and each coordinate appears in boundedly
+many constraints, uniformly in k. The bounds depend on the fixed gadget
+size, Tanner degrees and subdivision parameter. The seed constraint has
+constant scope. Make the primal graph G by connecting every pair of
+coordinates in a common constraint scope. Its degree Delta is bounded
+independently of k. Its number M of vertices is polynomial in the physical
+block size (indeed at most the sum of the level sizes).
+
+The local source correspondence is BDL Theorems 4.6 and 4.7, Remarks 4.4–4.5,
+and the bounded-degree construction. Their Section 5.2 already records full
+decoding histories and proves componentwise coarse-graining. The primal
+graph used here includes whole constraint scopes, so component restriction
+does not assume the stronger product property that failed numerically.
+
+### 2. Derive the history energy bound
+
+Write the history in the finest-to-coarsest direction. Every R_Z step is
+non-increasing in syndrome weight; every R_X step reduces it by at least
+one half. The two steps alternate. Thus, in either sector,
+
+    |s_(i-2)| <= |s_i|/2,
+    sum_i |s_i| <= 2 sum_(j>=0) 2^(-j) |s_2k| <= 4 |s_2k|.
+
+This holds for every valid history, including a history obtained by
+restricting to one connected support component. It is a support/energy
+inequality on the complete history, not a fixed-range metacheck assumption.
+
+### 3. Connected components give an exact polymer representation
+
+The all-zero history satisfies every constraint. Let h be valid and let
+Gamma be a connected component of its occupied coordinates in G. Setting
+all other coordinates to zero leaves a valid history:
+
+* a constraint touching Gamma cannot touch another occupied component,
+  because its scope is a clique;
+* on that scope the restricted assignment either agrees with h or is zero;
+* both assignments satisfy the constraint in the respective case.
+
+Conversely, the union of pairwise nonadjacent valid connected supports is
+valid by the same scope argument. Hence there is an exact bijection between
+histories and compatible polymer families. A polymer is a nonempty connected
+support Gamma whose standalone binary assignment satisfies every constraint.
+
+Let E(Gamma) count its occupied *finest-level* coordinates. The previous
+bound applied to that standalone valid history gives
+
+    E(Gamma) >= |Gamma|/4 > 0.
+
+There is no zero-energy polymer. Its activity at z=exp(-beta) is the
+monomial w_Gamma(z)=z^E(Gamma). Energy is additive on disjoint components.
+The polymer partition function is therefore exactly the thermal partition
+function on valid finest syndromes: there is no uncounted fibre multiplicity.
+
+### 4. Verify convergence with explicit constants
+
+Put B=(Delta+1)^2. A rooted depth-first traversal bounds the number of
+connected supports of size ell containing a fixed vertex by B^ell. There
+is at most one binary polymer assignment on a given support.
+
+An incompatible polymer meets the closed neighbourhood of Gamma, of size
+at most (Delta+1)|Gamma|. For r=B e |z|^(1/4),
+
+    sum_(eta incompatible Gamma) |w_eta(z)| exp(|eta|)
+       <= (Delta+1)|Gamma| sum_(ell>=1) r^ell
+       = (Delta+1)|Gamma| r/(1-r).
+
+For example choose the complex fugacity disk
+
+    delta = [1/(4 e B (Delta+2))]^4.
+
+Then r<1/[4(Delta+2)] throughout |z|<delta, so the displayed sum is less
+than |Gamma|. This is the Kotecky–Preiss criterion, derived here from the
+actual history bound. Taking the device temperature sufficiently low that
+0<z_0<delta, as well as below BDL's memory threshold, gives uniform slack.
+
+The algorithmic counting hypotheses are also explicit: connected supports
+of size ell can be listed in exp(O(ell+log M)); testing their local
+constraints and computing E takes polynomial time in ell; activities are
+monomials of order at least |Gamma|/4; and the full partition polynomial has
+degree at most the number of finest checks, hence at most M. The same
+convergence bound holds after deleting any set of polymers.
+
+Helmuth–Perkins–Regts Theorem 2.2 and its Section 2.6 generalization then
+supply a deterministic relative partition-function approximation for every
+remaining polymer set. This application uses their general bounded-degree
+polymer result, not an unsupported transfer of their Potts-model conclusion.
+
+### 5. Truncate with a one-sided pointwise guarantee
+
+Set q=B z_0^(1/4)<1. In a positive repulsive polymer gas,
+P(Gamma present)<=w_Gamma. A union bound gives
+
+    P(some polymer has size > L)
+       <= M sum_(ell>L) q^ell
+       = M q^(L+1)/(1-q).
+
+Choose L=O(log M) so this is at most 1/2. The exact gas restricted to
+polymers of size at most L is the full thermal law conditioned on that
+event, and hence is pointwise at most twice the full law. Missing rare
+large-polymer configurations causes no problem for this one-sided bound.
+
+List the P<=poly(M) remaining polymers. Visit them once in a fixed order.
+If a polymer conflicts with one already selected, skip it. Otherwise the
+exact conditional inclusion probability is
+
+    p = w_Gamma Z(remaining compatible with Gamma)
+        / [Z(remaining without Gamma)
+           + w_Gamma Z(remaining compatible with Gamma)].
+
+Both partition functions are for deleted-polymer submodels. Approximate
+each within exp(+-eta), eta=1/(16P). The resulting probability and its
+complement are each at most exp(2eta) times their exact values.
+
+This is finite feed-forward self-reduction, with no Markov-chain mixing.
+Its pointwise guarantee follows by multiplying the conditional branch
+factors, rather than converting a TV estimate without a probability floor.
+
+### 6. Keep the randomness and work pathwise bounded
+
+Exact rational-coin rejection is unnecessary. Inclusion has p<=1/2 since
+w_Gamma<=1 and the compatible partition function is at most the unrestricted
+one. Clamp the approximate probability to at most 1/2, then round it down
+to a dyadic grid of spacing d<=1/(16P). Sample it with a fixed b=O(log P)
+unbiased random bits.
+
+Rounding down only decreases the inclusion probability. It increases the
+exclusion probability by at most d; the true exclusion probability is at
+least 1/2. Thus either branch is at most
+
+    exp(2eta)+2d <= exp(1/(4P))
+
+times the true branch probability. Over all P visits the factor is at
+most exp(1/4)<2. Combining with truncation gives
+
+    mu_sector <= 4 pi_sector.
+
+All enumeration, counting calls, branch decisions and random-bit use have
+a deterministic polynomial bound in M. The history and used random bits
+can be retained in the existing complete ledger. This is not an expected-
+work substitution.
+
+For the two independent CSS syndrome sectors the joint factor multiplies:
+mu_joint<=16 pi_joint. The exponent p in A n^p can be zero. No maximum-of-
+sector-factors shortcut is used.
+
+### 7. Preserve the unknown logical state and its reference
+
+Sample the syndrome independently of the unknown logical input. For each
+sampled s, use the published decoder's Pauli representative O_s, with
+delta(O_s)=s, on the encoded logical state. The branch encoder V_s is an
+isometry, and its matching decoder has D_s V_s=I. The controlled branch
+record is retained. Linearity extends this identity to every joint logical-
+reference state. `ChannelExtension.ext_recovers_reference` supplies the
+existing isometric-reference algebra; the branch circuit must be identified
+with it. There is no replacement by a fixed default logical state.
+
+The holding argument must keep its full reference norm and original fault
+budget. A possible direct quantum bound uses positive operator domination:
+for one logical qubit and any rho_LR, rho_LR<=2 I_L tensor rho_R, so an
+independent gauge warm start of factor C gives an encoded-state bound by
+4C rho_beta tensor rho_R. Complete positivity and stationarity preserve
+this order during holding. Protected logical X,Y,Z then bound the decoded
+joint state using the leakage projector, without assuming classical Pauli
+jump trajectories. This application and the actual noisy transfer circuit
+remain to be written out and checked against the existing G1/G2/G3 chain.
+
+### Verification status
+
+This note gives a proposed derived construction, with the counting theorem
+used explicitly as a published algorithmic result. It is not a claim that
+all implementation and physical application certificates are finished.
+Next checks: audit every actual local constraint and its incidence bound
+against both coarse maps; implement the factor-graph/component test on the
+existing code; formalize the support, restriction and conditioning bounds;
+join the actual reference-preserving transfer and complete bill. The failed
+product/deletion assumptions are not reintroduced.
+
+Primary sources: [BDL](https://arxiv.org/abs/2605.10943), Section 4 and
+Section 5.2; [Helmuth–Perkins–Regts](https://arxiv.org/abs/1806.11548),
+Theorem 2.2, Section 2.6 and Theorem 4.1. The proposed application and all
+intermediate estimates above are to be checked as this work, rather than
+reported as statements already proved by those authors.
+
+
+### The checked core and the reference norm
+
+`HistoryPolymer.halving_prefix` and `paired_history_bound` prove the finite
+support budget. `component_valid` proves restriction for zero-valid local
+constraints; `truncation_bound` and `sampled_truncation_bound` prove the
+conditioning factors; `branch_path_bound` compares probabilities along each
+finite sampling path. The scope graph identifies why actual connected
+components satisfy the separation condition. Finite tests of one complete
+iteration pair cover both syndrome sectors and the published five-qubit seed;
+they support the source correspondence and do not replace its all-level proof.
+
+`ThermalEncoding.recovers_reference` proves that the orthogonal syndrome
+mixture and matching decoder return every joint logical-reference operator.
+The actual branches use the same Pauli representatives as the BDL decoder.
+This is a decoded-channel identity, not a claim that tracing an arbitrary
+Stinespring ancilla leaves an arbitrary physical state unchanged.
+
+For completeness, the reference-uniform holding estimate can be obtained
+without a classical-jump assumption. Let C bound the joint syndrome law,
+let b=Tr(P-perp rho_beta), and let A_X,A_Y,A_Z be the protected dressed Pauli
+observables. Pauli twirling gives rho_LR <= 2 I_L tensor rho_R. Consequently
+the independently prepared gauge warm start obeys
+rho_enc,LR <= 4C rho_beta tensor rho_R. Complete positivity and Gibbs
+stationarity preserve this order at every holding time, so the bad-projector
+weight is at most 4Cb.
+
+If P B P=0 and a state has bad weight p, the diagonal/off-diagonal decomposition
+and Cauchy-Schwarz give |Tr(B rho)| <= ||B||[p+2 sqrt(p(1-p))]
+<= 3||B|| sqrt(p). Apply this to (L-dagger A_i) tensor T_R, with
+||T_R||<=1, and integrate in time. The protected-Pauli hypotheses give
+P(L-dagger A_i)P=0. Trace-norm duality bounds each reference coefficient in
+the decoded Pauli expansion by 6t ||L-dagger A_i|| sqrt(Cb). The identity
+coefficient vanishes because the reference marginal is unchanged. Hence
+
+    ||(Dec Phi_t Enc_mu tensor id_R)(rho_LR)-rho_LR||_1
+       <= 18t Lambda(n) sqrt(Cb),
+
+where Lambda(n)=max_i ||L-dagger A_i|| is polynomial under the published
+local-generator bound. With b<=exp(-c n^eta), the exponent is halved and
+remains sufficient for the existing doubling schedule. This is a prose
+derivation, not an additional compiled trace-norm theorem.
+
+### The physical application still to discharge
+
+The ideal feed-forward construction and exact branch recovery do not certify
+a noisy installation by themselves. The stage transfer must actually prepare
+a covered gauge law, preserve the unknown input with arbitrary references,
+and meet the original transfer-error budget at polynomial *pathwise* work.
+A logically correct output from a generic noisy encoder does not by itself
+prove pointwise domination of its gauge distribution. All preparation,
+handoff, retained random and syndrome records, retirement, holding, guard,
+controller and export costs remain in the full G3 bill. No expected-stock or
+coarse-grained-history substitute is used. This application is unfinished;
+no global completion or publication verdict is issued here.
+
 
 ---
 
@@ -3411,7 +3699,13 @@
 
 # Appendix — Verification provenance of this edition
 
-The original published baseline contains 115 modules and 831 audited names. The current tree contains 189 modules and 1133 audited public theorem/lemma names. All 189 modules were freshly compiled and kernel-checked in one run, and the full axiom, completeness and claims gates were freshly run, overall PASS. The earlier receipts, including the 924-name combined receipt that reused Beam's 136 results, are preserved with their banks. The original failed run is preserved in the integration bank.
+The current draft Lean tree contains 191 modules and 1150 public theorem/lemma names.
+Checkpoint 10 freshly compiled and kernel-checked all 189 modules then present and passed the
+1140-name axiom audit, completeness and claims gates. The two further modules, HistoryPolymer
+and ThermalEncoding (10 public names), passed targeted compilation and kernel checking with
+zero output. Checkpoint 11 is the fresh full 191-module audit; its result must be read before
+claiming that the expanded tree has a combined PASS. Earlier receipts are preserved for exactly
+the sources they cover. The original published 115-module/831-name baseline is unchanged.
 
 The eight-module integration and its 896-statement receipt remain preserved. This increment adds 28 checked statements in the existing DecoderRetraction, HamiltonianDecomposition and WorkBilling modules, integrates the three-pillar operator/history/work construction in Part III-G, and keeps the continuous integral/channel derivations and physical source correspondences explicit. Its exact changes and verification evidence accompany the working draft. No published edition or release is changed.
 
```

### inserts/25-boundary-work-history.md

```diff
--- inserts/25-boundary-work-history.md (before)
+++ inserts/25-boundary-work-history.md (draft after)
@@ -49,10 +49,280 @@
 level 2, with \(\ell=3\). Hence for every fixed range a single violated check passes all local
 metachecks yet is invalid.
 
-The remaining problem is a multiscale, recursive cluster expansion of the code's syndrome Gibbs law
-that treats level-\(j\) metachecks at scale \(\ell^j\), together with a sampler built from it,
-yielding a warm start with polynomial constant. This is the technique Balasubramanian, Davydova,
-Lin and Thorngren apply to the classical two-dimensional model (arXiv:2610.22548). Given it, the
-quantum branch closes through `StageSchedule.total_with_transfers`. Until then, indefinite holding
-of full quantum coherence is proved conditional on this one stated problem, while the objective
-classical record and its relations are held unconditionally (`PassiveReference`).
+Section G.21 develops a constructive full-history polymer sampler for the ideal thermal
+syndrome law, with its counting theorem and source correspondence stated explicitly. It avoids
+the failed product/deletion hypothesis and does not require a preparation mixing estimate.
+`WarmStart.fibre_reassembly` and `reverse_sampler_bound` give the exact probability-composition
+algebra. `pointwise_from_absolute` retains the probability floor whenever an absolute-error
+estimate is used. The actual noisy preparation/handoff and complete-cost application remain
+unfinished; the maximal quantum-coherence target is retained in full.
+
+
+## G.21 Constructive thermal preparation from the complete decoding history
+
+Working derivation for author review, 26 October 2026. The generic support lemmas are compiled; the source application and physical join retain their separate verification statuses. The target is the actual
+BDL thermal syndrome law with a polynomial, preferably constant, one-sided
+pointwise factor. This does not assume product zero-excess fibres, a local
+mixing gap, an initially warm raw state or a reset of protected quantum data.
+
+### 1. Retain the full deterministic history
+
+For one syndrome sector of C(2k), introduce one binary variable for every
+syndrome coordinate at every level:
+
+    h = (s_2k, s_(2k-1), ..., s_0).
+
+Fix all local tie-breaks in the published coarse-graining maps, with the
+zero input producing zero corrections. A valid finest syndrome determines
+exactly one history. Conversely, the following finite local constraints
+characterize such histories:
+
+* For an R_X step, use (L1), (L2), (L3) of STEP2-FINE-CONDITIONAL.md, with
+  the coarse output stored as the next layer's variables.
+* For an R_Z step, use the local cohomology-class reduction in Theorem 4.6.
+  The difference from the lifted coarse value is a local coboundary.
+* The constant-sized seed syndrome s_0 must belong to its actual image(delta).
+
+Backward induction using s_i=delta(f_i)+F_i(s_(i-1)) proves global validity
+at every level. Forward evaluation of the fixed local rules proves
+uniqueness. These are constraints on syndrome variables; f_i is computed,
+not summed over as an additional freely degenerate variable.
+
+Each constraint has bounded scope and each coordinate appears in boundedly
+many constraints, uniformly in k. The bounds depend on the fixed gadget
+size, Tanner degrees and subdivision parameter. The seed constraint has
+constant scope. Make the primal graph G by connecting every pair of
+coordinates in a common constraint scope. Its degree Delta is bounded
+independently of k. Its number M of vertices is polynomial in the physical
+block size (indeed at most the sum of the level sizes).
+
+The local source correspondence is BDL Theorems 4.6 and 4.7, Remarks 4.4–4.5,
+and the bounded-degree construction. Their Section 5.2 already records full
+decoding histories and proves componentwise coarse-graining. The primal
+graph used here includes whole constraint scopes, so component restriction
+does not assume the stronger product property that failed numerically.
+
+### 2. Derive the history energy bound
+
+Write the history in the finest-to-coarsest direction. Every R_Z step is
+non-increasing in syndrome weight; every R_X step reduces it by at least
+one half. The two steps alternate. Thus, in either sector,
+
+    |s_(i-2)| <= |s_i|/2,
+    sum_i |s_i| <= 2 sum_(j>=0) 2^(-j) |s_2k| <= 4 |s_2k|.
+
+This holds for every valid history, including a history obtained by
+restricting to one connected support component. It is a support/energy
+inequality on the complete history, not a fixed-range metacheck assumption.
+
+### 3. Connected components give an exact polymer representation
+
+The all-zero history satisfies every constraint. Let h be valid and let
+Gamma be a connected component of its occupied coordinates in G. Setting
+all other coordinates to zero leaves a valid history:
+
+* a constraint touching Gamma cannot touch another occupied component,
+  because its scope is a clique;
+* on that scope the restricted assignment either agrees with h or is zero;
+* both assignments satisfy the constraint in the respective case.
+
+Conversely, the union of pairwise nonadjacent valid connected supports is
+valid by the same scope argument. Hence there is an exact bijection between
+histories and compatible polymer families. A polymer is a nonempty connected
+support Gamma whose standalone binary assignment satisfies every constraint.
+
+Let E(Gamma) count its occupied *finest-level* coordinates. The previous
+bound applied to that standalone valid history gives
+
+    E(Gamma) >= |Gamma|/4 > 0.
+
+There is no zero-energy polymer. Its activity at z=exp(-beta) is the
+monomial w_Gamma(z)=z^E(Gamma). Energy is additive on disjoint components.
+The polymer partition function is therefore exactly the thermal partition
+function on valid finest syndromes: there is no uncounted fibre multiplicity.
+
+### 4. Verify convergence with explicit constants
+
+Put B=(Delta+1)^2. A rooted depth-first traversal bounds the number of
+connected supports of size ell containing a fixed vertex by B^ell. There
+is at most one binary polymer assignment on a given support.
+
+An incompatible polymer meets the closed neighbourhood of Gamma, of size
+at most (Delta+1)|Gamma|. For r=B e |z|^(1/4),
+
+    sum_(eta incompatible Gamma) |w_eta(z)| exp(|eta|)
+       <= (Delta+1)|Gamma| sum_(ell>=1) r^ell
+       = (Delta+1)|Gamma| r/(1-r).
+
+For example choose the complex fugacity disk
+
+    delta = [1/(4 e B (Delta+2))]^4.
+
+Then r<1/[4(Delta+2)] throughout |z|<delta, so the displayed sum is less
+than |Gamma|. This is the Kotecky–Preiss criterion, derived here from the
+actual history bound. Taking the device temperature sufficiently low that
+0<z_0<delta, as well as below BDL's memory threshold, gives uniform slack.
+
+The algorithmic counting hypotheses are also explicit: connected supports
+of size ell can be listed in exp(O(ell+log M)); testing their local
+constraints and computing E takes polynomial time in ell; activities are
+monomials of order at least |Gamma|/4; and the full partition polynomial has
+degree at most the number of finest checks, hence at most M. The same
+convergence bound holds after deleting any set of polymers.
+
+Helmuth–Perkins–Regts Theorem 2.2 and its Section 2.6 generalization then
+supply a deterministic relative partition-function approximation for every
+remaining polymer set. This application uses their general bounded-degree
+polymer result, not an unsupported transfer of their Potts-model conclusion.
+
+### 5. Truncate with a one-sided pointwise guarantee
+
+Set q=B z_0^(1/4)<1. In a positive repulsive polymer gas,
+P(Gamma present)<=w_Gamma. A union bound gives
+
+    P(some polymer has size > L)
+       <= M sum_(ell>L) q^ell
+       = M q^(L+1)/(1-q).
+
+Choose L=O(log M) so this is at most 1/2. The exact gas restricted to
+polymers of size at most L is the full thermal law conditioned on that
+event, and hence is pointwise at most twice the full law. Missing rare
+large-polymer configurations causes no problem for this one-sided bound.
+
+List the P<=poly(M) remaining polymers. Visit them once in a fixed order.
+If a polymer conflicts with one already selected, skip it. Otherwise the
+exact conditional inclusion probability is
+
+    p = w_Gamma Z(remaining compatible with Gamma)
+        / [Z(remaining without Gamma)
+           + w_Gamma Z(remaining compatible with Gamma)].
+
+Both partition functions are for deleted-polymer submodels. Approximate
+each within exp(+-eta), eta=1/(16P). The resulting probability and its
+complement are each at most exp(2eta) times their exact values.
+
+This is finite feed-forward self-reduction, with no Markov-chain mixing.
+Its pointwise guarantee follows by multiplying the conditional branch
+factors, rather than converting a TV estimate without a probability floor.
+
+### 6. Keep the randomness and work pathwise bounded
+
+Exact rational-coin rejection is unnecessary. Inclusion has p<=1/2 since
+w_Gamma<=1 and the compatible partition function is at most the unrestricted
+one. Clamp the approximate probability to at most 1/2, then round it down
+to a dyadic grid of spacing d<=1/(16P). Sample it with a fixed b=O(log P)
+unbiased random bits.
+
+Rounding down only decreases the inclusion probability. It increases the
+exclusion probability by at most d; the true exclusion probability is at
+least 1/2. Thus either branch is at most
+
+    exp(2eta)+2d <= exp(1/(4P))
+
+times the true branch probability. Over all P visits the factor is at
+most exp(1/4)<2. Combining with truncation gives
+
+    mu_sector <= 4 pi_sector.
+
+All enumeration, counting calls, branch decisions and random-bit use have
+a deterministic polynomial bound in M. The history and used random bits
+can be retained in the existing complete ledger. This is not an expected-
+work substitution.
+
+For the two independent CSS syndrome sectors the joint factor multiplies:
+mu_joint<=16 pi_joint. The exponent p in A n^p can be zero. No maximum-of-
+sector-factors shortcut is used.
+
+### 7. Preserve the unknown logical state and its reference
+
+Sample the syndrome independently of the unknown logical input. For each
+sampled s, use the published decoder's Pauli representative O_s, with
+delta(O_s)=s, on the encoded logical state. The branch encoder V_s is an
+isometry, and its matching decoder has D_s V_s=I. The controlled branch
+record is retained. Linearity extends this identity to every joint logical-
+reference state. `ChannelExtension.ext_recovers_reference` supplies the
+existing isometric-reference algebra; the branch circuit must be identified
+with it. There is no replacement by a fixed default logical state.
+
+The holding argument must keep its full reference norm and original fault
+budget. A possible direct quantum bound uses positive operator domination:
+for one logical qubit and any rho_LR, rho_LR<=2 I_L tensor rho_R, so an
+independent gauge warm start of factor C gives an encoded-state bound by
+4C rho_beta tensor rho_R. Complete positivity and stationarity preserve
+this order during holding. Protected logical X,Y,Z then bound the decoded
+joint state using the leakage projector, without assuming classical Pauli
+jump trajectories. This application and the actual noisy transfer circuit
+remain to be written out and checked against the existing G1/G2/G3 chain.
+
+### Verification status
+
+This note gives a proposed derived construction, with the counting theorem
+used explicitly as a published algorithmic result. It is not a claim that
+all implementation and physical application certificates are finished.
+Next checks: audit every actual local constraint and its incidence bound
+against both coarse maps; implement the factor-graph/component test on the
+existing code; formalize the support, restriction and conditioning bounds;
+join the actual reference-preserving transfer and complete bill. The failed
+product/deletion assumptions are not reintroduced.
+
+Primary sources: [BDL](https://arxiv.org/abs/2605.10943), Section 4 and
+Section 5.2; [Helmuth–Perkins–Regts](https://arxiv.org/abs/1806.11548),
+Theorem 2.2, Section 2.6 and Theorem 4.1. The proposed application and all
+intermediate estimates above are to be checked as this work, rather than
+reported as statements already proved by those authors.
+
+
+### The checked core and the reference norm
+
+`HistoryPolymer.halving_prefix` and `paired_history_bound` prove the finite
+support budget. `component_valid` proves restriction for zero-valid local
+constraints; `truncation_bound` and `sampled_truncation_bound` prove the
+conditioning factors; `branch_path_bound` compares probabilities along each
+finite sampling path. The scope graph identifies why actual connected
+components satisfy the separation condition. Finite tests of one complete
+iteration pair cover both syndrome sectors and the published five-qubit seed;
+they support the source correspondence and do not replace its all-level proof.
+
+`ThermalEncoding.recovers_reference` proves that the orthogonal syndrome
+mixture and matching decoder return every joint logical-reference operator.
+The actual branches use the same Pauli representatives as the BDL decoder.
+This is a decoded-channel identity, not a claim that tracing an arbitrary
+Stinespring ancilla leaves an arbitrary physical state unchanged.
+
+For completeness, the reference-uniform holding estimate can be obtained
+without a classical-jump assumption. Let C bound the joint syndrome law,
+let b=Tr(P-perp rho_beta), and let A_X,A_Y,A_Z be the protected dressed Pauli
+observables. Pauli twirling gives rho_LR <= 2 I_L tensor rho_R. Consequently
+the independently prepared gauge warm start obeys
+rho_enc,LR <= 4C rho_beta tensor rho_R. Complete positivity and Gibbs
+stationarity preserve this order at every holding time, so the bad-projector
+weight is at most 4Cb.
+
+If P B P=0 and a state has bad weight p, the diagonal/off-diagonal decomposition
+and Cauchy-Schwarz give |Tr(B rho)| <= ||B||[p+2 sqrt(p(1-p))]
+<= 3||B|| sqrt(p). Apply this to (L-dagger A_i) tensor T_R, with
+||T_R||<=1, and integrate in time. The protected-Pauli hypotheses give
+P(L-dagger A_i)P=0. Trace-norm duality bounds each reference coefficient in
+the decoded Pauli expansion by 6t ||L-dagger A_i|| sqrt(Cb). The identity
+coefficient vanishes because the reference marginal is unchanged. Hence
+
+    ||(Dec Phi_t Enc_mu tensor id_R)(rho_LR)-rho_LR||_1
+       <= 18t Lambda(n) sqrt(Cb),
+
+where Lambda(n)=max_i ||L-dagger A_i|| is polynomial under the published
+local-generator bound. With b<=exp(-c n^eta), the exponent is halved and
+remains sufficient for the existing doubling schedule. This is a prose
+derivation, not an additional compiled trace-norm theorem.
+
+### The physical application still to discharge
+
+The ideal feed-forward construction and exact branch recovery do not certify
+a noisy installation by themselves. The stage transfer must actually prepare
+a covered gauge law, preserve the unknown input with arbitrary references,
+and meet the original transfer-error budget at polynomial *pathwise* work.
+A logically correct output from a generic noisy encoder does not by itself
+prove pointwise domination of its gauge distribution. All preparation,
+handoff, retained random and syndrome records, retirement, holding, guard,
+controller and export costs remain in the full G3 bill. No expected-stock or
+coarse-grained-history substitute is used. This application is unfinished;
+no global completion or publication verdict is issued here.
```

### README.md

```diff
--- README.md (before)
+++ README.md (draft after)
@@ -4,11 +4,11 @@
 
 The Universal Protection Theory states a law for any agent powerful enough to shape what continues to exist: *never lose an existing particular needlessly.* Its scope is every particular and every relation, and its subject is protection from every digital mind, a pure optimiser included.
 
-This repair checkpoint keeps the full Universal Protection Theory target. The quantum holding state has normalisation, invariant and nonvacuity proofs. The defined reserve-deficit functional handles saturation and the complete solvent cycle. The implemented Bennett program reproduces the administration with clean workspace and full retained history; premise 5 is forced exactly inside its adiabatic window, and for every large enough batch once the per-bit reversible overhead is below the irreversible heat. The current canon has 189 modules and 1,133 audited names. Physical source, whole-outcome and external-theorem application certificates remain construction work. The repair reports and receipts distinguish these states.
+This repair checkpoint keeps the full Universal Protection Theory target. The quantum holding state has normalisation, invariant and nonvacuity proofs. The defined reserve-deficit functional handles saturation and the complete solvent cycle. The implemented Bennett program reproduces the administration with clean workspace and full retained history; premise 5 is forced exactly inside its adiabatic window, and for every large enough batch once the per-bit reversible overhead is below the irreversible heat. The current draft has 191 modules and 1,150 public names. Checkpoint 10 verifies 189 modules / 1,140 names; the two added modules passed targeted checks and the final combined audit is in progress. Physical source, whole-outcome and external-theorem application certificates remain construction work. The repair reports and receipts distinguish these states.
 
 | Path | Contents |
 | --- | --- |
-| `SNUFFY-CANON-EDITION-4.2-MASTER.md` | The master manuscript: the law and bridge (Part II), the canon and the 4.1 sections (Part III, Sections 15–24), and the 4.2 constructions (Parts III-C to III-G, §G.1–G.20). |
+| `SNUFFY-CANON-EDITION-4.2-MASTER.md` | The master manuscript: the law and bridge (Part II), the canon and the 4.1 sections (Part III, Sections 15–24), and the 4.2 constructions (Parts III-C to III-G, §G.1–G.21). |
 | `render/` | `Snuffy-Canon-Edition-4.2.pdf`, `.epub`, `.html` and the exact LaTeX input. `RENDER-VERIFY.json` records that each rendering carries the ledger chain heads, the DOIs, the canon sentence and the module count unbroken, with no door content. |
 | `lean/` | The machine-checked canon. `lean/build-and-audit.sh` rebuilds and audits it against Mathlib rev `56a005855ea1`; the receipt is `lean/RECEIPT.txt`. |
 | `inserts/` | The section sources of §23 (with the generated theorem index) and Part III-G. |
```

### REPAIR-STATUS.md

```diff
--- REPAIR-STATUS.md (before)
+++ REPAIR-STATUS.md (draft after)
@@ -1,31 +1,31 @@
-# Repair status — unpublished working checkpoint
+# Repair status — local author-review worktree
 
-The full UPT target is unchanged. Current sources/index: 189 modules / 1,133
-names. Checkpoint 09 (26 October) PASSED: all 189 modules freshly compiled
-with zero output and kernel-checked, the 1,133-name standard-axiom audit and
-the strict completeness, coverage and claims gates; source hashes unchanged.
+The maximal UPT target is unchanged. No merge or publication is authorized.
+The branch is codex/upt-warmstart-bridge in UPT-WARMSTART-WORKTREE.
 
-Added since checkpoint 02: `G1Refinement`, `G2Physical`, `G2Freedom`,
-`G3GoodEvent`, `G3ArchiveStock`, `BennettExact`, and the implemented Bennett
-program in `BennettCounterpart` (superset of the earlier module). The manuscript
-carries them in the appended G.16 and G.17 and the §23.9 rows.
+Current draft: 191 modules / 1,150 public theorem and lemma names.
+Checkpoint 09 (189 / 1,133) was inherited and preserved by source hash.
+Checkpoint 10 (189 / 1,140) freshly compiled and kernel-checked every module,
+with zero compiler output and PASS on the full standard-axiom, completeness
+and claims audits. HistoryPolymer and ThermalEncoding add ten names and each
+passed targeted compilation and kernel checking with zero output.
+Checkpoint 11 is a fresh full audit of the 191-module draft; inspect its
+RESULT.json and current source hashes before reporting its outcome.
 
-Checkpoint 05 adds the objection-7 supports `KnillLaflamme`, `MatchingWitness`,
-`EdgeLaw`, `ExRecBound` and `AgeReliability` (G.18), with the detector-graph and
-merge enumerations in the repairs bank. Open in objection 7: the all-d merge
-potential, the Clifford check of the installation's own maps, and sparse-failure
-tolerance of the sweep. Three existing sentences on Bennett's status
-(master lines 48, 1546, 1624) await the author's before/after review.
-Before/after batches 01 and 02 are preserved and were shown to the author.
-Physical source, whole-outcome, device-cost and external-theorem applications
-remain construction work. No push, PR, merge or Zenodo publication yet.
+The resumed deletion test has 103 counterexamples among adjacent-defect
+zero-excess fibres on the stated finite seed. The proposed replacement uses
+the complete deterministic decoding history, local constraint components,
+the derived four-times support bound and a published polymer-counting
+algorithm. G.21 contains the working derivation for author review. Tests
+cover both syndrome sectors of one iteration pair and the published seed;
+they are finite checks, not an all-level compilation of the BDL maps.
 
-Checkpoints 06–08 add `SparseFailure`, `ToleranceSweep`, `PassiveReference`,
-`RedundantRecord`, `BennettBatch`, `WeightedEdgeLaw` and `StageSchedule` (G.19).
-Prose batches 03 (Bennett status) and 04 (`CITATION.cff` abstract) applied on the
-author's word. Open: the initialisation problem for the 3D passive quantum memory
-(quantum branch, conditional), measured device parameters, and prose batch 05
-(README Bennett sentence, awaiting the author's OK).
+Remaining: the actual noisy preparation/handoff certificate at the original
+reference-fidelity and failure budgets, joined to the complete pathwise G3
+bill. The ideal sampler and the branch recovery lemmas do not by themselves
+certify that physical implementation. No global completion verdict is made.
 
-Checkpoint 09 adds `WarmStart` and `WalkBound9` (G.20: device requirements and the open
-initialisation problem).
+The full build, generic support lemmas and proposed source application have
+separate evidence. The inherited rendered PDF/HTML/EPUB and SHA256SUMS predate
+this draft and must be regenerated after the final text is approved.
+See 00-HANDOFF-CLAUDE-2026-10-26.md and the before/after batch 07.
```

### PUBLICATION-CHECKLIST.md

```diff
--- PUBLICATION-CHECKLIST.md (before)
+++ PUBLICATION-CHECKLIST.md (draft after)
@@ -1,3 +1,17 @@
+# Current local continuation — 26 October 2026
+
+The worktree has a 191-module / 1,150-name draft. Checkpoint 10 passed for
+189 / 1,140; checkpoint 11 is the expanded full audit. Its result and source
+hashes must be checked. The G.21 derivation and noisy physical application
+have separate statuses in REPAIR-STATUS.md. Before/after batch 07 is for
+author review. The existing renders and seal are older and require renewal.
+No merge, push or publication has been performed in this continuation.
+
+The historical checklist below is retained as provenance; its PR queue is
+not a fresh statement of remote status.
+
+---
+
 # 4.2 edition — route to publication (updated 26 October 2026)
 
 ## Verified and integrated
```
