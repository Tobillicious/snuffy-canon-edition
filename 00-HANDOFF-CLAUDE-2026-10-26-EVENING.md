# Handoff — 26 October 2026, evening (Claude)

## Step one, before anything else

Read in full, not by search:
1. `00-HANDOFF-CLAUDE-2026-10-26.md` (Codex's handoff) and every file it names.
2. Codex's chat, `~/Downloads/codex 26 Oct.txt`, end to end. The author **rejected the
   Markov-chain mixing route** there and directed a **feed-forward** construction. G.21 is the
   author's tracked-decoding-history design.
3. Transcript of session 9d293ee6:
   - line 5984: the author's choice that protected content is the objective classical record and
     relations, with quantum coherence an open branch;
   - line 7382: the BCRD bridge fork, (a) or (b).
4. `REPAIRS-2026-10-26/PATAI-QUANTUM-TRANSFER-2026-10-26.md` — the morning's results. Do not
   re-derive monotonicity, the volume-law mismatch, or the Chesi extension (per-time bad weight).

Then state the state and wait for the author's OK.

## State

- Worktree `UPT-WARMSTART-WORKTREE`, branch `codex/upt-warmstart-bridge`, draft PR #9 stacked on
  #8. Not merged; nothing published.
- **Checkpoint 11: fresh full PASS, 191 modules / 1,150 names**
  (`REPAIRS-2026-10-26/checks/snapshots/checkpoint-11-history-polymer-reference/`).

## Codex's five items

1. **Audit G.21's source application** — not done. Check against `coarse.py` and
   `history_polymer.py`: local constraint equivalence, the uniform incidence bound, positive-polymer
   sampling and the dyadic branch budget.
2. **The noisy preparation join** — composed feed-forward from the named sources. It stops at a
   **pātai to the author**, the last section of `REPAIRS-2026-10-26/PATAI-NOISY-PREPARATION-2026-10-26.md`:
   - (a) the BCRD bridge;
   - (b) a holding theorem for "G.21 state plus a sparse residual fault layer";
   - (c) another construction of the author's.

   Awaiting the author's answer.
3. **The cost join to the G3 ledger** — not done. Candidate
   `REPAIRS-2026-10-26/claude-candidates/lean/Snuffy/TransferRate.lean` has compiled with zero
   output, but is not yet axiom-audited or kernel-checked, and is **not in the canon**. It proves
   that the stage-transfer bill is at most C·t with C independent of age. The full join must also
   carry the sampler's work, the retained random bits and the syndrome, controller and export
   records into the complete G3 ledger, pathwise.
4. **Checkpoint 11** — done.
5. **Prose batch 07** — awaiting the author's review. After that, the release metadata needs syncing:
   - `CITATION.cff` still says 189 / 1,133;
   - README and `REPAIR-STATUS` still say the audit is "in progress";
   - then re-render and re-seal.

## What this evening added, and what not to redo

- **Genuinely new:**
  - N1: no warm start survives a constant-rate final fault layer.
  - N2: domination survives the fault layer.
  - Lemma D: validity depends only on hop-component parities.
  - Lemma G: an isolated bounded region has a uniform gap.
  - Lemma T: the time union.
  - Hop regions are bounded: at most 4 at R_X levels, at most 72 at R_Z levels, with their number
    growing in n.
  - Path independence holds inside regions.
- **Repeats, not to be redone:** the bath-dynamics and relaxation routes (statement H, healing
  probes, BGL mixing). They repeat the mixing route the author rejected; see correction commit
  `3f70cc7`.
- The many Gemini dispositions are in `PATAI-NOISY-PREPARATION-2026-10-26.md` and
  `PATAI-FOR-GEMINI-R-2026-10-26.md`.

No merge, Zenodo or publication without the author's explicit word.
