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

## Round 1 answer (Gemini, Pātai 1 a–c): disposition, and the exact generator terms

None of the three parts is adopted.

### 1(a): the generator is not the heat-bath generator, and the maximum principle does not close

The paste writes a one-site creation/annihilation form λ₊(1−σ_x) − λ₋σ_x. In the real dynamics a
qubit flip toggles 1–4 checks at once, at a heat-bath rate that depends on those checks. Here is
the exact computation for a **weight-2 qubit q = (x, y)** with x ∈ A and y ∉ A, done by Claude.
Write u_A = P_t(A ⊆ σ_t), and r(σ_x, σ_y) for the heat-bath flip rate:
- r(1,0) = r(0,1) = r₀ for a free hop;
- r(0,0) = r₊ for pair creation, of order e^{−2β};
- r(1,1) = r₋ for pair annihilation, with r₋ > r₀.

Then q's contribution to d/dt u_A is

    gain − loss ≤ r₀ (u_{A−x+y} − u_A) + r₊ u_{A∖x} + (r₀ − r₋) u_{A+y}.

- The hop term is ≤ 0 at a maximum over sets of size |A|. This is fine.
- The annihilation term is ≤ 0. But it is proportional to u_{A+y}, the *larger* set, not to u_A.
- The creation term r₊ u_{A∖x} is positive, and **no sink proportional to u_A** balances it at
  the maximum.

So the paste's "first exit" argument, which needs a sink of size κ₂|A|²(Cρ*)^{|A|}, has no such
sink. Annihilation enters only through (|A|+1)-point functions, and bounding it from below would
need positive correlation, the opposite of what is wanted. **This is the precise obstruction to
tool (a).** The paste also asserts its sink without deriving it.

### 1(b): sign error and a rejected input

FKG-type inequalities give *positive* correlation of increasing functions, not negative. No
reflection positivity is established for this dynamics. "Lemma C's boundary projection operator"
misnames two things: Lemma C is the per-time reduction, and the projection bound is the rejected
BCRD lemma (‖P‖ ∈ {0, 1}).

### 1(c): mean field and the rejected factor

1(c) uses the rejected α_boundary = e^{−2β}/18 and a mean-field density inequality, which
constraint 6 excludes.

## Refined core: the trapped-charge gas (Claude; derived reduction, partly heuristic)

The obstruction above lives inside regions: pair creation is balanced by annihilation, which is a
higher-order term. Lemma G handles exactly this: each bounded region relaxes internally at a rate
λ₀(β) independent of n. This suggests moving the n-point bound to **region level**.
- A region with even parity relaxes to empty-plus-thermal-pairs in O(1) time; its occupation is a
  sink with rate λ₀.
- A region with odd parity holds a trapped charge that cannot leave internally.

The charges live on the region graph and react through the qubits of weight 3 and 4 that cross
regions. A weight-3 qubit touching regions R₁, R₂, R₃ flips all three parities. Its effective rates
are:

| Reaction | Energy change | Effective rate |
|---|---|---|
| (1,1,0) → (0,0,1) | −1 | about 1/|R|² |
| (0,0,1) → (1,1,0) | +1 | about e^{−β}/|R| |
| (1,1,1) → (0,0,0) | −3 | — |
| (0,0,0) → (1,1,1) | +3 | about e^{−3β} |

This is a reversible Z₂ charge-reaction network of bounded degree with detailed balance. It has
no free hops left, because they are averaged inside regions.

**Pātai 1′ (the refined core).** For this charge network, started from a law with odd-region
density at most c p |R|, prove

    P_t(R₁, …, R_k all odd) ≤ (C ρ_c)^k   for all t ≤ T, with ρ_c = c′(p |R| + e^{−β}).

Then prove that the averaging step is legitimate: intra-region relaxation at about λ₀ against
cross-region reactions at about 1/|R|². The separation of these time scales is not established, so
the averaging is heuristic and must be proved or replaced by a joint argument.
Region-level (★) implies fine-level (★), because a fine set A meets at most |A| regions, each odd
or occupied by a transient pair. That last step needs its own bound from Lemma G.

The weight-2 obstruction does not recur at region level. A creation event inside an empty region
is followed by internal annihilation at rate about λ₀, so the sink is proportional to the event
itself.

## Provenance check (26 October, evening)

The earlier sessions were searched for this problem:
- this session's pre-compaction transcript and its 13:48 export;
- `codex 26 Oct.txt`;
- `Codex _ 25 Oct.txt`;
- `# Review UPT publication readiness _ Codex 25th Oct.md`.

None treats preparation with noisy gates or the fault layer. The morning session reduced
initialisation to the warm start; it named as alternatives a codespace-start lifetime theorem or
fault-tolerant code switching to the thermal encoding. The morning's "multiscale grooming"
submission was not adopted (asserted inequality; `PATAI-QUANTUM-TRANSFER-2026-10-26.md` line 173).
Codex's 26 October chat records the noisy handoff as unfinished. N1 was first identified on
26 October.

## Round 2 answer (Gemini, Pātai 1′): disposition

It is not adopted. It has the right architecture: region-level parities, averaging, then a bridge to
fine checks. But each load-bearing step is asserted or misapplied.

1. **The region-level n-point bound.**
   - Dobrushin uniqueness and polymer expansion are statements about a *Gibbs* measure's
     conditional specification. P_t is a time-dependent, non-equilibrium law, and nothing transfers
     them to it.
   - The coefficient C_{R,R′} = (γ_u + γ_d)/λ₀ is a ratio of rates, not a Dobrushin influence
     coefficient.
   - The single-region bound z(R) ≤ ρ_c for all t is asserted. It is pātai 2, still open.
   - The creation rate ν includes p, a gate fault rate, during holding. Constraint 6 and N2 exclude
     this: faults enter only at t = 0.
2. **Averaging.**
   - Kurtz-type averaging gives limits over bounded time windows as a scale parameter tends to
     zero. It does not give error bounds uniform over t ≤ e^{c n^{η′}} for K_n regions, whose errors
     add.
   - The claimed error O((1/|R|²)/λ₀) is "small" only if λ₀ ≫ 1/|R|². Lemma G gives only
     λ₀(β) > 0, possibly e^{−O(72β)}, so the separation is unproved and may be reversed.
   - λ₀ = Θ(1) is asserted.
3. **The bridge to fine checks.**
   - P(A ⊆ σ) ≤ Σ_η P(η) Π_x P(x | η_{R(x)}) assumes that fine occupations are conditionally
     independent given the parities. That is not established for the dynamics.
   - Lemma G is a spectral gap, not a pair-density bound, so ρ_pair = e^{−2β}/μ is not derived
     from it.

**What would make this a proof.**
- (i) Pātai 2 at region level: a time-uniform bound on P_t(R odd).
- (ii) A genuine n-point inequality for the non-equilibrium charge network. One route is a
  generator-hierarchy computation like the weight-2 one above, at region level, where the sink is
  proportional to the event (internal relaxation).
- (iii) An actual estimate of λ₀ for the region types: numerically for the ≤ 72-check regions,
  then a bound.
- (iv) A conditional-independence or decoupling bound for fine occupations given region parities.
