# Endpoint Pauli feedback and controller invoice

27 October 2026. This derives the endpoint channel in the specified private
Pauli circuit model and an explicit degree bound for its finite controller.
The maximal target and original stage allowance are unchanged. Independence
of private fault sources is a model correspondence to establish for the
installation, not a consequence of a local-stochastic marginal bound.

## 1. Physical feedback, including label-dependent anisotropy

Represent I,X,Z,Y by the additive group F2^2. Let d_j(e) be the physical
private-decoder Pauli law at output j. The Bell outcome m is uniform.
Let c_j(eta|m) be the law of the error in the two classical correction bits.
Realise the requested correction by two fixed slots: X or idle, then Z or
idle. Let x_(j,b) and z_(j,b) be the physical post-slot Pauli error laws,
including the idle when b=0. Each is a four-entry probability vector.

The slots are fixed; an identity request does not remove a clock tick or
its noise. Conjugation of a Pauli by the requested second Pauli changes
only its phase. Consequently their combined residual law is

    r_(j,bx,bz)(f)=sum_(u+v=f) x_(j,bx)(u) z_(j,bz)(v).

When the private decoder and feedback faults have their specified private
conditional product law, the complete endpoint distribution is exactly

    q_j(a)=1/4 sum_(m,e,eta,f: e+eta+f=a)
                 d_j(e)c_j(eta|m)r_(j,m+eta)(f).

Thus the actual endpoint channel is N_j(rho)=sum_a q_j(a)P_a rho P_a.
Neither isotropy nor equality of the four feedback kernels is needed.
The erroneous decoded control bit is a Pauli error, not an omitted charge.
All variables in this expression are entries of the physical finite
fault-path kernel; there is no fitted spectral constant.

If p_D, p_C, p_X and p_Z bound the nonidentity probabilities of these four
parts, the union bound gives

    1-q_j(0) <= p_D+p_C+p_X+p_Z.

For the existing private-interface estimate p_D<=c_FT p, two readout bits
of error at most p and two feedback slots of error at most p give the
conservative bound (c_FT+4)p. The constant c_FT is that of the selected
fixed FT scheme, not a newly assigned numerical value. A directly counted
fault-path kernel may replace this conservative bound.

For a fixed Clifford gadget, propagate each local Pauli fault through its
remaining ideal gates and prescribed syndrome processing. Summing the
products of its actual gate-kernel entries gives d_j. The three-CNOT swap
already supplies an enumerated example; depolarizing noise is only its
special symmetric case. A private stabilizer simulation computes estimates
of d_j in polynomial time and retains every simulation coin and record.

Separate output gadgets with independent private fault sources give
N=product_j N_j. Shared causes require their joint kernel: multiplying
their marginal q_j is not an admissible substitution. This is the precise
remaining model boundary of this preparation route.

## 2. Derived local acceptance inequality

Let D_A,w,K_0 be the already constructed augmented-graph degree, maximum
syndrome footprint and history support constant. Put B=(D_A+1)^2. Choose
the fixed b and z by the explicit KP and witness inequalities in the
compensation note. Define

    p_star=b z^w/[2(1+b z^w)].

Then p_out<=p_star implies

    2p_out/(1-2p_out)<=b z^w,
    p_out/(1-p_out)<=b z^w.

These are respectively sufficient inverse-colour and forward-colour bounds.
The endpoint's acceptance check is the derived, checkable inequality

    p_D+p_C+p_X+p_Z <= p_star.

It is not established for a device merely by p<p_threshold. No new
numerical hardware performance is claimed. Finite-precision rates reserve
half the available slack and use the existing weighted-norm error bound.

## 3. Explicit counting-controller degree

Let M>=2 be the number of augmented history/fault vertices and set
h=ceil(log_2 B), u=h+2, v=ceil(log_2(3B)). The fixed truncation choice
L=ceil(log_2(4M)) is sufficient under the existing activity slack. Counting
connected supports then gives P<=C_P M^u candidate history components, with
C_P determined by B. Use relative counting precision eta=1/(256P).

