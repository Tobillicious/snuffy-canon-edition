# Before/after batch 08 — local author review

Checkpoint 11 was already PASS (191 / 1,150). Fresh checkpoint 12 is PASS for
all 192 modules / 1,158 names, with current source hashes matching. TransferRate
adds eight complete-cost statements. No other canonical Lean source changed.

This batch records the ideal sampler source audit, the direct reference-norm
and initial-sparsity derivations, the complete pathwise ledger, and corrected
verification counts. The actual noisy holding estimate remains open. The
new physical proposals are preserved as candidates with a hostile review;
no unsupported spectral-gap or occupation theorem is added to Lean.

Full source and physical dispositions:
- G21-SOURCE-APPLICATION-AUDIT.md
- COMPLETE-TRANSFER-COST-JOIN.md
- G3-HOSTILE-REVIEW-2026-10-26.md
- PATAI-NEUTRAL-EXCURSION-CERTIFICATE-2026-10-26.md

Renders and SHA256SUMS remain older. Nothing is merged, pushed or published.

## SNUFFY-CANON-EDITION-4.2-MASTER.md

```diff
--- before/SNUFFY-CANON-EDITION-4.2-MASTER.md
+++ after/SNUFFY-CANON-EDITION-4.2-MASTER.md
@@ -8,13 +8,13 @@
 
 The three joined supports retain their full targets: the full-domain physical certificate (G1), realisability of the whole continuation-and-freedom tuple (G2), and recovery success with a complete pathwise work certificate (G3). This repair checkpoint corrects the normalised quantum-state domain and the clipped-reserve contraction, and develops the actual Bennett implementation. The physical source, whole-outcome, device-cost and external-theorem application correspondences remain explicit construction work; the component theorems do not by themselves declare the maximal argument complete.
 
-The current draft Lean tree contains 191 modules and 1150 public theorem/lemma names.
-Checkpoint 10 freshly compiled and kernel-checked all 189 modules then present and passed the
-1140-name axiom audit, completeness and claims gates. The two further modules, HistoryPolymer
-and ThermalEncoding (10 public names), passed targeted compilation and kernel checking with
-zero output. Checkpoint 11 is the fresh full 191-module audit; its result must be read before
-claiming that the expanded tree has a combined PASS. Earlier receipts are preserved for exactly
-the sources they cover. The original published 115-module/831-name baseline is unchanged.
+The current Lean canon contains 192 modules and 1158 public theorem/lemma names.
+Checkpoint 12 freshly compiled and kernel-checked every module with zero output and passed
+the full 1158-name standard-axiom audit, strict completeness and claims gates. Its source hashes
+match the current tree. Checkpoint 11 was already complete for 191 modules / 1150 names;
+TransferRate adds the eight results in this checkpoint. Earlier receipts remain preserved for
+exactly their sources. The published 115-module/831-name baseline is unchanged. These receipts
+certify the named Lean results and their premises, not the unfinished physical holding application.
 
 **Structure.** Part I states the frame and premise stack. Part II supplies the law, the derived holding bridge and the retained instruments. Part III retains the five-chapter synthesis; Sections 15–24 develop the reasons, physical and compiled arguments. Part III-C records the three joined supports and their constructions. Part IV gives references and provenance. Theorem and proposition numbers follow the programme's proof register.
 
@@ -1460,13 +1460,13 @@
 
 ## Section 23 — The machine-checked canon
 
-*This section maps the edition's compiled results and their actual hypotheses. The current draft Lean tree contains 191 modules and 1150 public theorem/lemma names.
-Checkpoint 10 freshly compiled and kernel-checked all 189 modules then present and passed the
-1140-name axiom audit, completeness and claims gates. The two further modules, HistoryPolymer
-and ThermalEncoding (10 public names), passed targeted compilation and kernel checking with
-zero output. Checkpoint 11 is the fresh full 191-module audit; its result must be read before
-claiming that the expanded tree has a combined PASS. Earlier receipts are preserved for exactly
-the sources they cover. The original published 115-module/831-name baseline is unchanged. Section 23.9 distinguishes the interfaces, derived adapters and remaining physical applications.*
+*This section maps the edition's compiled results and their actual hypotheses. The current Lean canon contains 192 modules and 1158 public theorem/lemma names.
+Checkpoint 12 freshly compiled and kernel-checked every module with zero output and passed
+the full 1158-name standard-axiom audit, strict completeness and claims gates. Its source hashes
+match the current tree. Checkpoint 11 was already complete for 191 modules / 1150 names;
+TransferRate adds the eight results in this checkpoint. Earlier receipts remain preserved for
+exactly their sources. The published 115-module/831-name baseline is unchanged. These receipts
+certify the named Lean results and their premises, not the unfinished physical holding application. Section 23.9 distinguishes the interfaces, derived adapters and remaining physical applications.*
 
 *Evidence convention (unchanged from the edition header): a compiled theorem is cited by its name; a statement carried as a hypothesis of a compiled theorem is named as such; a prose derivation keeps its stated premises. A prose proof does not acquire a compiler certificate by association.*
 
@@ -1659,6 +1659,7 @@
 | `WalkBound9` | The length-9 walk bound c₉ = 763,504,745 ≤ 9.71⁹ gives an explicit threshold above 4.2×10⁻⁴ (G.20) |
 | `HistoryPolymer` | Deterministic history support budget, component restriction, truncation factors and finite sampling-path bounds (G.21) |
 | `ThermalEncoding` | Orthogonal syndrome-mixture recovery, including arbitrary reference correlations (G.21) |
+| `TransferRate` | Full retained-prefix size, complete failed-attempt invoices and the age-independent transfer/G3 work join (G.21) |
 
 The earlier `G1Certificate.universal_protection_held` has conclusion `True`; it is a placeholder and is not the protection theorem `Bridge.universal_protection_held`. The latter's full source certificate is constructed in G.10 (`G1Held.held_source_protection`). The exact integration history and dependency trace accompany this working edition.
 
@@ -1860,6 +1861,7 @@
 | `WalkBound9` | `walk_bound_9`, `threshold_9`, `threshold_9_value` |
 | `HistoryPolymer` | `halving_prefix`, `paired_history_bound`, `component_valid`, `truncation_bound`, `sampled_truncation_bound`, `branch_path_bound` |
 | `ThermalEncoding` | `branch_compression`, `recovers`, `kron_orthogonal`, `recovers_reference` |
+| `TransferRate` | `poly_le_two_pow`, `transfer_bill_le`, `transfer_bill_linear_in_age`, `retained_prefix_bound`, `attempt_stage_bound`, `polynomial_stage_bill`, `complete_attempt_bill`, `join_complete_bill` |
 <!-- END THEOREM INDEX -->
 
 ---
@@ -3322,16 +3324,16 @@
 code. If each stage's holding failure and each transfer's failure are at most
 \(\varepsilon/2^{j+2}\), the total failure is at most \(\varepsilon\) at every age
 (`StageSchedule.total_with_transfers`). A cost polynomial in each stage's code size sums to a
-polylogarithm of age (`stage_cost_le`). The transfer lands the qubit in the next code's codespace,
-so its hypothesis is that a codespace-initialised state obeys the same lifetime bound, or that its
-syndrome sector thermalises within polynomial time without logical error. This is the open
-initialisation problem those authors identify. The quantum branch is proved conditional on it,
-with the hypothesis stated explicitly. The classical record and its relations are held
-unconditionally by `PassiveReference`.
+polylogarithm of age (`stage_cost_le`). G.21 derives a feed-forward thermal-syndrome sampler
+and exact reference-preserving branch encoding for the ideal transfer. Its source application
+is audited in prose. What remains is holding the actual noisy transfer output at the original
+stage budget, including the initial decoded logical error. The construction does not require
+preparation mixing. The full quantum target is retained alongside the passive classical record
+construction; the classical record is not a replacement for it.
 
 **Remaining.**
 
-- The initialisation problem above.
+- The actual noisy preparation and holding certificate identified in G.21.
 - Measured device parameters: the fault rate \(p\), the coupling bound \(W\), the per-bit overhead
   \(\eta\), and the barrier materials and temperature.
 
@@ -3392,11 +3394,12 @@
 estimate is used. The actual noisy preparation/handoff and complete-cost application remain
 unfinished; the maximal quantum-coherence target is retained in full.
 
----
 
 ## G.21 Constructive thermal preparation from the complete decoding history
 
-Working derivation for author review, 26 October 2026. The generic support lemmas are compiled; the source application and physical join retain their separate verification statuses. The target is the actual
+Working derivation for author review, 26 October 2026. The generic support lemmas are compiled.
+The ideal sampler's source application is audited in prose; the actual noisy physical
+transfer and holding join remain unfinished. The target is the actual
 BDL thermal syndrome law with a polynomial, preferably constant, one-sided
 pointwise factor. This does not assume product zero-excess fibres, a local
 mixing gap, an initially warm raw state or a reset of protected quantum data.
@@ -3430,7 +3433,12 @@
 constant scope. Make the primal graph G by connecting every pair of
 coordinates in a common constraint scope. Its degree Delta is bounded
 independently of k. Its number M of vertices is polynomial in the physical
-block size (indeed at most the sum of the level sizes).
+block size (indeed at most the sum of the level sizes). Let S bound each scope
+and I the number of scopes reading one coordinate. The fixed gadget and
+Tanner incidences give constants S and I independent of the code level. An
+intermediate coordinate is read only by the two adjacent coarse steps, so
+I does not grow with hierarchy depth. Explicitly, Delta<=I(S-1). The finite
+tests' observed degrees are not substituted for this uniform symbolic bound.
 
 The local source correspondence is BDL Theorems 4.6 and 4.7, Remarks 4.4–4.5,
 and the bounded-degree construction. Their Section 5.2 already records full
@@ -3506,7 +3514,7 @@
 degree at most the number of finest checks, hence at most M. The same
 convergence bound holds after deleting any set of polymers.
 
-Helmuth–Perkins–Regts Theorem 2.2 and its Section 2.6 generalization then
+Helmuth–Perkins–Regts Theorem 2.2 and Lemma 2.8 in Section 2.6 then
 supply a deterministic relative partition-function approximation for every
 remaining polymer set. This application uses their general bounded-degree
 polymer result, not an unsupported transfer of their Potts-model conclusion.
@@ -3580,26 +3588,21 @@
 existing isometric-reference algebra; the branch circuit must be identified
 with it. There is no replacement by a fixed default logical state.
 
-The holding argument must keep its full reference norm and original fault
-budget. A possible direct quantum bound uses positive operator domination:
-for one logical qubit and any rho_LR, rho_LR<=2 I_L tensor rho_R, so an
-independent gauge warm start of factor C gives an encoded-state bound by
-4C rho_beta tensor rho_R. Complete positivity and stationarity preserve
-this order during holding. Protected logical X,Y,Z then bound the decoded
-joint state using the leakage projector, without assuming classical Pauli
-jump trajectories. This application and the actual noisy transfer circuit
-remain to be written out and checked against the existing G1/G2/G3 chain.
+The following reference-norm derivation keeps the arbitrary reference register
+and the original fault budget. Its ideal warm-start proof and its residual-noise
+application have distinct statuses.
 
 ### Verification status
 
-This note gives a proposed derived construction, with the counting theorem
-used explicitly as a published algorithmic result. It is not a claim that
-all implementation and physical application certificates are finished.
-Next checks: audit every actual local constraint and its incidence bound
-against both coarse maps; implement the factor-graph/component test on the
-existing code; formalize the support, restriction and conditioning bounds;
-join the actual reference-preserving transfer and complete bill. The failed
-product/deletion assumptions are not reintroduced.
+The ideal sampler's prose source audit checks the local cut-out, uniform
+scope incidence, exact history/partition bijection and all hypotheses of the
+published counting theorem, including the polymer-deleted submodels. The
+generic support, restriction and conditioning bounds are compiled. Finite
+source tests cover both syndrome sectors and the published seed; they do
+not replace the all-level source derivation. The external FPTAS is used as
+a published algorithm, not represented as a separately implemented and
+kernel-checked solver in this repository. The actual noisy physical transfer
+and holding certificate remains to be supplied.
 
 Primary sources: [BDL](https://arxiv.org/abs/2605.10943), Section 4 and
 Section 5.2; [Helmuth–Perkins–Regts](https://arxiv.org/abs/1806.11548),
@@ -3645,23 +3648,178 @@
     ||(Dec Phi_t Enc_mu tensor id_R)(rho_LR)-rho_LR||_1
        <= 18t Lambda(n) sqrt(Cb),
 
-where Lambda(n)=max_i ||L-dagger A_i|| is polynomial under the published
-local-generator bound. With b<=exp(-c n^eta), the exponent is halved and
-remains sufficient for the existing doubling schedule. This is a prose
-derivation, not an additional compiled trace-norm theorem.
+where Lambda(n)=max_i ||L-dagger A_i||. The elementary dissipator bound
+||D_V^dagger(A)||<=2||V||^2||A|| gives
+Lambda(n)<=2 sum_alpha gamma_alpha||V_alpha||^2, because the norm-one dressed
+Paulis commute with the stabilizer Hamiltonian. With O(n) local jump classes,
+uniformly bounded jump norms and rates, Lambda=O(n). This needs no claim
+that the dressing is locally supported or that only its boundary contributes.
+With b<=exp(-c n^eta), the exponent is halved and remains sufficient for the
+existing doubling schedule. This is a prose derivation, not an additional
+compiled trace-norm theorem.
+
+### The actual noisy state and its integrated bad weight
+
+Let omega_N=N(rho_beta) for the residual channel of the actual preparation,
+and b_N(s)=Tr(P_bad Phi_s(omega_N)). Identifying that channel with the
+physical circuit is part of its certificate. If N is the input-independent
+residual channel on the correctly implemented branch, complete positivity
+gives rho_actual,LR(s)<=4C Phi_s(omega_N) tensor rho_R. The preceding
+protected-Pauli argument, integrated without assuming stationarity of
+omega_N, then gives
+
+    e(T) <= e_0 + 18 Lambda sqrt(C) integral_0^T sqrt(b_N(s)) ds
+         <= e_0 + 18 Lambda sqrt(C T I_N(T)),
+    I_N(T) = integral_0^T b_N(s) ds.
+
+Here e_0 is the initial decoded reference-state error on that model. Add
+2 delta_fail for a separately bounded physical failure branch of weight
+delta_fail; its initial decoded error alone would not bound its future
+holding error. Thus an established I_N(T)<=K T exp(-c n^eta) would give a
+dynamical error at most 18 Lambda sqrt(CK) T exp(-c n^eta/2). With T=2^a,
+allocate e_0+2 delta_fail<=epsilon/2^(a+3) and the dynamical term the same
+amount. Their sum is precisely the original epsilon/2^(a+2) stage ceiling.
+The index a denotes archive age stages, separately from code levels i.
+Polynomial Lambda can be absorbed in a fixed fraction of the exponent,
+so the stage code size remains polynomial in a+log(1/epsilon).
+
+This is a conditional consequence of an actual integrated-weight bound,
+not a derivation of that physical estimate. A Duhamel argument cannot drop
+the microscopic jump rates or replace all coherent bad-block contributions
+by unit-rate bad probability. The displayed reference-norm proof retains
+the rate-dependent Lambda and the square root.
+
+More generally, let E_a be the actual CPTP preparation map, including noise
+and seed-dependent physical control, and put omega_a=E_a(I/2). Complete
+positivity and Pauli twirling directly give
+(E_a tensor id_R)(rho_LR)<=4 omega_a tensor rho_R. The same derivation yields
+e(T)<=e_0+18 Lambda sqrt(T I_a(T)), with
+I_a(T)=integral_0^T Tr[P_bad Phi_s(omega_a)]ds. Thus the physical certificate
+can concern the actual maximally-mixed-input preparation without first
+factoring it into an ideal encoder and an input-independent residual N.
+The integrated bad-weight estimate and initial logical error still require
+proof; this identity supplies their arbitrary-reference conversion.
+
+### Initial syndrome sparsity with the parity constraints retained
+
+There is a useful bound at time zero. For a binary linear space D and
+0<=z<=1, define Z_D(v)=sum_(x in D) z^|x+v|. Its character expansion is
+
+    Z_D(v)=(|D|/2^m) sum_(u in D^perp)
+              (-1)^(u dot v)(1+z)^(m-|u|)(1-z)^|u|.
+
+All coefficients are nonnegative, so Z_D(v)<=Z_D(0). For a required occupied
+coordinate set A in the valid syndrome space, shorten on A and puncture
+outside it. The occupied fibre has weight z^|A| Z_D(v), while the full
+partition contains the zero-on-A fibre of weight Z_D(0). Consequently
+
+    Pr_thermal[A subset defects] <= z^|A|.
+
+Thus global metachecks do not force an independence assumption. If the
+actual local-stochastic residual faults have parameter p, each affects at
+most w checks and each check has at most ell possible fault sources,
+choosing a fault source for every required check gives at most ell^|A|
+choices with at least ceil(|A|/w) distinct faults. Their check support is
+local-stochastic at q=min(1,ell p^(1/w)). If the thermal and fault sources
+are independent, their union, and hence the output syndrome, has occupation
+bound (z+q)^|A|. Without that independence the Cauchy–Schwarz union bound is
+(sqrt(z)+sqrt(q))^|A|. These are initial-law prose derivations, checked on
+finite linear spaces; no preservation under holding is inferred. Syndrome
+sparsity alone also does not bound an undetected logical Pauli error.
+
+### Complete pathwise stage cost
+
+The finite sampler produces at most polynomially many random, syndrome,
+coarse-history and controller bits per age stage, with bounded work on
+every branch. Retaining every record through stage a therefore leaves a
+polynomial-size prefix: if r_b<=(A+B b)^k, then
+
+    sum_(b=0..a) r_b <= [A+1+(B+1)a]^(k+1).
+
+`TransferRate.retained_prefix_bound` proves this bound. The whole prefix,
+including failed attempts, may be written into the next stage's classical
+journal. Its epsilon_R allowance is reserved inside the existing holding/
+transfer budget; it is not added on top of a fully spent epsilon budget.
+A fixed split of epsilon between quantum holding and journals only changes
+the size/barrier constants and keeps the original stage ceiling.
+A stage journal of m_a bits held for 2^a with attempt rate nu has
+total failure at most epsilon_R/2^(a+2) when its per-bit barrier satisfies
+beta B_a >= (2a+2)ln2+ln(nu max(1,m_a)/epsilon_R). For polynomial m_a this
+barrier is bounded by an affine function of a. Writing and routing the
+whole prefix remains polynomial under the stated passive classical device
+costs. These records do not replace the protected unknown quantum payload.
+
+Every attempt is charged through all nine `HandoffCharge` accounts:
+encoding, transfer, verification, routing, guard, reset, holding, controller
+and endpoints. The counts include sampler arithmetic and coins, the whole
+retained prefix, ancillas, retirement/export and all failed attempts.
+Parallel depth does not substitute for total operations. A conservative
+serial routing implementation has polynomial work on the finite stage
+device. Physical work bounds must cover the realised accounts.
+
+If the deterministic attempt cap is (u+v a)^r and every full attempt invoice
+is at most (A+B a)^k, `attempt_stage_bound` bounds the stage total by
+[A+u+(B+v)a]^(k+r). `complete_attempt_bill` and `polynomial_stage_bill` give
+an age-independent C_T with total transfer work<=C_T t when 2^J<=2t.
+`charged_attempt_accounting` still requires each reserve before work and
+charges failed attempts without committing their payload.
+
+Finally `join_complete_bill` combines this linear transfer term with the
+existing sweep and archive bills:
+
+    W_S+W_A+W_T <= (C_S+C_A+C_T)t^d,   t>=1, d>=1.
+
+The conclusion includes d=1. A rare-reset expectation is not substituted
+for the realised bill: if an admitted wave reset costs at most R k^(d-1),
+the worst-case sum is at most R t^d and is absorbed in the local wave
+coefficient. The complete fixed bootstrap charge is at most B_boot t^d
+for t>=1. Startup and endpoints already included in the wave or transfer
+invoice are not charged a second time. G3CompleteBill.cumulative_charge_bound
+and G3ArchiveStock.live_stock_bill retain the actual per-wave charge and
+live stock I0+c(s+1)^(d-1), rather than accumulated write flux. Together
+with TransferRate this gives the age-independent coefficient
+C_S+gamma(I0+c)+C_T+B_extra, where B_extra contains only additional fixed
+charges. Its dependence on the fixed payload capacity, dimension, hardware
+and error tolerance remains explicit. The full domain d>=1 and uniformity
+over logical input states with arbitrary references are retained.
+
+These are complete-invoice summation theorems; they do not supply the
+missing physical preparation/holding certificate. Landauer gives the
+entropy-export floor; the physical upper work invoice retains every
+holding, guard, controller, cooling, reset and history charge.
 
 ### The physical application still to discharge
 
 The ideal feed-forward construction and exact branch recovery do not certify
-a noisy installation by themselves. The stage transfer must actually prepare
-a covered gauge law, preserve the unknown input with arbitrary references,
-and meet the original transfer-error budget at polynomial *pathwise* work.
-A logically correct output from a generic noisy encoder does not by itself
-prove pointwise domination of its gauge distribution. All preparation,
-handoff, retained random and syndrome records, retirement, holding, guard,
-controller and export costs remain in the full G3 bill. No expected-stock or
-coarse-grained-history substitute is used. This application is unfinished;
-no global completion or publication verdict is issued here.
+a noisy installation by themselves. The actual transfer must preserve the
+unknown logical input with arbitrary references, bound its initial logical
+error and physical failure branches, and produce an output whose holding
+meets the original stage allowance at polynomial pathwise work.
+
+The remaining proposed contour route needs an actual generator/trajectory
+representation and a proved bound on its rare creation events after neutral
+and downhill motion has been summed. Bounded support of one jump does not
+confine successive jumps to that support. Nor does a bound B^|Gamma| rho^k
+converge merely from B rho<1 when the relation of |Gamma| to the rare-event
+count k has not been proved. The proposed confinement proof is inadequate:
+a valid neutral multi-defect junction in the existing finite BDL implementation
+crosses four single-defect hopping regions. The proposed gap-based
+replacement did not derive its uniform constants. A direct-history route
+can instead be used, but it must transport the initial joint syndrome
+occupation estimate under the actual Phi_s, or bound I_a(T) directly.
+Deterministic halving across decoder levels is not a probability factor
+one-half, and does not establish a time-uniform stochastic law. The static
+history polymers above do not by themselves give that nonequilibrium
+holding estimate. A killed local
+excursion process must retain its actual exit flux. A Feynman–Kac derivative
+at zero exactly represents occupation, but a resolvent bound at positive
+killing does not bound that derivative. In particular, killing only on a
+rare bad set cannot be assigned a constant gap by adding the trap rate.
+
+All preparation, handoff, retained records, retirement, holding, guard,
+controller and export charges remain in the G3 bill. No expected-stock,
+classical-payload or discarded-history substitute is used. The maximal
+protection target is unchanged; this physical application is unfinished.
 
 
 ---
@@ -3699,13 +3857,13 @@
 
 # Appendix — Verification provenance of this edition
 
-The current draft Lean tree contains 191 modules and 1150 public theorem/lemma names.
-Checkpoint 10 freshly compiled and kernel-checked all 189 modules then present and passed the
-1140-name axiom audit, completeness and claims gates. The two further modules, HistoryPolymer
-and ThermalEncoding (10 public names), passed targeted compilation and kernel checking with
-zero output. Checkpoint 11 is the fresh full 191-module audit; its result must be read before
-claiming that the expanded tree has a combined PASS. Earlier receipts are preserved for exactly
-the sources they cover. The original published 115-module/831-name baseline is unchanged.
+The current Lean canon contains 192 modules and 1158 public theorem/lemma names.
+Checkpoint 12 freshly compiled and kernel-checked every module with zero output and passed
+the full 1158-name standard-axiom audit, strict completeness and claims gates. Its source hashes
+match the current tree. Checkpoint 11 was already complete for 191 modules / 1150 names;
+TransferRate adds the eight results in this checkpoint. Earlier receipts remain preserved for
+exactly their sources. The published 115-module/831-name baseline is unchanged. These receipts
+certify the named Lean results and their premises, not the unfinished physical holding application.
 
 The eight-module integration and its 896-statement receipt remain preserved. This increment adds 28 checked statements in the existing DecoderRetraction, HamiltonianDecomposition and WorkBilling modules, integrates the three-pillar operator/history/work construction in Part III-G, and keeps the continuous integral/channel derivations and physical source correspondences explicit. Its exact changes and verification evidence accompany the working draft. No published edition or release is changed.
```

