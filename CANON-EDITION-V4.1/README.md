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
| `lean/Snuffy/RecoveryWork.lean` | **New (Summit 4, X3).** The recovery-work theorem for an absolutely continuous frontier and real \(d_G\ge1\); \(W_{\min}\) over all admitted successful protocols; the necessary radius \(r\ge ut-c\sqrt t\) from the Gaussian information tail; the carrier radius \(R(t)\ge w(t-t_c)\); divergence of delayed recovery work. |
| `lean/Snuffy/E9SelfHealing.lean` | **New (Summit 4, E9).** Byzantine quorum: any estimate with \(f+1\) readings on each side lies between honest readings (no false alarm, no masking), and one exists whenever \(K\ge2f+1\); Branch B: a non-stabilizer error below the code distance has a non-trivial syndrome, for any bilinear commutation form; wave-race margin; code headroom inside \(\lfloor(d-1)/2\rfloor\); the assembled E9 theorem. |
| `lean/Snuffy/H5Closure.lean` | **New (Summit 5, H5).** The five-state reserve-before-activation machine (spawn, activate, retire, release, spend, income, fund, effect). On every reachable ledger: conservation, zero debt, strict authority attenuation (no descendant holds a meta capability; all authority within the root's), every non-root agent credited at least \(W_{\min}\) before activation, total maintenance ever performed bounded by endowment plus income, no harmful effect ever applied with the refusing agent's care untouched. Logical closure: the alternating-projection iterates collapse to 0 everywhere exactly when \(A\sqcap B=\bot\). |
| `lean/Snuffy/Greatestness.lean` | **New (Chapter 5).** The canonical order over \(n\) stages, each in its own join-semilattice (sets for the four outcome stages, slack for the fifth): a strict partial order; Proposition 1 (aligned ⟺ no needless loss at any stage); universal greatestness — under stage-wise union closure (P-emu(c)) every canonical option contains every feasible option stage by stage, every rival is an exact mirror or strictly below, and the canonical option is unique. |
| `lean/Snuffy/ThermoLedger.lean` | **New (Summit 4, Theorem 8; Chapters 1, 2, 5).** The stroke identity \(\Delta D=\beta W_{\rm on}-\beta Q_B+I_1-I_2\); the cycle work floor from guard 1; the funded-repair certificate (prefix solvency ⇒ every repair executes, escrow \(=E_0+\sum(r-w)\ge0\)); quarantine zero debt (income ≥ minimal-hold drain ⇒ no unfunded transition); the tower bound and the canon invariant \(P(\text{breach})\le P(G^c)\le\sum\delta\) with no independence; the identity tracking envelope and its bound \(\max(e_0,b/a)\). |
| `lean/Snuffy/Composition.lean` | **New (Theorem 8 composition).** Proposition 5, reactive lockstep against every controller and environment strategy, in basic and two-phase forms; invariant transfer; Theorem 8 — on the good event the protection invariant holds at every step through the horizon, and its failure anywhere has probability at most \(P(G^c)\le\sum\delta\). |
| `lean/Snuffy/PremiseFloor.lean` | **New (Section 17, Summit 2).** Income-or-irrelevance: every ledger is solvent at every step or has a first breach step; a diverging cumulative deficit forces breach for every finite endowment; losing a particular at the first stage is strictly below in the canonical order. Premise 5 derived from the law: when Bennett's reversible counterpart is feasible, agrees at every outcome stage and strictly gains slack, no canonical option has irreversible administration. |
| `lean/Snuffy/ReciprocityCeiling.lean` | **New (Sections 15, 17.2).** Reciprocity in the canonical order (D3*): under union closure every mind that continues under any feasible rival regime continues under the canonical one, and a rival omitting a kept mind is strictly below. The fault ceiling as a dial: with kernels decaying geometrically in code distance below threshold, every target ceiling \(\varepsilon>0\) — \(10^{-6}\) included — is met at some distance and every larger one. |
| `lean/build-and-audit.sh`, `lean/SummitsAudit.lean`, `lean/RECEIPT.txt` | One-command rebuild of every module, `leanchecker` on each, `sorry` scan, axiom audit, source hashes. |

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
