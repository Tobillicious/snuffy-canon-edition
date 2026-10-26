# Manuscript before/after batch 09

27 October 2026. Local author review. Endpoint algebra and controller bounds integrated; the actual joint fault-kernel correspondence remains explicit.

## SNUFFY-CANON-EDITION-4.2-MASTER.md

```diff
--- before/SNUFFY-CANON-EDITION-4.2-MASTER.md
+++ after/SNUFFY-CANON-EDITION-4.2-MASTER.md
@@ -3398,8 +3398,10 @@
 ## G.21 Constructive thermal preparation from the complete decoding history
 
 Working derivation for author review, 26 October 2026. The generic support lemmas are compiled.
-The ideal sampler's source application is audited in prose; the actual noisy physical
-transfer and holding join remain unfinished. The target is the actual
+The ideal sampler's source application is audited in prose. The endpoint
+compensation, anisotropic feedback and complete controller-degree derivations
+are now included below; the installation's joint endpoint-kernel correspondence
+remains explicit. The target is the actual
 BDL thermal syndrome law with a polynomial, preferably constant, one-sided
 pointwise factor. This does not assume product zero-excess fibres, a local
 mixing gap, an initially warm raw state or a reset of protected quantum data.
@@ -3601,8 +3603,10 @@
 source tests cover both syndrome sectors and the published seed; they do
 not replace the all-level source derivation. The external FPTAS is used as
 a published algorithm, not represented as a separately implemented and
-kernel-checked solver in this repository. The actual noisy physical transfer
-and holding certificate remains to be supplied.
+kernel-checked solver in this repository. The later subsections construct
+noise compensation, private Pauli feedback and its controller invoice. Their
+physical-kernel correspondence and prose scope are stated explicitly; the
+canonical kernel receipt remains 192 modules / 1,158 names.
 
 Primary sources: [BDL](https://arxiv.org/abs/2605.10943), Section 4 and
 Section 5.2; [Helmuth–Perkins–Regts](https://arxiv.org/abs/1806.11548),
@@ -3788,38 +3792,304 @@
 entropy-export floor; the physical upper work invoice retains every
 holding, guard, controller, cooling, reset and history charge.
 
-### The physical application still to discharge
-
-The ideal feed-forward construction and exact branch recovery do not certify
-a noisy installation by themselves. The actual transfer must preserve the
-unknown logical input with arbitrary references, bound its initial logical
-error and physical failure branches, and produce an output whose holding
-meets the original stage allowance at polynomial pathwise work.
-
-The remaining proposed contour route needs an actual generator/trajectory
-representation and a proved bound on its rare creation events after neutral
-and downhill motion has been summed. Bounded support of one jump does not
-confine successive jumps to that support. Nor does a bound B^|Gamma| rho^k
-converge merely from B rho<1 when the relation of |Gamma| to the rare-event
-count k has not been proved. The proposed confinement proof is inadequate:
-a valid neutral multi-defect junction in the existing finite BDL implementation
-crosses four single-defect hopping regions. The proposed gap-based
-replacement did not derive its uniform constants. A direct-history route
-can instead be used, but it must transport the initial joint syndrome
-occupation estimate under the actual Phi_s, or bound I_a(T) directly.
-Deterministic halving across decoder levels is not a probability factor
-one-half, and does not establish a time-uniform stochastic law. The static
-history polymers above do not by themselves give that nonequilibrium
-holding estimate. A killed local
-excursion process must retain its actual exit flux. A Feynman–Kac derivative
-at zero exactly represents occupation, but a resolvent bound at positive
-killing does not bound that derivative. In particular, killing only on a
-rare bad set cannot be assigned a constant gap by adding the trap rate.
-
-All preparation, handoff, retained records, retirement, holding, guard,
-controller and export charges remain in the G3 bill. No expected-stock,
-classical-payload or discarded-history substitute is used. The maximal
-protection target is unchanged; this physical application is unfinished.
+### 8. Compensate the specified physical endpoint channel
+
+The prepared input law can account for the endpoint noise. For its actual
+specified Pauli syndrome channel N, construct q=N^(-1)pi and prove q is
+positive, rather than implement a nonpositive inverse quantum operation.
+If a bounded sampler produces mu<=4q, positivity gives Nmu<=4pi.
+The unknown logical state is not inverted or replaced.
+
+For a one-qubit Pauli law (a,b,c,d), in the order I,X,Z,Y, put
+
+    lambda=(1,a+b-c-d,a-b+c-d,a-b-c+d).
+
+The inverse weights are the four-point inverse Fourier transform of
+(1,lambda_1^(-1),lambda_2^(-1),lambda_3^(-1)). If p=b+c+d<1/2, all
+lambda_i>=1-2p. The identity inverse weight r_I>=1, and the convolution
+Neumann series gives |r_P/r_I|<=2p/(1-2p), P!=I. These statements allow
+unequal X,Y,Z rates. The separate PauliInterface development receipt
+checks the inverse/composition and domination algebra; it does not supply
+the physical noise law or the positivity argument below.
+
+For independent local endpoint channels, let u_(j,P)=r_(j,P)/r_(j,I).
+The candidate q is the finite signed sum
+
+    q(sigma)=(product_j r_(j,I))/Z
+       * sum_F (product_(j,P in F) u_(j,P)) z^|sigma+syndrome(F)|,
+
+where F selects at most one nonidentity Pauli colour per location.
+Convolution gives Nq=pi and sum q=1. To prove positivity, augment the
+full-history graph by its fault-colour vertices. A location's colours form
+a clique, and each finest check's history/fault scope forms a clique.
+For bounded footprint w and incidence, its degree D_A is fixed across
+levels. Put B=(D_A+1)^2. The history bound |H|<=K_0|sigma|, K_0=4, and
+the energy change bound |sigma+syndrome(F)|>=|sigma|-w|F| give
+
+    |activity(gamma)|<=b^|gamma|,
+    b=max(z^(1/K_0), max_(j,P)|u_(j,P)| z^(-w)).
+
+With b<=[8eB(D_A+2)]^(-1), the incompatible-activity sum is less than
+|gamma|, also after multiplying size-l activities by t^l for |t|<2.
+The same bound holds in every sampling-prefix/deleted-polymer model.
+Their partition functions are nonzero. Decreasing the real noise rates
+continuously to zero leaves them real, nonzero and positive at zero;
+therefore q and all physical history-prefix masses are positive.
+
+The signed auxiliaries are used only for counting. With s_0=Be b, the KP
+cavity bound gives each conditional original-history inclusion probability
+at most sum_(l>=1) s_0^l<1/4. The probability of a history component larger
+than L is at most M sum_(l>L) l s_0^l. Choose L=O(log M) making this at
+most 1/2. List the P polynomially many retained history components. At
+each decision, estimate the positive exclusion ratio to relative precision
+eta=1/(256P), take an upper enclosure, and round the inclusion probability
+down to a fixed dyadic mesh at most eta. Inclusion is not inflated;
+exclusion is inflated by at most 1+12eta. The full decision-path factor
+is below two. Truncation costs at most two, giving mu<=4q with polynomial
+work and a fixed finite coin budget. All histories and coins are retained.
+
+Finite precision in N is sufficient. In the weighted norm
+||f||_pi=max_sigma |f(sigma)|/pi(sigma), a size-w syndrome translation has
+norm at most z^(-w). If the nominal channel hatN_j has
+hatp_j(1+z^(-w))<=1/2, its inverse norm is at most two. For l1 probability
+vector error epsilon_j,
+
+    ||N_j hatN_j^(-1)||_pi<=1+2z^(-w)epsilon_j,
+    Nmu<=4 exp(2z^(-w)sum_j epsilon_j) pi.
+
+Consequently O(1/n) rate accuracy per output costs a fixed envelope factor;
+no global minimum-eigenvalue ratio or exponentially precise calibration
+is used. Calibration failure remains a separately budgeted branch.
+
+### 9. Physical private outputs and anisotropic feedback
+
+The short FT processor computes the ideal old decoder/new branch encoder.
+For each output prepare a separate encoded Bell pair A,B. Keep B encoded
+and private during waiting; move only A into the logical Bell measurement
+with the source output S. The encoded comparison measurement traces both
+measured auxiliary coordinates. For an arbitrary omega_(S,G_S,R), and
+resource |Phi><Phi|_(A_L,B_L) tensor eta_(G_A,G_B), the unnormalised
+receiving state at outcome m is exactly
+
+    (1/4) P_m omega_(B_L,R) P_m tensor Tr_(G_A)eta.
+
+Indeed tracing the measured gauges commutes with the logical measurement.
+The statement permits entangled gauges and an arbitrary old reference.
+Independent private resource pairs leave product receiving-gauge marginals.
+Private decoding W_j then has effective channel D_j(rho)=W_j(rho tensor
+tau_j). With ideal Pauli feedback its outcome average is the Pauli twirl
+(1/4)sum_m P_m D_j(P_m rho P_m)P_m.
+
+Christandl--Fawzi--Goswami, arXiv:2408.05260v3, Definition 20 and
+Lemmas 29--32, give the uniform encoded comparison and interfaces with
+polynomial overhead. Their general output theorem retains correlated
+auxiliaries; independence is not inferred from it. In the stochastic
+Pauli/stabilizer implementation, each fixed private fault path gives an
+input-independent Pauli, so let d_j be that private decoder's Pauli law.
+
+Actual feedback need not have isotropic or outcome-independent rates.
+Write I,X,Z,Y as F2^2. Let c_j(eta|m) describe corruption of the two
+correction bits. Use two fixed physical slots, X/idle then Z/idle, whose
+post-slot Pauli kernels are x_(j,bx),z_(j,bz). Their residual convolution
+is r_(j,bx,bz)(f)=sum_(u+v=f)x_(j,bx)(u)z_(j,bz)(v). The actual local
+endpoint law is
+
+    q_j(a)=1/4 sum_(m,e,eta,f:e+eta+f=a)
+               d_j(e)c_j(eta|m)r_(j,m+eta)(f).
+
+This follows by Pauli propagation through the actual requested correction;
+Pauli conjugation changes only irrelevant phases. Both idle slots, wrong
+control bits and every final gate fault remain included. If p_D,p_C,p_X,p_Z
+are the actual four nonidentity-mass bounds, then
+
+    1-q_j(0)<=p_D+p_C+p_X+p_Z.
+
+With b,z,w as above, the explicit threshold
+p_*=b z^w/[2(1+b z^w)] ensures both inverse and forward colour bounds
+whenever that sum is at most p_*. This is a derived inequality to check
+against the physical kernel, not a numerical hardware claim.
+
+Microscopic factorisation can be checked directly: if disjoint endpoint
+devices have initially product private reservoirs and conditional generator
+sum_j L_j(m_j) with disjoint supports, their conditional evolution is the
+tensor product of the local evolutions. Summing the uniform Bell outcomes
+then gives N=product_j N_j with the q_j above. This identifies exactly what
+the private hardware and guards must implement. A local-stochastic bound
+alone does not prove these reservoir/generator conditions. If shared causes
+remain admitted at these endpoints, their actual joint kernel must be
+retained and a compatible compensation or holding certificate supplied.
+
+The FT comparison error is at most C M_FT sqrt((c_FT p)^r), with constants
+of the selected fixed scheme. It is a diamond error before holding, so
+subsequent holding/decoding does not multiply it by 2^a. The r=O(a+log n+
+log(1/epsilon)) choice retains polynomial stage work. The source theorem's
+noiseless classical-control convention is not a free physical controller:
+the realised controller and its faults must occupy the charged accounts.
+
+### 10. Endpoint logical error and retained-record holding
+
+The signed gas supplies a joint-occupation bound for every partial endpoint
+layer. Add the already-applied positive forward-noise colours to its
+inverse-colour graph, with activity p_P/(1-p) z^(-w), and enlarge the fixed
+degree accordingly. If R_0=2Be b<1, then
+
+    Pr[A occupied]<=R_0^|A|.
+
+To prove it, select the augmented polymers meeting A. They cover A; the
+cavity bound controls their remaining partition ratio by exp(sum|gamma|).
+Choose the first uncovered mark and its size-l polymer. It removes at most
+l marks. Induction bounds the covering sum by
+R_0^|A| sum_(l>=1)(Be b/R_0)^l=R_0^|A|. Dropping compatibility only
+increases this nonnegative majorant. Positivity refers to the physical
+history marginal, not to the signed auxiliary weights.
+
+BDL's finest-syndrome witness count now applies with R_0 in place of
+thermal fugacity. In its notation a sufficient geometric ratio is
+
+    theta=2(Delta+1)^2[(1+R_0^(1/4))^M_l-1]^(1/(1+Delta_l^4))<=1/2.
+
+The witness-size threshold 2^(k-1) then gives unstable probability
+B_n<=poly(n)exp(-c n^eta_mem), uniformly over partial preparation layers
+and both sectors. This estimate concerns the preparation layer, not an
+unproved long-time transport of a sparse law. Stable-syndrome Pauli paths
+act as logical identity. Thus m endpoint locations give e_out<=8m B_n.
+The old block's bounded input-interface layer is covered by the earlier
+thermal-plus-fault occupation estimate, giving the corresponding e_in.
+
+Keep all sampler/teleportation records H in the actual map E:L->Q tensor H
+and put omega_QH=E(I/2). The reference inequality is
+(E tensor id_R)(rho_LR)<=4 omega_QH tensor rho_R; omega_QH need not factor.
+The compensated calculation only requires its physical marginal
+omega_Q<=C_out rho_beta. Holding the quantum block and keeping the record
+comparison as a spectator leaves the R,H marginal unchanged. Apply the
+same projector-block estimate to K tensor B_RH for arbitrary ||B_RH||<=1.
+The decoded Pauli expansion gives
+
+    ||rho_decoded,LHR(T)-rho_decoded,LHR(0)||_1
+       <=18 Lambda integral_0^T sqrt(Tr[P_bad Phi_s(omega_Q)])ds
+       <=18 Lambda T sqrt(C_out b_beta).
+
+This retains joint tests of the records and the old reference; it does not
+discard H to obtain a Gibbs product inequality. H's own storage faults and
+work remain in the classical-record account. A coherent private-channel
+version can insert stable projectors only in a comparison process. The
+gentle projection/telescoping bound gives the conservative endpoint error
+16m sqrt(B_n), preserving the stretched-exponential suppression.
+
+Add e_in,e_out, the FT diamond error, calibration/controller failure and
+the dynamical term inside the original epsilon/2^(a+2) stage allowance.
+The incoming logical error is carried additively in the global composition;
+it is not assumed to contract. With s=a+ln(1/epsilon)+1, choose the least
+available BDL size above K s^(2/eta_mem). Its volume is polynomial in s;
+the spatial exponent grows as s^2 while the time/allocation debt is O(s).
+A fixed sufficiently large K meets every stage budget, including the
+2a ln2 term. No new age-dependent noise rate is required.
+
+### 11. A derived controller degree and physical invoice
+
+For augmented degree D_A, put B=(D_A+1)^2,
+h=ceil(log_2 B), u=h+2, v=ceil(log_2(3B)). The truncation and connected-set
+count give P<=C M^u. To enclose a prefix partition ratio to relative
+eta=1/(256P), truncate log Z(t) at
+l=ceil(log_2(8M/eta)). The zero-free radius two gives log-tail bound
+M 2^(-l). Connected-support Mobius inversion computes these coefficients:
+for each connected U, enumerate W subset U and the occupied assignments
+of W. This costs at most 3^|U| assignment tests; disconnected support terms
+cancel by partition factorisation. Common-denominator rational arithmetic
+and finite-series evaluation give the conservative bit-operation bound
+
+    T_sampler<=C b_rate^4 M^kappa,
+    kappa=(u+1)v+u+13.
+
+The extra 13 allows root enumeration, eight powers of Taylor-order overhead
+and four powers of the common-denominator bit size. All are fixed graph/
+arithmetic bounds, not an assumed mixing exponent. The scalar exponential
+is enclosed by a finite convergent-series computation at the same precision.
+
+Let L_0 count the maximum recursive calls and physical operations in the
+selected finite FT base gadget, with its classical-control procedure.
+The recursion T_d<=L_0(T_(d-1)+1) gives degree
+nu=ceil(log_2(2L_0)) in the accuracy index r. Set g=ceil(2/eta_mem).
+Using n<=C s^g, M<=C n^2, b_rate,r<=C s, Gaussian CSS synthesis bounded
+by C n^3, and a fixed O(n^2 s) calibration samples per endpoint gives
+
+    K_c=max(2g kappa+nu+4, 3g+nu, 3g+4nu+1).
+
+
+The finite base gadget also includes the classical control implementation.
+Unroll its bounded syndrome/verification rounds and synthesize each Boolean
+control on its fixed m_0 measurement bits by a truth-table circuit. Compute
+three copies, with a private majority for each physical quantum-operation
+control. A fault in one copy is outvoted; a final majority fault affects one
+quantum location; corruption of a shared raw record is a faulty measurement
+outcome already covered by the syndrome-gadget proof. An unprotected control
+flag is never fanned out to many quantum locations. Padding prevents a bad
+flag from extending execution. Count these finite circuits in L_0 before
+the FT recursion. The degree above includes FT protection of the sampler
+and calibration computation as well as the quantum gates.
+
+The last term includes stabilizer-tableau simulation of the specified
+private fault kernel. Operation count, workspace and new records are at
+most C s^K_c. Retaining the entire prefix adds at most one degree. Serial
+routing adds one workspace factor, giving at most C s^(2K_c+2) primitive
+events. Total stock-times-duration, including every wait, guard and clock,
+is then bounded by C s^(3K_c+3) in unit-duration units.
+
+The classical activation/reset primitive supplies a physical upper invoice.
+Use logical states 0,1 and bridge state e with H(B)=B|e><e|; upwards rates
+are nu_0 exp(-beta B) and downwards rates nu_0. Its flip hazard is at most
+nu_0 exp(-beta B), matching the existing barrier model. Since
+0<=Tr(rho dH/dB)<=1, a barrier ramp's gross actuator work is at most its
+total variation, for every state/fault trajectory. A bounded local unitary
+has a Hamiltonian logarithm of norm at most pi in gate-time units, so
+switching it on/off has a fixed finite drive invoice.
+
+For reset, raise undesired levels by E and use their downwards reset jumps.
+The wrong-state probability obeys dp_bad/dt<=-nu_0 p_bad+2nu_0 exp(-beta E),
+and hence p_bad(t)<=exp(-nu_0 t)+2exp(-beta E). Taking B,E and the capped
+reset duration O(s) meets the union allocation for polynomially many
+controller operations. Ramps cost O(B+E), and the bounded-spectrum first
+law bounds net reset heat/export by control work plus O(B+E). Power-capped
+controller/export actuators have an O(s) realised invoice. Admitted extra
+circuit faults remain in the FT account, not omitted from this thermal
+estimate. Landauer supplies the lower floor, not this upper bound.
+
+Reset duration and the linear per-primitive invoice add two conservative
+degrees. Consequently the complete stage implementation in this device
+model satisfies
+
+    W_stage<=C s^(3K_c+5).
+
+All nine HandoffCharge accounts, the complete history, failed attempts,
+retirement and endpoints remain included. The existing deterministic cap
+and TransferRate.polynomial_stage_bill give total transfer work <=C_T t.
+TransferRate.join_complete_bill joins the existing sweep/archive bills for
+every d_G>=1. The coefficient is independent of archive age and the unknown
+logical input. These degree/invoice derivations are prose; the canonical
+Checkpoint 12 source count is unchanged.
+
+
+### Exact remaining physical correspondence
+
+The compensation and controller construction above close the specified
+private Pauli-interface application once the actual joint endpoint kernel
+has the displayed microscopic factorisation, including its input layer,
+classical-control faults and final feedback. That factorisation must be
+identified with the installation's guarded operation. It is not implied
+by the original local-stochastic inequality: two endpoint faults can share
+a cause while every required faulty set still has probability at most
+p^|S|. Their product of marginals would be the wrong physical channel.
+No general correlated-fault certificate is declared from that substitution.
+
+A retained joint-kernel compensation/holding construction can alternatively
+discharge this correspondence. The earlier integrated-bad-weight route
+also remains sufficient; static decoder halving alone does not supply its
+physical-time transport. These are routes to the same full quantum,
+arbitrary-reference, full-history target and original stage allowance.
+The stage arithmetic, controller operation degree and retained-prefix G3
+join need not be requested again. The installation's final kernel
+identification remains unfinished; no global completion verdict, weakened
+noise-domain replacement, merge or publication is issued.
 
 
 ---
```

