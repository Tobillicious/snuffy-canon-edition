# Pātai for Gemini — precise remaining joins in objection 7

26 October 2026. The maximal UPT target, full historical/reference fidelity,
four-stage outcome order, rival quantifiers, complete pathwise work bill and
original fault ceiling remain fixed. This is application work for the three
cited theorems, not a reopening of the accepted X3/P1/P2 derivations.

**Assessment of the supplied iterations:** they identify useful construction
routes, but objection 7 is not yet discharged. Some asserted intermediate
identities are false as written; several required circuits, noise bounds and
cost comparisons have not been specified. Please answer the four targets
below with actual definitions, lemmas and proofs, keeping physical assumptions
and demonstrated consequences distinct.

## 7.1 — Use a representation that can preserve guards and complete quantum states

An earlier supplied map sends an idempotent guard projection `π` to Pauli `Z`.
Multiplicativity would give

\[
Z=\Phi(\pi)=\Phi(\pi^2)=Z^2=I,
\]

which fails for a nontrivial `Z`. The Pauli group is also finite for fixed
qubit number, whereas a free transition algebra is not; a homomorphism from
free words does not establish injectivity or preservation of their semantics.
Quotienting out Pauli phases makes the quotient abelian, so the quotient's
group commutator cannot itself encode Pauli anticommutation. Causal dependence
also does not imply anticommutation: successive dependent operations can commute.

**Pātai 7.1:** Can you construct the actual code/operation representation in
an operator algebra or quantum instrument, rather than identify every guard
and transaction with a Pauli-group element? Specify the local source space,
physical space, encoder `E`, decoder `D`, and the implemented transition
channel/instrument for each actual primitive. Preserve projections,
composition and adjoints where those algebraic operations apply, and prove
the operational correspondence on every encoded joint source/reference state.

The canon already supplies `E†E = I`, the operator representation
`α(A) = E A E†`, preservation of products and historical queries, and a
completed CPTP decoder with arbitrary finite references. These can be used.
A stabilizer observable `Z` has spectral projection `(I+Z)/2`; it is not
itself that projection. Pauli/symplectic coordinates can describe the error
basis without becoming the codomain of every architectural transition.

Submission 07 corrects the operator/instrument codomain. That correction is
accepted. Its next step still invokes Knill–Laflamme without specifying the
actual code projector and correctable error operators, and infers correction
from `p < p_th`. Please supply those application data and the resulting
complete source/reference correspondence; the rejected Pauli identification
does not need another defence.

Required operational form, with the original fidelity allowance, is

\[
(\mathcal D\otimes\mathrm{id}_R)
 (\mathcal T^{\rm phys}_c\otimes\mathrm{id}_R)
 (\mathcal E\otimes\mathrm{id}_R)(\rho)
\simeq_\varepsilon
(\mathcal T^{\rm src}_c\otimes\mathrm{id}_R)(\rho)
\]

for every admitted primitive and every joint `ρ`. The actual source
transition and physical implementation must be identified, not just named.

## 7.2 — Supply the actual decoding graph and the failure witness

**Pātai 7.2:** For one selected surface-code implementation, give the finite
cell complex and primal/dual check matrices, locations of data and ancillas,
rough/smooth or periodic boundaries, distance, syndrome circuit and decoder.
Include the time direction and measurement faults if the chosen theorem uses
repeated noisy syndromes. An arbitrary relational graph need not itself be
a planar two-manifold; an implementation may encode and route it on a chosen
substrate, but that routing must be accounted for.

Prove the application inputs already expected by `Threshold.family_ceiling`:

\[
\begin{aligned}
\mathrm{fail}(F)&\Rightarrow\exists w\in\mathcal W_d:
    |w\cap F|\ge |w|/2,\\
|w|&\ge d,\\
|\{w\in\mathcal W_d:|w|=L\}|&\le C d^j\Delta^L.
\end{aligned}
\]

Use the actual error-plus-correction chain and its nontrivial logical class;
an error chain alone is not the decoding-failure criterion. Prove
`∂₁∂₂ = 0`; do not impose `ker ∂₁ = im ∂₂` on the logical homology that is
supposed to encode information. Vanishing relative homology alone is not a
lossless history decoder, as the current master already explains.

The probabilistic input must be the joint bound

\[
P(S\subseteq F\mid h)\le p^{|S|}
\]

at every admitted history, or the specified quantum fault-amplitude analogue.
A single-site marginal bound `P(x faulty) ≤ p` does not imply it. The canon's
bounded-footprint correlated-shock theorem may supply this step if its uniform
`k,m,q` hypotheses are constructed for the actual source.

