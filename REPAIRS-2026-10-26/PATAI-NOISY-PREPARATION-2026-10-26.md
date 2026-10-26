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
