# Pātai — the interacting fibres in the quantum warm-start sampler

26 October 2026. Worktree `codex/upt-warmstart-bridge`, based on `e291a99`.
The full maximal UPT proposition and the established gauntlet results remain
the target. This question concerns one support in the current quantum memory
construction; it does not propose a replacement proposition.

## What has been recovered and checked

The inherited checkpoint-09 receipt reports 189 modules / 1,133 names and PASS.
All 189 copied Lean sources match its source hashes. That is preservation of
existing verification, not a fresh compilation by Codex.

Claude's last unexecuted tool input was recovered from its local session and
preserved verbatim in `inputs/CLAUDE-LAST-UNEXECUTED-TRANSPORT-COMMAND.txt`.
Its deletion condition (Dec) asks: for every zero-excess fine syndrome with
two adjacent coarse defects y,z, deleting two occupied fine cells can leave
a member of D_y, and likewise a member of D_z. Here

    D_y = { sigma valid : |sigma| = 2, r(sigma) = e_y }.

The extension condition (Ext) asks that every member of D_y and D_z extend
by two occupied cells to a zero-excess syndrome in the two-defect fibre.

`checks/bdl-metacheck/transport.py` now enumerates all valid weight-four
syndromes of the 3 x 2 seed, rather than assuming that a local search window
contains every relevant syndrome. With the inherited deterministic map,
subdivision m=1 (ell=3), and PYTHONHASHSEED=0:

| Quantity | Result |
|---|---:|
| Valid weight-four syndromes checked | 204,772 |
| Adjacent coarse pairs | 7 |
| Zero-excess syndromes in those fibres | 1,475 |
| Dec failures | 103 |
| Ext failures | 0 |
| Zero-excess syndromes lacking a D_y / D_z product decomposition | 103 |
| Disjoint D_y / D_z products that leave the intended fibre | 139 |

These are finite results for the stated map and seed, not an all-level
theorem. The source hashes and witnesses are in
`checks/bdl-metacheck/TRANSPORT-3x2-GLOBAL.json`.

The first Dec witness has coarse support {(0,0),(0,1)} and fine-cell indices
{21,22,68,101} in that reproducible run. The result file includes semantic
cell labels. `verify_transport_witness.py` independently solves
delta(error)=sigma, checks all six two-cell subsets, and verifies that none
is a valid single-defect lift for either required defect. Its explicit
qubit-error preimage and subset results are in `TRANSPORT-WITNESS-CHECK.json`.

## Structural support that survives

The R_X cleaning corrections f_x and f_q read only the x and q pieces, not
the final z-pair coordinates. Thus, for a valid coarse increment xi,

    r(sigma + F(xi)) = r(sigma) + xi.

This is immediate from the four stages in BDL Theorem 4.7. Translation by
F(xi) is an involutive bijection between the corresponding full fibres and
changes at most 2|xi| fine syndrome bits. It does not preserve zero excess
in both directions.

In particular, let sigma have zero excess over s, and let xi be valid with
support disjoint from s. The weight bound gives

    2(|s|+|xi|) <= |sigma + F(xi)| <= |sigma|+2|xi|
                                      = 2(|s|+|xi|).

So extension by F(xi) preserves zero excess exactly. This proves the
corresponding extension property without a product assumption. Conversely,
deleting xi by that same translation can leave excess as large as 4|xi|;
it does not provide the missing zero-excess deletion condition.

## The precise support requested

For each actual R_X and R_Z step, with deterministic map r_i, define

    W_i(s) = sum_{r_i(sigma)=s} exp(-beta_i |sigma|)
           = exp(-2 beta_i |s|) Z_exc,i(s),
    pi_i^coarse(s) = W_i(s) / sum_u W_i(u).

Please supply a construction and uniform bound for sampling these
**interacting** fibres through all levels. The required output is an
explicit sampler, polynomial in the physical block size n, whose resulting
law satisfies

    mu_prep(sigma) <= C(n) pi_thermal(sigma),   C(n) <= A n^p,

with constants independent of recursion depth and age. A replacement
transport/cluster-expansion lemma is useful if it actually proves this
sampler bound for the interacting zero-excess configurations, rather than
assuming the failed product or deletion property. A different construction
meeting the same target is equally suitable.

For an exact fibre conditional K_i and a coarse proposal q_i, the identity is

    mu_i(sigma) / pi_i(sigma)
       = q_i(r_i(sigma)) / pi_i^coarse(r_i(sigma)).

Approximate conditionals add their one-sided pointwise factors. This is
the ratio that must stay polynomial. Sampling the unrenormalised coarse
Gibbs law, total-variation accuracy alone, and a local spectral gap do not
establish that bound.

The downstream obligations remain the original ones: logical transfer
preserves the full quantum state including reference correlations; stage
holding and transfer errors satisfy the existing summable schedule; and
preparation, correction, handoff, retirement, controllers and exports all
remain in the gross/pathwise bill. They are not removed by this question.

## Sources already followed

* The complete supplied Claude export and the actual failed final tool input.
* `STEP2-FINE-CONDITIONAL.md`, especially its conditional Hypothesis E.
* `PATAI-QUANTUM-TRANSFER-2026-10-26.md`, patai 2^5 through 2^9.
* The exact `bdl.py`, `coarse.py`, `hypothesis_e.py` and `product_range.py`
  construction and experiments.
* Balasubramanian–Davydova–Lin, arXiv:2605.10943, Theorem 4.7 and Lemmas
  4.8–4.14; its lifetime argument and explicit initialization discussion.
* Balasubramanian–Davydova–Lin–Thorngren, arXiv:2610.22548, as a recursive
  cluster-expansion model, with its classical scope retained.
* `WarmStart.lean`, `StageSchedule.lean`, and the current G.19 / G.20 argument.

Codex continues the independently available disintegration and composition
proofs while this support is requested. Global completion is not claimed.
