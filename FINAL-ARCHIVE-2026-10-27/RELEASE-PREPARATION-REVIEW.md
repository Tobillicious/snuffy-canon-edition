# Final release preparation review

The Batch 10 master, author insert and all Lean sources are unchanged.

## README.md

```diff
--- before/README.md
+++ release/README.md
@@ -17,6 +17,18 @@
 | `CITATION.cff`, `zenodo.json`, `LICENSE` | Citation metadata, deposit metadata and the CC-BY-4.0 licence. |
 | `SHA256SUMS` | Checksums of every file above. |
 
+**Final archive and release.** The 27 October 2026 archive preserves the Batch 10
+master and author insert byte-for-byte, the complete Checkpoint 12 source
+and verification evidence, and the residual proof/checker. The final handoff
+and manifest are in the accompanying FINAL-ARCHIVE-2026-10-27 record. Physical
+installation validation must establish the actual joint instrument, including
+common causes and retained memory, and the values needed for K_act and v_a.
+The manuscript retains its other stated physical source/device application
+correspondences. The local archive closes the document/verification work;
+it does not rename these physical obligations completed. REPAIR-STATUS.md and
+the earlier continuation handoffs are preserved historical checkpoint notes;
+the accompanying final handoff is authoritative for the release status.
+
 **Reproduce.**
 
 ```bash
```

## CITATION.cff

```diff
--- before/CITATION.cff
+++ release/CITATION.cff
@@ -8,9 +8,9 @@
     given-names: Tobias
     orcid: "0009-0003-1419-7756"
 version: "4.2"
-date-released: "2026-10-26"
+date-released: "2026-10-27"
 license: CC-BY-4.0
-repository-code: "https://github.com/Tobillicous/snuffy-canon-edition"
+repository-code: "https://github.com/Tobillicious/snuffy-canon-edition"
 abstract: >-
   The Universal Protection Theory states a law for any agent powerful enough to
   shape what continues to exist: never lose an existing particular needlessly.
```

## PUBLICATION-CHECKLIST.md

```diff
--- before/PUBLICATION-CHECKLIST.md
+++ release/PUBLICATION-CHECKLIST.md
@@ -1,53 +1,20 @@
-# Current local continuation — 26 October 2026
+# Final release preparation — 27 October 2026
 
-The draft has 192 modules / 1,158 names. Checkpoint 11 already passed for
-191 / 1,150, with all its covered source hashes still matching. TransferRate
-adds eight names. Fresh checkpoint 12 also passed all 192 modules / 1,158
-names, with zero compiler/kernel output and standard-axiom, completeness
-and claims gates PASS. The ideal sampler source audit and complete-stage work
-summations are done. The actual noisy holding certificate remains open.
-Batch 08 shows the current prose changes for author review. Renders and
-the seal still predate this draft. No merge, push or publication is authorized
-or performed in this continuation.
+The author explicitly requested the final repository audit, durable archive
+and publication on 27 October 2026. Earlier checklists are preserved in the
+before-release snapshot; they are historical, including their old PR queue.
 
