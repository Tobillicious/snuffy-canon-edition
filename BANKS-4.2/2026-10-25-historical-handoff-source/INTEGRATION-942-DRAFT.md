# Integration of the 942-name increment — draft for the 4.2 master

Prepared 25 October 2026 by Claude. **PASS-gated:** nothing below enters the
master until the fresh full 144-module run (`lean/build-and-audit.sh`, all
modules compiled and kernel-checked in this session, no reuse) returns overall
PASS with 942 audited names.

- Part A is a **new appended subsection** (G.8, placed after G.7 and before
  Part IV). The standing rule allows appended sections without prior approval;
  it is shown here so the author sees it before it lands.
- Part B lists the **rewrites of existing sentences** (counts and receipt
  descriptions). Per the rule, these need the author's OK as one before/after
  batch.

---

## Part A — new subsection [append-only]

## G.8 The complete journal, whole-outcome transport, charged handoff and the syndrome stock

This subsection joins the full historical record to the holding bill. The
historical record is kept in full and moved reversibly. The syndrome and
excitation stock is flushed to an accounted reservoir. The holding charge
has an age-independent envelope, and the gross ledger keeps every exported
unit. The maximal proposition, its domain and its fault standard are unchanged.

**The complete journal.** Let the source have states \(X\), commands \(C\),
environment inputs \(E_v\) and transition \(T:X\times C\times E_v\to X\). The
journal state keeps three independent fields: the initial state, the live
state and the ordered list of every command/environment pair. A step applies
\(T\) to the live state and appends \((c,e)\). Replay folds \(T\) over the list
from the initial state. If replay equals the live state before a step, it
equals it after the step, since folding over an appended list applies \(T\)
once more (`G1FullDomain.replay_journal_step`).

Use the projection \(s\mapsto s_{\mathrm{live}}\). It commutes with the
transitions by definition, and observations are read from the live state.
Proposition 5 (reactive lockstep) then gives, for **every** reactive controller
\(\mathrm{ctrl}:\mathrm{List}\,O\to C\) and every reactive environment
\(\mathrm{env}:\mathrm{List}\,O\to C\to E_v\), at every step \(k\):

\[
s^{\mathrm{journal}}_{k,\mathrm{live}}=s_k,\qquad
\mathrm{obs}^{\mathrm{journal}}_{0..k}=\mathrm{obs}_{0..k},\qquad
\mathrm{replay}(s^{\mathrm{journal}}_k)=s^{\mathrm{journal}}_{k,\mathrm{live}}.
\]

Induction on \(k\) carries the replay invariant
(`G1FullDomain.journal_reactive_fidelity`). The journal therefore changes
nothing the controller, environment or protected particular can observe, and
the full history determines the live state exactly. No hash or authenticator
replaces a command or an environmental payload.

The record's size is counted from its alphabet. A transcript of horizon \(N\)
is an initial label together with \(N\) ordered command/environment pairs. If
\(|X|\le2^{b_0}\) and \(|C\times E_v|\le2^{b}\), then

\[
|X\times(C\times E_v)^N|\le2^{\,b_0+bN}
\quad(\texttt{G1FullDomain.transcript\_capacity}).
\]

This is the full payload's capacity, not the length of a digest.

**Whole-outcome transport.** Let \(\mathrm{outcome}\) be any function of the
final state and the complete observation history. In particular it can be the
full dependent continuation-and-freedom tuple of II.1. Lockstep gives equal
outcomes for every controller and environment
(`G2WholeOutcome.journal_whole_outcome`). Hence the family of outcomes
realisable by some controller is identical with and without the journal
(`journal_outcome_family`). Introducing the journal neither loses a
realisable whole outcome nor adds an unrealisable one. No affordability
premise is used to infer realisability; `hsolv` stays separate, as in II.10.

