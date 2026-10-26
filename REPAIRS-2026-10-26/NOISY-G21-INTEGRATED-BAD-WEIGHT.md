# The reference-uniform join from an integrated bad weight

26 October 2026. Derived continuation of G.21. This records what follows
from the author's Duhamel/contour proposal and isolates the estimate still
requiring physical proof. No protected-state contraction or preparation
mixing is used. The unknown logical input and arbitrary references remain.

Let omega_N=N(rho_beta) for the actual residual preparation channel. Write
b_N(s)=Tr(P_bad Phi_s(omega_N)). Let C be the ideal joint-syndrome warm-start
factor (C<=16 in G.21). On the correctly implemented branch, if the physical
residual channel is the input-independent N in the setup, complete positivity
gives the initial and evolved order bounds

    rho_actual,LR <= 4C omega_N tensor rho_R,
    rho_actual,LR(s) <= 4C Phi_s(omega_N) tensor rho_R.

Identifying the actual circuit with that residual-channel model is part of
the physical certificate, not an automatic consequence of logical success.
For a separate implementation-failure branch of uniformly bounded weight
delta_fail, add 2 delta_fail to the final trace-norm estimate. Merely
observing a small initial decoded error on that branch would not control
its later holding error.

Let A_X,A_Y,A_Z be the existing protected dressed Paulis, with
P_good L^dagger(A_i) P_good=0, and Lambda=max_i ||L^dagger(A_i)||. For any
reference test T_R with norm at most one, the bad-block decomposition in
G.21 gives

    |Tr[(L^dagger A_i tensor T_R)rho_actual,LR(s)]|
       <= 6 Lambda sqrt(C b_N(s)).

Integrate each coefficient and use trace-norm duality in the decoded Pauli
expansion. The identity coefficient vanishes because the reference marginal
is unchanged. On the covered residual-channel model, if e_0 bounds the
initial decoded joint-state error, then

    e(T) <= e_0 + 18 Lambda sqrt(C) integral_0^T sqrt(b_N(s)) ds
         <= e_0 + 18 Lambda sqrt(C T I_N(T)),

where I_N(T)=integral_0^T b_N(s) ds. The second inequality is
Cauchy–Schwarz. This is a bound uniform in the reference dimension. It
compares **decoded** logical-reference states, not the entire physical
thermal state with its initial state.

Consequently an actual bound

    I_N(T) <= K T exp(-c n^eta)

would imply

    e(T) <= e_0 + 18 Lambda sqrt(CK) T exp(-c n^eta/2).

The square root halves the exponent and leaves a stretched-exponential
bound. With a separately bounded failure branch, write
E_0=e_0+2 delta_fail as the combined preparation allowance. For T=2^a,
allocating E_0<=epsilon/2^(a+3) and the displayed dynamic term
<=epsilon/2^(a+3) gives exactly epsilon/2^(a+2), the original stage ceiling.
A polynomial Lambda(n) is absorbed by a fixed fraction of the
stretched-exponential exponent. Thus n can remain polynomial in
a+log(1/epsilon), as in the original schedule.

## What the latest proposal has not yet established

The reply sets a spacetime contour weight

    w(Gamma) <= (C rho*)^|Gamma| exp(-c' n^eta')

and then sums it. It does not derive this inequality from the actual
Davies jump operators, rates, constrained BDL code and correlated residual
fault distribution. That inequality, together with the event-to-contour
map and multiplicity/time-measure bounds, is the missing physical support.
Kotecky–Preiss can control a specified polymer gas after its activities and
representation have been established. It does not itself produce those
activities for a nonequilibrium trajectory from N(rho_beta). The equilibrium
history polymers in G.21 are not yet such a spacetime expansion.

The proposed Duhamel step also drops the size of V=L-L_0. Trace-norm
contractivity alone cannot give ||V rho||_1<=Tr(P_bad rho). For example a
two-level jump from bad to good at rate lambda, applied to the pure bad
state, has ||V rho||_1=2 lambda while its bad weight is one. Rates have units
of inverse time. Coherences can require square-root bad-weight bounds as
well. A projected generator must separately be shown CPTP, and its decoded
action on all protected reference states identified. The existing protected-
observable proof above avoids needing those additional assertions.

The remaining request is therefore precise: derive I_N(T), or the stronger
pointwise b_N(s) bound, for the actual noisy preparation in the stated
code and generator, plus e_0. Supply the contour construction and activity
proof if that is the chosen route. The integration, arbitrary-reference
conversion, stage allocation and polynomial work summation are already
available. The maximal UPT conclusion is not narrowed while this support
is obtained.

## The two subsequent contour replies

Both replies are preserved verbatim, with provenance, in `inputs/`:
`AUTHOR-SPACETIME-JUMP-WEIGHT-REPLY-2026-10-26.txt` and
`AUTHOR-NEUTRAL-RESUMMATION-REPLY-2026-10-26.txt`.

