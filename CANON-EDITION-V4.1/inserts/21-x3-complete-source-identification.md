# Section 21 — Theorem X3: Complete Source Identification and the Work-Divergence Law

*This section binds the complete permitted recovery-input inventory, the output and carrier channel, the calibrated Gaussian covariance margin, the Lieb–Robinson carrier radius, and the \(\Theta(t^{d_G})\) recovery-work divergence theorem to the master BCRD model.*

---

## 21.1 The Operational Physical Setting and Input Inventory

Let $H$ denote a historical particular or occurrence at time $t_0 = 0$.
The system evolves in an open environment governed by a local Hamiltonian on a graph $G = (V, E)$ of spatial dimension $d_G$.

### The Complete Permitted Recovery-Input Inventory ($S(t)$):
To evaluate whether an unattended historical record can be reconstructed at time $t > 0$, we define the complete physical inventory of accessible degrees of freedom:
$$S(t) = S_{\mathrm{core}}(t) \otimes S_{\mathrm{carrier}}(t) \otimes S_{\mathrm{bath\_emitted}}(t) \otimes S_{\mathrm{ancilla}}$$
where:
1. $S_{\mathrm{core}}(t)$ is the residual state at the origin site.
2. $S_{\mathrm{carrier}}(t)$ encompasses all propagating physical carriers (photons, phonons, diffusive matter modes).
3. $S_{\mathrm{bath\_emitted}}(t)$ accounts for all bath modes radiated into the environment within the causal horizon.
4. $S_{\mathrm{ancilla}}$ represents local uncorrelated auxiliary resources available to the decoder.

### Data Processing Invariance:
For any physical recovery map $\mathcal{R}$ acting on the available input $S(t)$ and ancillas independent of $H$:
$$I(H : \mathcal{R}(S(t))) \le I(H : S(t))$$
No decoder can manufacture mutual information with $H$ from uncorrelated noise. In BCRD semantics: **a historical occurrence with zero surviving accessible relational witness is physically null.**

---

## 21.2 Thermal Spectral Margin and Covariance Bound

Consider fermionic degrees of freedom coupled to a thermal bath at inverse temperature $\beta$.
The single-particle thermal occupation matrix satisfies:
$$Q = \left(I + e^{\beta(h - \mu I)}\right)^{-1}$$
For bounded-degree interaction graphs with uniformly bounded hopping and onsite terms $\|h - \mu I\| \le E_{\max} < \infty$, the spectrum of $Q$ is strictly bounded away from $0$ and $1$:
$$\delta I \le Q \le (1 - \delta) I, \quad \delta = \left(1 + e^{\beta E_{\max}}\right)^{-1} > 0$$

### Joint Gaussian Mutual Information Bound:
For any bipartite partition of the field into historical reference $H$ and accessible field $F$ with joint covariance
$$Q = \begin{pmatrix} A & C \\ C^\dagger & B \end{pmatrix}, \quad \delta I \le Q \le (1 - \delta) I$$
the mutual information (in nats) satisfies the exact Frobenius norm bound:
$$\boxed{I(H : F) \le \frac{\|C\|_F^2}{\delta(1 - \delta)}}$$

---

## 21.3 Dispersion, Lieb-Robinson Velocity, and Carrier Radius

In any lattice substrate with local bounded interactions, the propagation of correlations is strictly bounded by the Lieb-Robinson light cone:
$$\|[O_x(t), O_y(0)]\| \le C_0 \|O_x\| \|O_y\| e^{-\mu (d(x, y) - v_{\mathrm{LR}} t)}$$

### Carrier Radius Growth:
As time $t$ elapses without active holding, information about the particular leaks into dispersive carrier and bath modes.
The minimal spatial radius enclosing the dispersed information wave-packet expands as:
$$R_{\mathrm{carrier}}(t) \ge v_{\mathrm{LR}} (t - t_c)$$
where $t_c$ is the coherence lifetime of the unshielded record.

