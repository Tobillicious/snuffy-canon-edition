

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
The ideal sampler's source application is audited in prose; the actual noisy physical
transfer and holding join remain unfinished. The target is the actual
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
kernel-checked solver in this repository. The actual noisy physical transfer
and holding certificate remains to be supplied.

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

### The physical application still to discharge

The ideal feed-forward construction and exact branch recovery do not certify
a noisy installation by themselves. The actual transfer must preserve the
unknown logical input with arbitrary references, bound its initial logical
error and physical failure branches, and produce an output whose holding
meets the original stage allowance at polynomial pathwise work.

The remaining proposed contour route needs an actual generator/trajectory
representation and a proved bound on its rare creation events after neutral
and downhill motion has been summed. Bounded support of one jump does not
confine successive jumps to that support. Nor does a bound B^|Gamma| rho^k
converge merely from B rho<1 when the relation of |Gamma| to the rare-event
count k has not been proved. The proposed confinement proof is inadequate:
a valid neutral multi-defect junction in the existing finite BDL implementation
crosses four single-defect hopping regions. The proposed gap-based
replacement did not derive its uniform constants. A direct-history route
can instead be used, but it must transport the initial joint syndrome
occupation estimate under the actual Phi_s, or bound I_a(T) directly.
Deterministic halving across decoder levels is not a probability factor
one-half, and does not establish a time-uniform stochastic law. The static
history polymers above do not by themselves give that nonequilibrium
holding estimate. A killed local
excursion process must retain its actual exit flux. A Feynman–Kac derivative
at zero exactly represents occupation, but a resolvent bound at positive
killing does not bound that derivative. In particular, killing only on a
rare bad set cannot be assigned a constant gap by adding the trap rate.

All preparation, handoff, retained records, retirement, holding, guard,
controller and export charges remain in the G3 bill. No expected-stock,
classical-payload or discarded-history substitute is used. The maximal
protection target is unchanged; this physical application is unfinished.
