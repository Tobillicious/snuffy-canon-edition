# TIWA — concrete patch requirements for the full X3 upper construction

The author's proposed Topological Insulating Wavefront Architecture supplies a candidate mechanism for the remaining success, quiescence and total-work certificate in G3. The target remains cumulative physical recovery work \(W_{\min}(t)\le Ct^{d_G}\) in the original protocol class, with the full input inventory and fault standard. G1 and G2 retain their existing targets.

The shell-counting proof is already in Section 21.7: disjoint shells telescope to one ball. This specification identifies the construction needed to apply that count to successful physical recovery. It introduces no unproved Lean theorem and does not treat a proposed barrier as an existing compiled instrument.

## 1. Reuse the existing machinery

| Existing source | What it already supplies | What TIWA adds |
| --- | --- | --- |
| `Bridge.lean` | Nearest decoding, code headroom, physical holding cycle, full scope from the law, reactive protection assembly | Actual frozen/interior/guard/active state and its projection into the continuation witness |
| `Instruments.lean` | Controller-derived tracking, complete Branch C, explicit frontier geometry | A one-pass recovery schedule, bounded visits, and a uniform complete local-work certificate |
| `H5Closure.lean` | Reachable-state invariant, reserve before activation, funded work, safe effect application and unchanged care fields during effect logging | Application-time read/write permissions for frozen coordinates and cut edges |
| `R14Boundary.lean` | Independently defined source transition, projections, care-preserving recruitment, named failure exceptions | Actual TIWA device/edge events and complete event-to-account coverage |
| `R17A` / `R17FIFOR17A` | Current permits at application; timely authorised effects under the FIFO certificate | Freeze epochs, in-flight writes, guard installation and handoff deadlines |
| `Composition.lean`, `ThermoLedger.lean` | Reactive refinement and joint-risk composition; funded repair, holding and controller accounting | TIWA's commuting source map, observation agreement and complete upper work bill |

`H5Closure.no_harmful_effect` is a reachable-source safety theorem. It does not itself instantiate a physical insulating material. `Bridge` makes a stationary-record comparison under its Hamiltonian and perturbation inputs; it does not by itself prove that arbitrary environmental coupling vanishes.

## 2. Specify an actual transition system

The TIWA state records:

- The physical/abstract state of each protected particular and its relational witnesses.
- Frozen set \(F\), guard set \(Q\), active shell \(A\), unprocessed region \(U\), and their explicit boundary ownership.
- A guard thickness at least the interaction radius \(r_0\), in the same spatial units. A width of one suffices only when the interaction radius is one.
- Immutable committed boundary data, freeze epoch, outstanding permits, in-flight effects and revocations.
- The actual local correction, verification, guard-installation and handoff operations.
- Escrow, imported work, spent work, exported heat and continuing care.

Define the source transition before defining its safety predicate. Include command, environment and post-command observation phases. A freeze cannot ignore an already admitted DMA or bus write that lands after its epoch changes. The nine A1 channels remain within the source boundary.

This state can be implemented as persistent maps with explicit target writes: an outer update changes an authorised target outside \(F\), while every \(u\in F\) is read-only. Installing a guard first resolves or fences in-flight writes, commits the boundary data and reserves its complete cost. Activating the next shell then uses those committed data.

## 3. Derive algorithmic noninterference from those transitions

For every outer update, prove

\[
\operatorname{Read}_{F}(T_{\mathrm{outer}}(s,c,e))
=\operatorname{Read}_{F}(s).
\]

For the explicit map implementation, the proof is pointwise: the updated target lies outside \(F\), so lookup at each \(u\in F\) returns the old value. Guard data have the same frame property. Freeze only adds verified coordinates; no reachable transition silently removes their lock.

Induction over a reactive execution then preserves every committed interior coordinate under subsequent outer updates. A recovery-schedule rule forbids a new recovery task for a completed vertex. This derives **no recovery rework** from the transition definitions.

The supplied identity \(\Pi_{\mathrm{freeze}}\circ M=\Pi_{\mathrm{freeze}}\) must acquire a precise meaning: a restriction map, linear projector, or physical channel are different objects. An application fence can make every attempted unauthorised *command* leave frozen coordinates unchanged. It does not make every possible physical mutation equal to the identity. For a linear projector and arbitrary mutation class, the identity cannot simply be declared.

