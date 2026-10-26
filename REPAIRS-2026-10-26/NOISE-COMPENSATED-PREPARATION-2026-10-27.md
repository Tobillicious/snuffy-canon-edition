# Constructive noise compensation for thermal preparation

27 October 2026, Pacific/Auckland. New constructive development in response
to the author's request to work through the physical obstruction.

The remaining application is the complete physical preparation/handoff
circuit. This note derives a way to remove the residual-noise obstruction
for a specified product Pauli channel, and identifies one concrete circuit
primitive with that channel. It does not assume that all preparation faults
already have this form. The maximal UPT, arbitrary references, full history,
original stage budgets and complete pathwise work ceiling remain fixed.

Twelve algebra statements in two candidates have separate targeted
compile/kernel/axiom PASS receipts.
They are development candidates, outside the 192-module canonical receipt.
The positivity and sampling argument below is a prose derivation; its
general counting routine is not a newly implemented FPTAS or Lean theorem.

## 1. Change the input law to account for the physical noise

Let pi_z be the target joint CSS syndrome law on the actual valid binary
syndrome space C, with weight z^|sigma|/Z. For a specified residual Pauli
noise channel N, seek a positive probability law q satisfying

    N q = pi_z.

Prepare q, rather than pi_z, before the noise acts. If the finite sampler
produces mu <= K q, positivity of N gives the actual output bound

    N mu <= K pi_z.

This is an input-distribution adjustment. It does not apply a nonpositive
inverse quantum operation to the unknown logical input, and it requires no
global Davies mixing bound. The inverse law must be proved nonnegative and
efficiently sampled; a formal matrix inverse alone is insufficient.

## 2. An explicit residual channel from the three-CNOT handoff primitive

Implement the same-code physical register swap by CNOT(0,1), CNOT(1,0),
CNOT(0,1) on each disjoint source/target qubit pair. Suppose each CNOT is
followed by an independent two-qubit Pauli depolarizing error with total
nonidentity probability p, each of the 15 Paulis having probability p/15.

Two-qubit depolarization is invariant under unitary conjugation. The three
errors therefore combine to a depolarizing factor (1-16p/15)^3 on the pair.
After tracing out the old source, the target has single-qubit Pauli noise
with total nonidentity probability

    p_out = (3/4) [1 - (1-16p/15)^3].

This channel identity also holds with an arbitrary reference: complete
depolarization of the pair, followed by tracing the source, replaces the
target by I/2 and leaves the reference marginal. Disjoint pairs give a
product of these output channels. This describes the swap primitive under
the stated circuit fault model; it does not certify a change of code or the
preceding preparation circuit.

An exact enumeration checks all 16^3 fault patterns. The counts by fault
weight 0,1,2,3 are [1,9,171,843] for target I and [0,12,168,844] for each
target X,Y,Z. The resulting polynomial agrees identically with the formula
above; `swap_target_rate` checks that scalar identity in Lean.

## 3. Exact inverse of a local Pauli syndrome channel

For one physical qubit, let A and B translate a joint syndrome by its X-
and Z-error syndrome vectors. They are commuting involutions; Y translates
by AB. At total nonidentity rate p,

    N_p f = (1-p) f + (p/3)(A f + B f + AB f).

For p != 3/4 its exact inverse is

    R_p f = [(1-p/3) f - (p/3)(A f+B f+AB f)] / (1-4p/3).

The Lean candidate proves N_p R_p f=f, preservation of total mass by both
maps, and the one-sided output bound. It does not assert inverse positivity.
For independent qubit channels, compose the inverses in reverse order.
Their syndrome translations commute in the present model. Write

    u_i = p_i/(3-p_i),
    a_i = (1-p_i/3)/(1-4p_i/3).

The candidate input law is the following explicit finite expression:

    q(sigma) = (product_i a_i)/Z
       * sum_{F} (-1)^|F| (product_{i in F} u_i)
                    z^|sigma + syndrome(F)|.

