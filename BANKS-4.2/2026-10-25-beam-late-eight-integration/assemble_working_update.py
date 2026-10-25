#!/usr/bin/env python3
"""Integrate verified Beam modules and author proposals into the full 4.2 draft."""
from pathlib import Path
import hashlib
import json
import re
import shutil

BANK = Path(__file__).resolve().parent
ROOT = BANK.parent.parent
EDITION = ROOT / "SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25"
MASTER = EDITION / "SNUFFY-CANON-EDITION-4.2-MASTER.md"
RESULT = json.loads((BANK / "RESULT.json").read_text())
assert RESULT["overall"] == "PASS"
for name, digest in RESULT["source_sha256"].items():
    assert hashlib.sha256((EDITION / "lean" / name).read_bytes()).hexdigest() == digest, name
COUNT = RESULT["fresh_axiom_statements"]
text = MASTER.read_text()
assert "# Part III-F — Unified architecture and the self-grounding capstone" not in text


def replace_once(old, new):
    global text
    assert text.count(old) == 1, old[:100]
    text = text.replace(old, new, 1)


replace_once(
    "The accompanying 115-module Lean source is unchanged from the existing audited canon. Its preserved receipt records 115 clean compilations, 115 kernel checks, 831 audited theorems, standard axioms only and overall PASS. These are existing verification results, not a new compilation of this prose draft.",
    f"The current Lean tree contains 144 modules and {COUNT} audited public theorem/lemma names. The combined receipt reuses Beam's 136 clean compilation/kernel results after source and object hash checks, adds eight freshly compiled and kernel-checked modules, and records a fresh full axiom audit, completeness and claims gates with overall PASS. Seven previously omitted public helper lemmas are included. The original published 115-module/831-name baseline remains preserved. The architecture interfaces and their construction links are distinguished in Section 23.9.")

decoder_note = r"""
**Connection to the supplied decoder interface.** `DecoderRetraction.finite_code_recovery` constructs the supplied `DecoderPair` from this existing finite nearest-codeword theorem. Encoding is the inclusion of the maintained code; decoding returns a codeword. The nearest-point inequality at a clean record has distance zero, so decoding after encoding is the identity. The same constructed pair corrects every received word within the radius above. The retraction and its noisy-input guarantee are derived together.

**A non-vanishing maintained witness.** If the physical null state is represented by zero and \(\varepsilon<d(c_x,0)\), continuation implies \(a_x\ne0\): otherwise \(d(a_x,c_x)=d(c_x,0)>\varepsilon\). This is `DecoderRetraction.nonvanishing_of_continuation`. The initial record, its separation from null, the funded controller and the source refinement supply this operational persistence. The full scope of particulars remains the scope established in II.1.

"""
replace_once("## II.4 Tracking follows from the controller",
             decoder_note + "## II.4 Tracking follows from the controller")

