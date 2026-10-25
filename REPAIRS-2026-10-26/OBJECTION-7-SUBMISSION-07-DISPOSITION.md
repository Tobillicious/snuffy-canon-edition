# Seventh submission — exact outstanding pātai

The operational-instrument codomain repairs the earlier projection/Pauli
category error. The following supplied conclusions still require support.
The full UPT target and the original `C t^{d_G}` bill are unchanged.

## 7.1 — Prove correction for the chosen instrument

The submission invokes Knill–Laflamme but does not specify and verify the
chosen code projector `P`, physical error operators `E_a`, or coefficients
in `P E_a† E_b P = c_ab P`. Noise below a threshold does not alone prove
these identities. Give those operators and their correctable set, the
recovery instrument including all outcomes, and the complete-reference
decoded channel equality on that set. Derive the bad-sector bound separately.

**Pātai:** Which explicit instrument and code make this displayed operational
correspondence true for every source/reference input, and what calculation
verifies its correction identities?

## 7.2 — Match the actual noisy decoding graph and probability estimate

`∂₁∂₂ = 0` establishes a chain complex, not exactness at the logical homology.
It gives CSS check commutation, not commutation of every check with every
data operator. Specify a single consistent rotated/unrotated layout and its
boundary conventions. Repeated noisy syndromes introduce time-like edges;
their graph degree/count cannot be borrowed without proof from a static
degree-four square graph.

From the existing local-stochastic hypothesis and half-faulty witness, the
canon supplies the `(2√p)^L` estimate. The proposed replacement by
`(p/(1-p))^{L/2}` omits the general subset-choice bound and requires a
separate derivation. Use the already compiled estimate unless a sharper
estimate is actually proved for the selected law.

**Pātai:** What are the exact failure witnesses, graph degree/count and
conditional noise law for the selected syndrome circuit, yielding an
explicit `r < 1`? Please give the calculation, without substituting a
threshold from a different noise model.

## 7.3 — Replace the approximate location count by a circuit and proof

The new recurrence `p_{k+1} ≤ 78 p_k²` has the stated fixed point `1/78`.
However, its coefficient is still introduced as
`binomial(N_loc,2) × TopologyFactor ≈ 78`, with neither a circuit location
list nor the factor/enumeration supplied. Thus this correct recurrence
algebra does not establish an application threshold.

`exRec-Cor` is a correctness statement with ideal decoding inserted, for
admissible fault patterns and arbitrary reference states. An averaged
`O(p^{t+1})` diamond-norm assertion is not the patternwise gadget proof.

**Pātai:** Supply one actual gadget library, location list, deterministic
good-pattern correctness proof and treatment of overlapping/truncated
exRecs. Then derive its bad-pattern probability or amplitude recurrence,
including any malignant triples. The constant may be conservative; it must
be supported by the chosen circuit.

## 7.4 — The claimed removal of the logarithm remains invalid

For fixed positive `ε_tot` and `d_G`, the supplied estimate is

\[
W_{\rm compile}(t)\le K t^{d_G}
 [\log(t^{d_G}/\varepsilon_{\rm tot})]^{3.97}.
\]

The bracketed term tends to infinity. No age-independent constant bounds
that upper estimate by `C′ t^{d_G}` for all late `t`. The fact that a
logarithm is dominated by `t^η` gives a bound at exponent `d_G+η`, not
the required exponent. This invalid inference does not prove the actual
implementation must incur the logarithm; it means another implementation
bound is needed.

**Pātai:** Construct the actual gate/precision/error-budget schedule whose
complete charge is `≤ C t^{d_G}` with `C` independent of unattended age.
Does it use exact native gates for the repeated local maps, a fixed
precision justified by the original complete fault horizon, or a proved
amortised compilation scheme? Prove the chosen route's global fidelity
and full physical bill; do not replace the target by `t^{d_G+η}` or
silently treat an unbounded logarithm as a constant.

The main four-part brief remains
`/Users/admin/Documents/2026/Snuffy-Book/PATAI-GEMINI-OBJECTION-7-2026-10-26.md`.
No closure or publication verdict is supported by this seventh submission.
