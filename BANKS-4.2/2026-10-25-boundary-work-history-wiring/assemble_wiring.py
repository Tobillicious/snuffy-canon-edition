#!/usr/bin/env python3
"""Join the checked boundary/work/history components to the current master."""
from pathlib import Path
import difflib, hashlib, json, re
bank = Path(__file__).resolve().parent
root = bank.parent.parent
edition = root / "SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25"
result = json.loads((bank / "RESULT.json").read_text())
assert result["overall"] == "PASS"
assert result["fresh_axiom_statements"] == 924
before = json.loads((bank / "BEFORE.json").read_text())

def write(path, text):
    path.write_text(text)

masterpath = edition / "SNUFFY-CANON-EDITION-4.2-MASTER.md"
s = masterpath.read_text()
assert "# Part III-G —" not in s, "Integration already present; inspect before rerunning"
indexsrc = (edition / "inserts/23-machine-checked-canon.md").read_text()
begin, end = "<!-- BEGIN THEOREM INDEX -->", "<!-- END THEOREM INDEX -->"
block = indexsrc.split(begin, 1)[1].split(end, 1)[0]
block = block.replace("## 23.A Complete theorem index", "### 23.A Complete theorem index", 1)
s = re.sub(re.escape(begin) + ".*?" + re.escape(end),
           lambda _: begin + block + end, s, flags=re.S)
s = re.sub(r"\b896\b", "924", s)
s = s.replace(
    "| `HamiltonianDecomposition` | The natural-valued bookkeeping terms sum to their defined total; an actual operator/Hamiltonian correspondence remains explicit |",
    "| `HamiltonianDecomposition` | Explicit Hermitian boundary/reservoir exchange, total-charge conservation, nonzero boundary pumping and a unitary charge-transfer gate; the full physical source correspondence remains explicit |")
s = s.replace(
    "| `WorkBilling` | Nonnegative natural work and the scalar bound interface; the complete source-event cost correspondence is specified in Section 21.7.5 |",
    "| `WorkBilling` | The first-law decoder work identity, free-energy floor and its saturation condition; a Gibbs entropy/energy allocation bound and funded decoder cycles; the complete physical source cost remains in Section 21.7.5 and Part III-G |")
s = s.replace(
    "| `DecoderRetraction` | `finite_code_recovery` fills the interface from the existing nearest-codeword construction and proves the radius guarantee; `nonvanishing_of_continuation` preserves separation from null; `finite_code_self_grounding` constructs the non-bottom fixed-point witness |",
    "| `DecoderRetraction` | Finite-code recovery and fixed-point witnesses; flux-derived isometry and adjoint decoder; explicit finite encoder/capacity bound; historical queries, ordered words, commutators and Gram preservation; exact exponential transport, work-shifted flow and a derived finite dual smearing kernel |")
s = s.replace(
    "The following items are required for the full G1–G3 construction. They are not\n"
    "discharged by the compiled support modules, which provide scaffolding only.",
    "The following source correspondences are required for the full G1–G3 construction. "
    "The compiled modules now include derived decoder, history, flow, charge and work "
    "components; the correspondences below join those components to the complete "
    "physical source and outcome.")
s = s.replace(
    "explicit.\n\n## E.4 Existing analytic support",
    "explicit. Part III-G now constructs a finite coordinate encoder and adjoint "
    "decoder, transports the full represented historical algebra and work-shifted "
    "flow, and derives its finite dual kernel. The source must instantiate their "
    "capacity assignment on the actual historical record and meter its physical "
    "retirement/handoff, retained memory and query operations in that complete bill.\n\n"
    "## E.4 Existing analytic support", 1)
s = s.replace(
    "The supplied history is a causal labelled graph",
    "Part III-G supplies the explicit operator/coordinate encoder, adjoint recovery "
    "and historical query transport developed from the later three-pillar submission. "
    "The topological route below retains its faithful source correspondence.\n\n"
    "The supplied history is a causal labelled graph", 1)
addition = (edition / "inserts/25-boundary-work-history.md").read_text()
s = s.replace("# Part IV — References and provenance",
              addition.rstrip() + "\n\n# Part IV — References and provenance", 1)
old = ("This increment integrates the eight, adds the derived finite-code recovery, "
       "complete-ledger and non-vanishing/fixed-point connections, repairs verification "
       "coverage and updates the author's supplied boundary and ontological proposals.")
new = ("The eight-module integration and its 896-statement receipt remain preserved. "
       "This increment adds 28 checked statements in the existing DecoderRetraction, "
       "HamiltonianDecomposition and WorkBilling modules, integrates the three-pillar "
       "operator/history/work construction in Part III-G, and keeps the continuous "
       "integral/channel derivations and physical source correspondences explicit.")
