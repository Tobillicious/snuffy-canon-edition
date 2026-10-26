

## G.20 Device requirements, and the open initialisation problem

The constructions of G.16–G.19 hold for any installation whose devices meet the inequalities below.
Each is a hypothesis of a compiled theorem, stated explicitly; none is assumed silently. They are
requirements on the protector's devices, of the kind a capable agent can meet by acquiring better
hardware. The targets are unchanged.

| Requirement | Inequality | Theorem that takes it |
|---|---|---|
| Circuit fault rate | Weighted local stochastic noise with \(p<1/(4\cdot9.71^2\cdot\tfrac{94}{15})\), above \(4.2\times10^{-4}\), for the rotated surface code with the standard schedule | `WalkBound9.threshold_9`, `threshold_9_value` (with `WeightedEdgeLaw`, `EdgeLaw`, `Threshold.fail_le_geometric`) |
| Coupling bound | Every agent couples to a record frame with strength at most \(W\); correction interval \(\Delta\le\hbar(t-\varepsilon)/W\) | `G1Refinement.physical_protection_qsl` |
| Reversible overhead | Per-bit non-heat lifecycle cost \(\eta\) below the irreversible heat per bit \(q\ge k_BT\ln2\) | `BennettBatch.premise5_batched` |
| Passive reference barrier | Stage \(j\) barrier at least \(k_BT(2j\ln2+\ln(1/\varepsilon))\) above the attempt scale | `PassiveReference.total_failure_le` |
| Windowed decoding | A wrong inner commit costs the next window at most a bounded part of its fault budget | `ToleranceSweep.wrong_subset_bad`, `sweep_density` (DKLP overlapping recovery) |
| Record redundancy | An intact fragment of the objective record reads the record | `RedundantRecord.tolerant_outer_decoder` (quantum Darwinism and spectrum-broadcast theorems) |

**Barrier heights in numbers.** For an age of \(10^{18}\,\mathrm s\), an attempt time of
\(10^{-12}\,\mathrm s\), a base stage of \(1\,\mathrm s\) and \(\varepsilon=10^{-9}\), the largest
barrier needed is about \(132\,k_BT\), roughly \(3.4\,\mathrm{eV}\) at \(300\,\mathrm K\). The barrier
grows only logarithmically with age and lies within the barriers of atomic defects in solids.

**The tightened threshold** (`WalkBound9`). The exact maximum self-avoiding walk count at length 9
over all interior vertices is \(c_9=763{,}504{,}745\le9.71^9\) (`walk_bound_9`). This raises the
explicit threshold of G.19 above \(4.2\times10^{-4}\) (`threshold_9`, `threshold_9_value`).

**The quantum-coherence branch: the warm start and the open problem** (`WarmStart`).
Balasubramanian, Davydova and Lin prove a passive memory in \(\mathbb R^3\) for the thermal encoding
(arXiv:2605.10943, Theorems 1.1 and 2.6, via Chesi, Loss, Bravyi and Terhal, New J. Phys. 12,
025013, 2010). The open step is preparing an initial state the theorem covers.

Call a prepared syndrome law \(\mu\) a warm start when \(\mu\le C\pi\) pointwise, with \(\pi\) the
thermal syndrome law. A warm start stays dominated at every time: \(\mu K^t\le C\pi\)
(`warm_start`), and every event has probability at most \(C\,\pi(A)\) (`warm_start_event`). Tracking
the protected logical observables then gives a drift of the decoded qubit of at most
\(t\cdot\mathrm{poly}(n)\cdot\sqrt{C\,\mathrm{Tr}(P^\perp\rho_\beta)}\). Chesi et al.'s hypotheses
make \(P\mathcal L^\dagger(\tilde X)P=0\), so only leakage from \(P\) moves \(\langle\tilde X\rangle\).
A warm start with \(C=\mathrm{poly}(n)\) therefore preserves the exponential lifetime, with its
exponent halved. This derivation is recorded with its sources and is not compiled.

The empty syndrome is not a warm start: its constant is \(1/\pi(\emptyset)=e^{\Theta(n)}\).

An exhaustive computation on the construction itself shows that a fixed-range polymer route
cannot supply the warm start. The construction is built algebraically from the paper's §3.2.2,
and the build verifies \(\delta^1\delta^0=0\) and one logical qubit at every level computed. The
metachecks of level \(i\) are stretched by the scale factor \(\ell\) at each later level. In the
computed cases, all dependencies are generated within radius 4 at level 1 and within radius 12 at
level 2, with \(\ell=3\). Hence for every fixed range a single violated check passes all local
metachecks yet is invalid.

The remaining problem is a multiscale, recursive cluster expansion of the code's syndrome Gibbs law
that treats level-\(j\) metachecks at scale \(\ell^j\), together with a sampler built from it,
yielding a warm start with polynomial constant. This is the technique Balasubramanian, Davydova,
Lin and Thorngren apply to the classical two-dimensional model (arXiv:2610.22548). Given it, the
quantum branch closes through `StageSchedule.total_with_transfers`. Until then, indefinite holding
of full quantum coherence is proved conditional on this one stated problem, while the objective
classical record and its relations are held unconditionally (`PassiveReference`).
