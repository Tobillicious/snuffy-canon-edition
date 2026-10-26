# Item 2 of the Codex handoff: the noisy preparation join (Claude, 26 October 2026)

Target unchanged: the full quantum holding branch at the original stage error budget, with
arbitrary references, polynomial pathwise work, and the complete G3 bill. This note sharpens what
the G.21 ideal sampler does and does not supply once the preparation gates are noisy.

## Proposition N1 (a pointwise warm start does not survive a constant-rate final layer) — proved

Let the last physical layer of the preparation apply, independently on every qubit q of a packing
set Q (the δq pairwise disjoint and non-adjacent, |Q| ≥ n/K), a Pauli flip with probability
p ∈ (0, 1/2). Here δq is the flip's syndrome pattern, of weight at least w. Let ν = μ ⊛ N be the
prepared syndrome law, for any ideal law μ whatsoever.

1. *Smoothness.* ν(s ⊕ δq) ≥ (p/(1−p)) ν(s) for every s and q ∈ Q, because
   N(e ⊕ q) ≥ (p/(1−p)) N(e) termwise.
2. *Comparison.* For s with δq ∩ s = ∅ on a set Q′ ⊆ Q of size k,
   π(s ⊕ δQ′)/π(s) = e^{−βwk}, while ν(s ⊕ δQ′) ≥ (p/(1−p))^k ν(s).
3. *Choice of s.* If p·w ≤ 1/(4KK′), the low-weight set {|s| ≤ n/(2KK′)} has ν-mass and π-mass at
   least 1/2 each, so it contains s* with ν(s*) ≥ π(s*)/2. Here K′ bounds how many δq meet a
   syndrome bit. Then k ≥ n/(2K) qubits of Q are free at s*.

Hence sup_s ν(s)/π(s) ≥ ½ (p e^{βw}/(1−p))^{n/(2K)}. This is exponential in n as soon as
p e^{βw} > 2(1−p). At the G.21 sampler temperature (z₀ = e^{−β} < δ = [4eB(Δ+2)]^{−4}), this holds
for every realistic device fault rate. No choice of ideal law μ and no hotter comparison
temperature repairs it, because pointwise domination with a polynomial constant forces the two
laws to agree on every local pattern's activity.

So the G.21 sampler cannot by itself make the *physical* prepared state a warm start. This is a
fact about the comparison, not a defect of the sampler.

## Proposition N2 (domination survives the fault layer) — proved

If μ ≤ Cπ, then ν = μ ⊛ N ≤ C (π ⊛ N), since convolution with a positive kernel preserves
pointwise order. In operator form, with the reference retained as in G.21:

    ρ_prep,LR ≤ 4C · (N ⊗ id_R)(ρ_β ⊗ ρ_R).

This holds for any CPTP fault channel N, local stochastic or not, applied after the ideal branch
preparation.

Faults interleaved with the preparation are commuted to the end as Pauli faults in the usual way,
because the branch preparation is the codespace encoder followed by a Pauli O_s. The encoder's own
faults need the ExRec treatment, see item (b) below.

## Heuristic N3 (why "close to thermal up to ε" also fails) — derived, not proved

Write both laws as polymer gases with activities a_ν(Γ) (fault layer on top of the ideal law) and
a_π(Γ) (thermal). On ν-typical configurations, the cluster expansion gives

    log ν/π ≈ N · Σ_Γ a_ν(Γ) φ(a_π(Γ)/a_ν(Γ)),   with φ(x) = x − 1 − log x ≥ 0,

which vanishes only if a_ν = a_π for every local pattern. A fault layer at a fixed rate p, unknown
beyond its local stochastic bound, cannot match every thermal activity. So ν and π are
asymptotically singular, and domination on a set of ν-probability 1 − ε fails as well as pointwise
domination. Exact deconvolution μ = π ⊛ N⁻¹ would need the fault channel known exactly, and the
divided kernel to stay positive under (1 − 2p)^{−|χ|} amplification.

Hence no argument of the form "the prepared law is close to π" (pointwise, up to ε, or in trace
distance) survives physical gates. The holding dynamics itself must carry the faulted state. This
is (R). Any proof that concludes μ_prep ≤ A n^p π for a noisy preparation contradicts N1.

## The precise remaining statement

By N2 and the G.21 holding derivation (positive order, CP of Φ_t, the protected dressed Paulis), the
quantum branch closes once the following holds for the one universal state N(ρ_β), which is
independent of the sampler and of the logical input:

**(R) Robust bad-weight bound.** For the BDL family below the stated temperature and every local
stochastic fault channel N of rate p ≤ p₀, there are c, η′ > 0 with

    Tr(P^⊥ Φ_t(N(ρ_β))) ≤ poly(n) e^{−c n^{η′}}   for all t ≤ e^{c n^{η′}}.

Given (R), the G.21 estimate goes through with b replaced by this bound. Each stage's code size is
chosen from c n_j^{η′} as in G.19, and StageSchedule.total_with_transfers sums the stages.

The same statement, with N also acting during holding (non-thermal noise alongside the Davies
bath), is what a physical installation needs anyway. BDL Theorem 1.1 is proved for the Davies
semigroup alone. (R) is therefore not a new kind of requirement introduced by preparation; it is
the robustness of the passive memory to the non-thermal part of the device noise.

## What (R) needs, and the routes

