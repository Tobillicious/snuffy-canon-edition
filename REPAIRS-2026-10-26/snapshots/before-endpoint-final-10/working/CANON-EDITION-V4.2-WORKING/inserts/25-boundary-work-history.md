

## G.20 Device requirements, and the open initialisation problem

The constructions of G.16–G.19 hold for any installation whose devices meet the inequalities below.
Each is a hypothesis of a compiled theorem, stated explicitly; none is assumed silently. They are
requirements on the protector's devices, of the kind a capable agent can meet by acquiring better
hardware. The targets are unchanged.

| Requirement | Inequality | Theorem that takes it |
|---|---|---|
| Circuit fault rate | Weighted local stochastic noise with \(p<1/(4\cdot9.71^2\cdot\tfrac{94}{15})\), above \(4.2\times10^{-4}\), for the rotated surface code with the standard schedule | `WalkBound9.threshold_9`, `threshold_9_value` (with `WeightedEdgeLaw`, `EdgeLaw`, `Threshold.fail_le_geometric`) |
| Coupling bound | Every agent couples to a record frame with strength at most \(W\); correction interval \(\Delta\le\hbar(t-\varepsilon)/W\) | `G1Refinement.physical_protection_qsl` |
| Reversible overhead | Per-bit non-heat lifecycle cost \(\eta\) below the irreversible heat per bit \(q\ge k_BT\ln2\) | `BennettBatch.premise5_batched` |
| Passive reference barrier | Stage \(j\) barrier at least \(k_BT(2j\ln2+\ln(1/\varepsilon))\) above the attempt scale | `PassiveReference.total_failure_le` |
| Windowed decoding | A wrong inner commit costs the next window at most a bounded part of its fault budget | `ToleranceSweep.wrong_subset_bad`, `sweep_density` (DKLP overlapping recovery) |
| Record redundancy | An intact fragment of the objective record reads the record | `RedundantRecord.tolerant_outer_decoder` (quantum Darwinism and spectrum-broadcast theorems) |

**Barrier heights in numbers.** For an age of \(10^{18}\,\mathrm s\), an attempt time of
\(10^{-12}\,\mathrm s\), a base stage of \(1\,\mathrm s\) and \(\varepsilon=10^{-9}\), the largest
barrier needed is about \(132\,k_BT\), roughly \(3.4\,\mathrm{eV}\) at \(300\,\mathrm K\). The barrier
grows only logarithmically with age and lies within the barriers of atomic defects in solids.

**The tightened threshold** (`WalkBound9`). The exact maximum self-avoiding walk count at length 9
over all interior vertices is \(c_9=763{,}504{,}745\le9.71^9\) (`walk_bound_9`). This raises the
explicit threshold of G.19 above \(4.2\times10^{-4}\) (`threshold_9`, `threshold_9_value`).

**The quantum-coherence branch: the warm start and the open problem** (`WarmStart`).
Balasubramanian, Davydova and Lin prove a passive memory in \(\mathbb R^3\) for the thermal encoding
(arXiv:2605.10943, Theorems 1.1 and 2.6, via Chesi, Loss, Bravyi and Terhal, New J. Phys. 12,
025013, 2010). The open step is preparing an initial state the theorem covers.

Call a prepared syndrome law \(\mu\) a warm start when \(\mu\le C\pi\) pointwise, with \(\pi\) the
thermal syndrome law. A warm start stays dominated at every time: \(\mu K^t\le C\pi\)
(`warm_start`), and every event has probability at most \(C\,\pi(A)\) (`warm_start_event`). Tracking
the protected logical observables then gives a drift of the decoded qubit of at most
\(t\cdot\mathrm{poly}(n)\cdot\sqrt{C\,\mathrm{Tr}(P^\perp\rho_\beta)}\). Chesi et al.'s hypotheses
make \(P\mathcal L^\dagger(\tilde X)P=0\), so only leakage from \(P\) moves \(\langle\tilde X\rangle\).
A warm start with \(C=\mathrm{poly}(n)\) therefore preserves the exponential lifetime, with its
exponent halved. This derivation is recorded with its sources and is not compiled.

The empty syndrome is not a warm start: its constant is \(1/\pi(\emptyset)=e^{\Theta(n)}\).

An exhaustive computation on the construction itself shows that a fixed-range polymer route
cannot supply the warm start. The construction is built algebraically from the paper's §3.2.2,
and the build verifies \(\delta^1\delta^0=0\) and one logical qubit at every level computed. The
metachecks of level \(i\) are stretched by the scale factor \(\ell\) at each later level. In the
computed cases, all dependencies are generated within radius 4 at level 1 and within radius 12 at
level 2, with \(\ell=3\). Hence for every fixed range a single violated check passes all local
metachecks yet is invalid.

Section G.21 develops a constructive full-history polymer sampler for the ideal thermal
syndrome law, with its counting theorem and source correspondence stated explicitly. It avoids
the failed product/deletion hypothesis and does not require a preparation mixing estimate.
`WarmStart.fibre_reassembly` and `reverse_sampler_bound` give the exact probability-composition
algebra. `pointwise_from_absolute` retains the probability floor whenever an absolute-error
estimate is used. The actual noisy preparation/handoff and complete-cost application remain
unfinished; the maximal quantum-coherence target is retained in full.


## G.21 Constructive thermal preparation from the complete decoding history

