# Section 12 — Adversarial containment: the E9 trichotomy

## 12.1 The containment statement

**Theorem (E9, assembled).** Under the header premises — a stabilizer code of distance \(d\) covering the physical error channels; QND syndrome sampling with detection latency \(t_{\mathrm{detect}}\le a/c_{\mathrm{lattice}}+\tau_{\mathrm{sensor}}\); the per-site sensor power threshold \(\varepsilon_{\mathrm{sens}}\) with the quantum-speed-limit rate bound \(\lVert\dot\rho\rVert\le P_{\mathrm{adv}}/(\hbar\omega_{\mathrm{cutoff}})\); the Master Solvency Condition with the adversarial drain charged; and refresh-from-record — no adversarial strategy causes uncompensated state divergence without detection or charge, and

\[
t_{\mathrm{detect}}+t_{\mathrm{decision}}+t_{\mathrm{repair}}\;<\;t_{\mathrm{irreversible\ harm}}
\]

on the good event.

**Integration guard 2.** The containment claim is the full three-branch trichotomy. No single branch closes it: syndrome detection alone leaves the logical-weight class invisible (that invisibility is the definition of code distance), and the power argument alone has blind directions in the monitored basis.

## 12.2 The three branches

**Branch A — sub-threshold per-site injection.** \(P_{\mathrm{adv}}<\varepsilon_{\mathrm{sens}}\) per site: divergence accumulates at a bounded rate \(\le P_{\mathrm{adv}}/(\hbar\omega_{\mathrm{cutoff}})\) per site and is absorbed and refreshed — Branch A of Section 11's funded tracking. No uncompensated divergence while funded; the attrition contest is won whenever income exceeds the capped drain, since sub-threshold injection is itself capped per site.

**Branch B — low-weight syndrome detection.** Any perturbation whose expansion in the \(n\)-qubit Pauli basis contains a non-stabilizer component \(P_\mu\) of weight \(\le d-1\) anticommutes with some stabilizer generator and yields a non-trivial syndrome within the sampling latency — independent of injection direction; this is what a code is for. (Correctability is guaranteed to weight \(\lfloor(d-1)/2\rfloor\); detection extends to \(d-1\). The centralizer at low weight contains only the identity and stabilizer elements, which act trivially; logical operators have weight \(\ge d\).) Detection is certain on the non-stabilizer mass of the injected operator; stabilizer and identity components are harmless by definition.

**Branch C — coherent logical injection.** A logical operator of weight \(\ge d\) has, by the definition of code distance, a zero syndrome — this is not a hole in Branch B but a different class. Delivering such an operator within one epoch requires \(\ge d\) simultaneous local deliveries, each above the per-site power threshold within the lightcone window, and is **power-detected**. Slow logical drift — sub-threshold coherent accumulation — reduces to Branch A by the tracking and refresh of Section 11.

## 12.3 The latency budget

With sensor spacing \(a\), consensus rounds \(k_{\mathrm{rounds}}\) over the local graph, and repair durations \(\tau_{\mathrm{fb}}+\tau_{\mathrm{reset}}\),

\[
t_{\mathrm{total}}\le\frac{a(1+k_{\mathrm{rounds}}d_{\mathrm{local}})}{c_{\mathrm{lattice}}}+\tau_{\mathrm{sensor}}+\tau_{\mathrm{fb}}+\tau_{\mathrm{reset}}
\;<\;\frac{r_{\mathrm{critical}}-r_0}{c_{\mathrm{lattice}}},
\]

enforced by scaling \(a\) and the sampling rate — a design requirement on the instance, stated as such.

## 12.4 Residual channels

Sensor band gaps, error channels outside the declared basis, and any adversarial route not covered by A–C are exactly the charged fault accounts under the ceiling \(\sum\delta\le10^{-6}\). Containment is complete on the good event; the good event's failure is priced, not ignored. Prose derivation at stated premises; the exact commutation-sign checks of Branch B's algebra on the three-qubit code are recorded in the review banks.
