# Residual certificates: precise statements and proofs

27 October 2026, Pacific/Auckland. This writes out the author's two
certificate arguments with explicit channel, record and exposure domains.
The general results below are analytical proofs. The companion script
verify-delta-joint.py performs finite exact-arithmetic and numerical checks;
it is not a Lean formalisation or a measurement of the installation.
Canonical Checkpoint 12 remains 192 modules / 1,158 statements.

## 1. Spaces, instruments and the norm

All spaces in this proof are finite-dimensional. The input L contains
the complete declared stage input, including any admitted noise memory
whose correlations matter. The output Q tensor H includes the quantum
payload and retained classical records. A further reference R is arbitrary
and is never traced out in the comparison.

An instrument with CP outcome maps M_h and trace-preserving sum is
represented by the CPTP recorded channel

    E(X) = sum_h M_h(X) tensor |h><h|.

For a linear map T, define

    ||T||_diamond = sup_r sup_{||X||_1=1} ||(T tensor id_r)(X)||_1,

where X acts on the joint input L tensor C^r. This avoids taking a
supremum over reference-only states. It also proves the desired bound for
all operators, hence in particular every joint input state rho_LR.

A CP trace-nonincreasing map has diamond norm at most one. To see this
directly, write Phi(X)=sum_j A_j X A_j^dagger and form
W psi=sum_j A_j psi tensor |j>. Then W^dagger W<=I. For every reference,
the ideal property of the trace norm gives

    ||(W tensor I) X (W^dagger tensor I)||_1 <= ||X||_1.

Partial trace is trace-norm contractive: duality gives
|Tr[B Tr_env(Y)]|=|Tr[(B tensor I)Y]|<=||Y||_1 for ||B||<=1.
Taking its supremum proves the claim. For a CPTP map the upper bound is
attained on a density matrix, so its diamond norm equals one. Submultiplicativity
follows by applying the amplified induced-norm inequalities in sequence.

## 2. Discrete joint-path certificate

Let K_0,K_act be probability distributions on the same finite path set
Lambda, independent of the unknown input. Let Phi_lambda:L->Q tensor H
be the same CPTP branch maps in both models, with the same retained-record
interpretation. Define

    E_b = sum_lambda K_b(lambda) Phi_lambda,  b in {0,act}.

Then both E_b are CPTP and

    ||E_act-E_0||_diamond
      <= sum_lambda |K_act(lambda)-K_0(lambda)|
       = 2 TV(K_act,K_0).

Proof. Put d_lambda=K_act(lambda)-K_0(lambda). For every r and every
joint operator X, the triangle inequality and section 1 give

    ||sum_lambda d_lambda (Phi_lambda tensor id_r)(X)||_1
      <= sum_lambda |d_lambda| ||(Phi_lambda tensor id_r)(X)||_1
      <= (sum_lambda |d_lambda|) ||X||_1.

