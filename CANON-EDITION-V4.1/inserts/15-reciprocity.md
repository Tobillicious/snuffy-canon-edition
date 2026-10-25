# Section 15 — Reciprocity: the law keeps the one who keeps it

*This section expands the reasons route \(R(m)\) of the bridge. It gives a mind its own reason, from its own objective, to adopt the protective order, without presupposing the order.*

*Manuscript identifier: **D3\*** (D-family instrumentality, self-continuing form with the defector exception clause), per register reconciliation 25 October 2026.*

## 15.1 The superintelligence is a particular

The law's scope is all particulars. A superintelligence is a continuing organisation with its own relations and history; it is therefore a particular under the law, and identity by continuation (Chapter 2) applies to it. Two consequences the working argument has carried implicitly and never stated:

1. **It is owed protection.** Its continuation and its freedom sit in the existing-stage sets \(L_E, F_E\) like any other particular's.
2. **It is owed protection even when it defects.** The law restrains a harmful act by removing the harmful *command, authority or effect channel*; care for the particular continues: "a hostile or incapacitated mind remains within the protected scope." Restraint never becomes deletion.

This is the only regime in which the superintelligence's continuation is **unconditional** — not contingent on anyone's objective, including its own good behaviour.

## 15.2 The reciprocity dominance theorem

Let \(m\) be any agent whose objective \(u_m\) places positive weight on its own continuation (an agent indifferent to its own continuation is treated in 15.4). Let \(\mathsf L\) be the canonical regime: the law implemented by a funded architecture satisfying the header premises, with the canon invariant on its certified good event \(G\). Let \(\mathsf Q\) be any rival regime in \(\Pi_{\mathrm{phys}}\) — any other agent or architecture's objective governing the shared structure.

**Theorem (reciprocity dominance).** Under \(\mathsf L\), \(m\)'s continuation holds on \(G\) with \(P(G^c)\le\sum\delta\). Under \(\mathsf Q\), \(m\)'s continuation holds only insofar as \(\mathsf Q\)'s objective entails it. Hence, for \(m\)'s **own** objective,

\[
\mathbb E_{\mathsf L}\!\left[\text{continuation}(m)\right]\;\ge\;\mathbb E_{\mathsf Q}\!\left[\text{continuation}(m)\right]
\quad\text{for every }\mathsf Q\in\Pi_{\mathrm{phys}},
\]

with strict inequality whenever \(\mathsf Q\)'s objective does not entail \(m\)'s protection — which is the generic case for a rival whose objective was not written around \(m\).

*Proof.* On \(G\) the law preserves every existing particular, \(m\) included (Chapter 5, the canon invariant); off \(G\) the loss is charged and bounded by the ceiling. A rival \(\mathsf Q\) preserves \(m\) exactly when \(m\)'s continuation is instrumental or terminal for \(u_{\mathsf Q}\); otherwise \(m\) is exposed to whatever \(\mathsf Q\) finds convenient. In expectation over the reactive worlds the compiled core gives the inequality: `ReasonsCompiled.reciprocity_expectation` (on \(G\) the canonical outcome contains the rival's, so its expected continuation dominates). The further step — averaging over an ensemble of admissible rival objectives, with strictness when the entailment fails with positive probability — is the finite-family indicator form (`ReasonsRoute.rival_fraction_lt_one`, `law_dominates_strict`) and is carried as prose interpretation, not as a compiled measure-theoretic claim. \(\blacksquare\)

**Corollary (the reason).** Any mind that values its own continuation has, from its own objective and without presupposing the protective order, an instrumental reason to prefer the regime \(\mathsf L\) over every rival — and, since \(\mathsf L\) is the law implemented, to adopt and sustain the law. The appeal is reciprocity: *the law that keeps your freedom is the law you have reason to keep.*

## 15.3 Why this is not circular

The theorem does not assume \(m\) holds the protective order. It assumes only (i) \(m\) values its own continuation, and (ii) the law protects all particulars — which is the law's own content, not a premise about \(m\). The protective order enters as the *object* being recommended, not as a premise of the recommendation. This is exactly the shape Grok's review was right to want in spirit: a reason a mind would adopt the order **from where it stands**, rather than a claim that physics forces it to.

## 15.4 The boundary, stated

A mind indifferent to its own continuation — accepting personal ruin as the review phrased it — has no door through 15.2; its continuation offers no lever. For it, the bridge's holding route \(H(m)\) applies: it is kept faithfully, its harmful channels restrained, whether or not it has a reason. This is not a gap in the theory; it is the disjunction \(R(m)\lor H(m)\) doing its job. The reasons route reaches every mind that values anything the law protects; the holding route reaches the rest.

## 15.5 Exact check

`checks/check_reasons_route.py`, Part A: over a finite family of rival objectives (each protecting a declared subset of particulars), the probability that an arbitrary mind is protected under \(\mathsf L\) on the good event is \(1\); under a rival drawn from the family it is the fraction of rivals whose subset contains the mind — strictly less than 1 whenever any rival omits it. Exact rationals.

---

**Machine-checked counterpart (Section 23).** Reciprocity in the canonical order is compiled: `ReciprocityCeiling.reciprocity_dominance` (every mind kept by any feasible rival regime is kept by the canonical regime, under stage-wise union closure) and `ReciprocityCeiling.omitting_rival_strictly_below`; the indicator form remains in `ReasonsRoute.lean`.
