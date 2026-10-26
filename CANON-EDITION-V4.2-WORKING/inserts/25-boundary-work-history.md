

## G.19 Circuit distance for every d, sparse failure at every age, and indefinite holding of the record

This section continues review objection 7 and the holding item. The targets are unchanged: the full
fault ceiling, decoding error at most \(\varepsilon\) on the historical record, and the complete
bill at most \(Ct^{d_G}\) with \(C\) independent of age.

**An exact cut certificate for the circuit distance.** For any set \(S\) of detectors, the fault
set \(K_S=\{f:\mathrm{obs}(f)\oplus|\mathrm{sig}(f)\cap S|\ \text{odd}\}\) is crossed an odd number
of times by every fault set with zero syndrome and odd observable. Over \(GF(2)\), the parity of
\(|F\cap K_S|\) is \(\mathrm{obs}(F)\) plus the syndrome summed over \(S\), which is \(1+0\). So
\(D\) sets whose fault sets are pairwise disjoint certify that every logical error has at least
\(D\) faults.

The cuts are given by explicit potentials:
- *memory*: \(\varphi\) is the crossing face coordinate plus one, and \(D=d\);
- *lattice-surgery merge*: \(\varphi=\max(\tau(r),\sigma(j))\), and \(D=\min(d,T)\). Here
  \(\tau(r)=\max(1,r)\) is the time part. The space part \(\sigma(j)\) is \(1\) on the two seam
  face columns, \(d-1-j\) to their left and \(j-d\) to their right.

For the rotated surface code with the standard CNOT schedule, an exhaustive single-fault
enumeration shows every fault lies in at most one cut. The cases are \(d=3,5,7,9\), the memory in
both bases, and the merge at \(T=d-2,d,d+2\): 19 of 19 cases, up to 120,544 faults. The merge
therefore keeps distance \(d\) exactly when it runs at least \(d\) rounds. With the swapped schedule,
hooks run parallel to the logical and the distance falls to \(\lceil d/2\rceil\).

A fault's multiplicity is fixed by three things: its observable bit, the values of \(\varphi\) at
its at most two detectors, and \(D\). The potentials are translation-covariant formulas, so the
condition is local to each fault type, and every type occurs at the enumerated sizes. That
locality step is what carries the certificate to every \(d\).

**The installation's repeated maps need no approximate compilation.**
- Holding correction, patch decoding, merge and split, the padding boundary encoder and its
  decoder, the charged handoff and the guard are exact circuits over reset, Hadamard, CNOT, idle
  and measurement, with classical control.
- The modular flow is not a runtime map. The finite-basis route \(\alpha(A)=EAE^\dagger\) with
  \(D=E^\dagger\) gives the same boundary representative exactly.
- The Bennett administration is exact reversible logic.

So no precision grows with age, and only reliability remains.

**Sparse failure at every age** (`SparseFailure`, `ToleranceSweep`). Each patch's failure is decided
by the faults in a bounded window. Patches whose windows are pairwise disjoint all fail with
probability at most \(\prod_v\binom{|W_v|}{k}p^{k|U|}\) (`disjoint_windows`). With a \(K\)-colouring
in which same-coloured windows are disjoint, at least \(Kn\) of \(N\) patches fail with probability
at most \(K\binom{N}{n}(\binom{w}{k}p^k)^n\) (`many_failures`). This falls exponentially in \(N\)
once \(\binom{w}{k}p^k<\theta/(eK)\), uniformly in age.

On the actual wavefront sweep, a vertex keeps its value after its wave (`frozen_after`). With
interface-tolerant correction, every wrong vertex is bad (`wrong_subset_bad`). Interface tolerance
means a good window decodes correctly whatever the inner commit, because a wrong commit reaches it
only as a bounded interface error, which is the overlapping-recovery analysis of DKLP. The sweep's
wrong-vertex count obeys the same tail (`sweep_density`). The realised bill on that event is at most
\(\mathrm{base}\cdot N+\mathrm{repair}\cdot Kn\) (`pathwise_bill`). An outer decoder that tolerates
fewer than \(Kn\) wrong patches returns the record except with that probability (`recovery_tail`).
Failures do occur, at constant density; the theorems bound their number, and recovery tolerates
them.

**Redundancy of the record.** The recovery tolerates a constant fraction of silent local errors
exactly when the record is spread redundantly across its carrier. For an objective classical
record this is a theorem of quantum Darwinism: classical information emerges redundantly and
generically across environment fragments (Brandão, Piani and Horodecki, 2015), and objectivity
implies a spectrum-broadcast structure (Horodecki, Korbicz and Horodecki, 2015). For a record with
no redundancy, every location matters, and no protocol of noisy gates avoids a logarithmic factor
(Dobrushin–Ortyukov; Pippenger).