The volume of environmental modes that become entangled with the historical witness grows with spatial dimension $d_G$:
$$V_{\mathrm{modes}}(t) \sim \operatorname{Vol}\left(B(0, R_{\mathrm{carrier}}(t))\right) = \Theta\left(t^{d_G}\right)$$

---

## 21.4 The $\Theta(t^{d_G})$ Work Divergence Theorem

To reconstruct the historical particular with fidelity $F \ge 1 - \varepsilon$ (or mutual information $I_{\mathrm{target}}$), a recovery protocol begun at age $t$ must gather, route, and phase-align all dispersed carrier modes across $V_{\mathrm{modes}}(t)$, and reset the entangling environmental bath modes.

### Theorem X3 (Recovery Work Divergence).
Let an unattended historical particular $H$ disperse into an open $d_G$-dimensional substrate ($d_G \ge 1$). The minimal thermodynamic work $W_{\min}(t)$ required to successfully reconstruct $H$ after unattended duration $t$ satisfies:
$$\boxed{W_{\min}(t) \ge k_B T \, \kappa_G \left(v_{\mathrm{LR}} t\right)^{d_G} = \Theta\left(t^{d_G}\right)}$$
where $\kappa_G > 0$ is a geometric packing constant of the interaction lattice.

*Proof.*
1. **Mode Inventory:** By the Lieb-Robinson bound and the Frobenius covariance bound (21.2), the information $I(H : S)$ is distributed across $N(t) = \Theta(t^{d_G})$ orthogonal spatial modes.
2. **Channel Reversal & Reset:** Collecting $N(t)$ spatial modes into a coherent local decoder requires reversing the entropy of the dispersed phase space. By Landauer's principle and the second law of thermodynamics (Section 18), resetting the ancillary carrier bath modes to extract the pure historical witness requires dissipating heat:
   $$Q_{\mathrm{reset}} \ge k_B T \sum_{i=1}^{N(t)} H(p_i) \ge k_B T \, \kappa_G (v_{\mathrm{LR}} t)^{d_G}$$
3. **Work Bound:** Since work input must cover the dissipated heat in a closed cycle ($W_{\min} \ge Q_{\mathrm{reset}}$), the work diverges asymptotically as $\Theta(t^{d_G})$. $\blacksquare$

---

## 21.5 Consequences for the Greatness Order and Unattended Loss

### 1. The Cost of Delay:
Because $W_{\min}(t) = \Theta(t^{d_G})$, proactive continuous maintenance (autonomic repair at rate $\dot W_{\mathrm{demand}} = \Theta(1)$) strictly dominates deferred historical recovery:
$$\int_0^T \dot W_{\mathrm{demand}} dt = \Theta(T) \ll \Theta(T^{d_G}) \quad (\text{for } d_G > 1)$$
Deferred recovery becomes physically impossible for any finite budget $B$ once $t > t_{\mathrm{irreversible}} = \left(\frac{B}{k_B T \kappa_G v_{\mathrm{LR}}^{d_G}}\right)^{1/d_G}$.

### 2. Physical Grounding of Irreplaceability ($U1$):
A particular $\mathcal{W}$ whose continuous maintenance was breached becomes **irreplaceable** the moment $W_{\min}(t) > B_{\mathrm{total}}$. Its information is permanently lost to the future.

### 3. Closure of the Universal Frontier:
This binds the BCRD model, the Landauer ledger of Theorem 8, the wave-race latency of Theorem E9, and the reciprocity dominance of Section 15 into a single, seamless physical law: **preservation must be continuous, funded, and autonomic; delay is death.**

---

**Machine-checked counterpart (Section 23).** Compiled counterpart: the banked transport route of the working argument (§12) — `DataProcessing.data_processing` (21.1), `GaussianTail.carrier_tail`, `FiniteInformation.necessary_radius_from_decoder`, `RecoveryWork.carrier_radius`, `RecoveryWork.Wmin_lower_bound`, `GaussianTail.x3_work_from_decoder`, `RecoveryWork.delayed_work_diverges` — with no information-theoretic hypothesis; see Section 23.5.