## inserts/25-boundary-work-history.md

```diff
--- before/inserts/25-boundary-work-history.md
+++ after/inserts/25-boundary-work-history.md
@@ -60,7 +60,9 @@
 
 ## G.21 Constructive thermal preparation from the complete decoding history
 
-Working derivation for author review, 26 October 2026. The generic support lemmas are compiled; the source application and physical join retain their separate verification statuses. The target is the actual
+Working derivation for author review, 26 October 2026. The generic support lemmas are compiled.
+The ideal sampler's source application is audited in prose; the actual noisy physical
+transfer and holding join remain unfinished. The target is the actual
 BDL thermal syndrome law with a polynomial, preferably constant, one-sided
 pointwise factor. This does not assume product zero-excess fibres, a local
 mixing gap, an initially warm raw state or a reset of protected quantum data.
@@ -94,7 +96,12 @@
 constant scope. Make the primal graph G by connecting every pair of
 coordinates in a common constraint scope. Its degree Delta is bounded
 independently of k. Its number M of vertices is polynomial in the physical
-block size (indeed at most the sum of the level sizes).
+block size (indeed at most the sum of the level sizes). Let S bound each scope
+and I the number of scopes reading one coordinate. The fixed gadget and
+Tanner incidences give constants S and I independent of the code level. An
+intermediate coordinate is read only by the two adjacent coarse steps, so
+I does not grow with hierarchy depth. Explicitly, Delta<=I(S-1). The finite
+tests' observed degrees are not substituted for this uniform symbolic bound.
 
 The local source correspondence is BDL Theorems 4.6 and 4.7, Remarks 4.4–4.5,
 and the bounded-degree construction. Their Section 5.2 already records full
@@ -170,7 +177,7 @@
 degree at most the number of finest checks, hence at most M. The same
 convergence bound holds after deleting any set of polymers.
 
-Helmuth–Perkins–Regts Theorem 2.2 and its Section 2.6 generalization then
+Helmuth–Perkins–Regts Theorem 2.2 and Lemma 2.8 in Section 2.6 then
 supply a deterministic relative partition-function approximation for every
 remaining polymer set. This application uses their general bounded-degree
 polymer result, not an unsupported transfer of their Potts-model conclusion.
@@ -244,26 +251,21 @@
 existing isometric-reference algebra; the branch circuit must be identified
 with it. There is no replacement by a fixed default logical state.
 
-The holding argument must keep its full reference norm and original fault
-budget. A possible direct quantum bound uses positive operator domination:
-for one logical qubit and any rho_LR, rho_LR<=2 I_L tensor rho_R, so an
-independent gauge warm start of factor C gives an encoded-state bound by
-4C rho_beta tensor rho_R. Complete positivity and stationarity preserve
-this order during holding. Protected logical X,Y,Z then bound the decoded
-joint state using the leakage projector, without assuming classical Pauli
-jump trajectories. This application and the actual noisy transfer circuit
-remain to be written out and checked against the existing G1/G2/G3 chain.
+The following reference-norm derivation keeps the arbitrary reference register
+and the original fault budget. Its ideal warm-start proof and its residual-noise
+application have distinct statuses.
 
 ### Verification status
 
-This note gives a proposed derived construction, with the counting theorem
-used explicitly as a published algorithmic result. It is not a claim that
-all implementation and physical application certificates are finished.
-Next checks: audit every actual local constraint and its incidence bound
-against both coarse maps; implement the factor-graph/component test on the
-existing code; formalize the support, restriction and conditioning bounds;
-join the actual reference-preserving transfer and complete bill. The failed
-product/deletion assumptions are not reintroduced.
+The ideal sampler's prose source audit checks the local cut-out, uniform
+scope incidence, exact history/partition bijection and all hypotheses of the
+published counting theorem, including the polymer-deleted submodels. The
+generic support, restriction and conditioning bounds are compiled. Finite
+source tests cover both syndrome sectors and the published seed; they do
+not replace the all-level source derivation. The external FPTAS is used as
+a published algorithm, not represented as a separately implemented and
+kernel-checked solver in this repository. The actual noisy physical transfer
+and holding certificate remains to be supplied.
 
 Primary sources: [BDL](https://arxiv.org/abs/2605.10943), Section 4 and
 Section 5.2; [Helmuth–Perkins–Regts](https://arxiv.org/abs/1806.11548),
@@ -309,20 +311,175 @@
     ||(Dec Phi_t Enc_mu tensor id_R)(rho_LR)-rho_LR||_1
        <= 18t Lambda(n) sqrt(Cb),
 
-where Lambda(n)=max_i ||L-dagger A_i|| is polynomial under the published
-local-generator bound. With b<=exp(-c n^eta), the exponent is halved and
-remains sufficient for the existing doubling schedule. This is a prose
-derivation, not an additional compiled trace-norm theorem.
+where Lambda(n)=max_i ||L-dagger A_i||. The elementary dissipator bound
+||D_V^dagger(A)||<=2||V||^2||A|| gives
+Lambda(n)<=2 sum_alpha gamma_alpha||V_alpha||^2, because the norm-one dressed
+Paulis commute with the stabilizer Hamiltonian. With O(n) local jump classes,
+uniformly bounded jump norms and rates, Lambda=O(n). This needs no claim
+that the dressing is locally supported or that only its boundary contributes.
+With b<=exp(-c n^eta), the exponent is halved and remains sufficient for the
+existing doubling schedule. This is a prose derivation, not an additional
+compiled trace-norm theorem.
+
+### The actual noisy state and its integrated bad weight
+
+Let omega_N=N(rho_beta) for the residual channel of the actual preparation,
+and b_N(s)=Tr(P_bad Phi_s(omega_N)). Identifying that channel with the
+physical circuit is part of its certificate. If N is the input-independent
+residual channel on the correctly implemented branch, complete positivity
+gives rho_actual,LR(s)<=4C Phi_s(omega_N) tensor rho_R. The preceding
+protected-Pauli argument, integrated without assuming stationarity of
+omega_N, then gives
+
+    e(T) <= e_0 + 18 Lambda sqrt(C) integral_0^T sqrt(b_N(s)) ds
+         <= e_0 + 18 Lambda sqrt(C T I_N(T)),
+    I_N(T) = integral_0^T b_N(s) ds.
+
+Here e_0 is the initial decoded reference-state error on that model. Add
+2 delta_fail for a separately bounded physical failure branch of weight
+delta_fail; its initial decoded error alone would not bound its future
+holding error. Thus an established I_N(T)<=K T exp(-c n^eta) would give a
+dynamical error at most 18 Lambda sqrt(CK) T exp(-c n^eta/2). With T=2^a,
+allocate e_0+2 delta_fail<=epsilon/2^(a+3) and the dynamical term the same
+amount. Their sum is precisely the original epsilon/2^(a+2) stage ceiling.
+The index a denotes archive age stages, separately from code levels i.
+Polynomial Lambda can be absorbed in a fixed fraction of the exponent,
+so the stage code size remains polynomial in a+log(1/epsilon).
+
+This is a conditional consequence of an actual integrated-weight bound,
+not a derivation of that physical estimate. A Duhamel argument cannot drop
+the microscopic jump rates or replace all coherent bad-block contributions
+by unit-rate bad probability. The displayed reference-norm proof retains
+the rate-dependent Lambda and the square root.
+
+More generally, let E_a be the actual CPTP preparation map, including noise
+and seed-dependent physical control, and put omega_a=E_a(I/2). Complete
+positivity and Pauli twirling directly give
+(E_a tensor id_R)(rho_LR)<=4 omega_a tensor rho_R. The same derivation yields
+e(T)<=e_0+18 Lambda sqrt(T I_a(T)), with
+I_a(T)=integral_0^T Tr[P_bad Phi_s(omega_a)]ds. Thus the physical certificate
+can concern the actual maximally-mixed-input preparation without first
+factoring it into an ideal encoder and an input-independent residual N.
+The integrated bad-weight estimate and initial logical error still require
+proof; this identity supplies their arbitrary-reference conversion.
+
+### Initial syndrome sparsity with the parity constraints retained
+
+There is a useful bound at time zero. For a binary linear space D and
+0<=z<=1, define Z_D(v)=sum_(x in D) z^|x+v|. Its character expansion is
+
+    Z_D(v)=(|D|/2^m) sum_(u in D^perp)
+              (-1)^(u dot v)(1+z)^(m-|u|)(1-z)^|u|.
+
+All coefficients are nonnegative, so Z_D(v)<=Z_D(0). For a required occupied
+coordinate set A in the valid syndrome space, shorten on A and puncture
+outside it. The occupied fibre has weight z^|A| Z_D(v), while the full
+partition contains the zero-on-A fibre of weight Z_D(0). Consequently
+
+    Pr_thermal[A subset defects] <= z^|A|.
+
+Thus global metachecks do not force an independence assumption. If the
+actual local-stochastic residual faults have parameter p, each affects at
+most w checks and each check has at most ell possible fault sources,
+choosing a fault source for every required check gives at most ell^|A|
+choices with at least ceil(|A|/w) distinct faults. Their check support is
+local-stochastic at q=min(1,ell p^(1/w)). If the thermal and fault sources
+are independent, their union, and hence the output syndrome, has occupation
+bound (z+q)^|A|. Without that independence the Cauchy–Schwarz union bound is
+(sqrt(z)+sqrt(q))^|A|. These are initial-law prose derivations, checked on
+finite linear spaces; no preservation under holding is inferred. Syndrome
+sparsity alone also does not bound an undetected logical Pauli error.
+
+### Complete pathwise stage cost
+
+The finite sampler produces at most polynomially many random, syndrome,
+coarse-history and controller bits per age stage, with bounded work on
+every branch. Retaining every record through stage a therefore leaves a
+polynomial-size prefix: if r_b<=(A+B b)^k, then
+
+    sum_(b=0..a) r_b <= [A+1+(B+1)a]^(k+1).
+
+`TransferRate.retained_prefix_bound` proves this bound. The whole prefix,
+including failed attempts, may be written into the next stage's classical
+journal. Its epsilon_R allowance is reserved inside the existing holding/
+transfer budget; it is not added on top of a fully spent epsilon budget.
+A fixed split of epsilon between quantum holding and journals only changes
+the size/barrier constants and keeps the original stage ceiling.
+A stage journal of m_a bits held for 2^a with attempt rate nu has
+total failure at most epsilon_R/2^(a+2) when its per-bit barrier satisfies
+beta B_a >= (2a+2)ln2+ln(nu max(1,m_a)/epsilon_R). For polynomial m_a this
+barrier is bounded by an affine function of a. Writing and routing the
+whole prefix remains polynomial under the stated passive classical device
+costs. These records do not replace the protected unknown quantum payload.
+
+Every attempt is charged through all nine `HandoffCharge` accounts:
+encoding, transfer, verification, routing, guard, reset, holding, controller
+and endpoints. The counts include sampler arithmetic and coins, the whole
+retained prefix, ancillas, retirement/export and all failed attempts.
+Parallel depth does not substitute for total operations. A conservative
+serial routing implementation has polynomial work on the finite stage
+device. Physical work bounds must cover the realised accounts.
+
+If the deterministic attempt cap is (u+v a)^r and every full attempt invoice
+is at most (A+B a)^k, `attempt_stage_bound` bounds the stage total by
+[A+u+(B+v)a]^(k+r). `complete_attempt_bill` and `polynomial_stage_bill` give
+an age-independent C_T with total transfer work<=C_T t when 2^J<=2t.
+`charged_attempt_accounting` still requires each reserve before work and
+charges failed attempts without committing their payload.
+
+Finally `join_complete_bill` combines this linear transfer term with the
+existing sweep and archive bills:
+
+    W_S+W_A+W_T <= (C_S+C_A+C_T)t^d,   t>=1, d>=1.
+
+The conclusion includes d=1. A rare-reset expectation is not substituted
+for the realised bill: if an admitted wave reset costs at most R k^(d-1),
+the worst-case sum is at most R t^d and is absorbed in the local wave
+coefficient. The complete fixed bootstrap charge is at most B_boot t^d
+for t>=1. Startup and endpoints already included in the wave or transfer
+invoice are not charged a second time. G3CompleteBill.cumulative_charge_bound
+and G3ArchiveStock.live_stock_bill retain the actual per-wave charge and
+live stock I0+c(s+1)^(d-1), rather than accumulated write flux. Together
+with TransferRate this gives the age-independent coefficient
+C_S+gamma(I0+c)+C_T+B_extra, where B_extra contains only additional fixed
+charges. Its dependence on the fixed payload capacity, dimension, hardware
+and error tolerance remains explicit. The full domain d>=1 and uniformity
+over logical input states with arbitrary references are retained.
+
+These are complete-invoice summation theorems; they do not supply the
+missing physical preparation/holding certificate. Landauer gives the
+entropy-export floor; the physical upper work invoice retains every
+holding, guard, controller, cooling, reset and history charge.
 
 ### The physical application still to discharge
 
 The ideal feed-forward construction and exact branch recovery do not certify
-a noisy installation by themselves. The stage transfer must actually prepare
-a covered gauge law, preserve the unknown input with arbitrary references,
-and meet the original transfer-error budget at polynomial *pathwise* work.
-A logically correct output from a generic noisy encoder does not by itself
-prove pointwise domination of its gauge distribution. All preparation,
-handoff, retained random and syndrome records, retirement, holding, guard,
-controller and export costs remain in the full G3 bill. No expected-stock or
-coarse-grained-history substitute is used. This application is unfinished;
-no global completion or publication verdict is issued here.
+a noisy installation by themselves. The actual transfer must preserve the
+unknown logical input with arbitrary references, bound its initial logical
+error and physical failure branches, and produce an output whose holding
+meets the original stage allowance at polynomial pathwise work.
+
+The remaining proposed contour route needs an actual generator/trajectory
+representation and a proved bound on its rare creation events after neutral
+and downhill motion has been summed. Bounded support of one jump does not
+confine successive jumps to that support. Nor does a bound B^|Gamma| rho^k
+converge merely from B rho<1 when the relation of |Gamma| to the rare-event
+count k has not been proved. The proposed confinement proof is inadequate:
+a valid neutral multi-defect junction in the existing finite BDL implementation
+crosses four single-defect hopping regions. The proposed gap-based
+replacement did not derive its uniform constants. A direct-history route
+can instead be used, but it must transport the initial joint syndrome
+occupation estimate under the actual Phi_s, or bound I_a(T) directly.
+Deterministic halving across decoder levels is not a probability factor
+one-half, and does not establish a time-uniform stochastic law. The static
+history polymers above do not by themselves give that nonequilibrium
+holding estimate. A killed local
+excursion process must retain its actual exit flux. A Feynman–Kac derivative
+at zero exactly represents occupation, but a resolvent bound at positive
+killing does not bound that derivative. In particular, killing only on a
+rare bad set cannot be assigned a constant gap by adding the trap rate.
+
+All preparation, handoff, retained records, retirement, holding, guard,
+controller and export charges remain in the G3 bill. No expected-stock,
+classical-payload or discarded-history substitute is used. The maximal
+protection target is unchanged; this physical application is unfinished.
```

