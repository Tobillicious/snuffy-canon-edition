# Item 4 — the installation's own repeated maps, classified (26 October 2026)

**Question (pātai (a)).** Does any repeated runtime map of holding, recovery, encoding, handoff,
smearing or guarding need an approximate compilation whose precision must grow with age? If none
does, there is no compilation logarithm, and the remaining logarithm question is reliability alone
(item 5). The target is unchanged.

**Gate inventory.** The syndrome-extraction, memory and lattice-surgery circuits enumerated in
`checks/obj7-detector-graph/` (`detector_graph.py`, `merge_graph.py`) use only these operations:
reset to |0⟩ (R), Hadamard (H), CNOT (CX), idle (I) and Z-basis measurement (M). Every one is
exact and native, and all are Clifford or Pauli measurement. The circuits correctly measure the
stabilizers: the enumerations certify circuit distance d, and the merge distance min(d, T).

| # | Map (canon pointer) | Physical realisation | Class | Approximation needed? |
|---|---|---|---|---|
| 1 | Holding correction, `G1Refinement.guardedStep` (writes the nearest codeword into each readout) | stabilizer syndrome extraction (R, H, CX, M), classical decoding, Pauli correction | Clifford + classical control | no |
| 2 | Patch decode, `G3PatchDecode.patchCorr` | the same circuits within a patch | Clifford + classical control | no |
| 3 | Lattice-surgery merge/split (joint measurements in handoff and recovery) | merged-patch stabilizer rounds, then split (`merge_graph.py`) | Clifford | no |
| 4 | Boundary encoder, `DecoderRetraction.coordinateBoundaryEncoder` (E_j x)_{j(a)} = x_a | with the padding injection j(x) = x‖0^{b−a}: prepare b−a ancillas in \|0⟩ | Clifford (preparation only) | no |
| 5 | Decoder D = E†, `adjoint_decodes_isometry`, `coordinate_boundary_roundtrip` | for the padding encoder: verify the ancillas in \|0⟩ (M) and discard | Clifford | no |
| 6 | Charged handoff, `WorkBilling.chargedAttempt` (move, verify, commit) | register transfer by teleportation (H, CX, M, Pauli correction) or SWAP (3 CX) | Clifford | no |
| 7 | TIWA guard installation, `TIWAGuard.installGuard` (write fence, commit) | classical access control; the boundary is committed by stabilizer measurement | classical + Clifford | no |
| 8 | Modular flow and smearing, G.3–G.4, `SmearingIntegral` (U_s = e^{isG}, s ∈ ℝ) | continuous unitary family | non-Clifford in general | **not a runtime map** (below) |
| 9 | Bennett administration, `BennettCounterpart.implementedProgram` (s,0,0) ↦ (h(g s),0,s) | reversible permutation of basis states | exact classical reversible logic (Toffoli native); quantum lift exact over Clifford+T | no Solovay–Kitaev |

**Map 8.** The smearing integral is a reconstruction identity. The canon's own finite-basis route
gives the same boundary representative exactly: α(A) = E A E†, decoded by D = E†
(`boundary_observable_on_code`, `historical_query_preserved`, `historical_flow_roundtrip`;
G.2, G.4 "at τ = 0, use the finite-basis formula directly").
* The runtime decoder of the historical algebra is therefore maps 4–5, which are exact Clifford.
* The supplied smearing construction and its compiled identity are retained unchanged, as a
  derivation, not as a required runtime map.
* If a smeared probe schedule is nevertheless implemented, each use carries a fixed compiled
  precision. Its residual is a constant-rate fault in a charged account, and `SparseFailure` and
  `ToleranceSweep` tolerate constant-rate failures. Under the tolerance model the precision
  therefore need not grow with age.

**Map 9.**
* As classical reversible logic, Toffoli is a native exact gate.
* If the quantum lift is run, Toffoli is exact over Clifford+T (seven T gates), so no
  approximation is needed. The quality of the T states is then a constant per-gate error rate, and
  it falls under the same constant-rate fault treatment as map 8.

**Conclusion.**
* No repeated runtime map needs an approximation whose precision depends on ε or on age, so there
  is no compilation logarithm.
* The approximation-free claim rests on three choices, all already in the canon:
  - the explicit padding encoder, rather than a general isometry;
  - the finite-basis decoder, rather than the continuous flow;
  - exact Toffoli for the Bennett administration.
* What remains of the logarithm question is reliability alone. That is item 5, whose open inputs
  are the decoder's interface property, W's tolerance and long-lived holding.

**What this classification does not establish.**
* That the physical device realises these gates at the stated error rates. That is the fault model
  and its charged accounts, objection 7's application certificate.
* That the classical control is itself reliable. Classical decoding and control faults belong to
  the controller account.
