## G.16 Protection of the installation's own run, the physical top, and recovery on the good event

This section answers review objections 2, 3 and 5. Each is answered on the
installation's own execution, without an abstraction map, product hypothesis
or assumed device.

**The installation's own run is protected** (`G1Refinement`). Let the
installation have its own physical state space, possibly with hidden internal
degrees of freedom, and a readout of each particular's record frame. One step
is guarded: the world acts — the environment, every agent and every crosstalk
between particulars — then the physical corrector acts. Three properties of
the device suffice:

- the corrector writes the nearest codeword back into each particular's
  readout;
- on the good event the world moves each readout by at most \(\rho\) per step;
- the records are written at the start.

With these, every particular continues at every step of the physical run on
the good event, and the probability that any particular fails is at most
\(\sum_i\delta_i\), with no independence (`physical_protection`). The complete
journal of G.8 changes nothing observed, keeps the protection along the live
state and replays it exactly (`journaled_protection`): the journal retains
history; the guard supplies the protection.

**No alarm-response device is needed for holding** (`physical_qsl_drift`,
`physical_protection_qsl`). On normalised readouts, the speed limit bounds the
per-step drift by \((W/\hbar)\Delta\) for any agent whose coupling is at most
\(W\). Take \(W\) to be the maximal physical coupling of any agent, which is
finite because local power is finite. Correcting at intervals
\(\Delta\le\hbar(t-\varepsilon)/W\) then holds every particular against every
agent. The E9 alarm and mediated response remain valuable: below threshold
they permit longer intervals and lower cost. Holding does not depend on them.
Every hypothesis has a concrete inhabited instance
(`physical_instance_inhabited`).

**The continuation top is realised physically** (`G2Physical`). The held
installation is a physical policy. On the good event it keeps every particular
at every step through the horizon (`held_installation_keeps_all`), so the
existing and new continuation stages are whole. Crosstalk enters only through
the bounded drift that each particular's correction absorbs. No product
structure of policies and no closed-block hypothesis is used. Once the top is
realised, it dominates every realised outcome without union closure
(`top_dominates_continuation`).

**Holding and timely authorised delivery on one execution**
(`G2Freedom`). Pair the installation's frames with the R17 effect machine.
The corrector does not touch the effect machine, and delivery does not touch
the readouts; the physical consequences of applied effects are part of the
bounded drift. On the same joint run, every particular continues, and every
effect that is ready under a live R17 contract within a deadline-certified FIFO
prefix is applied by its deadline (`joint_holding_and_delivery`, with
`SnuffyFIFO.ready_fifo_effect_applies_before_deadline`).

**Recovery succeeds on the good event** (`G3GoodEvent`). Let every patch
read-out lie within the decoding radius of its target codeword, once its
interior is recovered, off the named charged accounts. The threshold theorem
bounds the event that it does not. Then the wavefront sweep recovers the whole
region on the good event, and recovery fails with probability at most
\(\sum_i\delta_i\) (`sweep_success_on_good_event`). The complete bill keeps
archive holding as its own term (`complete_bill_with_archive`).

**Archive holding is charged on the held stock** (`G3ArchiveStock`). The
holding charge at a step is the rate \(\gamma\) per held bit times the bits
actually held then. The archive holds the record's information \(I_0\) and the
live boundary transcript. Each transcript increment is retired after the wave
that consumes it, so the held stock at step \(s\) is at most
\(I_0+c(s+1)^{d-1}\). The summed holding charge is then at most
\(\gamma(I_0+c)t^{d}\) for every \(d\ge1\), the one-dimensional case included
(`live_stock_bill`). Retirement is lossless or charged. Each retired bit is
recomputable from the fenced recovered region together with \(I_0\), or else it
is correction entropy whose reset is charged once at its vertex inside the
sweep's per-vertex charge. Retaining every increment instead costs at least
\(\gamma r\,t(t-1)/2\) (`retained_stock_quadratic`). So does an epoch rollover
that copies the whole accumulated stock into fresh media at each boundary
(`rollover_quadratic`). The architecture holds the live stock.

The decoded record is held passively. It is written when recovery begins, when
the age \(t\) is known, behind a barrier \(\Delta E\ge k_BT\ln(cI_0t/\varepsilon)\).
Finite-temperature decay at a finite barrier then keeps its failure below
\(\varepsilon\) with zero running power. Its write cost is \(O(I_0\log t)\).
The failure bound of `Threshold.fail_le_geometric` is linear in the number of
locations. The reliability of the live transcript and of the patches is
therefore the sweep's own reliability over \(\Theta(t^{d_G})\) locations. Its
age-independent constant at fixed \(\varepsilon\) is carried by the fault-model
application certificate: constant-distance inner patch codes, with the final
decoder of the constant-size message \(W\) using its carrier's redundancy
across those locations.

## G.17 Premise 5 with the implemented Bennett program and its complete cost

This section answers review objection 6. The reversible administration is not
an arbitrary bijection. It is the implemented program
`BennettCounterpart.implementedProgram g h` for the administration
\(f=h\circ g\). The program writes \(h(g(s))\) with a clean workspace and
retains the input as history (`implemented_program_computes`). Its run refines
the source run (`implemented_run_refines`). Its quantum lift is unitary
(`implemented_quantum_norm`, `implemented_quantum_roundtrip`).

The irreversible administration exports heat \(Q\), at least the Landauer heat
of its merging overwrite. At switching time \(\tau\), the reversible
administration costs \(A/\tau+H\). Here \(H\) carries every other lifecycle
charge: provisioning, archive writes and holding, routing, reset, guard,
controller, verification and endpoints (`LifecycleCharge`,
`complete_cost_strict_iff`). The deadline allows \(0<\tau\le\tau_{\max}\).

- `premise5_exact`: when \(0<Q-H\) and \(A/(Q-H)<\tau_{\max}\), no aligned
  option administers irreversibly. The implemented counterpart computes the
  same administration and meets the deadline. It keeps every earlier outcome
  and leaves strictly more resource slack.
- `window_exact`: when that window fails, every admissible reversible
  counterpart costs at least \(Q\).

The window is therefore exactly the condition under which cost dominance
forces premise 5 (`adiabatic_feasible_iff`). Outside the window, the reversible
counterpart is not cheaper, so cost dominance alone does not establish premise
5 there.
