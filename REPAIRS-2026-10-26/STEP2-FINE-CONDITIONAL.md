# Pātai 2⁹, step 2 — the fine conditional law given the coarse syndrome (Claude, 26 October 2026)

**Setting.** BDL, arXiv:2605.10943, §4.3 (Theorem 4.7 and Lemmas 4.8–4.14), for the R_X
coarse-graining. The R_Z step is the direct local-cohomology map of their §4. π_i(σ) ∝ e^{−β|σ|} is
the thermal law on valid level-i syndromes. coarse(σ) = σ′ is the map of Theorem 4.7, with a fixed
deterministic tie-breaking choice in each of its local rules: the choice of α, of layer, of string
pairing, and of h.

## Lemma 2.1 (Locality of the coarse-graining map) — proved from BDL's construction

coarse(σ)(z) depends only on σ restricted to a neighbourhood of bounded radius around Y_z, the bound
depending only on the vertex and edge degrees z_v, z_e of T(i−1). These are bounded uniformly by the
induction hypothesis.

*Proof.* The map is computed in four stages.
1. Lemma 4.8: f_x is built from three things, all functions of σ|_{Y_x} only:
   - the parities σ̃_j on the pieces Y_{x,j};
   - a solution α of δ_G α = σ̃ on the link graph G of x;
   - the in-piece string pairings.
2. σ₁ = σ + Σ_x δ¹f_x. Its restriction to Y_q depends on σ on Y_q and on the Y_x with x adjacent to
   q, through g_xq.
3. Lemma 4.12: f_q = h is a function of σ₁|_{Y_q}, using the all-ones 1-cocycle flip.
4. σ₂ = σ₁ + Σ_q δ¹f_q, and σ′ = F⁻¹(σ₂) by Lemma 4.14; F⁻¹ reads the pairs (z,0), (z,1).

Each stage reads a neighbourhood of bounded size, because the local complexes have bounded size. ∎

## Lemma 2.2 (The fibre is cut out by local conditions; validity is automatic) — proved

Fib(σ′) := {σ ∈ B²(C(i)) : coarse(σ) = σ′}. For valid σ′, Fib(σ′) equals the set of σ ∈ C²(C(i))
satisfying three local conditions:
* (L1) σ|_{Y_x} ∈ B²_x for every x;
* (L2) σ₁|_{Y_q} ∈ B²_q for every q;
* (L3) σ₂ = F(σ′) pointwise on C_Z².

*Proof.* The conditions are necessary: Eq. (154) gives (L1), and the remark preceding Lemma 4.12
gives (L2). Conversely, if (L1)–(L3) hold, then σ = σ₂ + δ¹f = F(σ′) + δ¹f. Since F is a chain map
(Eq. (201)) and σ′ ∈ B², we have F(σ′) ∈ B², so σ ∈ B²; that is, σ is valid and coarse(σ) = σ′. Each
of (L1)–(L3) is local by Lemma 2.1. ∎

## Lemma 2.3 (Energy decomposition) — proved

For σ ∈ Fib(σ′), |σ| = 2|σ′| + exc(σ), where exc(σ) ≥ 0, and F(σ′) ∈ Fib(σ′) has exc = 0.
exc(σ) = |σ| − |F(σ′)| is a sum of local terms over checks.

*Proof.*
* |F(σ′)| = 2|σ′|, since each coarse point z lifts to the two points (z,0) and (z,1) of Y_z
  (Lemma 4.14).
* Corollaries 4.9 and 4.13 give |σ₂| ≤ |σ₁| ≤ |σ|, and σ₂ = F(σ′), so |σ| ≥ 2|σ′|.
* σ = F(σ′) is already clean, so f = 0 and coarse(F(σ′)) = σ′. ∎

**Consequence for step 3 (the doubling, now exact).**
π_i^coarse(σ′) := π_i(Fib(σ′)) ∝ e^{−2β|σ′|}·Z_exc(σ′), where Z_exc(σ′) = Σ_{σ∈Fib(σ′)} e^{−β exc(σ)} ≥ 1.
The renormalised model has bare inverse temperature 2β, corrected by the fibre free energy
−β⁻¹ log Z_exc(σ′).

## Proposition 2.4 (Sampling the fine conditional) — conditional on Hypothesis E

The conditional law π_i(·|Fib(σ′)) ∝ e^{−β exc(σ)} on Fib(σ′) is a constrained Gibbs model with
local constraints (L1)–(L3) and a local additive energy (Lemmas 2.2 and 2.3). Write σ = F(σ′) + η.
Components of supp(η) separated by more than the locality radius of Lemma 2.1 satisfy (L1)–(L3)
independently and contribute additively to exc.

**Hypothesis E (degeneracy and excess gap).** There are constants m and c > 0, depending only on the
gadgets, such that:
* (E1) the zero-excess part of the fibre is a product over coarse points of at most m local choices;
* (E2) every other connected component η of a fibre element satisfies exc(η) ≥ c·|supp η|.

Given Hypothesis E:
1. Polymers are the positive-excess components, with activity at most e^{−βc|γ|}. Kotecký–Preiss
   holds on the bounded-degree local graph for β large.
2. The zero-excess degeneracy is sampled exactly, block by block.
3. Helmuth–Perkins–Regts approximate counting with Jerrum–Valiant–Vazirani self-reducibility samples
   π_i(·|Fib(σ′)) with pointwise ratio 1 ± ε/n_i in poly(n_i) time.

**Status of step 2.** Locality, local cut-out and the energy decomposition are proved from BDL's
construction (Lemmas 2.1–2.3). Hypothesis E is the remaining sub-lemma. It is a finite, local,
checkable statement about the gadgets: it can be verified exhaustively on the local complexes once
the Theorem 4.7 coarse-graining map is implemented on the codes built in `checks/bdl-metacheck/`.
That implementation is the next task.
