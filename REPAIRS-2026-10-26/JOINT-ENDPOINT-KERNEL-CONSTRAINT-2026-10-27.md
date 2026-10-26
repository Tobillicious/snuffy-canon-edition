# Joint endpoint kernel constraint and residual allowance

27 October 2026. Final local integration support for G.21. These are
derived channel constraints and error bounds. No measured installation
kernel, new canonical Lean theorem or global UPT completion is asserted.

## Exact finite joint law

The comparison preparation must specify the complete joint fault-path law,
including input interfaces, private decoders, Bell outcomes, both feedback
slots and idles, classical commands, reset flags and retained records.
Independent qubit marginals alone do not specify this law. A sufficient
output law includes the local Pauli channels already derived, composed
with the following bounded common causes:

    N_0 = product_e [(1-p_e) id + p_e Ad(P_e)],
    p_e = (1-exp(-2 integral gamma_e(t) dt))/2 < 1/2.

Every P_e has fixed bounded physical support, syndrome footprint at most w,
and bounded incidence per check. The Pauli axes are fixed in the actual
control interaction frame. This follows exactly from the specified
generator sum_e gamma_e(t)(Ad(P_e)-id), since all its conjugations commute.
During pulses, commutation with the control Hamiltonian suffices. Otherwise
the actual time-ordered channel must be propagated or charged below.
Common random rates must retain their shared conditioning or be integrated
into the joint kernel; substituting their means is not this identity.

Its cause inverse is [(1-p_e)id-p_e Ad(P_e)]/(1-2p_e). Require the existing
KP and witness inequalities on the augmented graph containing both CSS
sectors and all inverse/forward cause vertices. In particular,

    max_e p_e/(1-p_e) <= b z^w,
    z^(1/K_0) <= b,  b <= [8eB(D_A+2)]^(-1),
    theta(2Be b) <= 1/2.

Any additional local four-Pauli factors retain their existing inverse and
forward activity bounds. The same weighted-norm estimate permits total
probability-vector rate error sum_e epsilon_e=O(1), hence O(1/n) per cause
when their number is O(n). No independence between the two syndrome sectors
is assumed for a cause that flips both.

For a k-qubit cause, split it into at most k single-qubit Paulis only to
bound initial logical error. A partial split translates the syndrome by a
fixed v of weight at most w_split. The existing occupation estimate gives

    Pr[A subset supp(sigma+v)] <= R_0^(-w_split) R_0^|A|.

Indeed occupation of A outside supp(v) is necessary. Thus the extra factor
C_split=R_0^(-w_split) is independent of n. The witness bound and endpoint
union bound keep their stretched-exponential suppression, with a factor
at most k C_split. No full-system Gibbs energy ratio is introduced.

## Residual bound with the records and reference retained

Let E_0 and E_act be the nominal and actual preparation instruments with
the same retained-record output H. Include any source noise memory in the
input/dilation when it can be correlated with the protected state. Require
a bound uniform on the admitted joint inputs, rather than a data-only
marginal comparison. Put delta_ep=||E_act-E_0||_diamond. For any subsequent
CPTP holding/decoder F and any reference,

    ||(F E_act tensor id)(rho)-(F E_0 tensor id)(rho)||_1 <= delta_ep.

There is no factor 2^a for a discrepancy confined to preparation. Two
useful, explicit certificates for delta_ep are as follows.

* If both maps use the same branch channels V_lambda and input-independent
  joint probabilities K_act(lambda),K_0(lambda), including all correlations,
  then delta_ep <= sum_lambda |K_act(lambda)-K_0(lambda)| = 2 TV(K_act,K_0).
  This follows by the triangle inequality and ||V_lambda||_diamond=1.
  State-dependent outcome laws require the full instrument norm instead.
* If the joint nominal and actual generators on the same space generate
  CPTP propagators and differ by V(t), their Duhamel identity is

      U_act(t,0)-U_0(t,0)
        = integral_0^t U_act(t,u) V(u) U_0(u,0) du.

  Complete trace-norm contraction therefore gives delta_ep <= integral
  ||V(u)||_diamond du. An omitted Hamiltonian contributes at most
  2 integral ||H_cross(u)||/hbar du; an omitted dissipator gamma D_L
  contributes at most 2 integral gamma(u)||L(u)||^2 du. A shared memory
  is retained in this joint generator, not replaced by independent baths.

Add bounds over disjoint residual segments only; do not double-charge
faults already covered by the FT comparison or named failure accounts.
Cap the sum at two. If a residual coupling remains during holding, its
integral runs through that holding interval of length 2^a as well. The
preparation-only contraction argument does not remove that interval.

## Unchanged stage budget

Write B_a=epsilon/2^(a+2). A concrete sufficient allocation is

    e_in + e_out + e_dyn + delta_FT + delta_reset
      + 2 delta_cal + 2 delta_ctrl,record + delta_joint <= B_a,

with each of the eight displayed terms at most B_a/8. The counter-cap
comparison in the gross reset construction belongs to delta_ctrl,record
at its stated diamond/probability conversion, not to a free extra budget.
Incoming logical error is added separately and is never assumed to shrink.
All previously retained history and arbitrary reference tests remain in
these instruments. The existing size schedule supplies the represented
model terms; it does not establish the residual joint-kernel bound.

For example, an unmodelled generator bounded by v_a over a total short
exposure tau_a has residual at most tau_a v_a. The allocated condition is
tau_a v_a <= epsilon/2^(a+5). For a finite stochastic endpoint kernel it
is enough that TV(K_act,K_0) <= epsilon/2^(a+6). These requirements apply
to the unrepresented residual, not to the fixed represented Pauli rates.

No installation values for K_act or V have been supplied by the finite
checks. Without a source bound the universal residual bound is two; the
positive excess max(0,e_model+delta_joint-B_a) may therefore remain.
The exact remaining support is now quantitative: identify the complete
joint cause/instrument model, or prove its residual fits the displayed
unused allowance, and bind the capped controller/export device to the
same execution. This does not narrow the original fault domain.
