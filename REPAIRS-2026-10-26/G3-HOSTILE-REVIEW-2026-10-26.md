# Hostile review of the proposed G3 synthesis and direct-history route

26 October 2026. The author's new direct-history and four-vulnerability
drafts are preserved verbatim in inputs/, with message provenance. This
review retains the maximal UPT and the already established proof chain.
It does not substitute expected work, classical records, or a smaller
domain for the existing target.

Checkpoint 11 already passed 191 modules / 1,150 names. Checkpoint 12 now
passes all 192 modules / 1,158 names, including the eight TransferRate
results. A PASS certifies the actual theorem statements and premises; it
does not certify the additional physical claims in these new drafts.

## The direct-history proposal: precise remaining step

The route can be pursued without a spectral-gap estimate. The existing
HistoryPolymer.paired_history_bound proves a deterministic support bound
on the complete decoder history of one syndrome. Its halving is across
code levels, not physical holding time and not a probability of one half.

For a history component Gamma of size m, the finest syndrome must occupy
at least m/4 specified coordinates. If the physical syndrome law at time s
has a joint occupation bound K theta^|A|, then a union bound over at most
M B^m supports yields the desired static large-component estimate when
B theta^(1/4)<1. The initial-law proof supplies such a bound at s=0 under
its stated preparation/fault correspondence. The needed support is its
propagation under the actual holding generator, or a weaker direct bound
on the integrated bad weight. Neither deterministic halving nor the
Feynman–Kac representation proves that propagation.

A proposed factor 2^(-c m) is not supplied by a deterministic halving
inequality. Likewise the full occupation integral uses Phi_s, not a killed
semigroup with its exit contribution omitted. Feynman–Kac gives a derivative
at zero; a finite positive-killing resolvent does not bound that derivative.

The exact compiled modules were checked:

- HistoryPolymer: halving/support, component restriction, truncation and
  finite decision-path comparisons.
- ThermalEncoding: orthogonal branch compression/recovery, including an
  arbitrary reference register.
- TheoremEightLyapunov: clipped reserve deficit, capacity, replenishment,
  solvent-cycle energy accounting and iteration. It has no Feynman–Kac
  theorem or Davies occupation bound.

The density-matrix operator norm ||rho||_infinity is also not defect
density. A pure code state has norm one and zero defects. Occupation must
be expressed with the commuting violated-check projectors or their joint
moments. The initial-sparsity theorem here is about those events.

No numerical constants 4.23 or 1.85 have been calculated for an actual
specified return kernel. The proposed recurrence with division by ell^zeta
allows decay when 0<zeta<1. The later withdrawal of that gap route is
retained; the current sufficient target is a physical occupation bound.

## 1. Reset expectation does not give the pathwise bill

If X_k indicates an allowed reset, its realised cost is
sum R k^(d-1) X_k. The proposed sum weighted by P_err(k) is its expectation.
A finite expected sum, or even almost-sure finiteness, does not give the
fixed deterministic complete-work constant required by G3.

There is a simpler pathwise bound for the proposed one-reset-per-shell
policy: since X_k<=1,

    sum_(k<=t) R k^(d-1) X_k <= R t^d,  d>=1, t>=1.

For multiple attempts use the deterministic invoice/cap construction of
TransferRate and the complete local wave charge, including all failed
attempts. No convergence of expected reset debt is needed for this work
ceiling. The old, stronger G3CompleteBill.cumulative_charge_bound already
meters every local cost, the fixed startup charge and its allowed rollback.
It must not be replaced by the new expected-cost argument.

## 2. Correct shell sum, including d=1

For nonnegative alpha,beta and integer t>=1,

    sum_(k=1..t) [alpha k^(d-1)+beta] <= (alpha+beta)t^d.

This uses k^(d-1)<=t^(d-1) and t<=t^d. The draft's sharper-looking expression
drops beta t into beta t^(d-1), which fails at d=1. For example alpha=beta=1
and t=10 gives actual cost 20, while that displayed bound is 12. The simple
bound above and the existing compiled cumulative-charge theorem retain
every d>=1; the project is not restricted to d=2,3.

