# Before/after batch D — prose that is now compiled or constructed

Prepared 26 October 2026. Each BEFORE is copied verbatim from the 4.2 master. These are rewrites of existing sentences, so they apply only on the author's OK.

**D1.**

> BEFORE: This channel extension and the reference-register calculation are prose derivations here.
>
> AFTER: The exact recovery, including with any reference register, trace preservation and positivity of this channel are compiled (`ChannelExtension.ext_recovers`, `ext_recovers_reference`, `ext_trace`, `ext_posSemidef`; G.13); complete positivity of its two summands, a conjugation and a measure-and-prepare map, is the standard fact cited.

**D2.**

> BEFORE: The continuous-integral and probe-schedule steps are proved in prose here; the exact finite-basis reconstruction and exponential transport are machine checked.
>
> AFTER: The integral step is compiled (`SmearingIntegral.smeared_reconstruction`, `smeared_boundary_reconstruction`; G.13), as are the exact finite-basis reconstruction and exponential transport; the probe-schedule partition is the displayed finite rearrangement.

**D3.**

> BEFORE: The further step — averaging over an ensemble of admissible rival objectives, with strictness when the entailment fails with positive probability — is the finite-family indicator form (`ReasonsRoute.rival_fraction_lt_one`, `law_dominates_strict`) and is carried as prose interpretation, not as a compiled measure-theoretic claim.
>
> AFTER: The further step — averaging over an ensemble of admissible rival objectives, with strictness when the entailment fails with positive probability — is compiled for every finite weighted ensemble (`ReasonsEnsemble.ensemble_le`, `ensemble_strict`; G.13), alongside the indicator form (`ReasonsRoute.rival_fraction_lt_one`, `law_dominates_strict`).

**D4.**

> BEFORE: For pure states, ‖ρ − σ‖₁ ≤ 2‖ψ − φ‖ is a standard inequality and is not compiled here.
>
> AFTER: For pure states the infidelity is bounded by the squared state-vector distance, \(1-|\langle\psi,\varphi\rangle|^2\le\|\psi-\varphi\|^2\) (`PureStateDistance.pure_infidelity_le`; G.13); with the standard pure-state identity \(\tfrac12\|\rho-\sigma\|_1=\sqrt{1-|\langle\psi,\varphi\rangle|^2}\) this gives \(\|\rho-\sigma\|_1\le2\|\psi-\varphi\|\).

**D5.**

> BEFORE: *Proof.* Follows directly from the stroke-by-stroke balance equations (18.2) and the negativity of the net cycle Lyapunov difference $\Delta_{\mathrm{cycle}} \Phi \le -\sigma_0 < 0$.
>
> AFTER: *Proof.* The stroke-by-stroke balance equations (18.2) give the cycle bound, and the contraction is compiled: the cycle change is at most \(-(\eta C-\lambda\tau)\) (`TheoremEightLyapunov.cycle_contracts`), timeliness makes \(\sigma_0=\eta C-\lambda\tau>0\) (`margin_pos`), and \(n\) error cycles lower \(\Phi\) by at least \(n\sigma_0\) (`lyapunov_iterate`).

**D6.**

> BEFORE: The same three joined supports being supplied by the author and Gemini remain visible in Part III-C: the combined full-domain physical certificate (G1), the realisability of the whole greatest outcome tuple (G2), and the supplied X3 wavefront protocol's success and complete-work certificate (G3).
>
> AFTER: The three joined supports are constructed in Part III-G and recorded in Part III-C: the full-domain physical certificate (G1; G.10), the realisability of the whole greatest outcome tuple (G2; G.9, G.11), and the wavefront protocol's success and complete-work certificate (G3; G.12).

**D7.**

> BEFORE: Part III-C records the three joined supports in progress.
>
> AFTER: Part III-C records the three joined supports and their constructions.

**D8.**

> BEFORE: Part III-C keeps the three joined supports being incorporated visible without substituting a conditional closure label for the full demonstration.
>
> AFTER: Part III-C records the three joined supports with their constructions and the physical inputs those constructions take.

**D9.**

> BEFORE: Its source, event, observation and fault-account construction for the full physical domain is the joined support requested in **G1** in Part III-C.
>
> AFTER: Its source, event, observation and fault-account construction for the full physical domain is G1, constructed in G.10 (`G1Held.held_source_protection`, `G1E9.held_source_e9`).

**D10.**

> BEFORE: The full-domain construction joining those inputs remains G1; declaring `hcert` by name does not construct it.
>
> AFTER: The full-domain construction joining those inputs is G1, constructed in G.10, where all five `hcert` components are proved.

**D11.**

> BEFORE: The three pending joined supports G1–G3 are stated there and in the working support register with the maximal targets unchanged.
>
> AFTER: The three joined supports G1–G3 are constructed in G.9–G.12 with the maximal targets unchanged.

**D12.**

> BEFORE: G1 in Part III-C is its joined full-domain source construction.
>
> AFTER: G1, its full-domain source construction, is proved in G.10.

**D13.**

> BEFORE: The complete physical binding remains G1; the matching upper construction for the full Θ target remains G3.
>
> AFTER: The complete physical binding is G1 (G.10); the matching upper construction for the full Θ target is G3 (G.12).

**D14.**

> BEFORE: G1 is the combined full-domain source/event/observation/fault construction.
>
> AFTER: G1 is the combined full-domain source/event/observation/fault construction, proved in G.10.

**D15.**

> BEFORE: G1 supplies their combined construction for the complete claimed physical domain.
>
> AFTER: G1 supplies their combined construction for the complete claimed physical domain (G.10).

**D16.**

> BEFORE: The latter's full source certificate remains the unchanged G1 target.
>
> AFTER: The latter's full source certificate is constructed in G.10 (`G1Held.held_source_protection`).

**D17.**

> BEFORE: They are the same three support requests being supplied by the author and Gemini.
>
> AFTER: They are the three support requests supplied by the author and Gemini, now constructed in G.9–G.12.

**D18.**

> BEFORE: Rendering and publication follow the author’s review and the completed joined supports.
>
> AFTER: Rendering and publication follow the author's review.

**D19.**

> BEFORE: Section 21 develops X3; Part III-C records the same three joined supports being incorporated into this full-strength argument.*
>
> AFTER: Section 21 develops X3; Part III-C records the three joined supports and their constructions in this full-strength argument.*