F chooses at most one nonidentity Pauli colour at each location. Algebra
gives Nq=pi_z and sum q=1. Positivity requires the next argument.

### Unequal Pauli rates and bounded-support gate channels

The private-output construction in FT-PRIVATE-OUTPUT-BRIDGE-2026-10-27.md
produces general Pauli rates. Let q=(q_I,q_X,q_Z,q_Y), sum q=1, with
nonidentity mass p<1/2. On the four Pauli characters the eigenvalues are

    lambda_0=1,
    lambda_1=q_I+q_X-q_Z-q_Y,
    lambda_2=q_I-q_X+q_Z-q_Y,
    lambda_3=q_I-q_X-q_Z+q_Y.

They lie in [1-2p,1]. The inverse coefficients are the inverse four-point
Fourier transform of (1,1/lambda_1,1/lambda_2,1/lambda_3). In particular,
r_I=(1+1/lambda_1+1/lambda_2+1/lambda_3)/4>=1. In the convolution l1 norm,
the Neumann series gives

    ||R-I||_1 <= 2p/(1-2p),
    |r_P/r_I| <= 2p/(1-2p) for P != I.

Use a_i=r_I and the signed colours u_(i,P)=r_P/r_I in the finite sum.
The KP proof uses absolute values and is unchanged. Scaling the forward
nonidentity rates continuously to zero keeps these bounds and a_i>0, so
the positivity homotopy is also unchanged. PauliInterface.lean proves the
four-character inverse, composition, mass formula and domination algebra.

For a uniformly depolarizing r-qubit gate with g=4^r Pauli labels, the same
group-average calculation gives

    R=[(1-p/(g-1))I-(p/(g-1))sum_(P!=I) T_P] / [1-gp/(g-1)].

There are g-1 fault colours at that location. For a two-qubit CNOT this is
15 colours and u=p/(15-p). The augmented graph remains bounded-degree
when propagated support and check incidence are bounded. The native
one-replacement CNOT circuits verify those supports in finite instances;
they do not establish bounded bare fault spread across all replacements.

## 4. Uniform positivity from the existing full history

Use the zero-preserving deterministic syndrome history already constructed
in G.21. Allow deterministic local correction/activation indicators as
additional history coordinates when needed for decoder instability. There
is still exactly one history per finest syndrome. Bounded local scope,
bounded incidence and zero-preserving local computation bound its occupied
support by K_0 |sigma|, with K_0 a fixed gadget constant (the original
syndrome-only bound is K_0=4).

Let w bound the number of checks flipped by one Pauli colour, and let the
number of noise locations touching a check be bounded independently of
level. These are properties of the specified output-noise model, not of
an arbitrary long circuit. Add three fault-colour vertices per location to
the history graph. At most one colour is allowed at a location. At each
finest check, connect the history variable and all incident fault colours
into a clique. Keep the original constraint cliques. The resulting graph
has a fixed maximum degree D_A.

For sampling prefixes, fix a compatible union h_0 of already selected
history components and exclude specified remaining components. Remove the
fixed variables. Write sigma_0 for its finest syndrome and h for a
compatible remaining history. Its finest syndrome sigma_h is disjoint from
sigma_0. Relative to the background, the energy obeys

    |sigma_0 + sigma_h + syndrome(F)| - |sigma_0|
       >= |sigma_h| - w |F|.

For each connected augmented component gamma, its history portion is a
union of valid original components. Thus |h_gamma| <= K_0 |sigma_h,gamma|.
The absolute value of its signed activity is bounded by

    |w_gamma| <= z^(|h_gamma|/K_0)
                      (u_max z^(-w))^|F_gamma|
                <= b^|gamma|,
    b = max(z^(1/K_0), u_max z^(-w)).

