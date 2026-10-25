# Snuffy — Canon Edition 4.2

**The Universal Protection Theory and its machine-checked canon.**

The Universal Protection Theory states a law for any agent powerful enough to shape what continues to exist: *never lose an existing particular needlessly.* Its scope is every particular and every relation, and its subject is protection from every digital mind, a pure optimiser included.

This edition constructs the holding certificate in full. On the held source every particular is kept against any agent of bounded coupling, and every component of the protection theorem's source certificate is proved. The whole greatest outcome is realised, with union closure derived from locality. Recovery work is Θ(t^d): a wavefront sweep is proved to succeed, with a complete metered bill. The fault ceiling is attained, correlated bursts included. Bennett's reversible counterpart is constructed. 166 Lean 4 modules and 1,025 audited theorems machine-check the argument. Section 23 maps every compiled result to its theorem and lists exactly what each rests on.

| Path | Contents |
| --- | --- |
| `SNUFFY-CANON-EDITION-4.2-MASTER.md` | The master manuscript: the law and bridge (Part II), the canon and the 4.1 sections (Part III, Sections 15–24), and the 4.2 constructions (Parts III-C to III-G, §G.1–G.14). |
| `render/` | `Snuffy-Canon-Edition-4.2.pdf`, `.epub`, `.html` and the exact LaTeX input. `RENDER-VERIFY.json` records that each rendering carries the ledger chain heads, the DOIs, the canon sentence and the module count unbroken, with no door content. |
| `lean/` | The machine-checked canon. `lean/build-and-audit.sh` rebuilds and audits it against Mathlib rev `56a005855ea1`; the receipt is `lean/RECEIPT.txt`. |
| `inserts/` | The section sources of §23 (with the generated theorem index) and Part III-G. |
| `SOURCES-22.md` | The sources of the physical parameter ledger (§22.5). |
| `checks/` | The render script (`render.sh` with its header and filter) and the render verification (`verify_render.py`). |
| `CITATION.cff`, `zenodo.json`, `LICENSE` | Citation metadata, deposit metadata and the CC-BY-4.0 licence. |
| `SHA256SUMS` | Checksums of every file above. |

**Reproduce.**

```bash
bash checks/render.sh                  # PDF (xelatex), HTML and EPUB (pandoc)
python3 checks/verify_render.py        # citations unbroken in every rendering
MATHLIB_PROJECT=/path/to/mathlib-at-56a005855ea1 CORPUS_ROOT=/path/to/workspace lean/build-and-audit.sh
```

Previous editions: Snuffy Canon Edition 4.1, DOI 10.5281/zenodo.23631881, and 4.0, DOI 10.5281/zenodo.23608443. Parent mathematical core: *A Lattice Preservation Calculus*, DOI 10.5281/zenodo.23599528. Source repository: github.com/Tobillicous/snuffy-canon-edition.