Each disjoint shell is charged when processed. This sum does not process
all earlier interiors again at every physical time step. Actual overlap,
rollback and retry work must remain in the per-wave invoice; the bounded
wave-count/age conversion is already in valid_bill_bound_in_age.

## 3. Stock, boundary size and information capacity are different

Instruments.card_box counts the box, (2r+1)^d. For r>=1 the cubical boundary
count is (2r+1)^d-(2r-1)^d. Neither count alone proves that an arbitrary bulk
Hilbert space can be losslessly encoded into a smaller boundary Hilbert
space. An isometry requires source dimension at most target dimension.
The actual maintained source/code, exact decoder and capacity correspondence
must be used; a Lieb–Robinson propagation bound is not that correspondence.

The new Stream Two also changes the live-stock bound to
I0+c sum_(k<=s) k^(d-1). If that accumulated stock is held at a fixed
per-bit-step rate, its holding bill can grow as t^(d+1). This is the same
stock/flux issue already settled in ARCHIVE-HOLDING-DISPOSITION.md and
G3ArchiveStock.retained_stock_quadratic. It is not accepted as new progress.

The existing live-stock route uses stock(s)<=I0+c(s+1)^(d-1), with retired
transcripts either losslessly recomputable from retained data or their
correction-entropy resets fully charged. G3ArchiveStock.live_stock_bill
then gives holding <=gamma(I0+c)t^d. The new sampler's entire growing stage
journal is retained and charged separately on its doubling schedule.

A linearly growing code distance is not derived by a site count. The actual
circuit/outer-code construction and its fault model must supply its
distance and complete work. The established tolerant sweep and redundancy
route are retained rather than replaced by that new assertion.

## 4. Operator algebra is already handled by the isometry

For E^dagger E=I,

    (EAE^dagger)(EBE^dagger)=EAB E^dagger,
    [EAE^dagger,EBE^dagger]=E[A,B]E^dagger.

The identity of the image algebra is P=EE^dagger. An encoded Pauli squares
to P on the ambient boundary space, not to the ambient identity. This
preserves the code algebra; it does not identify a guard projection with
a Pauli observable.

As a state encoder rho->E rho E^dagger is CPTP. Its Heisenberg adjoint is
B->E^dagger B E; calling EAE^dagger the adjoint channel conflates the
directions. DecoderRetraction.boundary_observable_mul,
boundary_observable_commutator and historical_word_on_code already prove
the relevant algebra and ordered-history transport. ThermalEncoding
proves the branch-mixture reference recovery. These supports are carried
forward; a closed-Lie-algebra slogan supplies no extra certificate.

## 5. Landauer is a lower bound, not a device-work upper bound

QuantumLandauer.quantum_landauer and quantum_guard_one already derive the
entropy/heat floor. They do not show every correction costs exactly one
erased bit, or that heat is at most k_B T ln 2 per bit. A conditional Pauli
correction can be unitary; the measurement/control record's reset and its
conditional entropy must be counted.

Writing R=eta_eff k_B T ln 2 with eta_eff>=1 defines an efficiency factor.
It does not bound eta_eff or the other physical costs. A complete upper
invoice must include gates, guards, clocks, cooling, retained records,
controller and export. The existing Bennett and WorkBilling constructions
already retain those charges. No new axiom equating the Landauer floor
with total device cost is introduced.

Finite expected heat from rare rollbacks also does not bound the total
heat from routine correction over an infinite horizon. Routine work may
grow as t^d while remaining within G3. Bath stability requires the already
charged export/maintenance balance, not a false assertion that all
historical correction heat has finite cumulative total.

## 6. Startup absorption is valid; a speed limit is not an upper clock bound

