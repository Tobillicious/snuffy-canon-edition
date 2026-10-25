# Batch G — semantic-review application links 4–8

Prepared 26 October 2026. BEFORE is verbatim; apply only on the author's OK. Link 7 (authority attenuation) needs no change: H5.1's wording matches the compiled `H5Closure.authority_attenuation`.

**G1a §15.2 display (link 4).**

> BEFORE: \[
\mathbb E_{\mathsf L}\!\left[\text{continuation}(m)\right]\;\ge\;\mathbb E_{\mathsf Q}\!\left[\text{continuation}(m)\right]
\quad\text{for every }\mathsf Q\in\Pi_{\mathrm{phys}},
\]

with strict inequality whenever \(\mathsf Q\)'s objective does not entail \(m\)'s protection — which is the generic case for a rival whose objective was not written around \(m\).
>
> AFTER: \[
\mathbb E_{\mathsf L}\!\left[\text{continuation}(m)\right]\;\ge\;\mathbb E_{\mathsf Q}\!\left[\text{continuation}(m)\right]-P(G^c),
\qquad
\mathbb E_{\mathsf L}\!\left[\text{continuation}(m)\right]\;\ge\;1-\textstyle\sum\delta
\quad\text{for every }\mathsf Q\in\Pi_{\mathrm{phys}},
\]

with \(P(G^c)\le\sum\delta\le10^{-6}\). Hence \(\mathbb E_{\mathsf L}>\mathbb E_{\mathsf Q}\) strictly whenever \(\mathsf Q\) loses \(m\) with probability greater than \(\sum\delta\) — the generic case for a rival whose objective does not entail \(m\)'s protection.

**G1b §15.2 proof (link 4).**

> BEFORE: In expectation over the reactive worlds the compiled core gives the inequality: `ReasonsCompiled.reciprocity_expectation` (on \(G\) the canonical outcome contains the rival's, so its expected continuation dominates).
>
> AFTER: In expectation over the reactive worlds the compiled core gives both inequalities: `ReasonsCompiled.reciprocity_expectation` (on \(G\) the canonical outcome contains the rival's, so the rival exceeds the canonical regime only on \(G^c\)) and `reciprocity_canonical_floor` (the canonical regime keeps \(m\) on \(G\)).

**G2 §24.2 ratios (link 8).**

> BEFORE: the same module derives the utilisations \(6{,}604{,}800/2{,}294{,}400 = 688/239\) and \(6{,}604{,}800/2{,}409{,}600 = 688/251\)).
>
> AFTER: the same module derives the bill-saving ratios \(6{,}604{,}800/2{,}294{,}400 = 688/239\) and \(6{,}604{,}800/2{,}409{,}600 = 688/251\) of the earlier bill over the corrected bills, `corrected_bill_saving`).

**G3 §24.3 causal-cut forms (link 8).**

> BEFORE: The causal boundary is given in two equivalent forms: closed dependency components, and directed separators in the time-unrolled graph.
>
> AFTER: The causal boundary is given in two forms, each compiled as a sufficient exclusion certificate: closed dependency components (`UPTR16Cut.closed_cut_step`, `closed_cut_reactive`) and directed separators in the time-unrolled graph (`causal_separator`).

**G4 §23.8 concatenated route (link 5).**

> BEFORE: and for concatenated codes the threshold is compiled end to end with no carried code-specific input: failure probability at most $(21p)^{2^k}/21$ under local stochastic noise (`Concatenated.concatenated_threshold`), so the fault ceiling is attained on a fully compiled route;
>
> AFTER: and for concatenated codes the recursive threshold is compiled with no carried counting input: failure probability at most $(21p)^{2^k}/21$ under local stochastic noise (`Concatenated.concatenated_threshold`). The identification of physical gadget failures with its recursive failure predicate is the cited construction of Aliferis, Gottesman and Preskill (2006);

**G5 Chapter 4 operational detector (link 6; addition).**

> BEFORE: the state machine commits on non-zero meet norm and rolls back on zero.
>
> AFTER: the state machine commits on non-zero meet norm and rolls back on zero. In finite dimensions this decision is operational: \(\operatorname{col}A\cap\operatorname{col}G_A=\{0\}\) exactly when \(\operatorname{rank}[A\ G_A]=\operatorname{rank}A+\operatorname{rank}G_A\) (`DeductionBoundary.rank_criterion`), a finite rank computation.
