# Pātai — the remaining join for indefinite quantum-coherence holding (26 October 2026)

**Context.** Balasubramanian, Davydova and Lin (arXiv:2605.10943, May 2026) prove a passive memory
whose Hamiltonians are 3D-local CSS stabilizer codes C(k) on n_k = e^{Θ(k)} qubits. Below T_c, the
thermal encoding satisfies ‖Φ_t∘Enc_k(ρ) − Enc_k(ρ)‖₁ ≤ t·exp(−Θ(n_k^η)).

Holding a qubit at fixed ε for every age needs a doubling schedule. At age 2^j, move the stored qubit
from C(k_j) to a larger C(k_{j+1}), choosing n_{k_j}^η of order j + ln(1/ε). Each move must fail with
probability at most ε/2^{j+1}, at polylog(t) cost. The paper's Outlook item 2 lists efficient
preparation of the thermal encoding as open. The target is unchanged.

**Pātai.** Answer with definitions, lemmas and proofs. Give the source of every cited result (DOI or
arXiv identifier), and keep assumptions separate from demonstrated consequences.

1. **Code switching.** Is there a fault-tolerant map taking Enc_k(ρ) to a state within ε_j (trace
   distance) of Enc_{k+1}(ρ)? It must be built from local operations, plus measurement and feedback,
   at a cost polynomial in n_{k+1}. The recursive refinement and doubling gadgets that build C(k+1)
   from C(k) are the natural candidates. Does each gadget have a fault-tolerant implementation?