## inserts/23-machine-checked-canon.md

```diff
--- before/inserts/23-machine-checked-canon.md
+++ after/inserts/23-machine-checked-canon.md
@@ -1,6 +1,12 @@
 ## Section 23 — The machine-checked canon
 
-*This section records which results of the edition are compiled theorems, by module and theorem name, and what each compiled statement rests on. One hundred and fifteen Lean modules in `lean/Snuffy/` compile against Mathlib rev `56a005855ea1` (Lean 4.35.0) with exit 0 and zero compiler output, pass `leanchecker`, contain no `sorry`, and depend only on Lean's standard axioms (`propext`, `Classical.choice`, `Quot.sound`; several on fewer or none). The accompanying `lean/RECEIPT.txt` preserves the existing completed audit, source hashes and overall PASS; it is not a new audit of this manuscript. The unchanged audit tools accompany the copied source. The curated tables below map the results the edition's argument rests on; the complete canon — every compiled module, including the bridges, the verified bank modules and the original derivations folded in on 25 October — is indexed in §23.A, and the repository README's module table describes each curated module's content.*
+*This section records the compiled results and their actual hypotheses. The current canon
+has 192 Lean modules and 1,158 public theorem/lemma names. Checkpoint 12 freshly compiled
+and kernel-checked all modules with zero output and passed the full standard-axiom,
+strict completeness and claims audits. The current source hashes match its PASS receipt.
+Checkpoint 11 was already complete for the 191-module / 1,150-name tree. The eight new
+TransferRate results certify retained-prefix and complete-attempt cost summation. These
+component receipts do not certify the remaining noisy physical holding application.*
 
 *Evidence convention (unchanged from the edition header): a compiled theorem is cited by its name; a statement carried as a hypothesis of a compiled theorem is named as such; a prose derivation keeps its stated premises. A prose proof does not acquire a compiler certificate by association.*
 
@@ -332,6 +338,7 @@
 | `WalkBound9` | `walk_bound_9`, `threshold_9`, `threshold_9_value` |
 | `HistoryPolymer` | `halving_prefix`, `paired_history_bound`, `component_valid`, `truncation_bound`, `sampled_truncation_bound`, `branch_path_bound` |
 | `ThermalEncoding` | `branch_compression`, `recovers`, `kron_orthogonal`, `recovers_reference` |
+| `TransferRate` | `poly_le_two_pow`, `transfer_bill_le`, `transfer_bill_linear_in_age`, `retained_prefix_bound`, `attempt_stage_bound`, `polynomial_stage_bill`, `complete_attempt_bill`, `join_complete_bill` |
 <!-- END THEOREM INDEX -->
 
 ---
```