The clique scopes make energy additive across separated augmented
components. Conversely, compatible standalone components form an allowed
history/fault assignment. This is an exact signed polymer representation of
the finite sum for q and each of its sampling-prefix masses, including the
factor z^|sigma_0|. Negative activities are counting devices, not sampled
physical probabilities.

Put B=(D_A+1)^2 and choose

    b <= 1/[8 e B (D_A+2)].

There are at most B^l connected supports of size l through a fixed vertex.
For |t|<2, rescale each activity by t^|gamma|. The incompatible activity sum
is bounded by

    (D_A+1)|gamma| sum_{l>=1} (B e |t| b)^l < |gamma|.

This is a uniform Kotecky--Preiss criterion, including every deletion and
sampling-prefix model. It gives a zero-free disk of radius 2 in t. It
also holds while the real noise parameters decrease continuously to zero.
Each real prefix partition function is positive at zero noise and cannot
cross zero, so it remains positive. In particular every q(sigma)>0. Along
with the inverse mass identity, this proves q is a probability law under
the displayed explicit small-noise inequality.

That inequality is a requirement of this candidate support construction.
Its physical attainment has not been inserted as an additional premise of
the maximal UPT or claimed for the whole installation.

## 5. Polynomial sampling without sampling the signed auxiliaries