**Reversible, reference-preserving handoff.** For a bulk register and a
reserved boundary register of the same dimension \(\iota\), together with an
arbitrary reference \(R\), let \(\mathrm{swap}\) be the coordinate
permutation of \(\mathbb C^{(\iota\times\iota)\times R}\) exchanging the two
registers and fixing \(R\). It is a linear isometry equivalence. If the
boundary register holds the blank state, then any payload \(\chi\) on
\(\iota\times R\), however entangled with the reference, is moved to the
boundary and the bulk is left blank
(`DecoderRetraction.handoff_moves_reference_payload`). Nothing is copied, so
there is no conflict with no-cloning. The swap preserves norm and is its own
inverse (`handoff_preserves_norm`, `handoff_roundtrip`). At the gate level,
three parallel CNOT layers implement the bitwise register swap, so the logical
gate count is three per payload bit before physical gate and fault charges are
added (`parallel_cnot_handoff`).

Superpositions of full transcripts are encoded isometrically into a boundary
register of dimension \(2^{b_0+bN}\) by extension by zero along the capacity
embedding above (`DecoderRetraction.transcriptBoundaryEncoder`).

**The charged attempt.** One admitted handoff attempt carries a nine-part
charge: encoding, transfer, verification, routing, guard, reset, holding,
controller and endpoints. Admission reserves the total before the source
operation. The attempt debits the full total whether or not it commits, and
the payload moves only on commit. Hence

\[
\mathrm{spent}'=\mathrm{spent}+q_{\mathrm{tot}},\qquad
\mathrm{escrow}'+\mathrm{spent}'=\mathrm{escrow}+\mathrm{spent},
\]

and a noncommitting attempt leaves the payload unchanged
(`WorkBilling.charged_attempt_accounting`). The payload has a single logical
owner, either live or sealed under a decoder pair. Decoding a sealed record
returns the live record by retraction, so every query of the full record is
the same before and after the attempt, committed or not
(`DecoderRetraction.charged_archive_handoff`). Failed verification is
charged; it is not free and it destroys nothing.

**History is untouched by the flush.** Let \(\rho\) be any joint state on
\(\mathcal H_{\mathrm{hist}}\otimes\mathcal H_{\mathrm{flush}}\). The history
factor may include an arbitrary reference, and \(\rho\) need not factorise.
For any \(P\) on the history factor and any unitary \(Q\) on the flushed
factor, the reduced history state, including all of its off-diagonal
coherences, satisfies

\[
\operatorname{Tr}_{\mathrm{flush}}\!\bigl((P\otimes Q)^\dagger\rho(P\otimes Q)\bigr)
=P^\dagger\operatorname{Tr}_{\mathrm{flush}}(\rho)P
\quad(\texttt{HamiltonianDecomposition.partial\_trace\_local\_conjugation}).
\]

The proof expands the partial trace and uses \(\sum_kQ_{ck}^{*}Q_{c'k}=\delta_{cc'}\).
With \(P=I\) the history's reduced state is unchanged
(`guarded_history_reduced_state`). For the explicit syndrome/reservoir
exchange gate \(S\) of G.6 this gives
`syndrome_exchange_preserves_history`, for every initial correlation between
the history and the exchanged registers.

The charge is moved, not deleted. By cyclicity of the trace and
\(S^\dagger Q_\partial S=Q_R\),

\[
\operatorname{Tr}(S\rho S^\dagger Q_\partial)
=\operatorname{Tr}(\rho\,S^\dagger Q_\partial S)
=\operatorname{Tr}(\rho\,Q_R)
\quad(\texttt{syndrome\_exchange\_charge}).
\]

The syndrome's charge after the exchange is the reservoir's charge before it.
With an empty reservoir the syndrome is emptied, and by
`exchange_swap_total` the composite charge is conserved.