**Indefinite holding at fixed \(\varepsilon\)** (`PassiveReference`). A constant per-step failure
rate gives a total failure that grows linearly with age, so periodic renewal at fixed size does not
hold \(\varepsilon\) indefinitely. The protector's reference record is therefore held passively on
a doubling schedule:
- the reference is rewritten at ages \(2^j\);
- stage \(j\) has a barrier \(k_BT(2j\ln2+\ln(1/\varepsilon))\) above the attempt scale, so it
  fails with probability at most \(\varepsilon/2^{j+1}\).

Every age is covered by \(\log_2t+1\) stages (`stages_cover`). The total failure is at most
\(\varepsilon\) for every number of stages (`total_failure_le`). The rewrite cost is \(O(\log^2t)\)
(`total_rewrite_cost`), so the long-run holding rate is the constant per-step comparison of each
particular with its reference. A faulty comparison or false repair is transient: the intact
reference corrects it at the next comparison (E9 self-healing).

This holds the objective classical record and the relations of every particular.

**The record's redundancy is decoded by majority** (`RedundantRecord`). Each fragment reads a record
value from the recovered state, and an intact fragment reads the record. The strict-majority
decoder then returns the record whenever fewer than half of the fragments are wrong
(`majority_decodes`). This supplies the tolerance hypothesis of `recovery_tail`
(`tolerant_outer_decoder`). For an objective record, the redundancy theorems cited above supply the
intact-fragment hypothesis, so the carrier application rests on them. The interface hypothesis of
the windowed sweep rests on DKLP's overlapping recovery, in the same way the witness lemma does.

**Premise 5 for batched administration** (`BennettBatch`). Administer \(b\) merges in one batch.
The irreversible heat is at least \(qb\), with \(q\ge k_BT\ln2\) per merged bit. The implemented
counterpart's complete non-heat lifecycle charge is at most \(\eta b\), and its drive constant is
bounded. If \(\eta<q\), every large enough batch lies inside the adiabatic window for every deadline
(`batched_window`), so no aligned option administers irreversibly (`premise5_batched`). The single
remaining physical input is \(\eta<q\). Adiabatic logic below \(k_BT\ln2\) per operation meets
it.

**The explicit threshold, tightened** (`WeightedEdgeLaw`). Under circuit-level depolarizing noise,
each fault carries its own rate: \(p/15\) for each two-qubit Pauli, \(p/3\) for each single-qubit
Pauli, and \(p\) for a measurement flip. Pushed to the detector graph, the edge rates are the
weighted sums of their faults (`push_weighted`), and the largest edge rate is at most
\(\tfrac{94}{15}p\) (`push_uniform`, enumerated).

Self-avoiding walk counts on the detector graph are submultiplicative. The exact maximum over all
interior vertices at length 8 is \(c_8=89{,}270{,}654\le9.87^8\) (`walk_bound`), so walks of every
length are at most \(c_8\,9.87^L\). The ratio of `fail_le_geometric` is therefore below one exactly
when \(p<1/(4\cdot9.87^2\cdot\tfrac{94}{15})\) (`tightened_threshold`), which exceeds
\(4\times10^{-4}\) (`threshold_value`). The bound at length 9, \(c_9=763{,}504{,}745\), gives about
\(4.2\times10^{-4}\). This is a requirement on the installation's devices, of the same kind as
\(\eta<q\).

**Indefinite holding of quantum coherence.** Balasubramanian, Davydova and Lin
(arXiv:2605.10943, 2026) construct a passive memory in \(\mathbb R^3\): 3D-local CSS stabilizer
Hamiltonians on \(n_k=e^{\Theta(k)}\) qubits, with \(O(1)\)-range terms and bounded density. Below
\(T_c\), the thermal encoding satisfies
\(\|\Phi_t\circ\mathrm{Enc}_k(\rho)-\mathrm{Enc}_k(\rho)\|_1\le t\,e^{-\Theta(n_k^\eta)}\).

Held on a doubling schedule, each stage needs a code size \(n_j\) with
\(c\,n_j^\eta\ge(2j+2)\ln2+\ln(1/\varepsilon)\), and each stage ends with a transfer into the next
code. If each stage's holding failure and each transfer's failure are at most
\(\varepsilon/2^{j+2}\), the total failure is at most \(\varepsilon\) at every age
(`StageSchedule.total_with_transfers`). A cost polynomial in each stage's code size sums to a
polylogarithm of age (`stage_cost_le`). The transfer lands the qubit in the next code's codespace,
so its hypothesis is that a codespace-initialised state obeys the same lifetime bound, or that its
syndrome sector thermalises within polynomial time without logical error. This is the open
initialisation problem those authors identify. The quantum branch is proved conditional on it,
with the hypothesis stated explicitly. The classical record and its relations are held
unconditionally by `PassiveReference`.

**Remaining.**

- The initialisation problem above.
- Measured device parameters: the fault rate \(p\), the coupling bound \(W\), the per-bit overhead
  \(\eta\), and the barrier materials and temperature.