Every queried partition polynomial has degree at most M, constant term one
and no zero in |t|<2. Factoring over its zeros bounds the tail of its log
Taylor series after l terms by M 2^(-l). It therefore suffices to use

    l=ceil(log_2(8M/eta)) <= (u+1)log_2 M+C_l.

There is an explicit finite coefficient algorithm. Enumerate connected
vertex sets U with |U|<=l. The support-Mobius formula for log Z uses the
coefficients of log Z[W] for W subset U. For each W, enumerate its occupied
assignments, test the existing local constraints and excluded-component
list, and form its partition polynomial. Across all W subset U this costs
at most 3^|U| assignment tests. Formal-series arithmetic recovers the
required log coefficients. Disconnected support terms cancel because the
partition function factors across disconnected induced supports.

At most M B^j connected j-sets occur. With rational local coefficients of
bit length b_rate, a common product denominator for the M local parameters
keeps the exact truncated arithmetic polynomial in M,b_rate,l. Using
schoolbook arithmetic, the deliberately loose bound

    T_count <= C b_rate^4 M^13 (3B)^l

is sufficient: it allows four powers of the common-denominator bit size,
eight powers for finite-series operations, and root/enumeration overhead.
The final scalar exponential can be enclosed to relative precision eta
by its convergent series, with the same polynomial allowance. Over all
P decisions, fixed coins and comparisons, this yields

    T_sampler <= C b_rate^4 M^kappa,
    kappa=(u+1)v+u+13.

No unexplained FPTAS degree is inserted into the invoice. The constants
depend on the fixed graph and local table sizes, independently of age.
The finite small-graph coefficient check is separate from the general
proof of this bound; it is not labelled a complete FPTAS implementation.

## 4. FT, calibration, routing and retained records

Let L_0 be the maximum number of recursive calls and physical operations
in any fixed base FT gadget, including its bounded syndrome/feedback
procedure. For concatenation depth d, a conservative recurrence is
T_d<=L_0(T_(d-1)+1). The accuracy index r is within a fixed factor of 2^d.
Thus nu=ceil(log_2(2L_0)) gives T_FT<=C r^nu. L_0 is obtained by counting
the selected finite gadget, rather than assigning an unsupported gap.

Classical control can be included in this finite gadget count. Unroll the
fixed cap on syndrome/verification rounds. The gadget reads a fixed finite
number m_0 of measurement bits, so each required Boolean control has a
truth-table circuit of at most C m_0 2^m_0 gates. Compute three copies and
use a separate majority gate for each physical quantum-operation control.
Never fan an unprotected majority result out to several quantum locations.
A fault in one decoder copy is outvoted; a final majority fault affects
one quantum location; corruption of one shared raw measurement record is
already a faulty measurement outcome in the syndrome-gadget fault model.
Branching is padded/unrolled, so a faulty flag cannot extend execution.
Thus the classical implementation introduces no single fault with a new
unbounded effect. Its constant finite gate count is included in L_0 before
the threshold recursion. This uses the selected gadget's existing
one-fault correctness, including faulty measurements; it is not a claim
that nearest-codeword memory decoding alone proves a circuit threshold.

For the existing stage size s=a+ln(1/epsilon)+1, take
g=ceil(2/eta_mem), n<=C s^g, M<=C n^2 and r<=C s. Gaussian CSS synthesis,
source decoding and conditional Pauli representatives need at most C n^3
logical/classical operations. The sampler has b_rate<=C s. Therefore a
conservative exponent covering the sampler and encoded transfer is

    K_base=max(2g kappa+4, 3g+nu).