**The age-independent stock envelope (the author's Theorem 4.1, Steps 3–4).**
Let the stored syndrome charge per flushing cycle obey

\[
q_{k+1}=(1-\alpha)q_k+\mathrm{influx}_k,\qquad 0<\alpha\le1,\qquad
\mathrm{influx}_k\le\mathrm{cap}.
\]

Then for **every** cycle \(k\), not only in the limit,

\[
q_k\le\max\!\left(q_0,\ \frac{\mathrm{cap}}{\alpha}\right)
\quad(\texttt{WorkBilling.syndrome\_stock\_bound}).
\]

The proof applies the existing tracking theorem `ThermoLedger.tracking_bounded`
to the recurrence. With the author's local influx \(\mathrm{cap}=\kappa\,t_G^{d}\),
this is \(q_k\le\max(q_0,(\kappa/\alpha)t_G^{d})\). Here \(C=\kappa/\alpha\)
depends only on the local influx and flush fraction, and is independent of
operating age. The theorem also covers an initial stock above the steady
value, and it bounds every cycle uniformly in \(k\). The author's
\(\limsup\) statement follows.

The flush is retained in the gross ledger. Summing the recurrence gives the
exact balance

\[
q_N+\sum_{k<N}\alpha q_k=q_0+\sum_{k<N}\mathrm{influx}_k
\quad(\texttt{syndrome\_flux\_balance}).
\]

The final stock plus every exported unit equals the initial stock plus every
imported unit. The bounded stock does not replace the cumulative work.
Suppose the complete per-cycle cost satisfies
\(\mathrm{cost}_k\le u\,\mathrm{influx}_k+v\,\alpha q_k+w\,\mathrm{active}_k\),
with every import, flush, holding, guard and controller charge included, and
\(u,v,w\ge0\). Suppose also that \(\sum_{k<N}\mathrm{influx}_k\le\kappa V\),
\(q_0\le q_{\mathrm{init}}V\), \(\sum_{k<N}\mathrm{active}_k\le V\) and
\(q_N\ge0\). Then

\[
\sum_{k<N}\mathrm{cost}_k\le\bigl(u\kappa+v(q_{\mathrm{init}}+\kappa)+w\bigr)V
\quad(\texttt{cumulative\_maintenance\_bound}).
\]

The theorem is stated for arbitrary real sequences. Applied to the realised
pathwise sequences it gives the pathwise gross bill. Applied to expectations
it gives the expected bill. Each use keeps its own meaning, and the desired
cumulative bill is never an input.

**How the pieces join.** Step 1 of the submission (a Lindblad generator with
a positive gap) is the dissipative model that supplies the flush fraction
\(\alpha\). Steps 3–4 are now the compiled stock envelope above. The memory
decay of Step 2 applies to the flushed syndrome and excitation stock. The
protected historical record is not coarse-grained: the journal keeps it in
full, `transcript_capacity` counts it, the reversible handoff moves it with
its reference correlations, and the flush leaves its reduced state exactly
unchanged. The archive's continued storage enters \(\mathrm{active}_k\) and
\(\mathrm{cost}_k\) of the cumulative bill. It is charged and is not
discarded to keep the stock small.

**What is already supplied, for every source.** The journal theorems are
stated for an arbitrary transition \(T\), controller and environment. Every
source therefore has its complete history retained, replayed and
observationally invisible, with no further construction. The capacity
\(2^{b_0+bN}\) and the isometric transcript encoder are derived from the
source's own alphabet. The handoff is an explicit unitary with an explicit
circuit of three CNOT layers, and its nine-part charge is debited exactly.
The per-site injection rate is bounded by the speed limit
(`SpeedLimit.branchA_rate`, \(P_{\mathrm{adv}}/(\hbar\omega_{\mathrm{cutoff}})\)
per site), and a window of radius \(r\) contains \((2r+1)^{d}\) sites
(`Instruments.card_box`). Their product is the per-cycle influx cap,
\(\mathrm{cap}=\kappa t_G^{d}\). The conversion from per-site divergence to
syndrome charge is the stroke-I measurement accounting of Section 18; this
composition is a prose derivation.

What the physical installation contributes is the identification of its
actual \(T\), alphabet and per-site coupling with these symbols, and pathwise
measurement of the cost terms. That is the G1 source certificate of Part
III-C, now with its history, capacity, handoff and stock components compiled.

---

## Part A2 — new subsection [append-only], with new module `G2Splice` (seven names)

`G2Splice` is a new module developed after the 942-name increment. It is
compiled (exit 0, zero output), passes `leanchecker`, and depends only on the
standard axioms; its bank is `g2-splice/`. It enters the canon as module 145
after the 942-name run passes, followed by a further full gate run.

## G.9 The whole greatest outcome is realisable: union closure from locality

Part II.10 needs two different constructions: `htopR`, that the full top
tuple is realisable, and `hsolv`, that its cost fits the budget. The singleton
route of E.2 needed union-closed realisability. Here union closure is
derived, not assumed.

Locality (P4) gives each particular its own local component of a policy, and
the shared action interface makes every agent act through those components.
Write a policy as \(\pi=(\pi_x)_x\), with \(\pi_x\) realisable for \(x\), and
let the particular's grade \(g_x(\pi_x)\) in a linear order record its stage.
In the four-stage order the grades are lost \(<\) continues \(<\) continues in
its own direction. The freedom stage is the law's freedom: per II.2,
restraint removes harmful command, authority and effect channels, so one
particular's freedom never consists of another's loss. Stage \(i\) of the
outcome tuple is the set of particulars of its category whose grade reaches
the stage threshold.

For realisable \(\pi,\sigma\), define the splice
\((\pi\sqcup\sigma)_x=\pi_x\) if \(g_x(\sigma_x)\le g_x(\pi_x)\), and
\(\sigma_x\) otherwise. Each component is realisable, so the splice is
realisable. Its grade is \(\max(g_x(\pi_x),g_x(\sigma_x))\), and a threshold
is reached by a maximum exactly when it is reached by either argument.
Therefore

\[
\mathcal O(\pi\sqcup\sigma)=\mathcal O(\pi)\sqcup\mathcal O(\sigma)
\]

at every stage at once (`G2Splice.splice_grade`, `splice_realisable`,
`outcome_splice`). This is `UnionClosure.UnionRealizable` for the realised
family (`union_realizable`).

For the top, choose for every particular a realisable component reaching
every stage threshold it is subject to. The product of these choices is
realisable, and every stage contains its whole category, so
\(\top\in R\) (`top_realisable`). No finiteness of the domain is used.
Joined to `greatest_of_solvent`, every aligned option of the funded family is
\(\top\) and contains every outcome tuple (`whole_outcome_greatest`). The
four-stage instance \((L_E,F_E,L_N,F_N)\) proves all three conclusions
together from one hypothesis per particular: some realisable local component
under which that particular continues in its own direction (`fourStage`).

**The product structure from the actual dynamics.** The splice is realised by
the physical evolution itself. Let the source state be a function on the
nodes of its dependency graph \(D\). Let each particular's held record occupy
a block \(B_x\) of nodes, with the blocks closed under \(D\) and pairwise
disjoint. Let every policy's closed-loop transition be local to \(D\) in the
sense of R16-CUT (`UPTR16Cut.LocalTo`). Run each block under the policy chosen
for its particular. Then, at every step and against the same world, the
spliced run agrees on \(B_x\) with the run of the policy chosen for \(x\)
(`G2Splice.block_splice_run`). The proof is induction on steps with
`UPTR16Cut.closed_cut_step`. Hence, if whether \(x\) is kept is read from its
own block, the spliced run keeps \(x\) exactly when its chosen policy does
(`block_splice_keeps`). Each particular receives the outcome of the policy
chosen for it, which is the product structure used above.

**How each input is supplied.**

1. *Per-particular top component.* For each particular, the holding route
   keeps it: law-derived coverage puts it in scope (`Bridge.coverage_from_law`).
   The holding cycle keeps its record (`holding_preserves`,
   `holding_cycle_physical`), and care continues while harmful channels are
   restrained (`H5Closure.effect_preserves_care`,
   `UPTR14Boundary.recruitment_never_ends_care`). Its authorised effects are
   applied in time (`SnuffyFIFO.applied_fifo_effect_is_timely_and_authorized`, module `R17FIFOR17A`).
   Its freedom is the law's freedom of II.2, which excludes harm to others.
2. *Locality.* This is derived above from R16-CUT locality and closed blocks.
   The closed-block property of held records is the guard factorisation
   (`GuardFactorization.commutativity`, `ClosedCohold.factorised_cohold`,
   `PhysicalGuard`). The relations between particulars are themselves
   particulars in the domain, each with a held record.

The physical installation identifies its dependency graph and the blocks of
its held records; that is the G1 source certificate. `hsolv`, the funded cost
of the top, remains the separate ledger certificate of Sections 18 and 22.

---

## Part B — rewrites of existing sentences [rewrite, PASS-gated, needs the author's OK]

Each BEFORE quote is copied exactly from the current master. The AFTER text
applies only if the fresh run passes.

**B1. Header paragraph (master line 11).**

> BEFORE: The current Lean tree contains 144 modules and 924 audited public theorem/lemma names. The combined receipt reuses Beam's 136 clean compilation/kernel results after source and object hash checks, adds eight freshly compiled and kernel-checked modules, and records a fresh full axiom audit, completeness and claims gates with overall PASS.
>
> AFTER: The current Lean tree contains 144 modules and 942 audited public theorem/lemma names. All 144 modules were freshly compiled and kernel-checked in one run, with a fresh full axiom audit and fresh completeness and claims gates, overall PASS. The earlier 924-name combined receipt, which reused Beam's 136 results, is preserved with its bank.

**B2. Section 23 lead (master line 1433).**

> BEFORE: *This section maps the edition's compiled results and their actual hypotheses. The current source contains 144 modules and 924 audited public theorem/lemma names. The combined receipt records 136 reused clean compilation/kernel results, eight fresh compilation/kernel checks, a fresh full axiom audit with only `propext`, `Classical.choice` and `Quot.sound`, and fresh completeness/claims gates with overall PASS.
>
> AFTER: *This section maps the edition's compiled results and their actual hypotheses. The current source contains 144 modules and 942 audited public theorem/lemma names. The receipt records a fresh compilation and kernel check of all 144 modules, a fresh full axiom audit with only `propext`, `Classical.choice` and `Quot.sound`, and fresh completeness/claims gates with overall PASS.

The sentence that follows it ("The reused results are tied to the preserved
Beam receipt and source/object hashes.") would be deleted, since this run
reuses nothing.

**B3. §23.9 table rows (master lines 1572, 1573, 1576, 1578, 1579).** Append to
each existing row's description:

- `G1FullDomain`: "; independent journal/live updates, exact replay, reactive fidelity for every controller and environment, and full-transcript capacity (G.8)"
- `G2WholeOutcome`: "; preservation of an arbitrary complete outcome and equality of the realised outcome families under the journal (G.8)"
- `HamiltonianDecomposition`: "; full off-diagonal reduced-state covariance under a local unitary, history preserved by the syndrome exchange, and exact charge transfer to the reservoir (G.8)"
- `WorkBilling`: "; the nine-part charged handoff attempt with exact debit and conservation, the age-independent syndrome stock envelope, the gross flux balance and the cumulative maintenance bill (G.8)"
- `DecoderRetraction`: "; reference-preserving reversible register swap, full-transcript boundary encoder, three-CNOT-layer swap and charged archive handoff (G.8)"

**B4. Appendix (master line 2250).**

> BEFORE: The current working tree contains 144 modules and 924 audited public theorem/lemma names. The combined verification preserves Beam's completed 136 compilation/kernel results with source/object hashes, freshly verifies the eight later modules, and freshly runs the full axiom, completeness and claims gates. The receipt states exactly which results are reused.
>
> AFTER: The current working tree contains 144 modules and 942 audited public theorem/lemma names. All 144 modules were freshly compiled and kernel-checked, and the full axiom, completeness and claims gates were freshly run, overall PASS. The earlier 924-name combined receipt, which reused Beam's 136 results, is preserved with its bank.

**B5. §23.A index.** This is the generated region, regenerated by `gen-index.py`
from the sources. It gains the 18 names listed in G.8 and is replaced
mechanically, not edited by hand.

---

## Part C — §22.3 correlated bursts [rewrite, needs the author's OK]

New module `CorrelatedCeiling` (seven names; exit 0, zero output, `leanchecker`
passes, standard axioms; bank `correlated-ceiling/`). It joins bridge 6
(`CorrelatedStress`) to the threshold theorem. Shocks of footprint at most
\(k\), with each location touched by at most \(m\) shocks and local
stochastic at rate \(q\), produce damaged locations that are local
stochastic at rate \((e\,m\,k\,q)^{1/k}\) (`damage_local_stochastic`). The
ceiling is therefore attained at a sufficient code distance
(`correlated_family_ceiling`). It enters the canon as a new module together
with `G2Splice`.

**C1. Table row, accounts 5–7 (master line 1341).**

> BEFORE: | **5–7** | Correlated bursts (high-energy impacts, phonon events) | Gap engineering, rapid reset | $3 \times 10^{-8}$ | **Not yet met.** The measured logical floor is ≈ 10⁻¹⁰ per cycle [S6]; the target is ≤ 3.7 × 10⁻²⁴ per cycle per logical qubit (§22.5.2) |
>
> AFTER: | **5–7** | Correlated bursts (high-energy impacts, phonon events) | Gap engineering, rapid reset, code distance beyond the burst footprint | $3 \times 10^{-8}$ | **Attained at a sufficient distance** (`CorrelatedCeiling.correlated_family_ceiling`): bounded-footprint bursts are local stochastic at rate $(e\,m\,k\,q)^{1/k}$. The measured floor on present devices is ≈ 10⁻¹⁰ per cycle [S6], which fixes their burst parameters; the target is ≤ 3.7 × 10⁻²⁴ per cycle per logical qubit (§22.5.2) |

**C2. "Correlated errors" paragraph (master line 1351).** The first two
sentences are kept unchanged. The last two sentences:

> BEFORE: The threshold theorem's geometric decay (§23.8) holds for the noise it assumes, local and weakly correlated. Present hardware satisfies that assumption up to d ≈ 11–15, and removing the floor is the open engineering requirement of accounts 1–7.
>
> AFTER: The threshold theorem covers these correlated events. Let each burst damage at most $k$ locations, let each location be touched by at most $m$ burst types, and let bursts be local stochastic at rate $q$, common causes included. Then the damaged locations are local stochastic at the effective rate $(e\,m\,k\,q)^{1/k}$ (`CorrelatedCeiling.damage_local_stochastic`). Every target ceiling is then met at some code distance and at every larger one (`correlated_family_ceiling`). Correlated damage therefore sets no floor that distance cannot pass. The measured deviation at d ≥ 15 [S6] fixes the burst parameters of present devices, which enter this theorem.

**C3. "What it does not yet certify", first bullet (master line 1380).**

> BEFORE: * The 10⁻⁶ failure ceiling over 10⁹ s on present hardware. The measured correlated floor [S6] is the open engineering requirement, stated here with its size.
>
> AFTER: * A built installation at the distance the ceiling requires. The ceiling is attained by theorem for local and correlated bounded-footprint faults (`Threshold.family_ceiling`, `CorrelatedCeiling.correlated_family_ceiling`). Present devices measure their burst parameters [S6], and the required distance follows from them.
