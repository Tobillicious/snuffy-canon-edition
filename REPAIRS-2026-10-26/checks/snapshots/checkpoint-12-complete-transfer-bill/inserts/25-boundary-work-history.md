

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

Working derivation for author review, 26 October 2026. The generic support lemmas are compiled; the source application and physical join retain their separate verification statuses. The target is the actual
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
block size (indeed at most the sum of the level sizes).

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

Helmuth–Perkins–Regts Theorem 2.2 and its Section 2.6 generalization then
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

The holding argument must keep its full reference norm and original fault
budget. A possible direct quantum bound uses positive operator domination:
for one logical qubit and any rho_LR, rho_LR<=2 I_L tensor rho_R, so an
independent gauge warm start of factor C gives an encoded-state bound by
4C rho_beta tensor rho_R. Complete positivity and stationarity preserve
this order during holding. Protected logical X,Y,Z then bound the decoded
joint state using the leakage projector, without assuming classical Pauli
jump trajectories. This application and the actual noisy transfer circuit
remain to be written out and checked against the existing G1/G2/G3 chain.

### Verification status

This note gives a proposed derived construction, with the counting theorem
used explicitly as a published algorithmic result. It is not a claim that
all implementation and physical application certificates are finished.
Next checks: audit every actual local constraint and its incidence bound
against both coarse maps; implement the factor-graph/component test on the
existing code; formalize the support, restriction and conditioning bounds;
join the actual reference-preserving transfer and complete bill. The failed
product/deletion assumptions are not reintroduced.

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

where Lambda(n)=max_i ||L-dagger A_i|| is polynomial under the published
local-generator bound. With b<=exp(-c n^eta), the exponent is halved and
remains sufficient for the existing doubling schedule. This is a prose
derivation, not an additional compiled trace-norm theorem.

### The physical application still to discharge

The ideal feed-forward construction and exact branch recovery do not certify
a noisy installation by themselves. The stage transfer must actually prepare
a covered gauge law, preserve the unknown input with arbitrary references,
and meet the original transfer-error budget at polynomial *pathwise* work.
A logically correct output from a generic noisy encoder does not by itself
prove pointwise domination of its gauge distribution. All preparation,
handoff, retained random and syndrome records, retirement, holding, guard,
controller and export costs remain in the full G3 bill. No expected-stock or
coarse-grained-history substitute is used. This application is unfinished;
no global completion or publication verdict is issued here.