Rate estimation to O(1/n) per endpoint takes a fixed O(n^2 log(n/delta))
samples per endpoint. A stabilizer simulation of a private gadget costs
at most C r^(3nu) using a quadratic-size tableau. Its total exponent is
at most 3g+3nu+1 when log(1/delta)=O(s). Include this in K_base.

This simulation bound concerns a specified primitive noise kernel. Physical
calibration additionally needs its actual readout/drift certificate. The
mathematical weighted-norm robustness permits the same O(1/n) precision;
it does not certify an unknown physical kernel by itself.

Let K=max(2g kappa+nu+4,3g+nu,3g+4nu+1). Operation count, workspace and newly
retained records are each at most C s^K. Copying the complete earlier prefix
adds at most one degree, by TransferRate.retained_prefix_bound. Serial
nearest-neighbour routing on at most C s^(K+1) occupied sites adds at most
one workspace factor: total operations/duration <=C s^(2K+2). Paying for
every occupied site's hold/guard/clock charge during that duration gives
at most C s^(3K+3) unit-duration primitive invoices. The explicit journal
primitive below has reset duration O(s), adding one degree to elapsed
time, and drive/lifecycle charge O(s), adding one further degree. Thus

    W_stage <= C s^(3K+5).

### A journal/controller primitive with a derived linear charge

Use the existing thermal activation model explicitly: the classical states
|0>,|1> have energy zero, and the bridge state |e> has energy B. Bath jumps
0,1 -> e have rates nu exp(-beta B), while e -> 0,1 have rates nu. There
is no uncontrolled direct 0<->1 jump in this activation-barrier primitive.
Its logical flip hazard is at most nu exp(-beta B), precisely the existing
PassiveReference device requirement. Additional admitted circuit faults
remain in the controller's FT fault account, not hidden in that hazard.

For barrier setting H(B)=B|e><e|, 0<=Tr(rho dH/dB)<=1. Therefore gross
actuator work along any ramp is at most the total variation of B, on every
fault trajectory. Raising/lowering the barrier costs at most 2B. A fixed
local unitary can use a Hamiltonian logarithm with norm at most pi in the
chosen gate-time units; switching it on/off has bounded variation at most
2pi. This supplies a finite local gate invoice independent of archive age.

For a reset, bias the undesired levels by E, with beta E=O(s), and couple
them to the existing downward reset channel of fixed rate nu. Waiting
O(s)/nu makes both the transient exp(-nu t) and equilibrium leakage
O(exp(-beta E)) fit the allocated per-operation failure. Bias ramps cost
at most 2E. The bounded energy spectrum and the first law bound the reset's
net heat/export by its control work plus an energy difference O(B+E).
The controller/export actuators are power-capped and run for this fixed
duration, so their complete realised charge is O(s). A failure cannot
extend the allotted duration or draw an unbounded retry reserve.

The barrier and reset inequalities use s=a+ln(1/epsilon)+1 and the already
counted polynomial number of operations. The union allowance contributes
only log(operation count)=O(log s), so B,E and the capped reset duration
are O(s). This derives the linear primitive charge used above. Landauer
is its lower entropy-export constraint, not its upper-work proof. Thermal
up/down fluctuations are not counted as unperformed actuator operations.

All nine HandoffCharge fields remain paid, including every failed attempt,
workspace reset, endpoint feedback slot and export. The attempt cap is
deterministic. The existing TransferRate theorem absorbs this polynomial
stage invoice into C_T t and joins G3 for every d_G>=1. It does not fund
unperformed work or certify a missing physical primitive.

## 5. Status

The endpoint algebra, local rate threshold and controller operation degree
are derived here. The installation still has to identify its joint endpoint
kernel. The displayed finite controller primitive supplies a pathwise
upper-invoice construction within the existing barrier model. The independent-kernel
specialisation cannot be promoted to the original general local-stochastic
claim without that correspondence. G.21 must retain this exact distinction;
neither invented rates nor an unverified linear physical-cost assumption
can be used to mark the complete physical join locked.