## inserts/25-boundary-work-history.md

```diff
--- before/inserts/25-boundary-work-history.md
+++ after/inserts/25-boundary-work-history.md
@@ -61,8 +61,10 @@
 ## G.21 Constructive thermal preparation from the complete decoding history
 
 Working derivation for author review, 26 October 2026. The generic support lemmas are compiled.
-The ideal sampler's source application is audited in prose; the actual noisy physical
-transfer and holding join remain unfinished. The target is the actual
+The ideal sampler's source application is audited in prose. The endpoint
+compensation, anisotropic feedback and complete controller-degree derivations
+are now included below; the installation's joint endpoint-kernel correspondence
+remains explicit. The target is the actual
 BDL thermal syndrome law with a polynomial, preferably constant, one-sided
 pointwise factor. This does not assume product zero-excess fibres, a local
 mixing gap, an initially warm raw state or a reset of protected quantum data.
@@ -264,8 +266,10 @@
 source tests cover both syndrome sectors and the published seed; they do
 not replace the all-level source derivation. The external FPTAS is used as
 a published algorithm, not represented as a separately implemented and
-kernel-checked solver in this repository. The actual noisy physical transfer
-and holding certificate remains to be supplied.
+kernel-checked solver in this repository. The later subsections construct
+noise compensation, private Pauli feedback and its controller invoice. Their
+physical-kernel correspondence and prose scope are stated explicitly; the
+canonical kernel receipt remains 192 modules / 1,158 names.
 
 Primary sources: [BDL](https://arxiv.org/abs/2605.10943), Section 4 and
 Section 5.2; [Helmuth–Perkins–Regts](https://arxiv.org/abs/1806.11548),
@@ -451,35 +455,301 @@
 entropy-export floor; the physical upper work invoice retains every
 holding, guard, controller, cooling, reset and history charge.
 
-### The physical application still to discharge
-
-The ideal feed-forward construction and exact branch recovery do not certify
-a noisy installation by themselves. The actual transfer must preserve the
-unknown logical input with arbitrary references, bound its initial logical
-error and physical failure branches, and produce an output whose holding
-meets the original stage allowance at polynomial pathwise work.
-
-The remaining proposed contour route needs an actual generator/trajectory
-representation and a proved bound on its rare creation events after neutral
-and downhill motion has been summed. Bounded support of one jump does not
-confine successive jumps to that support. Nor does a bound B^|Gamma| rho^k
-converge merely from B rho<1 when the relation of |Gamma| to the rare-event
-count k has not been proved. The proposed confinement proof is inadequate:
-a valid neutral multi-defect junction in the existing finite BDL implementation
-crosses four single-defect hopping regions. The proposed gap-based
-replacement did not derive its uniform constants. A direct-history route
-can instead be used, but it must transport the initial joint syndrome
-occupation estimate under the actual Phi_s, or bound I_a(T) directly.
-Deterministic halving across decoder levels is not a probability factor
-one-half, and does not establish a time-uniform stochastic law. The static
-history polymers above do not by themselves give that nonequilibrium
-holding estimate. A killed local
-excursion process must retain its actual exit flux. A Feynman–Kac derivative
-at zero exactly represents occupation, but a resolvent bound at positive
-killing does not bound that derivative. In particular, killing only on a
-rare bad set cannot be assigned a constant gap by adding the trap rate.
-
-All preparation, handoff, retained records, retirement, holding, guard,
-controller and export charges remain in the G3 bill. No expected-stock,
-classical-payload or discarded-history substitute is used. The maximal
-protection target is unchanged; this physical application is unfinished.
+### 8. Compensate the specified physical endpoint channel
+
+The prepared input law can account for the endpoint noise. For its actual
+specified Pauli syndrome channel N, construct q=N^(-1)pi and prove q is
+positive, rather than implement a nonpositive inverse quantum operation.
+If a bounded sampler produces mu<=4q, positivity gives Nmu<=4pi.
+The unknown logical state is not inverted or replaced.
+
+For a one-qubit Pauli law (a,b,c,d), in the order I,X,Z,Y, put
+
+    lambda=(1,a+b-c-d,a-b+c-d,a-b-c+d).
+
+The inverse weights are the four-point inverse Fourier transform of
+(1,lambda_1^(-1),lambda_2^(-1),lambda_3^(-1)). If p=b+c+d<1/2, all
+lambda_i>=1-2p. The identity inverse weight r_I>=1, and the convolution
+Neumann series gives |r_P/r_I|<=2p/(1-2p), P!=I. These statements allow
+unequal X,Y,Z rates. The separate PauliInterface development receipt
+checks the inverse/composition and domination algebra; it does not supply
+the physical noise law or the positivity argument below.
+
+For independent local endpoint channels, let u_(j,P)=r_(j,P)/r_(j,I).
+The candidate q is the finite signed sum
+
+    q(sigma)=(product_j r_(j,I))/Z
+       * sum_F (product_(j,P in F) u_(j,P)) z^|sigma+syndrome(F)|,
+
+where F selects at most one nonidentity Pauli colour per location.
+Convolution gives Nq=pi and sum q=1. To prove positivity, augment the
+full-history graph by its fault-colour vertices. A location's colours form
+a clique, and each finest check's history/fault scope forms a clique.
+For bounded footprint w and incidence, its degree D_A is fixed across
+levels. Put B=(D_A+1)^2. The history bound |H|<=K_0|sigma|, K_0=4, and
+the energy change bound |sigma+syndrome(F)|>=|sigma|-w|F| give
+
+    |activity(gamma)|<=b^|gamma|,
+    b=max(z^(1/K_0), max_(j,P)|u_(j,P)| z^(-w)).
+
+With b<=[8eB(D_A+2)]^(-1), the incompatible-activity sum is less than
+|gamma|, also after multiplying size-l activities by t^l for |t|<2.
+The same bound holds in every sampling-prefix/deleted-polymer model.
+Their partition functions are nonzero. Decreasing the real noise rates
+continuously to zero leaves them real, nonzero and positive at zero;
+therefore q and all physical history-prefix masses are positive.
+
+The signed auxiliaries are used only for counting. With s_0=Be b, the KP
+cavity bound gives each conditional original-history inclusion probability
+at most sum_(l>=1) s_0^l<1/4. The probability of a history component larger
+than L is at most M sum_(l>L) l s_0^l. Choose L=O(log M) making this at
+most 1/2. List the P polynomially many retained history components. At
+each decision, estimate the positive exclusion ratio to relative precision
+eta=1/(256P), take an upper enclosure, and round the inclusion probability
+down to a fixed dyadic mesh at most eta. Inclusion is not inflated;
+exclusion is inflated by at most 1+12eta. The full decision-path factor
+is below two. Truncation costs at most two, giving mu<=4q with polynomial
+work and a fixed finite coin budget. All histories and coins are retained.
+
+Finite precision in N is sufficient. In the weighted norm
+||f||_pi=max_sigma |f(sigma)|/pi(sigma), a size-w syndrome translation has
+norm at most z^(-w). If the nominal channel hatN_j has
+hatp_j(1+z^(-w))<=1/2, its inverse norm is at most two. For l1 probability
+vector error epsilon_j,
+
+    ||N_j hatN_j^(-1)||_pi<=1+2z^(-w)epsilon_j,
+    Nmu<=4 exp(2z^(-w)sum_j epsilon_j) pi.
+
+Consequently O(1/n) rate accuracy per output costs a fixed envelope factor;
+no global minimum-eigenvalue ratio or exponentially precise calibration
+is used. Calibration failure remains a separately budgeted branch.
+
+### 9. Physical private outputs and anisotropic feedback
+
+The short FT processor computes the ideal old decoder/new branch encoder.
+For each output prepare a separate encoded Bell pair A,B. Keep B encoded
+and private during waiting; move only A into the logical Bell measurement
+with the source output S. The encoded comparison measurement traces both
+measured auxiliary coordinates. For an arbitrary omega_(S,G_S,R), and
+resource |Phi><Phi|_(A_L,B_L) tensor eta_(G_A,G_B), the unnormalised
+receiving state at outcome m is exactly
+
+    (1/4) P_m omega_(B_L,R) P_m tensor Tr_(G_A)eta.
+
+Indeed tracing the measured gauges commutes with the logical measurement.
+The statement permits entangled gauges and an arbitrary old reference.
+Independent private resource pairs leave product receiving-gauge marginals.
+Private decoding W_j then has effective channel D_j(rho)=W_j(rho tensor
+tau_j). With ideal Pauli feedback its outcome average is the Pauli twirl
+(1/4)sum_m P_m D_j(P_m rho P_m)P_m.
+
+Christandl--Fawzi--Goswami, arXiv:2408.05260v3, Definition 20 and
+Lemmas 29--32, give the uniform encoded comparison and interfaces with
+polynomial overhead. Their general output theorem retains correlated
+auxiliaries; independence is not inferred from it. In the stochastic
+Pauli/stabilizer implementation, each fixed private fault path gives an
+input-independent Pauli, so let d_j be that private decoder's Pauli law.
+
+Actual feedback need not have isotropic or outcome-independent rates.
+Write I,X,Z,Y as F2^2. Let c_j(eta|m) describe corruption of the two
+correction bits. Use two fixed physical slots, X/idle then Z/idle, whose
+post-slot Pauli kernels are x_(j,bx),z_(j,bz). Their residual convolution
+is r_(j,bx,bz)(f)=sum_(u+v=f)x_(j,bx)(u)z_(j,bz)(v). The actual local
+endpoint law is
+
+    q_j(a)=1/4 sum_(m,e,eta,f:e+eta+f=a)
+               d_j(e)c_j(eta|m)r_(j,m+eta)(f).
+
+This follows by Pauli propagation through the actual requested correction;
+Pauli conjugation changes only irrelevant phases. Both idle slots, wrong
+control bits and every final gate fault remain included. If p_D,p_C,p_X,p_Z
+are the actual four nonidentity-mass bounds, then
+
+    1-q_j(0)<=p_D+p_C+p_X+p_Z.
+
+With b,z,w as above, the explicit threshold
+p_*=b z^w/[2(1+b z^w)] ensures both inverse and forward colour bounds
+whenever that sum is at most p_*. This is a derived inequality to check
+against the physical kernel, not a numerical hardware claim.
+
+Microscopic factorisation can be checked directly: if disjoint endpoint
+devices have initially product private reservoirs and conditional generator
+sum_j L_j(m_j) with disjoint supports, their conditional evolution is the
+tensor product of the local evolutions. Summing the uniform Bell outcomes
+then gives N=product_j N_j with the q_j above. This identifies exactly what
+the private hardware and guards must implement. A local-stochastic bound
+alone does not prove these reservoir/generator conditions. If shared causes
+remain admitted at these endpoints, their actual joint kernel must be
+retained and a compatible compensation or holding certificate supplied.
+
+The FT comparison error is at most C M_FT sqrt((c_FT p)^r), with constants
+of the selected fixed scheme. It is a diamond error before holding, so
+subsequent holding/decoding does not multiply it by 2^a. The r=O(a+log n+
+log(1/epsilon)) choice retains polynomial stage work. The source theorem's
+noiseless classical-control convention is not a free physical controller:
+the realised controller and its faults must occupy the charged accounts.
+
+### 10. Endpoint logical error and retained-record holding
+
+The signed gas supplies a joint-occupation bound for every partial endpoint
+layer. Add the already-applied positive forward-noise colours to its
+inverse-colour graph, with activity p_P/(1-p) z^(-w), and enlarge the fixed
+degree accordingly. If R_0=2Be b<1, then
+
+    Pr[A occupied]<=R_0^|A|.
+
+To prove it, select the augmented polymers meeting A. They cover A; the
+cavity bound controls their remaining partition ratio by exp(sum|gamma|).
+Choose the first uncovered mark and its size-l polymer. It removes at most
+l marks. Induction bounds the covering sum by
+R_0^|A| sum_(l>=1)(Be b/R_0)^l=R_0^|A|. Dropping compatibility only
+increases this nonnegative majorant. Positivity refers to the physical
+history marginal, not to the signed auxiliary weights.
+
+BDL's finest-syndrome witness count now applies with R_0 in place of
+thermal fugacity. In its notation a sufficient geometric ratio is
+
+    theta=2(Delta+1)^2[(1+R_0^(1/4))^M_l-1]^(1/(1+Delta_l^4))<=1/2.
+
+The witness-size threshold 2^(k-1) then gives unstable probability
+B_n<=poly(n)exp(-c n^eta_mem), uniformly over partial preparation layers
+and both sectors. This estimate concerns the preparation layer, not an
+unproved long-time transport of a sparse law. Stable-syndrome Pauli paths
+act as logical identity. Thus m endpoint locations give e_out<=8m B_n.
+The old block's bounded input-interface layer is covered by the earlier
+thermal-plus-fault occupation estimate, giving the corresponding e_in.
+
+Keep all sampler/teleportation records H in the actual map E:L->Q tensor H
+and put omega_QH=E(I/2). The reference inequality is
+(E tensor id_R)(rho_LR)<=4 omega_QH tensor rho_R; omega_QH need not factor.
+The compensated calculation only requires its physical marginal
+omega_Q<=C_out rho_beta. Holding the quantum block and keeping the record
+comparison as a spectator leaves the R,H marginal unchanged. Apply the
+same projector-block estimate to K tensor B_RH for arbitrary ||B_RH||<=1.
+The decoded Pauli expansion gives
+
+    ||rho_decoded,LHR(T)-rho_decoded,LHR(0)||_1
+       <=18 Lambda integral_0^T sqrt(Tr[P_bad Phi_s(omega_Q)])ds
+       <=18 Lambda T sqrt(C_out b_beta).
+
+This retains joint tests of the records and the old reference; it does not
+discard H to obtain a Gibbs product inequality. H's own storage faults and
+work remain in the classical-record account. A coherent private-channel
+version can insert stable projectors only in a comparison process. The
+gentle projection/telescoping bound gives the conservative endpoint error
+16m sqrt(B_n), preserving the stretched-exponential suppression.
+
+Add e_in,e_out, the FT diamond error, calibration/controller failure and
+the dynamical term inside the original epsilon/2^(a+2) stage allowance.
+The incoming logical error is carried additively in the global composition;
+it is not assumed to contract. With s=a+ln(1/epsilon)+1, choose the least
+available BDL size above K s^(2/eta_mem). Its volume is polynomial in s;
+the spatial exponent grows as s^2 while the time/allocation debt is O(s).
+A fixed sufficiently large K meets every stage budget, including the
+2a ln2 term. No new age-dependent noise rate is required.
+
+### 11. A derived controller degree and physical invoice
+
+For augmented degree D_A, put B=(D_A+1)^2,
+h=ceil(log_2 B), u=h+2, v=ceil(log_2(3B)). The truncation and connected-set
+count give P<=C M^u. To enclose a prefix partition ratio to relative
+eta=1/(256P), truncate log Z(t) at
+l=ceil(log_2(8M/eta)). The zero-free radius two gives log-tail bound
+M 2^(-l). Connected-support Mobius inversion computes these coefficients:
+for each connected U, enumerate W subset U and the occupied assignments
+of W. This costs at most 3^|U| assignment tests; disconnected support terms
+cancel by partition factorisation. Common-denominator rational arithmetic
+and finite-series evaluation give the conservative bit-operation bound
+
+    T_sampler<=C b_rate^4 M^kappa,
+    kappa=(u+1)v+u+13.
+
+The extra 13 allows root enumeration, eight powers of Taylor-order overhead
+and four powers of the common-denominator bit size. All are fixed graph/
+arithmetic bounds, not an assumed mixing exponent. The scalar exponential
+is enclosed by a finite convergent-series computation at the same precision.
+
+Let L_0 count the maximum recursive calls and physical operations in the
+selected finite FT base gadget, with its classical-control procedure.
+The recursion T_d<=L_0(T_(d-1)+1) gives degree
+nu=ceil(log_2(2L_0)) in the accuracy index r. Set g=ceil(2/eta_mem).
+Using n<=C s^g, M<=C n^2, b_rate,r<=C s, Gaussian CSS synthesis bounded
+by C n^3, and a fixed O(n^2 s) calibration samples per endpoint gives
+
+    K_c=max(2g kappa+nu+4, 3g+nu, 3g+4nu+1).
+
+
+The finite base gadget also includes the classical control implementation.
+Unroll its bounded syndrome/verification rounds and synthesize each Boolean
+control on its fixed m_0 measurement bits by a truth-table circuit. Compute
+three copies, with a private majority for each physical quantum-operation
+control. A fault in one copy is outvoted; a final majority fault affects one
+quantum location; corruption of a shared raw record is a faulty measurement
+outcome already covered by the syndrome-gadget proof. An unprotected control
+flag is never fanned out to many quantum locations. Padding prevents a bad
+flag from extending execution. Count these finite circuits in L_0 before
+the FT recursion. The degree above includes FT protection of the sampler
+and calibration computation as well as the quantum gates.
+
+The last term includes stabilizer-tableau simulation of the specified
+private fault kernel. Operation count, workspace and new records are at
+most C s^K_c. Retaining the entire prefix adds at most one degree. Serial
+routing adds one workspace factor, giving at most C s^(2K_c+2) primitive
+events. Total stock-times-duration, including every wait, guard and clock,
+is then bounded by C s^(3K_c+3) in unit-duration units.
+
+The classical activation/reset primitive supplies a physical upper invoice.
+Use logical states 0,1 and bridge state e with H(B)=B|e><e|; upwards rates
+are nu_0 exp(-beta B) and downwards rates nu_0. Its flip hazard is at most
+nu_0 exp(-beta B), matching the existing barrier model. Since
+0<=Tr(rho dH/dB)<=1, a barrier ramp's gross actuator work is at most its
+total variation, for every state/fault trajectory. A bounded local unitary
+has a Hamiltonian logarithm of norm at most pi in gate-time units, so
+switching it on/off has a fixed finite drive invoice.
+
+For reset, raise undesired levels by E and use their downwards reset jumps.
+The wrong-state probability obeys dp_bad/dt<=-nu_0 p_bad+2nu_0 exp(-beta E),
+and hence p_bad(t)<=exp(-nu_0 t)+2exp(-beta E). Taking B,E and the capped
+reset duration O(s) meets the union allocation for polynomially many
+controller operations. Ramps cost O(B+E), and the bounded-spectrum first
+law bounds net reset heat/export by control work plus O(B+E). Power-capped
+controller/export actuators have an O(s) realised invoice. Admitted extra
+circuit faults remain in the FT account, not omitted from this thermal
+estimate. Landauer supplies the lower floor, not this upper bound.
+
+Reset duration and the linear per-primitive invoice add two conservative
+degrees. Consequently the complete stage implementation in this device
+model satisfies
+
+    W_stage<=C s^(3K_c+5).
+
+All nine HandoffCharge accounts, the complete history, failed attempts,
+retirement and endpoints remain included. The existing deterministic cap
+and TransferRate.polynomial_stage_bill give total transfer work <=C_T t.
+TransferRate.join_complete_bill joins the existing sweep/archive bills for
+every d_G>=1. The coefficient is independent of archive age and the unknown
+logical input. These degree/invoice derivations are prose; the canonical
+Checkpoint 12 source count is unchanged.
+
+
+### Exact remaining physical correspondence
+
+The compensation and controller construction above close the specified
+private Pauli-interface application once the actual joint endpoint kernel
+has the displayed microscopic factorisation, including its input layer,
+classical-control faults and final feedback. That factorisation must be
+identified with the installation's guarded operation. It is not implied
+by the original local-stochastic inequality: two endpoint faults can share
+a cause while every required faulty set still has probability at most
+p^|S|. Their product of marginals would be the wrong physical channel.
+No general correlated-fault certificate is declared from that substitution.
+
+A retained joint-kernel compensation/holding construction can alternatively
+discharge this correspondence. The earlier integrated-bad-weight route
+also remains sufficient; static decoder halving alone does not supply its
+physical-time transport. These are routes to the same full quantum,
+arbitrary-reference, full-history target and original stage allowance.
+The stage arithmetic, controller operation degree and retained-prefix G3
+join need not be requested again. The installation's final kernel
+identification remains unfinished; no global completion verdict, weakened
+noise-domain replacement, merge or publication is issued.
```