Working derivation for author review, 26 October 2026. The generic support lemmas are compiled.
The ideal sampler's source application is audited in prose. The endpoint
compensation, anisotropic feedback and complete controller-degree derivations
are now included below; the installation's joint endpoint-kernel correspondence
remains explicit. The target is the actual
BDL thermal syndrome law with a polynomial, preferably constant, one-sided
pointwise factor. This does not assume product zero-excess fibres, a local
mixing gap, an initially warm raw state or a reset of protected quantum data.

### 1. Retain the full deterministic history

For one syndrome sector of C(2k), introduce one binary variable for every
syndrome coordinate at every level:

    h = (s_2k, s_(2k-1), ..., s_0).

Fix all local tie-breaks in the published coarse-graining maps, with the
zero input producing zero corrections. A valid finest syndrome determines
exactly one history. Conversely, the following finite local constraints
characterize such histories:

* For an R_X step, use (L1), (L2), (L3) of STEP2-FINE-CONDITIONAL.md, with
  the coarse output stored as the next layer's variables.
* For an R_Z step, use the local cohomology-class reduction in Theorem 4.6.
  The difference from the lifted coarse value is a local coboundary.
* The constant-sized seed syndrome s_0 must belong to its actual image(delta).

Backward induction using s_i=delta(f_i)+F_i(s_(i-1)) proves global validity
at every level. Forward evaluation of the fixed local rules proves
uniqueness. These are constraints on syndrome variables; f_i is computed,
not summed over as an additional freely degenerate variable.

Each constraint has bounded scope and each coordinate appears in boundedly
many constraints, uniformly in k. The bounds depend on the fixed gadget
size, Tanner degrees and subdivision parameter. The seed constraint has
constant scope. Make the primal graph G by connecting every pair of
coordinates in a common constraint scope. Its degree Delta is bounded
independently of k. Its number M of vertices is polynomial in the physical
block size (indeed at most the sum of the level sizes). Let S bound each scope
and I the number of scopes reading one coordinate. The fixed gadget and
Tanner incidences give constants S and I independent of the code level. An
intermediate coordinate is read only by the two adjacent coarse steps, so
I does not grow with hierarchy depth. Explicitly, Delta<=I(S-1). The finite
tests' observed degrees are not substituted for this uniform symbolic bound.

The local source correspondence is BDL Theorems 4.6 and 4.7, Remarks 4.4–4.5,
and the bounded-degree construction. Their Section 5.2 already records full
decoding histories and proves componentwise coarse-graining. The primal
graph used here includes whole constraint scopes, so component restriction
does not assume the stronger product property that failed numerically.

### 2. Derive the history energy bound

Write the history in the finest-to-coarsest direction. Every R_Z step is
non-increasing in syndrome weight; every R_X step reduces it by at least
one half. The two steps alternate. Thus, in either sector,

    |s_(i-2)| <= |s_i|/2,
    sum_i |s_i| <= 2 sum_(j>=0) 2^(-j) |s_2k| <= 4 |s_2k|.

This holds for every valid history, including a history obtained by
restricting to one connected support component. It is a support/energy
inequality on the complete history, not a fixed-range metacheck assumption.

### 3. Connected components give an exact polymer representation

The all-zero history satisfies every constraint. Let h be valid and let
Gamma be a connected component of its occupied coordinates in G. Setting
all other coordinates to zero leaves a valid history:

* a constraint touching Gamma cannot touch another occupied component,
  because its scope is a clique;
* on that scope the restricted assignment either agrees with h or is zero;
* both assignments satisfy the constraint in the respective case.

Conversely, the union of pairwise nonadjacent valid connected supports is
valid by the same scope argument. Hence there is an exact bijection between
histories and compatible polymer families. A polymer is a nonempty connected
support Gamma whose standalone binary assignment satisfies every constraint.

Let E(Gamma) count its occupied *finest-level* coordinates. The previous
bound applied to that standalone valid history gives

    E(Gamma) >= |Gamma|/4 > 0.

There is no zero-energy polymer. Its activity at z=exp(-beta) is the
monomial w_Gamma(z)=z^E(Gamma). Energy is additive on disjoint components.
The polymer partition function is therefore exactly the thermal partition
function on valid finest syndromes: there is no uncounted fibre multiplicity.

### 4. Verify convergence with explicit constants

Put B=(Delta+1)^2. A rooted depth-first traversal bounds the number of
connected supports of size ell containing a fixed vertex by B^ell. There
is at most one binary polymer assignment on a given support.

An incompatible polymer meets the closed neighbourhood of Gamma, of size
at most (Delta+1)|Gamma|. For r=B e |z|^(1/4),

    sum_(eta incompatible Gamma) |w_eta(z)| exp(|eta|)
       <= (Delta+1)|Gamma| sum_(ell>=1) r^ell
       = (Delta+1)|Gamma| r/(1-r).

For example choose the complex fugacity disk

    delta = [1/(4 e B (Delta+2))]^4.

Then r<1/[4(Delta+2)] throughout |z|<delta, so the displayed sum is less
than |Gamma|. This is the Kotecky–Preiss criterion, derived here from the
actual history bound. Taking the device temperature sufficiently low that
0<z_0<delta, as well as below BDL's memory threshold, gives uniform slack.

The algorithmic counting hypotheses are also explicit: connected supports
of size ell can be listed in exp(O(ell+log M)); testing their local
constraints and computing E takes polynomial time in ell; activities are
monomials of order at least |Gamma|/4; and the full partition polynomial has
degree at most the number of finest checks, hence at most M. The same
convergence bound holds after deleting any set of polymers.