window = r"""
#### 21.7.5 Boundary encoding, a sliding window, and the complete bill

The supplied continuation of TIWA keeps a fixed-width active window of shells and transfers a retiring patch's protected historical and relational record to the next boundary code. Let the window width be \(L\), independent of age. With the disjoint shells already defined, put

\[
A_k=\bigcup_{\max(0,k-L+1)\le j\le k}S_j.
\]

Every vertex of \(S_j\) belongs to at most \(L\) such windows. Hence the total active vertex-time count is at most \(L|B_R|\). This is a constant-overlap extension of the settled telescoping count; it needs no separate upper bound on each shell's surface area. If each active visit's complete charge is at most \(K\), the window work is at most \(KL|B_R|\). The charge includes holding, decoding, guard operation, control, routing, verification, routine ancilla reset, deployment and handoff. Continuing physical work outside that window must also remain in the complete ledger.

The boundary handoff has the original preservation target: a recovery of the encoded record must return its historical state and relations at the same fidelity standard. In symbols, the actual source maps must supply \(\mathcal R_k\mathcal E_k\simeq_\varepsilon\mathrm{id}\) on that full record, including its reference correlations. The code-capacity certificate and the physical implementation join this identity to the sliding-window charge. Section III-F records the supplied homological route and its chain-map correspondence.

For the supplied per-wave certificate, write \(q_k\) for the complete non-rollback charge and suppose its constructed local bound is

\[
q_k\le\alpha k^{d_G-1}+\beta,\qquad k\ge1.
\]

Let \(F\) be fixed initial/final charge and \(r_k\in\{0,1\}\) the controller's metered local rollback flag, charged at most \(R_*\) per wave. This explicit schedule gives the pathwise bill

\[
\mathcal Q(N)=F+\sum_{k=1}^{N}(q_k+R_*r_k).
\]

Routine erasure is already in \(q_k\), including successful decoding. With \(d_G\ge1\) and \(N\ge1\), every \(k^{d_G-1}\le N^{d_G-1}\), so

\[
\sum_{k=1}^{N}k^{d_G-1}\le N^{d_G},\qquad
\mathcal Q(N)\le(F+\alpha+\beta+R_*)N^{d_G}.
\]

This bound allows a metered rollback on every wave. An expected reset allowance is therefore unnecessary for the cost certificate. Successful recovery and any failed/rejected decoding still use the original charged fault accounts. Where the source admits more rollback operations, their actual count and cost must be included in \(q_k\) or separately bounded by the metering schedule.

For \(N(t)\le at+b\) and \(t\ge1\), \(N(t)\le(a+b)t\), yielding the age-independent coefficient

\[
\mathcal Q(t)\le
(F+\alpha+\beta+R_*)(a+b)^{d_G}t^{d_G}.
\]

`G3CompleteBill.cumulative_charge_bound` proves this cumulative implication in the existing natural-valued work-bill interface. `valid_work_bill_from_complete_ledger` derives `G3_ValidWorkBill` from the full ledger equality, local cost bounds and coefficient; `valid_bill_bound_in_age` supplies the wave-to-age conversion. The real-exponent argument is the displayed maximum-term proof. The constant-overlap calculation retains the full polynomial-growth graph domain when a per-shell surface upper estimate is unavailable.

The remaining source correspondence is the actual boundary encoder, preserved semantic observables, storage capacity, charged retirement map and complete cost equality. These are the construction links of the same G1/G3 task; the cumulative upper inequality is not taken as its own input.

"""
replace_once("### 21.8 Consequences for preservation and the fixed proof target",
             window + "### 21.8 Consequences for preservation and the fixed proof target")

start = text.index("*This section records which results of the edition are compiled theorems")
end = text.index("\n\n*Evidence convention", start)
text = text[:start] + (
    f"*This section maps the edition's compiled results and their actual hypotheses. "
    f"The current source contains 144 modules and {COUNT} audited public theorem/lemma names. "
    "The combined receipt records 136 reused clean compilation/kernel results, eight fresh "
    "compilation/kernel checks, a fresh full axiom audit with only `propext`, `Classical.choice` "
    "and `Quot.sound`, and fresh completeness/claims gates with overall PASS. "
    "The reused results are tied to the preserved Beam receipt and source/object hashes. "
    "Section 23.9 gives the new interfaces and derived adapters; their verification does not "
    "substitute their names for the full source construction.*"
) + text[end:]

interfaces = r"""
### 23.9 Supplied architecture interfaces and derived connections

| Module | Verified result and current role |
| --- | --- |
| `G1FullDomain` | Source/fault enumeration and append-preserved event compliance; the full physical source and charged faults must supply their correspondence to `Bridge.hcert` |
| `G2WholeOutcome` | Authorized transaction records are closed and record positive work; the whole continuation/freedom tuple and its realisability remain the G2 construction |
| `G3CompleteBill` | `cumulative_charge_bound`, `valid_work_bill_from_complete_ledger` and `valid_bill_bound_in_age` derive the bill from complete metered local charges and the wave schedule |
| `GuardOperator` | The threshold cases select the supplied projection or penalty map |
| `HamiltonianDecomposition` | The natural-valued bookkeeping terms sum to their defined total; an actual operator/Hamiltonian correspondence remains explicit |
| `GuardSignature` | The supplied guard record carries idempotence and monotonicity; its physical instance and fault nullification must be constructed |
| `WorkBilling` | Nonnegative natural work and the scalar bound interface; the complete source-event cost correspondence is specified in Section 21.7.5 |
| `DecoderRetraction` | `finite_code_recovery` fills the interface from the existing nearest-codeword construction and proves the radius guarantee; `nonvanishing_of_continuation` preserves separation from null; `finite_code_self_grounding` constructs the non-bottom fixed-point witness |

The earlier `G1Certificate.universal_protection_held` has conclusion `True`; it is a placeholder and is not the protection theorem `Bridge.universal_protection_held`. The latter's full source certificate remains the unchanged G1 target. The exact integration history and dependency trace accompany this working edition.

"""
replace_once("<!-- BEGIN THEOREM INDEX -->", interfaces + "<!-- BEGIN THEOREM INDEX -->")
index = (EDITION / "inserts/23-machine-checked-canon.md").read_text()
block = re.search(r"<!-- BEGIN THEOREM INDEX -->.*?<!-- END THEOREM INDEX -->",
                  index, re.S).group(0).replace("## 23.A Complete theorem index",
                                               "### 23.A Complete theorem index", 1)