(a) **Stationarity is unavailable for N(ρ_β)**, so the proof must use locality: a sparse fault
layer creates history polymers with activity at most (B′p)^{|Γ|/c}, which is subcritical below a
threshold. The bad event requires a large polymer, at scale ≥ n^{η}, in the history representation.
A route is a disagreement-coupling of the Davies dynamics from N(ρ_β) and from ρ_β under the same
graphical randomness, showing the disagreement set stays subcritical: an isolated fault is undone
by a downhill flip at rate Θ(1) and spreads only through excitation moves. Its control is the
missing estimate.

(b) **Encoder faults.** Faults inside the codespace encoder are not a final Pauli layer in general.
They are handled by the existing ExRec / KnillLaflamme chain only if the encoder is built from
fault-tolerant gadgets, in which case they reduce to a local stochastic Pauli layer plus a logical
failure of probability at most the stage budget. This identification is to be written against
`ExRecBound` and the G1 sources.

(c) **Literature to read first.** Before asking the author, check:
- the BDL paper's own discussion of perturbations;
- Alicki–Fannes–Horodecki on 4D toric thermal stability;
- stability of self-correcting memories under non-thermal noise.

Statement (R) is the precise question if no source supplies it.

## Literature check (done 26 October)

- **BDL, §1.3 item 2 and footnote 4.** BDL leave initialisation open: "energetic bottlenecks might
  be an obstruction for rapid mixing". They point to Bergamaschi–Gheissari–Liu (their [25]) and note
  that BGL's results need an LDPC metacheck matrix, "which is not the case in our code". This agrees
  with our computation in `checks/bdl-metacheck` that the metachecks stretch by ℓ per level.
- **Bergamaschi, Gheissari and Liu, arXiv:2507.10976 (SODA 2026), Theorem 1.7.** Under the
  connectedness criterion (Properties 5.12: LDPC checks and metachecks, an energy barrier, locally
  erasable small clusters), a polylog(n)-local Lindbladian started from a ground state satisfies
  ‖e^{tL}[ψ] − ρ_β^ψ‖₁ ≤ c₁ n e^{−c₂t} + t n e^{−(β−β_M) log^{c₃} n}. The proof is path coupling
  within a high-measure set of geometrically well-behaved configurations ("cluster-distance
  contraction"), with a memory lemma keeping the chain in that set. It does not treat non-thermal
  noise, and the chain is a designed sampler, not the physical bath.

- **BGL, introduction, on the state of the art.** In BGL's words: "in the absence of monotonicity,
  even proving the ground state stability for the 4D toric code is still an open problem: current
  techniques are insufficient to rigorously rule out the possibility that running Glauber dynamics
  from the ground state quickly loses the logical information." Statement (R) asks for stability
  under the physical Glauber/Davies dynamics from a *faulted* state, on BDL's code (non-LDPC
  metachecks). It is therefore at least as hard as a stability question the field records as open.
  It is a research step, not a retrieval or integration gap.
- **Why the obvious escapes fail.**
  - The ground state is a warm start with C = Z = e^{O(n e^{−β})}. That beats b = e^{−c n^η} only if
    β grows like (1−η) log n.
  - Even then, the final-layer faults restore an exponential factor unless the bare fault rate falls
    like n^{−w(1−η)}, which is not a fixed device inequality.
  - Relative entropy and Hölder interpolation lose a factor linear in n against the n^η exponent.
  - A local (per-site) domination ν_t|_R ≤ K^{|R|} π|_R would suffice, because history polymers have
    thermal probability exponential in their size. However, Davies dynamics is not known to
    preserve such a bound; positivity plus stationarity preserve only the global one.

## Two consequences

1. **Trace distance suffices for the holding bound.** Once a state σ is within ε′ in trace
   distance of the thermal encoding Enc_β(ρ_LR), contraction of trace distance under CPTP maps gives
   ‖(Dec Φ_t ⊗ id)(σ) − ρ_LR‖₁ ≤ ε′ + (the BDL/G.21 bound). A within-sector mixing theorem that
   starts from N(ψ) therefore closes (R) without any pointwise domination. Here N(ψ) is a
   ground state hit by the sparse fault layer. Such a state lies in BGL's well-behaved set with high
   probability below threshold.
2. **The history lift supplies the LDPC structure BDL lack.** In the G.21 history representation,
   every constraint has bounded scope and bounded incidence, uniformly in level. A single-qubit flip
   changes O(1) history coordinates per level, so O(log n) coordinates in all, a polylog locality
   matching BGL's block dynamics. The proposed route is therefore to verify Properties 5.6 and 5.10
   for the history factor graph (energy barrier and local erasability, with components measured in
   the primal graph G). Then BGL's path coupling would be run on histories, started from the noisy
   ground state.

   Two joins remain.
   - The block updates must themselves be implemented by the installation, and their faults
     re-enter as a sparse layer. The memory lemma must therefore be proved with that layer, which
     needs a contraction margin. Path coupling's contraction is exactly where such a margin lives.
   - The passive-holding statement (R′) is (R) with non-thermal noise during holding.

## What the BGL route transfers, and what it cannot avoid

- **Domain SSM transfers.** BGL's spatial-mixing input (their Theorem 1.6) holds for the history
  polymer gas. G.21 proves Kotecký–Preiss convergence with explicit constants on the
  bounded-degree history graph, and boundary conditions are polymer deletions, which preserve the
  criterion (G.21 §4). The standard cluster-expansion argument then gives exponential decay of
  boundary influence uniformly in level. This is derived, not compiled.
