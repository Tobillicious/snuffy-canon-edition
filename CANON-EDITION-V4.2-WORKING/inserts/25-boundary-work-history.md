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