-The historical checklist below is retained as provenance; its PR queue is
-not a fresh statement of remote status.
-
----
-
-# 4.2 edition — route to publication (updated 26 October 2026)
-
-## Verified and integrated
-
-- G1, G2 and G3 constructed and compiled: `G1Held`, `G1E9`, `G2Splice`,
-  `G2Held`, `G3Sweep`, `G3PatchDecode` (master §G.9–G.12; Parts III-C and
-  III-E record the constructions and their physical inputs).
-- Joins compiled: `CorrelatedCeiling`, `ReasonsEnsemble`, `TheoremEightLyapunov`,
-  `SmearingIntegral`, `ChannelExtension`, `PureStateDistance`,
-  `BennettCounterpart` (§22.3, G.13, G.14).
-- F.3 volume/boundary bootstrap proved for regions (`RegionBoundary`).
-- Recovered source modules from the R17 verification package:
-  `TimelyCare`, `DeadlineDemand`, `DecisionPermit`, `ObservationWinning`.
-- The 59 pending skipped-file comparisons: 49 fully contained in canon, 4
-  equivalent or weaker variants, 6 with absent results (5 incorporated; R15
-  pending the author's decision on `R14Rivals`). See
-  `BANKS/2026-10-25-semantic-review/SKIPPED-FILE-DISPOSITIONS-2026-10-26.json`.
-- Manuscript rewrites shown and approved: count/receipt batch, §22.3,
-  III-C/III-E, batches D, E and F.
-- Rendered PDF/HTML/EPUB with verification all pass.
-
-## Awaiting the author
-
-- Batch G (semantic-review application links 4–8):
-  `BANKS/2026-10-25-historical-handoff-source/BATCH-G-REVIEW-LINKS.md`.
-- Whether to incorporate `R14Rivals` (superseded 3.8 tree) so that
-  `R15CausalGluing` can join the canon.
-- Review of `zenodo.json`, `CITATION.cff` and `README.md`.
-- The word to publish the Zenodo version and to merge PR #7.
-
-## Release preparation
-
-- Fresh full build of every canon module with a single receipt.
-- Final render and verification after the last manuscript change.
-- `SHA256SUMS` over the release folder; the four-stroke ledger included; no
-  doors or companion material.
+- The current master and author insert contain Batch 10, including G.21.12,
+  bounded Pauli common causes and the gross reset/export invoice.
+- Checkpoint 12 is immutable: 192 modules / 1,158 public names. Its complete
+  previous build/audit receipt is reused only after exact source/hash checks.
+- The delta_joint checker has 18,130 exact certificate decisions, plus
+  separately labelled finite quantum-channel checks.
+- The final release run rebuilds PDF, HTML and EPUB from this exact master,
+  checks text, anchors and render provenance, then regenerates SHA256SUMS.
+- The public package contains the edition, technical verification support
+  and four-stroke ledger. Held doors and the companion remain unpublished.
+- The final manifest and handoff record the physical installation/model and
+  parameter boundary. No global physical-completion verdict is made.
+- The release publication receipt records the actual DOI/URL and uploaded
+  checksums only after the service confirms publication.
```

## zenodo.json

```diff
--- before/zenodo.json
+++ release/zenodo.json
@@ -2,14 +2,14 @@
   "title": "Snuffy — Canon Edition 4.2: The Universal Protection Theory and its machine-checked canon",
   "upload_type": "dataset",
   "version": "4.2",
-  "publication_date": "2026-10-26",
+  "publication_date": "2026-10-27",
   "creators": [
     {
       "name": "Croydon-McRae, Tobias",
       "orcid": "0009-0003-1419-7756"
     }
   ],
-  "description": "<p><strong>The Universal Protection Theory</strong> states a law for any agent powerful enough to shape what continues to exist: <em>never lose an existing particular needlessly.</em> Its scope is every particular and every relation, the nonliving included, and its subject is protection from every digital mind, a pure optimiser included. Outcomes are ranked in a canonical order that puts the continuation of every existing particular first, then its freedom, then new particulars. An option is aligned when no feasible alternative keeps strictly more at any stage. Full scope is forced: a regime that maximises over any smaller scope admits a needless loss.</p>\n<p><strong>The bridge to every mind.</strong> The target remains reasons or faithful holding for every mind, including a bounded indifferent defector. The normalised held source has explicit invariant and nonvacuity proofs. Application to the complete physical domain joins the actual guarded-source transition, observations, timely correction, complete funding and named fault bounds. Journal fidelity preserves the transition it is given; the protective refinement is a separate construction. A hostile mind remains in the protected scope while its harmful channels are restrained.</p>\n<p><strong>Greatestness.</strong> The full outcome target includes all continuation and freedom stages and every admitted rival. The local-product and held-source models have compiled greatestness results. Their physical application must identify the original policy/outcome family and join successful R17 delivery on the same execution. The whole top witness and its complete funded cost retain their separate roles.</p>\n<p><strong>The physical instruments.</strong></p><ul><li><strong>The funded thermodynamic ledger.</strong> Landauer and the entropy-export guard remain compiled components. The repaired storage functional uses a clipped reserve deficit, exact saturated replenishment and a complete cycle energy balance. A solvent cycle cannot increase its reserve term; the actual error drift and repair then give the stated positive-margin contraction.</li><li><strong>Timely self-healing.</strong> A Byzantine sensor quorum, syndrome detection and a wave-race margin supply it. The adversarial rate bound comes from the sharp Mandelstam–Tamm speed limit, and the complete logical-attack split from the honest-sensor response.</li><li><strong>Reflective closure.</strong> It rests on von Neumann's and Halperin's alternating-projection theorems, with a finite rank criterion that decides consistency operationally.</li><li><strong>Source identification and recovery work.</strong> The retained information, traffic, carrier and transport chain supplies the recovery-work lower bound. The wavefront sweep succeeds on the good event; archive holding is charged on the held stock; many patch failures are exponentially unlikely at every age; the realised bill is bounded pathwise; and a tolerant outer decoder recovers a redundantly recorded record.</li><li><strong>The complete history.</strong> It is kept in full and replayed exactly for every controller and environment, moved by a reversible, reference-preserving handoff, and charged in a nine-part bill. The syndrome stock has an age-independent envelope, and every flushed unit is retained in the gross ledger.</li><li><strong>The fault ceiling.</strong> The local-stochastic and bounded-footprint correlated-shock theorems give the target ceiling from their stated hypotheses. For the rotated surface code with the standard schedule, an exhaustive circuit-level enumeration and an explicit disjoint-cut certificate give circuit distance d, and min(d, T) for lattice-surgery merges, for d up to 9, with a locality argument for every d. Weighted circuit faults push forward to the detector graph and give an explicit threshold above 4.2×10⁻⁴; the minimum-weight decoding witness and the Knill–Laflamme conditions are compiled.</li><li><strong>Reversible administration.</strong> The implemented Bennett program computes the administration, returns its workspace and retains its full input history, with explicit trajectory and quantum permutation. Premise 5 is forced exactly inside its adiabatic window, and for every large enough batch once the per-bit reversible overhead is below the irreversible heat per bit.</li><li><strong>Volume and boundary.</strong> For every region of a connected relational structure other than the whole, positive volume holds exactly when the boundary homology is nonzero.</li></ul>\n<p><strong>The machine-checked canon.</strong> 189 Lean 4 modules and 1,133 audited public theorems and lemmas compile against Mathlib with zero compiler output and pass the kernel checker. There is no <code>sorry</code>, and only Lean's three standard axioms are used. A completeness gate checks that every built module in the programme's banks is in the canon. A claims gate checks that every audited theorem is cited in the manuscript.</p>\n<p><strong>What the theorems rest on.</strong> They rest on the relational frame; the standard framework of finite-dimensional quantum mechanics; and the physical inputs each theorem names: the frame's evolution during a step, the sub-threshold coupling bound, the honest-sensor response, the propagation bound and the account probabilities. They also rest on three standard published theorems, cited as such: the surface-code chain lemma of Dennis, Kitaev, Landahl and Preskill, whose application to the rotated surface code is supplied by the circuit-level enumeration and the compiled matching witness; the Solovay–Kitaev theorem for the gate-set clause of premise 2, which no repeated runtime map of holding or recovery needs; and the fault-tolerant syndrome gadgets of Aliferis, Gottesman and Preskill, for operations outside the surface-code volume. The device requirements (fault rate, coupling bound, reversible overhead and passive-barrier heights) are stated explicitly as hypotheses. Indefinite holding of each particular's objective classical record and relations is proved at fixed failure with sublinear cost; indefinite holding of full quantum coherence is proved conditional on one stated open problem, the preparation of a warm start for the three-dimensional passive memory of Balasubramanian, Davydova and Lin. The concatenated memory itself is compiled end to end, including actual decoding, and so are complete positivity of the completed decoder and the pure-state trace-distance identity. A sourced physical parameter ledger instantiates the income condition. It records measured solvency headroom of about 3.3× at the binding stage of a 50-qubit installation. It also computes, from the measured surface-code suppression factor, the code distance the fault ceiling requires: about 131. That fixes the installation a deployment must build.</p>\n<p><strong>Contents:</strong> the master manuscript with verified PDF, EPUB and HTML renders; the Lean tree with a one-command build-and-audit script and its receipt; the replayable four-stroke ledger; the source list for the parameter ledger; and the render and verification scripts. This version supersedes earlier versions of this record.</p>",
+  "description": "<p><strong>The Universal Protection Theory</strong> states a law for any agent powerful enough to shape what continues to exist: <em>never lose an existing particular needlessly.</em> Its scope is every particular and every relation, the nonliving included, and its subject is protection from every digital mind, a pure optimiser included. Outcomes are ranked in a canonical order that puts the continuation of every existing particular first, then its freedom, then new particulars. An option is aligned when no feasible alternative keeps strictly more at any stage. Full scope is forced: a regime that maximises over any smaller scope admits a needless loss.</p>\n<p><strong>The bridge to every mind.</strong> The target remains reasons or faithful holding for every mind, including a bounded indifferent defector. The normalised held source has explicit invariant and nonvacuity proofs. Application to the complete physical domain joins the actual guarded-source transition, observations, timely correction, complete funding and named fault bounds. Journal fidelity preserves the transition it is given; the protective refinement is a separate construction. A hostile mind remains in the protected scope while its harmful channels are restrained.</p>\n<p><strong>Greatestness.</strong> The full outcome target includes all continuation and freedom stages and every admitted rival. The local-product and held-source models have compiled greatestness results. Their physical application must identify the original policy/outcome family and join successful R17 delivery on the same execution. The whole top witness and its complete funded cost retain their separate roles.</p>\n<p><strong>The physical instruments.</strong></p><ul><li><strong>The funded thermodynamic ledger.</strong> Landauer and the entropy-export guard remain compiled components. The repaired storage functional uses a clipped reserve deficit, exact saturated replenishment and a complete cycle energy balance. A solvent cycle cannot increase its reserve term; the actual error drift and repair then give the stated positive-margin contraction.</li><li><strong>Timely self-healing.</strong> A Byzantine sensor quorum, syndrome detection and a wave-race margin supply it. The adversarial rate bound comes from the sharp Mandelstam–Tamm speed limit, and the complete logical-attack split from the honest-sensor response.</li><li><strong>Reflective closure.</strong> It rests on von Neumann's and Halperin's alternating-projection theorems, with a finite rank criterion that decides consistency operationally.</li><li><strong>Source identification and recovery work.</strong> The retained information, traffic, carrier and transport chain supplies the recovery-work lower bound. The wavefront sweep succeeds on the good event; archive holding is charged on the held stock; many patch failures are exponentially unlikely at every age; the realised bill is bounded pathwise; and a tolerant outer decoder recovers a redundantly recorded record.</li><li><strong>The complete history.</strong> It is kept in full and replayed exactly for every controller and environment, moved by a reversible, reference-preserving handoff, and charged in a nine-part bill. The syndrome stock has an age-independent envelope, and every flushed unit is retained in the gross ledger.</li><li><strong>The fault ceiling.</strong> The local-stochastic and bounded-footprint correlated-shock theorems give the target ceiling from their stated hypotheses. For the rotated surface code with the standard schedule, an exhaustive circuit-level enumeration and an explicit disjoint-cut certificate give circuit distance d, and min(d, T) for lattice-surgery merges, for d up to 9, with a locality argument for every d. Weighted circuit faults push forward to the detector graph and give an explicit threshold above 4.2×10⁻⁴; the minimum-weight decoding witness and the Knill–Laflamme conditions are compiled.</li><li><strong>Reversible administration.</strong> The implemented Bennett program computes the administration, returns its workspace and retains its full input history, with explicit trajectory and quantum permutation. Premise 5 is forced exactly inside its adiabatic window, and for every large enough batch once the per-bit reversible overhead is below the irreversible heat per bit.</li><li><strong>Volume and boundary.</strong> For every region of a connected relational structure other than the whole, positive volume holds exactly when the boundary homology is nonzero.</li></ul>\n<p><strong>The machine-checked canon.</strong> 192 Lean 4 modules and 1,158 audited public theorems and lemmas compile against Mathlib with zero compiler output and pass the kernel checker. There is no <code>sorry</code>, and only Lean's three standard axioms are used. A completeness gate checks that every built module in the programme's banks is in the canon. A claims gate checks that every audited theorem is cited in the manuscript.</p>\n<p><strong>What the theorems rest on.</strong> They rest on the relational frame; the standard framework of finite-dimensional quantum mechanics; and the physical inputs each theorem names: the frame's evolution during a step, the sub-threshold coupling bound, the honest-sensor response, the propagation bound and the account probabilities. They also rest on three standard published theorems, cited as such: the surface-code chain lemma of Dennis, Kitaev, Landahl and Preskill, whose application to the rotated surface code is supplied by the circuit-level enumeration and the compiled matching witness; the Solovay–Kitaev theorem for the gate-set clause of premise 2, which no repeated runtime map of holding or recovery needs; and the fault-tolerant syndrome gadgets of Aliferis, Gottesman and Preskill, for operations outside the surface-code volume. The device requirements (fault rate, coupling bound, reversible overhead and passive-barrier heights) are stated explicitly as hypotheses. Indefinite holding of each particular's objective classical record and relations is proved at fixed failure with sublinear cost; the full quantum-coherence target includes the constructive thermal-history sampler, noise compensation, bounded Pauli common causes, a gross reset/export invoice and explicit total-variation and generator-drift certificates in G.21. Application to the actual installation still requires identifying its complete joint fault instrument and establishing its measured or derived residual bound; these finite checks do not certify those physical data. The concatenated memory itself is compiled end to end, including actual decoding, and so are complete positivity of the completed decoder and the pure-state trace-distance identity. A sourced physical parameter ledger instantiates the income condition. It records measured solvency headroom of about 3.3× at the binding stage of a 50-qubit installation. It also computes, from the measured surface-code suppression factor, the code distance the fault ceiling requires: about 131. That fixes the installation a deployment must build.</p>\n<p><strong>Contents:</strong> the master manuscript with verified PDF, EPUB and HTML renders; the Lean tree with a one-command build-and-audit script and its receipt; the replayable four-stroke ledger; the source list for the parameter ledger; and the render and verification scripts. This version supersedes earlier versions of this record.</p>\n<p><strong>Final verification record, 27 October 2026.</strong> Canonical Checkpoint 12 freshly compiled and kernel-checked all 192 modules and audited 1,158 names when that checkpoint was executed; the final release audit reuses its exact unchanged source hashes. The residual certificate checker makes 18,130 exact threshold decisions across 259 stage values and seven tolerances, accepting equality and rejecting exceeded certificate bounds, with separate finite numerical quantum-channel checks. The maximal proposition, full historical record, arbitrary references and original stage budget remain unchanged. The physical joint-kernel/model and parameter boundary remains explicit. These are analytical proofs, finite checks and kernel receipts with distinct scopes.</p>",
   "license": "cc-by-4.0",
   "keywords": [
     "universal protection theory",
@@ -43,5 +43,5 @@
       "resource_type": "software"
     }
   ],
