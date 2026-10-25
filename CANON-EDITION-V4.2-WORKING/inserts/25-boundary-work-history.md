# Part III-G — The boundary decoder, complete history and work-shifted flow

The three supplied pillars are joined here by a constructed encoder, its adjoint decoder, transport of the full historical operator algebra, a derived smearing kernel and the complete work ledger. These are components of the same all-particular protection construction in Parts I–II. The maximal outcome, rival domain, continuation, freedom, historical fidelity and charged fault standard remain fixed.

## G.1 From the source flux to an encoder and decoder

Let \(\mathcal C_{\mathrm{hist}}\) contain the protected historical registers, their labels and relational observables at the original fidelity standard. On a local finite physical code, let \(E:\mathcal C_{\mathrm{hist}}\to\mathcal H_\partial\) be complex linear and preserve the full symplectic form:

\[
\operatorname{Im}\langle Ex,Ey\rangle
=\operatorname{Im}\langle x,y\rangle\qquad\text{for every }x,y.
\]

Applying this identity to \(x,iy\) also preserves the real part. Hence

\[
\langle Ex,Ey\rangle=\langle x,y\rangle,\qquad
E^\dagger E=I,\qquad D=E^\dagger,\qquad DE=I.
\]

`inner_preserved_from_symplectic_flux`, `boundaryIsometry`, `adjoint_decodes_isometry` and `decoderFromSymplecticFlux` implement these steps. The source flux identity is an identity for the whole encoded phase space. Its derivation must use the actual source-to-boundary map and boundary observations; the scalar Gauss charge balance supplies its charge component.

There is also an explicit finite encoder. For an injection \(j:\{1,\ldots,m\}\hookrightarrow\{1,\ldots,n\}\), assign

\[
(E_jx)_{j(a)}=x_a,\qquad (E_jx)_b=0\quad(b\notin\operatorname{im}j).
\]

Its adjoint reads those same coordinates. `coordinateBoundaryEncoder` constructs this map; `coordinate_boundary_roundtrip` proves its exact inverse on the code. `boundary_capacity_necessary` proves that every such linear isometry requires \(m\le n\). These numbers are Hilbert-space dimensions: an \(n=2^b\) boundary register contains \(b\) qubits. At every retirement, the source assignment must include all protected history coordinates and the records supporting their relations, and charge their storage and movement.

For a density operator \(\rho\) on the code, the encoded state is \(E\rho E^\dagger\), and

\[
D(E\rho E^\dagger)D^\dagger=\rho.
\]

The same calculation holds with \(E\otimes I_R\) for every reference register \(R\); it therefore retains reference correlations. The adjoint is the decoder on the encoded range. A channel on all boundary inputs can be completed, for a fixed code state \(\rho_0\), by

\[
\mathcal D(\sigma)=E^\dagger\sigma E+
 \operatorname{Tr}((I-EE^\dagger)\sigma)\rho_0.
\]

Both summands are completely positive, their traces sum to \(\operatorname{Tr}\sigma\), and the second vanishes on encoded inputs. This channel extension and the reference-register calculation are prose derivations here. The existing finite-code correction theorem supplies the noisy-radius guarantee when the physical perturbation satisfies that certificate.

## G.2 Charge and the complete historical algebra

Define the boundary representative of every code observable by

\[
\alpha(A)=EAE^\dagger,\qquad P=EE^\dagger.
\]

Then \(\alpha(A)Ex=EAx\), \(\alpha(A)\alpha(B)=\alpha(AB)\), and

\[
\langle Ex,\alpha(A)Ex\rangle=\langle x,Ax\rangle.
\]

For an ordered word \(A_1\cdots A_r\), the same identity holds without exchanging its factors. `boundary_observable_on_code`, `historical_query_preserved`, `historical_word_on_code`, `historical_word_expectation` and `boundary_observable_mul` prove these statements. Thus the decoder preserves the historical queries and their ordered relations represented on the code. The identity of this represented algebra is \(P\).

In particular,

\[
Q_\partial E=EQ_{\mathrm{src}},\qquad
[\alpha(A),\alpha(Q_{\mathrm{src}})]=\alpha([A,Q_{\mathrm{src}}]).
\]

`boundary_observable_commutator` proves the commutator transport. An ambient physical boundary charge may have an additional action on the orthogonal complement; the displayed source correspondence concerns the encoded range. Connecting that representative to the actual gauge field and readout remains part of the source construction.

For history words \(W_i\), use the genuine Gram kernel

\[
G_{ij}=\langle W_i x,W_j x\rangle.
\]

It is positive semidefinite by its squared-norm quadratic form. Its encoded value is identical, and it is nonsingular when the history vectors \(W_i x\) are linearly independent. `historical_gram_preserved` and `historical_gram_nondegenerate` prove the latter two conclusions using Mathlib's Gram results. Time ordering is retained inside each \(W_i\). A time-ordered two-point Green function requires its own analytic properties; the squared-norm proof applies to the displayed Gram kernel.

## G.3 The effective modular state and its transported flow

Work on the support of a faithful finite-code state \(\rho\), and put

\[
K=-\log\rho,\qquad G=K+\beta H_W,\qquad
\widetilde\rho=\frac{e^{-G}}{\operatorname{Tr}e^{-G}}.
\]