- **Local erasability transfers.** Every history component has its correction inside a bounded
  neighbourhood at each level, by BDL Theorems 4.6 and 4.7, Remarks 4.4–4.5 and the componentwise
  coarse-graining of their §5.2.
- **The fault layer cannot be avoided by contraction.** A path-coupling contraction of rate κ, with
  noisy block updates each perturbing O(pn) coordinates, keeps the chain within O(pn/κ) of its
  target in Hamming/Wasserstein distance, not in trace distance. Every physically prepared state is
  therefore "thermal encoding plus a sparse fault layer", and (R) is the unavoidable remaining
  statement. Its content is that the physical holding dynamics heals sparse disagreements, starting
  from N(ρ_β). Below threshold, an isolated flip is undone downhill at rate Θ(1), and uphill moves
  cost e^{−βΔ}. The missing estimate is that disagreements spread subcritically under the energy
  non-increasing moves.

## Numerical probe (not a proof): `checks/bdl-metacheck/healing_probe.py`

The probe runs on the level-2 code (5,116 qubits, 2,256 Z-checks), from the 3 × 2 seed. It starts
from a random fault layer of density p and runs single-site heat-bath dynamics with energy equal to
the number of violated Z-checks. Results are in `HEALING-PROBE-LEVEL2.jsonl`, 3 trials per row.

- β = 6:
  - p = 0: the excitation count fluctuates at 0–4;
  - p = 0.005: about 60 excitations fall to 2–11 after 100 sweeps;
  - p = 0.02: about 220 fall to 7–13.
- β = 8:
  - p = 0: the count stays at 0;
  - p = 0.005: about 58 fall to 0–5, with one trial reaching syndrome zero with no logical error;
  - p = 0.02: about 220 fall to 6–11.

Most of the fault layer heals within about 10 sweeps. A sparse residue of stuck excitations then
decays slowly, consistent with BDL's warning about energetic bottlenecks. The logical question
cannot be resolved at this size. The probe suggests stating (R) for the actual dynamics as "the
residual excitation set stays sparse and isolated, and so cannot assemble the large history
polymer that the bad event needs", rather than as complete healing.

Status: N1 and N2 are proved above, in elementary form. (R) is open; its literature status is
recorded, and the history-lift route is the next construction. The target is unchanged.

## Disposition: pasted "Local Warm-Start Exponential Decay" proof (26 October, evening)

The paste claims ‖ρ_R^prep − ρ_R^thermal‖₁ ≤ C K^{|∂R|} f(p). It is not adopted, for four reasons.

1. **The bound is false at time zero.** For a single qubit, the fault layer moves the marginal by
   order p, with no decay. For larger R the two marginals differ at constant density over |R|
   sites, so their trace distance rises towards 1 with |R| (N3 applied locally). It does not fall
   like K^{|∂R|}.
2. **Step 2 assumes the open statement.** It posits that a local recovery channel contracts to the
   thermal marginal with K < 1, which is (R) itself. It also uses active recovery, not the passive
   holding dynamics.
3. **Lieb–Robinson lightcones do not localise anything here.** At the exponentially long holding
   times in question, they cover the whole system.
4. **It targets the wrong quantity.** The local warm-start lemma needed is a *multiplicative*
   bound ν_t|_R ≤ K^{|R|} π|_R, preserved for all t ≤ e^{c n^{η′}}. At t = 0 it holds with
   K = 1 + p(e^{βw} − 1). The open content is its preservation in time, which the paste does not
   address.

## The stuck residue is free-hopping point defects (computed 26 October, evening)

`checks/bdl-metacheck/stuck_barrier.py` is run on the level-2 code at β = 8 and p = 0.02, for 100
sweeps and 3 seeds (`STUCK-BARRIER-LEVEL2.jsonl`). Every residual cluster is a single violated
Z-check. None has a downhill single flip, and none can be annihilated by any path of at most 4
flips in its neighbourhood. Each has 3–5 zero-energy single flips that move it.

`hop_orbits.py` computes the components of the zero-energy hop graph: Z-checks, with an edge for
every qubit of syndrome weight 2 (`HOP-ORBITS.jsonl`).

| Level | Z-checks | Components | Largest component | Sink-free components | Checks in sink-free components |
|---|---|---|---|---|---|
| 1 | 136 | 90 | 4 | 62 | 100 |
| 2 | 2,256 | 90 | 72 | 62 | 1,656 |

The number of components stays fixed while their size grows about 18-fold per level. A lone fine
defect therefore wanders for free over a region that grows with the code. It disappears only on
meeting another defect, or by reaching a sink (a weight-1 qubit) where its component has one.
Paths inside a component differ by zero-syndrome cycles. The energy barrier BDL prove forces those
cycles to be stabilizers, so free wandering inside a component by itself causes no logical error.

### Disposition: pasted "Spacetime Polymer Cluster Expansion" proof

It is not adopted.

1. **The activity bound fails on exactly this residue.** The paste assigns every spacetime site of
   a polymer the factor e^{−βΔE}. A free-hopping defect's worldline pays its energy once, at
   creation, and then has weight Θ(1) per unit time. So the activity per spacetime volume is not
   small, and the Kotecký–Preiss sum over worldline lengths diverges with the holding time.
