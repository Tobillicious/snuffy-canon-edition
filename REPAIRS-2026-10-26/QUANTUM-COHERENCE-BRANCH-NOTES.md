# Quantum-coherence holding branch — notes for the author (26 October 2026)

**Question.** Can the full quantum coherence of each particular be held indefinitely at fixed failure
ε with holding power Θ(1), uniformly in age? The author is working on this branch. These notes record
Claude's assessment; they do not change the target.

## The submission under review (pasted by the author): the "Tri-Partite Coherence Preservation Architecture"

* **Tier 1** converts continuous drift to erasures with GKP–surface codes.
  - Assessment: it lowers the effective error rate by a constant factor. Residual non-erasure errors
    remain, so the failure rate per unit time stays constant and the total failure grows with age.
* **Tier 2** uses a holographic tensor-network scaffold.
  - Assessment: no constant-overhead threshold under local noise has been proved for holographic
    codes. At fixed size the lifetime is still fixed.
* **Tier 3** is a driven–dissipative engine with a non-equilibrium steady state, dρ/dt = 𝓛ρ = 0,
  unique.
  - Assessment: a unique steady state does not depend on the initial state, so it stores nothing.
  - A memory needs a degenerate steady manifold. Local perturbations lift that degeneracy, giving a
    finite lifetime.

## A likely no-go in three or fewer dimensions (for the author to weigh)

1. **Fixed size forgets.** Let local noise of positive rate act on every qubit at every step, and
   compose it with any correction channel. The composite is strictly positive, so it has a unique
   fixed point and contracts exponentially. A memory of fixed size therefore forgets at an
   exponential rate.
2. **Fixed ε at every age needs growing size.** A distance-d code has a logical failure rate per
   step of order (p/p_th)^{d/2}. Holding ε over age t needs d, and so the number of physical
   qubits, of order log(t/ε).
3. **Active protection costs growing power.** Noise injects entropy into each physical qubit at a
   constant rate. Removing it costs at least k_B T ln 2 per bit of entropy (Landauer). The holding
   power is therefore at least of order log t.
4. **Passive protection does not remove the cost in ≤ 3D.**
   - Bravyi and Terhal (New J. Phys. 11, 043029, 2009) prove there is no self-correcting
     2D stabilizer memory.
   - Haah's 3D cubic code has a lifetime bounded at fixed temperature (Bravyi and Haah, PRL 111,
     200501, 2013).
   - The 4D toric code is self-correcting.
5. **Classical records escape.** A growing energy barrier suppresses flips without pumping
   (`PassiveReference`: total failure ≤ ε, total cost O(log² t)).

**Consequence if this holds.** Indefinite holding of full quantum coherence at fixed ε needs power of
order log t in three or fewer dimensions. The Θ(1)-rate maintenance demand (master line 536) then holds
for the objective classical record and its relations, which `PassiveReference` and the item-5 modules
already cover.

**Decision.** The author's. No canon text has been changed.

---

## Tier proofs 1–3 (pasted by the author, 26 October): assessment

None removes the age dependence. Each leaves either a constant logical failure rate per unit time
or a resource that grows like log t.

* **Tier 1 (GKP erasure conversion).**
  - A shift beyond the Voronoi boundary is not heralded. It is indistinguishable from a smaller
    shift in the opposite direction, so it becomes a silent logical error. Soft information can flag
    shifts near the boundary, but unheralded errors remain at a positive rate, not O(P²).
  - The 50% erasure threshold is the code-capacity threshold for pure erasure.
  - Whatever the threshold, a fixed d below threshold gives a constant logical failure rate per
    round, so P_fail ≈ rate · t. The conclusion "without requiring d to grow with age" does not
    follow.
* **Tier 2 (holographic tensor network).**
  - The submission's own Lemma 1 gives N_boundary = O(log t): the boundary resource grows like log
    t. That is the same growth, relocated, not removed.
  - No threshold under local noise with constant overhead has been proved for HaPPY-type codes. The
    recurrence p_{k+1} ≤ C p_k² is asserted.
  - At fixed size the centre logical has a fixed distance, and therefore a fixed failure rate per
    step.
* **Tier 3 (driven–dissipative NESS).**
  - Lemma 1 asserts a unique steady state, which stores no information.
  - Its step 3 describes a degenerate null space (all states commuting with the stabilizer
    projectors), which contradicts that uniqueness.
  - With environmental jump operators present, the degeneracy is lifted. The logical manifold then
    mixes at a rate of order the logical error rate, so its lifetime is finite.
  - The stationary entropy bound applies to the physical error sectors, not to the stored logical
    information. The logical subsystem's entropy tends to its maximum as t → ∞, while the physical
    error density stays stationary.

