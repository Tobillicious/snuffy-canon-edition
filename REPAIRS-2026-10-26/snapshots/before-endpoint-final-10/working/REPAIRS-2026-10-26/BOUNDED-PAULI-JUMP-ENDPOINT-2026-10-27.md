# Joint endpoint kernel from bounded Pauli jump causes

27 October 2026. This extends the compensated channel beyond independent
output qubits. It is a calculated generator model, not a deduction from
local-stochastic marginals alone.

Let P_e be physical Pauli products supported on at most k endpoint qubits,
with at most ell cause terms incident on a check. For a specified exposure
interval t_e, take the actual endpoint generator term

    L_e=gamma_e(Ad(P_e)-id).

Pauli conjugations commute even when the underlying Paulis anticommute:
their scalar phases cancel. Also Ad(P_e)^2=id. Therefore the complete
channel of this joint generator is exactly

    exp(sum_e t_e L_e)=product_e [(1-p_e)id+p_e Ad(P_e)],
    p_e=(1-exp(-2gamma_e t_e))/2 <=gamma_e t_e.

The output qubits are correlated. The factorisation is over the specified
bounded jump causes, not over qubit marginal laws. It follows from the
given finite generator and requires no global mixing or spectral-gap claim.
The same result holds for time-dependent scalar gamma_e(t), replacing
gamma_e t_e by its integral, when the Pauli axes remain fixed.

Each factor has the exact inverse

    [(1-p_e)id-p_e Ad(P_e)]/(1-2p_e).

Its identity coefficient is positive and its nonidentity relative activity
is p_e/(1-p_e). Use one fault-colour vertex per cause in the existing signed
history graph. If the cause flips at most w syndrome checks and each check
has bounded cause incidence, the augmented degree remains constant.
The same positivity, counting, joint-occupation and rate-precision proofs
apply with max_e[p_e/(1-p_e)]z^(-w) in the activity bound. Thus shared
bounded Pauli jumps are included without replacing their joint law by
a product of output marginals.

For a pulse interval, the formula also holds when every active jump Pauli
commutes with the control Hamiltonian. The explicit X/idle and Z/idle
feedback construction has this property for its respective longitudinal
single- or multi-endpoint Pauli causes. In that case the control unitary
factors from the calculated noise channel. Noncommuting pulse-time noise
must instead be propagated through its actual time-ordered channel.

At a stable syndrome, a bounded-support P_e can be split into at most k
single-qubit Paulis for the initial logical-error estimate. A partial split
is a bounded syndrome translation. The uniform signed-gas occupation bound
also holds after each such bounded translation, by including that fixed
translation as a background in the same local energy bound. Constants may
depend on fixed k,w,ell; no system-size energy ratio appears. This retains
the polynomial prefactor times stretched-exponential endpoint error.

This generator identifies an explicit sufficient joint endpoint law and
substantially widens the product-qubit construction. A generic correlated
local-stochastic instrument need not have this commuting-cause generator.
Nor does a common fluctuating rate become a deterministic gamma_e(t)
without retaining its conditioning. The physical source must identify the
actual cause generator, including any remaining cross or memory terms.