2. **Wrong time scale.** T = O(log n) is not the holding time. Each stage must hold for times up to
   e^{c n^{η′}}.
3. **The trajectory law is not a product over disjoint spacetime supports.** Transition rates depend
   on neighbouring configurations. The rigorous object is a graphical construction with
   disagreement percolation, not an abstract polymer gas.
4. **Gate faults do not occur during passive holding.** The fault factor (p/(1−p))^{|γ|} belongs
   only to the initial time slice.
5. **The threshold is inverted.** Its own convergence condition μ e^{−βΔE+a} p/(1−p) < 1 does not
   give p_c = (1 + μ e^{βΔE})^{−1}.

### What this means for (R)

A correct spacetime argument has to treat the faulted state's leftovers as diffusing charges inside
macroscopic hop components. The precise sub-questions are now these.

- **(R1)** Pairwise annihilation inside a component never produces a logical error. Inside a single
  component this is the stabilizer property of its cycles. Across components it is the coarse-level
  statement.
- **(R2)** The defects that cannot pair inside their component (odd parity) stay at bounded density
  and cannot assemble the large history polymer of the bad event within e^{c n^{η′}}. Their
  motion between components needs uphill moves, which is where the hierarchical barrier enters.

Neither BDL nor BGL proves (R1) or (R2) for the physical dynamics. This sharpens (R) into these two
statements.

## (R1) inside a component: verified at levels 1–2; derived for all levels

`checks/bdl-metacheck/hop_cycles.py` (`HOP-CYCLES.jsonl`) tests every fundamental cycle of the
zero-energy hop graph for membership in the X-stabilizer row space:

| Level | Fundamental cycles | Cycles that are not stabilizers |
|---|---|---|
| 1 | 4 | 0 |
| 2 | 2,062 | 0 |

**Lemma (proved, elementary).** In any graph, two edge sets with the same boundary differ by an
element of the cycle space. So if every hop cycle is a stabilizer, *every* way the dynamics
wanders and pairs defects inside a component yields the same logical class. That class is fixed by
the fault set alone. Free wandering is then logically harmless, whatever the trajectories.

**All levels (derived, not compiled).** A logical hop cycle would be a logical operator reachable at
energy at most 2: create a pair, move one defect around the cycle at zero cost, annihilate. Under
the Davies dynamics it would occur at rate at least e^{−2β}/poly(n), which contradicts BDL
Theorem 1.1's lifetime t·e^{−Θ(n^η)} for large n. The derivation needs the completion
probability of the walk around the cycle to be at least 1/poly(n). BDL state no energy-barrier
theorem for their own code; the barrier is used only through this lifetime contradiction.

The pasted (R1) proof is not needed for this result and is not adopted. It assumes the regions are
small, with diameter much less than L, but the computed components are macroscopic: 90
components cover the code at every level computed.

## (R2) as pasted is false: escape costs O(1)

From the same run, the least single-flip energy cost for a lone defect to leave its hop component
at level 2 is:
- +1 for 1,520 checks;
- +2 for 128 checks;
- no single-flip exit for 608 checks.

The pasted premise ΔE_hier = Θ(n^{η′}) at a component's boundary is false. Defects leave
components at rate about e^{−β}, which happens constantly over e^{c n^{η′}}, so the union bound
N·T/τ_escape exceeds 1. The thermal state itself has such crossings, so confinement is the wrong
mechanism.

The correct (R2) is collective: with within-component class fixed (above), the remaining danger is
inter-component transport. That transport must stay subcritical, in the sense that the
odd-parity charges and the uphill crossings do not assemble the large history polymer of the bad
event. This is the remaining open statement.

## Disposition: pasted "Kinetic Steady-State Dilution" proof

It is not adopted. Its qualitative picture (a diffusing, annihilating dilute gas) matches the
probes, but the load-bearing step is asserted.

1. **The rate equation is mean-field, not a theorem.** dρ/dt = G − kρ² describes the expected
   density only, by mass action. It ignores the correlations that the bad event is about.
   Annihilating random walks in low dimension depart from mean-field kinetics.
2. **Mean density does not give cluster tails.** "ρ below the percolation threshold ⇒ clusters of
   size O(log n)" holds for *independent* site percolation. The dynamic law is correlated, and a
   low mean density does not imply exponential cluster tails. Proving such tails uniformly in time
   is the local warm-start lemma, i.e. (R) itself.
3. **The union over time is missing.** Even granting a tail c₁e^{−c₂s} at each time, the maximum
   over n sites and T ≈ e^{c n^{η′}} times is about (log n + c n^{η′})/c₂ = Θ(n^{η′}), not
   O(log n). That is the same order as the danger scale, so the constants c, c₂, η′ and η would
   have to be compared explicitly.
4. **The wrong bad event.** Logical failure in BDL needs a large *history polymer* across levels,
   not a geometric cluster of fine defects. Defects far apart at the fine level combine at coarse
   levels.
5. **G = O(p) conflates gate faults with holding.** During passive holding, defect generation is
   thermal, at rate about e^{−β}.

The remaining (R) is unchanged: the dynamic law must keep history-polymer tails of the thermal
type uniformly over the stage time. Point 3 shows the constants then matter, and that the stage
time exponent can be chosen against them in the doubling schedule.

