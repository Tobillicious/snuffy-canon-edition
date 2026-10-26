### 8. Compensate the specified physical endpoint channel

The prepared input law can account for the endpoint noise. For its actual
specified Pauli syndrome channel N, construct q=N^(-1)pi and prove q is
positive, rather than implement a nonpositive inverse quantum operation.
If a bounded sampler produces mu<=4q, positivity gives Nmu<=4pi.
The unknown logical state is not inverted or replaced.

For a one-qubit Pauli law (a,b,c,d), in the order I,X,Z,Y, put

    lambda=(1,a+b-c-d,a-b+c-d,a-b-c+d).

The inverse weights are the four-point inverse Fourier transform of
(1,lambda_1^(-1),lambda_2^(-1),lambda_3^(-1)). If p=b+c+d<1/2, all
lambda_i>=1-2p. The identity inverse weight r_I>=1, and the convolution
Neumann series gives |r_P/r_I|<=2p/(1-2p), P!=I. These statements allow
unequal X,Y,Z rates. The separate PauliInterface development receipt
checks the inverse/composition and domination algebra; it does not supply
the physical noise law or the positivity argument below.

For independent local endpoint channels, let u_(j,P)=r_(j,P)/r_(j,I).
The candidate q is the finite signed sum

    q(sigma)=(product_j r_(j,I))/Z
       * sum_F (product_(j,P in F) u_(j,P)) z^|sigma+syndrome(F)|,

where F selects at most one nonidentity Pauli colour per location.
Convolution gives Nq=pi and sum q=1. To prove positivity, augment the
full-history graph by its fault-colour vertices. A location's colours form
a clique, and each finest check's history/fault scope forms a clique.
For bounded footprint w and incidence, its degree D_A is fixed across
levels. Put B=(D_A+1)^2. The history bound |H|<=K_0|sigma|, K_0=4, and
the energy change bound |sigma+syndrome(F)|>=|sigma|-w|F| give

    |activity(gamma)|<=b^|gamma|,
    b=max(z^(1/K_0), max_(j,P)|u_(j,P)| z^(-w)).

With b<=[8eB(D_A+2)]^(-1), the incompatible-activity sum is less than
|gamma|, also after multiplying size-l activities by t^l for |t|<2.
The same bound holds in every sampling-prefix/deleted-polymer model.
Their partition functions are nonzero. Decreasing the real noise rates
continuously to zero leaves them real, nonzero and positive at zero;
therefore q and all physical history-prefix masses are positive.

The signed auxiliaries are used only for counting. With s_0=Be b, the KP
cavity bound gives each conditional original-history inclusion probability
at most sum_(l>=1) s_0^l<1/4. The probability of a history component larger
than L is at most M sum_(l>L) l s_0^l. Choose L=O(log M) making this at
most 1/2. List the P polynomially many retained history components. At
each decision, estimate the positive exclusion ratio to relative precision
eta=1/(256P), take an upper enclosure, and round the inclusion probability
down to a fixed dyadic mesh at most eta. Inclusion is not inflated;
exclusion is inflated by at most 1+12eta. The full decision-path factor
is below two. Truncation costs at most two, giving mu<=4q with polynomial
work and a fixed finite coin budget. All histories and coins are retained.

Finite precision in N is sufficient. In the weighted norm
||f||_pi=max_sigma |f(sigma)|/pi(sigma), a size-w syndrome translation has
norm at most z^(-w). If the nominal channel hatN_j has
hatp_j(1+z^(-w))<=1/2, its inverse norm is at most two. For l1 probability
vector error epsilon_j,

    ||N_j hatN_j^(-1)||_pi<=1+2z^(-w)epsilon_j,
    Nmu<=4 exp(2z^(-w)sum_j epsilon_j) pi.

Consequently O(1/n) rate accuracy per output costs a fixed envelope factor;
no global minimum-eigenvalue ratio or exponentially precise calibration
is used. Calibration failure remains a separately budgeted branch.

### 9. Physical private outputs and anisotropic feedback

The short FT processor computes the ideal old decoder/new branch encoder.
For each output prepare a separate encoded Bell pair A,B. Keep B encoded
and private during waiting; move only A into the logical Bell measurement
with the source output S. The encoded comparison measurement traces both
measured auxiliary coordinates. For an arbitrary omega_(S,G_S,R), and
resource |Phi><Phi|_(A_L,B_L) tensor eta_(G_A,G_B), the unnormalised
receiving state at outcome m is exactly

    (1/4) P_m omega_(B_L,R) P_m tensor Tr_(G_A)eta.