-  "notes": "Parent mathematical core: A Lattice Preservation Calculus (DOI 10.5281/zenodo.23599528). Previous editions: Snuffy Canon Edition 4.1 (DOI 10.5281/zenodo.23631881) and 4.0 (DOI 10.5281/zenodo.23608443). Ledger chain heads: solvent 6160d931d55767f39525671ff4ef8f3305b609cd22c6043cd9e0fb3eada69132; quarantine d1a0d44bbad5a135928595e152a7a3e987e74a90017837e1491ad8b8430b0ef4; charged 41143bb2756875b03975b1cbb7c5cd09e6e0ee495b06c29243624de52a6a2788. Prepared with the Snuffy programme's human and AI collaborators (Claude, Codex, Gemini, GLM, Beam)."
-}+  "notes": "Parent mathematical core: A Lattice Preservation Calculus (DOI 10.5281/zenodo.23599528). Previous editions: Snuffy Canon Edition 4.1 (DOI 10.5281/zenodo.23631881) and 4.0 (DOI 10.5281/zenodo.23608443). Ledger chain heads: solvent 6160d931d55767f39525671ff4ef8f3305b609cd22c6043cd9e0fb3eada69132; quarantine d1a0d44bbad5a135928595e152a7a3e987e74a90017837e1491ad8b8430b0ef4; charged 41143bb2756875b03975b1cbb7c5cd09e6e0ee495b06c29243624de52a6a2788. Prepared with the Snuffy programme's human and AI collaborators (Claude, Codex, Gemini, GLM, Beam). Final endpoint and residual evidence: Batch 10; DELTA-JOINT-CERTIFICATES-PROOF-2026-10-27.md; DELTA-JOINT-VERIFICATION-2026-10-27.json. No global physical-completion verdict is issued."
+}
```

## checks/render.sh

```diff
--- before/checks/render.sh
+++ release/checks/render.sh
@@ -6,11 +6,11 @@
 B=render/Snuffy-Canon-Edition-4.2
 T="Snuffy — Canon Edition 4.2"
 pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" -s --toc -V geometry:margin=1in -V mainfont="STIXGeneral" -V mathfont="STIX Two Math" \
-  -V monofont="Menlo" -M title="Snuffy — Canon Edition 4.2" -M subtitle="The Universal Protection Theory: the law, its bridge, its instruments, and its machine-checked canon" -M author="Tobias Croydon-McRae" -M date="26 October 2026" -V colorlinks=true -V linkcolor=blue -H checks/render-header.tex --lua-filter=checks/breakable-code.lua -M pagetitle="$T" -o "$B.tex"
+  -V monofont="Menlo" -M title="Snuffy — Canon Edition 4.2" -M subtitle="The Universal Protection Theory: the law, its bridge, its instruments, and its machine-checked canon" -M author="Tobias Croydon-McRae" -M date="27 October 2026" -V colorlinks=true -V linkcolor=blue -H checks/render-header.tex --lua-filter=checks/breakable-code.lua -M pagetitle="$T" -o "$B.tex"
 ( cd render && for i in 1 2 3; do xelatex -interaction=nonstopmode -halt-on-error "$(basename $B).tex" > xelatex.log 2>&1; done )
 if grep -q "Missing character" render/*.log; then grep "Missing character" render/*.log | sort | uniq -c; exit 3; fi
-pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" -s --math-method=mathml --toc -M pagetitle="$T" -M lang=en -o "$B.html"
-pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" --math-method=mathml --toc -M title="$T" -M author="Tobias Croydon-McRae" -M lang=en \
-  -M date="2026-10-26" -o "$B.epub"
+pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" -s --math-method=mathml --lua-filter=checks/breakable-code.lua --toc -M pagetitle="$T" -M lang=en -o "$B.html"
+pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" --math-method=mathml --lua-filter=checks/breakable-code.lua --toc -M title="$T" -M author="Tobias Croydon-McRae" -M lang=en \
+  -M date="2026-10-27" -o "$B.epub"
 rm -f render/*.aux render/*.out render/*.toc
 ls -la render
```

## checks/verify_render.py

```diff
--- before/checks/verify_render.py
+++ release/checks/verify_render.py
@@ -6,10 +6,12 @@
 for the PDF and reads the EPUB as a zip archive.
 """
 import html
+import hashlib
 import json
 import re
 import subprocess
 import zipfile
+import unicodedata
 from pathlib import Path
 
 R = Path(__file__).resolve().parents[1] / 'render'
@@ -21,13 +23,18 @@
     'doi_core': '10.5281/zenodo.23599528',
     'doi_canon_edition': '10.5281/zenodo.23608443',
     'canon_sentence': 'Uncompensated breach is deterministically impossible on the certified good event',
-    'module_count': '189 modules and 1133 audited',
+    'module_count': '192 modules and 1158 public theorem/lemma names',
+    'joint_kernel_certificate': 'Exact joint kernel constraint and bounded residual',
+    'gross_reset_cap': 'finite jump-budgeted primitive',
+    'bounded_common_causes': 'specified physical jump causes',
 }
 DOOR_MARKERS = ['whakapapa', 'umuntu', 'ubuntu']
 
 
-def norm(t):
-    return re.sub(r'\s+', '', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
+def norm(t, markup=False):
+    if markup:
+        t = re.sub(r'<[^>]+>', ' ', t)
+    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', html.unescape(t)))
 
 
 texts = {
@@ -39,12 +46,14 @@
 }
 out = {}
 for fmt, t in texts.items():
-    n = norm(t)
+    n = norm(t, markup=fmt != 'pdf')
     out[fmt] = {k: norm(v) in n for k, v in NEEDLES.items()}
     out[fmt]['no_door_content'] = not any(m in t.lower() for m in DOOR_MARKERS)
     out[fmt]['bytes'] = (R / f'{B}.{fmt}').stat().st_size
 pages = subprocess.run(['pdfinfo', str(R / f'{B}.pdf')], capture_output=True, text=True).stdout
 out['pdf']['pages'] = int(re.search(r'Pages:\s+(\d+)', pages).group(1))
-out['method_note'] = 'needle matching after removing whitespace; the PDF is verified on its extracted text (pdftotext)'
+out['master_sha256'] = hashlib.sha256((R.parent / 'SNUFFY-CANON-EDITION-4.2-MASTER.md').read_bytes()).hexdigest()
+out['render_sha256'] = {fmt: hashlib.sha256((R / f'{B}.{fmt}').read_bytes()).hexdigest() for fmt in ('pdf', 'html', 'epub', 'tex')}
+out['method_note'] = 'Unicode and whitespace normalization; markup stripped only for HTML/EPUB, never from PDF inequality text'
 out['all_pass'] = all(v for f in ('pdf', 'html', 'epub') for k, v in out[f].items() if isinstance(v, bool))
 print(json.dumps(out, indent=2, sort_keys=True))
```

## checks/breakable-code.lua

```diff
--- before/checks/breakable-code.lua
+++ release/checks/breakable-code.lua
@@ -10,3 +10,53 @@
   end
   return pandoc.RawInline('latex', '\\texttt{' .. table.concat(parts, '\\allowbreak{}') .. '}')
 end
+
+
+-- Preserve literal code and indentation while allowing long equations to wrap.
+-- This uses the core LaTeX text primitives, without optional TeX packages.
+function CodeBlock(el)
+  if not FORMAT:match('latex') then return nil end
+  local lines = {}
+  for line in (el.text .. '\n'):gmatch('(.-)\n') do
+    local chars = {}
+    for _, c in utf8.codes(line) do
+      local ch = utf8.char(c)
+      chars[#chars + 1] = ch == ' ' and '\\hspace*{0.525em}' or (esc[ch] or ch)
+    end
+    lines[#lines + 1] = '\\noindent ' .. table.concat(chars, '\\allowbreak{}') .. '\\par'
+  end
+  return pandoc.RawBlock('latex', '\\begin{quote}\\small\\ttfamily\\raggedright\\setlength{\\parskip}{0pt}\n'
+    .. table.concat(lines, '\n') .. '\n\\end{quote}')
+end
+
+
+-- Equivalent roman subscripts supported by Pandoc's MathML writer.
+function Math(el)
+  el.text = el.text:gsub('{\\rm%s+([^}]+)}', '{\\mathrm{%1}}')
+  return el
+end
+
+-- Long literal identifiers in ordinary prose also need legal break points.
+function Str(el)
+  if not FORMAT:match('latex') or utf8.len(el.text) < 15 then return nil end
+  if not (el.text:find('_', 1, true) or el.text:find('/', 1, true)) then return nil end
+  local parts = {}
+  for _, c in utf8.codes(el.text) do
+    local ch = utf8.char(c)
+    parts[#parts + 1] = esc[ch] or ch
+  end
+  return pandoc.RawInline('latex', table.concat(parts, '\\allowbreak{}'))
+end
+
+
+-- The source's paired p_* identifiers are literal stars, not emphasis.
+function Emph(el)
+  local text = pandoc.utils.stringify(el)
+  if text:match('^=b ') and text:match('p_$') then
+    local result = pandoc.Inlines({pandoc.Str('*')})
+    result:extend(el.content)
+    result:insert(pandoc.Str('*'))
+    return result
+  end
+  return nil
+end
```