text = re.sub(r"<!-- BEGIN THEOREM INDEX -->.*?<!-- END THEOREM INDEX -->",
              lambda _: block, text, count=1, flags=re.S)
text = text.replace("`G1Certificate` (computable safety certificate)",
                    "`G1Certificate` (placeholder with conclusion `True`)")

proposal_start = text.index("# Part III-D — Proposed constructions")
proposal_end = text.index("# Part III-E — Outstanding construction work", proposal_start)
text = text[:proposal_start] + r"""# Part III-D — Transducer, trajectory and semantic constructions

These constructions retain their full proposed conclusions. Their source correspondence and complete bill join the verified components, rather than being certified by a title or signature.

## D.1 Transduced Preservation Theorem (TPT)

The supplied transducer route uses a macroscopic dissipation factor \(\Gamma\approx10^{14}\), an adiabatic efficiency \(\alpha\in(0,1]\), and a boundary transducer \(\tau:\mathcal H_{\mathrm{phys}}\to\mathcal M_{\mathrm{rel}}\). Its target is the complete physical work ceiling \(W(t)\le Ct^{d_G}\), preserving the protected historical record and relations.

Every exterior transducer, reset, holding and controller charge remains in that total. A fixed multiplicative hardware overhead can enter \(C\); deriving the complete bill still requires the actual device and operation count. Section 21.7.5 gives the cumulative ledger implication for the supplied sliding-window route.

## D.2 Topological entropy and trajectory bounding

For the supplied trajectory count \(N(t,\varepsilon)\le Kt^{d_G}\) and complete work correspondence \(W(t)=\beta N(t,\varepsilon)\), the intended conclusion is \(W(t)\le\beta Kt^{d_G}\). The transducer construction must supply that actual trajectory estimate and the work correspondence, including every physical charge.

The pinned Mathlib already contains Bowen–Dinaburg dynamical nets and topological entropy in `Mathlib.Dynamics.TopologicalEntropy.NetEntropy` and `CoverEntropy`. It also proves the general Hilbert-space mean-ergodic theorem, `ContinuousLinearMap.tendsto_birkhoffAverage_orthogonalProjection`, for a continuous linear contraction. Missing upstream infrastructure is not a blocker for these results. Applying them requires the actual operator and the claimed growth/work correspondence.

## D.3 Top continuation and the constructed evaluation fixed point

The `Htopkeeps` record carries `eval ⊤ = ⊤` as its unitality field. Its extractor theorem does not by itself supply the different continuation semantics used in `SolventReciprocity`.

The supplied decoder interface now has a derived construction. For its code inclusion and recovery, put \(P=\mathrm{encode}\circ\mathrm{decode}\). Retraction gives \(P(P(y))=P(y)\) and \(P(\mathrm{encode}(c))=\mathrm{encode}(c)\). `DecoderRetraction.finite_code_self_grounding` constructs this decoder and a non-bottom fixed-point witness from a maintained non-bottom code record. Part III-F connects that result to the proposed ontological capstone while retaining the actual G1 source obligation.

---

""" + text[proposal_end:]

