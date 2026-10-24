# Section 8 — The four-stroke thermodynamic core

## 8.1 The corrected stroke identity

Let the protected system \(S\) carry the constrained reference \(\tau\) on the protected subspace, with fixed endpoint Hamiltonian. Let a feedback stroke deliver work \(W_{\mathrm{on}}\) across \(S\)'s boundary and export heat \(Q_B\) to the bath, and let the correlation \(I(S\!:\!A)\) change from \(I_1\) to \(I_2\). Then always

\[
\Delta D_{S,\mathrm{II}}
= -\Delta S_S+\beta\,\Delta U_S
= \beta W_{\mathrm{on}}-\beta Q_B+I_1-I_2 .
\]

With the syndrome correlation fully consumed, \(I_1=I_M\) and \(I_2=0\):

\[
\boxed{\;\Delta D_{S,\mathrm{II}}=\beta W_{\mathrm{on}}-\beta Q_B+I_M.\;}
\]

The identity is elementary — it is the definition of relative entropy at fixed Hamiltonian with the first law \(\Delta U_S=W_{\mathrm{on}}-Q_B\) and the correlation bookkeeping \(\Delta S_S=I_2-I_1\) — and it settles the sign question that ran the gauntlet: **consuming correlation contributes \(+I_M\)** to the divergence at non-negative work. Information caps the increase (Sagawa–Ueda: \(\Delta D\le\beta W_{\mathrm{on}}+I_M\)); it never supplies a free decrease.

**Integration guard 1.** The second-law export bound used throughout this edition is the *unconditional* form

\[
\boxed{\;\beta Q_B\;\ge\;I_M+D_{\mathrm{err}}\;}
\]

— the bath must absorb the exported entropy: the consumed correlation and the removed damage. The condensed form \(Q_B\ge W_{\mathrm{on}}+I_M+D_{\mathrm{err}}\) is **regime-dependent** (under a purifying repair it reduces to \(D_{\mathrm{err}}\ge\sigma_{\mathrm{irr}}\) and fails when intrinsic dissipation exceeds damage) and appears only as a noted special case, never as the operative bound.

## 8.2 The funded-repair certificate

There are no free repairs. For each repair cycle — QND extraction, dissipative correction, ancilla reset — the bath must eventually absorb at least \(I_M+D_{\mathrm{err}}+\delta_I\) nats, so the per-cycle work cost satisfies

\[
W_{\mathrm{cycle}}\;\ge\;k_BT\,(I_M+D_{\mathrm{err}}+\delta_I)+(1-\eta)C ,
\]

with equality only in the reversible limit. The Sagawa–Ueda optimum allows the consumed correlation to fund part of this in the ideal extractive limit; the safety ledger charges gross, which is conservative and correct for a budget invariant.

**Certificate.** With escrow \(E\), income flux \(r(t)\) and cumulative demand \(\mathcal D(t)=\sum_{\mathrm{cycles}}W_{\mathrm{cycle}}\):

\[
E(0)+\int_0^t r(s)\,ds-\mathcal D(t)\;\ge\;0\quad\text{for all }t
\;\Longrightarrow\;
\text{protection is maintained.}
\]

Within each cycle the divergence excursion is bounded by \(D_{\mathrm{err}}^{\max}\), whose arrival is bounded by the charged fault kernels. Insolvency — the budget below the required charge at a damage event — is a well-defined **charged failure event** with its own conditional kernel \(\delta_{\mathrm{fund}}\), joining the twenty-one accounts. No independence is used in the composition (tower property and union bound).

The proposed compound storage functional of the draft series is retired as a certificate: under consistent accounting its stroke change is identically \(-(2D_{\mathrm{err}}+I_M)\), independent of the escrow \(C\), the efficiency \(\eta\), and the intrinsic dissipation — a bookkeeping identity of damage removal, not a funding proof. The funded-repair invariant above carries what it was meant to carry.

## 8.3 The four strokes

- **Stroke I — extraction.** QND syndrome sampling with measurement cost \(W_{\mathrm{meas}}\) from the operating budget; the ancilla entropy rises by \(I_M+\delta_I\).
- **Stroke II — funded repair.** Escrow liquidation \(C\) at efficiency \(\eta\); the drive is dissipative, and the identity of 8.1 holds with the export bound of guard 1.
- **Stroke III — Bennett reset.** The ancilla returns to \(|0\rangle\) by logically reversible computation; the erasure cost \(k_BT(I_M+\delta_I)\) is paid from income and dumped to the bath.
- **Stroke IV — maintenance and slack.** Boundary maintenance \(\omega_0R(t)^{d_G-1}\); the authority-attenuation tax redistributes and conserves; reversible administration is charged at the Landauer floor in erased nats; the residual enters the slack register of Section 14.

## 8.4 Ledger evidence

The exact-rational, hash-chained traces of the replayable four-stroke ledger execute this section's bookkeeping cycle by cycle and assert, at every cycle: the identity \(\Delta D_{\mathrm{II}}=-D_{\mathrm{err}}\) on the declared schedule; the first-law heat; the export bound of guard 1; reset funded from income; tax conservation; administration at the floor; bath entropy non-decreasing; and reserve-before-activation gating. Three scenarios are sealed:

| Scenario | Behaviour demonstrated | \(\sum\delta\) | Chain head |
| --- | --- | --- | --- |
| solvent | eight funded cycles, breach \(0\) on the good event | \(2.06419526094\times10^{-7}\) | `6160d931…69132` |
| quarantine | underfunding routes to minimal-hold **before** any unfunded transition; breach \(0\); nothing charged | \(2.06419526094\times10^{-7}\) | `d1a0d44b…b0ef4` |
| charged | income below the minimal-hold drain; one priced event; breach still \(0\) on the good event | \(9.86419526094\times10^{-7}\le10^{-6}\) | `41143bb2…a2788` |

Engine hash `4689df1b…252c2`; trace hashes in the ledger's `SHA256SUMS`; replay with `four_stroke_ledger.py --verify`. These are exact replay receipts for the listed instances and invariants — evidence of the arithmetic, with the physical theorems carried by the premises of the header and this section.
