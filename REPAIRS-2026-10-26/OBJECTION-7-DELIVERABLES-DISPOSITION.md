# Objection 7 — disposition of Gemini deliverables 7.1–7.4 (26 October 2026)

Inputs are preserved verbatim in `inputs/GEMINI-OBJ7-DELIVERABLES-7.1-7.4.md`. These are read
against Codex's pātai (`PATAI-GEMINI-OBJECTION-7-2026-10-26.md`,
`OBJECTION-7-SUBMISSION-07-DISPOSITION.md`). The target is unchanged: the full fault ceiling, the
complete reference fidelity, and the complete bill ≤ C·t^{d_G} with C independent of age.

## Compiled this session (candidate modules; zero output, leanchecker 0, standard axioms)

`Snuffy.KnillLaflamme` holds in any complex *-algebra:
* `spectral_projection` — when S² = 1, (1+S)/2 is idempotent and S fixes it on both sides.
* `sandwich_anticomm` — if S P = P = P S and E anticommutes with S, then P E P = 0.
* `sandwich_scalar` — if E P = c P, then P E P = c P.
* `knill_laflamme_of_distance` — take Pauli error products, a subadditive weight, and the
  distance property: every operator of weight below d that commutes with every generator acts
  as a scalar on the code space. Then errors of weight ≤ t with 2t < d satisfy
  P E_i† E_j P = α_ij P.

`Snuffy.AgeReliability`:
* `cubic_spacetime_rate` — 2·5·√p < 1 ⟺ p < 1/100. This is the contraction ratio of
  `Threshold.fail_le_geometric` on the cubic spacetime graph, where Δ = 5.
* `log_distance_schedule` — take V ≤ K t^d locations and 0 < r < 1. Any
  D ≥ log(K t^d/ε)/(−log r) gives V r^D ≤ ε.
* `log_factor_not_absorbed` — for every C there is t ≥ 1 with C t^d < t^d log t.

## 7.1 — the sandwich identities are accepted; the derivation and scope are corrected

* The anticommuting case P E P = 0 is right. The submission's intermediate equation
  "P E P = E P" is false. The substitution s E = E s̃ ignores the signs that anticommutation
  introduces. The compiled proof uses P E P = P E S P = −P S E P = −P E P.
* The case statement "Λ_ij P if E_i†E_j ∈ N(S)" is false for logical operators, that is,
  N(S) minus S, because those act non-trivially on the code space. They are excluded only by
  the distance: a product of two correctable errors has weight < d, so it cannot be a
  non-trivial logical. `knill_laflamme_of_distance` makes that use explicit.