old_start = text.index("## E.4 Deep proofs requiring Mathlib support")
old_end = text.index("# Part IV — References and provenance", old_start)
text = text[:old_start] + r"""## E.4 Existing analytic support and its source correspondence

The general contraction mean-ergodic theorem and topological entropy are present in the pinned Mathlib, with the names and files listed in Part III-D. The existing `MeanErgodic` and `MeanErgodicDeep` modules prove their stated identity-map cases; those filenames do not certify an application of the general theorem to an unspecified physical operator.

`GuardFactorization` proves commuting Kronecker factors. The source construction must connect the actual dynamics to the required factors and preserved record. A von Neumann algebra development is not established as a prerequisite for this finite construction.

---

# Part III-F — Unified architecture and the self-grounding capstone

This section integrates the author's supplied unified ledger and homological proposal into the full working edition. Parts I–III and their maximal domain, outcome order and rival quantifiers remain in force. The original submissions are preserved with the integration record.

## F.1 The unified gate and work ledger

The guard is an idempotent, monotone projection with the intended fault-nullification action. The transaction emits \((h_{\mathrm{pre}},h_{\mathrm{post}},w,a,c)\) and enforces \(a=1\Rightarrow(c=1\land w>0)\). The complete work functional is additive over executed traces and has the full target \(\mathcal W(T)\le Ct^{d_G}\).

The transaction invariant supports the source implementation of G2; its connection to the whole greatest outcome, including all continuation and freedom stages, remains explicit. The work derivation in 21.7.5 now supplies `G3_ValidWorkBill` from its complete local ledger. Guard operation, transduction, boundary encoding, retirement and preserved history belong to that same charged execution.

## F.2 Historical boundary encoding and recovery

The supplied history is a causal labelled graph \(\mathcal H=(V,E,\phi)\). Its full preservation target is

\[
\mathcal R_{\mathrm{bnd}}(\mathcal E_{\mathrm{bnd}}(\mathcal H),v)=\phi(v)
\]

at the original fidelity standard, together with preservation of the relevant relations. Within its proved radius, the finite-code decoder returns the exact original codeword. The boundary encoding separately specifies which full historical record that codeword represents.

The supplied accumulator route retains the proposed representation \((\partial\mathcal H,\operatorname{Acc}(V),\bigoplus_{e\in E}\psi(e))\) and capacity target

\[
|\mathcal B_{\mathrm{boundary}}(t)|\le K\log\operatorname{Vol}(U(t)).
\]

Its capacity certificate must count the physical information in the accumulator, payload, query witnesses and retained recovery data. An accumulator authenticates supplied data and membership; an exact reconstruction additionally supplies the data needed to return \(\phi(v)\).

The supplied retirement charge is

\[
W_{\mathrm{retire}}
=c_{\mathrm{acc}}|V_{\mathrm{retire}}|
+c_{\mathrm{bound}}|E_{\mathrm{retire}}|\log|V_{\mathrm{retire}}|.
\]

For the protocol's fixed-radius local retirement patches, bounded degree gives \(|V_{\mathrm{retire}}|\le M_0\) and \(|E_{\mathrm{retire}}|\le D_{\max}|V_{\mathrm{retire}}|\). Thus this local term is at most \((c_{\mathrm{acc}}+c_{\mathrm{bound}}D_{\max}\log M_0)|V_{\mathrm{retire}}|\), a constant charge per retired vertex. The settled bounded-overlap count absorbs it into \(O(t^{d_G})\). Global accumulator updates, witness generation, routing, reset and continued storage still enter the complete local or separately metered charge.

The proposed topological route represents history by a chain complex and uses

\[
0\longrightarrow C_*(\partial U)\xrightarrow{i}C_*(K)
\longrightarrow C_*(K,\partial U)\longrightarrow0.
\]

Its long exact sequence contains

\[
H_n(\partial U)\xrightarrow{i_*}H_n(K)\xrightarrow{j_*}
H_n(K,\partial U)\xrightarrow{\delta_n}H_{n-1}(\partial U).
\]

The supplied route is implemented by constructing a boundary chain map \(\rho:C_*(K)\to C_*(\partial U)\), inclusion \(i\), and chain homotopy

\[
i\rho-\mathrm{id}=dh+hd.
\]

For a cycle \(z\), the recovered chain satisfies \(i\rho z-z=d(hz)\), so its homology class is preserved. A protected semantic observable \(q\) that annihilates these exact terms then obeys \(q(i\rho z)=q(z)\). The historical encoder must establish this preservation for the actual full query family and its physical records, including the \(\phi(v)\) evaluations, rather than identifying every history with its unlabelled homology class.

Exactness identifies images and kernels. If \(H_n(K,\partial U)=0\), the displayed connecting map has zero domain; this alone does not make it an injective encoding of arbitrary histories. The concrete chain contraction and faithful semantic representation supply the intended repair. Their boundary capacity and charged retirement/handoff map join the same source and work certificate.

## F.3 The Axiom of Internal Self-Grounding

The author proposes the following ontological capstone:

\[
\exists e\in\mathcal M_{\mathrm{rel}},\qquad
\mathcal E(e)=e,\qquad \tau(e)\ne\bot.
\]

Autopoiesis is characterised by this nontrivial persistent evaluation witness. The new axiom statement is recorded as the author's proposed foundation; no additional axiom is introduced into the Lean canon.

There is a derived finite-code witness for the displayed property. Use the constructed decoder, let

\[
\mathcal E=\tau=\mathrm{encode}\circ\mathrm{decode},
\qquad e=\mathrm{encode}(c),
\]

where \(c\) is a maintained non-bottom record. Retraction gives

\[
\mathcal E(e)=e,\qquad \tau(e)=e\ne\bot.
\]

`DecoderRetraction.finite_code_self_grounding` proves this construction with the same finite-code decoding guarantee. Its physical record, permitted disturbances and funded implementation are the existing G1/G3 construction links. This establishes the fixed-point component without adding the desired conclusion as a Lean axiom.

The proposed mutual-bootstrap statement is retained in full:

\[
\operatorname{Vol}(U)>0\quad\Longleftrightarrow\quad H_*(\partial U)\ne0.
\]

Its interpretation must specify the actual relational volume, boundary, coefficient system and history representation, and derive the two directions for that model. The long exact sequence alone does not establish this volume equivalence.

## F.4 Funding, persistence and lifetime error

The work ceiling bounds demand. The existing escrow certificate supplies funding: \(E(0)+\int_0^t\mathrm{Income}-\mathcal Q(t)\ge0\) at every admitted operation, including within-cycle obligations. Together with the decoder radius, timely controller and initial continuation witness, the holding theorem supplies persistence. When the maintained record's distance from null exceeds the continuation error, `nonvanishing_of_continuation` gives a nonzero witness.

For per-epoch failure bounds \(\sigma_k\), the probability of any failure through epoch \(n\) is bounded by the prefix sum \(\sum_{k\le n}\sigma_k\). The bound on a future failure from \(n\) onward is the tail \(\sum_{k\ge n}\sigma_k\). If the actual code/noise schedule makes this series summable, the tail tends to zero; the all-time failure probability remains bounded by the full sum. The existing declared fault standard is retained.

This completes the unified working presentation of the supplied gates, bill derivation, decoder, historical-boundary route and self-grounding capstone. The full source, semantic-capacity and physical work correspondences remain the same construction task; the new axiom wording is not used as a replacement for their derivation.

---

""" + text[old_end:]