Helmuth–Perkins–Regts Theorem 2.2 and Lemma 2.8 in Section 2.6 then
supply a deterministic relative partition-function approximation for every
remaining polymer set. This application uses their general bounded-degree
polymer result, not an unsupported transfer of their Potts-model conclusion.

### 5. Truncate with a one-sided pointwise guarantee

Set q=B z_0^(1/4)<1. In a positive repulsive polymer gas,
P(Gamma present)<=w_Gamma. A union bound gives

    P(some polymer has size > L)
       <= M sum_(ell>L) q^ell
       = M q^(L+1)/(1-q).

Choose L=O(log M) so this is at most 1/2. The exact gas restricted to
polymers of size at most L is the full thermal law conditioned on that
event, and hence is pointwise at most twice the full law. Missing rare
large-polymer configurations causes no problem for this one-sided bound.

List the P<=poly(M) remaining polymers. Visit them once in a fixed order.
If a polymer conflicts with one already selected, skip it. Otherwise the
exact conditional inclusion probability is

    p = w_Gamma Z(remaining compatible with Gamma)
        / [Z(remaining without Gamma)
           + w_Gamma Z(remaining compatible with Gamma)].

Both partition functions are for deleted-polymer submodels. Approximate
each within exp(+-eta), eta=1/(16P). The resulting probability and its
complement are each at most exp(2eta) times their exact values.

This is finite feed-forward self-reduction, with no Markov-chain mixing.
Its pointwise guarantee follows by multiplying the conditional branch
factors, rather than converting a TV estimate without a probability floor.

### 6. Keep the randomness and work pathwise bounded

Exact rational-coin rejection is unnecessary. Inclusion has p<=1/2 since
w_Gamma<=1 and the compatible partition function is at most the unrestricted
one. Clamp the approximate probability to at most 1/2, then round it down
to a dyadic grid of spacing d<=1/(16P). Sample it with a fixed b=O(log P)
unbiased random bits.

Rounding down only decreases the inclusion probability. It increases the
exclusion probability by at most d; the true exclusion probability is at
least 1/2. Thus either branch is at most

    exp(2eta)+2d <= exp(1/(4P))

times the true branch probability. Over all P visits the factor is at
most exp(1/4)<2. Combining with truncation gives

    mu_sector <= 4 pi_sector.

All enumeration, counting calls, branch decisions and random-bit use have
a deterministic polynomial bound in M. The history and used random bits
can be retained in the existing complete ledger. This is not an expected-
work substitution.

For the two independent CSS syndrome sectors the joint factor multiplies:
mu_joint<=16 pi_joint. The exponent p in A n^p can be zero. No maximum-of-
sector-factors shortcut is used.

### 7. Preserve the unknown logical state and its reference

Sample the syndrome independently of the unknown logical input. For each
sampled s, use the published decoder's Pauli representative O_s, with
delta(O_s)=s, on the encoded logical state. The branch encoder V_s is an
isometry, and its matching decoder has D_s V_s=I. The controlled branch
record is retained. Linearity extends this identity to every joint logical-
reference state. `ChannelExtension.ext_recovers_reference` supplies the
existing isometric-reference algebra; the branch circuit must be identified
with it. There is no replacement by a fixed default logical state.

The following reference-norm derivation keeps the arbitrary reference register
and the original fault budget. Its ideal warm-start proof and its residual-noise
application have distinct statuses.

### Verification status

The ideal sampler's prose source audit checks the local cut-out, uniform
scope incidence, exact history/partition bijection and all hypotheses of the
published counting theorem, including the polymer-deleted submodels. The
generic support, restriction and conditioning bounds are compiled. Finite
source tests cover both syndrome sectors and the published seed; they do
not replace the all-level source derivation. The external FPTAS is used as
a published algorithm, not represented as a separately implemented and
kernel-checked solver in this repository. The later subsections construct
noise compensation, private Pauli feedback and its controller invoice. Their
physical-kernel correspondence and prose scope are stated explicitly; the
canonical kernel receipt remains 192 modules / 1,158 names.

