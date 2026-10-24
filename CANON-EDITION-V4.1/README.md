# Canon Edition v4.1 — Summit 1 closed: von Neumann's alternating projection theorem

The operator bridge of the H5 meet algebra is now machine-checked end to end. In a Hilbert space, for closed subspaces A and B and every vector x,

\[
(P_A P_B)^n x \longrightarrow P_{A\sqcap B}\,x
\qquad\text{and}\qquad
(P_B P_A)^n x \longrightarrow P_{A\sqcap B}\,x
\]

in norm. Together with the identification step already proved in `MathlibAnalyticBridge.lean`, this gives Chapter 4's meet \(P_{\phi\wedge\psi}=\lim_n(P_\phi P_\psi)^n\) as a theorem, not a declared hypothesis.

## What is here

| File | Content |
| --- | --- |
| `lean/Snuffy/CanonVonNeumann.lean` | **New.** The existence step. Discharges both `limit` fields of `VonNeumannConvergence A B (A ⊓ B)` (`canon_von_neumann_convergence`), the same structure in its `Snuffy.Opial` form (`canon_opial_convergence`), and the scalar norm limit that the Pythagoras upgrade takes as input (`opial_norm_sq_tendsto`, `opial_route_closes`). |
| `lean/Snuffy/CanonVonNeumannAudit.lean` | **New.** Prints the axioms of each headline result. |
| `lean/CanonVonNeumann.receipt.txt` | Compile receipt: exit 0, zero output, zero `sorry`, `leanchecker` exit 0, axiom audit, source hashes. |
| `lean/Snuffy/MathlibAnalyticBridge.lean` | The canon tree's bridge with the full identification step (`von_neumann_identification`), unchanged. |
| `lean/Snuffy/HalperinDecay.lean`, `lean/Snuffy/OpialBridge.lean` | The v4.1 engines (Bregman asymptotic regularity; weak-cluster lemmas and the invariant Pythagoras upgrade), unchanged. |

The three unchanged modules are byte-identical to the author-side canon tree (hashes in the receipt).

## The proof

With \(T=P_AP_B\):

1. \(T\) is linear and contractive, and \(T^n\) fixes \(A\sqcap B\).
2. **Successive steps vanish.** Halperin's chain identity gives \(\|T^nz-T^{n+1}z\|\to0\) for every \(z\) (`HalperinDecay.asymptotic_regularity`).
3. **The complement of the range.** If \(w\perp(z-Tz)\) for all \(z\), then \(P_BP_Aw=w\); so \(\|P_Aw\|=\|w\|\), Pythagoras gives \(w\in A\), and then \(w\in B\). Hence \(\operatorname{range}(I-T)^\perp\le A\sqcap B\).
4. **Density.** In a Hilbert space \(K^{\perp\perp}=\overline K\), so \((A\sqcap B)^\perp\subseteq\overline{\operatorname{range}(I-T)}\).
5. **Decay on \((A\sqcap B)^\perp\).** For \(u=z-Tz\), \(T^nu=T^nz-T^{n+1}z\to0\). Approximate any \(y\perp A\sqcap B\) by such a \(u\) within \(\varepsilon/2\); contraction keeps \(\|T^n(y-u)\|<\varepsilon/2\) uniformly in \(n\).
6. **The limit.** \(T^nx=P_{A\sqcap B}x+T^n(x-P_{A\sqcap B}x)\to P_{A\sqcap B}x\). The mirrored product is the same theorem with \(A,B\) exchanged, since \(B\sqcap A=A\sqcap B\).

Setting: a complete inner product space — the Hilbert space of von Neumann's theorem and of Chapter 4. The identification step needs no completeness.

## Reproduce

Lean 4.35.0 and Mathlib rev `56a005855ea1`. From a Mathlib project at that revision, with `LEAN_PATH` set to its oleans plus a build directory, compile in order with `lean -R CANON-EDITION-V4.1/lean -o <build>/Snuffy/<Module>.olean CANON-EDITION-V4.1/lean/Snuffy/<Module>.lean` for `MathlibAnalyticBridge`, `HalperinDecay`, `OpialBridge`, `CanonVonNeumann`; then run `CanonVonNeumannAudit.lean` for the axiom list.

The frozen canon-v4.0 release in `SNUFFY-CANON-EDITION-2026-10-24/` is untouched.
