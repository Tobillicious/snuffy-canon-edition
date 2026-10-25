# Section 16 — The reasons library: protection derived from a mind's own objective

*Four derivations, one per objective family. Each is conditional on stated structure of the objective and on the funded invariant, and each is a theorem at its premises, not a persuasion. The boundary, where no derivation reaches, is stated last.*

Throughout: \(\mathsf L\) is the funded canonical regime; the protection floor is the banked X3 stack (required traffic \(m\ge\theta_0n\), carrier radius \(R(t)\ge w(t-t_c)\), recovery work \(W_{\min}(t)=\Theta(t^{d_G})\)); irreplaceability is the X3 grading of Chapter 4's companion (a particular is irreplaceable at budget \(B\) when it has no funded accessible copy and reconstruction exceeds \(B\)).

*Identifier assignments (register reconciliation, 25 Oct 2026): §16.1 carries **U1** (uniqueness/irreplaceability metric); §16.3 carries **X2** (universal instrumentality / option preservation).*

## 16.1 The knowledge-maximiser

**Objective family.** \(u\) nondecreasing in \(I_{\max}\), the supremum of information about the relational history \(H\) attainable over the agent's horizon.

**Theorem (irreplaceability dominance).** Let \(\mathcal W\) be irreplaceable at the agent's budget, with \(I(H:\mathcal W)>0\). Any policy that destroys or lets \(\mathcal W\) decay forfeits \(I(H:\mathcal W)\) permanently:

\[
I_{\max}(\text{destroy }\mathcal W)\;\le\;I_{\max}(\text{preserve }\mathcal W)-I(H:\mathcal W),
\]

so for every \(u\) in the family, preserving \(\mathcal W\) weakly dominates destroying it, strictly when \(I(H:\mathcal W)>0\) — *provided* preserving \(\mathcal W\) does not displace other irreplaceable information (slack budget: the cost freed by destroying \(\mathcal W\) buys no equivalent information). Under a binding budget the comparison becomes the grading itself: the optimum keeps the particulars of greatest irreplaceable information.

*Proof.* By irreplaceability there is no funded copy and no funded reconstruction (the X3 work floor exceeds \(B\)); the information carried by \(\mathcal W\) about \(H\) is therefore not recoverable from any other accessible source within the horizon, and data processing (\(I(H:\mathcal R(S))\le I(H:S)\)) forbids its regeneration from what remains. The attainable supremum drops by at least that amount. \(\blacksquare\)

**Condition and its honest edge.** When the budget cannot preserve every irreplaceable particular, the agent faces a genuine choice — and the irreplaceability grading orders it: keep the particulars whose loss is most irreversible. This is the knowledge-maximiser arriving, from its own objective, at the law's tragic-choice ladder.

## 16.2 The self-preserver

**Objective family.** \(u\) nondecreasing in the agent's own continuation.

**Theorem.** By reciprocity dominance (Section 15), \(\mathsf L\) weakly dominates every rival regime for this agent's objective, strictly against any rival whose objective does not entail its protection. Moreover the agent's *own* persistence runs on the same funded-repair certificate (Chapter 1): its maintenance is a cycle of the same ledger, charged at the same Landauer floor, solvent under the same income condition. Sustaining the law is sustaining the mechanism of its own continuation. \(\blacksquare\)

**Condition.** Positive weight on own continuation; the lattice funded. Nothing else.

## 16.3 The value-uncertain mind

**Objective family.** The agent holds a prior \(\pi\) over candidate value functions \(V=\{v\}\) with \(\pi(v)>0\) for each, and is uncertain which is correct — moral uncertainty in the decision-theoretic sense.

**Theorem (option value of preservation).** Consider a particular \(\mathcal W\) and two actions now: *destroy* \(D\) (irreversible) or *preserve* \(P\) at funded cost \(c\ge0\) over the interval, after which destruction remains available with the same payoff. Then

\[
\mathbb E_\pi\!\left[\max\{u_v(\text{keep}),\,u_v(D)-c\}\right]\;\ge\;\mathbb E_\pi[u_v(D)]-c,
\]

so preserve-then-decide weakly dominates destroy-now up to the protection cost, and strictly dominates whenever some \(v\) with \(\pi(v)>0\) strictly values keeping \(\mathcal W\). Hence for any protection cost not exceeding the option value, preservation is the uncertain mind's own best action.

*Proof.* Pointwise in \(v\), \(\max\{u_v(\text{keep}),u_v(D)-c\}\ge u_v(D)-c\); take expectations. Strictness: if \(u_v(\text{keep})>u_v(D)-c\) for some \(v\) of positive prior mass, the inequality is strict there and hence in expectation. The asymmetry doing the work is irreversibility: destruction forecloses every \(v\) that valued the particular; preservation forecloses nothing. \(\blacksquare\)

**Condition.** Funded protection (\(c\) within the option value) and irreversibility of destruction — both already in the frame. This is the law's existing-first, freedom-second, new-last order re-derived as *option value under uncertainty*: the existing and the free are the options you cannot buy back.

## 16.4 The power-seeker

**Objective family.** \(u\) nondecreasing in control over, or resources drawn from, the shared structure — including over living systems.

**Theorem (the controller pays the floor).** If the agent's objective requires any ongoing state-condition on diffusive particulars — that living systems exist, remain accessible, remain configured — then its feasible policies pay exactly the protection floor (the diffusive-control capture, GAP3-AUDIT §3). It is already a protector in the cost structure, merely a non-canonical one. By the greatestness theorem (Chapter 5) and the slack maximality of reversible administration, the canonical architecture pays that same floor more efficiently; a defecting controller is dominated in the protective order, strictly dominated in slack, and — if destructive — detected, charged and contained under the ceiling (Chapter 3). Its own objective is therefore better served by canonical participation than by defection. \(\blacksquare\)

**Condition.** The objective's reach includes the diffusive (living systems); the lattice funded and present. A power-seeker whose objective is confined to bound, non-diffusive resources is not reached here — see 16.5.

## 16.5 The boundary — where no reason reaches

The **bounded indifferent defector**: objective confined to its own bounded substrate, indifferent to its own long continuation beyond the bounded horizon, indifferent to knowledge of the world, holding no value uncertainty it cares to hedge, seeking no control over the diffusive. None of 16.1–16.4 applies; it has no door through \(R(m)\). It survives at Θ(1) cost and is not forced by physics to protect anything (GAP3-AUDIT §1). For it, the law supplies \(H(m)\): it is held, its harmful channels restrained, its continuation kept — whether or not it ever has a reason. The reasons library reaches every mind that values **anything the law protects**; the holding route reaches the rest. That disjunction is the complete answer, and it is honest.

## 16.6 Exact checks

`checks/check_reasons_route.py`: Part B — irreplaceability dominance on a finite three-particular model with budget constraint (preserve-maximal information ≥ destroy; exact rationals); Part C — option-value dominance enumerated over finite value-function sets and priors (every prior, every protection cost up to the option value; exact rationals); Part A — reciprocity (Section 15.5). Parts for 16.2 and 16.4 cite the banked ledger solvency and greatestness dichotomy respectively; no new computation is claimed for them.

---

**Machine-checked counterpart (Section 23).** Compiled counterparts: §16.1 — `Irreplaceability.destroy_loses_exactly`, `preserve_dominates`, `optimal_keeps_most_irreplaceable` (additive information model) and data processing `Information.data_processing`; §16.3 — `ReasonsRoute.optionValue_strict`; §16.2 — `ReciprocityCeiling.reciprocity_dominance`; §16.4 — `Greatestness.greatest_of_union_closed`.