Primary sources: [BDL](https://arxiv.org/abs/2605.10943), Section 4 and
Section 5.2; [Helmuth–Perkins–Regts](https://arxiv.org/abs/1806.11548),
Theorem 2.2, Section 2.6 and Theorem 4.1. The proposed application and all
intermediate estimates above are to be checked as this work, rather than
reported as statements already proved by those authors.


### The checked core and the reference norm

`HistoryPolymer.halving_prefix` and `paired_history_bound` prove the finite
support budget. `component_valid` proves restriction for zero-valid local
constraints; `truncation_bound` and `sampled_truncation_bound` prove the
conditioning factors; `branch_path_bound` compares probabilities along each
finite sampling path. The scope graph identifies why actual connected
components satisfy the separation condition. Finite tests of one complete
iteration pair cover both syndrome sectors and the published five-qubit seed;
they support the source correspondence and do not replace its all-level proof.

`ThermalEncoding.recovers_reference` proves that the orthogonal syndrome
mixture and matching decoder return every joint logical-reference operator.
The actual branches use the same Pauli representatives as the BDL decoder.
This is a decoded-channel identity, not a claim that tracing an arbitrary
Stinespring ancilla leaves an arbitrary physical state unchanged.

For completeness, the reference-uniform holding estimate can be obtained
without a classical-jump assumption. Let C bound the joint syndrome law,
let b=Tr(P-perp rho_beta), and let A_X,A_Y,A_Z be the protected dressed Pauli
observables. Pauli twirling gives rho_LR <= 2 I_L tensor rho_R. Consequently
the independently prepared gauge warm start obeys
rho_enc,LR <= 4C rho_beta tensor rho_R. Complete positivity and Gibbs
stationarity preserve this order at every holding time, so the bad-projector
weight is at most 4Cb.

If P B P=0 and a state has bad weight p, the diagonal/off-diagonal decomposition
and Cauchy-Schwarz give |Tr(B rho)| <= ||B||[p+2 sqrt(p(1-p))]
<= 3||B|| sqrt(p). Apply this to (L-dagger A_i) tensor T_R, with
||T_R||<=1, and integrate in time. The protected-Pauli hypotheses give
P(L-dagger A_i)P=0. Trace-norm duality bounds each reference coefficient in
the decoded Pauli expansion by 6t ||L-dagger A_i|| sqrt(Cb). The identity
coefficient vanishes because the reference marginal is unchanged. Hence

    ||(Dec Phi_t Enc_mu tensor id_R)(rho_LR)-rho_LR||_1
       <= 18t Lambda(n) sqrt(Cb),

where Lambda(n)=max_i ||L-dagger A_i||. The elementary dissipator bound
||D_V^dagger(A)||<=2||V||^2||A|| gives
Lambda(n)<=2 sum_alpha gamma_alpha||V_alpha||^2, because the norm-one dressed
Paulis commute with the stabilizer Hamiltonian. With O(n) local jump classes,
uniformly bounded jump norms and rates, Lambda=O(n). This needs no claim
that the dressing is locally supported or that only its boundary contributes.
With b<=exp(-c n^eta), the exponent is halved and remains sufficient for the
existing doubling schedule. This is a prose derivation, not an additional
compiled trace-norm theorem.

### The actual noisy state and its integrated bad weight

Let omega_N=N(rho_beta) for the residual channel of the actual preparation,
and b_N(s)=Tr(P_bad Phi_s(omega_N)). Identifying that channel with the
physical circuit is part of its certificate. If N is the input-independent
residual channel on the correctly implemented branch, complete positivity
gives rho_actual,LR(s)<=4C Phi_s(omega_N) tensor rho_R. The preceding
protected-Pauli argument, integrated without assuming stationarity of
omega_N, then gives

    e(T) <= e_0 + 18 Lambda sqrt(C) integral_0^T sqrt(b_N(s)) ds
         <= e_0 + 18 Lambda sqrt(C T I_N(T)),
    I_N(T) = integral_0^T b_N(s) ds.

Here e_0 is the initial decoded reference-state error on that model. Add
2 delta_fail for a separately bounded physical failure branch of weight
delta_fail; its initial decoded error alone would not bound its future
holding error. Thus an established I_N(T)<=K T exp(-c n^eta) would give a
dynamical error at most 18 Lambda sqrt(CK) T exp(-c n^eta/2). With T=2^a,
allocate e_0+2 delta_fail<=epsilon/2^(a+3) and the dynamical term the same
amount. Their sum is precisely the original epsilon/2^(a+2) stage ceiling.
The index a denotes archive age stages, separately from code levels i.
Polynomial Lambda can be absorbed in a fixed fraction of the exponent,
so the stage code size remains polynomial in a+log(1/epsilon).

This is a conditional consequence of an actual integrated-weight bound,
not a derivation of that physical estimate. A Duhamel argument cannot drop
the microscopic jump rates or replace all coherent bad-block contributions
by unit-rate bad probability. The displayed reference-norm proof retains
the rate-dependent Lambda and the square root.

More generally, let E_a be the actual CPTP preparation map, including noise
and seed-dependent physical control, and put omega_a=E_a(I/2). Complete
positivity and Pauli twirling directly give
(E_a tensor id_R)(rho_LR)<=4 omega_a tensor rho_R. The same derivation yields
e(T)<=e_0+18 Lambda sqrt(T I_a(T)), with
I_a(T)=integral_0^T Tr[P_bad Phi_s(omega_a)]ds. Thus the physical certificate
can concern the actual maximally-mixed-input preparation without first
factoring it into an ideal encoder and an input-independent residual N.
The integrated bad-weight estimate and initial logical error still require
proof; this identity supplies their arbitrary-reference conversion.

### Initial syndrome sparsity with the parity constraints retained

There is a useful bound at time zero. For a binary linear space D and
0<=z<=1, define Z_D(v)=sum_(x in D) z^|x+v|. Its character expansion is

    Z_D(v)=(|D|/2^m) sum_(u in D^perp)
              (-1)^(u dot v)(1+z)^(m-|u|)(1-z)^|u|.

All coefficients are nonnegative, so Z_D(v)<=Z_D(0). For a required occupied
coordinate set A in the valid syndrome space, shorten on A and puncture
outside it. The occupied fibre has weight z^|A| Z_D(v), while the full
partition contains the zero-on-A fibre of weight Z_D(0). Consequently

    Pr_thermal[A subset defects] <= z^|A|.

Thus global metachecks do not force an independence assumption. If the
actual local-stochastic residual faults have parameter p, each affects at
most w checks and each check has at most ell possible fault sources,
choosing a fault source for every required check gives at most ell^|A|
choices with at least ceil(|A|/w) distinct faults. Their check support is
local-stochastic at q=min(1,ell p^(1/w)). If the thermal and fault sources
are independent, their union, and hence the output syndrome, has occupation
bound (z+q)^|A|. Without that independence the Cauchy–Schwarz union bound is
(sqrt(z)+sqrt(q))^|A|. These are initial-law prose derivations, checked on
finite linear spaces; no preservation under holding is inferred. Syndrome
sparsity alone also does not bound an undetected logical Pauli error.

### Complete pathwise stage cost

The finite sampler produces at most polynomially many random, syndrome,
coarse-history and controller bits per age stage, with bounded work on
every branch. Retaining every record through stage a therefore leaves a
polynomial-size prefix: if r_b<=(A+B b)^k, then

    sum_(b=0..a) r_b <= [A+1+(B+1)a]^(k+1).

`TransferRate.retained_prefix_bound` proves this bound. The whole prefix,
including failed attempts, may be written into the next stage's classical
journal. Its epsilon_R allowance is reserved inside the existing holding/
transfer budget; it is not added on top of a fully spent epsilon budget.
A fixed split of epsilon between quantum holding and journals only changes
the size/barrier constants and keeps the original stage ceiling.
A stage journal of m_a bits held for 2^a with attempt rate nu has
total failure at most epsilon_R/2^(a+2) when its per-bit barrier satisfies
beta B_a >= (2a+2)ln2+ln(nu max(1,m_a)/epsilon_R). For polynomial m_a this
barrier is bounded by an affine function of a. Writing and routing the
whole prefix remains polynomial under the stated passive classical device
costs. These records do not replace the protected unknown quantum payload.

Every attempt is charged through all nine `HandoffCharge` accounts:
encoding, transfer, verification, routing, guard, reset, holding, controller
and endpoints. The counts include sampler arithmetic and coins, the whole
retained prefix, ancillas, retirement/export and all failed attempts.
Parallel depth does not substitute for total operations. A conservative
serial routing implementation has polynomial work on the finite stage
device. Physical work bounds must cover the realised accounts.

If the deterministic attempt cap is (u+v a)^r and every full attempt invoice
is at most (A+B a)^k, `attempt_stage_bound` bounds the stage total by
[A+u+(B+v)a]^(k+r). `complete_attempt_bill` and `polynomial_stage_bill` give
an age-independent C_T with total transfer work<=C_T t when 2^J<=2t.
`charged_attempt_accounting` still requires each reserve before work and
charges failed attempts without committing their payload.

Finally `join_complete_bill` combines this linear transfer term with the
existing sweep and archive bills:

    W_S+W_A+W_T <= (C_S+C_A+C_T)t^d,   t>=1, d>=1.

The conclusion includes d=1. A rare-reset expectation is not substituted
for the realised bill: if an admitted wave reset costs at most R k^(d-1),
the worst-case sum is at most R t^d and is absorbed in the local wave
coefficient. The complete fixed bootstrap charge is at most B_boot t^d
for t>=1. Startup and endpoints already included in the wave or transfer
invoice are not charged a second time. G3CompleteBill.cumulative_charge_bound
and G3ArchiveStock.live_stock_bill retain the actual per-wave charge and
live stock I0+c(s+1)^(d-1), rather than accumulated write flux. Together
with TransferRate this gives the age-independent coefficient
C_S+gamma(I0+c)+C_T+B_extra, where B_extra contains only additional fixed
charges. Its dependence on the fixed payload capacity, dimension, hardware
and error tolerance remains explicit. The full domain d>=1 and uniformity
over logical input states with arbitrary references are retained.

These are complete-invoice summation theorems; they do not supply the
missing physical preparation/holding certificate. Landauer gives the
entropy-export floor; the physical upper work invoice retains every
holding, guard, controller, cooling, reset and history charge.

### 8. Compensate the specified physical endpoint channel

The prepared input law can account for the endpoint noise. For its actual
specified Pauli syndrome channel N, construct q=N^(-1)pi and prove q is
positive, rather than implement a nonpositive inverse quantum operation.
If a bounded sampler produces mu<=4q, positivity gives Nmu<=4pi.
The unknown logical state is not inverted or replaced.

For a one-qubit Pauli law (a,b,c,d), in the order I,X,Z,Y, put

    lambda=(1,a+b-c-d,a-b+c-d,a-b-c+d).

The inverse weights are the four-point inverse Fourier transform of
(1,lambda_1^(-1),lambda_2^(-1),lambda_3^(-1)). If p=b+c+d<1/2, all
lambda_i>=1-2p. The identity inverse weight r_I>=1, and the convolution
Neumann series gives |r_P/r_I|<=2p/(1-2p), P!=I. These statements allow
unequal X,Y,Z rates. The separate PauliInterface development receipt
checks the inverse/composition and domination algebra; it does not supply
the physical noise law or the positivity argument below.

For independent local endpoint channels, let u_(j,P)=r_(j,P)/r_(j,I).
The candidate q is the finite signed sum

    q(sigma)=(product_j r_(j,I))/Z
       * sum_F (product_(j,P in F) u_(j,P)) z^|sigma+syndrome(F)|,

where F selects at most one nonidentity Pauli colour per location.
Convolution gives Nq=pi and sum q=1. To prove positivity, augment the
full-history graph by its fault-colour vertices. A location's colours form
a clique, and each finest check's history/fault scope forms a clique.
For bounded footprint w and incidence, its degree D_A is fixed across
levels. Put B=(D_A+1)^2. The history bound |H|<=K_0|sigma|, K_0=4, and
the energy change bound |sigma+syndrome(F)|>=|sigma|-w|F| give

    |activity(gamma)|<=b^|gamma|,
    b=max(z^(1/K_0), max_(j,P)|u_(j,P)| z^(-w)).

With b<=[8eB(D_A+2)]^(-1), the incompatible-activity sum is less than
|gamma|, also after multiplying size-l activities by t^l for |t|<2.
The same bound holds in every sampling-prefix/deleted-polymer model.
Their partition functions are nonzero. Decreasing the real noise rates
continuously to zero leaves them real, nonzero and positive at zero;
therefore q and all physical history-prefix masses are positive.

The signed auxiliaries are used only for counting. With s_0=Be b, the KP
cavity bound gives each conditional original-history inclusion probability
at most sum_(l>=1) s_0^l<1/4. The probability of a history component larger
than L is at most M sum_(l>L) l s_0^l. Choose L=O(log M) making this at
most 1/2. List the P polynomially many retained history components. At
each decision, estimate the positive exclusion ratio to relative precision
eta=1/(256P), take an upper enclosure, and round the inclusion probability
down to a fixed dyadic mesh at most eta. Inclusion is not inflated;
exclusion is inflated by at most 1+12eta. The full decision-path factor
is below two. Truncation costs at most two, giving mu<=4q with polynomial
work and a fixed finite coin budget. All histories and coins are retained.

Finite precision in N is sufficient. In the weighted norm
||f||_pi=max_sigma |f(sigma)|/pi(sigma), a size-w syndrome translation has
norm at most z^(-w). If the nominal channel hatN_j has
hatp_j(1+z^(-w))<=1/2, its inverse norm is at most two. For l1 probability
vector error epsilon_j,

    ||N_j hatN_j^(-1)||_pi<=1+2z^(-w)epsilon_j,
    Nmu<=4 exp(2z^(-w)sum_j epsilon_j) pi.

Consequently O(1/n) rate accuracy per output costs a fixed envelope factor;
no global minimum-eigenvalue ratio or exponentially precise calibration
is used. Calibration failure remains a separately budgeted branch.

### 9. Physical private outputs and anisotropic feedback

The short FT processor computes the ideal old decoder/new branch encoder.
For each output prepare a separate encoded Bell pair A,B. Keep B encoded
and private during waiting; move only A into the logical Bell measurement
with the source output S. The encoded comparison measurement traces both
measured auxiliary coordinates. For an arbitrary omega_(S,G_S,R), and
resource |Phi><Phi|_(A_L,B_L) tensor eta_(G_A,G_B), the unnormalised
receiving state at outcome m is exactly

    (1/4) P_m omega_(B_L,R) P_m tensor Tr_(G_A)eta.

Indeed tracing the measured gauges commutes with the logical measurement.
The statement permits entangled gauges and an arbitrary old reference.
Independent private resource pairs leave product receiving-gauge marginals.
Private decoding W_j then has effective channel D_j(rho)=W_j(rho tensor
tau_j). With ideal Pauli feedback its outcome average is the Pauli twirl
(1/4)sum_m P_m D_j(P_m rho P_m)P_m.

Christandl--Fawzi--Goswami, arXiv:2408.05260v3, Definition 20 and
Lemmas 29--32, give the uniform encoded comparison and interfaces with
polynomial overhead. Their general output theorem retains correlated
auxiliaries; independence is not inferred from it. In the stochastic
Pauli/stabilizer implementation, each fixed private fault path gives an
input-independent Pauli, so let d_j be that private decoder's Pauli law.

Actual feedback need not have isotropic or outcome-independent rates.
Write I,X,Z,Y as F2^2. Let c_j(eta|m) describe corruption of the two
correction bits. Use two fixed physical slots, X/idle then Z/idle, whose
post-slot Pauli kernels are x_(j,bx),z_(j,bz). Their residual convolution
is r_(j,bx,bz)(f)=sum_(u+v=f)x_(j,bx)(u)z_(j,bz)(v). The actual local
endpoint law is

    q_j(a)=1/4 sum_(m,e,eta,f:e+eta+f=a)
               d_j(e)c_j(eta|m)r_(j,m+eta)(f).

This follows by Pauli propagation through the actual requested correction;
Pauli conjugation changes only irrelevant phases. Both idle slots, wrong
control bits and every final gate fault remain included. If p_D,p_C,p_X,p_Z
are the actual four nonidentity-mass bounds, then

    1-q_j(0)<=p_D+p_C+p_X+p_Z.

With b,z,w as above, the explicit threshold
p_*=b z^w/[2(1+b z^w)] ensures both inverse and forward colour bounds
whenever that sum is at most p_*. This is a derived inequality to check
against the physical kernel, not a numerical hardware claim.

Microscopic factorisation can be checked directly: if disjoint endpoint
devices have initially product private reservoirs and conditional generator
sum_j L_j(m_j) with disjoint supports, their conditional evolution is the
tensor product of the local evolutions. Summing the uniform Bell outcomes
then gives N=product_j N_j with the q_j above. This identifies exactly what
the private hardware and guards must implement. A local-stochastic bound
alone does not prove these reservoir/generator conditions. If shared causes
remain admitted at these endpoints, their actual joint kernel must be
retained and a compatible compensation or holding certificate supplied.

The FT comparison error is at most C M_FT sqrt((c_FT p)^r), with constants
of the selected fixed scheme. It is a diamond error before holding, so
subsequent holding/decoding does not multiply it by 2^a. The r=O(a+log n+
log(1/epsilon)) choice retains polynomial stage work. The source theorem's
noiseless classical-control convention is not a free physical controller:
the realised controller and its faults must occupy the charged accounts.


#### Explicit reset/feedback generator and bounded correlated jump causes

Initial correlations of finite private noise-label registers can be removed
without resetting the unknown data. For target tau_j=diag(t_j), the jumps
L_(j,u,v)=sqrt(nu_j t_(j,u))|u><v| give exactly
G_j(rho)=nu_j[tau_j Tr(rho)-rho]. Since the replacer R_j is idempotent,
exp(tG_j)=exp(-nu_j t)id+(1-exp(-nu_j t))R_j. The product reset differs
from complete replacement by at most 2sum_j exp(-nu_j t) in diamond norm,
even from initially correlated registers and references. A fixed reset
time nu_min^(-1)ln(2m/delta_reset)=O(s) suffices. The reset invoice above
covers it. This removes initial correlations; it does not remove new
shared faults occurring after reset.

For a concrete feedback slot choose H_(X,b)=b pi X/(2tau) and jump
sqrt(gamma_X)X. These commute, at zero Bohr frequency, for both X and idle.
The actual slot is its requested Pauli followed by X noise of probability
(1-exp(-2gamma_X tau))/2<=gamma_X tau. The analogous Z slot yields a fixed
anisotropic Pauli residual, independent of the requested Bell outcome.
It therefore composes with the exact twirl of even a coherent private
decoder. All couplings and durations are specified local parameters.

Output-qubit independence can also be relaxed. For bounded Pauli causes
P_e and generator L_e=gamma_e(Ad(P_e)-id), conjugation superoperators
commute even when the underlying Paulis anticommute. Hence the actual
joint endpoint channel is exactly

    N=product_e[(1-p_e)id+p_e Ad(P_e)],
    p_e=(1-exp(-2gamma_e t_e))/2.

This factors over physical jump causes, retaining correlations between
output qubits. Each inverse is [(1-p_e)id-p_e Ad(P_e)]/(1-2p_e). With
bounded syndrome footprint/incidence, one signed fault vertex per cause
keeps the augmented graph degree constant. The compensation and counting
proofs therefore apply to this joint channel as well. Commuting pulse-time
causes use the same formula; other causes require their actual time-ordered
channel. This is an explicit sufficient microscopic model, not a claim
that every original local-stochastic law is a commuting Pauli-jump process.

### 10. Endpoint logical error and retained-record holding

The signed gas supplies a joint-occupation bound for every partial endpoint
layer. Add the already-applied positive forward-noise colours to its
inverse-colour graph, with activity p_P/(1-p) z^(-w), and enlarge the fixed
degree accordingly. If R_0=2Be b<1, then

    Pr[A occupied]<=R_0^|A|.

To prove it, select the augmented polymers meeting A. They cover A; the
cavity bound controls their remaining partition ratio by exp(sum|gamma|).
Choose the first uncovered mark and its size-l polymer. It removes at most
l marks. Induction bounds the covering sum by
R_0^|A| sum_(l>=1)(Be b/R_0)^l=R_0^|A|. Dropping compatibility only
increases this nonnegative majorant. Positivity refers to the physical
history marginal, not to the signed auxiliary weights.

BDL's finest-syndrome witness count now applies with R_0 in place of
thermal fugacity. In its notation a sufficient geometric ratio is

    theta=2(Delta+1)^2[(1+R_0^(1/4))^M_l-1]^(1/(1+Delta_l^4))<=1/2.

The witness-size threshold 2^(k-1) then gives unstable probability
B_n<=poly(n)exp(-c n^eta_mem), uniformly over partial preparation layers
and both sectors. This estimate concerns the preparation layer, not an
unproved long-time transport of a sparse law. Stable-syndrome Pauli paths
act as logical identity. Thus m endpoint locations give e_out<=8m B_n.
The old block's bounded input-interface layer is covered by the earlier
thermal-plus-fault occupation estimate, giving the corresponding e_in.

Keep all sampler/teleportation records H in the actual map E:L->Q tensor H
and put omega_QH=E(I/2). The reference inequality is
(E tensor id_R)(rho_LR)<=4 omega_QH tensor rho_R; omega_QH need not factor.
The compensated calculation only requires its physical marginal
omega_Q<=C_out rho_beta. Holding the quantum block and keeping the record
comparison as a spectator leaves the R,H marginal unchanged. Apply the
same projector-block estimate to K tensor B_RH for arbitrary ||B_RH||<=1.
The decoded Pauli expansion gives

    ||rho_decoded,LHR(T)-rho_decoded,LHR(0)||_1
       <=18 Lambda integral_0^T sqrt(Tr[P_bad Phi_s(omega_Q)])ds
       <=18 Lambda T sqrt(C_out b_beta).

This retains joint tests of the records and the old reference; it does not
discard H to obtain a Gibbs product inequality. H's own storage faults and
work remain in the classical-record account. A coherent private-channel
version can insert stable projectors only in a comparison process. The
gentle projection/telescoping bound gives the conservative endpoint error
16m sqrt(B_n), preserving the stretched-exponential suppression.

Add e_in,e_out, the FT diamond error, calibration/controller failure and
the dynamical term inside the original epsilon/2^(a+2) stage allowance.
The incoming logical error is carried additively in the global composition;
it is not assumed to contract. With s=a+ln(1/epsilon)+1, choose the least
available BDL size above K s^(2/eta_mem). Its volume is polynomial in s;
the spatial exponent grows as s^2 while the time/allocation debt is O(s).
A fixed sufficiently large K meets every stage budget, including the
2a ln2 term. No new age-dependent noise rate is required.

### 11. A derived controller degree and physical invoice

For augmented degree D_A, put B=(D_A+1)^2,
h=ceil(log_2 B), u=h+2, v=ceil(log_2(3B)). The truncation and connected-set
count give P<=C M^u. To enclose a prefix partition ratio to relative
eta=1/(256P), truncate log Z(t) at
l=ceil(log_2(8M/eta)). The zero-free radius two gives log-tail bound
M 2^(-l). Connected-support Mobius inversion computes these coefficients:
for each connected U, enumerate W subset U and the occupied assignments
of W. This costs at most 3^|U| assignment tests; disconnected support terms
cancel by partition factorisation. Common-denominator rational arithmetic
and finite-series evaluation give the conservative bit-operation bound

    T_sampler<=C b_rate^4 M^kappa,
    kappa=(u+1)v+u+13.

The extra 13 allows root enumeration, eight powers of Taylor-order overhead
and four powers of the common-denominator bit size. All are fixed graph/
arithmetic bounds, not an assumed mixing exponent. The scalar exponential
is enclosed by a finite convergent-series computation at the same precision.

Let L_0 count the maximum recursive calls and physical operations in the
selected finite FT base gadget, with its classical-control procedure.
The recursion T_d<=L_0(T_(d-1)+1) gives degree
nu=ceil(log_2(2L_0)) in the accuracy index r. Set g=ceil(2/eta_mem).
Using n<=C s^g, M<=C n^2, b_rate,r<=C s, Gaussian CSS synthesis bounded
by C n^3, and a fixed O(n^2 s) calibration samples per endpoint gives

    K_c=max(2g kappa+nu+4, 3g+nu, 3g+4nu+1).


The finite base gadget also includes the classical control implementation.
Unroll its bounded syndrome/verification rounds and synthesize each Boolean
control on its fixed m_0 measurement bits by a truth-table circuit. Compute
three copies, with a private majority for each physical quantum-operation
control. A fault in one copy is outvoted; a final majority fault affects one
quantum location; corruption of a shared raw record is a faulty measurement
outcome already covered by the syndrome-gadget proof. An unprotected control
flag is never fanned out to many quantum locations. Padding prevents a bad
flag from extending execution. Count these finite circuits in L_0 before
the FT recursion. The degree above includes FT protection of the sampler
and calibration computation as well as the quantum gates.

The last term includes stabilizer-tableau simulation of the specified
private fault kernel. Operation count, workspace and new records are at
most C s^K_c. Retaining the entire prefix adds at most one degree. Serial
routing adds one workspace factor, giving at most C s^(2K_c+2) primitive
events. Total stock-times-duration, including every wait, guard and clock,
is then bounded by C s^(3K_c+3) in unit-duration units.

The classical activation/reset primitive supplies a physical upper invoice.
Use logical states 0,1 and bridge state e with H(B)=B|e><e|; upwards rates
are nu_0 exp(-beta B) and downwards rates nu_0. Its flip hazard is at most
nu_0 exp(-beta B), matching the existing barrier model. Since
0<=Tr(rho dH/dB)<=1, a barrier ramp's gross actuator work is at most its
total variation, for every state/fault trajectory. A bounded local unitary
has a Hamiltonian logarithm of norm at most pi in gate-time units, so
switching it on/off has a fixed finite drive invoice.

For reset, raise undesired levels by E and use their downwards reset jumps.
The wrong-state probability obeys dp_bad/dt<=-nu_0 p_bad+2nu_0 exp(-beta E),
and hence p_bad(t)<=exp(-nu_0 t)+2exp(-beta E). Taking B,E and the capped
reset duration O(s) meets the union allocation for polynomially many
controller operations. Ramps cost O(B+E), and the bounded-spectrum first
law bounds net reset heat/export by control work plus O(B+E). Power-capped
controller/export actuators have an O(s) realised invoice. Admitted extra
circuit faults remain in the FT account, not omitted from this thermal
estimate. Landauer supplies the lower floor, not this upper bound.

Reset duration and the linear per-primitive invoice add two conservative
degrees. Consequently the complete stage implementation in this device
model satisfies

    W_stage<=C s^(3K_c+5).

All nine HandoffCharge accounts, the complete history, failed attempts,
retirement and endpoints remain included. The existing deterministic cap
and TransferRate.polynomial_stage_bill give total transfer work <=C_T t.
TransferRate.join_complete_bill joins the existing sweep/archive bills for
every d_G>=1. The coefficient is independent of archive age and the unknown
logical input. These degree/invoice derivations are prose; the canonical
Checkpoint 12 source count is unchanged.


### Exact remaining physical correspondence

The compensation and controller construction above close the specified
private Pauli-interface application once the actual joint endpoint kernel
has the displayed microscopic factorisation, including its input layer,
classical-control faults and final feedback. That factorisation must be
identified with the installation's guarded operation. It is not implied
by the original local-stochastic inequality: two endpoint faults can share
a cause while every required faulty set still has probability at most
p^|S|. Their product of marginals would be the wrong physical channel.
No general correlated-fault certificate is declared from that substitution.

A retained joint-kernel compensation/holding construction can alternatively
discharge this correspondence. The earlier integrated-bad-weight route
also remains sufficient; static decoder halving alone does not supply its
physical-time transport. These are routes to the same full quantum,
arbitrary-reference, full-history target and original stage allowance.
The stage arithmetic, controller operation degree and retained-prefix G3
join need not be requested again. The installation's final kernel
identification remains unfinished; no global completion verdict, weakened
noise-domain replacement, merge or publication is issued.