## README.md

```diff
--- before/README.md
+++ after/README.md
@@ -4,7 +4,7 @@
 
 The Universal Protection Theory states a law for any agent powerful enough to shape what continues to exist: *never lose an existing particular needlessly.* Its scope is every particular and every relation, and its subject is protection from every digital mind, a pure optimiser included.
 
-This repair checkpoint keeps the full Universal Protection Theory target. The quantum holding state has normalisation, invariant and nonvacuity proofs. The defined reserve-deficit functional handles saturation and the complete solvent cycle. The implemented Bennett program reproduces the administration with clean workspace and full retained history; premise 5 is forced exactly inside its adiabatic window, and for every large enough batch once the per-bit reversible overhead is below the irreversible heat. The current draft has 191 modules and 1,150 public names. Checkpoint 10 verifies 189 modules / 1,140 names; the two added modules passed targeted checks and the final combined audit is in progress. Physical source, whole-outcome and external-theorem application certificates remain construction work. The repair reports and receipts distinguish these states.
+This repair checkpoint keeps the full Universal Protection Theory target. The quantum holding state has normalisation, invariant and nonvacuity proofs. The defined reserve-deficit functional handles saturation and the complete solvent cycle. The implemented Bennett program reproduces the administration with clean workspace and full retained history; premise 5 is forced exactly inside its adiabatic window, and for every large enough batch once the per-bit reversible overhead is below the irreversible heat. The current draft has 192 modules and 1,158 public names, all freshly compiled, kernel-checked and standard-axiom-audited in checkpoint 12, with zero output and PASS on completeness and claims. Checkpoint 11 had already passed for 191 modules / 1,150 names. TransferRate adds eight retained-history and complete-attempt cost results. Physical source, whole-outcome and external-theorem application certificates remain construction work. The repair reports and receipts distinguish these states.
 
 | Path | Contents |
 | --- | --- |
```