Indeed tracing the measured gauges commutes with the logical measurement.
The statement permits entangled gauges and an arbitrary old reference.
Independent private resource pairs leave product receiving-gauge marginals.
Private decoding W_j then has effective channel D_j(rho)=W_j(rho tensor
tau_j). With ideal Pauli feedback its outcome average is the Pauli twirl
(1/4)sum_m P_m D_j(P_m rho P_m)P_m.

Christandl--Fawzi--Goswami, arXiv:2408.05260v3, Definition 20 and
Lemmas 29--32, give the uniform encoded comparison and interfaces with
polynomial overhead. Their general output theorem retains correlated
auxiliaries; independence is not inferred from it. In the stochastic
Pauli/stabilizer implementation, each fixed private fault path gives an
input-independent Pauli, so let d_j be that private decoder's Pauli law.

Actual feedback need not have isotropic or outcome-independent rates.
Write I,X,Z,Y as F2^2. Let c_j(eta|m) describe corruption of the two
correction bits. Use two fixed physical slots, X/idle then Z/idle, whose
post-slot Pauli kernels are x_(j,bx),z_(j,bz). Their residual convolution
is r_(j,bx,bz)(f)=sum_(u+v=f)x_(j,bx)(u)z_(j,bz)(v). The actual local
endpoint law is

    q_j(a)=1/4 sum_(m,e,eta,f:e+eta+f=a)
               d_j(e)c_j(eta|m)r_(j,m+eta)(f).

This follows by Pauli propagation through the actual requested correction;
Pauli conjugation changes only irrelevant phases. Both idle slots, wrong
control bits and every final gate fault remain included. If p_D,p_C,p_X,p_Z
are the actual four nonidentity-mass bounds, then

    1-q_j(0)<=p_D+p_C+p_X+p_Z.

With b,z,w as above, the explicit threshold
p_*=b z^w/[2(1+b z^w)] ensures both inverse and forward colour bounds
whenever that sum is at most p_*. This is a derived inequality to check
against the physical kernel, not a numerical hardware claim.

Microscopic factorisation can be checked directly: if disjoint endpoint
devices have initially product private reservoirs and conditional generator
sum_j L_j(m_j) with disjoint supports, their conditional evolution is the
tensor product of the local evolutions. Summing the uniform Bell outcomes
then gives N=product_j N_j with the q_j above. This identifies exactly what
the private hardware and guards must implement. A local-stochastic bound
alone does not prove these reservoir/generator conditions. If shared causes
remain admitted at these endpoints, their actual joint kernel must be
retained and a compatible compensation or holding certificate supplied.

The FT comparison error is at most C M_FT sqrt((c_FT p)^r), with constants
of the selected fixed scheme. It is a diamond error before holding, so
subsequent holding/decoding does not multiply it by 2^a. The r=O(a+log n+
log(1/epsilon)) choice retains polynomial stage work. The source theorem's
noiseless classical-control convention is not a free physical controller:
the realised controller and its faults must occupy the charged accounts.


#### Explicit reset/feedback generator and bounded correlated jump causes

Initial correlations of finite private noise-label registers can be removed
without resetting the unknown data. For target tau_j=diag(t_j), the jumps
L_(j,u,v)=sqrt(nu_j t_(j,u))|u><v| give exactly
G_j(rho)=nu_j[tau_j Tr(rho)-rho]. Since the replacer R_j is idempotent,
exp(tG_j)=exp(-nu_j t)id+(1-exp(-nu_j t))R_j. The product reset differs
from complete replacement by at most 2sum_j exp(-nu_j t) in diamond norm,
even from initially correlated registers and references. A fixed reset
time nu_min^(-1)ln(2m/delta_reset)=O(s) suffices. The reset invoice above
covers it. This removes initial correlations; it does not remove new
shared faults occurring after reset.

For a concrete feedback slot choose H_(X,b)=b pi X/(2tau) and jump
sqrt(gamma_X)X. These commute, at zero Bohr frequency, for both X and idle.
The actual slot is its requested Pauli followed by X noise of probability
(1-exp(-2gamma_X tau))/2<=gamma_X tau. The analogous Z slot yields a fixed
anisotropic Pauli residual, independent of the requested Bell outcome.
It therefore composes with the exact twirl of even a coherent private
decoder. All couplings and durations are specified local parameters.

