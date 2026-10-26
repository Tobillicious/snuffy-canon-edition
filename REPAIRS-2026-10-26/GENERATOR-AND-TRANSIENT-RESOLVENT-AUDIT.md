# Generator prefactor and transient-resolvent audit

26 October 2026. The author's geometric/resolvent attachments and Step 4
are preserved in inputs/, with hashes and provenance. The two geometric
attachments are byte-identical. This gives the usable analytical steps
without treating the unproved physical correspondence as a completed UPT.

## The generator prefactor is polynomial by a direct bound

For a bounded operator A and a Lindblad term with rate gamma>=0,

    D_V^dagger(A)=V^dagger A V - (V^dagger V A+A V^dagger V)/2,
    ||D_V^dagger(A)|| <= 2 ||V||^2 ||A||.

This follows by the triangle inequality and submultiplicativity. The factor
2 is needed: V=X, A=Z gives D_X^dagger(Z)=-2Z. For the Hamiltonian term,
||i[H,A]||<=2||H||||A||. The dressed Paulis have norm one and commute with
the stabilizer Hamiltonian, so that term vanishes here. Consequently

    Lambda(n) <= 2 sum_alpha gamma_alpha ||V_alpha||^2.

If there are at most J n frequency-resolved local jumps, rates at most
gamma_max and jump norms at most v, the bound is
Lambda(n)<=2 J gamma_max v^2 n. All constants are independent of archive
age. Bounded local check incidence and fixed interaction arity give a
bounded number of local energy changes per local coupling operator. Even
without the commutation identity, a sum of O(n) bounded Hamiltonian terms
adds only O(n) to the bound.

Thus the polynomial prefactor needs neither a locally supported dressing
nor a claim that only its spatial boundary contributes. No numerical check
weights 4, degree 12, or region size 72 are used without identifying those
constants for the actual BDL construction. This is a complete elementary
norm derivation at the stated local rate and multiplicity bounds. Those
rate bounds are separate from any bound on the thermal bad-event weight.

## Full-space gap versus a transient Green's operator

A finite Markov generator L has L1=0 in the observable convention. Hence
e^(tL)1=1 and integral_0^T e^(tL)1 dt=T1. A positive smallest nonzero
eigenvalue magnitude does not remove this stationary component.

For example L=[[-1,1],[1,-1]] has nonzero decay rate 2 and nevertheless a
divergent full-space Green's integral. Subtracting the stationary projection
can give a reduced resolvent, but its signed kernel does not automatically
majorize the positive trajectory weights needed here.

A useful sufficient certificate is instead a genuine killed process Q
whose surviving mass obeys, uniformly over allowed initial states,

    Pr_x[tau_abs > k tau_0] <= (1-alpha)^k,
    tau_0>0, 0<alpha<=1.

The Markov property gives this from the finite-time absorption bound
Pr_x[tau_abs<=tau_0]>=alpha. In the mass norm,

    ||integral_0^infinity exp(tQ)dt|| <= tau_0/alpha.

Every allowed state must reach the specified absorption set. A finite graph
or positive hopping rates alone does not establish that: a closed
odd-parity class can retain a defect forever under pair annihilation.
The required uniformity must include the code level and boundary conditions.
A finite list of actual local regions with explicit absorption paths could
certify this bound; no such all-level region/absorption list is in the reply.

## Correcting the creation-chain integration

Suppose, after the physical identification, a killed propagation segment
has norm <=M exp(-lambda t), lambda>0, and a creation vertex has norm <=a.
For a chain with k propagation gaps g_1,...,g_k after an initial creation
time t_0, positivity permits enlarging its ordered-time domain to
[0,T] times [0,infinity)^k. Its integrated occupation contribution is at
most

    integral_0^T dt_0 product_(r=1..k)
      integral_0^infinity M a exp(-lambda g_r) dg_r
      = T (M a/lambda)^k.

This is the valid source of a single factor T. It does not follow by
bounding first by T^k/k! times a resolvent norm and then replacing that
quantity by T times a constant^k. Initial-seed chains need their own
starting weights; INITIAL-SYNDROME-SPARSITY.md supplies an initial
occupation estimate under its stated fault-channel correspondence.

If a proved resummed topology count is <=B^m and k>=c m for each topology,
set r=M a/lambda<1. Summing k gives a bound r^(c m)/(1-r), and summing
m>=m_0 gives

    I_N(T) <= [T/((1-r)(1-q))] q^m_0,
    q=B r^c<1.

Additional polynomial anchor counts are retained in the prefactor. The
exponent is m_0[c ln(1/r)-ln B]. It cannot replace ln B by c ln B. To get
the intended stretched-exponential estimate one still needs the actual
witness-size lower bound and the uniform weighted activity/resummation
certificate. A distance bound on k does not alone control all topology
sizes m.

## The proposed spectral-gap perturbation is not generally valid

For nonnormal generators a Euclidean operator-norm perturbation does not
shift every decay eigenvalue by at most that norm. A concrete killed
generator is

    Q_0=[[-1,1],[0,-1]],
    Q_e=[[-1,1],[e,-1-e]],  e=1/16.

Both are valid sub-Markov generators, with an absorbing third state if
desired. Q_0 has decay eigenvalue 1. Q_e's slow decay is
(33-sqrt(65))/32<25/32. The perturbation norm is sqrt(2)/16<1/8, so the
claimed Weyl bound would give decay >7/8, a contradiction. The self-adjoint
Weyl estimate requires a justified common Hilbert norm and self-adjoint
restrictions; it is not a general Markov-generator gap estimate.

