# Current local UPT continuation — updated 27 October 2026

The remaining physical task is the full noisy G.21 transfer/holding
installation at the original stage budget, with arbitrary reference
correlations and its admitted fault model. The author asked us to construct
the bridge ourselves. A new noise-compensated preparation and private
output-interface route is now derived in development notes; continue that
construction, not another cycle of rejecting the pasted proposals. The
maximal UPT, full history and gross pathwise work target remain fixed.

Worktree: /Users/admin/Documents/2026/Snuffy-Book/UPT-WARMSTART-WORKTREE.
Branch: codex/upt-warmstart-bridge. Work is local and staged for author
review; no merge, push or publication. Published trees are untouched.

## Exact current construction — start here

Read REPAIRS-2026-10-26/FT-PRIVATE-OUTPUT-BRIDGE-2026-10-27.md and
NOISE-COMPENSATED-PREPARATION-2026-10-27.md. The new route is:

1. Sample a positive law q satisfying Nq=pi for the actual specified local
   Pauli output channel N, rather than prepare pi and ignore N. A signed
   auxiliary polymer representation proves positivity under explicit fixed
   local inequalities. Positive-history self-reduction gives mu<=4q in
   polynomial pathwise work and finite coins. This is a prose application
   of the counting theorem, not an implemented general FPTAS.
2. A short FT processor performs the transfer. Fresh independent encoded
   Bell resources, logical Bell measurement and private output decoders
   remove the old output-gauge correlations. The exact channel identity
   retains arbitrary references. Its private-interface model yields product
   Pauli output channels, with unequal rates allowed. The primary FT I/O
   source itself does NOT assert independent output noise.
3. The initial input and partial output layers have joint-occupation bounds.
   The new signed-polymer covering argument gives Pr[A occupied]<=R^|A|;
   BDL witness counting then bounds endpoint logical errors. No long-time
   sparsity-transport theorem is assumed.
4. Nmu<=4pi restores the existing actual-state Gibbs envelope. The existing
   reference holding bound then applies. The FT comparison error is a
   diamond error before holding and does not acquire a factor 2^a. All
   short-stage work is polynomial in a and joins the existing all-d G3 bill.

Batch 10 completes the local endpoint prose integration in G.21 and the
author insert. It incorporates the controller gross-cost fix, the bounded
Pauli common-cause extension and the exact joint-kernel/residual criterion.
Read JOINT-ENDPOINT-KERNEL-CONSTRAINT-2026-10-27.md and the controller,
microscopic and bounded-jump notes in REPAIRS-2026-10-26. Three-jump reset
caps and a single-use label-reset latch give the stated gross O(s)
primitive invoice in that explicit device model; the installation must
supply their actual binding and fault treatment. The controller degree
remains 3 K_c+5, and the all-d G3 target is unchanged.

The original stage ceiling is epsilon/2^(a+2). Eight explicitly named
contributions receive at most one eighth each, including a joint residual
of at most epsilon/2^(a+5). A full stochastic-kernel comparison bounds it
by 2 TV; a retained-memory generator comparison bounds it by the integral
of its diamond norm. Preparation-only discrepancies are not multiplied by
2^a. Any residual still active during holding must be integrated over that
interval as well. No installation residual value is currently certified.
Bounded Pauli common causes are retained exactly; general local-stochastic
faults have not been replaced by independent output marginals. Known-rate
simulation and the O(1/n) rate-precision argument retain their model scope.

Run REPAIRS-2026-10-26/checks/verify-endpoint-join.py for fresh targeted
finite checks and source/hash verification. Its final receipt is
checks/ENDPOINT-FINAL-INTEGRATION-2026-10-27.json. This is separate from
canonical Checkpoint 12; it does not recompile the Lean canon.

BDL-REFINEMENT-CIRCUIT-2026-10-27.md constructs native CNOT code refinement.
Six seed/replacement cases and the 206-to-5116-qubit alternating step pass
full independent stabilizer replay. Reproducible gate lists and source hashes
are saved; the larger step is no longer only an unreproducible heredoc run.
Do not assume that composing bare refinements keeps fault spread constant.

Two development Lean candidates, NoiseCompensation and PauliInterface,
contain six statements each. Both have separate zero-output compile/kernel
PASS receipts and standard axioms only. They remain outside the canonical
192 modules / 1,158 names. Exact rational tests include all 4,096 joint
syndromes of the 13-qubit seed, unequal Pauli rates, perturbation bounds,
and the three-CNOT swap. The gauge-refresh complete-channel checks use
floating point and are explicitly distinguished from kernel proofs.

## Verification already finished

Checkpoint 11 was already PASS: 191 modules / 1,150 names. All 191 covered
sources still match it. Do not restart it as outstanding work.

Checkpoint 12 is now also PASS: all 192 modules freshly compiled and
kernel-checked, zero output, all 1,158 public names standard-axiom-audited,
strict completeness and claims gates PASS, current sources hash-matched.
Receipt: REPAIRS-2026-10-26/checks/snapshots/checkpoint-12-complete-transfer-bill/RESULT.json.

