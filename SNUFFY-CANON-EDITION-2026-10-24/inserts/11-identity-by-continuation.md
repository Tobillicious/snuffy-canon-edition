# Section 11 — Identity by continuation and the active tracking controller

## 11.1 What the identity layer must prove

The manifold certificate of Section 8 bounds divergence from the constrained reference \(\tau\). Identity by continuation requires more: each particular must remain close to **its own** target trajectory \(\rho_A^*(t)\). Mutual distinguishability is not faithfulness — two states can remain maximally distant from one another while both drift maximally far from their own targets — so the identity layer is stated as a tracking bound, and the manifold and tracking certificates together carry the bridge's \(R(m)\lor H(m)\).

## 11.2 The tracking recursion, honestly solved

Let \(e_k=\lVert\rho_A(k\Delta t)-\rho_A^*(k\Delta t)\rVert_1\). Correctable errors (weight \(\le\lfloor(d-1)/2\rfloor\)) are removed exactly per epoch by the Knill–Laflamme recovery, which acts as an isometry on the code space; the residual injections are the uncorrectable leakage at rate \(\gamma_{\mathrm{leak}}\propto p^{\lfloor d/2\rfloor+1}\) and the per-recovery fault cost \(\varepsilon_{\mathrm{fault}}\). With the active dissipative tracking controller of Theorem 2.3 — the reset-type generator \(\mathcal L_{\mathrm{ctrl}}(\rho)=-\kappa_{\mathrm{ctrl}}(\rho-\rho^*_t)\), valid Lindblad dynamics toward the intended trajectory, which the maintained record supplies — the recursion is

\[
e_{k+1}\;\le\;\bigl(1-(\Gamma_{\mathrm{corr}}+\kappa_{\mathrm{ctrl}})\Delta t\bigr)\,e_k+\bigl(\gamma_{\mathrm{leak}}\Delta t+\varepsilon_{\mathrm{fault}}\bigr).
\]

The leakage term **stays in the recursion**: the controller suppresses accumulation, it does not delete injection. The geometric solution is

\[
\boxed{\;\lVert\rho_A(t)-\rho_A^*(t)\rVert_1\;\le\;\varepsilon_0\,e^{-(\Gamma+\kappa)t}
+\frac{\gamma_{\mathrm{leak}}+\varepsilon_{\mathrm{fault}}/\Delta t}{\Gamma+\kappa_{\mathrm{ctrl}}}
\Bigl(1-e^{-(\Gamma+\kappa)t}\Bigr)\;}
\]

with steady-state envelope

\[
e_\infty=\frac{\gamma_{\mathrm{leak}}+\varepsilon_{\mathrm{fault}}/\Delta t}{\Gamma_{\mathrm{corr}}+\kappa_{\mathrm{ctrl}}}.
\]

**Active compression.** Sufficient gain \(\kappa_{\mathrm{ctrl}}>\bigl(\gamma_{\mathrm{leak}}+\varepsilon_{\mathrm{fault}}/\Delta t\bigr)/\varepsilon_0-\Gamma_{\mathrm{corr}}\) compresses the envelope below the measurement resolution \(\varepsilon_0\); in the checked instance, envelope \(0.081<\varepsilon_0=0.1\) at sufficient gain, and \(0.625>\varepsilon_0\) at insufficient gain. The controller's own drain — the continuous export of the injected entropy, at least \(k_BT\gamma_{\mathrm{leak}}\) plus control overhead — is a rate component of the header's Master Solvency Condition. Nothing here is free.

## 11.3 The refresh regime

With refresh-from-record (re-encoding from the funded, maintained history each epoch), the error resets and does not accumulate:

\[
e_k\;\le\;\lambda_{\mathrm{env}}=\gamma_{\mathrm{leak}}\tau+\varepsilon_{\mathrm{fault}}\qquad\text{for all }k,
\]

uniformly over arbitrary horizons while funding holds. Concatenation makes \(\lambda_{\mathrm{env}}\) superpolynomially small at polylogarithmic overhead (threshold theorem). Adversarial identity damage — any deviation beyond these envelopes — is a charged event joining the fault accounts.

## 11.4 Statement of the layer

**Theorem (identity by continuation).** Under the header premises — sub-threshold noise, the funded cycle of Section 8, the controller and refresh above — every covered particular satisfies \(\lVert\rho(t)-\rho^*_t\rVert_1\le\varepsilon\) for all \(t\), where \(\varepsilon\) is a design parameter compressed below measurement resolution by controller gain. This is \(\varepsilon\)-faithfulness, and it is the honest form: exact equality is impossible under stochastic noise, and the law's faithful-holding comparison operates on these bounded outcomes. Prose derivation at stated premises; finite exact checks of the recursion solution and the compression threshold are recorded in the review banks.