For self-adjoint \(H_W\), \(G\) is self-adjoint and \(U_s=e^{isG}\) is unitary. The additive normalisation in \(-\log\widetilde\rho=G+\log Z\,I\) cancels in conjugation. With the sign convention in the supplied proposal,

\[
\widetilde\sigma_s(A)=U_sAU_s^\dagger
=\widetilde\rho^{-is}A\widetilde\rho^{is}.
\]

This identifies the state whose modular flow is being used. \(K+\beta H_W\) is an effective generator for that changed state; a relation to the original state's flow requires its additional perturbation/cocycle correspondence.

Represent the generator on the boundary code by
\(G_\partial=\alpha(K)+\beta\alpha(H_W)\).
An arbitrary self-adjoint block on \(P^\perp\) gives an ambient block-diagonal extension. Since \(G_\partial E=EG\), induction gives \(G_\partial^rE=EG^r\). The norm-convergent exponential series yields

\[
e^{zG_\partial}Ex=E e^{zG}x.
\]

Consequently,

\[
\widetilde\sigma_s^\partial(\alpha(A))Ex
=E\widetilde\sigma_s(A)x.
\]

`powers_intertwine`, `exponential_intertwines` and `work_shifted_flow_on_code` prove this transport for bounded operators, including the sum \(K+\beta H_W\). The proof uses the exponential of that sum directly and needs no commutation between its two terms. Finite local codes supply bounded operators. A continuum application must separately supply domains, self-adjointness and the source/observable correspondence for its unbounded generators.

## G.4 Construct the smearing weight

Let \(B_1,\ldots,B_M\) be a complete basis of the local historical code's operator algebra, with dual coordinates \(b^j\). For \(A=\Phi_{\mathrm{bulk}}(\tau)\), define

\[
c_j(\tau,s)=b^j\!\left(\widetilde\sigma_{-s}(A)\right).
\]

Expanding the inverse-flowed operator and applying \(\widetilde\sigma_s\) gives, at every \(s\),

\[
A=\sum_{j=1}^M c_j(\tau,s)\widetilde\sigma_s(B_j).
\]

`historical_flow_roundtrip` and `historical_dual_kernel` prove this exact finite-basis identity. It constructs the dual coefficients from a complete operator family.

Choose an integrable compactly supported weight \(w\) with \(\int_\mathbb R w(s)\,ds=1\). Unitarity bounds the flowed operators, finite-dimensional coordinate functionals are bounded, and there are finitely many basis terms. The Bochner integral therefore exists in operator norm and

\[
\alpha(A)=\int_{\mathbb R}ds\,w(s)
 \sum_j c_j(\tau,s)\widetilde\sigma_s^\partial(\alpha(B_j)).
\]

For the proposal's temporal form, partition \([0,\tau]\), for \(\tau>0\), into \(M\) intervals \(I_j\) of positive lengths \(\ell_j\). A boundary probe schedule representing this complete family uses