Output-qubit independence can also be relaxed. For bounded Pauli causes
P_e and generator L_e(t)=gamma_e(t)(Ad(P_e)-id), conjugation superoperators
commute even when the underlying Paulis anticommute. Each is an involution,
so exponentiating its two eigenspaces gives the exact joint channel

    N=product_e[(1-p_e)id+p_e Ad(P_e)],
    p_e=(1-exp(-2 integral gamma_e(t)dt))/2 <= integral gamma_e(t)dt.

This factors over the specified physical jump causes, retaining correlations
between output qubits. Each inverse is
[(1-p_e)id-p_e Ad(P_e)]/(1-2p_e), with relative activity p_e/(1-p_e).
One inverse vertex and one forward vertex per cause suffice. Bounded
physical support, syndrome footprint w and incidence keep the augmented
history graph's degree fixed. Include both CSS sectors in this graph when
a cause flips both; their independence is not asserted. The existing KP,
counting and O(1/n)-precision bounds therefore apply to this joint cause
model with its enlarged fixed graph constants.

For a k-qubit cause, its at most k single-qubit factors are used only in
the initial logical-error proof. A partial factorisation translates the
syndrome by a vector v of fixed weight at most w_split. Occupation of A
after that translation requires occupation of A outside supp(v) before it.
Thus Pr[A occupied after translation]<=C_split R_0^|A|, with
C_split=R_0^(-w_split). The endpoint witness/union bound gains only the
fixed factor k C_split. No global energy or probability ratio is used.

The pulse formula requires the active Pauli causes to commute with the
control Hamiltonian, or their actual propagated interaction-frame axes to
remain fixed. Other causes retain their time-ordered channel and the
residual bound in subsection 12. A common fluctuating rate retains its
joint conditioning; replacing it by its mean would change the channel.
This is a sufficient microscopic construction with bounded common causes,
not a deduction that every admitted local-stochastic law has this form.

### 10. Endpoint logical error and retained-record holding

The signed gas supplies a joint-occupation bound for every partial endpoint
layer. Add the already-applied positive forward-noise colours to its
inverse-colour graph, with activity p_P/(1-p) z^(-w), and enlarge the fixed
degree accordingly. If R_0=2Be b<1, then

    Pr[A occupied]<=R_0^|A|.

To prove it, select the augmented polymers meeting A. They cover A; the
cavity bound controls their remaining partition ratio by exp(sum|gamma|).
Choose the first uncovered mark and its size-l polymer. It removes at most
l marks. Induction bounds the covering sum by
R_0^|A| sum_(l>=1)(Be b/R_0)^l=R_0^|A|. Dropping compatibility only
increases this nonnegative majorant. Positivity refers to the physical
history marginal, not to the signed auxiliary weights.

BDL's finest-syndrome witness count now applies with R_0 in place of
thermal fugacity. In its notation a sufficient geometric ratio is

    theta=2(Delta+1)^2[(1+R_0^(1/4))^M_l-1]^(1/(1+Delta_l^4))<=1/2.

The witness-size threshold 2^(k-1) then gives unstable probability
B_n<=poly(n)exp(-c n^eta_mem), uniformly over partial preparation layers
and both sectors. This estimate concerns the preparation layer, not an
unproved long-time transport of a sparse law. Stable-syndrome Pauli paths
act as logical identity. For m single-qubit endpoint locations and m_c
additional k-qubit causes, the explicit bound is

    e_out<=8(m+k m_c C_split) B_n.

Here C_split is the fixed translation factor derived above; it is one for
the original single-qubit estimate. The old block's bounded input-interface
layer is covered by the earlier
thermal-plus-fault occupation estimate, giving the corresponding e_in.

Keep all sampler/teleportation records H in the actual map E:L->Q tensor H
and put omega_QH=E(I/2). The reference inequality is
(E tensor id_R)(rho_LR)<=4 omega_QH tensor rho_R; omega_QH need not factor.
The compensated calculation only requires its physical marginal
omega_Q<=C_out rho_beta. Holding the quantum block and keeping the record
comparison as a spectator leaves the R,H marginal unchanged. Apply the
same projector-block estimate to K tensor B_RH for arbitrary ||B_RH||<=1.
The decoded Pauli expansion gives

    ||rho_decoded,LHR(T)-rho_decoded,LHR(0)||_1
       <=18 Lambda integral_0^T sqrt(Tr[P_bad Phi_s(omega_Q)])ds
       <=18 Lambda T sqrt(C_out b_beta).