appendix_start = text.index("The unchanged accompanying Lean baseline contains 115 modules")
appendix_end = text.index("**The analytic bridge.**", appendix_start)
text = text[:appendix_start] + (
    f"The original published baseline contains 115 modules and 831 audited names. "
    f"The current working tree contains 144 modules and {COUNT} audited public theorem/lemma names. "
    "The combined verification preserves Beam's completed 136 compilation/kernel results with "
    "source/object hashes, freshly verifies the eight later modules, and freshly runs the full "
    "axiom, completeness and claims gates. The receipt states exactly which results are reused. "
    "The original failed run is preserved in the integration bank.\n\n"
    "This increment integrates the eight, adds the derived finite-code recovery, complete-ledger "
    "and non-vanishing/fixed-point connections, repairs verification coverage and updates the "
    "author's supplied boundary and ontological proposals. Its exact changes and verification "
    "evidence accompany the working draft. No published edition or release is changed.\n\n"
) + text[appendix_end:]

# Preserve the full existing text while removing malformed math control escapes.
assert not [c for c in text if ord(c) < 32 and c not in "\n\t"], "Unexpected control character"
MASTER.write_text(text)

README = EDITION / "README.md"
readme = README.read_text()
a = readme.index("The accompanying `lean/` tree")
z = readme.index("The published 4.1 tree", a)
readme = readme[:a] + (
    f"The current verification covers 144 modules and {COUNT} public theorem/lemma names. "
    "Its combined receipt reuses 136 verified compilation/kernel results from Beam and freshly "
    "compiles and checks the eight later modules; the complete axiom audit, strict coverage, "
    "corpus completeness and claims gates pass. Seven previously omitted public helpers are included.\n\n"
    "The new derived connections construct Beam's finite-code decoder, derive the complete "
    "metered bill and age bound, and prove the non-vanishing/fixed-point witnesses. The historical "
    "boundary encoder and self-grounding proposal are integrated in Part III-F with their "
    "actual source and semantic correspondences visible.\n\n"
    "[Current integration, before/after and dependency trace]"
    "(../BANKS/2026-10-25-beam-late-eight-integration/DEPENDENCY-TRACE.md).\n\n"
) + readme[z:]
README.write_text(readme)
print(f"Updated full working master and README: 144 modules, {COUNT} audited statements.")
