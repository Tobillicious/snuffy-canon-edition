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
