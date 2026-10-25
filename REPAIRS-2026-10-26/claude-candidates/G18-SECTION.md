## G.18 Application data for the cited fault-tolerance theorems

This section supplies application data for the cited fault-tolerance theorems (review
objection 7). The full fault ceiling and the complete bill \(\le Ct^{d_G}\) with an
age-independent \(C\) are unchanged. Components are compiled or computed; the remaining joins are
named at the end.

**Knill–Laflamme from the code distance** (`KnillLaflamme`). In any complex \(*\)-algebra, the
spectral projection \((1+S)/2\) of an involution is idempotent and fixed by \(S\)
(`spectral_projection`). The code projector annihilates any operator that anticommutes with a
generator (`sandwich_anticomm`). It returns \(cP\) for an operator acting as the scalar \(c\) on
the code space (`sandwich_scalar`). Let errors have weight at most \(t\) with \(2t<d\), where
distance \(d\) means that every operator of weight below \(d\) commuting with all generators acts
as a scalar on the code space. Then \(PE_i^\dagger E_jP=\alpha_{ij}P\) for every pair
(`knill_laflamme_of_distance`). Logical operators are excluded by the distance, not by the case
split.

**The witness property of minimum-weight decoding** (`MatchingWitness`). Take a
minimum-weight decoder and a syndrome additive under symmetric difference. Every zero-syndrome
\(\gamma\subseteq E\,\triangle\,C\) of the residual is then at least half faulty:
\(|\gamma|\le2|\gamma\cap E|\) (`half_faulty`, `matching_witness`). This is the witness
hypothesis of `Threshold.fail_le_witness` and `fail_le_geometric`. The nontrivial component of
a failed residual is a simple cycle or a boundary-to-boundary path, of length at least the
circuit distance.

**The circuit-level detector graph.** A dependency-free Pauli-frame enumeration covers the
rotated surface-code memory over \(d\) rounds, with X checks in a Z-shaped CNOT order and Z
checks in an N-shaped order. The faults enumerated are the 15 two-qubit Paulis after every CNOT,
\(X\), \(Y\), \(Z\) after every reset, Hadamard and idle, and every measurement flip. For
\(d=3,5,7,9\) the enumeration gives:

- every fault flips at most two detectors of each check type;
- the maximum detector degree is 12;
- at most 52 (location, Pauli) faults produce each edge of the relevant type;
- the circuit distance is exactly \(d\).

With the orders swapped, so that hooks run parallel to the logical, the distance falls to
\(\lceil d/2\rceil\). The orientation is load-bearing.

The bound for every \(d\) uses a potential. Let \(\varphi\) be the face coordinate across the
logical. Boundary edges attach only at \(\varphi=0\) and \(\varphi=d-2\), and every edge,
time-like and hook edges included, changes \(\varphi\) by at most one. So any walk joining
opposite boundaries has at least \(d\) edges. Every fault is local to one check neighbourhood
in one round, so the edge types for larger \(d\) are translates of those enumerated. The script
and its results are banked with their hashes.

**Lattice-surgery merges.** The same enumeration was applied to the merge. Two \(d\times d\)
patches and a seam column were merged as the \(d\times(2d+1)\) patch for \(T\) rounds, with the
seam initialised and finally split in the conjugate basis. The joint logical is found by \(GF(2)\)
elimination over the random seam checks. For \(d=3,5,7\) and \(T\in\{d-2,d,d+2\}\), the circuit
distance is exactly \(\min(d,T)\) and every fault is graphlike. A merge therefore keeps distance
\(d\) exactly when it runs at least \(d\) rounds; with fewer, the time-like failure of the
merged-product outcome binds. The horizontal merge enumerated measures \(\bar X\bar X\); the
vertical merge, measuring \(\bar Z\bar Z\), is the same construction rotated and was not run
separately.

**The edge law and the explicit ratio** (`EdgeLaw`, `ExRecBound`). Suppose circuit faults are
local stochastic at rate \(p\) on (location, Pauli) pairs, and at most \(c\) of them produce
each edge. Then the induced edge law is local stochastic at rate \(cp\)
(`push_localStochastic`). With degree 12, so non-backtracking branching at most 11, and
\(c=52\), `fail_le_geometric` applies with \(r=22\sqrt{52p}\). This ratio is below one exactly
when \(p<1/25168\) (`surface_code_rate`).

An operation outside the spacetime-volume argument has its own gadget bound. Under local
stochastic noise, if every failing pattern contains a malignant pair or at least three faults,
then \(P(\mathrm{fail})\le|M_2|p^2+\binom{|L|}{3}p^3\) (`exrec_pair_bound`).

**Reliability against age** (`AgeReliability`). A distance \(D\ge\log(Kt^d/\varepsilon)/(-\log r)\)
holds the global failure over \(Kt^d\) locations below \(\varepsilon\) at every age
(`log_distance_schedule`). A logarithmic overhead per location, however, is not absorbed into an
age-independent constant: for every \(C\) some \(t\ge1\) has \(Ct^d<t^d\log t\)
(`log_factor_not_absorbed`). The age-independent bill therefore needs the logarithm removed by
construction.

**Remaining joins.**

- The potential argument for merges at every \(d\), with the round index as the time-like
  potential.
- A map-by-map list showing that every repeated local map of holding, recovery, encoding, handoff
  and smearing is a Clifford circuit with exact native gates. This removes the compilation
  logarithm.
- Tolerance of the wavefront sweep to sparse patch failures, so that constant-distance inner
  patches suffice. This needs:
  - confinement of each failure;
  - no cascade through the feedforward front;
  - an outer decoder of the constant-size message \(W\) using its carrier's redundancy, with
    its deviation bound.

  This removes the reliability logarithm.
