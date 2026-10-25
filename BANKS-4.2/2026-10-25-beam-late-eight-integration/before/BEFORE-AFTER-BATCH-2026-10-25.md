# BEFORE/AFTER BATCH — master and §23 to the compiled state (25 October 2026)

*For the author's decision, per the rule: canon prose is never silently rewritten; every rewrite goes to you as before/after in one batch. Items marked **[PASS-gated]** land only after the 111-module strict audit returns overall PASS and RECEIPT.txt is committed. New additions (append-only) are marked **[append-only]**; rewrites of existing sentences are marked **[rewrite]**.*

---

## 1. The module count — three places in `checks/assemble_master.py` **[PASS-gated] [rewrite]**

**1a. FRONT matter (script line 48):**

> BEFORE: … It also adds **the machine-checked canon**: forty-one Lean modules that compile against Mathlib with no `sorry` and only Lean's standard axioms. …
>
> AFTER: … It also adds **the machine-checked canon**: one hundred and eleven Lean modules that compile against Mathlib with no `sorry` and only Lean's standard axioms. …

**1b. NOTE_I3 (the I.3 status note):**

> BEFORE: … forty-one Lean modules compiled against Mathlib rev `56a005855ea1`, each with exit 0, zero compiler output and `leanchecker` passing …
>
> AFTER: … one hundred and eleven Lean modules compiled against Mathlib rev `56a005855ea1`, each with exit 0, zero compiler output and `leanchecker` passing …

**1c. APPENDIX_41 (the appendix paragraph):**

> BEFORE: **The machine-checked canon.** Forty-one Lean modules (`lean/Snuffy/` of the 4.1 tree) build against Mathlib rev `56a005855ea1` on Lean 4.35.0 with one command, `lean/build-and-audit.sh`. …
>
> AFTER: **The machine-checked canon.** One hundred and eleven Lean modules (`lean/Snuffy/`) build against Mathlib rev `56a005855ea1` on Lean 4.35.0 with one command, `lean/build-and-audit.sh`. The script compiles every module in dependency order and requires exit 0 with zero compiler output. It runs `leanchecker` on each module, scans the sources for `sorry`, `admit` and `axiom`, and prints the axioms of every headline theorem. The completeness gate checks that every module built in the banks is present in the canon; the claims gate checks that every audited theorem is cited in §23. It writes `lean/RECEIPT.txt` with source hashes. The only axioms are Lean's standard three: `propext`, `Classical.choice` and `Quot.sound`.