2. **Non-thermal initialisation.** Does a lifetime bound of the same form hold for a state prepared
   in the codespace, without the thermal sector, for example |ψ⟩_L ⊗ |∅⟩ syndromes? Alternatively,
   does the dynamics thermalise the syndrome sector within time poly(n), without logical error?
   (Compare the paper's footnote on Ref. [25], which needs an LDPC metacheck matrix.)
3. **Teleportation alternative.** Can the qubit be teleported from C(k) into C(k+1) using a Bell pair
   prepared fault-tolerantly between the two codes? What is the failure probability, given the
   distance of each code (a power of n), and what is the preparation cost?
4. **Accounting.** For whichever route works, state the per-stage cost and failure. Show that the
   total over all stages up to age t is sublinear, with total failure at most ε.

---

## Response received (26 October): pātai 4 answered; pātai 1–3 remain, and they reduce to pātai 2

* **Pātai 4 (accounting) is answered and correct.** It is compiled as `Snuffy.StageSchedule`
  (candidate; zero output, leanchecker 0, standard axioms):
  - `total_with_transfers`: if each stage's holding and transfer failures are each at most
    ε/2^{j+2}, the total failure is at most ε;
  - `stage_cost_le`: polynomial per-stage cost sums to J·(a + bJ)^κ, which is polylogarithmic in
    age.
* **Correction to the response.** A stage lasts 2^j, so its holding failure is at most
  2^j·exp(−c·n_j^η). The code size must therefore satisfy c·n_j^η ≥ (2j + 2) ln 2 + ln(1/ε), not
  (j + 1) ln 2 + ln(1/ε). The order of growth is unchanged.
* **Pātai 1–3 (the transfer gadget) are not answered.** The response assumes a migration gadget with
  failure ε_j at cost poly(n).
* **All three routes reduce to pātai 2.** Code switching and teleportation both land the qubit in the
  codespace of C(k+1), not in its thermal encoding Enc_{k+1}. The single remaining question is
  therefore:
  - does the lifetime bound hold for codespace-initialised states, or
  - does the syndrome sector thermalise within poly(n) time with logical error at most ε_j?

  Given either, a fault-tolerant logical transfer between the LDPC codes C(k) and C(k+1) — logical
  measurement or surgery for LDPC codes, a separate cited input — completes the join.

---

## Pātai 2 responses (26 October): not proved; a sharper route recorded

Three submissions were received: an out-of-equilibrium contour expansion, a "Peierls barrier plus
Liouvillian sector decoupling" argument, and an MLSI timescale separation. None proves pātai 2.

* **MLSI.** A modified log-Sobolev constant for the full generator, bounded independently of size,
  would make the whole state mix to the Gibbs state in O(log n) time, logical qubit included. That
  contradicts self-correction: a self-correcting memory must have an exponentially small global gap.
  A sector-restricted inequality that excludes the logical degree of freedom is exactly what is
  missing. The submission's "local steady state σ" is undefined.
* **"The LDPC metacheck matrix structure from BDL" is false.** arXiv:2605.10943, footnote 4, states
  that the metacheck matrix is not LDPC. This is why the fast-initialisation result of their
  Ref. [25] does not apply.
* **An energy barrier alone is insufficient.** Haah's code has a growing barrier and an O(1)
  lifetime. BDL's lifetime proof controls entropy through the stationary syndrome distribution,
  which is why it uses the thermal encoding. The contour submission asserts "absence of
  percolation" at precisely the point where a proof is needed.

**Sharper route (pātai 2′).** BDL's lifetime theorem (their Theorem 2.6, from Ref. [22]) reduces to
the condition P_{σ∼Σ(β)}(σ unstable under the decoder) ≤ e^{−n^η}. Pātai 2 then follows if:
(i) **Monotonicity.** For a CSS code under Davies dynamics with Pauli jump operators, the syndrome
    process is a classical Markov chain. It must be monotone, or attractive, for the coordinatewise
    order of excitations, so that the law at time t starting from the empty syndrome is
    stochastically dominated by the stationary law Σ(β).
(ii) **Up-set.** "Unstable under the decoder D" must be an up-set: adding excitations cannot make a
    stable syndrome unstable.
Given (i) and (ii), P_t(unstable) ≤ P_{Σ(β)}(unstable) at every time t, and BDL's theorem then gives the
lifetime bound from codespace initialisation.

**Pātai 2′ for Gemini.** Prove or refute (i) and (ii) for the BDL codes, their decoder D and Glauber or
Davies jump rates. If (i) fails, give a coupling or a comparison inequality that still bounds
P_t(unstable) by a polynomial multiple of P_{Σ(β)}(unstable). Cite with DOI or arXiv identifier.

---

## Pātai 2′ responses (26 October): monotone route not established; trajectory route fails

* **Holley's criterion does not apply as written.** It is a single-site birth–death criterion, but a
  Pauli flip toggles several checks at once. The respondent then refuted its own monotonicity (i)
  and up-set (ii) claims for BDL. Neither is established.
* **The trajectory likelihood ratio fails at "ΔF₀ = O(1)".**
  - At finite temperature the thermal syndrome gas has finite defect density, so
    π_th(∅) ≈ e^{−cn}.
  - The likelihood ratio at t = 0 is therefore 1/π_th(∅) = e^{Θ(n)}, which is volume-law.
  - The change of measure then gives P_∅(fail) ≤ e^{Θ(n)} e^{−Θ(n^η)}, which is useless for η < 1.
  - The relative-entropy version fails in the same way: D(δ_∅‖π_th) ~ n, far larger than
    ln(1/π_th(fail)) ~ n^η.

**Status.** Pātai 2 is BDL's Outlook item 2 and is open in the literature as of May 2026. The quantum
branch is proved conditional on this one named problem, through
`StageSchedule.total_with_transfers`, whose hypotheses are stated explicitly. The classical branch is
closed. How to present this is the author's decision.

---

## The initialisation problem in its correct form: a warm start (26 October)

**The submission ("shell-wise adiabatic embedding").** It identifies the right obstruction, the
volume-law initial mismatch. As written, though:
* **Lemma 1 asserts its conclusion.** Each recursive level adds a constant fraction of the qubits,
  not only a boundary, so an O(1) mismatch per qubit sums back to Θ(n).
* **Lemma 2 has the wrong sign and an empty citation.** A mismatch enters as a factor e^{+D}. It must
  also be the max-divergence: a KL bound gives only polynomial suppression.

**Compiled: `Snuffy.WarmStart`** (candidate; zero output, leanchecker 0, standard axioms).
* `warm_start`: if the initial syndrome law satisfies μ ≤ Cπ pointwise and π is stationary, then
  μKᵗ ≤ Cπ at every time t.
* `warm_start_event`: P_t(A) ≤ C·π(A) for every event A and every time t.

With C = poly(n) and π(unstable) ≤ e^{−Θ(n^η)}, the stationary bound survives at every time. This
assumes the lifetime proof uses only per-time marginal bounds; that must be checked against BDL
Theorem 2.6.

**Pātai 2″, the sharpened open problem.** Prepare a warm start with a polynomial constant,
D_max(μ‖π_th) = O(log n).
* **Independent generators.** The thermal syndrome law is a product. Exact preparation is a
  classical sample followed by a depth-1 layer of the corresponding Pauli pure errors.
* **BDL's code.** The redundant generators (metachecks) make π_th a constrained classical model, so
  the problem is classical sampling: sample BDL's metacheck-constrained thermal syndrome
  distribution exactly, or within a polynomial pointwise ratio, in polynomial time. BDL's analogous
  classical code (their §6) is the natural first target.

---

## Derived (Claude, 26 October): a warm start suffices — extension of Chesi–Loss–Bravyi–Terhal Theorem 1

**Sources, read directly.**
* BDL Theorem 2.6 cites Chesi, Loss, Bravyi and Terhal, New J. Phys. 12, 025013 (2010),
  arXiv:0907.2807, Theorem 1: ‖Φ_t∘Φ_in(η) − Φ_in(η)‖₁ ≤ 8t‖𝓛‖₁ Tr(P^⊥ρ_β).
* Their proof (§6.2) uses ρ(0) = Oρ_β, with O in the logical algebra and ‖O‖ ≤ 2, together with
  𝓛(ρ_β) = 0. It bounds ‖ρ(t) − ρ(0)‖ ≤ t‖𝓛(ρ(0))‖. A warm start relaxes, so this route does not
  apply to it directly.

**Extension: track the logical observables, not the state.** Let ρ(0) = η ⊗ μ_A with
μ_A ≤ C·η_A, where η_A is the thermal factor and ρ_β = ½I ⊗ η_A.
1. **Domination.** ρ(0) ≤ 2C·ρ_β, because η ≤ I. Since Φ_t is positive and ρ_β is stationary,
   ρ(t) ≤ 2C·ρ_β for all t. This is the quantum form of `WarmStart.warm_start`. Hence
   Tr(P^⊥ρ(t)) ≤ 2C·ε, where ε = Tr(P^⊥ρ_β).
2. **Protection.** From their hypotheses [X̃, S_a]P = 0 and P[S_a†, X̃] = 0,
   𝓛†(X̃) = ½Σ_a(S_a†[X̃, S_a] + [S_a†, X̃]S_a), so P𝓛†(X̃)P = 0.
3. **Drift.** d/dt Tr(X̃ρ(t)) = Tr(𝓛†(X̃)ρ(t)). Only the blocks PρP^⊥, P^⊥ρP and P^⊥ρP^⊥ contribute.
   By Cauchy–Schwarz, |Tr(A PρP^⊥)| ≤ ‖A‖√Tr(P^⊥ρ). So
   |d/dt⟨X̃⟩_t| ≤ c‖𝓛‖(√(2Cε) + 2Cε), and likewise for Z̃.
4. **Conclusion.** ⟨X̃⟩_0 = Tr(ηX) exactly. So the decoded qubit's Bloch components drift by at most
   t·c‖𝓛‖·√(2Cε) + O(Cε) over time t. With C = poly(n) and ε = e^{−Θ(n^η)}, the drift is
   t·poly(n)·e^{−Θ(n^η)/2}: still exponentially small, with the exponent halved.

**Details to check.**
* Whether Ỹ = iX̃Z̃ satisfies the same protection conditions, or whether ⟨X̃⟩ and ⟨Z̃⟩ alone fix the
  decoded state through Φ_out (Bloch components). The hypotheses on P and the commutation relations
  must be checked against Chesi et al. §4.
* The norm ‖𝓛†(X̃)‖ in terms of their ‖𝓛‖₁.

**Status.** Up to these checks, pātai 2 reduces rigorously to pātai 2″: prepare a warm start with a
polynomial constant. That is the classical problem of sampling BDL's metacheck-constrained thermal
syndrome distribution within a polynomial pointwise ratio.

**The two submissions on pātai 2″ (multiscale grooming; decimated BP sampler).**
* The grooming submission's differential inequality is asserted, not derived.
* The sampler's per-level pointwise error bound ε₀e^{−γj} is asserted without derivation, and so are
  its claims of bounded tree-width and a polymer expansion.
* BDL §6 is the explicit-embedding construction and a classical 2D self-correcting code
  (their Theorem 6.1), not a classical model of the syndrome marginal, as the sampler submission
  describes it.

Neither closes pātai 2″.

---

## Pātai 2″ — cluster-expansion route (26 October): companion paper verified; route sharpened

**Verified source.** Balasubramanian, Davydova, Lin and Thorngren, "A thermally and perturbatively
stable classical spin model in two dimensions", arXiv:2610.22548 (15 October 2026). It proves
stability of the 2D classical model of BDL §6 (Theorem 6.1) by a recursive application of the cluster
expansion. The abstract does not mention "gauge averaging", which the submission attributes to it.

**Corrections to the submissions.**
* The stabilizer terms have uniform strength. Metachecks are constraints, not couplings decaying
  like e^{−μj}.
* Each scale carries Θ(n) polymers. A tail bound summed over scales alone, Σ_j e^{−μj} = O(1),
  omits the sum over locations. A fixed truncation order leaves an O(1) error per site, which totals
  Θ(n).

**Sharpened route (pātai 2‴).**
1. **Convergence.** A convergent (Kotecký–Preiss) polymer representation of the X- and Z-syndrome
   Gibbs laws of C(k). Source candidate: the recursive cluster expansion of arXiv:2610.22548,
   extended from the 2D classical model to the syndrome laws of the 3D code, including conditional
   (boundary-fixed) measures.
2. **Approximate counting.** Algorithmic cluster expansion at low temperature: Helmuth, Perkins and
   Regts, "Algorithmic Pirogov–Sinai theory", Probab. Theory Relat. Fields (2020),
   arXiv:1806.11548. A truncation order of about log n gives relative error 1/poly(n) for the
   conditional partition functions.
3. **Sampling.** Self-reducibility (Jerrum, Valiant and Vazirani, Theoret. Comput. Sci. 43, 1986).
   With n conditional steps each accurate to ε/n, the sampled law is within a factor (1 ± ε) of
   π_synd at every configuration. That is a warm start with C = O(1).

**To verify.**
* Step 1 for the 3D quantum code's syndrome laws.
* Polymer enumeration in poly(n) despite the non-LDPC metachecks, since step 2 assumes bounded
  degree.

---

## Targets 1 and 2 (five submissions, 26 October): not closed; error-sampling reformulation

**Not closed.**
* **Target 2.** "Metachecks are local edges with degree 3 + c" contradicts BDL, whose footnotes 2 and
  4 describe metachecks "whose weight scales with the system size" and a metacheck matrix that "is
  not LDPC". A constraint on about n variables has unbounded degree in any representation.
* **Decay with depth.** The e^{−μ·depth} weight decay is repeated without support; the stabilizer
  terms have uniform strength.
* **The companion paper.** arXiv:2610.22548 treats the 2D classical model. Its extension to the 3D
  code's syndrome laws is Target 1 itself, not a supplied fact.
* **Target 1.** Self-reducibility pins up to all n variables, so the pinned set becomes extensive.
  Perturbative stability against local Hamiltonian terms is not stability under extensive
  pinning.

**Reformulation: sample errors, not syndromes.**
* π_synd(s) ∝ e^{−β|s|} on valid syndromes, since every valid sector has equal dimension.
* The error model μ(e) ∝ e^{−β|∂e|} on Pauli error patterns pushes forward to exactly π_synd, since
  each valid s has |ker ∂| preimages.
* μ is a bounded-degree local model: its interactions are the code's own O(1)-weight checks.
* Metachecks are satisfied automatically by syndromes of errors, so the non-LDPC obstacle to Target 2
  disappears.

**Remaining difficulty (pātai 2⁗).** μ has a local gauge symmetry, e ↦ e + g for any stabilizer g.
* A polymer representation modulo this symmetry is needed. Candidate polymers: connected syndrome
  clusters, each the boundary of a nearby error.
* Clusters that are valid only when paired with distant ones are to be controlled by BDL's
  coboundary-expansion bound (their eq. (6); exponent γ, Outlook item 6).
* Then the Kotecký–Preiss convergence, Helmuth–Perkins–Regts counting and
  Jerrum–Valiant–Vazirani sampling chain applies on a bounded-degree model.

---

## Gauge-factored polymer submissions (26 October): the crux isolated as metacheck soundness (pātai 2⁵)

**Assessment.**
* The Jerrum–Valiant–Vazirani error accumulation is correct: N steps of relative error ε/N give a
  factor at most e^ε, so C = O(1).
* Step 3 asserts the crux and misreads BDL eq. (6). That equation reads
  |δe| ≥ α·min_b |e + b|^γ: a polynomial bound controlling error size by syndrome size. It is not a
  linear activity bound, and it does not count errors.
* In syndrome space the degeneracy Ω(s) = |ker ∂| is constant on valid syndromes, so
  π_synd(s) ∝ e^{−β|s|}·𝟙[s valid] carries no error entropy at all. The only obstacle is the
  validity indicator.
* With non-LDPC metachecks, a component can be invalid alone and valid only when paired with a
  distant one. Polymers are then not compatible-iff-disjoint, and the claim in Step 4 that
  metachecks are "entirely absent" passes over this.

**Pātai 2⁵ (metacheck soundness).** For the BDL complexes, prove that every valid syndrome decomposes,
at a fixed interaction range r₀, into connected components each of which is individually valid,
except for components of size at least n^κ for some κ > 0. This is coboundary expansion one degree
up the complex, for the metacheck map, analogous to BDL eq. (6).

**Given pātai 2⁵, the chain closes.**
1. Exceptional clusters are suppressed by e^{−β n^κ}, which beats their poly(n) placements.
2. The remaining clusters form a hard-core polymer gas with activity e^{−β|γ|} on a bounded-degree
   graph, and the Kotecký–Preiss condition holds for large β.
3. Helmuth–Perkins–Regts counting and Jerrum–Valiant–Vazirani sampling give a warm start with
   C = O(1).
4. The warm-start extension of Chesi–Loss–Bravyi–Terhal then preserves the lifetime, and the branch
   closes through `StageSchedule.total_with_transfers`.

---

## Metacheck-soundness submissions (five, 26 October): not closed; the question made computable

**Why these submissions do not close it.**
* **Contractibility.** BDL's complexes are Tanner square complexes and sheaf codes with a random
  embedding, not cell complexes of a 3D manifold. "A small patch is homeomorphic to B³, hence exact"
  does not apply, and local non-exactness (point-like excitations at punctures) is what BDL warn of
  in Brell's proposal.
* **"Exact local projector."** If the metachecks were locally generated, the metacheck matrix would
  be LDPC; BDL state that it is not.
* **Decoupling lemma.** Syndromes live over F₂. There I − ∂†(∂∂†)⁻¹∂ is not an orthogonal projector,
  ∂∂† need not be invertible, and commutator norms of real matrices do not decide F₂ membership.
  The decay with tree distance is asserted.
* **A shared confusion.** Passing the metachecks of bounded support is not the same as validity. A
  small cluster can pass every local metacheck and still have odd overlap with a large one.

**The exact computable question (pātai 2⁵ made concrete).** For BDL's C(k), let
w_min(k) = min{ |s| : s passes every metacheck of support ≤ r₀, yet M·s ≠ 0 for some metacheck M }.
* If w_min(k) ≥ n_k^κ, pātai 2⁵ holds and the chain closes.
* If w_min(k) = O(1), the polymer route fails as stated.

This is finite linear algebra over F₂ at each level k. Claude can compute it for small k given BDL's
code matrices, the same way the surface-code distances were certified. Building the construction from
the paper alone is possible but substantial.

**Suggested step.** Ask the authors (Balasubramanian, Davydova, Lin; arXiv:2605.10943) for their
construction or matrices, and whether they know of this soundness property. Their Outlook item 2 is
this problem.

---

## COMPUTED (26 October): metacheck soundness at a fixed range is FALSE for the BDL codes

**Method.** `checks/bdl-metacheck/bdl.py` builds C(i) algebraically from arXiv:2605.10943 §3.2.2,
with ℓ = 3. The embedding does not change the complex.
* Checks: δ¹∘δ⁰ = 0 at every level, and the logical count is 1 at levels 0, 1 and 2 (13, 206 and
  5,116 qubits), as the paper proves.
* `soundness.py` computes D, the span of all dependencies; D_loc(r), the span of dependencies
  supported in radius-r balls; and an exhaustive search for connected clusters that pass D_loc(r)
  but are invalid.

**Results.**

| Level | Family | Radius r | dim D | dim D_loc | Smallest dangerous cluster |
|---|---|---|---|---|---|
| 1 | Z-checks | 2 | 15 | 8 | 1 |
| 1 | Z-checks | 3 | 15 | 13 | 1 |
| 1 | Z-checks | ≥ 4 | 15 | 15 | none (all locally generated) |
| 2 | Z-checks | 4, 6, 8, 10 | 15 | 0, 4, 8, 13 | 1 |
| 2 | Z-checks | 12 | 15 | 15 | none |
| 2 | X-checks | ≥ 4 | 366 | 366 | none (new metachecks; the next R_X stretches them) |

**Conclusion.** Each iteration stretches the existing metachecks by the scale factor ℓ: the radius
needed goes from 4 to 12, a factor 3 = ℓ. At level k the old metachecks have support of order ℓ^k,
which matches BDL's "metachecks whose weight scales with the system size". For any fixed range r₀,
a single violated check is therefore a dangerous cluster at high enough level, so w_min = 1.
Pātai 2⁵ as stated (fixed-range soundness) is false. Brute-force polymer gases at fixed range
cannot work.

**Corrected target (pātai 2⁶).** A multiscale, recursive cluster expansion treats level-j metachecks
at scale ℓ^j. This is the technique of Balasubramanian, Davydova, Lin and Thorngren,
arXiv:2610.22548, for the classical 2D model. The task is to extend it to the X- and Z-syndrome Gibbs
measures of the 3D quantum code C(k), and to give an algorithmic, sampling version of the multiscale
expansion: a multiscale analogue of Helmuth–Perkins–Regts with Jerrum–Valiant–Vazirani sampling,
reaching a warm start with C = poly(n).

Research-level; open.

---

## Multiscale and "BCRD bridge" submissions (four, 26 October): not closed; foothold is BDL Theorem 4.7

**Why these submissions fail.**
* The renormalization contraction ε_{j+1} ≤ Cε_j^α e^{−βΔc₀ℓ^j} is asserted. BDL eq. (6) is a
  polynomial expansion bound.
* The top-down sampler's per-level error is undercounted. Each conditional law
  P(s^{(j)}|s^{(j+1)}) is over Θ(n_j) variables, so pointwise-accurate sampling of it is the original
  problem at size n_j.
* The "relational tree" changes the metric, not the measure. The polymer activity e^{−β|Γ|_rel}
  omits the entropy of the violated checks inside each block, which holds up to ℓ^{3j} checks. The
  computed partner requirement at distance ℓ^j is unchanged.
* Exact splitting over F₂ holds for any short exact sequence of vector spaces but gives no locality;
  local splitting is the question. Operator norms over F₂ are not meaningful.
* These submissions do not address the substantive BCRD question: whether entanglement-type relations
  are identity-constituting under P2 and P3.

**Foothold (read directly).** BDL Theorem 4.7, for R_X; §4 gives the R_Z analogue. For every level-i
syndrome σ there is a locally computable coarse-graining σ ↦ (σ′, f) with σ = δf + F(σ′) and
|σ′| ≤ |σ|/2. Every valid syndrome is therefore a locally valid part δf plus the embedded image of a
coarser syndrome of at most half the weight. This is metacheck soundness in multiscale form.

**Pātai 2⁷ (the sharpened target).** Build a sampler that inverts this decomposition: sample σ′ at
level i − 1 recursively, then the local f, then set σ = δf + F(σ′). Bound its pointwise ratio to the
thermal law π_i level by level, by counting the fibres {(σ′, f) ↦ σ} and their Boltzmann weights. BDL's
lifetime analysis (§4–5) controls these coarse-graining steps under the Gibbs measure and is the base
to build on.

---

## Fibre-counting submissions (three, 26 October): wrong direction; the renormalised measure is assumed

**Why these submissions fail.**
* **The inequality runs the wrong way.** A warm start needs μ̃ ≤ Cπ, that is, sup μ̃/π. All three
  bound π/μ̃ instead. One displayed bound, exp(−(β/2 − c₀/n^γ)|σ| + ΔZ), decays with |σ|, which
  would put π far below μ̃ on heavy syndromes — the opposite of a warm start.
* **The key step is assumed.** Sampling σ′ ∼ π_{i−1} and then f from a local rule reproduces π_i
  only if two things hold:
  - the push-forward of π_i under BDL's coarse-graining map equals π_{i−1}, or is controllably close;
  - P(f|σ′) is π_i's conditional.
  Neither is shown, and the first is generally false. A renormalised measure is not the coarser Gibbs
  law, since |σ| = |δf + F(σ′)| is not a function of σ′ alone. The fibre bound
  log|𝓕_σ| ≤ c₀|σ|/n^γ and the "Bayes" factorisation both presuppose it.
* **The remainder does not touch the gap.**
  - Dobrushin total-variation contraction gives no pointwise ratio.
  - The tail-sum algebra is correct only given the per-level errors δ_i, which are not derived.
  - Azuma concentration for local observables is unrelated to pointwise domination.

**Pātai 2⁸ (sharpened).** Compute the renormalised measure: the push-forward of π_i under the
Theorem 4.7 coarse-graining map (and its R_Z analogue), as a Gibbs-like law on level-(i − 1)
syndromes with explicit effective weights. Then bound sup_σ μ̃_i(σ)/π_i(σ) for the reverse sampler,
level by level.

---

## Renormalised-measure submissions (two, 26 October): correct object, crux asserted; corrected design (pātai 2⁹)

**What is correct.** The renormalised law π_i^coarse(σ′) with effective Hamiltonian
H_eff(σ′) = |F(σ′)| − β⁻¹ log 𝒵_fiber(σ′) is the right object.

**Why these submissions fail.**
* Step 4 asserts Z_i/(Z_{i−1}𝒵_fiber) = 1 + O(e^{−cn^γ}). But 𝒵_fiber depends on σ′, and its
  variation is H_eff. A sampler drawing σ′ ∼ π_{i−1}, with energy |σ′|, is off from π_i^coarse by
  e^{β(H_eff(σ′) − |σ′|)} pointwise. That factor is extensive, not 1 + small.
* The bounds on F (|F(σ′)| ≤ |σ′|, "norm ≤ 1") are unsupported. F lifts by thickening or doubling.
* Wasserstein-1 contraction does not give pointwise domination.

**Pātai 2⁹ (corrected design).**
1. Sample each coarse level from the renormalised law π_i^coarse itself, so that the recursion samples
   a flow of effective models.
2. **Fine step.** Given σ′, the conditional law of the local correction f is a local, bounded-degree
   Markov random field; f are free local cochains with no metachecks. Helmuth–Perkins–Regts counting
   with Jerrum–Valiant–Vazirani sampling then gives pointwise accuracy 1 ± ε/n_i. To verify against
   Theorem 4.7's local rule: that the constraint "lies in the image of the coarse-graining map" is
   local.
3. **RG stability (the open content).** Show that the effective potentials stay finite-range and small
   at every level, by a recursive cluster expansion in the manner of arXiv:2610.22548, so that each
   level's model stays in the class handled by step 2.

Given steps 2 and 3, the reverse sampler is pointwise accurate, with C = O(1).