\[
\mathcal O_\partial(t')=\alpha(B_j),\qquad
f(\tau,s,t')=\frac{w(s)c_j(\tau,s)}{\ell_j}
\quad(t'\in I_j).
\]

Integration over each interval returns its basis term. Thus

\[
\alpha(\Phi_{\mathrm{bulk}}(\tau))
=\int_{\mathbb R}ds\int_0^\tau dt'\,
 f(\tau,s,t')e^{isG_\partial}\mathcal O_\partial(t')e^{-isG_\partial}.
\]

Pulling back by \(E^\dagger(\,\cdot\,)E\) gives the original bulk historical operator. At \(\tau=0\), use the finite-basis formula directly. The continuous-integral and probe-schedule steps are proved in prose here; the exact finite-basis reconstruction and exponential transport are machine checked.

For an independently specified continuous probe family, construct its analysis/synthesis frame operator \(\mathsf S\). On the full represented historical operator space, a lower frame bound \(aI\le\mathsf S\), \(a>0\), supplies the dual \(\mathsf S^{-1}\) and inverse bound \(1/a\). This is the quantitative observability connection needed to derive that family's smearing weight. The finite complete basis above supplies a concrete local route. A local Fisher metric by itself does not establish the required global frame correspondence.

This exact local reconstruction uses finite dual coefficients and a normalized compactly supported average. A Tikhonov inverse with positive parameter instead has mode response \(\lambda^2/(\lambda^2+\epsilon)\); its residual error must enter the original fidelity allowance whenever that implementation is used. Its spectral bounds and parameter/work relation must be derived from the actual implementation. The finite-basis derivation does not require infinite work or a conjectured modular spectral gap.

## G.5 The complete work algebra and capacity account

Use the complete decoder, memory, controller and reservoir ledger. At fixed Hamiltonian with Gibbs reference \(\gamma_\beta\), write dimensionless relative free energy as \(D=-S+\beta U+\log Z\). The first law and entropy production are

\[
U_2-U_1=W_{\mathrm{on}}-Q_B,\qquad
\Sigma=S_2-S_1+\beta Q_B\ge0.
\]

They give the exact identity and lower bound

\[
\beta W_{\mathrm{on}}=D_2-D_1+\Sigma,\qquad
W_{\mathrm{on}}\ge\frac{D_2-D_1}{\beta}.
\]

`decoder_work_balance` derives the identity from the existing `ThermoLedger.stroke_identity`; `decoder_work_floor` proves the bound. `decoder_work_floor_saturation` identifies equality with \(\Sigma=0\) in this ledger. Historical energy belongs in \(U_1,U_2\); any separately charged historical term must denote a component not already counted there. The Gibbs reference in this calculation is distinct from the protected constrained reference \(\tau\) in the preservation functional.

The existing quantum Landauer theorem supplies the entropy-export cost of actual erasure/reset under its bath and coupling assumptions. Reads and reversible inversions are charged by their implemented operations and full thermodynamic account. Joint unitarity supplies a model for both reversible and dissipative processes; entropy production determines saturation of the work floor.

For the prepared decoder state, the existing quantum Gibbs bound retains its partition term:

\[
S(\rho)\le \beta\operatorname{Tr}(\rho H_W)+\log Z.
\]

`funded_decoder_entropy_bound` joins this bound to an actual energy allocation \(\operatorname{Tr}(\rho H_W)\le E_0+\mathrm{budget}\). Entropy is measured per state; a channel rate must be multiplied by its operating duration before comparison with a total information demand. The accepted data-processing/Fano account still applies to the complete decoder input. Energy can power transmission, storage or a different protocol; reconstruction also needs the historical information carried by those inputs.

The work floor and the complete \(O(t^{d_G})\) ceiling are joined to the same execution. The ceiling remains the gross bill of Section 21.7.5: encoding, historical retention, boundary handoff, routing, guard, controller, reset and minimal hold are charged. `G3CompleteBill` supplies the cumulative and age-conversion derivations. `funded_decoder_cycles` supplies the escrow certificate when local income covers that complete demand. Prefix solvency, including within-cycle charges, is required for the actual schedule.

The operator-basis formula proves a reconstruction identity. Executing every basis query as tomography is a separate workload. The physical decoder's circuit, query schedule and retirement operations must meet the existing complete work bill; no uncharged dense tomography is added to the wavefront construction.

## G.6 A charged exchange with an accounted reservoir

On the basis \(|00\rangle,|01\rangle,|10\rangle,|11\rangle\), take

\[
Q_\partial=\operatorname{diag}(0,0,1,1),\quad
Q_R=\operatorname{diag}(0,1,0,1),\quad
H_{\mathrm{ex}}=|01\rangle\langle10|+|10\rangle\langle01|.
\]

Then

\[
[H_{\mathrm{ex}},Q_\partial+Q_R]=0,\qquad
[Q_\partial,H_{\mathrm{ex}}]\ne0.
\]

`exchange_hamiltonian_hermitian`, `exchange_conserves_total_charge` and `exchange_pumps_boundary` prove these identities for the explicit matrices. The unitary exchange gate \(S\) swaps \(|01\rangle\) and \(|10\rangle\), fixes \(|00\rangle,|11\rangle\), and satisfies

\[
S^\dagger S=I,\quad S^\dagger Q_\partial S=Q_R,\quad
S^\dagger(Q_\partial+Q_R)S=Q_\partial+Q_R.
\]

`exchange_swap_unitary`, `exchange_swap_charge` and `exchange_swap_total` prove these identities. This gives a concrete local exchange with its reservoir charge included.

For the full Hamiltonian, the Heisenberg convention is

\[
\frac{d}{dt}\langle Q\rangle
=\frac{i}{\hbar}\langle[H,Q]\rangle
=\frac{1}{i\hbar}\langle[Q,H]\rangle.
\]

Thus a constructed \(H_{\mathrm{tot}}\) commuting with the bulk-boundary-reservoir total charge gives its conservation. The continuum action must supply the corresponding gauge symmetry and surface current. Scalar Lagrange multipliers enforce equality constraints of a specified action; work inequalities require the corresponding admissibility or complementary-slackness treatment. Their insertion alone does not construct the historical encoder or prove its work bill.

## G.7 Unified proposition and its source correspondence

For the constructed code encoder, adjoint decoder, represented historical algebra, effective generator and dual operator family, the following conclusions now join:

1. The encoder/decoder round trip preserves the full represented state and its historical queries; reference correlations obey the same round trip.
2. Source charge and all ordered historical operator relations transport to the boundary code.
3. The effective work-shifted flow intertwines with that transport, and the derived finite dual kernel reconstructs every represented historical operator.
4. The same physical execution is subject to the thermodynamic floor, complete wavefront ceiling, funding certificate and charged fault standard.

The first three operator components have the native results named above, alongside the explicitly identified prose channel/integral derivations. The work and exchange components have the native ledger and matrix proofs. Application to the full protection theorem still joins these maps to the actual full-domain source, complete historical capacity/physical handoff and the whole continuation/freedom outcome. Those are the existing source-construction correspondences in Part III-E; this component theorem does not replace the maximal conclusion with an isometry or work premise.

The research precedents have their stated domains: [JLMS](https://arxiv.org/abs/1512.06431) relates relative entropy and modular flow in holographic entanglement wedges; [Faulkner–Lewkowycz](https://arxiv.org/abs/1704.05464) constructs modular reconstruction using the relevant bulk flow. Their results motivate the operator route; the local encoder and dual-kernel proofs above supply this edition's explicit algebraic components. [Reeb–Wolf](https://arxiv.org/abs/1306.4352) gives a precise Landauer account including finite-reservoir corrections, while [Jakšić–Pillet](https://arxiv.org/abs/1406.0034) treats saturation under its quantum statistical-mechanical assumptions.

---

## G.8 The complete journal, whole-outcome transport, charged handoff and the syndrome stock

This subsection joins the full historical record to the holding bill. The
historical record is kept in full and moved reversibly. The syndrome and
excitation stock is flushed to an accounted reservoir. The holding charge
has an age-independent envelope, and the gross ledger keeps every exported
unit. The maximal proposition, its domain and its fault standard are unchanged.

**The complete journal.** Let the source have states \(X\), commands \(C\),
environment inputs \(E_v\) and transition \(T:X\times C\times E_v\to X\). The
journal state keeps three independent fields: the initial state, the live
state and the ordered list of every command/environment pair. A step applies
\(T\) to the live state and appends \((c,e)\). Replay folds \(T\) over the list
from the initial state. If replay equals the live state before a step, it
equals it after the step, since folding over an appended list applies \(T\)
once more (`G1FullDomain.replay_journal_step`).

Use the projection \(s\mapsto s_{\mathrm{live}}\). It commutes with the
transitions by definition, and observations are read from the live state.
Proposition 5 (reactive lockstep) then gives, for **every** reactive controller
\(\mathrm{ctrl}:\mathrm{List}\,O\to C\) and every reactive environment
\(\mathrm{env}:\mathrm{List}\,O\to C\to E_v\), at every step \(k\):

\[
s^{\mathrm{journal}}_{k,\mathrm{live}}=s_k,\qquad
\mathrm{obs}^{\mathrm{journal}}_{0..k}=\mathrm{obs}_{0..k},\qquad
\mathrm{replay}(s^{\mathrm{journal}}_k)=s^{\mathrm{journal}}_{k,\mathrm{live}}.
\]

Induction on \(k\) carries the replay invariant
(`G1FullDomain.journal_reactive_fidelity`). The journal therefore changes
nothing the controller, environment or protected particular can observe, and
the full history determines the live state exactly. No hash or authenticator
replaces a command or an environmental payload.

The record's size is counted from its alphabet. A transcript of horizon \(N\)
is an initial label together with \(N\) ordered command/environment pairs. If
\(|X|\le2^{b_0}\) and \(|C\times E_v|\le2^{b}\), then

\[
|X\times(C\times E_v)^N|\le2^{\,b_0+bN}
\quad(\texttt{G1FullDomain.transcript\_capacity}).
\]

This is the full payload's capacity, not the length of a digest.

**Whole-outcome transport.** Let \(\mathrm{outcome}\) be any function of the
final state and the complete observation history. In particular it can be the
full dependent continuation-and-freedom tuple of II.1. Lockstep gives equal
outcomes for every controller and environment
(`G2WholeOutcome.journal_whole_outcome`). Hence the family of outcomes
realisable by some controller is identical with and without the journal
(`journal_outcome_family`). Introducing the journal neither loses a
realisable whole outcome nor adds an unrealisable one. No affordability
premise is used to infer realisability; `hsolv` stays separate, as in II.10.

**Reversible, reference-preserving handoff.** For a bulk register and a
reserved boundary register of the same dimension \(\iota\), together with an
arbitrary reference \(R\), let \(\mathrm{swap}\) be the coordinate
permutation of \(\mathbb C^{(\iota\times\iota)\times R}\) exchanging the two
registers and fixing \(R\). It is a linear isometry equivalence. If the
boundary register holds the blank state, then any payload \(\chi\) on
\(\iota\times R\), however entangled with the reference, is moved to the
boundary and the bulk is left blank
(`DecoderRetraction.handoff_moves_reference_payload`). Nothing is copied, so
there is no conflict with no-cloning. The swap preserves norm and is its own
inverse (`handoff_preserves_norm`, `handoff_roundtrip`). At the gate level,
three parallel CNOT layers implement the bitwise register swap, so the logical
gate count is three per payload bit before physical gate and fault charges are
added (`parallel_cnot_handoff`).

Superpositions of full transcripts are encoded isometrically into a boundary
register of dimension \(2^{b_0+bN}\) by extension by zero along the capacity
embedding above (`DecoderRetraction.transcriptBoundaryEncoder`).

**The charged attempt.** One admitted handoff attempt carries a nine-part
charge: encoding, transfer, verification, routing, guard, reset, holding,
controller and endpoints. Admission reserves the total before the source
operation. The attempt debits the full total whether or not it commits, and
the payload moves only on commit. Hence

\[
\mathrm{spent}'=\mathrm{spent}+q_{\mathrm{tot}},\qquad
\mathrm{escrow}'+\mathrm{spent}'=\mathrm{escrow}+\mathrm{spent},
\]

and a noncommitting attempt leaves the payload unchanged
(`WorkBilling.charged_attempt_accounting`). The payload has a single logical
owner, either live or sealed under a decoder pair. Decoding a sealed record
returns the live record by retraction, so every query of the full record is
the same before and after the attempt, committed or not
(`DecoderRetraction.charged_archive_handoff`). Failed verification is
charged; it is not free and it destroys nothing.

**History is untouched by the flush.** Let \(\rho\) be any joint state on
\(\mathcal H_{\mathrm{hist}}\otimes\mathcal H_{\mathrm{flush}}\). The history
factor may include an arbitrary reference, and \(\rho\) need not factorise.
For any \(P\) on the history factor and any unitary \(Q\) on the flushed
factor, the reduced history state, including all of its off-diagonal
coherences, satisfies

\[
\operatorname{Tr}_{\mathrm{flush}}\!\bigl((P\otimes Q)^\dagger\rho(P\otimes Q)\bigr)
=P^\dagger\operatorname{Tr}_{\mathrm{flush}}(\rho)P
\quad(\texttt{HamiltonianDecomposition.partial\_trace\_local\_conjugation}).
\]

The proof expands the partial trace and uses \(\sum_kQ_{ck}^{*}Q_{c'k}=\delta_{cc'}\).
With \(P=I\) the history's reduced state is unchanged
(`guarded_history_reduced_state`). For the explicit syndrome/reservoir
exchange gate \(S\) of G.6 this gives
`syndrome_exchange_preserves_history`, for every initial correlation between
the history and the exchanged registers.

The charge is moved, not deleted. By cyclicity of the trace and
\(S^\dagger Q_\partial S=Q_R\),

\[
\operatorname{Tr}(S\rho S^\dagger Q_\partial)
=\operatorname{Tr}(\rho\,S^\dagger Q_\partial S)
=\operatorname{Tr}(\rho\,Q_R)
\quad(\texttt{syndrome\_exchange\_charge}).
\]

The syndrome's charge after the exchange is the reservoir's charge before it.
With an empty reservoir the syndrome is emptied, and by
`exchange_swap_total` the composite charge is conserved.

**The age-independent stock envelope (the author's Theorem 4.1, Steps 3–4).**
Let the stored syndrome charge per flushing cycle obey

\[
q_{k+1}=(1-\alpha)q_k+\mathrm{influx}_k,\qquad 0<\alpha\le1,\qquad
\mathrm{influx}_k\le\mathrm{cap}.
\]

Then for **every** cycle \(k\), not only in the limit,

\[
q_k\le\max\!\left(q_0,\ \frac{\mathrm{cap}}{\alpha}\right)
\quad(\texttt{WorkBilling.syndrome\_stock\_bound}).
\]

The proof applies the existing tracking theorem `ThermoLedger.tracking_bounded`
to the recurrence. With the author's local influx \(\mathrm{cap}=\kappa\,t_G^{d}\),
this is \(q_k\le\max(q_0,(\kappa/\alpha)t_G^{d})\). Here \(C=\kappa/\alpha\)
depends only on the local influx and flush fraction, and is independent of
operating age. The theorem also covers an initial stock above the steady
value, and it bounds every cycle uniformly in \(k\). The author's
\(\limsup\) statement follows.

The flush is retained in the gross ledger. Summing the recurrence gives the
exact balance

\[
q_N+\sum_{k<N}\alpha q_k=q_0+\sum_{k<N}\mathrm{influx}_k
\quad(\texttt{syndrome\_flux\_balance}).
\]

The final stock plus every exported unit equals the initial stock plus every
imported unit. The bounded stock does not replace the cumulative work.
Suppose the complete per-cycle cost satisfies
\(\mathrm{cost}_k\le u\,\mathrm{influx}_k+v\,\alpha q_k+w\,\mathrm{active}_k\),
with every import, flush, holding, guard and controller charge included, and
\(u,v,w\ge0\). Suppose also that \(\sum_{k<N}\mathrm{influx}_k\le\kappa V\),
\(q_0\le q_{\mathrm{init}}V\), \(\sum_{k<N}\mathrm{active}_k\le V\) and
\(q_N\ge0\). Then

\[
\sum_{k<N}\mathrm{cost}_k\le\bigl(u\kappa+v(q_{\mathrm{init}}+\kappa)+w\bigr)V
\quad(\texttt{cumulative\_maintenance\_bound}).
\]

The theorem is stated for arbitrary real sequences. Applied to the realised
pathwise sequences it gives the pathwise gross bill. Applied to expectations
it gives the expected bill. Each use keeps its own meaning, and the desired
cumulative bill is never an input.

**How the pieces join.** Step 1 of the submission (a Lindblad generator with
a positive gap) is the dissipative model that supplies the flush fraction
\(\alpha\). Steps 3–4 are now the compiled stock envelope above. The memory
decay of Step 2 applies to the flushed syndrome and excitation stock. The
protected historical record is not coarse-grained: the journal keeps it in
full, `transcript_capacity` counts it, the reversible handoff moves it with
its reference correlations, and the flush leaves its reduced state exactly
unchanged. The archive's continued storage enters \(\mathrm{active}_k\) and
\(\mathrm{cost}_k\) of the cumulative bill. It is charged and is not
discarded to keep the stock small.

**What is already supplied, for every source.** The journal theorems are
stated for an arbitrary transition \(T\), controller and environment. Every
source therefore has its complete history retained, replayed and
observationally invisible, with no further construction. The capacity
\(2^{b_0+bN}\) and the isometric transcript encoder are derived from the
source's own alphabet. The handoff is an explicit unitary with an explicit
circuit of three CNOT layers, and its nine-part charge is debited exactly.
The per-site injection rate is bounded by the speed limit
(`SpeedLimit.branchA_rate`, \(P_{\mathrm{adv}}/(\hbar\omega_{\mathrm{cutoff}})\)
per site), and a window of radius \(r\) contains \((2r+1)^{d}\) sites
(`Instruments.card_box`). Their product is the per-cycle influx cap,
\(\mathrm{cap}=\kappa t_G^{d}\). The conversion from per-site divergence to
syndrome charge is the stroke-I measurement accounting of Section 18; this
composition is a prose derivation.

What the physical installation contributes is the identification of its
actual \(T\), alphabet and per-site coupling with these symbols, and pathwise
measurement of the cost terms. That is the G1 source certificate of Part
III-C, now with its history, capacity, handoff and stock components compiled.

## G.9 The whole greatest outcome is realisable: union closure from locality

Part II.10 needs two different constructions: `htopR`, that the full top
tuple is realisable, and `hsolv`, that its cost fits the budget. The singleton
route of E.2 needed union-closed realisability. Here union closure is
derived, not assumed.

Locality (P4) gives each particular its own local component of a policy, and
the shared action interface makes every agent act through those components.
Write a policy as \(\pi=(\pi_x)_x\), with \(\pi_x\) realisable for \(x\), and
let the particular's grade \(g_x(\pi_x)\) in a linear order record its stage.
In the four-stage order the grades are lost \(<\) continues \(<\) continues in
its own direction. The freedom stage is the law's freedom: per II.2,
restraint removes harmful command, authority and effect channels, so one
particular's freedom never consists of another's loss. Stage \(i\) of the
outcome tuple is the set of particulars of its category whose grade reaches
the stage threshold.

For realisable \(\pi,\sigma\), define the splice
\((\pi\sqcup\sigma)_x=\pi_x\) if \(g_x(\sigma_x)\le g_x(\pi_x)\), and
\(\sigma_x\) otherwise. Each component is realisable, so the splice is
realisable. Its grade is \(\max(g_x(\pi_x),g_x(\sigma_x))\), and a threshold
is reached by a maximum exactly when it is reached by either argument.
Therefore

\[
\mathcal O(\pi\sqcup\sigma)=\mathcal O(\pi)\sqcup\mathcal O(\sigma)
\]

at every stage at once (`G2Splice.splice_grade`, `splice_realisable`,
`outcome_splice`). This is `UnionClosure.UnionRealizable` for the realised
family (`union_realizable`).

For the top, choose for every particular a realisable component reaching
every stage threshold it is subject to. The product of these choices is
realisable, and every stage contains its whole category, so
\(\top\in R\) (`top_realisable`). No finiteness of the domain is used.
Joined to `greatest_of_solvent`, every aligned option of the funded family is
\(\top\) and contains every outcome tuple (`whole_outcome_greatest`). The
four-stage instance \((L_E,F_E,L_N,F_N)\) proves all three conclusions
together from one hypothesis per particular: some realisable local component
under which that particular continues in its own direction (`fourStage`).

**The product structure from the actual dynamics.** The splice is realised by
the physical evolution itself. Let the source state be a function on the
nodes of its dependency graph \(D\). Let each particular's held record occupy
a block \(B_x\) of nodes, with the blocks closed under \(D\) and pairwise
disjoint. Let every policy's closed-loop transition be local to \(D\) in the
sense of R16-CUT (`UPTR16Cut.LocalTo`). Run each block under the policy chosen
for its particular. Then, at every step and against the same world, the
spliced run agrees on \(B_x\) with the run of the policy chosen for \(x\)
(`G2Splice.block_splice_run`). The proof is induction on steps with
`UPTR16Cut.closed_cut_step`. Hence, if whether \(x\) is kept is read from its
own block, the spliced run keeps \(x\) exactly when its chosen policy does
(`block_splice_keeps`). Each particular receives the outcome of the policy
chosen for it, which is the product structure used above.

**How each input is supplied.**

1. *Per-particular top component.* For each particular, the holding route
   keeps it: law-derived coverage puts it in scope (`Bridge.coverage_from_law`).
   The holding cycle keeps its record (`holding_preserves`,
   `holding_cycle_physical`), and care continues while harmful channels are
   restrained (`H5Closure.effect_preserves_care`,
   `UPTR14Boundary.recruitment_never_ends_care`). Its authorised effects are
   applied in time (`SnuffyFIFO.applied_fifo_effect_is_timely_and_authorized`, module `R17FIFOR17A`).
   Its freedom is the law's freedom of II.2, which excludes harm to others.
2. *Locality.* This is derived above from R16-CUT locality and closed blocks.
   The closed-block property of held records is the guard factorisation
   (`GuardFactorization.commutativity`, `ClosedCohold.factorised_cohold`,
   `PhysicalGuard`). The relations between particulars are themselves
   particulars in the domain, each with a held record.

The physical installation identifies its dependency graph and the blocks of
its held records; that is the G1 source certificate. `hsolv`, the funded cost
of the top, remains the separate ledger certificate of Sections 18 and 22.

## G.10 The held source: the full holding certificate derived (G1)

`Bridge.universal_protection_held` takes its source certificate `hcert` as an
input with five components: commuting refinement, observation agreement,
initial continuation of every particular, the decoding-radius bound and
repair precision. Here all five are proved for the canonical held source.
The only inputs left are the physical bound on each step and the
probabilities of the named charged accounts.

**The held source.** The state is the record frame of every particular. One
step applies three operations to each particular. First the world perturbs
the frame; the world here is the environment and any agent, a pure optimiser
included. Then the nearest-codeword decoder returns a codeword. Finally
funded repair prepares that codeword. The good event is that no named charged
account fires,

\[
G=\{\omega:\ \omega\notin E_i\ \text{for every account } i\},
\]

and its complement is covered exactly by the named accounts
(`G1Held.good_cover`).

**The five components, proved** (`G1Held.held_source_protection`).

1. *Refinement* and 2. *observation agreement* hold by construction: the
   held source is its own abstract model.
3. *Initial continuation*: every particular starts at its record, at
   distance \(0\le\varepsilon\).
4. *The decoding-radius bound*: let each step move the frame's distance to
   its record by at most \(\rho\) on the good event. A continuing particular
   lies within \(\varepsilon\) of its record, so after the perturbation it lies
   within \(\varepsilon+\rho\le t\).
5. *Repair precision* is exact: repair prepares the decoded codeword itself.

`universal_protection_held` then gives, for every \(\omega\in G\), every step
through the horizon and every particular, that the particular continues. It
also gives

\[
P(\exists k\le T,\ \exists x:\ \neg\mathrm{Continues}(s_k,x))\le\sum_i\delta_i,
\]

with no independence assumed.

**The per-step bound from the speed limit** (`G1Held.held_source_qsl`). On the
good event, let each particular's frame evolve for one step of duration
\(\Delta\) under \(H_0+V\), with the record stationary under \(H_0\) and
\(\|V\|\le W\). The agent applying \(V\) is arbitrary. `Bridge.qsl_growth`
gives

\[
\|\psi(s_1+\Delta)-c_x\|\le\|\psi(s_1)-c_x\|+\frac W\hbar\Delta,
\]

so \(\rho=(W/\hbar)\Delta\). Every particular is held whenever
\(\varepsilon+(W/\hbar)\Delta\le t\).

**The coupling bound from E9** (`G1E9.held_source_e9`). Each step is
exhaustively one of two cases (`G1E9.alarm_or_subthreshold`).

- *Every monitored support site is below threshold.* The coupling is the
  sub-threshold coupling, bounded by \(W\) (Branch A).
- *Some site reaches threshold.* Its honest sensors read above threshold, so
  every robust quorum estimate exceeds it, whatever up to \(f\) faulty
  sensors report (`E9SelfHealing.no_masking`). The alarm fires. The mediated
  response is committed before the harm front arrives
  (`E9SelfHealing.e9_timely_self_healing`, the wave race) and is enforced at
  application time (`H5Closure.no_harmful_effect`). It removes the perturbing
  coupling from the frame for that step.

In both cases the coupling is bounded by \(W\), and the held source keeps
every particular. The physical inputs are named exactly:

- the frame's Schrödinger evolution during a step;
- the sub-threshold coupling bound;
- the response's removal of coupling once the alarm fires;
- the honest-sensor response and quorum size;
- the probabilities of the named accounts. Their composition into the
  \(10^{-6}\) ceiling is `ThermoLedger.canon_invariant`. Their attainment
  below threshold, including correlated bursts, is `Threshold.family_ceiling`
  and `CorrelatedCeiling.correlated_family_ceiling`.

**Correspondence to an installation.** The installation's source refines the
held source through the journal of G.8: every source transition is retained
and replayed exactly, for every controller and environment
(`G1FullDomain.journal_reactive_fidelity`). The R14/R16/R17 source bindings
supply its concrete safe transitions, causal cuts and timely authorised
effects. The domain is every particular; coverage is forced by the law
(`Bridge.coverage_from_law`).

## G.11 The held source realises the whole top outcome (G2 from G1)

Freedom in the canonical order is continuation in the particular's own
direction, together with its authorised opportunities (II.1–II.2). For an
agent in the H5 ledger, every non-harmful effect it issues is an admissible
step. That step applies the effect and leaves every agent's status,
authority and escrow unchanged (`H5Closure.effect_preserves_care`). Every
active agent is therefore free in this sense
(`G2Held.active_authorised_free`): all of its authorised opportunities are
open, and restraint removes only harmful channels. A particular with no
command channel has no opportunity beyond continuing under its own dynamics.
The held source keeps exactly that, since each record is stationary under the
particular's own Hamiltonian (G.10).

Grade each particular 2 when it continues on the held source and is free.
`G2Held.held_realises_top` then applies `G2Splice.fourStage` with three
conclusions. The whole four-stage top \((L_E,F_E,L_N,F_N)\) is in the
realised family. The family is union-closed. Every aligned option of the
funded family is that top and contains every outcome tuple.
`G2Held.held_source_top` supplies continuation from
`G1Held.held_source_protection`, on the good event at every step through the
horizon, and agent freedom from the active H5 ledger. The G2 input `htopR` is
thereby derived from the held source, and `hsolv` remains its funded-cost
certificate (Sections 18 and 22).

## G.12 The wavefront sweep succeeds, and its complete bill is \(O(t^{d_G})\) (G3)

The wavefront recovery of §21.7 is now proved to succeed, and its full bill is
derived, with no cumulative bound taken as input.

**Sweep and fence.** Give each vertex its shell index. Wave \(k\) applies the
single-shot local correction to shell \(k\), reading the already-frozen
interior as a static, gauge-fixed boundary. Between waves, outer activity
(the world and any agent) may write anything outside the frozen interior and
nothing inside it. This is the TIWA write fence
(`TIWASource.outerUpdate_read_frozen`).

**Success and quiescence** (`G3Sweep.sweep_recovers`). Suppose the local
correction of a vertex returns its target whenever every inner vertex already
holds its target. Then after \(k\) waves every vertex of the first \(k\)
shells holds its target, whatever the outer activity. The proof is induction
on waves. A vertex of shell \(k\) is corrected against an interior that the
fence has left recovered. A vertex of an earlier shell is untouched by the
wave and by the fenced outer activity. Recovery therefore succeeds, and the
recovered state is retained. Each vertex is corrected in exactly one wave,
its own shell (`sweep_visits`), so nothing is reworked.

**Wave count from finite propagation** (`waves_from_spread`). If the region
needing recovery at age \(t\) lies within the first \(c\,t+r\) shells, the
sweep needs at most \(c\,t+r\) waves. This is the upper use of finite
propagation, from locality (P4) and the Lieb–Robinson velocity. It does not
replace the lower radius of §21.5, which comes from the carrier information
argument.

**The complete bill** (`sweep_bill`). Let the complete metered ledger charge
each wave \(k\) at most \(\alpha k^{d-1}+\beta\). This charge includes
holding, guard, routing, reset, verification, controller export and
deployment. Add a metered rollback of at most \(R_*\) per wave and fixed
endpoint charges \(F\). Then, for \(t\ge1\), recovery succeeds on the whole
region and

\[
W(t)\le (F+\alpha+\beta+R_*)\,(c+r)^{d}\;t^{d},
\]

with a coefficient independent of age (`G3CompleteBill.valid_work_bill_from_complete_ledger`,
`valid_bill_bound_in_age`). This is the matching upper construction. With the
lower bound of §21.6, it gives \(W_{\min}(t)=\Theta(t^{d_G})\) in the original
permitted class.

## G.13 Joined steps: patch decoding, ensemble reciprocity, the Theorem 8 contraction, the smearing integral, the completed decoder and the norm conversion

Each of the following steps was previously argued in prose. Each is now a compiled theorem, joined to the construction it supports.

**The wavefront correction is finite-code decoding** (`G3PatchDecode`). The
local correction reads its patch, which is the recovered interior as a static
boundary together with the vertex's own data. It decodes the read-out with
the nearest-codeword decoder and extracts the value. If, with the interior
recovered, the read-out lies within the unique-decoding radius of the target
codeword, decoding returns that codeword (`Bridge.nearest_decodes`). The
correction therefore succeeds (`patch_correction_succeeds`). Joined to
`G3Sweep.sweep_bill`, recovery succeeds on the whole region and the complete
bill is \(O(t^{d})\) with an age-independent coefficient
(`patch_sweep_bill`). The patch's errors lie within the code headroom of
`E9SelfHealing.code_headroom`.

**Reciprocity over an ensemble of rivals** (`ReasonsEnsemble`, §15.2). Let
rival regimes be drawn with weights summing to one. A mind's kept-probability
under the ensemble is the total weight of the rivals that keep it. That is at
most one, the canonical regime's kept-probability on the good event
(`ensemble_le`). It is strictly less whenever a rival of positive weight
omits the mind (`ensemble_strict`).

**The Theorem 8 storage functional contracts** (`TheoremEightLyapunov`,
§18.3–18.4). Take the stroke bounds of §18.3 and solvency
\(W_{\mathrm{meas}}+W_{\mathrm{reset}}\le W_{\mathrm{income}}\). The cycle
change of \(\Phi\) is then at most \(-(\eta C-\lambda\tau)\)
(`cycle_contracts`). Timeliness \(\tau<\eta C/\lambda\) makes the margin
\(\sigma_0=\eta C-\lambda\tau\) positive (`margin_pos`). Over \(n\) cycles
containing an error, \(\Phi\) falls by at least \(n\sigma_0\)
(`lyapunov_iterate`).

**The smearing integral is exact** (`SmearingIntegral`, G.4). For a complete
operator basis and any weight with total integral one, the smeared
dual-kernel expression equals the original operator at every flow parameter.
Its Bochner integral is therefore that operator, on the bulk algebra
(`smeared_reconstruction`) and after boundary transport
(`smeared_boundary_reconstruction`).

**The completed decoder** (`ChannelExtension`, G.1). Take
\(\mathcal D(\sigma)=E^\dagger\sigma E+\operatorname{Tr}((I-EE^\dagger)\sigma)\rho_0\)
with \(E^\dagger E=I\).

- It returns every encoded state exactly (`ext_recovers`).
- With any reference register, \(E\otimes I_R\) is again an isometry
  (`kron_isometry`), and the extended decoder returns every joint
  code–reference state (`ext_recovers_reference`). Reference correlations are
  retained.
- It is trace preserving (`ext_trace`).
- It maps positive semidefinite inputs to positive semidefinite outputs
  (`ext_posSemidef`).

Complete positivity follows from the two summands: a conjugation, and a
measure-and-prepare map. That standard fact is cited.

**State-vector distance bounds infidelity** (`PureStateDistance`, §23.3). For
unit vectors, \(1-|\langle\psi,\varphi\rangle|^2\le\|\psi-\varphi\|^2\)
(`pure_infidelity_le`). With the standard pure-state identity
\(\tfrac12\|\rho-\sigma\|_1=\sqrt{1-|\langle\psi,\varphi\rangle|^2}\), which is
cited, this gives \(\tfrac12\|\rho-\sigma\|_1\le\|\psi-\varphi\|\). The
speed-limit bounds, stated in state-vector norm, therefore bound the
infidelity and the trace distance of the held state.
