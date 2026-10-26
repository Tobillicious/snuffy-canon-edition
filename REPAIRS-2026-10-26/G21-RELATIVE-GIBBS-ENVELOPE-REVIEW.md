# Residual-noise and Gibbs-envelope candidate review

26 October 2026. Both author messages are preserved under inputs/, with
provenance. This records corrected algebra and sufficient estimates; it
does not add an unproved physical lemma to the canon.

## 1. Recovery must actually preserve the thermal state

Logical recovery does not by itself imply R(rho_beta)=rho_beta. An ordinary
syndrome reset changes the thermal syndrome distribution. If a different
recovery, such as thermal re-preparation after decoding, is intended, its
actual definition and noisy implementation must be supplied.

If R is CPTP and R(rho_beta)=rho_beta has been proved, the valid identity is

    N(rho_beta)-rho_beta = R[E(rho_beta)-rho_beta].

Hence trace-norm contractivity gives

    ||N(rho_beta)-rho_beta||_1 <= ||E(rho_beta)-rho_beta||_1.

This supplies no code-distance suppression without an additional result.
The proposed Kraus subtraction by 1/rank(E) is not justified: subtraction
weights over Kraus indices must sum to one, and Kraus representations are
not unique. Channel rank is not an arbitrary representation's Kraus count.

A physical fault rate and code distance can bound decoded logical failure
when the actual correction construction is proved. They do not automatically
make the entire physical gauge state O(p^D)-close to thermal equilibrium.

## 2. Correct additive-to-relative conversion

Let rho be positive definite, Delta=sigma-rho Hermitian, and
||Delta||_infinity<=delta. Then

    Delta <= delta I,
    I <= rho/lambda_min(rho),
    sigma <= [1+delta/lambda_min(rho)]rho.

If the proposed additive estimate delta<=C p^D ||rho||_infinity is assumed,
the resulting envelope is

    sigma <= [1+C p^D kappa(rho)]rho,
    kappa(rho)=lambda_max(rho)/lambda_min(rho).

The displayed intermediate inequality I<=kappa(rho)rho is itself false
for a generic normalized full-rank state. On its minimum-eigenvalue vector,
the right side has eigenvalue lambda_max(rho)<1. The corrected inequality
uses 1/lambda_min(rho), as above.

For a Gibbs state,

    kappa(rho_beta)=exp[beta(E_max-E_min)].

For n independent unit-energy checks this is exp(beta n). This is a
size-dependent factor, not a universal constant. Restricting to a proposed
low-energy subspace requires a proved tail and complete accounting of the
discarded complement; it cannot silently change the target state or its
reference guarantee.

## 3. The correct relative quantity

A direct sufficient envelope lemma would control the Gibbs-weighted norm:

    ||rho_beta^(-1/2) [N(rho_beta)-rho_beta] rho_beta^(-1/2)||_infinity <= eta.

It then follows algebraically that N(rho_beta)<=(1+eta)rho_beta. An upper
bound on the largest eigenvalue of that relative operator is sufficient
as well. Relative entropy or ordinary trace/operator norm alone does not
supply this estimate without the minimum-eigenvalue loss.

This weighted estimate must be proved for the actual preparation noise.
It is stronger than necessary: the direct integrated bad-weight route in
the existing patai remains available. No requirement to prove an
exponentially accurate return to full thermal equilibrium is added to UPT.

## 4. The new generator assumptions are not established

- A circuit channel R composed with E is not automatically the exponential
  of a time-independent Lindblad generator.
- exp(tau L)=I+tau L is only a first-order expansion, with a remainder.
- A fault-tolerance threshold does not itself prove a positive uniform
  Liouvillian/log-Sobolev constant for a specified physical generator.
- A spectral gap alone does not give the asserted inverse bound in an
  arbitrary operator norm; the space, norm and transient/reduced inverse
  have to be specified.
- The stationary state rho_N and the finite-time image N(rho_beta) are
  different quantities. A perturbative fixed-point formula is not yet
  a bound on that image.
- If the same full generator L really satisfies L(rho_beta)=0 and
  N=exp(tau L), then N(rho_beta)=rho_beta exactly. A noise-perturbed
  generator needs its own analysis; these premises cannot be interchanged.
- D is code distance. It is not the work dimension d_G. The proposed
  O(p^D) physical perturbation norm is not derived merely by choosing D.

The Sympy output exp(C_0*p**d*t) only prints the expression. It does not
verify these assumptions or their constants.

## 5. What a proved envelope would supply

For a single residual map after the ideal preparation, suppose a bound
N(rho_beta)<=K rho_beta is actually proved. Complete positivity and Gibbs
stationarity then transport the ideal order inequality to

    rho_actual,LR(t) <= 4 C K rho_beta tensor rho_R.

The existing protected-Pauli argument bounds subsequent decoded drift by
18 t Lambda sqrt(C K b_beta). Initial decoded error and physical failure
branches remain separately charged. A thermal fixed-point test does not
bound the initial logical error: a logical Pauli can preserve the Gibbs
state while changing a reference-entangled logical state.

If a nonthermal channel is applied repeatedly during holding, each such
operation and its envelope factor must be included. From per-step factors
1+eta_s the product is at most exp(sum eta_s). The desired factor 1+epsilon
requires sum eta_s<=ln(1+epsilon), with the original stage fidelity and full
maintenance work still met. This is not implied by writing the product.

## Result

The corrected relative conversion is recorded. The physical perturbation,
weighted envelope or integrated bad-weight estimate has not been derived
by the supplied arguments. The original full-strength UPT target and
existing G.21 constructions are retained. No canonical Lean source changed.
