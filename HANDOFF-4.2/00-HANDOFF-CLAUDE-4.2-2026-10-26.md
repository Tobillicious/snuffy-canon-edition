# Claude handoff — Snuffy 4.2, 26 October 2026 (session limit)

Read AGENTS.md and this file first. Everything is in git: repo `snuffy-canon-edition`,
branch `canon-v4.2-working`, draft PR #7 (main = published 4.1, untouched).

## State
- Canon (SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25/lean): 167 modules / 1,029 names.
  Last PASS receipt: BANKS/2026-10-25-historical-handoff-source/RECEIPT-166-INCREMENT.txt
  (157 fresh full run + 9 fresh). ConcatenatedDecoding (module 167) compiled, kernel-checked,
  standard axioms; a single fresh full 167-module build was running at stand-down
  (writes lean/RECEIPT.txt; build dir job tmp/build167). Rerun it if RECEIPT.txt lacks "overall".
- Banked, NOT yet in canon: BANKS/2026-10-25-historical-handoff-source/cited-small/lean/Snuffy/
  ChannelCP.lean (completed decoder completely positive for every reference) and
  PureStateTraceNorm.lean (pure-state trace-distance identity). Both zero output, kernel-checked.
- Master: G.8–G.15 appended; batches B–G applied (author-approved); G4 derived via
  ConcatenatedDecoding and applied. Counts in master/README/CITATION/zenodo.json say 166/1,025:
  update to the final count.

## Next, in order
1. Add ChannelCP and PureStateTraceNorm to lean/Snuffy and MODULES (169 modules), gen-index.py,
   one fresh full build-and-audit (MATHLIB_PROJECT=BEAM-UPT-2026-10-22/mathlib-probe,
   CORPUS_ROOT=Snuffy-Book). Require overall PASS.
2. Manuscript: update counts (header line 11, §23 lead, appendix: "All N modules ... in one run");
   §23.9 rows for ConcatenatedDecoding, ChannelCP, PureStateTraceNorm; in G.13 replace "That
   standard fact is cited" (CP) and "which is cited" (pure-state identity) with the compiled
   theorems; §23.8 cited list now: surface-code chain lemma, Solovay–Kitaev (with Nielsen–Chuang
   §4.5), AGP fault-tolerant syndrome gadgets. Add the hypothesis-match table for those three
   (drafted reasoning: DKLP counting needs only P(set faulty) ≤ p^|S| = LocalStochastic; SK in
   operator norm feeds ErrorBudget's ε/m; AGP's model is local stochastic noise, threshold constant
   from exRec location count, not 1/21). Show any rewrite of existing prose to the author first.
3. Re-render (checks/render.sh), verify (checks/verify_render.py; update module_count needle),
   SHA256SUMS over the release folder, fill counts in zenodo.json/CITATION.cff/README.md.
4. Commit, push, merge PR #7 (author authorised "merge when ready").
5. Zenodo: stage a draft new version of 10.5281/zenodo.23631881 (dataset, include
   LEDGER-FOUR-STROKE-2026-10-24, no doors; token ~/.zenodo-token). Publish only on the
   author's word, after he reads the description.
6. 4.3 track: compile the surface-code chain lemma, Solovay–Kitaev, AGP.
