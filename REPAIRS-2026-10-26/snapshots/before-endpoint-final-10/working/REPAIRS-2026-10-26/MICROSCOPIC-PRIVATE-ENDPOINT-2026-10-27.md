# Microscopic private endpoint: reset and commuting feedback

27 October 2026. Constructive continuation of the endpoint obligation.
This supplies explicit finite generators for the private component. It
does not infer absence of a cross-device term from local-stochastic rates.
The whole installation still has to implement the stated decomposition.

## 1. Remove initial correlations from finite noise-label registers

Let tau_j=diag(t_j) be the specified full-rank distribution of a private
finite label register. Its dimension is four for one-qubit Pauli labels
and sixteen for two-qubit labels. Define the actual local jump operators

    L_(j,u,v)=sqrt(nu_j t_(j,u)) |u><v|.

Summing their dissipators gives exactly

    G_j(rho)=nu_j [tau_j Tr(rho)-rho].

The diagonal Hamiltonian E_(j,u)=-beta^(-1)ln t_(j,u), up to a constant,
has Gibbs state tau_j. The paired transition-rate ratio is t_u/t_v, so
the jumps satisfy detailed balance. Off-diagonal density entries decay at
the same nu_j rate. This is a calculated constant-dimensional generator,
not an inferred global mixing theorem.

Writing R_j(rho)=tau_j Tr(rho), R_j^2=R_j gives the exact semigroup

    exp(t G_j)=e^(-nu_j t) id+(1-e^(-nu_j t)) R_j.

It acts on the known auxiliary registers, never on the protected unknown
logical state. For disjoint registers, the G_j commute. Starting from an
arbitrary correlated label/reference state chi, the channel obtained by
resetting all m registers differs from the full product replacer by

    ||(product_j exp(t G_j))-product_j R_j||_diamond
         <=2 sum_j e^(-nu_j t).

This follows by a telescoping channel sum; each local replacer difference
has diamond norm at most two. The product replacer sends chi to
(product_j tau_j) tensor chi_reference. Thus initial auxiliary correlations
need not be assumed absent. Taking

    t_reset >=nu_min^(-1)ln(2m/delta_reset)

gives the required delta_reset error. For m polynomial in the age-stage
size and delta_reset exponentially small in a, this is O(s) time and the
existing capped reset invoice is polynomial. Zero target probabilities
can be replaced by a finite positive floor with total probability at most
delta_reset/4; the resulting channel error is separately budgeted.

## 2. Exact anisotropic feedback from a commuting Davies jump

For an X/idle slot of duration tau, use

    H_(X,b)=b pi X/(2tau),
    D_X(rho)=gamma_X(X rho X-rho),       b in {0,1}.

The jump X commutes with H_(X,b), and its Bohr frequency is zero for both
requests. The dephasing rate is the same fixed zero-frequency bath rate,
not a function fitted to the requested correction. Hence the actual slot is

    exp[tau(-i ad H_(X,b)+D_X)] = E_X Ad(X^b),
    E_X=(1-p_X)id+p_X Ad X,
    p_X=(1-exp(-2gamma_X tau))/2 <=gamma_X tau.

Use the corresponding Z/idle slot, with its own gamma_Z. Pauli conjugation
channels commute, so the complete two-slot residual law is

    e_I=(1-p_X)(1-p_Z), e_X=p_X(1-p_Z),
    e_Z=(1-p_X)p_Z,     e_Y=p_X p_Z.

It is anisotropic and independent of the requested Bell label. Both idle
slots have been retained. Its error mass is at most
(gamma_X+gamma_Z)tau. The endpoint rate threshold therefore gives a direct
inequality on these specified bath couplings and pulse duration.

Unlike an arbitrary label-dependent faulty correction, this explicit
residual E commutes with every Pauli. For any private decoder channel D,
including a coherent D, the complete outcome average is consequently

    E [ (1/4)sum_m Ad(P_m) D Ad(P_m) ].

It is a Pauli channel by the exact twirl. The classical command holder
uses the charged bounded controller; incorrect high-level commands are
part of its allocated failure branch. No O(p) command error is silently
declared exponentially small. A different controller with O(p) leaf errors
must use the full label-dependent formula and its corresponding private
Pauli-decoder certificate.

## 3. The full source model and what remains to identify

For the explicitly disjoint microscopic model, the joint endpoint
generator is the sum of these local terms, with each finite auxiliary
reset before use. Conditional pulse unitaries and local dissipators then
factor. Initial reservoir/label correlations contribute only the proved
delta_reset term. Resource/processor FT comparison errors and classical
command failures retain their own existing stage allocations. This is an
actual channel construction in that generator model, with all its rates
and error bounds written above.

Writing the physical generator as sum_j G_j is a substantive source
statement. If the installation has an additional common-cause generator
V_cross or a correlated fault instrument, it must remain in the model.
Resetting initial labels does not remove new shared faults after reset.
The exact component construction here must not be represented as a proof
that every original local-stochastic law has that decomposition. Either
the guarded microscopic implementation must supply it, or the actual
retained joint channel must be handled. This is the same maximal target,
not a new independent-noise replacement theorem.
