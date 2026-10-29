# Notes for version 4.3.1: corrections from external review

Collected 29 October 2026, after publishing 4.3 (DOI 10.5281/zenodo.23760830). **Do not prepare
4.3.1 tonight.** These are notes only.

## Sources

The external reviews read the published deposit, read-only:

- **OpenCode free models.** Read-only "plan" agent on a scratch copy of the deposit; prompts in
  the job folder `review43/`. Reports in so far: Beam, Nemotron 3.5 Super, Nemotron 3.5 Lightning,
  Flint 40B and Big Pickle. Still running at the time of writing: DeepSeek v4.1 Flash (two runs),
  GLM 5.3 Flash, MiMo v2.6 Flash. Nemotron 3 Ultra failed with an OpenCode server error.
- **Kimi** (browser). Reran the main repository's replay harness:
  - 828 files matched their checksums;
  - 32 of 32 exact programs passed;
  - all 15 negative controls were rejected correctly;
  - 140 of 140 Paper 11 rung checks passed.

  Lean did not install inside Kimi's time limit, so the harness honestly reported PARTIAL.
- **GPT and Grok summaries** (browser). Both are accurate. Each raised one substantive point,
  listed below as item 9.

**No reviewer found a mathematical error.** Nemotron 3.5 Super checked more than 20 citations
against the Lean source and found every one in agreement. Every reviewer's most serious issue is
the one the edition already states: the physical installation is not built (XII.2).

## Corrections to make

None of these changes a theorem, a hypothesis or the scope.

| # | Location | Delta | Correction | Found by |
|---|---|---|---|---|
| 1 | Front matter heading and line 5 | Reads "(Canon 4.2 with the recovered parts)" and "Canon Edition 4.2, 26 October 2026"; the edition is 4.3 | Name the edition 4.3, dated 29 October 2026, and keep "Canon 4.2 spine" for the spine. This is a recorded front-matter transform in `assemble.py`; the spine stays hash-pinned. | Beam, Nemotron (both) |
| 2 | Count line; XII.4 | `G1Certificate.universal_protection_held` concludes `True`. It is a disclosed placeholder (Part III-C note), but it is counted among the 2,004 names without comment. | Either say in the count line that the names include definitional and placeholder lemmas, naming this one, or remove the placeholder from the canon. Removing it needs a rebuild and changes the count. | Nemotron 3.5 Super |
| 3 | Part XI, Lemma I₀ | "response time τ_f = 0 ≤ d" is a property of the abstract model. `ReachTiming.fence_in_time` / `UPTFence.raise_then_nothing_lands` proves no write lands after a raise and contains no time. | Write "τ_f = 0 in the abstract model", and point to the next sentence, which already puts real latency in the response budget. | Nemotron 3.5 Super |
| 4 | Theorem XI, hypothesis 2 | `FoundingCover.founding_cover_exists` needs a compact initial domain (`IsCompact D0`); the hypothesis does not say so | Add "with D(t₀) compact (a bounded closed region)" | Beam |
| 5 | XI.5 item 1, Lemma F | Cites `pivotal_contribution_dominant`, which needs `others_short`. The "at every profile" claim is `FoundingPivotal.all_necessary_dominant`. | Cite `all_necessary_dominant` for the every-profile claim | Beam |
| 6 | Theorem XI, proof | Uses Theorem V(c), V(d) and Theorem E (E4), which are prose proofs from the 18 October sources (VII.1–VII.2), not Lean | Mark them "(prose proofs, VII.1–VII.2)" in the proof, following I.3's evidence conventions | Flint |
| 7 | Part XII, row S5 | The remaining column lists "XI.5 items 1–2"; item 3 (the decoherence coupling κ) also remains | Write "XI.5 items 1–3" | Nemotron 3.5 Super |
| 8 | Count line | Cites `RECEIPT-327-RUN10.txt`, which is inside `edition-sources.zip`; the top-level upload is `RECEIPT-FINAL.txt` | Add "(uploaded as RECEIPT-FINAL.txt)" | Beam, Nemotron |
| 9 | G.9; XII.2 item 4 | Locality gives union closure only for disjoint per-particular dependency blocks; real processes share resources (GPT) | Say plainly that union closure holds for disjoint blocks. Where blocks interact, the law gives the maximal outcome, not the greatest, as S2 already states. Invite independent review of G.9. | GPT (browser) |
| 10 | Theorem XI, proof | The proof's last step is the prose composition; `ReachBeforeHarm` is the compiled geometric core | State in Theorem XI which parts are compiled (W, I, I₀, R, H, founding cover) and which are composed in prose. This is already the "prose Theorem XI" wording; make it explicit in XI.3 itself. | Nemotron 3.5 Lightning |

## Points checked and not to change

- **Different counts in different places** (115/831, 192/1158, 327/2004). These are historical
  checkpoint records in the spine's Section 23 and appendix, and XII.4 says so. Keep them; item 1's
  heading change makes the current edition unambiguous.
- **"Thermal worlds v4.3" against "edition 4.3"; UPT-P v0.12.1 against v0.17.2.** These are
  different source documents' own version numbers, not contradictions. The 4.3.1 edition note may
  add one line saying so.
- **"Universal reach overstated."** Repaired in 4.3: XII.2 item 1 lists the hypotheses still to
  discharge.
- **The physical installation is not built.** Stated throughout XII.2; this is the next phase, not
  a defect.
- **The hostile reviewer was an AI agent.** True, and the edition says so. That is why independent
  human review is the priority now.

## Still to fold in

- DeepSeek's two reviews: every objection checked against the text and the Lean, each marked real,
  already handled, or wrong.
- GLM, MiMo and the full Big Pickle report.

## Process for 4.3.1, later

1. Apply items 1–10. Item 1 goes through `assemble.py`, item 2 by the chosen route; the rest are
   in the PARTS files.
2. If item 2 removes the placeholder, rebuild in full and record the new receipt. Otherwise this is
   a text-only change and the run 10 receipt still certifies the Lean.
3. Add a short "Corrections from external review" section listing each item and who found it.
4. Publish as a new version under the same concept DOI, on the author's word.