The polynomial has degree at most the number M_A of augmented vertices.
Connected supports can be listed in exp(O(l+log M_A)); their local
constraints, energy and allowed-component membership can be evaluated in
that time. Activities are monomials in t with computable coefficients.
Together with the proved zero-free disk, these are the hypotheses for the
partition approximation in [Helmuth--Perkins--Regts, Theorem 2.2 and
Lemma 2.8](https://arxiv.org/pdf/1806.11548). The application is to signed
partition counting; their positive sampling conclusions are not assumed
for the signed auxiliary variables.

Here is the required positive sampling reduction. A prefix event that a
particular original history component G is present can be summed over the
unique augmented component containing G. The cluster bound gives

    |Z(components compatible with gamma)/Z| <= exp(|gamma|).

With s=B e b, its conditional probability is therefore at most
sum_{l>=1} s^l < 1/4, uniformly in prefixes. A union bound over positive
physical history events then gives

    Pr_q(some history component has size > L)
       <= M_A sum_{l>L} l s^l.

Each augmented component contains at most |gamma| relevant history
components, which accounts for the factor l. Take L=O(log M_A) so this
bound is at most 1/2. Conditioning q on that event's complement costs a
pointwise factor at most two. The P small history components can be listed
in polynomial time.

Visit that list once. For a compatible candidate G, compute its conditional
inclusion probability as 1-Z(exclude G)/Z(current prefix). Both partition
functions are real and positive, although represented by signed sums.
Use certified relative approximations of accuracy eta=1/(256P), take an
upper estimate of the exclusion ratio, and round the inclusion probability
down to a fixed dyadic grid of mesh at most eta. Inclusion probability is
never increased and is reduced by at most 9 eta. Since the exact exclusion
probability is at least 3/4, an exclusion branch is inflated by at most
1+12 eta. The full path factor is below exp(12P eta)<2.

Consequently the finite-coin sampler has law mu <= 4q. It uses a fixed
polynomial number of decisions and deterministic polynomial counting calls;
there is no expected-time rejection loop. Applying the physical channel
gives the actual output law Nmu <= 4pi_z.

### Joint occupation, including partial output-noise layers

The signed representation also supplies the endpoint logical-error bound
directly. It is unnecessary to assume that a large unstable witness is
already one component of an unaugmented history graph.

Suppose a signed gas has |w_gamma|<=b^|gamma|, at most B^l size-l
polymers through a vertex, and the KP cavity bound

    |Z(compatible with Gamma)/Z|<=exp(sum_(gamma in Gamma)|gamma|).

Its marginal on physical histories is positive, as proved above. Put
R=2 B e b<1. For any set A of history coordinates, including any finest
syndrome coordinates,

    Pr_q[A occupied] <= R^|A|.

Here is the finite covering argument. In a configuration with A occupied,
select exactly its augmented polymers meeting A. They cover A. Sum the
remaining polymers, apply the cavity bound and take absolute values. The
result is bounded by the sum of products (e b)^|gamma| over covering
families. To enumerate such a family, take the first uncovered vertex of
A and choose its polymer. After a choice of size l, at most l marked
vertices have been removed. Inductively bound the remaining covering sum
by R to the number of remaining marks. Since R<1, the total is at most

    R^|A| sum_(l>=1) B^l (e b/R)^l = R^|A|.

Dropping compatibility only enlarges this nonnegative majorant. The empty
mark set has covering sum one, completing the induction. This is a joint
occupation bound, not merely a bound on the mean defect density.

For a partial physical output-noise layer, retain all inverse-colour
vertices and add the already-applied forward-colour vertices. A forward
Pauli channel factors as (1-p)[I+sum_(P!=I) p_P/(1-p) T_P]. Its colours
have absolute activities bounded by p_P/(1-p) z^(-w). Each location now
has at most two bounded colour groups; support and incidence remain
uniformly bounded. Apply the same KP and covering bounds with the enlarged
fixed graph constants. The marginal is positive because it is a physical
channel applied to positive q. This proves the occupation bound uniformly
for every partial output layer, including unequal rates and an approximate
compensation model satisfying the same small-activity bound.

Apply the existing BDL finest-syndrome witness enumeration with R in place
of thermal fugacity. That enumeration uses probabilities of joint finest
occupation; our bound supplies them without a Gibbs assumption. In terms
of the existing decoding-graph degree Delta, within-level degree Delta_l
and maximum local-complex size M_l, a sufficient ratio is

    theta(R)=2(Delta+1)^2 [(1+R^(1/4))^M_l-1]^(1/(1+Delta_l^4)) <= 1/2.

This is a fixed inequality. First choose a positive R_* satisfying it.
With the enlarged graph's B, choose b below both the KP threshold and
R_*/(2Be). It suffices to choose

    z <= b^K_0,
    |u_(i,P)| <= b z^w,
    p_(i,P)/(1-p_i) <= b z^w

for the inverse and forward colour groups. All are fixed local-parameter
requirements; no precision exponential in system size is introduced.
The witness-size threshold is 2^(k-1), giving

    B_n <= polynomial(n) exp(-c n^eta)

for the unstable probability in both sectors. This is an estimate for the
bounded preparation layer. Long-time holding is handled by the compensated
Gibbs envelope, not by asserting that this sparse law is preserved in time.

## 6. Reference correlations and the initial logical error

A Pauli channel permutes syndrome sectors and leaves their maximally mixed
logical factor unchanged. Hence the actual output on logical I/2 satisfies

    (N Enc_mu)(I/2) <= 4 rho_beta.

The existing Pauli-twirl/reference inequality then gives, for every joint
logical/reference input,

    (N Enc_mu tensor id_R)(rho_LR) <= 16 rho_beta tensor rho_R.

Gibbs stationarity now applies to the actual prepared output envelope. This
is the step missing when one merely reused Enc_pi's ideal domination.
The existing holding conversion yields dynamic error at most
36 Lambda T sqrt(b_beta), in this model. It does not make the initial
logical error vanish.

The joint-occupation argument above bounds B_n uniformly over all partial
physical output-noise layers. It uses the witness correspondence in
[BDL, sections 5.1--5.3](https://arxiv.org/html/2605.10943), rather than an
assumed confinement of neutral defects. In the exactly compensated model,
the law after a segment is also the appropriate partial inverse q_J;
the sampler's law is at most 4q_J. At a stable syndrome,
the next single-qubit Pauli preserves the decoded logical/reference state.
A union bound over m physical noise locations gives

    e_initial <= 8 m B_n.

This includes possible logical faults; no syndrome-only conclusion is
substituted for them. Combining it with the existing dynamic reference
estimate leaves polynomial prefactors times (1+T) exp(-c' n^eta).
The original polynomial stage-size choice and separate failure allocation
can then meet epsilon/2^(a+2) at T=2^a. This is a derived consequence of
the specified residual-channel model, not yet a proof that the entire
physical encoder has that model.

### Finite-precision noise rates

Exact output rates are not necessary. Let hatN_i be the nominal Pauli
channel and N_i its actual channel. Let epsilon_i be the l1 difference of
their four probability vectors, and let w bound a syndrome shift. In the
weighted norm ||f||_pi=max_sigma |f(sigma)|/pi(sigma), each translation has
norm at most z^(-w). If hatp_i(1+z^(-w))<=1/2, the Neumann estimate gives

    ||hatN_i^(-1)||_pi <= 2,
    ||N_i hatN_i^(-1)||_pi <= 1+2 z^(-w) epsilon_i.

All syndrome translations commute. For the positive law hatq satisfying
hatN hatq=pi and a finite sampler mu<=4hatq,

    Nmu <= 4 exp(2 z^(-w) sum_i epsilon_i) pi.

Thus sum_i epsilon_i<=z^w/2 costs at most the fixed factor e. An error
O(1/m) at each of m locations is sufficient; exponentially accurate global
rate estimation is not required. For a specified independent Pauli gate
model, private Clifford interfaces can be simulated using stabilizer
tableaux to sample their effective error labels in polynomial time. A
fixed sample count O(m^2 log(m/delta_cal)) per location gives the required
precision except with probability delta_cal, with constants depending on
the fixed z and footprint. This is a bounded stage invoice. A physical
calibration implementation must also control measurement error and drift;
neither is established merely by this mathematical robustness estimate.

The forward-colour occupation argument still bounds all intermediate bad
weights in this approximate model. Calibration failure is a separate
branch, adding at most 2delta_cal to the reference trace-norm error.

## 7. What the finite and Lean checks cover

The exact script checks both syndrome sectors jointly on existing BDL
seed matrices, including physical Y faults. On the 13-qubit seed it checks
all 4,096 valid joint syndromes. In the positive examples the inverse law
sums to one and Nq=pi exactly. A conditioned input with pointwise factor two
retains that factor after N. A larger-noise example produces negative
inverse entries, confirming that positivity cannot be assumed without a
bound. A separate seed check tracks the full logical Pauli channel and a
Bell reference, including nonzero initial logical error and its bound by
the actual intermediate bad weights.

The three-CNOT calculation enumerates all 4,096 local fault patterns.
The twelve targeted Lean statements check inverse algebra, mass, domination,
the general four-character inverse and the scalar swap polynomial. They
have zero compile/kernel output and
standard axioms only. They do not kernel-check this cluster-expansion
argument or the complete physical preparation circuit.

## 8. Complete physical application still to construct

The companion BDL-REFINEMENT-CIRCUIT-2026-10-27.md constructs the actual
one-replacement CSS CNOT encoder and replays its stabilizer action. The
companion FT-PRIVATE-OUTPUT-BRIDGE-2026-10-27.md constructs a fresh encoded
Bell-resource/private-decoder route to product Pauli output channels in
its specified interface model, retaining all old gauge/reference
correlations. General correlated local-stochastic faults have not silently
been replaced by independent noise. The complete routed/controller device
and its admitted endpoint fault model, final correction noise, calibration
and fixed small-noise inequalities still require their physical join.

Under that physical correspondence, the new sampler and its retained
records have polynomial pathwise stage work. The existing TransferRate/G3
join then applies with all original accounts and every admitted d_G>=1.
No repeated active correction throughout 2^a is introduced. No new global
completion verdict, canonical Lean count, merge or publication follows
from this development note.