**Status.** The likely no-go recorded above stands. In three or fewer dimensions, indefinite holding of
quantum coherence at fixed ε needs power of order log t. The branch is the author's to decide.

---

## The 4D exemption (pasted by the author, 26 October): accepted, with two refinements

**Accepted.** The 4D toric code is self-correcting below T_c:
* its excitations are loops;
* a logical error must sweep a membrane whose boundary grows to order L, so the energy barrier is
  Θ(L);
* its lifetime is τ(L) ~ e^{cL/k_BT}.

DKLP (2002) proposed it. The thermal stability proof is Alicki, Horodecki, Horodecki and Horodecki,
Open Syst. Inf. Dyn. 17, 1 (2010).

**Refinement 1.** At fixed L the lifetime is finite. Holding ε at age t needs L ~ (k_BT/c) ln(t/ε),
so the size still grows logarithmically, but passively: no pumping and no running power. The cost
structure is the one in `PassiveReference`: growth or rewrite on a doubling schedule, with sublinear
total cost and a Θ(1) long-run holding rate. The submission's "without time-dependent spatial
growth" is too strong.

**Refinement 2.** Physical space is three-dimensional. Embedding a 4D lattice in 3D needs couplings
whose range grows with L.
* Local 3D stabilizer codes with translation and scale symmetry are not self-correcting (Yoshida,
  Ann. Phys. 326, 2566, 2011).
* Haah's cubic code has a bounded lifetime at fixed temperature.
* Review: Brown et al., Rev. Mod. Phys. 88, 045005 (2016).

**The branch reduces to one question.** Can the installation realise a self-correcting quantum memory
(4D-type or equivalent) with couplings of bounded cost in three-dimensional space?
* **If yes**, quantum coherence holds at a Θ(1) rate, on the classical pattern.
* **If no**, holding power grows like log t.

This remains the author's open branch.

---

## CORRECTION (26 October): a 3D self-correcting memory exists; the "likely no-go" above is superseded

The author supplied Balasubramanian, Davydova and Lin, "A passive self-correcting quantum memory in
three dimensions", arXiv:2605.10943 (11 May 2026; preprint, 102 pp.). Claude fetched the record and
read the main results directly; the text was extracted locally.

**Theorem 1.1 (rigorous for the random-embedding construction).**
* There is a family of 3D local Hamiltonians H_k of CSS stabilizer codes C(k) on n_k = e^{Θ(k)}
  qubits.
* Each code encodes one logical qubit, with encoding and decoding maps satisfying Dec_k∘Enc_k = id.
* Constants T_c > 0 and η > 0, independent of k, are such that for T < T_c:
  ‖Φ_{1/T,t}∘Enc_k(ρ_L) − Enc_k(ρ_L)‖₁ ≤ t·exp(−Θ(n_k^η)), and t_mem ≥ exp(Θ(n_k^η)).
* The thermal model is Markovian Lindblad evolution with O(1)-support jump operators and Gibbs
  fixed point (e.g. generalised Glauber).

**Theorem 1.2 (embedding in R³).** Each term has support within a ball of radius O(1), and every unit
ball holds O(1) qubits.

**Why it escapes the cited no-go results.** They assume translation invariance (Yoshida; Haah-type
codes), and this construction breaks it. The earlier statement in these notes, that no
self-correcting quantum memory is known in three or fewer dimensions, was out of date.

**Consequence for the branch.** Holding ε at age t needs n ≳ (ln(t/ε)/c)^{1/η}. That is
polylogarithmic in t, and passive: there is no running power. On a doubling schedule the total cost
is polylog(t), so the long-run quantum holding rate is Θ(1) or better. The branch closes in the
affirmative subject to:

1. **Preprint status.** The paper is unrefereed.
2. **The remaining join: transfer at each doubling stage.** Each stage needs a fault-tolerant transfer
   or encoding into C(k+1), with failure at most ε/2^{j+1} and polylog cost. The paper's Outlook item
   2 lists efficient initialisation of the thermal encoding as open.
3. **Scope of the proof.** The lifetime proof covers the random embedding; the explicit embedding's
   proof is left to future work. Perturbative stability (TQO-2) is promised for an updated version.