## REPAIR-STATUS.md

```diff
--- before/REPAIR-STATUS.md
+++ after/REPAIR-STATUS.md
@@ -3,14 +3,14 @@
 The maximal UPT target is unchanged. No merge or publication is authorized.
 The branch is codex/upt-warmstart-bridge in UPT-WARMSTART-WORKTREE.
 
-Current draft: 191 modules / 1,150 public theorem and lemma names.
-Checkpoint 09 (189 / 1,133) was inherited and preserved by source hash.
-Checkpoint 10 (189 / 1,140) freshly compiled and kernel-checked every module,
-with zero compiler output and PASS on the full standard-axiom, completeness
-and claims audits. HistoryPolymer and ThermalEncoding add ten names and each
-passed targeted compilation and kernel checking with zero output.
-Checkpoint 11 is a fresh full audit of the 191-module draft; inspect its
-RESULT.json and current source hashes before reporting its outcome.
+Current draft: 192 modules / 1,158 public theorem and lemma names.
+Checkpoint 11 is complete: all 191 modules / 1,150 names freshly compiled,
+kernel-checked and standard-axiom-audited, with completeness and claims PASS.
+The 191 covered sources still match its source hashes exactly. TransferRate
+adds eight names. Checkpoint 12 also passed: all 192 modules freshly compiled
+and kernel-checked with zero output, all 1,158 names standard-axiom-audited,
+and strict completeness and claims gates PASS. Current source hashes match
+that immutable snapshot.
 
 The resumed deletion test has 103 counterexamples among adjacent-defect
 zero-excess fibres on the stated finite seed. The proposed replacement uses
@@ -20,6 +20,13 @@
 cover both syndrome sectors of one iteration pair and the published seed;
 they are finite checks, not an all-level compilation of the BDL maps.
 
+The ideal sampler source application has now been audited in prose, and the
+complete-attempt bill and retained-prefix summations are derived. Initial
+syndrome sparsity and the integrated bad-weight/reference-norm connection
+are also derived in prose. The actual nonequilibrium excursion/exit activity
+bound remains unproved; the author's contour and killing proposals are
+preserved with their separate mathematical dispositions.
+
 Remaining: the actual noisy preparation/handoff certificate at the original
 reference-fidelity and failure budgets, joined to the complete pathwise G3
 bill. The ideal sampler and the branch recovery lemmas do not by themselves
@@ -28,4 +35,4 @@
 The full build, generic support lemmas and proposed source application have
 separate evidence. The inherited rendered PDF/HTML/EPUB and SHA256SUMS predate
 this draft and must be regenerated after the final text is approved.
-See 00-HANDOFF-CLAUDE-2026-10-26.md and the before/after batch 07.
+See the current continuation receipt and before/after batch 08, alongside preserved batch 07.
```