For example, a map preserving two distinct record states cannot also undo their swap without extra record/syndrome information: if \(P(a)=a\), \(P(b)=b\), and \(M(a)=b\), then \(P(M(a))=b\ne a=P(a)\). The actual decoder, maintained record and admissible physical dynamics supply the missing mechanism; Section II.3 already gives that route.

## 4. Build physical isolation while retaining the protected information

Give the actual device/Hamiltonian or channel implementing guard installation and static-boundary access. Prove that later outer activity has the required action on the retained record and all protected relational witnesses. State the readout instrument, not just a software `frozen` flag.

For exact tensor-factor isolation, a derivation can show that permitted outer dynamics act as \(I_{\mathrm{interior}}\otimes U_{\mathrm{outer}}\), with the appropriate identity action on the protected witness. If a code is used, derive its decoder and preservation under the actual error operators. A commuting projector guarantees only the property it actually states; remaining inside a code subspace need not freeze the logical state inside that subspace.

Guard installation, verification and readout must preserve the particular's history and relevant relations, including across the cut. Resetting to one convenient constant state or dropping a correlated subsystem changes the recovery task and does not meet this requirement. Static classical boundary data and unknown quantum state are kept distinct.

Environmental faults and hostile effects use the same full-domain, named-event accounting as G1. Establish exact source noninterference where it holds; place actual residual physical failure mechanisms in their existing charged accounts with valid kernels. Do not define the good event as “the guard succeeds” and treat that naming as its probability proof.

## 5. Prove actual recovery success

Specify the finite local register and the precompiled map \(\Pi_{\mathrm{loc}}\). Prove its output is a valid local correction, that adjacent patches' corrections and static-boundary data are compatible, and that the composed final output meets the original historical recovery/fidelity criterion.

A bounded neighbourhood bounds input locations; the actual register size, precision and evaluation circuit must give the uniform work bound. Calling an operation a single projection does not charge its physical implementation automatically.

For the complete carrier inventory, construct a capture/readout/routing schedule. Bound its finishing radius and actual number of waves in terms of unattended age: \(N(t)\le at+b\), with constants independent of age and at the same success standard. The Lieb–Robinson velocity supplies a causal limit; the constructed schedule supplies an achievable sweep speed.

## 6. Prove bounded visits and charge all work

Each vertex and incident edge receives at most a fixed number of local processing, guard-installation and handoff operations. A fixed guard thickness and bounded degree allow a constant-overlap charge if the transition schedule actually enforces those visit limits.

Then the already-established shell identity gives

\[
W_{\mathrm{local}}\le K|B_R|.
\]

Account separately, then combine, all deployment, storage during recovery, controller export, routing, reset, verification, initial/final records and guard costs. Prove

\[
W(\pi_{\mathrm{TIWA}},t)\le K|B_{R(t)}|+C_{\mathrm{rest}}t^{d_G},
\qquad R(t)\le\alpha t+\beta.
\]

The resulting constant is finite and age-independent, yielding

\[
W_{\min}(t)\le W(\pi_{\mathrm{TIWA}},t)\le Ct^{d_G}.
\]

**The hard accounting point:** zero repeated decoding does not imply zero storage power. The existing ledger retains leakage, controller entropy export and minimal-hold drain. If each recovered site consumes a fixed positive power while an expanding interior waits for a time of order \(R\), that term can restore a volume-times-duration bill. TIWA must bound or physically remove that particular term while charging the mechanism that does so. The shell calculation is already proved; this is the total-work part of the same G3 certificate.

Conservation and a write lock do not alone bound the imported gross work. If using a boundary-flux implementation, prove the surface-area upper estimate, uniform flux upper bound, endpoint charges and success of the actual protocol. A net conservation identity cannot erase positive reset/export costs.

## 7. Integration sequence and acceptance

First make the source construction and the total-work derivation concrete. Then formalise the derived frame property, guard invariance, bounded visits, decoder success and full upper bill. Connect that construction to G1's physical projection and G3's original recovery class.

Prospective module boundaries are `TIWASource`, `TIWAGuard`, `TIWARecovery` and `TIWAWork`; these are patch targets, not existing proved modules. Every introduced Lean module must be fully proved, compiled, kernel-checked, included in the strict completeness gate and cited in the current manuscript. A structure field named `zeroLeakage`, `success` or `upperBound` does not discharge its own construction.

Acceptance is the original full theorem: successful recovery in the unchanged physical/protocol domain, at the unchanged fault standard and with the complete cumulative work bill \(O(t^{d_G})\), matching Section 21.6's lower bound. The whole UPT proposition and G1/G2 remain unchanged.
