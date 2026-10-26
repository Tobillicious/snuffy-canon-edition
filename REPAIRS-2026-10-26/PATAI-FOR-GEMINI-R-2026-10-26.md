# Pātai for the gauntlet on statement (R) — 26 October 2026 (Claude)

The target is unchanged: full quantum-coherence holding at the original stage budget, with
arbitrary references, fixed device constants and the complete bill. Background is in
`PATAI-NOISY-PREPARATION-2026-10-26.md`. Everything below is stated so that an answer can be checked.

## The reduction (Claude, derived from G.21's own algebra)

**Lemma C.** The G.21 holding estimate uses, at each time t, only the bad weight
b_t = Tr(P^⊥ ρ_t), through |Tr(Bρ)| ≤ 3‖B‖√(b_t) whenever P B P = 0. Integrating over time gives

    ‖(Dec Φ_t Enc ⊗ id)(ρ_LR) − ρ_LR‖₁ ≤ 18 Λ(n) ∫₀ᵗ √(b_s) ds.

So a warm start and stationarity are only one way to bound b_t. Any bound on b_t valid at every
time suffices.

Here P^⊥ ⊆ {the history of σ_t has a polymer of size ≥ L*}, the decoder's failure region in BDL
§5.2. Checking that BDL's Chesi projector satisfies this inclusion is part of pātai 4.

**Sufficient condition (the n-point occupation bound).** Suppose that for every t ≤ T and every
finite set A of fine checks,

    P_t(A ⊆ σ_t) ≤ (C ρ*)^{|A|},   with ρ* = c (p + e^{−β}) independent of n and t.     (★)

Every history polymer Γ has at least |Γ|/4 occupied finest checks (G.21 §2). Hence

    P_t(a polymer of size ≥ L is present) ≤ M Σ_{ℓ≥L} B^ℓ (C ρ*)^{ℓ/4},

which is small once B (C ρ*)^{1/4} < 1, a fixed device inequality. Lemma T takes the union over
time, and Lemma C then gives holding. (★) holds at t = 0 for the faulted thermal state N(ρ_β), by
the local stochastic fault bound and the thermal polymer gas. **(★) for all t ≤ T is the one open
statement.**

## Hard constraints: any answer violating one is rejected

All of these are computed on the constructed code, in `checks/bdl-metacheck/`.

1. **Regions.** The zero-energy hop regions are bounded: at most 4 checks at R_X levels and at most
   72 at R_Z levels. Their number K_n grows linearly with n (level 3 has 56,552). Any argument that
   needs K_n bounded fails.
2. **Cross-region moves.** 688 level-2 qubits each touch at least two regions (592 of weight 3, 96
   of weight 4). Flipping one when two of its checks are occupied is downhill (ΔH = −1), at rate
   about 1. There is no barrier "ΔH ≥ 2" for crossing regions.
3. **Free merging.** Free hops (ΔH = 0) merge history polymers: 725 of 13,810 sampled moves grew
   the largest polymer, one from 14 to 28.
4. **No monotonicity.** The dynamics has no attractive partial order. Arguments that need one must
   construct it.
5. **No device constants depending on n.** No β that grows with n and no fault rate that falls with
   n. Only fixed inequalities in p, β and the code's local constants are allowed.
6. **The required output.** Bounds must hold at every t ≤ e^{c n^{η′}}, or be combined with Lemma T,
   with error below the stage budget ε/2^{j+2}. Mean-field rate equations, "mixing time O(1)" or
   "O(log n)" without proof, and pointwise domination of the faulted state (impossible by N1 and
   N3) are not admissible.
7. **No new axioms.** BCRD P1–P4 supply locality and finite speed (P4), already used. They supply
   no contraction property.

## The pātai

**Pātai 1 (the core).** Prove (★) for the heat-bath (Davies-Pauli) dynamics of the BDL syndrome,
started from N(ρ_β), at a fixed β with B(Cρ*)^{1/4} < 1. Candidate tools:
- (a) a closed hierarchy for the n-point functions u_A(t) = P_t(A ⊆ σ_t). Compute d/dt u_A from the
  generator exactly. Show that the weighted family u_A/(Cρ*)^{|A|} cannot first exceed 1 (a
  maximum-principle or barrier argument over the hierarchy). The terms from free hops,
  annihilation and the downhill flips of weight 3 and 4 must be written out explicitly.
- (b) a duality or correlation inequality. Annihilating and coalescing random walks have known
  duality and negative-correlation results; one could extend them to this system with creation and
  the weight-3/4 moves.
- (c) a disagreement coupling with the stationary process from ρ_β, which satisfies (★) by the
  thermal polymer gas, showing that disagreements stay locally sparse.

State which tool, and give every term.

**Pātai 2 (the one-point case first).** Prove u_{x}(t) ≤ c(p + e^{−β}) for every check x and every
t ≤ T. This is the density never rising above the fault or thermal scale. Note that uphill creation
at rate about e^{−β} per site must be balanced by annihilation; a bound that grows linearly in t
fails.

**Pātai 3 (the two-point case).** Prove u_{x,y}(t) ≤ (Cρ*)² for adjacent x, y, including x, y in
the same region (free hops bring them together; annihilation removes them) and x, y in different
regions joined by a cross-region qubit. This is the first case where clustering could appear.

**Pātai 4 (the projector).** Using BDL Theorem 2.6 (Chesi, Loss, Bravyi and Terhal, Theorem 1)
and BDL §5, give the exact definition of the protected projector P in their lifetime proof. Confirm
or refute that P^⊥ is contained in "some history polymer of size ≥ L* is present", with L* of
order n^η, and quote the lines.

**Pātai 5 (literature, with checkable citations).** Give exact theorem statements, with arXiv or
DOI references, for any of the following:
- n-point correlation bounds or negative association for annihilating random walks with
  branching or creation on graphs;
- stability of self-correcting memories started from perturbed or non-thermal states;
- bounds on the time-dependent bad weight b_t under Davies dynamics.

We will read every reference before using it.

## What Claude will run against any answer

- A numerical test of (★) for |A| = 1, 2, 3 on the level-2 and level-3 codes, comparing u_A(t)
  with (Cρ*)^{|A|} over time, from N(ρ_β). These are `healing_probe.py`-style simulations.
- A term-by-term check of any generator computation against the actual qubit columns.
