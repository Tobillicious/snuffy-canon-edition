# Section 13 — Logical extension: the meet algebra (H5)

## 13.1 The embedding and the detector

The logical boundary fragments are embedded by the declared map \(\Pi\) — a component of the header premises, not a derived canonicalizer — which assigns to each formula \(\phi\) the projection \(P_\phi\) onto its model subspace, with conjunction as the meet

\[
P_{\phi\wedge\psi}=\bigwedge\{P_\phi,P_\psi\}=\lim_{n\to\infty}(P_\phi P_\psi)^n
\]

(von Neumann alternating projections). A presentation \(\mathcal T\) is consistent exactly when its global meet is non-zero:

\[
\mathcal T\ \text{consistent}\iff P_{\mathcal T}=\bigwedge_{\phi\in\mathcal T}P_\phi\neq0 .
\]

The Gram determinant of the projection set is **retired** as a detector, on two exact counterexamples recorded in the review banks: the contradictory pair \(\{\psi,\neg\psi\}\) has Gram determinant \(4>0\) (orthogonal operators are independent), and the canonical, pairwise-consistent, jointly inconsistent triple \(\{p,\,q,\,\neg(p\wedge q)\}\) has determinant \(7>0\) with a zero triple meet. The meet detects what the Gram cannot: theory-level inconsistency is an empty intersection, not a linear dependence.

## 13.2 Anchor preservation under valid deduction

**Theorem.** Let \(\mathcal T_0\) be the protected anchor set with \(P_{\mathcal T_0}\neq0\). If \(\Delta\Sigma\) is deduced from \(\mathcal T_0\), the anchor meet is preserved identically; if \(\Delta\Sigma\) contradicts \(\mathcal T_0\), the combined meet collapses to zero.

*Proof.* For deduced \(\phi\), entailment gives \(P_{\mathcal T_0}\le P_\phi\), and the meet satisfies \(P_A\le P_B\Rightarrow P_A\wedge P_B=P_A\); hence \(P_{\mathcal T_0\cup\Delta\Sigma}=P_{\mathcal T_0}\). For contradiction, \(\mathcal T_0\vdash\neg\phi\) gives \(P_{\mathcal T_0}\le I-P_\phi\), whence \(P_{\mathcal T_0}\wedge P_\phi=0\) and the global meet collapses by associativity. ∎

The boundary state machine commits an expansion when the meet norm is non-zero and rolls back on zero — protected anchors are preserved unconditionally under valid deduction. One honest note: an *asserted* (non-deduced) consistent extension may shrink the anchor meet without triggering rollback; this matches the declared semantics and is stated, not hidden. Deduction-boundary closure beyond the fragments continues to use the banked rank criterion \(\operatorname{col}(A)\cap\operatorname{col}(G)=\{0\}\), applied to boundaries rather than formula projections.
