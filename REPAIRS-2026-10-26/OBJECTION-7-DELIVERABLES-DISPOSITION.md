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