A fixed complete bootstrap invoice B_boot is absorbed because
B_boot<=B_boot t^d for t>=1. The existing G3 cumulative charge includes its
fixed field. The actual finite startup program and device timing give a
completion bound. An upper propagation speed v_max gives a lower possible
traversal time r/v_max; it does not prove completion by that time.
This correction does not reopen the settled geometric bootstrap argument.

## 7. Correlated bursts and lifetime

CorrelatedCeiling.correlated_stress_ceil and damage_local_stochastic bound joint
fault-set probabilities. They do not make damaged locations independent.
In that module k is a shock's maximal footprint, not code distance. The
draft's conflation reverses the interpretation of its rate formula.

A fixed one-window leakage probability is not an infinite-age error
budget. Use the existing tolerant-sweep results and summable stage budgets
with their actual hypotheses. Replacing the admitted burst footprint by an
independent noise model, or invoking refresh alone, does not prove that
join. The full X3 channel/traffic argument is retained; no old
Lieb–Robinson shortcut is substituted for it.

## 8. Constant tracking

For each fixed lambda>0 and integer d>=1 the expected series
S=sum k^(d-1)exp(-lambda k) is finite. The displayed integral-only bound
S<=Gamma(d)/lambda^d is not valid for all admitted d. At d=4 and lambda=ln2,
S=sum k^3/2^k=26>6/(ln2)^4.

A safe elementary bound follows by integrating (x+1)^(d-1)exp(-lambda x)
on each interval [k-1,k]:

    S <= sum_(r=0..d-1) binom(d-1,r) r! /lambda^(r+1)
      = (d-1)!/lambda^d sum_(s=0..d-1) lambda^s/s!.

This establishes an explicit finite expected constant, not a pathwise
reset ceiling. For the latter use the complete invoice bound above.

Strict p<p_threshold gives a positive decay exponent for each fixed
hardware rate. It does not give a uniform lower bound on that exponent
over rates approaching threshold. Similarly age independence does not
prove that every hardware coefficient is small or uniform in dimension.
Input-state uniformity at fixed payload capacity differs from a constant
uniform over unbounded initial payload sizes. I0 and the actual hardware
parameters remain explicit in the existing bill. A dimensionless error
epsilon is not itself a work coefficient unless a cost conversion is given.

## Correct master accounting connection

For the admitted complete local wave invoices, including their reset
allowances, the existing G3 theorem gives C_S t^d. Live archive holding
gives gamma(I0+c)t^d. The full stage/attempt invoices, including the whole
retained journal, give C_T t. Fixed startup/endpoints are charged once and
absorbed at t>=1. Thus a valid combined coefficient is

    C_full=C_S+gamma(I0+c)+C_T+B_extra,

where B_extra contains only genuinely additional fixed charges, with no
double counting of the startup/endpoints already in C_S or C_T. Then
W(t)<=C_full t^d for every d>=1. This is the completed accounting join at
the actual local invoice bounds. It does not prove success or holding of
the physical noisy transfer output. That remains the precise patai.

The maximal protection target, full retained history and arbitrary-reference
fidelity remain fixed. The proposed hostile defenses are not adopted as a
publication-ready substitute for the existing stronger ledger.

## Final supplied physical-time recurrence

The subsequent reply is preserved as
inputs/AUTHOR-PHYSICAL-SUPPORT-RECURRENCE-REPLY-2026-10-26.txt. The scalar
solution of w_(t+1)<=delta w_t+kappa for 0<=delta<1 is correct. Its premise
is not derived for the actual Davies holding process. Decoder-scale
halving does not establish this physical-time contraction or a fixed
global pathwise injection cap. If an active correction process is intended,
its actual operations and full holding work must be identified and charged.

The next step again assumes Pr(w_T>=n)<=K exp(-c n^eta). A geometric
isoperimetric inequality alone does not define or bound a probability law.
Finally eta=d_G-1>0 fails at d_G=1 and is not the BDL memory exponent used
in G.21. The original positive memory exponent and every admitted d_G>=1
are retained. The pātai remains the actual occupation/transport bound;
no new Lean assertion or global completion verdict is added.