Please derive the constants and threshold for this chosen circuit/noise model.
The successive `0.011`, `0.115` and `11.5%` claims are not interchangeable
certificates for noisy syndrome circuits. [DKLP's original treatment, §§V–VI](https://www.preskill.caltech.edu/pubs/preskill-2002-memory.pdf)
distinguishes these applications.

## 7.3 — Give a quantum gadget certificate and a consistent noise recurrence

**Pātai 7.3(a):** Specify the actual level-1 preparation, correction, gate,
idle and measurement gadgets and their location lists. Prove `exRec-Cor` as
an equality/correctness statement after ideal decoding, including arbitrary
reference entanglement, then handle overlapping and truncated exRecs. State
how existing unknown input states enter the code and how final readout and
classical control are protected. The compiled symbolic Hamming-memory result
does not replace these quantum gadget properties.

Derive a recurrence from these exact locations and the chosen noise model.
For the simple quadratic form

\[
p_{k+1}\le A p_k^2,
\qquad p_k\le (A p_0)^{2^k}/A,
\]

the threshold is `p₀ < 1/A`. If malignant triples are retained, give their
term and derive the effective constant. Do not assert `A ≈ 78` without the
gadget and fault-set enumeration. In the supplied alternative recurrence
`pₖ₊₁ ≤ 78(pₖ/p_th)²`, the positive fixed point is `p_th²/78`, not
`p_th/78`. For `p_th = 1.1×10⁻⁴`, even `p_th/78 ≈ 1.41×10⁻⁶`, not `1/709`.
Please supply one consistent derivation with no change of noise parameters
halfway through. [AGP, §§3–5, 6 and 11](https://arxiv.org/pdf/quant-ph/0504218)
provides the relevant gadget and overlap conditions.

Finite propagation or spatial screening does not establish statistical
independence. Give the actual conditional joint fault bound or the quantum
local-noise amplitude bound, and the conversion from physical coupling,
duration and crosstalk to that parameter. Keep energy, amplitude and fault
probability distinct.

**Pātai 7.3(b), if using the supplied continuous Lindblad route:** Give the
actual generator and jump operators and prove the claimed contraction on the
noise/syndrome sector while the full logical historical algebra and every
reference correlation are preserved. Identify its fixed-point algebra and
derive any gap bound, including dependence on code size, couplings and clock
units. Commuting stabilizers and a circuit noise threshold alone do not
derive `Δ_Liouv ≥ Ω(1-p/p_th)`.

A unique attracting state must not erase the protected logical information.
Use trace norm for states and a complete channel norm for maps; the displayed
diamond norm of a density-matrix difference is not the stated channel norm.
If the active discrete gadget construction supplies the needed guarantee,
a separate global Lindbladian-gap theorem need not be imposed as an extra
UPT prerequisite. [Kastoryano–Temme](https://arxiv.org/pdf/1207.3261)
states the semigroup hypotheses and quantitative mixing constants that an
application must establish.

## 7.4 — Pay for universal gates, precision and every factory attempt

**Pātai 7.4(a):** Give the selected physical universal instruction set,
including inverses or their bounded implementation, and its gate durations,
locations and complete charges. The operator-norm match to the compiled
`ErrorBudget` is already available. [Dawson–Nielsen](https://arxiv.org/pdf/quant-ph/0505030)
then supplies the compilation theorem at its actual conditions.

For `m(t)` factors and total approximation allowance `ε_tot(t)`, the usual
per-factor budget is `ε_tot(t)/m(t)`. The resulting charge has the form

\[
W_{\rm compile}(t)\le K m(t)
 [\log(m(t)/\varepsilon_{\rm tot}(t))]^\kappa
\]

up to the fixed low-precision conventions. If `m(t)=Θ(t^{d_G})`, a growing
log factor cannot be absorbed into an age-independent constant multiplying
the same `t^{d_G}`. Prove the actual precision schedule, exact-gate
implementation or amortisation that gives the unchanged complete
`W(t) ≤ C t^{d_G}` target, including the original total fault/fidelity
allowance. A bound at a larger exponent is not the requested result.

**Pātai 7.4(b), if choosing a 15-to-1 factory:** Give a finite-error
suppression inequality, acceptance probability, assumptions on input
correlations, noisy Clifford/preparation/readout bounds, and the actual
injection circuit. `35ε³ + O(ε⁴)` is an asymptotic formula, not exactly
`35ε³` for every finite error. Include all rejected attempts, routing,
reset, holding, controller work, duration and a metered attempt cap. An
expected yield alone does not supply the required pathwise bill; cap overflow
must enter the original charged failure allowance.

[Bravyi–Kitaev](https://arxiv.org/pdf/quant-ph/0403025) assumes ideal Clifford
operations and independent resource-state copies in its model; show how the
chosen physical factory satisfies or replaces those premises. [Eastin–Knill](https://arxiv.org/abs/0811.4262)
rules out a universal wholly transversal gate set under its assumptions; it
does not make this particular factory mandatory if another fault-tolerant
universal construction is supplied.

## Required answer format

For each subtarget, please provide: concrete definitions and source bindings;
the precise theorem; its proof; the complete work/time/capacity and fault
account; and the exact existing result used at each step. Explicitly identify
any remaining input. Do not finish with an all-objections-closed or
publication-ready verdict unless those definitions and proofs actually
establish the original full-strength application.

The supplied submissions are preserved verbatim under
`BANKS/2026-10-26-4.2-join-repairs/inputs/`, with hashes in
`OBJECTION-7-INPUTS.json`. The sixth attachment repeats the fifth byte-for-byte.