## Disposition: pasted Steps 1–2 (particle-system domination; Dobrushin and cluster tails)

These pastes take points 1 and 2 above as steps. They are not adopted, for the reasons below, but
they identify the right shape of the remaining lemma.

**Step 1 (domination by a linear-death process) fails on the computed code.**
- The comparison process kills every defect at rate μ > 0. But a lone defect in a sink-free hop
  component has *no* death channel: there is no downhill flip and no annihilation path of at most
  4 flips (STUCK-BARRIER, HOP-ORBITS). It disappears only by meeting another defect.
- The paste's own proviso μ ≤ kρ_min therefore forces μ = 0, because ρ_min = 0 for an isolated
  defect, and then ρ_max = λ/(μ − z v_max) is meaningless.
- A pathwise Harris coupling η_t ≤ ξ_t also requires a monotone (attractive) system. Annihilation
  A + A → 0 is not monotone: adding a particle can remove another.
- The model also ignores the real move structure:
  - within-component hops are free (rate Θ(1)), and only inter-component moves cost +1 or +2;
  - flips of weight 3 or 4 create several defects at once;
  - defects are constrained by syndrome validity.
- The −z v_max term has no derivation: hopping conserves particle number.

**Step 2 (Dobrushin, then disagreement percolation, then lattice-animal tails) does not follow.**
- Dobrushin's condition concerns a Gibbs specification. The time-t law of a non-equilibrium
  process has no controlled conditional specification.
- A low *mean* density does not imply domination by a product measure. Liggett–Schonmann–Stacey
  domination needs a *conditional* bound: P(η(x) = 1 | the configuration outside a fixed
  neighbourhood of x) ≤ q, uniformly.
- The max over e^{c n^{η′}} times (point 3) is deferred.

**The corrected target, the remaining core lemma.** Uniformly in t ≤ T, and for every history
polymer Γ:

    P_t(Γ present | the history outside a fixed neighbourhood of Γ) ≤ q^{|Γ|}

with q < 1/B, so that the G.21 counting applies. This is the local warm-start lemma in its usable,
conditional (Liggett–Schonmann–Stacey) form, stated for history coordinates (point 4). It holds at
t = 0 for the faulted thermal state with q of order (e^{−β} + p e^{βw})^{1/4}. The open content is
its preservation by the physical dynamics. Points 3 (time union with explicit constants) and 5
(thermal generation) then follow by bookkeeping.

## Point 3 done: the time union (Lemma T) — proved, given the core lemma

**Setting.** Uniformise the holding dynamics: every site has total jump rate at most R, so the
process is a discrete chain X_0, X_1, … run at the times of a Poisson clock of rate Rn. Let A_L be
the event that some history polymer of size at least L is present. Suppose the core lemma holds for
the uniformised chain at every step k ≤ K, with q < 1/B. By the G.21 counting this gives

    P(A_L at step k) ≤ ε_L := M (Bq)^L / (1 − Bq).

**Lemma T.** For any T > 0, take K = ⌈2RnT⌉. Then

    P(A_L at some time t ≤ T) ≤ K ε_L + P(Poisson(RnT) > K) ≤ K ε_L + e^{−RnT/3}.

*Proof.* A_L can hold during [0, T] only at a step reached before T. Apply the union bound over
the first K steps, and the Poisson tail bound P(Poisson(λ) ≥ 2λ) ≤ e^{−λ/3}. ∎

**Choice of constants.** For a target δ, it suffices that

    L ≥ [log(2RnTM/δ) + log(1/(1 − Bq))] / log(1/(Bq)).

With T = e^{c n^{η′}} this is L ≈ (c n^{η′} + O(log n)) / log(1/(Bq)). The bound is useful if L
stays below the smallest polymer size L* that can cause a logical error, of order n^{η} by BDL's
decoder argument. This holds when η′ < η, or when η′ = η and c < c* log(1/(Bq)). The doubling
schedule chooses n_j with 2^j ≤ T(n_j), so this is a choice of stage sizes, not a new hypothesis.

**Disposition of the pasted Step 3.** Its union-bound arithmetic is the right shape and is
superseded by Lemma T. Its other claims are not adopted:
- τ_mix = O(log n) "independent mixing epochs": no such mixing time is established, and BDL warn
  of bottlenecks;
- the Azuma–Hoeffding step: X_m is not a bounded-difference martingale in any stated sense;
- "c₂ > c": asserted without derivation.

**Disposition of the pasted 5-step plan.** It agrees with this note's corrected target. Two notes:
- Step 1, the monotone envelope for pairs: grouping defects into pairs does not restore
  monotonicity, because pair annihilation is still non-attractive.
- Step 4, the preservation of the conditional bound q(t) < 1/B for all t ≤ T, is the core lemma.
  It is stated there as a task, not proved.

## Status of the five points

- 1 and 2: replaced by the conditional core lemma.
- 3: done (Lemma T).
- 4: done (bad event = history polymer, G.21 counting).
- 5: done (thermal generation during holding; the gate faults enter only at t = 0, via N2).

Open: the core lemma's preservation under the physical dynamics.

## Disposition: pasted "Lemma P (Preservation of the Conditional LSS Bound)"

This is the first proposal aimed at the core lemma itself. It is not adopted, for three reasons;
the first two are each fatal.

