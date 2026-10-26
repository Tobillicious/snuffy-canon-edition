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

The classical activation/reset primitive supplies a physical upper invoice.
Use logical states 0,1 and bridge state e with H(B)=B|e><e|; upwards rates
are nu_0 exp(-beta B) and downwards rates nu_0. Its flip hazard is at most
nu_0 exp(-beta B), matching the existing barrier model. Since
0<=Tr(rho dH/dB)<=1, a barrier ramp's gross actuator work is at most its
total variation, for every state/fault trajectory. A bounded local unitary
has a Hamiltonian logarithm of norm at most pi in gate-time units, so
switching it on/off has a fixed finite drive invoice.

A gross reset invoice needs a physical cap: bounded energy and the first
law bound net heat, while thermal recrossings can make gross heat arbitrarily
large on a finite-time trajectory. Use a three-state reset star with ground
0 and two undesired levels of energy E. During the reset, switch off the
bridge bath and use jumps i->0 of rate nu_0 and 0->i of rate
nu_0 exp(-beta E). The uncapped wrong-state probability is at most
exp(-nu_0 tau)+2exp(-beta E).

Make this a finite jump-budgeted primitive. Append a four-state counter
c=0,1,2,3, and replace every reset jump L by
L tensor |c+1><c| for c<3. At c=3 the reset coupling is off and a cap flag
is retained. The clock still ends the attempt after the fixed tau. Every
path of this instrument, including a capped failure, has at most three
bath jumps, so its gross heat exchange is at most 3E. This is an actual
finite generator specification, not a declaration that a noisy software
flag can shut down an otherwise uncapped bath.

Reaching three jumps requires an upward jump: without one there is at most
the initial downward jump. The upward intensity is at most
2nu_0 exp(-beta E), uniformly in the input and reference. Thus

    Pr[cap reached]<=2nu_0 tau exp(-beta E),
    ||Reset_cap-Reset_uncapped||_diamond<=4nu_0 tau exp(-beta E).

The two trajectory instruments agree until the cap; the remaining channels
have trace-norm difference at most two. Both the ordinary reset error and
this extra cap contribution fit the existing controller allocation with
E,tau=O(s), since log(polynomial operation count)=O(log s). The counter is
constant-dimensional. Apply the same finite jump cap to activation-bath
exposures whose gross throughput enters the invoice: without an upward
jump there is again at most one downward jump, and the cap probability is
bounded by 2nu_0 t exp(-beta B). A fixed constant safety shift in the
existing journal barrier pays this allowance even for t=2^a. Thus uncapped activation recrossings are not hidden
elsewhere in the primitive. Counter initialisation, flags, export and any
additional faults remain in the charged controller/source model. A transition that
bypasses this cap must enter the actual joint kernel or its residual.

For the full-rank private-label replacer, a single-use latch avoids a
recrossing bill altogether. With flag initially 0, use jumps
sqrt(nu_j t_(j,u))|u,1><v,0| and make flag 1 absorbing. Summing over u,v
makes the no-jump hazard exactly nu_j. Tracing the retained flag gives
exp(-nu_j tau)id+(1-exp(-nu_j tau))R_j exactly, including every reference.
There is at most one jump; the label energy span is O(s), also when a
positive probability floor is used. This is an engineered reset instrument;
the latch and its preparation are paid, rather than inferred from detailed
balance of the uncapped reduced generator.

Finally debit the gross drive and export work separately. Hamiltonian ramps
cost at most their total variation O(B+E+1), and an exporter with bounded
nonnegative power P_exp over its fixed duration costs at most P_exp tau.
The capped reset contributes at most 3E of bath throughput; the single-use
label reset contributes at most its energy span. With the constant-size
latches/counters, this gives a complete O(s) primitive invoice in the
specified device model on successful and failed attempts. It uses no net
heat cancellation, expected jump count or Landauer upper bound. The actual
cap, exporter and their faults must be bound to this same installation.

Reset duration and this gross linear primitive invoice add two conservative
degrees. Consequently the complete stage implementation in this device
model satisfies


    W_stage<=C s^(3K_c+5).

All nine HandoffCharge fields remain paid, including every failed attempt,
workspace reset, endpoint feedback slot and export. The attempt cap is
deterministic. The existing TransferRate theorem absorbs this polynomial
stage invoice into C_T t and joins G3 for every d_G>=1. It does not fund
unperformed work or certify a missing physical primitive.

## 5. Status

The endpoint algebra, local rate threshold and controller operation degree
are derived here. The installation still has to identify its joint endpoint
kernel or meet the quantitative residual allowance in
JOINT-ENDPOINT-KERNEL-CONSTRAINT-2026-10-27.md. The displayed finite controller primitive supplies a pathwise
upper-invoice construction within the existing barrier model. The independent-kernel
specialisation cannot be promoted to the original general local-stochastic
claim without that correspondence. G.21 must retain this exact distinction;
neither invented rates nor an unverified linear physical-cost assumption
can be used to mark the complete physical join locked.
