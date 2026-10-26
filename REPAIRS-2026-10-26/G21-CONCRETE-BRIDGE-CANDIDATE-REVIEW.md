# Review of the proposed concrete G.21 bridge and fibre sampler

26 October 2026. The supplied attachment and accompanying message are
preserved under inputs/ with their provenance. They are candidate
derivations, not compiler receipts. This review keeps the current G.21
ideal construction and the maximal UPT target unchanged.

## 1. The noisy-state interface is still unproved

The displayed 18 t Lambda sqrt(C b) estimate is the already derived ideal
warm-start holding estimate. The new text does not show that the physical
output retains its initial domination.

For an actual residual channel N after the ideal preparation, complete
positivity gives

    rho_actual,LR <= 4C N(rho_beta) tensor rho_R,
    rho_actual,LR(t) <= 4C Phi_t(N(rho_beta)) tensor rho_R.

Stationarity says Phi_t(rho_beta)=rho_beta. It does not replace the
different state Phi_t(N(rho_beta)) by rho_beta. This is the precise missing
transition in the proposed concrete application.

One sufficient support would be a proved polynomial domination of the
actual prepared state by rho_beta. Another is the already stated direct
integrated bad-weight bound for omega_a=E_a(I/2). The latter avoids assuming
that the actual circuit factors through a single input-independent N.

The correct reference comparison includes preparation and decoding:

    ||[(Dec Phi_t E_a) tensor id_R](rho_LR)-rho_LR||_1.

The physical semigroup and a logical input must not be subtracted without
identifying their spaces. Initial decoded error and separately excluded
failure branches remain in the original stage allowance.

## 2. Use the correct bad projector

P_bad in the holding estimate is the complement of the protected
stable-syndrome sector for the dressed logical observables. It is not
generally the complement of the zero-syndrome ground codespace.
Correctable thermal excitations are allowed.

For example, with m independent unit-energy checks and z=exp(-beta)>0,
the thermal zero-syndrome probability is (1+z)^(-m). The probability outside
that codespace tends to one as m grows; it is not exp(-c n^eta).
The existing stable-projector argument in G.21 is retained.

The memory exponent eta is the positive exponent of the memory
construction. Identifying it with d_G-1 and requiring d_G>=2 would remove
the required d_G=1 work case. That substitution is not adopted.

## 3. The attachment does not replace the completed ideal sampler

For the exact conditional fibre law,

    K(sigma|s)=pi(sigma)/pi_coarse(s),  s=r(sigma),

so exact reassembly gives

    mu(sigma)/pi(sigma)=q(r(sigma))/pi_coarse(r(sigma)).

There is no additional Z_global/Z_local factor after this normalization.
An approximate conditional sampler would instead need its own controlled
pointwise decision-path factor, as in the current construction.

The excess partition function is defined by excess energy. The full fibre
weight is W(s)=exp(-2 beta |s|) Z_exc(s). Those two quantities must not be
given the same prefactor a second time.

The proposed inequality

    exp(C n^(d_G-1)) <= A n^p

does not hold for fixed positive C and d_G>1 as n grows: its logarithmic
left side grows faster than log A+p log n. Subextensive free energy is not
a polynomial density bound.

Further, a circuit fault threshold does not itself prove a small-activity
criterion for the conditional thermal fibre gas. Gibbs activities are
controlled by the actual energy/fugacity and degeneracy; these must be
established for that representation. Compatible polymer families also
cannot be sampled as independent contours.

Current G.21 already avoids these issues: it uses the entire deterministic
history, proves E(Gamma)>=|Gamma|/4, verifies uniform incidence and the
Kotecky–Preiss bound, applies HPR counting to deleted-polymer submodels,
and uses finite self-reduction with fixed-bit coins. Its ideal factor is
at most 4 per CSS sector and 16 jointly. This source-audited construction
is kept; the new conditional-excess sketch is not substituted for it.

## 4. Stage allocations and physical estimates are different

Choosing weights omega_s with sum omega_s<=1 allocates an error budget.
It does not prove the actual drift or fault probability meets that budget.
The drift integral in the supplied text still needs a specified generator,
observable/decoded norm estimate and a proved bound on its integrand.

The established code-size choice is polynomial in the age-stage index
a+log(1/epsilon). Setting n proportional to 2^a instead turns a polynomial
in n into a polynomial in age, and does not automatically satisfy the
original t^d_G work ceiling. TransferRate's verified argument requires
the actual complete stage invoices to be polynomial in the stage index.

## 5. Cost theorem attribution remains important

TransferRate proves finite-invoice summation bounds. It does not define
a physical entropy current R_trans or derive a work upper bound by
multiplying that current by the Landauer floor. The physical upper invoice
is the complete nine-account HandoffCharge, including failed attempts.

Likewise StageSchedule.total_with_transfers sums error allowances, not
work charges. The reset term weighted by P_err is expected work and does
not replace the realised pathwise invoice. The current complete ledger
already accounts for those distinctions.

## Result

The attachment and message do not yet discharge the actual noisy-state
holding application. The completed ideal sampler, reference algebra and
upper-cost accounting remain available. The remaining patai is the actual
physical domination/occupation estimate, with initial error and full costs.
No canonical Lean source, target quantifier or original budget was changed.