1. **Its conclusion does not give the lemma.** It bounds Z_t(q) = Σ_Γ q^{|Γ|} P_t(Γ | ext) by 1.
   Since q < 1, this yields only P_t(Γ | ext) ≤ q^{−|Γ|}, which is vacuous. The per-polymer bound
   P_t(Γ | ext) ≤ q^{|Γ|} needs control of Σ_Γ q^{−|Γ|} P_t(Γ | ext), the weights growing with
   size. Z_0(q) ≤ 1 is also not established: the sum runs over all polymers.
2. **"Free hops do not inflate polymers" is false on the code.** `checks/bdl-metacheck/free_hop_merge.py`
   (`FREE-HOP-MERGE.json`) runs the full-history representation on the 3 × 2 seed. Of 13,810
   zero-energy single flips applied to random valid syndromes, 725 increase the largest history
   polymer, 576 of them by merging components. One move takes the largest polymer from 14 to 28
   with no energy paid. Zero-energy motion therefore assembles polymers. This is exactly the
   mechanism the core lemma must control, so it cannot be dropped as "≤ 0".
3. **The calculus does not apply.** d/dt P_t(Γ | ext) is not Σ L P_t(Γ | ext): conditioning on the
   exterior does not commute with the dynamics, because the exterior also evolves. The
   μ_dissip ln(1/q) term is introduced without derivation.

**What this sharpens.** Any proof of preservation must bound merging by free motion. One candidate
quantity is the rate at which zero-energy hops join two polymers, weighted by their sizes. Bounding
it requires that the encounter rate of free-wandering defects with other polymers be small, which
depends on defect density inside the macroscopic hop components. That density is the residual
fault density, not e^{−β}. This interplay is the precise mathematical content still open.

## Lemma D (validity depends only on component parities) — proved

Let d be any dependency among the Z-checks, so that Σ_k d_k (row k of D1) = 0. Then every qubit
column meets d in an even number of checks.
- For a weight-2 qubit with δq = {k, k′}, either both k and k′ lie in d or neither does. So d is a
  union of whole hop components.
- For a weight-1 qubit (a sink) with δq = {k}, the check k is not in d. So no dependency meets a
  component that has a sink.

Hence a fine syndrome s is valid iff the parity vector P(s) of its sink-free components satisfies
the dependencies. ∎

**Consequence for the thermal law.** The energy is Σ_components |s ∩ component|. Since validity
depends only on P(s), the thermal law conditioned on the parity pattern is a *product over
components* of independent single-component gases, each with fixed parity:

    π(· | P = P₀) = ⊗_components π_C(· | parity_C = P₀(C)).

## The pattern route to (R): a candidate proof plan, not a proof

Let K_n be the number of sink-free hop components. It was 62 at both levels 1 and 2, out of 90
components in all; level 3 is still being computed.

1. **Pattern level.** The parity pattern takes at most 2^{K_n} values. If every valid pattern has
   π(P₀) ≥ c^{K_n}, then any law on patterns is at most c^{−K_n} times π's pattern marginal. The
   Chesi/G.21 holding bound tolerates C = e^{γ K_n} provided γ K_n < c n^{η}. So this step needs
   only K_n = o(n^{η}), and K_n is constant at the levels computed.
2. **Inside a component.** For a fixed pattern, the weight-2 (free) moves act independently on
   each component and are reversible with respect to π_C. Every hop cycle is a stabilizer
   (HOP-CYCLES), so the defect configuration inside a component determines the error modulo
   stabilizers. The component chain is then a non-frustrated parity system with no energy barrier
   above 2. Its relaxation from the faulted density to π_C should be polynomial; this is the
   statement to prove, a far simpler one than (R).
3. **Coupling.** Weight-3 and weight-4 flips move parity between components, some downhill at rate
   Θ(1). A proof must show that they do not obstruct step 2, for example by a two-time-scale
   argument, or by including them in the component chain together with the pattern.
4. **Logical safety during relaxation.** Inside components this is covered by the path-independence
   lemma. Across components it reduces to the coarse decoding of the fault set, below threshold.

If steps 1–4 hold, then after a polynomial relaxation the faulted state is ε-close to a law at most
C π with C = e^{O(K_n)}. That is a warm start, and (R) follows through N2, G.21 and Lemma T.

Open in this plan: the growth of K_n with level, the mixing time in step 2, and the coupling in
step 3. All three are concrete and can be tested on the constructed code.

## Disposition: pasted Steps 2–3 (intra-region spectral gap; Duhamel coupling)

Not adopted. The paste reads "K small" as "regions bounded"; the opposite is the case.

**Step 2: "region size bounded ⇒ gap uniformly positive" is false.**
- K, the number of regions, is small. The regions themselves grow with the code: the largest has
  4 checks at level 1 and 72 at level 2, about 18-fold per level.
- The finite-chain spectral gap is therefore not uniform in n.
- Its TV prefactor √(max π_k / min π_k) is exponential in the region size.
- What step 2 actually needs is a mixing-time bound polynomial in the region size, for a region
  chain with free hops, downhill pair annihilation and uphill pair creation at about e^{−2β}.
  That is unproved.

**Step 3: the coupling is not small, and the bound is not usable.**
- Coupling across regions is not O(e^{−β} + p). Flips of weight 3 and 4 include downhill moves at
  rate Θ(1): 1,648 of the 2,256 level-2 checks lie on such a qubit (HOP-CYCLES escape histogram).