assert old in s
s = s.replace(old, new)
write(masterpath, s)

insert = edition / "inserts/23-machine-checked-canon.md"
t = insert.read_text()
t = re.sub(r"\b896\b", "924", t)
prefix, suffix = t.split(begin, 1)
for module in ("HamiltonianDecomposition", "WorkBilling", "DecoderRetraction"):
    oldrow = re.search(r"^\| `" + module + r"` \|.*$", prefix, re.M)
    newrow = re.search(r"^\| `" + module + r"` \|.*$", s, re.M)
    if oldrow and newrow:
        prefix = prefix[:oldrow.start()] + newrow.group(0) + prefix[oldrow.end():]
write(insert, prefix + begin + suffix)

readme = edition / "README.md"
t = re.sub(r"\b896\b", "924", readme.read_text())
t += ("\nThe operator/history/work continuation adds 28 checked statements in the "
      "existing three modules. [Part III-G](inserts/25-boundary-work-history.md) "
      "constructs the encoder/adjoint decoder, historical operator transport, "
      "work-shifted flow, dual kernel, work floor and reservoir charge exchange. "
      "[Verification and before/after](../BANKS/2026-10-25-boundary-work-history-wiring/BEFORE-AFTER.md) "
      "record exactly what was checked and the remaining source correspondences.\n")
write(readme, t)

checklist = edition / "PUBLICATION-CHECKLIST.md"
t = re.sub(r"\b896\b", "924", checklist.read_text())
t = t.replace("## Proof construction and review to finish",
    "- The 28 new operator/history/work statements pass compilation, kernel and "
    "axiom checks in the existing late modules; Part III-G contains their "
    "construction and identifies the prose integral/channel derivations.\n\n"
    "## Proof construction and review to finish", 1)
t = t.replace(
    "- Join the actual historical boundary encoder to the full query/relational\n"
    "  fidelity, code capacity, physical handoff and complete local charges.",
    "- Instantiate the constructed coordinate/flux encoder on the actual full "
    "historical query/relational record, with its boundary capacity assignment, "
    "physical handoff, retained memory and complete local charges.")
write(checklist, t)

support = edition / "SUPPORTS-FOR-GEMINI.md"
t = re.sub(r"\b896\b", "924", support.read_text())
t += ("\n## Three-pillar continuation incorporated\n\n"
      "Part III-G now derives the complex-linear flux-to-isometry step, constructs "
      "a finite coordinate encoder and its adjoint decoder, preserves historical "
      "queries and ordered operator words, transports the work-shifted exponential "
      "flow and constructs exact dual smearing coefficients from a complete finite "
      "operator basis. The work/entropy balance, saturation condition, energy "
      "allocation bound, funded cycles and explicit reservoir charge exchange are "
      "also checked. The present receipt is 144 modules/924 public statements.\n\n"
      "The source construction now instantiates these maps on the actual full "
      "historical record and metered physical handoff, supplies its capacity "
      "assignment and complete work equality, and joins the full-domain G1 "
      "certificate and whole continuation/freedom G2 outcome. No repeat of the "
      "shell exponent, finite decoder, or derived operator/ledger lemmas is "
      "requested. The continuous smearing integral and channel extension are "
      "prose derivations identified separately from the native Lean results.\n")
write(support, t)

agents = root / "AGENTS.md"
t = agents.read_text()
t = t.replace(
    "`BANKS/2026-10-25-beam-late-eight-integration/`.\n  All eight late Beam modules",
    "`BANKS/2026-10-25-boundary-work-history-wiring/`.\n  The prior eight-module integration remains preserved in\n  `BANKS/2026-10-25-beam-late-eight-integration/`.\n  All eight late Beam modules", 1)
t = t.replace("144 modules and 896 public theorem/lemma names", "144 modules and 924 public theorem/lemma names", 1)
marker = "- Six derived connections are now in the existing late modules:"
note = ("- The three-pillar continuation adds 28 checked statements in the existing\n"
        "  DecoderRetraction, HamiltonianDecomposition and WorkBilling modules.\n"
        "  Part III-G constructs flux-derived/coordinate encoding, adjoint decoding,\n"
        "  preservation of historical queries and ordered words, commutator and Gram\n"
        "  transport, bounded exponential/work-shifted flow and exact finite dual\n"
        "  smearing coefficients. The same increment proves the work/entropy balance,\n"
        "  correct free-energy floor and saturation condition, energy-allocation\n"
        "  entropy bound, funded cycles and a concrete charge-exchange reservoir.\n"
        "  Continuous integral/channel extensions are prose derivations, identified\n"
        "  explicitly. The remaining application is the actual full-history source,\n"
        "  capacity assignment, physical handoff and complete bill, joined to the\n"
        "  full G1 certificate and whole-outcome G2. Do not request the new component\n"
        "  derivations again or equate their verification with global completion.\n")