This retains joint tests of the records and the old reference; it does not
discard H to obtain a Gibbs product inequality. H's own storage faults and
work remain in the classical-record account. A coherent private-channel
version can insert stable projectors only in a comparison process. The
gentle projection/telescoping bound gives the conservative private-decoder
error 16m sqrt(B_n). Add the bounded Pauli-cause error above; both retain
stretched-exponential suppression.

Add e_in,e_out, the FT diamond error, calibration/controller failure and
the dynamical term inside the original epsilon/2^(a+2) stage allowance.
The incoming logical error is carried additively in the global composition;
it is not assumed to contract. With s=a+ln(1/epsilon)+1, choose the least
available BDL size above K s^(2/eta_mem). Its volume is polynomial in s;
the spatial exponent grows as s^2 while the time/allocation debt is O(s).
A fixed sufficiently large K meets every stage budget, including the
2a ln2 term. No new age-dependent noise rate is required.

### 11. A derived controller degree and physical invoice

For augmented degree D_A, put B=(D_A+1)^2,
h=ceil(log_2 B), u=h+2, v=ceil(log_2(3B)). The truncation and connected-set
count give P<=C M^u. To enclose a prefix partition ratio to relative
eta=1/(256P), truncate log Z(t) at
l=ceil(log_2(8M/eta)). The zero-free radius two gives log-tail bound
M 2^(-l). Connected-support Mobius inversion computes these coefficients:
for each connected U, enumerate W subset U and the occupied assignments
of W. This costs at most 3^|U| assignment tests; disconnected support terms
cancel by partition factorisation. Common-denominator rational arithmetic
and finite-series evaluation give the conservative bit-operation bound

    T_sampler<=C b_rate^4 M^kappa,
    kappa=(u+1)v+u+13.

The extra 13 allows root enumeration, eight powers of Taylor-order overhead
and four powers of the common-denominator bit size. All are fixed graph/
arithmetic bounds, not an assumed mixing exponent. The scalar exponential
is enclosed by a finite convergent-series computation at the same precision.

Let L_0 count the maximum recursive calls and physical operations in the
selected finite FT base gadget, with its classical-control procedure.
The recursion T_d<=L_0(T_(d-1)+1) gives degree
nu=ceil(log_2(2L_0)) in the accuracy index r. Set g=ceil(2/eta_mem).
Using n<=C s^g, M<=C n^2, b_rate,r<=C s, Gaussian CSS synthesis bounded
by C n^3, and a fixed O(n^2 s) calibration samples per endpoint gives

    K_c=max(2g kappa+nu+4, 3g+nu, 3g+4nu+1).


The finite base gadget also includes the classical control implementation.
Unroll its bounded syndrome/verification rounds and synthesize each Boolean
control on its fixed m_0 measurement bits by a truth-table circuit. Compute
three copies, with a private majority for each physical quantum-operation
control. A fault in one copy is outvoted; a final majority fault affects one
quantum location; corruption of a shared raw record is a faulty measurement
outcome already covered by the syndrome-gadget proof. An unprotected control
flag is never fanned out to many quantum locations. Padding prevents a bad
flag from extending execution. Count these finite circuits in L_0 before
the FT recursion. The degree above includes FT protection of the sampler
and calibration computation as well as the quantum gates.

The last term includes stabilizer-tableau simulation of the specified
private fault kernel. Operation count, workspace and new records are at
most C s^K_c. Retaining the entire prefix adds at most one degree. Serial
routing adds one workspace factor, giving at most C s^(2K_c+2) primitive
events. Total stock-times-duration, including every wait, guard and clock,
is then bounded by C s^(3K_c+3) in unit-duration units.

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

All nine HandoffCharge accounts, the complete history, failed attempts,
retirement and endpoints remain included. The existing deterministic cap
and TransferRate.polynomial_stage_bill give total transfer work <=C_T t.
TransferRate.join_complete_bill joins the existing sweep/archive bills for
every d_G>=1. The coefficient is independent of archive age and the unknown
logical input. These degree/invoice derivations are prose; the canonical
Checkpoint 12 source count is unchanged.

### 12. Exact joint kernel constraint and bounded residual

#### Exact finite joint law

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

#### Residual bound with the records and reference retained

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

#### Unchanged stage budget

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