Take the two suprema defining the diamond norm. The final equality is
the definition TV(K,K')=(1/2)sum_lambda |K(lambda)-K'(lambda)|. This proves
the bound with all correlations among the components of lambda retained.

The same linear bound holds for common branch maps of diamond norm at
most one. If they are only trace-nonincreasing, trace preservation of
the complete E_b must be established separately. An operator V_lambda
denotes a single-Kraus map X->V_lambda X V_lambda^dagger, whereas
Phi_lambda denotes a channel. A CPTP single-Kraus branch requires
V_lambda^dagger V_lambda=I. General channels require multiple Kraus
operators. Their norms must not be confused with an operator norm of V.

Ordinary measurement outcome probabilities can depend on the input.
Normalising a postselected branch generally produces a nonlinear map;
it cannot be substituted for Phi_lambda here. Such an installation uses
the complete recorded-instrument norm or a proved common-path decomposition.

For any common subsequent CPTP F, including holding, decoding and record
handling, submultiplicativity gives

    ||F E_act-F E_0||_diamond <= ||E_act-E_0||_diamond.

A residual confined to preparation therefore acquires no multiplier from
the duration of later holding. Different residual segments may be combined
by telescoping, with each segment counted once.

## 3. Continuous generator certificate

Let L_0(t),L_act(t) be bounded piecewise-continuous generators on the same
joint space for 0<=t<=tau. Suppose their forward two-parameter propagators
U_b(t,s), s<=t, are CPTP, and put V(t)=L_act(t)-L_0(t). The difference V
need not itself generate a CPTP evolution. An initial correlated memory
must be included in this common joint description; separate reduced baths
are not inferred from marginal rates.

For a fixed terminal tau, differentiate
F(u)=U_act(tau,u) U_0(u,0) on each continuity interval. The two evolution
equations give

    F'(u) = -U_act(tau,u) V(u) U_0(u,0).

Because F(0)=U_act(tau,0) and F(tau)=U_0(tau,0), integration yields

    U_act(tau,0)-U_0(tau,0)
      = integral_0^tau U_act(tau,u) V(u) U_0(u,0) du.

The identity extends across the finitely many break points by summing
the interval integrals. The norm of an operator-valued integral is bounded
by the integral of the norm. Applying submultiplicativity and the unit
diamond norms of both forward propagators therefore proves

    ||U_act(tau,0)-U_0(tau,0)||_diamond
      <= integral_0^tau ||V(u)||_diamond du.

No exponential factor is needed: both outside propagators are CPTP. A
reduced non-Markovian description without CPTP intermediate propagators
does not supply this hypothesis merely because its maps from time zero
are CPTP. A suitable retained-memory generator or another norm bound
must supply it.

## 4. Bound each retained perturbation term

Suppose the complete difference is

    V(u)(X) = -i[H_cross(u),X]/hbar
              + sum_j gamma_j(u) D_{L_j(u)}(X) + V_other(u)(X),
    D_L(X) = L X L^dagger - (L^dagger L X + X L^dagger L)/2.

For any reference and any joint X, the trace-norm ideal property gives

    ||[H_cross tensor I,X]||_1 <= 2||H_cross|| ||X||_1,
    ||(D_L tensor id)(X)||_1 <= 2||L||^2 ||X||_1.

The second inequality is the sum of the first term, bounded by
||L||^2||X||_1, and two half-weight terms with that same bound. Taking
the diamond suprema and the triangle inequality proves

    ||V(u)||_diamond
      <= 2||H_cross(u)||/hbar
         + 2 sum_j |gamma_j(u)| ||L_j(u)||^2
         + ||V_other(u)||_diamond.

For an omitted physical dissipator gamma_j>=0. Absolute values also
cover signed differences of specified rates. Every remaining cross or
memory term belongs in V_other or in an explicitly separate discrepancy;
none may be omitted from v_a.

## 5. Original stage allocation and exposure length

Let a be a nonnegative integer and 0<epsilon<=1. The existing residual
allocation is b_a=epsilon/2^(a+5), one eighth of the original stage ceiling
epsilon/2^(a+2). If ||V(u)||_diamond<=v_a throughout an exposure tau_a,
then a sufficient continuous certificate is

    delta_joint <= min(2,tau_a v_a),
    tau_a v_a <= b_a.

If the residual persists for the entire holding interval tau_a=2^a, the
certificate condition is exactly

    2^a v_a <= epsilon/2^(a+5)
      iff v_a <= epsilon/2^(2a+5).

For a short preparation exposure the applicable condition remains
v_a<=b_a/tau_a. The full-holding rate requirement is not imposed on
preparation-only discrepancies, which obey section 2's subsequent-channel
contraction. For the discrete certificate the corresponding condition is

    2 TV(K_act,K_0) <= epsilon/2^(a+5)
      iff TV(K_act,K_0) <= epsilon/2^(a+6).

These conditions are sufficient tests for the stated certificates. If
one fails, that certificate does not establish the allocation; it does
not prove that the actual channel error exceeds it. Both complete channels
always have distance at most two. The incoming logical error, other seven
stage terms, full history and all reference correlations retain their
existing separate accounting.

## 6. Verification scope

checks/verify-delta-joint.py checks exact rational thresholds, equality
cases and rejection of exceeded bounds over its recorded stage/tolerance
ranges. It also checks finite recorded quantum channels and the Duhamel
identity on complete matrix-unit bases in specified finite examples.
Floating-point matrix checks are labelled separately from exact arithmetic.
It hashes every canonical source and every file of the existing Checkpoint
12 snapshot before and after execution, without compiling or modifying them.

The proof supplies the certificate implications. The finite checks supply
their stated computational evidence. No actual K_act, H_cross, dissipator
or v_a has been measured or newly identified for the installation here;
the existing physical-source obligation is unchanged.