The second correctly separates uphill creation from neutral/downhill jumps.
It still needs two actual estimates. First, bounded **support of one jump**
does not imply bounded connected components of the neutral transition graph:
successive overlapping local moves can carry a defect arbitrarily far.
The number 72 must be identified and shown uniform for the actual code
levels before it can be used as a confinement or resummation bound.

Second, the proposed bound is B^|Gamma| rho^k(Gamma), with B>1. The condition
B rho<1 controls this series only if a relation between |Gamma| and the
number k of rare events is proved, or if the neutral paths have already
been summed with their correct holding-time factors into a constant^k
bound. Counting neutral paths by B^m and assigning each weight at most one
does not do that summation. The asserted k>=c d addresses the desired
rare-event count but is itself the missing BDL-specific geometric lemma;
it also does not control arbitrarily large m for fixed k.

The continuous-time path measure must retain ordered jump times, no-jump
survival factors, initial defects and the spatial/time anchors. For example,
at a state with neutral exit rate lambda, the zero-neutral-jump probability
over duration T is exp(-lambda T), and k jump-time integrals have simplex
volume T^k/k!. Replacing all those factors by one is not a uniform
resummation proof. The norm Lambda=max_i ||L^dagger A_i|| used in the decoded
drift need not bound individual microscopic jump rates; conserved logical
observables can have Lambda=0 while gauge jumps remain nonzero.

The exact tail, once a valid resummed activity bound and witness threshold
m_0 are established, is elementary:

    sum_(m>=m_0) m q^m
      = q^m_0 [m_0/(1-q)+q/(1-q)^2],   0<=q<1.

One must also count spatial anchors unless they are already included in
the definition of q or the prefactor. Polynomial prefactors are absorbable
in the target stretched-exponential estimate. The missing support is the
creation-event/witness correspondence and its uniform neutral resummation,
not that final geometric tail or the stage-budget arithmetic.

## Generator norm and the subsequent killed/Feynman–Kac inputs

The norm prefactor is now derived directly:
Lambda(n)<=2 sum_alpha gamma_alpha||V_alpha||^2=O(n) for O(n) uniformly
bounded local jump classes. The norm-one dressed Paulis commute with H.
The factor two is retained; locality of the dressing's boundary is not
needed. The full proof is in `GENERATOR-AND-TRANSIENT-RESOLVENT-AUDIT.md`.

That audit also preserves and examines the later attachments. A genuine
transient excursion process has a finite Green's operator once uniform
absorption has been proved. The actual boundary-exit flux must remain in
the expansion. Artificial killing cannot be used to discard it. The
Feynman–Kac derivative at zero is a valid representation of occupation,
with the full generator and a correctly defined killing superoperator;
a positive-killing resolvent does not itself bound that derivative.

Accordingly the new inputs are recorded as candidate supports and corrected
analytical identities, not as a completed BDL spacetime activity theorem.
The remaining certificate is still the uniform bound on I_N(T) for the
actual noisy output, together with its initial logical/failure allowance.

## A direct certificate for any actual preparation channel

The reference argument need not require a factorization through a residual
channel N. Let E_a be the actual CPTP preparation map from one protected
logical qubit, including its physical noise, and put omega_a=E_a(I/2).
Pauli twirling gives rho_LR<=2 I tensor rho_R; complete positivity gives

    (E_a tensor id_R)(rho_LR) <= 4 omega_a tensor rho_R.

Repeat the protected-Pauli argument with
I_a(T)=integral_0^T Tr[P_bad Phi_s(omega_a)] ds. For an initial decoded
error allowance e_0 it gives

    e(T) <= e_0 + 18 Lambda sqrt(T I_a(T)).

This version includes arbitrary reference correlations and seed-dependent
physical control already inside E_a. Separately excluded failure branches
still add their uniform trace-norm allowance. It moves no burden onto a
classical replacement of the quantum state. The actual preparation's
initial decoded error and its integrated bad weight still require proof.

## Latest replacement proposal

The entropy-weighted excursion reply is preserved in
`inputs/AUTHOR-ENTROPY-WEIGHTED-EXCURSION-REPLY-2026-10-26.txt`. It correctly
allows the neutral multi-defect junction demonstrated by the finite
witness. Its bound W_exc(m)<=constant^k exp((kappa-c_gap)m), however, is
asserted rather than derived from a specified return kernel. The condition
c_gap>kappa is exactly the new uniform excursion-decay support required.
A temporal spectral gap does not automatically give the stated spatial
path-length decay, and an abstract polymer convergence theorem applies
only after its activities and full trajectory correspondence are proved.
The proposal is recorded as a candidate route; the physical certificate
remains open at this precise inequality.