- p plays no part during holding.
- The Duhamel error term is extensive: summed over all n sites, the perturbation's total mass is
  of order εMn, so εMn/λ ≫ 1.
- Π = ⊗π_k is not the stationary law of the coupled dynamics.
- Even O(ε/λ) total-variation closeness would be far too coarse. The holding bound needs a
  remainder at most the stage budget ε/2^{j+2}.

The plan's steps 2 and 3 therefore remain open, exactly as stated above.

## Disposition: pasted Lemma 2 (finite-time thermalisation) and Lemma 3 (parity hypercube)

Neither is adopted. Both contradict facts already computed on the code.

- **Lemma 2.**
  - Not every in-region move has ΔH = 0. A weight-2 flip on two empty checks creates a pair (+2),
    and one on two occupied checks annihilates a pair (−2).
  - π_k(· | p_k) weights configurations by e^{−β|s|}; it is not uniform.
  - No non-trivial finite Markov chain reaches its stationary law exactly at a finite time.
  - Path independence concerns the logical class, not mixing.
  - D_k grows with the region: the largest region has 4 checks at level 1 and 72 at level 2.
- **Lemma 3.**
  - It repeats λ_jump = O(e^{−β} + p) and τ_intra = O(1), both refuted above: downhill
    cross-region flips occur at rate Θ(1) on 1,648 of 2,256 level-2 checks, and regions grow.
  - The parity vector alone is not a Markov chain: its jump rates depend on the fine configuration.

**Hard constraints for any further attempt** (all computed; see HOP-ORBITS, HOP-CYCLES and
FREE-HOP-MERGE):

1. Regions are few (62 sink-free at levels 1 and 2) but grow about 18-fold per level.
2. Cross-region downhill flips occur at rate Θ(1).
3. In-region dynamics includes pair creation (+2) and annihilation (−2). The target law is
   e^{−β|s|} with fixed parity.
4. The required output is closeness to C·π, with a remainder at most the stage budget
   ε/2^{j+2}.
5. Free hops merge history polymers: one move took the largest polymer from 14 to 28.

## Disposition: pasted "path-space cluster expansion" with a bridge activity

Not adopted.

1. **It charges free bridges.** It puts e^{−2βm} on each bridge of size m. But the merging bridge
   in constraint 5 is made of zero-energy hops (FREE-HOP-MERGE: 14 → 28 with ΔH = 0), so its
   energy factor is 1. Free hops pay no e^{−2β}. Removing the factor leaves the base 18^k·B·Θ(1)·q,
   which exceeds 1 at high levels.
2. **Its own conclusion is an n-dependent temperature.** It requires β > ½ ln(18^k B Θ(1) q), so β
   must grow linearly in the level k, that is like log n. The device temperature would then have to
   fall like 1/log n as the code grows. This is not a fixed device inequality; it is the escape
   already ruled out above. Adopting it would add a condition the target does not permit.
3. **It assumes what it proves.** It defines the polymer weight as w(Γ) = q^{|Γ|}, which is the
   claim, and asserts the composition rule w(Γ₁ ∪ Δ ∪ Γ₂) ≤ w(Γ₁) w(Γ₂) ψ(Δ) for path-space
   polymers without derivation.

It is, however, the first attempt to name the quantity that must be controlled. That quantity is
the entropy of zero-energy bridges, about 18^k per level, against what suppresses them. With free
bridges, suppression cannot come from energy. It must come from the rarity of the defects that do
the bridging: the residual fault density inside a region, and its decay by pair annihilation. This
is the same mechanism as before, now isolated.

## CORRECTION (26 October, late): free-movement regions are bounded; their number grows

The level-3 computation, run with `checks/bdl-metacheck/fastbuild.py` (verified identical to bdl.py
at level 2), gives:

| Level | Step | Z-checks | Components | Largest component | Sink-free components |
|---|---|---|---|---|---|
| 1 | R_X | 136 | 90 | 4 | 62 |
| 2 | R_Z | 2,256 | 90 | 72 | 62 |
| 3 | R_X | 94,560 | 56,552 | 4 | 55,032 |

The earlier statements in this note that the regions "grow about 18-fold per level" and are
"macroscopic" are **wrong**. Levels 1 and 2 were read as consecutive growth, but they are an R_X
level followed by an R_Z level.
- R_Z merges each R_X component into a block. The largest component goes from 4 to 72, while the
  number of components is unchanged.
- The next R_X breaks the code back into components of size at most 4.

So components are bounded uniformly in level for this seed: at most 4 at R_X levels and at most 72
at R_Z levels, the latter predicted for level 4, which is not computed. Their number K_n grows
linearly with n.

Consequences, replacing the affected statements above:
- **Constraint 1** of the hard-constraint list is withdrawn. Regions are bounded (about 72), not
  growing. The pasted Lemma 2 and Step 2 claims of a uniform intra-region gap are therefore right in
  their conclusion: each region is a finite reversible chain of bounded size, so it has a gap
  bounded below independently of n, depending on β. Their stated proofs still contained the other
  errors recorded.
- **Free merging is local.** A zero-energy bridge lies inside one bounded region, so the 14 → 28
  merge has bounded range. The bridge entropy is bounded per region, not 18^k.
- **The pattern route's step 1 fails.** The factor 2^{K_n} is exponential in n.
- **The (R1) and Lemma D results are unaffected.**