*(The count is 111 in the audit script's module list, verified today. The gates sentence in 1c is new prose describing what the script now actually does — approve or trim.)*

---

## 2. §23.8 "What the compiled theorems rest on" — the carried-premises list **[rewrite]**

File: `inserts/23-machine-checked-canon.md` (author tree and repo together).

> BEFORE:
> * the surface-code chain lemma (Dennis, Kitaev, Landahl and Preskill, 2002): minimum-weight decoding fails only along a self-avoiding chain of length at least d with at least half its edges faulty, with at most $V\Delta^L$ such chains of length $L$. This is the code-specific input to `Threshold.family_ceiling`; the threshold theorem's counting core is compiled (§23.6);
> * feasibility of Bennett's reversible counterpart;
> * the gate-set clause of premise 2 (a universal simulator implements each local factor);
> * the relational frame BCRD P1–P4.
>
> AFTER:
> * the surface-code chain lemma (Dennis, Kitaev, Landahl and Preskill, 2002), as the code-specific input to `Threshold.family_ceiling` for the surface-code instance. The threshold theorem's counting core is compiled (§23.6), and for concatenated codes the threshold is compiled end to end with no carried code-specific input: failure probability at most $(21p)^{2^k}/21$ under local stochastic noise (`Concatenated.concatenated_threshold`), so the fault ceiling is attained on a fully compiled route;
> * Bennett's reversible counterpart, no longer carried as prose: given a Bennett counterpart with the stated properties (a reversible map preserving base cost, zero heat on reversible options, positive heat on irreversible ones), the law itself forces reversible administration (`Bennett.premise5_from_bennett`). What remains carried is the counterpart's existence, now stated as explicit hypotheses of the compiled theorem;
> * the gate-set clause of premise 2, no longer carried as prose: every unitary on $\mathbb{C}^n$ is a finite product of two-level unitaries (`TwoLevel.two_level_decomposition`), so a simulator implementing each two-level factor implements every local evolution. What remains carried is that the universal simulator's gate set reaches every two-level factor;
> * the relational frame BCRD P1–P4.

---

## 3. §23.8 instance certificates — the R∨H coverage clause **[rewrite]**

> BEFORE (inside "Instance certificates, carried as hypotheses…"): … route coverage R(x) ∨ H(x), …
>
> AFTER: … route coverage R(x) ∨ H(x) — for the full existing domain, now derived from the law itself (`Bridge.coverage_from_law`, from `Law.scope_guarantee_iff`): a canonical maximiser on the whole existing domain has no needless existing loss, so every existing particular is covered — …

---

## 4. NOTE_C5 (Chapter 5 status note) — add greatestness at the declared premises **[append-only]**

Append two bullets to the Chapter 5 compiled list in `assemble_master.py` NOTE_C5 (they will render under §5.3's existing **4.1** note):

> * universal greatestness at the declared premises: under the Master Solvency Condition the canonical option keeps every particular, and every rival outcome is contained in it — no union-closure or slack condition (`UnionClosure.greatest_of_solvent`, `strict_of_solvent`);
> * greatest or not a protector: by income-or-irrelevance, the canonical regime is greatest at every step or has a first breach and is comparison-void (`UnionClosure.greatest_or_irrelevant`; the unfunded branch is `insolvent_not_greatest`).

---

## 5. §23.1 greatestness rows and §23.8 "Greatestness" paragraph — **already staged, no new decision**

These were folded in during this morning's consolidation (change record) and are already in the committed insert 23 and in the repo working tree (the §23.8 union-closure paragraph replaced by the Greatestness paragraph). They ride into the master on re-assembly. Listed here so the batch is complete:
* §23.1: "Universal greatestness at the declared premises" row (`greatest_of_solvent`, `greatest_or_irrelevant`, `insolvent_not_greatest`), replacing the union-closure-only rows as the headline; the resource-model rows retained below full solvency.
* §23.8: the union-closure paragraph now reads as the Greatestness paragraph (derived from the Master Solvency Condition; resource form compiled as well).

## 6. §23.A theorem index — **[append-only], needs your OK**

The generated complete theorem index (`<!-- BEGIN THEOREM INDEX -->` … §23.A, produced by `lean/gen-index.py`) is in the repo working tree but not yet committed anywhere. On your OK: commit it in the repo and copy it into the author-tree insert 23 so assembly carries it into the master. It is generated, not hand-written; regenerate after any module change.

## 7. Repo README — **needs your OK (already staged in the working tree)**

The one-paragraph change replaces the union-closure headline with "universal greatestness derived from the Master Solvency Condition" and updates the `UnionClosure.lean` row description. Full diff available: `git -C /Users/admin/Documents/2026/snuffy-canon-edition diff CANON-EDITION-V4.1/README.md`.

---

**Not in this batch (no prose change proposed):** §5.3's 4.0 proof text and integration guards 3–4 stay verbatim — the new derivation strengthens the result the note reports, and the edition's convention is that status notes record, not replace. Part I's stack table (§17.2) already reads correctly against items 2–3 above.

---

# ADDENDUM — the hostile re-read and the artifact review (same decision session)

*Items 8–16 come from the 25 October hostile re-read and the Gap-7 artifact review. Each is marked **[FOUND: source]** — the correct text already exists somewhere in the programme and needs porting — or **[NEW]** — never fixed anywhere; drafted fresh below.*

## 8. §22.5.2 arithmetic — **[NEW]** (introduced in the 25 Oct sourced rewrite)

> BEFORE (line 964): Ten thousand physical qubits at the [S5] footprint $(2d-1)^2$ hold about 9 logical qubits.
>
> AFTER: Ten thousand physical qubits at the [S5] footprint $(2d-1)^2$ hold about 4 logical qubits at d = 25 (2,401 physical each); the 9-logical allocation below corresponds to an installation of about $2.2\times10^4$ physical qubits.

*(At d = 25 the footprint is 49² = 2,401, so 10⁴ qubits hold ~4. The "9" survived from the earlier d = 17 text (33² = 1,089). Every downstream number — the 4.9×10⁻²⁴ target and the d = 25 conclusion — was computed at 9 logical qubits and is unaffected: d = 25 meets even the 9-logical target.)*

## 9. §21.2 "fermionic/bosonic" → "fermionic" — **[FOUND: `BANKS/2026-10-24-codex-x3-korero-preservation/X3-DERIVATIONS.md` §3–4]**

The banked derivation says "jointly gauge-invariant **fermionic** Gaussian state"; the occupation bound δI ≤ Q ≤ (1−δ)I is fermionic only (bosonic occupation is unbounded). The insert drifted from its own source.

> BEFORE: Consider fermionic/bosonic degrees of freedom coupled to a thermal bath…
>
> AFTER: Consider fermionic degrees of freedom coupled to a thermal bath…

## 10. §21.1 citation misnomer — **[NEW]** (caught by the new verify-all-4.1 step 6)

> BEFORE: `Information.data_processing` (21.1)
>
> AFTER: `DataProcessing.data_processing` (21.1)

## 11. "Theorem 15" in §20.4 — **[NEW]** (orphan: no tree in the workspace has ever had a Theorem 15)

> BEFORE: *Proof.* By Theorem 15 (Reciprocity Dominance) and Chapter 5…
>
> AFTER: *Proof.* By the reciprocity dominance theorem (§15.2) and Chapter 5…

## 12. Proposition 7 stated — **[FOUND: `WHOLE-EDITION-3.7-candidate-2026-10-24/edition/source/UPT-Master-Argument.md`, §Proposition 7]**

Proposition 7 is cited in §23.4 but never stated in this edition. Propose adding the one-line statement to Part II's retained core:

> **Proposition 7 (context-closed finite certificates).** If primitive deduction boundaries lie in im A and each generating context satisfies $C_jA = AM_j$, then every finite deduction boundary lies in im A (structural induction on the deduction tree). Compiled as `DeductionBoundary.rank_criterion` and `boundary_mem_image`.

## 13. Numbering-convention sentence, front matter — **[NEW]**

Append to the **Structure** paragraph of the front matter:

> Theorem and proposition numbers (Theorem 8, Proposition 7, E9, H5, X3, D1–D4…) follow the working series and the proof register; this edition cites them by their register names.

## 14. §17.1 proof precision — **[NEW]** (as written it contradicts §21.5's own Θ(1) maintenance)

> BEFORE: …the banked X3 forcing applies — maintaining any particular's witness against open-boundary flux demands $\Theta(t^{d_G})$ work, a finite budget is exhausted, and the breach is charged to $a$'s own account.
>
> AFTER: …the banked X3 forcing applies — once a witness goes unheld its recovery costs $W_{\min}(t)=\Theta(t^{d_G})$, exceeding any finite budget past $t_{\mathrm{irreversible}}$ (§21.5), so the breach is irreversible and charged to $a$'s own account; and until then the mandatory maintenance demand, though only $\Theta(1)$ in rate, is positive, so a finite budget is exhausted at finite $t_{\mathrm{breach}}$.

## 15. §20.5 middle bullet aligned with Chapter 4 — **[FOUND: Chapter 4's own language]**

> BEFORE: …the alternating projection eliminates all contradictory components, projecting the knowledge state back onto the verified safe core $A \sqcap B$.
>
> AFTER: …when the candidate contradicts the anchors the global meet collapses to zero and the state machine rolls back (Chapter 4); when it is consistent the anchors are preserved with zero distortion ($A \subseteq B \Rightarrow A \sqcap B = A$).

## 16. Part II source-of-record note and §23 scope sentence — **[FOUND raw material: repo README's 41-row module table + the generated §23.A index]**

**16a.** Append to Part II's preamble (after "proofs and precise premises at the source"):

> Where a Part II statement and a Section 23 compiled statement differ in scope or precision, the compiled statement is the statement of record.

**16b.** Add to §23's preamble a scope sentence covering the folded-in canon:

> The curated tables below map the results the edition's argument rests on. The complete canon — every compiled module, including the bridges, the verified bank modules and the original derivations folded in on 25 October — is indexed in §23.A; the README's module table describes each curated module's content.

---

**Sequence after your word:** apply 1–4 to `assemble_master.py` and the insert, commit 6–7 in the repo, re-run `assemble_master.py` → `check_master_assembly.py` → `render.sh` → `verify_render.py`, then the Zenodo draft for your review.

## 17. Authorised 4.2 stronger-argument incorporation

Applied to the new working 4.2 master on the author's instruction to incorporate
the stronger argument. The sealed published trees are unchanged. The full
before/after review, exact diff, original Gemini wavefront submission and
integration receipt are in `BANKS/2026-10-25-4.2-stronger-argument/`.

The working manuscript is
`SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25/SNUFFY-CANON-EDITION-4.2-MASTER.md`.
It includes the stronger physical bridge, controller-derived tracking, complete
Branch C, whole-outcome greatestness, full X3 derivation and the newly supplied
one-pass wavefront counting proof. G1–G3 retain the full targets. The author's
TIWA proposal is specified in the accompanying `TIWA-PATCH-REQUIREMENTS.md`;
its actual success, physical guard and complete work certificate remain the
construction task, rather than another request for the shell exponent.