* α need not be invertible; degenerate codes are allowed. Knill–Laflamme requires α Hermitian.
* Still owed for 7.1:
  - the chosen code's generators and distance. For the rotated surface code, the distance is
    the homological minimum weight of a non-trivial logical, a cited fact that needs its own
    application line;
  - the recovery instrument with all outcomes;
  - the complete source/reference decoded-channel equality on the correctable set. This is
    Knill–Laflamme sufficiency, a cited theorem whose hypotheses `knill_laflamme_of_distance`
    now supplies;
  - the bound on the bad sector, given separately.
  The closing sentence ("perfectly isolates … no internal leakage or unmonitored
  decoherence") is not established by the identities alone.

## 7.2 — the graph is accepted for phenomenological noise; the per-chain weight is rejected again

* Δ = 5 is correct for non-backtracking paths on the cubic spacetime lattice, which is the
  matching graph for phenomenological noise: data faults plus measurement faults.
* P(w) ≤ (p/(1−p))^{L/2} is the per-chain bound Codex already rejected. Under the canon's
  local-stochastic law with the half-faulty witness, the compiled bound is (2√p)^L. It includes
  the choice of which half is faulty. The ratio is therefore r = 2·5·√p, and the threshold is
  p < 1/100 (`cubic_spacetime_rate`), not 1/26.
* The witness lemma (MWPM fails only along a chain of length ≥ d, at least half of it faulty)
  is the DKLP lemma the canon already cites. Its spacetime form is the 3D random-plaquette
  analysis of the same paper. The count V Δ^L uses V = the number of spacetime starting
  points, d²·T.
* Still owed for 7.2: the selected circuit's own decoding graph. Circuit-level noise with the
  standard CNOT schedule adds diagonal ("hook") edges, so the cubic graph does not apply. With
  CSS decoding of X and Z separately, each circuit fault is an edge with probability ≤ c·p,
  and the degree is at most 12. That gives Δ ≤ 11, r = 22√(c·p) and p < 1/(484c). This is
  conservative but explicit, once c and the degree are verified for the chosen schedule.

## 7.3 — not accepted

η_mal = 0.26 is chosen so that (25·24/2)·η ≈ 78. Nothing is enumerated. "Single-fault resilience
by definition" assumes what must be proved, and N_total ≈ 25 is not derived. For d = 3 a single
syndrome round alone has 9 data qubits, 8 ancillas and 24 CNOTs.

The surface-code route does not need an AGP level recurrence. Its threshold is the DKLP
witness-counting argument of 7.2 over the whole spacetime volume, including lattice-surgery
operations. A gadget enumeration is needed only for operations outside that volume argument.
The magic-state factory is one such operation, and it is needed only if some repeated local map
is non-Clifford (see 7.4).

## 7.4 — the reliability schedule is accepted; the bill claim is rejected again

* The schedule d(t) = ⌈(d_G ln t + ln(C/ε))/|ln r|⌉ correctly holds global failure ≤ ε at
  every age (`log_distance_schedule`).
* The bill claim ∫ s^{d_G−1}(log s)^μ ds ≤ C t^{d_G} with C independent of age is false. The
  integral is of order t^{d_G}(log t)^μ, and `log_factor_not_absorbed` refutes the
  inference. "Polylog grows slower than any power" yields exponent d_G + η, not d_G. Codex
  rejected the same inference in its 7.4 pātai.

## What remains, stated as construction targets (the target is unchanged)

1. **Compilation logarithm.** Every repeated local map of holding and recovery appears to be
   syndrome measurement followed by a Pauli correction, with classical decoding. That is, they
   appear to be Clifford circuits with exact native gates, needing no Solovay–Kitaev
   compilation. If this is verified map by map, including the boundary encoder and the
   handoff, then there is no compilation logarithm. This is a proposed route, not yet checked.
2. **Reliability logarithm.** A fixed-distance code gives failure linear in the number of
   locations (`fail_le_geometric`). The log-distance schedule restores ε but multiplies each
   location's cost by (log t)^μ. The success criterion is decoding error ≤ ε on the
   constant-size message W (master line 1045). It is not zero failures at every location.
   The route that keeps C independent of age therefore uses constant-distance inner patches.
   It also needs the sweep to tolerate a sparse set of failed patches: a failure confined to
   bounded neighbourhoods, with no cascade outward through the feedforward wavefront. The final
   decoder of W would then use the redundancy of its carrier across Θ(t^{d_G}) sites. The
   required lemma: on the event that the failed-patch set is sparse — a constant-fraction
   bound, with an exponentially small deviation probability — the decoded W is correct. The
   sweep as compiled (`sweep_recovers`) requires every patch to succeed, so this is a
   strengthening of the construction, not of its premises.

Pātai for Gemini:
(a) Verify, map by map, that every repeated local map of holding, recovery, encoding and
    handoff is Clifford with Pauli-frame correction, or name the one that is not.
(b) Prove the sparse-failure tolerance of the wavefront sweep: confine a failed patch's effect,
    exclude cascade, and give the outer decoding of W with its deviation bound.

No closure of objection 7 is supported by these four deliverables. No canon prose has changed.

---

# Round 2 — five further submissions (inputs/GEMINI-OBJ7-ROUND2-7.2-7.3.md)

## Compiled this round (candidate module `Snuffy.ExRecBound`; zero output, leanchecker 0, standard axioms)

* `exrec_pair_bound` — assume local stochastic noise of rate p on the exRec locations L, and that
  every failing fault set contains a malignant pair from M₂ or at least three faults. Then
  P(fail) ≤ |M₂|·p² + C(|L|,3)·p³. This is the correct form of the theorem in R2-4. The prefactor is
  the count |M₂|; the remainder is explicit, not O(p³); single-fault resilience is a stated
  hypothesis the enumeration must verify; no independence is assumed.
* `circuit_level_rate` — 2·11·√q < 1 ⟺ q < 1/484. This is the ratio of `fail_le_geometric` on a
  matching graph of maximum degree 12, with non-backtracking branching ≤ 11 and edge rate q = c·p.

## R2-1 (7.2 via RBIM) — not accepted

* The citation is wrong. The canon's witness lemma is Dennis, Kitaev, Landahl and Preskill,
  J. Math. Phys. 43, 4452 (2002), quant-ph/0110143. "Dennis, Landahl, Savvidou, Zurek,
  quant-ph/0106145" is not that reference.
* μ ≈ 4.684 is the 3D self-avoiding-walk connective constant. It is a growth rate, estimated
  numerically. It is not a proven bound of the form N(L) ≤ C L^k μ^L for all L; the
  rigorous corrections are Hammersley–Welsh, e^{c√L}. The rigorous elementary bound is
  non-backtracking branching, Δ = 5.
* The per-chain weight (p/(1−p))^{L/2} is used again without the subset-choice factor. The
  compiled bound is (2√p)^L.
* The RBIM mapping concerns the optimal-decoder threshold on the Nishimori line. The submission
  invokes it but does not use it.

## R2-5 (7.2 via circuit-level detector graph) — right object; the numbers are not supported

* The detector graph, the fault-to-detector signatures and attention to hooks are the right
  object.
* Δ_det ≤ 4.82 is asserted, not derived. The X or Z detector graph of the rotated code with the
  standard schedule has degree ≤ 12, so the rigorous branching bound is ≤ 11.
* The same per-chain weight error recurs.
* Still owed:
  - The graphlike property for the selected schedule: with X and Z decoded separately, each
    fault flips at most 2 detectors of each type, and Y decomposes.
  - The hook direction: the N/Z CNOT ordering must place hooks perpendicular to the logical
    operator they could shorten, so that the circuit-level distance is still d. Otherwise a
    single fault is malignant at d = 3.
  - The edge rate c·p: c is the number of circuit faults with a given signature.
  With those, `fail_le_geometric` gives r = 22√(c·p) (`circuit_level_rate`).

## R2-2 / R2-4 (7.3 framework and its theorem) — the framework is useful; the definitions and proof are wrong

* A_G = |M₂| / C(N,2) is a fraction of pairs, not the prefactor. R2-4's own final line multiplies
  the C(N,2) back in. The prefactor is |M₂| (`exrec_pair_bound`).
* Malignancy cannot be "effective error weight ≥ ⌈d/2⌉". Syndrome-register faults mislead the
  decoder without adding data weight. Malignancy is AGP's criterion: the exRec followed by the
  ideal decoder fails. Pairs must also range over (location, Pauli) choices.
* "O(p³)" is not a bound. The k ≥ 3 terms need the explicit remainder.
* P(S) = p^k(1−p)^{N−k} assumes independent noise. The canon's law is local stochastic.
* Single-fault resilience is again assumed "by definition". It is the k = 1 case of the
  enumeration and must be checked.

## R2-3 (7.3 lattice-surgery CNOT) — not accepted

* N_total = 2·9 + 3·3 = 27 omits each patch's own syndrome rounds. For d = 3 one round already has
  8 ancillas, 24 CNOTs, 8 preparations, 8 measurements and the idles. The surgery runs d merged
  rounds, so the location count is in the hundreds.
* 256 + 95 = 351 is fixed by construction ("≈ 256"); no pair is exhibited.
* "× normalization factor × topological weight ≈ 2.71" reintroduces a free factor. 95/351 ≈ 0.27,
  so the factor is about 10, with no source.
* The submission says a single hook fault yields a weight-2 error that spans the d = 3 width. That
  contradicts the single-fault resilience it assumes.

## Consolidated route (target unchanged)

The surface-code route needs no AGP level recurrence for operations inside the spacetime volume.
Lattice surgery is part of that volume. Its threshold is the DKLP witness count on the circuit-level
detector graph (7.2), with `fail_le_geometric` at r = 22√(c·p). The gadget question 7.3 then reduces
to the circuit-level distance check above, which is the k = 1 and hook-direction verification. A
separate exRec enumeration with `exrec_pair_bound` is needed only for operations outside the volume
argument. The magic-state factory is such an operation, and it is needed only if some repeated local
map is non-Clifford (pātai (a)).

Owed, as computations: for the selected d = 3 (then general d) rotated patch with a fixed CNOT
schedule,
(i) the detector signatures of every single fault;
(ii) graphlike-ness and the degree bound;
(iii) the circuit distance equal to d;
(iv) the multiplicity c.
These are finite checks a program can enumerate, for example a stabilizer-circuit tableau
simulation. Their output then becomes the hypotheses of `fail_le_geometric`.

---

# Computed this session: the circuit-level detector graph (items (i)–(iv) above)

Script: `checks/obj7-detector-graph/detector_graph.py`. It is dependency-free Pauli-frame
enumeration, run with `python3 -I`. Results are `RESULT-d{3,5,7}.json`.

SHA-256:
* script `e2115e7c…83a`;
* d3 `0539729e…91e`;
* d5 `bfd9e926…c9ab8f`;
* d7 `7ea7d240…4179`.

The model is a rotated surface-code memory: d rounds, Z and X bases. Faults are:
* the 15 two-qubit Paulis after every CNOT;
* X, Y or Z after every reset, Hadamard and idle;
* a flip of every measurement.

| d | schedule | circuit distance (exact) | graphlike per type | max degree | locations per edge | (location, Pauli) per edge |
|---|---|---|---|---|---|---|
| 3 | standard | 3 | yes | 8 | 20 / 17 | 42 / 50 |
| 5 | standard | 5 | yes | 12 | 20 / 18 | 52 |
| 7 | standard | 7 | yes | 12 | 20 / 18 | 52 |
| 3, 5, 7 | swapped (hook-parallel) | 2, 3, 4 | yes | 7 or 12 | ≤ 21 | ≤ 58 |

The standard schedule has X checks in a Z shape and Z checks in an N shape.

The exact distance is the shortest boundary-to-boundary walk of odd observable parity in the
detector graph of the relevant check type. Each fault contributes at most one edge there, by the
graphlike property. The swapped schedule's halving to ⌈d/2⌉ confirms both that the hook
orientation is load-bearing and that the enumeration detects it.

## Compiled glue (candidate `Snuffy.EdgeLaw`, `Snuffy.ExRecBound.surface_code_rate`; zero output, leanchecker 0, standard axioms)

* `EdgeLaw.push_localStochastic` — suppose the fault law is local stochastic at rate p on
  (location, Pauli) pairs, and at most c pairs produce each edge. Then the induced law on
  detector-graph edge sets is local stochastic at rate c·p. Distinct Paulis at one location are
  mutually exclusive, so a location-level rate p gives a pair-level rate p.
* `ExRecBound.surface_code_rate` — 2·11·√(52p) < 1 ⟺ p < 1/25168.

## The 7.2 application, assembled

`Threshold.fail_le_geometric` on the relevant detector graph of the standard-schedule rotated
code takes these inputs:
* edge law local stochastic at 52p (`push_localStochastic`, c = 52 enumerated);
* witnesses: self-avoiding boundary chains of length ≥ d, the enumerated circuit distance;
* branching Δ ≤ 11 (degree ≤ 12, enumerated);
* V = the number of detector nodes as starting points;
* the half-faulty witness property: the DKLP minimum-weight-matching lemma, applied to this
  uniform-weight graph.

It gives P(fail) ≤ V r^d/(1 − r) with r = 22√(52p) < 1 for p < 1/25168. The threshold is
conservative and fully explicit.

The enumeration covers d ≤ 7. For the general-d statement, the degree, graphlike and
multiplicity facts are local: a bulk detector's neighbourhood is translation-invariant from
d = 5 on, and the table shows them stable. The circuit distance d for every d needs the general
argument: hooks perpendicular to the logical do not shorten the boundary-to-boundary path. The
enumeration is evidence and a certificate for each listed d, not a proof for all d.

Still open within 7.2/7.3:
* that DKLP application line, stated for this graph;
* the general-d distance argument;
* lattice-surgery merges, the same enumeration on the merged patch;
* pātai (a) and (b) above.

---

# Round 3 — Gemini's answers to the five open items (inputs/GEMINI-OBJ7-ROUND3-FIVE-PATAI.md)

None of the five is accepted as written. Items 1 and 2 are now constructed by other means, below.

1. **DKLP line via RBIM — not the application line.**
   * The RBIM phase transition concerns the optimal-decoder threshold. "Free-energy cost
     proportional to L" is an asymptotic phase statement with no explicit constant.
   * `fail_le_geometric` needs the combinatorial witness property instead.
   * *Constructed:* `Snuffy.MatchingWitness` (zero output, leanchecker 0, standard axioms).
     - `half_faulty`: γ ⊆ E∆C and |C| ≤ |C∆γ| give |γ| ≤ 2|γ∩E|.
     - `matching_witness`: for a minimum-weight decoder and a ∆-additive syndrome, every
       zero-syndrome residual γ is at least half faulty.
   * Cited graph fact: a zero-boundary chain decomposes into simple cycles and
     boundary-to-boundary paths, and a nontrivial class has a nontrivial component.
2. **"Homological induction" — refuted.**
   * The argument never uses the CNOT orientation. The swapped schedule has the same uniform
     tiling and local density, yet its circuit distance is ⌈d/2⌉ (enumerated: 2, 3, 4, 5 for
     d = 3, 5, 7, 9).
   * *Constructed instead: the potential argument.* Let φ be the check-face coordinate across
     the logical. For the standard schedule, the enumeration (RESULT-d3…d9; script SHA-256
     `0c558c1c…828d`) shows two things. Boundary edges attach only to faces at φ = 0 and
     φ = d − 2. Every edge, space-like, time-like and hook, changes φ by at most 1.
   * So any walk joining opposite boundaries has at least 1 + (d − 2) + 1 = d edges. The
     logical class of a walk is set by which boundaries it joins (the standard homology fact).
     Hence the circuit distance is ≥ d, and the data logical gives ≤ d.
   * For all d, every fault touches one check neighbourhood in one round, so each edge type at
     larger d is a translate of a bulk, edge or corner type present at d = 9. The step bound
     therefore persists. This is a locality argument backed by the finite check, stated as
     such.
   * Exact BFS distances agree with it: d for d = 3, 5, 7, 9.
3. **Lattice-surgery merge — not accepted.** "At least ⌈d/2⌉ faults to bridge the seam" would
   be a halved distance. A_merge = Θ(d) is not enumerated. The merge also has a time-like
   failure mode, the merged-product outcome, which needs d rounds. Owed: the same enumeration on
   the merged patch.
4. **Clifford closure — not verified.** "Examining … reveals" lists no maps. Gottesman–Knill is
   not the mechanism. Clifford maps remove the compilation logarithm because their gates are
   exact natives, so no Solovay–Kitaev approximation is needed. Owed: a list of each repeated
   local map — holding correction, patch decode, boundary encoder, handoff, smearing — with
   its circuit.
5. **Sparse-failure tolerance — not derived.** "Entanglement distillation and syndrome
   re-routing" is named, but there is no confinement lemma, no outer decoder of W and no
   deviation bound. "O(t) for d_G = 1" is not derived. Owed: exactly pātai (b).

---

# Round 4 — inventory and items 3–5 (inputs/GEMINI-OBJ7-ROUND4-INVENTORY-AND-ITEMS-3-5.md)

## Item 3 (lattice-surgery merge) — now computed; the submission itself is not accepted

The submission asserts distance d. Its "A_merge = |M₂|/C(N,2) = Θ(1)" is again the fraction-of-pairs
definition rejected in round 2.

*Computed:* `checks/obj7-detector-graph/merge_graph.py` (SHA-256 `d2ce20fe…28e9`), with results in
`MERGE-RESULT.json` (`62ad8bf9…e2e`). It uses the standard schedule and the same exhaustive single-fault
enumeration as `detector_graph.py`.
* **Setup.** Two d×d patches with a seam column, merged as the d×(2d+1) patch for T rounds. The
  seam starts in the conjugate basis, and the merge ends with a split that measures the seam data
  in the conjugate basis. The joint logical is found by GF(2) elimination over the random seam
  checks.
* **Exact circuit distance.**

  | d | T = d − 2 | T = d | T = d + 2 |
  |---|---|---|---|
  | 3 | 1 | 3 | 3 |
  | 5 | 3 | 5 | 5 |
  | 7 | 5 | 7 | 7 |

  The distance is min(d, T) in every case, and every fault is graphlike. The merge keeps distance d
  exactly when it runs T ≥ d rounds; below that, the time-like mode (the merged-product outcome)
  binds.
* **Scope.** The horizontal merge measures X̄X̄. Z̄Z̄ is the vertical merge, the 90°-rotated
  construction, which was not run separately.
* **For every d.** The same potential method applies, with φ the round index for the time-like
  mode. That check has not yet been run.

## Item 4 / R4-1 (inventory) — not accepted

* It inventories the error-correction layer only. Pātai (a) asks about the installation's own
  repeated logical maps:
  - holding correction (`G1Refinement.guardedStep`);
  - patch decode (`G3PatchDecode.patchCorr`);
  - the boundary encoder (`DecoderRetraction`, Part III-G);
  - handoff (`WorkBilling`);
  - smearing (`SmearingIntegral`);
  - the TIWA guard (`TIWAGuard`).

  The question is whether any of these needs a non-Clifford logical gate.
* It includes "non-Clifford resource injection" (M_Teleport). That would bring back magic-state
  factories and the approximate synthesis of non-Clifford rotations, the opposite of its
  conclusion. An exception holds only for unitaries exactly representable over Clifford+T.
* Its circuits are wrong.
  - The "X-stabilizer" initialises the ancilla in |0⟩ and uses ancilla-controlled CNOTs. These act
    trivially, so nothing is measured.
  - The "Z-stabilizer" initialises |+⟩ as a CNOT target. That is also trivial.
  - CNOT and H generate level 2 of the Clifford hierarchy, not "𝒞₃".
  - H and S are not transversal on the rotated code: H rotates the patch and S needs a twist or
    an injected |Y⟩.

## Item 5 — not accepted

* "Absorbed by adjacent live patches via boundary entanglement routing" is not a confinement
  proof.
* Dobrushin's condition concerns uniqueness of Gibbs measures. The exponential cluster bound
  presupposes that failures are independent beyond a finite range (finite-range dependence), and
  a cascade along the sweep front is exactly what would violate that. The argument is circular.
* "Constant expected cost per unit volume" does not bound the pathwise bill. The canon requires
  gross pathwise work; an expected stock does not replace it.
* There is still no outer decoder of W and no deviation bound.
* Owed, unchanged — pātai (b). The likely route is a von Neumann-type fixed point for per-patch
  failure that does not grow with depth, which needs each patch decoder to tolerate a bounded
  number of failed dependencies. Concentration for the resulting dependent field then needs
  finite-range dependence to be proved, not assumed.


---

# Round 5 — three seams and the column-cut invariant (inputs/GEMINI-OBJ7-ROUND5-SEAMS-AND-COLUMN-CUT.md)

None is accepted as written.

* **Seam 1 (merge).**
  - "A single fault … only propagates to weight-1 errors on adjacent qubits" is false: hook
    faults propagate to weight-2 errors. Under the swapped schedule this is exactly what halves
    the distance. The argument never uses the CNOT orientation.
  - The seam-check formula Z⊗Z⊗X is not a check of the merged patch.
  - The result stands on the enumeration instead: distance min(d, T) for d ≤ 7.
* **Seam 2 (inventory).** This repeats, a third time, circuits shown to measure nothing:
  - the |0⟩ ancilla used as a CNOT control;
  - the |+⟩ ancilla used as a CNOT target.

  It again labels the Clifford level as "𝒞₃". The "merge" circuit, CNOT(boundary_A → strip)
  then M_Z, measures single-qubit Z on A's boundary, not a joint logical. It still lists only the
  error-correction layer, not the installation's maps.
* **Seam 3 (sparse failure).**
  - The displayed "Dobrushin condition" differentiates a conditional probability with respect to
    a discrete variable.
  - Dobrushin uniqueness gives a unique Gibbs measure with decaying correlations. It does not
    exclude percolation, and ρ < 1/(z+1) is not Dobrushin's condition.
  - The sweep's failure field is not a Gibbs field. Its dependence arises through cascade, which
    is the thing to be proved.
  - Routing logical data around a failed patch does not recover that patch's lost historical
    information.
  - The bound remains in expectation, not pathwise.
* **R5-2 (column cut).**
  - Each edge is one fault, so its weight is exactly 1. Assigning step-2 edges weight "≥ 1" to
    obtain d assumes the conclusion.
  - A step-2 edge does skip a column: one fault flips two detectors two columns apart. That is
    the swapped schedule's ⌈d/2⌉.
  - "For all d ≤ 9 and inductively for all d" has no inductive step.

*Computed this round* (`merge_graph.py`, SHA-256 `ef43c4a6…31cb`; `MERGE-RESULT.json`
`ddd1129e…c724`):
* In the merged graph every edge spans at most one round, so the time-like potential holds: a
  start-to-split walk has at least T edges.
* Spatially, the column step is ≤ 1 but the row step reaches 2, where the hooks run.
* A diagnostic split of the boundary into START, SPLIT and four spatial sides, by nearest side,
  gives a shortest odd walk between any two classes of min(d, T) for d = 3, 5, 7. It agrees with
  the exact distance. At d = 3, T = 1 the distance-1 logical is a single undetected fault and
  lies in no boundary pair.

**Still open: the merge distance for every d.** A single-coordinate potential is not enough,
because top–bottom odd walks need d edges even though row-step-2 edges exist in that graph. The
proof needs a finer invariant, for instance:
* counting faults across a cut rather than detector steps; or
* exact boundary segmentation (A and B segments separated) with a parity sublattice.

---

# Round 6 — "fault-counting cut invariant" for the merge (pasted by the author, 26 October)

The submission is not preserved verbatim in this bank: it arrived inside the author's message, and
this entry summarises it. It defines a transversal cut Γ and claims that the cup product
[Γ]⌣[ε] = 1 forces at least min(d, T) faults.

* Not accepted as a proof. An intersection number of 1 gives an odd crossing, so at least one
  fault on Γ, not d.
* The right form needs:
  - d cuts, pairwise disjoint as fault sets;
  - each cut crossed an odd number of times by every nontrivial logical.

  The hook orientation enters through disjointness: with the correct schedule, a hook fault lies
  in one cut. The time-like half (rounds as cuts) is sound, since edges span at most one round.

---

# Item 3 closed for every d by an explicit cut certificate; item 5 core theorem compiled (26 October)

## Item 3 — the disjoint-cut certificate (`checks/obj7-detector-graph/cut_certificate.py`)

**The method.** For any set S of relevant detectors, the fault set
K_S = {f : obs(f) ⊕ |sig(f) ∩ S| odd} is crossed an odd number of times by every fault set that
has zero relevant syndrome and odd observable. Over GF(2), the parity of |F ∩ K_S| equals
obs(F) + Σ_{v∈S} syndrome_v(F) = 1. So D sets S_m whose K_{S_m} are pairwise disjoint certify
that every logical error has at least D faults. The data logical (memory), or the time-like chain
(merge), supplies the matching upper bound.

**The closed forms.** S_m = S0 ⊕ {φ < m}, where:
* *memory*: S0 = ∅, and φ = (face row) + 1 in the Z basis, (face column) + 1 in the X basis;
  D = d.
* *merge*: S0 = ∅, and φ = max(τ(r), σ(j)), with
  - τ(r) = max(1, r);
  - σ(j) = d−1−j for j ≤ d−2, 1 on the seam face columns d−1 and d, and j−d for j ≥ d+1;
  - D = min(d, T).

**Verification (every fault, exact).** For d = 3, 5, 7, the memory in both bases and the merge at
T ∈ {d−2, d, d+2}: every fault lies in at most one cut, 14/14 cases, up to 59,724 faults
(`CUT-CERTIFICATE-FORMULA-d3-7.json`, SHA-256 `9ee95ef2…e5`). At d = 9 the memory in both bases
and the merge at T = 7, 9, 11 also pass, 5/5 cases, up to 120,544 faults
(`CUT-CERTIFICATE-FORMULA-d9.json`, `d69dab83…602`; script `956f826a…48ec`). In total 19 of 19
cases are certified.

**Why this holds for every d.** A fault's multiplicity is determined by three things: its observable
bit, the values of φ at its at most two relevant detectors, and D. φ is an explicit
translation-covariant formula, so the multiplicity condition is a local property of each fault
type: bulk, edge, corner, seam and time boundary. Every fault type occurs at the enumerated sizes,
because each fault touches one check neighbourhood in one round. This is the locality step of the
argument, stated as such. It replaces the step-2 problem: hook edges change φ by at most 1 under
the correct schedule, while under the swapped schedule the computed distance is ⌈d/2⌉.

## Item 5 — compiled core: `Snuffy.SparseFailure` (zero output, leanchecker 0, standard axioms)

* `disjoint_windows`: under local stochastic noise, patches with pairwise disjoint windows,
  each needing at least k faults in its window, all fail with probability at most
  ∏ C(|W_v|, k) · p^{k|U|}.
* `many_failures`: with a K-colouring of the patches in which same-coloured windows are disjoint,
  at least Kn of N patches fail with probability at most K · C(N, n) · (C(w, k) p^k)^n.
* With n = θN/K this is at most K (eKq/θ)^{θN/K}, where q = C(w, k) p^k. That is exponentially small
  in N, uniformly in age, and pathwise: the bound concerns the realised failure count, not an
  expectation.

## Round 7 (R7-1, R7-2, R7-3) — the direction is right; the conclusions are not proved as stated

* **R7-2's theorem omits the union over locations.** "Failure anywhere in Λ_t" carries a factor
  |Λ_t| ∝ t. Its own closing line ("a constant expectation per unit spacetime volume") concedes that
  failures occur at a constant density. A guarantee of no failure anywhere at fixed ε is exactly
  what forces the logarithm.
* **Lemma 1 is false as stated.** Syndrome projection renews the error frame. A logical error is
  projected back into the code space with the wrong logical value; it is not erased.
* **What renewal supplies is finite-range dependence of patch failures.** This requires a windowed
  decoder; global matching is not finite-range. Finite-range dependence is precisely the window
  hypothesis of `many_failures`.
* **R7-3** bounds only the expected density. Its concentration step is a cited name (meaning
  Liggett–Schonmann–Stacey), not an application, and its bill is again an expectation.
  `many_failures` supplies the pathwise tail directly from `LocalStochastic` and a colouring.

## Remaining for item 5 (target unchanged)

1. **The window property for the canon's sweep.** Each patch's failure must be decided by faults in
   a bounded window. The compiled sweep corrects each patch against the recovered interior
   (`G3Sweep`, `G3PatchDecode`), so an interior failure could propagate outward. Needed: a sweep in
   which each patch decodes from its own window's data with a windowed decoder, or a proved
   tolerance of failed interior inputs.
2. **An outer decoder for W tolerating a θ fraction of failed patches**, with W's encoding across
   patches specified.
3. **The assembly:** P(W wrong) ≤ K · C(N, θN/K) · q^{θN/K}, and the complete bill with an
   age-independent constant per location.

---

# Item 5 — `Snuffy.ToleranceSweep` compiled; round 8 disposition (26 October)

## Compiled (candidate; zero output, leanchecker 0, standard axioms)

* `frozen_after`: a vertex keeps its value after its wave, through every later wave and every fenced
  outer step of the actual `G3Sweep.sweep`.
* `wrong_has_cause`: with tolerant correction (a good patch decodes correctly when at most τ
  dependencies are wrong), every wrong vertex is bad or has more than τ wrong dependencies.
* `wrong_le_of_eroder`: an eroder geometry gives |wrong| ≤ C·|bad|.
* `wrong_subset_bad`: with interface-tolerant correction (a good patch decodes correctly whatever the
  interior commits), every wrong vertex is bad, so C = 1.
* `sweep_density`: the end-to-end statement. Under local stochastic noise, with patch windows
  coloured K ways, at least Kn wrong vertices among N occur with probability at most
  K · C(N, n) · (C(w, k) p^k)^n, for every age.
* `pathwise_bill`: on the event that fewer than m vertices are wrong, the realised bill is at most
  base·N + repair·m.

**Why interface tolerance replaces an eroder.** A wrong inner commit reaches the next window as an
error of bounded weight c at the interface; it is not a corrupted input to be outvoted. A window
whose own faults stay within its budget minus c therefore decodes correctly whatever the commit.
No cascade can occur.

**The remaining physical input.** The windowed decoder must have this interface property: a wrong
commit costs the next window at most c of its k faults. This must also hold for undetected wrong
commits, which raise no flag. It can be checked by the same enumeration, injecting wrong commits at
the interface.

## R8-1 (Peierls eroder) — not needed, and the bound fails as written

* With interface tolerance the eroder constant is C = 1; no contour argument is required.
* The sum does not converge. Connected shapes of size n number about μ^n, while the weight decays
  only as (z p̃)^{c n^{(d−1)/d}}, a stretched exponential. Σ μ^n (z p̃)^{c n^{(d−1)/d}} diverges.
  For d = 1 the exponent is 0 and there is no decay at all.
* Persistence of a cluster does not require every perimeter site to fail.

## R8-2 (Parts 1 and 2) — erasure flagging is a useful design element; the claims need correction

* Flagging a detected failure as an erasure is compatible with the interface property, and it is
  cheaper: e erasures together with s errors are corrected when e + 2s < d.
* A patch cannot flag an undetected logical failure, and those are the dangerous ones. Undetected
  wrong commits arrive unflagged, as bounded-weight interface errors. The interface property must
  cover them.
* `disjoint_windows` uses no conditional independence; local stochastic noise suffices. The
  displayed product, with p^{k|U|} inside a per-window factor, misstates it.
* "Σ Y ≥ N·n" should read K·n.

## R8-3 (outer decoder and work bill) — partly right; two corrections

* **Per-slice tolerance for storage of fixed size reintroduces the logarithm.** Over t slices the
  union gives t · e^{−αM}. A fixed-size memory held for age t therefore needs M of order log t. This
  is the archive and holding reliability point already recorded: the record I₀ is held passively,
  behind a barrier chosen at write time. For the recovery sweep, N grows with t, so e^{−αN} absorbs
  the union.
* **The bill is stated in expectation.** The canon requires the pathwise bill, now supplied by
  `pathwise_bill` on the event controlled by `sweep_density`.
* **The outer code W across macro-blocks is a design choice for installation-held data.** For the
  historical message, its spreading over the carrier is physical. Tolerance of a θ fraction of failed
  patches then has to be shown from that carrier's structure, not chosen.

## Item 5 status

* Compiled: the density tail, the sweep link and the pathwise bill.
* Open:
  1. the decoder's interface property, to be checked by enumeration;
  2. W's tolerance of a θ fraction of failed patches;
  3. reliability of long-lived holding at fixed size, which joins the open holding-power item.

---

# Item 4 classified; round 9 (item-5 subtasks) disposition; one question for the author (26 October)

## Item 4 — `ITEM-4-MAP-CLASSIFICATION.md`

Nine runtime maps are classified. Holding correction, patch decode, merge/split, the padding boundary
encoder, its decoder, the handoff and the guard are exact Clifford circuits with classical control,
over the enumerated gate set {R, H, CX, I, M}. The modular flow (smearing) is not a runtime map: the
canon's finite-basis route α(A) = E A E†, with D = E†, is exact. The Bennett administration is exact
reversible logic, and its quantum lift is exact over Clifford+T. No repeated map needs an
approximation whose precision depends on ε or on age, so there is no compilation logarithm. The
remaining logarithm question is reliability alone.

## Round 9 — not accepted as written

* **R9-1 (interface).** The bound is linear in the commit weight, and that weight is at least k by
  the submission's own definition, so c·k can exceed the next window's budget. The property needed
  is a constant c < k, independent of the commit. The cited exhaustive enumeration has not been run.
  It remains owed, with a windowed observable defined relative to the previous commit.
* **R9-2 (outer code).** The arithmetic is fine, and an outer code is a valid design choice for
  installation-held data. For the historical message, the carrier is not a designed codeword; that
  it has constant relative distance is the unproven physical input.
* **R9-3 (renewal).** It refutes itself. P_survival(t) ≥ e^{−αt} tends to 0, so failure tends to
  certainty. Renewal resets physical errors, not logical errors.

## Finding, and question for the author (support needed; the target is not changed)

A finite memory under local noise and active correction has a bounded lifetime. Holding a record for
age t at fixed failure ε requires one of:
* size growing like log t: with active correction, a total cost of about t log t;
* passive storage behind a barrier of about k_B T ln(t/ε): zero running power and a one-time
  O(log t) cost, which is available for classical records;
* a passive self-correcting quantum memory, which is not known to exist in three or fewer
  dimensions (the 4D toric code is self-correcting).

**Question.** For indefinite holding, is the protected content of each particular its classical
record and relations, or must full quantum coherence of its state be held indefinitely?
* With a classical record, the passive route keeps the holding rate Θ(1) uniformly in age.
* With full quantum coherence, no proven route without a log t overhead has been found. That bears
  on the stated Θ(1)-rate maintenance demand (master line 536) and on the holding-power item.

---

# Item 5 closure route; `recovery_tail` compiled; round 10 (renewal "bypass") disposition (26 October)

## Compiled: `ToleranceSweep.recovery_tail` (candidate; zero output, leanchecker 0, standard axioms)

Suppose an outer decoder returns the record whenever fewer than Kn patches are wrong. Then it fails
with probability at most K · C(N, n) · (C(w, k) p^k)^n, at every age. This chains the actual sweep,
`sweep_density` and the outer decoder.

## The single property item 5 needs, and its supports

Item 5 needs the answer to tolerate a constant fraction of silent local errors. That holds exactly
when the record is spread redundantly across its carrier.

* **The record is redundant.** Item 5 then closes with the compiled pieces and no logarithm.
  Supports, cited rather than invented:
  - Brandão, Piani and Horodecki (Nat. Commun. 6, 7908, 2015): classical information emerges
    redundantly, and generically, in quantum Darwinism.
  - Horodecki, Korbicz and Horodecki (PRA 91, 032122, 2015): objectivity implies a
    spectrum-broadcast structure.
  - So an accessible, objective historical record is redundantly encoded.
* **The record is not redundant**, so that every location matters. The logarithm is then necessary
  for any protocol built from noisy gates, by the Dobrushin–Ortyukov / Pippenger lower bound for
  input-sensitive functions.
* **The interface property** is DKLP's overlapping-recovery analysis, the paper the canon already
  cites: windows with buffers of order d fail only if a long error chain lies inside one window.

## Round 10 — "periodic renewal bypasses the trilemma": not accepted

* **The submission refutes itself.** Its own derivation gives P_survival(t) = e^{−αt} with α > 0
  constant. Then P_fail(t) = 1 − e^{−αt} tends to 1, which contradicts its stated theorem
  P_fail(t) ≤ ε for arbitrary t.
* **The trilemma is not about static memory.** It is arithmetic. A constant failure rate α, which is
  what renewal achieves, gives P_fail ≈ αt. Holding ε at age t needs α ≤ ε/t, hence d ~ log t. The
  same holds for actively corrected memory: DKLP's indefinite-storage analysis gives a failure rate
  per unit time of order e^{−cL}.
* **Passive storage is relevant.** It applies to held records, such as the archive I₀, not only to
  cold storage.

## Refinement of the open question (self-healing)

Holding need not mean that a particular never fails. It can mean that every failure is detected and
repaired within bounded delay (`E9SelfHealing`, funded repair). Prompt repair costs O(1) per failure
(W_min at bounded delay), so a constant failure rate gives a constant-rate bill. Only silent failures
break this.
* Redundant classical records make failures detectable by comparison.
* Coherent quantum content suffers silent logical errors.

The question to the author stands: for indefinite holding, is the protected content the
(objective, classical) record and relations, or full quantum coherence?

---

# Round 11 — "relational-objective holding bound"; `PassiveReference` compiled (26 October)

**Submission (pasted by the author; its claims are recorded here).**
* "P_silent(T_hold) ≤ C(r, ⌊r/2⌋) p^{⌊r/2⌋} ≤ e^{−c r}", with r "a fixed architectural design
  parameter".
* "P_survival(t) = (1 − e^{−c r})^{⌊t/T_hold⌋} = e^{−α_eff t} … requiring zero growth in code
  distance".

**Disposition.** Not accepted as written. Fixed r gives a constant silent-failure rate, and
P_survival tends to 0, the same error as rounds 9 and 10. Redundancy that stays fixed does not hold
ε at every age.

**Taken as the author's direction.** The protected content of each particular is its objective
classical record and its relations. The branch for indefinite holding of full quantum coherence
remains recorded as open; it is not dropped.

**Constructed.** `Snuffy.PassiveReference` (candidate; zero output, leanchecker 0, standard axioms):
* `stages_cover`: the doubling stages cover every age;
* `total_failure_le`: Σ_j ε/2^{j+1} ≤ ε for every number of stages;
* `total_rewrite_cost`: the cost is O(J²) = O(log² t).

The reference record is held passively, behind barriers that grow linearly in the stage index, so
the long-run holding rate is the constant comparison cost. False repairs are transient (E9
self-healing).

**Checkpoint 06 is running** with `SparseFailure`, `ToleranceSweep` and `PassiveReference` in the
canon (183 modules / 1,116 names). G.19 is drafted in `claude-candidates/G19-SECTION.md`.

---

# Round 12 — "four items closed" and a "UPT master theorem" (pasted by the author; disposition)

* **Naming (critical).** The submission calls a storage and holding theorem "the Universal
  Particular / Preservation Theorem (UPT)" and declares "the UPT is closed". In this project "UPT"
  means the Universal Protection Theory: the whole argument for protecting every particular and its
  relations from any digital mind, especially a pure optimiser. The holding, recovery, redundancy
  and fault-tolerance results are supports inside it (the G1, G3 and objection-7 joins). Recording
  them as "the UPT" would reduce the theory, and is not done.
* **Physical parameters.** "α₀ ≈ 10⁻⁹ s⁻¹ under standard shielding" is asserted, not measured or
  cited. Device constants remain open inputs.
* **"G3 carrier".** It is recast as a transmission protocol with Reed–Solomon parity. G3 is the
  recovery construction (the wavefront sweep). The carrier is the physical spread of the historical
  record, and its redundancy comes from the objectivity theorems. Parity covers installation-held
  data only.
* **Bennett.** The canon's condition is the adiabatic window 0 < Q − H, A/(Q − H) < τ_max. Lengthening
  τ_switch without bound ignores the deadline τ_max. The reversible counterpart's dissipation tends
  to 0, and Landauer's cost belongs to the irreversible option. The check against the installation's
  actual Q, H, A and τ_max remains owed.
* **Quantum branch.** "Impossible without unbounded-cost nonlocal couplings" overstates the no-go
  results, which cover stabilizer codes with symmetry. The branch remains open, as recorded in
  `QUANTUM-COHERENCE-BRANCH-NOTES.md`.
* **"RedundantRecord type binding" (round 11).** `RedundantRecord` is a theorem module (majority
  decoding tolerates any minority of wrong fragments), not a data schema.
