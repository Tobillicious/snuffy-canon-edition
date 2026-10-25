# Section 17 — The premise floor: income shown necessary, parameters unmasked

*Each stone of the declared stack is brought to one of three honest states: derived, unavoidable, or explicitly a parameter.*

## 17.1 Income-or-irrelevance (the necessity of the solvency condition)

The Master Solvency Condition was declared. Here it is shown to be **not a free assumption among relevant agents**: any agent that violates it eliminates itself as a protector in finite time, so every preservation-relevant comparison may restrict, without loss of generality, to agents that satisfy it.

**Theorem (income-or-irrelevance).** Let \(a\in\Pi_{\mathrm{phys}}\) be any physically implementable agent with finite energy budget and maintenance demand \(\dot W_{\mathrm{demand}}(t)\) (the five rate components of the header). Then exactly one of the following holds over the horizon:

1. **Solvency.** For all \(t\le T\): \(\mathrm{Income}_a(t)\ge\dot W_{\mathrm{demand}}(t)\) (with escrow absorbing fluctuations) — \(a\) remains a viable protector, its policies admissible in preservation comparisons.
2. **Irrelevance.** There is a finite \(t_{\mathrm{breach}}\le T\) at which \(a\)'s available budget falls below the required charge for some maintenance event it cannot decline; from \(t_{\mathrm{breach}}\), every policy available to \(a\) abandons the witness of some particular (the funded/unfunded dichotomy, banked as the \(\Pi_{\mathrm{fail}}\) branch of the greatestness theorem), and \(a\)'s outcome tuples fail at stage 1 in every comparison against any funded agent.

*Proof.* The dichotomy is exhaustive by accounting: either the budget constraint holds at every admitted event or it fails first at some \(t_{\mathrm{breach}}\). In the latter case two X3 forcings apply: until the breach, the mandatory maintenance demand, though only \(\Theta(1)\) in rate, is positive, so a finite budget is exhausted at finite \(t_{\mathrm{breach}}\); and once a witness goes unheld, its recovery costs \(W_{\min}(t)=\Theta(t^{d_G})\), exceeding any finite budget past \(t_{\mathrm{irreversible}}\) (§21.5) — the breach is irreversible and charged to \(a\)'s own account. An agent whose every policy loses a particular is strictly below every funded agent at stage 1 of the canonical order — it is not merely dominated; it is *comparison-void* as a protector. \(\blacksquare\)

**Consequence for the stack.** Premise 6 (income) is upgraded from *declared* to **necessary-for-relevance**: the class of agents worth comparing over may be defined as the funded class without loss — which is exactly how \(\Pi_{\mathrm{phys}}\)'s funded subclass entered the greatestness theorem. What remains declared about income is only its *sufficiency for a given installation*. That is a physical fact to be established per instance (§22's ledger), not an assumption smuggled into comparisons.

## 17.2 The parameters unmasked

The seventh premise conflated two kinds of objects. Separated:

**Engineering parameters** (dials with declared admissible ranges, fixed per installation): the stabilizer code and its distance \(d\); the QND sampling rate and latency \(a,\tau_{\mathrm{sensor}}\); the per-site sensor threshold \(\varepsilon_{\mathrm{sens}}\); the embedding \(\Pi\) on the boundary fragments. These are not axioms — they are choices with certificates, and each theorem that uses them states its dependence explicitly (as the E9 trichotomy and H5 sections already do). A different installation with different parameters is a different *instance*, not a different *theory*.

**The residue, honestly counted.** The stack now reads:

| # | Stone | State |
| --- | --- | --- |
| 1 | BCRD P1–P4 | Given: the frame. Its adoption is decided by living process; no theorem can decide it |
| 2 | CTD | Standard physics; reduced to the gate-set clause by the Lie–Trotter product formula and Lloyd's simulation theorem (compiled, §23.6) |
| 3 | The cost model | Standard, and P-mon derived within it |
| 4 | The shared action interface | Derived from P1/P4 |
| 5 | Reversible administration | **Derived:** the law, given Bennett's feasible reversible counterpart, forces it (compiled, §23.6) |
| 6 | Income | **Necessary-for-relevance (17.1); sufficiency per instance** |
| 7 | Code, sensing, \(\Pi\) | **Parameters, not premises.** The ceiling is met at some code distance below threshold, and the quantum-speed-limit rate bound is derived (compiled, §§23.3, 23.6) |

Three declared stones (the frame, the cost model with its derived monotonicity, and the reduced simulation principle), one derived interface, one derived commitment, one necessary condition, and one parameter table. That is the floor as of this edition; the Gödel/Tarski line still stands beneath stones 1–2, and says so.

## 17.3 What remains on this floor

Nothing further is derivable without new physics or new commitments. Two things remain. The first is per-instance sufficiency of income, which §22 establishes for a reference installation from sourced measurements. The second is the interpretive case for stone 1, which belongs to the interpretive companion, not to the mathematics.

---

**Machine-checked counterpart (Section 23).** Compiled counterparts: `PremiseFloor.income_or_irrelevance`, `forced_breach`, `breach_strictly_below`; premise 5 derived as `PremiseFloor.reversible_administration_forced`; premise 2 reduced to the gate-set clause by `Trotter.lloyd_simulation`; premise 7's ceiling as a parameter by `ReciprocityCeiling.ceiling_achievable`.