The only new canonical Lean source in this continuation is TransferRate:
eight statements for polynomial stage work, full retained prefixes,
complete failed-attempt invoices and the G3 join, including d=1. Every
other canonical Lean source is unchanged from checkpoint 11. These
accounting theorems do not assert the missing physical holding result.

## Retained direct-transport alternative and earlier patai

Read the current master for the full argument, as required by the standing
project instructions. Its G.21 now includes the source-audited ideal
sampler, the existing reference norm, a direct conversion for the actual
preparation E_a(I/2), initial syndrome sparsity, and the complete cost join.

The earlier direct-transport question and sources already followed are in:
REPAIRS-2026-10-26/PATAI-NEUTRAL-EXCURSION-CERTIFICATE-2026-10-26.md.

This remains an alternative sufficient route; the new compensated-output
construction above can avoid that long-time transport estimate. Do not
restart the old question as though no constructive progress has occurred.

A finite, valid zero-energy qubit flip crosses four single-defect hopping
regions. Its explicit preimages and reproducible script are recorded there.
It invalidates the proposed confinement sublemma, not the maximal target.
The author's replacement direct-history route still needs an actual
time-evolved occupation bound. Static decoder halving is not probability
decay in physical time. No spectral gap is required if the direct bound
can be proved. Initial logical error remains separately budgeted.

For any actual CPTP preparation E_a, omega_a=E_a(I/2), the derived
reference-uniform conversion is

    e(T)<=e_0+18 Lambda sqrt(T I_a(T)),
    I_a(T)=integral_0^T Tr[P_bad Phi_s(omega_a)]ds.

Initial/failure allocations and the original epsilon/2^(a+2) ceiling are
explicit in G.21. The norm bound Lambda=O(n) is derived in prose.
Do not label these prose derivations newly kernel-verified.

The author's later BCRD pointer led back to the existing G.8 construction:
`HamiltonianDecomposition.guarded_history_reduced_state` and the explicit
syndrome/reservoir exchange preserve the complete history, including arbitrary
reference correlations, under the specified factorised operation. This is
already kernel-checked. A direct physical application preserving the decoded
history algebra could bypass Gibbs domination; an occupation estimate is not
the only permitted route. The precise remaining source question is where the
actual noisy G.21 evolution is identified with that construction, including its
fault allowance. Read REPAIRS-2026-10-26/BCRD-HISTORY-BRIDGE-SOURCE-REVIEW.md
before asking for the algebra again. The pasted SLH/local-energy reconstruction
does not itself establish the identification or a global polynomial envelope.

The later active-correction candidate is reviewed in
REPAIRS-2026-10-26/ACTIVE-HOLDING-BRIDGE-CANDIDATE-REVIEW.md. The existing
Threshold/EdgeLaw/MatchingWitness route gives its corrected conditional
distance estimate; static HistoryPolymer histories are not physical fault
trajectories. The actual circuit must establish the branchwise quantum
correctness and witness/fault-law correspondence, and charge all 2^a recovery
cycles. Polynomial work per cycle is not polynomial work per age-stage. The
candidate does not yet close the full application or its all-d G3 bill.

## Completed independent work and later draft review

- G21-SOURCE-APPLICATION-AUDIT.md: the ideal full-history polymer sampler's
  source correspondence, uniform incidence and counting-theorem application.
- COMPLETE-TRANSFER-COST-JOIN.md: every account, all failed attempts,
  complete retained journal, startup and the pathwise G3 summation.
- INITIAL-SYNDROME-SPARSITY.md: character-expansion proof and exact checks.
- G3-HOSTILE-REVIEW-2026-10-26.md: the later three-stream/hostile-defense
  proposals, with corrections grounded in the actual compiled modules.
- GENERATOR-AND-TRANSIENT-RESOLVENT-AUDIT.md: norm, killed-process,
  exit-flux, Feynman–Kac and cited-source dispositions.
- Every author proposal is preserved verbatim under inputs/, with provenance.

Retain the existing stronger ledger. Expected reset cost is not its
pathwise upper bound. Stock is not cumulative write flux. Landauer gives
a lower heat bound, not a device-work upper bound. The existing exact
isometric algebra and reference recovery are already compiled; they need
not be requested again. Do not re-open settled X3/P1/P2.

## Review and release

Batch 10 shows the final endpoint/controller integration before and after;
batches 07–09 remain preserved. README, CITATION and REPAIR-STATUS carry the
192 / 1,158 PASS status. PDF/HTML/EPUB and SHA256SUMS remain older and are
explicitly not a seal of this draft. Review, rendering/resealing, merge and
publication have distinct statuses. The author's explicit word is still
required for merge/publication.

Other physical source/application statuses in the master remain explicit.
This continuation does not issue a global completion verdict.