## Revised picture and route (a candidate, not a proof)

1. **Fine level.** Free motion is confined to regions of bounded size; each region is a finite
   reversible chain with an n-independent gap. Leftover charges, one per odd region, are trapped
   in bounded regions. They leave only by flips of weight ≥ 3: uphill at rate about e^{−β}, or
   downhill when neighbouring regions are occupied.
2. **Local relaxation.** With bounded ranges and rates, the fine-level excess relaxes on an
   n-independent time scale. Global total-variation closeness ε then needs time O(log(n/ε)),
   provided spatial correlations decay. This is the BGL-type within-sector statement at the fine
   level.
3. **Coarse levels.** A fault layer of density p creates level-i coarse excitations at density
   about (c p)^{2^i}, while the thermal law has about e^{−β 2^i}. If c p < e^{−β}, a *fixed*
   device inequality, the faulted state is colder than thermal at every coarse level. No coarse
   relaxation, which is where the energetic bottlenecks lie, is then needed.
4. **The remaining core.** Being colder at coarse levels does not imply safety, because the
   dynamics lacks monotonicity. This is exactly BGL's open "ground-state stability" question, now
   for BDL with bounded fine regions. That bounded-region structure is new and is the handle a
   proof can use.

### Scaling probe, levels 2 and 3 (not a proof)

Run with `HEALING-PROBE-SCALING.jsonl` at β = 8, p = 0.02 and PYTHONHASHSEED = 0, starting from a
fault layer. Excitations per 1,000 checks every 10 sweeps:

| Level | Qubits | 0 | 10 | 20 | 30 | 40 |
|---|---|---|---|---|---|---|
| 2 (R_Z, regions ≤ 72) | 5,116 | 94.0 | 17.7 | 12.4 | 9.8 | 8.0 |
| 3 (R_X, regions ≤ 4) | 144,760 | 80.3 | 1.95 | 1.05 | 1.02 | 1.02 |

The larger code relaxes faster, because its regions are smaller. This is consistent with local,
n-independent relaxation (route step 2). The level-3 plateau of about 1 per 1,000 is the trapped
odd-parity residue in bounded regions; it can leave only by activated flips (rate about e^{−β} per
attempt). Route step 3 asks that this residue's coarse content be colder than thermal, and route
step 4, the open core, asks that this does not lead to logical failure despite non-monotonicity.

`fastbuild.py` note: an early version keyed its square-index cache by `id(T)`, which Python can
reuse. It now keys by object identity. Under PYTHONHASHSEED = 0 it gives exactly the hashes of
bdl.py at levels 1 and 2; the level-3 comparison is running. The level-3 component counts were
recomputed with the fixed builder and are unchanged.

## Lemma G (uniform gap of an isolated region) — proved; adopted from the pasted Step 1, corrected

Freeze every check outside a hop component R, and allow only the weight-2 flips inside R. These are
free hops, pair creation (+2) and pair annihilation (−2), with heat-bath rates. The resulting chain
on R's defect configurations of fixed parity is irreducible: the edges of a connected graph
generate every even change of its vertex set. It is reversible with respect to π_R(· | parity),
with π_R ∝ e^{−β|s|} (not e^{−2β·pairs}, as the paste had it).

The components have bounded size (at most 72) and bounded degree, so there are finitely many
isomorphism types. Hence its spectral gap λ_R ≥ λ₀(β) > 0, uniformly in n and level. The constant
may be as small as e^{−O(72β)}, but it does not depend on n. ∎

What Lemma G does not give: the real dynamics also contains flips of weight 3 and 4 between regions,
some downhill at rate Θ(1). A product-of-regions quasi-stationary picture is therefore not implied.
Any error term of the form t·e^{−2β} per region is extensive, about K_n·t·e^{−2β} in total.

## Disposition of the rest of this batch

- **Firebreak and contour proposals.** Domination by Bernoulli variables at the coarse density is
  asserted, not derived. A later paste in the same batch correctly notes that contour sums ignore
  free bridges.
- **Trapped-charge Step 2.** "ΔH_barrier ≥ 2 for escape" contradicts the computed escape costs:
  +1 for 1,520 of 2,256 level-2 checks, and downhill cross-region flips at rate Θ(1). Its
  quasi-stationary error is extensive.
- **"Kinetic starvation".** This is the mean-field rate equation again (dispositions above).
- **BCRD boundary-projection lemma.** Not adopted, for three reasons.
  1. The holding dynamics is a classical Markov chain on syndromes, the Davies Pauli dynamics.
     The lemma's Hilbert-space factorisation H_bulk ⊗ H_∂ and "relational low-pass filter" are not
     properties of that chain, and nothing in the UPT's BCRD axioms implies them for BDL's code.
  2. The bound ‖O_∂ χ‖ ≤ (|∂R|/|R|) e^{−βΔH} ‖χ‖ has no meaning as stated. A restriction or
     projection has operator norm 0 or 1, and a Boltzmann factor is not part of an operator norm.
  3. It uses ΔH_boundary ≥ 2, contradicted as above. It also conflates R_X-level region size (at
     most 4) with the boundary of R_Z-level regions.

BCRD's legitimate role, raised by the author earlier, concerns *which relations constitute a
particular's identity*. That bears on the target, not on the proof of (R). Changing the target
on that basis is the author's decision under the standing rules, and nothing here does so.