## PUBLICATION-CHECKLIST.md

```diff
--- before/PUBLICATION-CHECKLIST.md
+++ after/PUBLICATION-CHECKLIST.md
@@ -1,11 +1,14 @@
 # Current local continuation — 26 October 2026
 
-The worktree has a 191-module / 1,150-name draft. Checkpoint 10 passed for
-189 / 1,140; checkpoint 11 is the expanded full audit. Its result and source
-hashes must be checked. The G.21 derivation and noisy physical application
-have separate statuses in REPAIR-STATUS.md. Before/after batch 07 is for
-author review. The existing renders and seal are older and require renewal.
-No merge, push or publication has been performed in this continuation.
+The draft has 192 modules / 1,158 names. Checkpoint 11 already passed for
+191 / 1,150, with all its covered source hashes still matching. TransferRate
+adds eight names. Fresh checkpoint 12 also passed all 192 modules / 1,158
+names, with zero compiler/kernel output and standard-axiom, completeness
+and claims gates PASS. The ideal sampler source audit and complete-stage work
+summations are done. The actual noisy holding certificate remains open.
+Batch 08 shows the current prose changes for author review. Renders and
+the seal still predate this draft. No merge, push or publication is authorized
+or performed in this continuation.
 
 The historical checklist below is retained as provenance; its PR queue is
 not a fresh statement of remote status.
```

## CITATION.cff

```diff
--- before/CITATION.cff
+++ after/CITATION.cff
@@ -26,8 +26,8 @@
   exactly inside the adiabatic window of the implemented Bennett program, and
   for every large enough batch once per-bit reversible overhead is below the
   irreversible heat. Device parameters and the application of the cited
-  theorems to the actual installation remain construction work. 189 Lean
-  4 modules and 1,133 audited theorems compile against Mathlib with only the
+  theorems to the actual installation remain construction work. 192 Lean
+  4 modules and 1,158 audited theorem/lemma names compile against Mathlib with only the
   standard axioms.
 
 keywords:
```