assert marker in t
t = t.replace(marker, note + marker, 1)
write(agents, t)

register = root / "NEXT-PROOF-REGISTER-2026-10-25.md"
t = register.read_text()
intro = "*The open Lean tasks, stated precisely against the current 113-module canon. Companion to `BANKS/2026-10-24-next-proof-register/REGISTER.md`.*"
replacement = ("*Historical queue recorded against the then 113-module canon. Current "
    "4.2 working state: 144 modules / 924 audited statements; the older entries "
    "below retain their dated context. Companion to "
    "`BANKS/2026-10-24-next-proof-register/REGISTER.md`.*\n\n"
    "## Current 4.2 checkpoint\n\n"
    "Solvent and affordable reciprocity are incorporated in the checked canon. "
    "`ErrorBudget.telescoping_delta` and `error_budget` now supply the compiled "
    "product-error engine. Their older waiting/registered labels below are "
    "superseded by this checkpoint.\n\n"
    "The boundary/work/history continuation adds 28 checked statements in the "
    "existing late modules and Part III-G of the working master. Current work is "
    "the actual full-history source/capacity/physical handoff and complete charge "
    "correspondence, full G1 source/fault certificate, whole continuation/freedom "
    "G2 outcome, and the remaining semantic review. Shell counting, finite-code "
    "recovery, cumulative billing, operator flow and finite dual-kernel derivations "
    "are established component results. Verification evidence: "
    "`BANKS/2026-10-25-boundary-work-history-wiring/RESULT.json`.")
assert intro in t
write(register, t.replace(intro, replacement, 1))

after = {}
diffs = []
changes = []
for key, info in before.items():
    src = (root / key[len("@root/"):]) if key.startswith("@root/") else (edition / key)
    data = src.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    after[key] = sha
    oldpath = bank / info["archive"]
    assert hashlib.sha256(oldpath.read_bytes()).hexdigest() == info["sha256"]
    if sha != info["sha256"]:
        changes.append(key)
        diffs.extend(difflib.unified_diff(oldpath.read_text().splitlines(True),
            data.decode().splitlines(True), fromfile="before/" + key, tofile="after/" + key))
newkey = "inserts/25-boundary-work-history.md"
newpath = edition / newkey
after[newkey] = hashlib.sha256(newpath.read_bytes()).hexdigest()
changes.append(newkey)
diffs.extend(difflib.unified_diff([], newpath.read_text().splitlines(True),
    fromfile="/dev/null", tofile="after/" + newkey))
(bank / "CHANGES.diff").write_text("".join(diffs))
(bank / "CHANGES.json").write_text(json.dumps({"changed": changes, "after_sha256": after}, indent=2) + "\n")

audit = (edition / "lean/SummitsAudit.lean").read_text()
statements = re.findall(r"^#print axioms (\S+)", audit, re.M)
master = masterpath.read_text()
master_index = master.split(begin, 1)[1].split(end, 1)[0]
insert_index = (edition / "inserts/23-machine-checked-canon.md").read_text().split(begin, 1)[1].split(end, 1)[0]
assert master_index.replace("### 23.A", "## 23.A", 1) == insert_index
assert len(statements) == len(set(statements)) == 924
assert len(re.findall(r"^\| `[^`]+` \|", master_index, re.M)) == 144
assert not [c for c in master if ord(c) < 32 and c not in "\n\r\t"]
assert master.count("# Part III-G —") == 1
assert all((edition / "lean" / name).read_bytes() and
           hashlib.sha256((edition / "lean" / name).read_bytes()).hexdigest() == digest
           for name, digest in result["source_sha256"].items())
checks = {"overall": "PASS", "audit_statements": 924, "index_modules": 144,
    "index_matches": True, "source_hashes_match_receipt": True,
    "control_characters": 0, "part_III_G_copies": 1,
    "changed_paths": len(changes),
    "master_sha256": hashlib.sha256(masterpath.read_bytes()).hexdigest()}
(bank / "MANUSCRIPT-CHECKS.json").write_text(json.dumps(checks, indent=2) + "\n")
print(json.dumps(checks, indent=2))