## REPAIR-STATUS.md

```diff
--- before/REPAIR-STATUS.md
+++ after/REPAIR-STATUS.md
@@ -23,9 +23,11 @@
 The ideal sampler source application has now been audited in prose, and the
 complete-attempt bill and retained-prefix summations are derived. Initial
 syndrome sparsity and the integrated bad-weight/reference-norm connection
-are also derived in prose. The actual nonequilibrium excursion/exit activity
-bound remains unproved; the author's contour and killing proposals are
-preserved with their separate mathematical dispositions.
+are also derived in prose. G.21 now includes the compensated endpoint law, anisotropic feedback,
+tracked-record holding conversion and explicit controller-degree/invoice
+derivations. The installation's joint endpoint-kernel correspondence remains
+unproved; local-stochastic marginals do not establish the required product
+law. The earlier excursion route remains an alternative.
 
 Remaining: the actual noisy preparation/handoff certificate at the original
 reference-fidelity and failure budgets, joined to the complete pathwise G3
@@ -35,4 +37,4 @@
 The full build, generic support lemmas and proposed source application have
 separate evidence. The inherited rendered PDF/HTML/EPUB and SHA256SUMS predate
 this draft and must be regenerated after the final text is approved.
-See the current continuation receipt and before/after batch 08, alongside preserved batch 07.
+See the current continuation receipt and before/after batch 09, with batches 07 and 08 preserved.
```