## The later boundary-trap proposal

The killed-resolvent input is preserved as
inputs/AUTHOR-KILLED-RESOLVENT-ATTACHMENT-2026-10-26.txt and its accompanying
message, with provenance. A boundary killing term K=gamma P_boundary does
not shift every eigenvalue by gamma. With unit hopping on two states and
killing rate one only at the second, the slow decay is
(3-sqrt(5))/2, not the old nonzero gap 2 plus the killing rate 1. A closed
class avoiding the boundary can retain a zero mode altogether.

There is also a necessary probability-accounting identity. For the
original neutral generator L and Q=L-K, variation of constants gives

    exp(tL)=exp(tQ)+integral_0^t exp((t-s)Q) K exp(sL) ds.

For a classical positive kernel, exp(tQ)<=exp(tL) entrywise. Dropping the
second, nonnegative term is therefore not an upper bound on the original
bad-event weight. In a first-exit construction one must retain the exit
kernel and its destination. Bad exits count as failures; other exits start
subsequent excursions. An artificial large trap rate cannot be selected
to make the actual physical failure small. The exact full process must
be reconstructed from the killed propagation and the physical exit flux.

## Remaining physical support

Provide the actual BDL region/ancestry construction, its jump operators and
rates, and a uniform bound on the complete excursion/exit kernels that
accounts for initial seeds. Prove the rare-event witness toll in that
construction. Its local transient resolvent and the positive exit/re-entry
terms must jointly yield the claimed activity bound; auxiliary killing
must not discard bad mass. The explicit integrated reference-state bound,
norm prefactor, stage allocation and complete polynomial-stage work
summation can then be applied without changing the maximal claim.

## The subsequent Feynman–Kac attachment

The attachment is preserved as
inputs/AUTHOR-FEYNMAN-KAC-ATTACHMENT-2026-10-26.txt. There is a correct
finite-dimensional derivative identity behind the proposal. It must use
the **full** generator L whose occupation is wanted. On density matrices,
use the completely positive trace-decreasing killing construction

    L_alpha(rho)=L(rho)-alpha {P_bad,rho}/2.

On the classical syndrome sector this is the ordinary killing potential.
Duhamel differentiation and trace preservation at alpha=0 give exactly

    -d/dalpha Tr[exp(T L_alpha)rho] at alpha=0
       = integral_0^T Tr[P_bad exp(sL)rho] ds.

Thus occupation can be represented without dropping mass. This identity
does not bound its derivative at zero using a resolvent at alpha=1. At zero,
the original stationary mode returns. The attachment also switches its
definition at alpha=0 to L_0-P_bad; these are different operators.

A one-state example isolates the issue: L=0 and P_bad=1 give
F(alpha)=exp(-alpha T), with finite resolvent 1/alpha for every alpha>0,
while -F'(0)=T. Finite killed resolvents at positive alpha do not imply a
small occupation integral.

There is a further obstruction to a uniform gap for killing only on a
rare bad set. For a reversible classical generator with stationary law pi,
the constant test function in the Rayleigh quotient gives

    lambda_min(-L+alpha P_bad) <= alpha pi(bad).

If pi(bad) is exponentially small, that killed gap cannot be bounded below
by a fixed positive constant. This does not obstruct rare-event protection;
it shows that this proposed route to its proof uses the wrong uniform-gap
claim. The local excursion process killed on annihilation and actual exits
is a different object and still needs its physical construction and flux
accounting. The Feynman–Kac identity preserves the quantity to be bounded;
it does not supply the missing creation/exit activity estimate.

## The return-kernel/source reply

The latest source reply is preserved in
inputs/AUTHOR-RETURN-KERNEL-SOURCE-REPLY-2026-10-26.txt. It does not yet
provide the required applicable theorem or estimate.

1. The displayed transition formula has no condition that the chosen edge
   sends sigma to sigma-prime. As written its row is not a transition
   probability distribution. A corrected embedded jump chain must include
   the actual destination, accepted jump rates and holding/rejection
   probabilities; its continuous-time occupation also needs the waiting
   times. It cannot replace the physical generator by degree normalization
   without proving that correspondence.
2. For fixed Delta_0 and ell>1, Delta_0/ell^j tends to zero. It does not
   give a strictly positive level-independent lower bound c_0. Increasing
   a fixed microscopic coupling does not change this limiting fact.
3. The stated BDL Section 4.2 citation supplies a local coarse-graining
   construction, not the asserted hierarchical Poincare inequality. The
   primary-source search found Hastings and Haah's 2021 paper
   [Dynamically Generated Logical Qubits](https://arxiv.org/abs/2107.02194).
   Its searchable text contains none of Davies, Sobolev or spectral gap.
   No exact title/theorem was supplied for a different result; that generic
   attribution is not used as a certificate.
4. The alternative direct argument asserts the same final bound on
   I_a(T). Initial density alone does not supply its evolution, joint
   occupation tails, or contour activity. The already derived initial
   footprint-aware estimate is retained; it is not replaced by independent
   per-check fault factors.

The primary BDL source checked for this audit is
[the v1 paper, Section 4.2](https://arxiv.org/html/2605.10943v1#S4.SS2).
The remaining pātai asks for an actual kernel calculation or a precise
applicable source theorem establishing the required excursion/occupation
bound. The finite norm, integration, budget and work results do not confer
that physical theorem by association.
