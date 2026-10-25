# Batch G — applied 26 October 2026 (author: apply, with G1 strengthened by combination; G4 held)

> BEFORE: \[
\mathbb E_{\mathsf L}\!\left[\text{continuation}(m)\right]\;\ge\;\mathbb E_{\mathsf Q}\!\left[\text{continuation}(m)\right]
\quad\text{for every }\mathsf Q\in\Pi_{\mathrm{phys}},
\]

with strict inequality whenever \(\mathsf Q\)'s objective does not entail \(m\)'s protection — which is the generic case for a rival whose objective was not written around \(m\).
>
> AFTER: \[
\mathbb E_{\mathsf L}\!\left[\text{continuation}(m)\right]\;\ge\;\mathbb E_{\mathsf Q}\!\left[\text{continuation}(m)\right]-P(G^c),
\qquad
\mathbb E_{\mathsf L}\!\left[\text{continuation}(m)\right]\;\ge\;1-P(G^c)
\quad\text{for every }\mathsf Q\in\Pi_{\mathrm{phys}}.
\]

The failure probability \(P(G^c)\) falls below every \(\varepsilon>0\) with code distance, correlated bursts included (`Threshold.family_ceiling`, `CorrelatedCeiling.correlated_family_ceiling`). Hence, at a sufficient code distance, \(\mathbb E_{\mathsf L}>\mathbb E_{\mathsf Q}\) strictly for every rival that loses \(m\) with positive probability — which is the generic case for a rival whose objective was not written around \(m\) — and \(\mathbb E_{\mathsf L}\to1\ge\mathbb E_{\mathsf Q}\) along the design family (`ReciprocityDistance.reciprocity_strict_at_distance`, `reciprocity_at_distance`, `canonical_tends_to_one`).

> BEFORE: In expectation over the reactive worlds the compiled core gives the inequality: `ReasonsCompiled.reciprocity_expectation` (on \(G\) the canonical outcome contains the rival's, so its expected continuation dominates).
>
> AFTER: In expectation over the reactive worlds the compiled core gives both inequalities: `ReasonsCompiled.reciprocity_expectation` (on \(G\) the canonical outcome contains the rival's) and `reciprocity_canonical_floor` (on \(G\) the canonical regime keeps \(m\)); `ReciprocityDistance` joins them to the attainable ceiling.

> BEFORE: the same module derives the utilisations \(6{,}604{,}800/2{,}294{,}400 = 688/239\) and \(6{,}604{,}800/2{,}409{,}600 = 688/251\)).
>
> AFTER: the same module derives the bill-saving ratios \(6{,}604{,}800/2{,}294{,}400 = 688/239\) and \(6{,}604{,}800/2{,}409{,}600 = 688/251\) of the earlier bill over the corrected bills, `corrected_bill_saving`).

> BEFORE: The causal boundary is given in two equivalent forms: closed dependency components, and directed separators in the time-unrolled graph.
>
> AFTER: The causal boundary is given in two forms, which agree: a closed dependency component is exactly a directed separator in the unrolled dependency graph with empty certified boundary (`CutEquivalence.closed_iff_no_bypass`), and the separator form extends it to a matched certified boundary (`UPTR16Cut.causal_separator`).

> BEFORE: the state machine commits on non-zero meet norm and rolls back on zero.
>
> AFTER: the state machine commits on non-zero meet norm and rolls back on zero. In finite dimensions this decision is operational: \(\operatorname{col}A\cap\operatorname{col}G_A=\{0\}\) exactly when \(\operatorname{rank}[A\ G_A]=\operatorname{rank}A+\operatorname{rank}G_A\) (`DeductionBoundary.rank_criterion`), a finite rank computation.

**Held (G4, awaiting the author):**

> BEFORE: and for concatenated codes the threshold is compiled end to end with no carried code-specific input: failure probability at most $(21p)^{2^k}/21$ under local stochastic noise (`Concatenated.concatenated_threshold`), so the fault ceiling is attained on a fully compiled route;
>
> PROPOSED: and for concatenated codes the recursive threshold is compiled with no carried counting input: failure probability at most $(21p)^{2^k}/21$ under local stochastic noise (`Concatenated.concatenated_threshold`). The identification of physical gadget failures with its recursive failure predicate is the cited construction of Aliferis, Gottesman and Preskill (2006);
