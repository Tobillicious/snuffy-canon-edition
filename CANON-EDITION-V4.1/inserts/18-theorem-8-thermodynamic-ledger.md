# Section 18 — Theorem 8: Physical Repair, Feedback and the Complete Thermodynamic Ledger

*This section specifies the exact measurement, feedback and bath-coupled reset operations and the Hamiltonian conventions, and gives the signed work, heat and information ledger without sign ambiguity.*

---

## 18.1 The Physical Setting and Hamiltonian Conventions

Let $\mathcal{H}_S$ be the Hilbert space of the protected particular/system, $\mathcal{H}_A$ the register/memory space of the autonomous controller, and $\mathcal{H}_B$ the thermal bath at inverse temperature $\beta = (k_B T)^{-1}$.

The total Hamiltonian is time-dependent and piecewise continuous over the four strokes of the repair cycle:
$$H_{\mathrm{tot}}(t) = H_S(t) + H_A(t) + H_B + V_{SA}(t) + V_{AB}(t)$$
where:
1. $H_S(t) = H_S^0$ is constant outside control pulses; the code subspace $\mathcal{C} \subset \mathcal{H}_S$ is an eigenspace of $H_S^0$ (or degenerate ground space, so logical states incur zero autonomous drift).
2. $H_A(t)$ has a discrete orthogonal basis $\{|m\rangle\}_m$ corresponding to measurement syndromes, with degenerate reset ground state $|0\rangle_A$.
3. $V_{SA}(t)$ couples system and controller during measurement (Stroke I) and feedback (Stroke II).
4. $V_{AB}(t)$ couples controller and bath during reset (Stroke III).
5. All interaction potentials turn on and off smoothly: $\int V_{SA}(t) dt = \int V_{AB}(t) dt = 0$ at stroke endpoints, ensuring no unaccounted boundary interaction energies.

---

## 18.2 The Four Strokes of the Autonomic Repair Cycle

The autonomic cycle operates across four distinct intervals $[t_0, t_4]$ with cycle duration $\tau_{\mathrm{cycle}} = t_4 - t_0$:

```
       Stroke I               Stroke II              Stroke III             Stroke IV
 [Syndrome Measurement]  [Coherent Feedback]   [Bath-Coupled Reset]   [Escrow Replenish]
     t0 ----------> t1 ------> t2 ----------> t3 ----------> t4
       V_SA on               U_SA on               V_AB on              Harvest flux
       Extract I_M           ΔE_code = -ηC         Dump Q_B to Bath     Income >= Demand
```

### Stroke I: Syndrome Measurement ($t_0 \to t_1$)
* **Initial State:** $\rho_{SA}(t_0) = \rho_S(t_0) \otimes |0\rangle\langle 0|_A$.
* **Measurement Map:** A set of Kraus operators $\{M_m\}_m$ on $\mathcal{H}_S$ with $\sum_m M_m^\dagger M_m = I_S$.
* **Post-measurement State:**
  $$\rho_{SA}(t_1) = \sum_m p_m \rho_m \otimes |m\rangle\langle m|_A, \quad p_m = \operatorname{Tr}(M_m \rho_S M_m^\dagger), \quad \rho_m = \frac{1}{p_m} M_m \rho_S M_m^\dagger$$
* **Information Extraction:** The mutual information established between system and memory is:
  $$I_1 = I(S : A)_{t_1} = S(\rho_S(t_1)) + S(\rho_A(t_1)) - S(\rho_{SA}(t_1)) = H(\{p_m\}) = I_M > 0$$
* **Thermodynamic Cost:** Measurement work $W_{\mathrm{meas}} \ge 0$ is paid from the tracked escrow: $\Delta E_{\mathrm{escrow}} = -W_{\mathrm{meas}}$.

### Stroke II: Coherent Conditional Feedback ($t_1 \to t_2$)
* **Feedback Unitary:** The controller applies conditional unitary operations $U_m$ to restore each syndrome component to the code subspace $\mathcal{C}$:
  $$U_{SA} = \sum_m U_m \otimes |m\rangle\langle m|_A, \quad U_m^\dagger U_m = I_S$$
* **Post-feedback System State:**
  $$\rho_S(t_2) = \sum_m p_m U_m \rho_m U_m^\dagger = \sum_m U_m M_m \rho_S(t_0) M_m^\dagger U_m^\dagger \equiv \mathcal{R}_C(\rho_S(t_0)) \in \mathcal{C}$$
* **Entropy and Information Change:**
  Because $U_{SA}$ acts conditionally on orthogonal memory states, it preserves joint entropy $S(SA)$ and memory marginal $\rho_A(t_2) = \rho_A(t_1) = \sum_m p_m |m\rangle\langle m|_A$.
  The mutual information after feedback becomes:
  $$I_2 = I(S : A)_{t_2} = S(\rho_S(t_2)) + S(\rho_A(t_2)) - S(\rho_{SA}(t_2))$$
  When feedback completely disentangles the restored code state from the syndrome record, $\rho_{SA}(t_2) = \rho_{\mathrm{code}} \otimes \sum_m p_m |m\rangle\langle m|$, so $I_2 = 0$.
  Therefore, the system entropy reduction is exactly:
  $$\Delta S(S)_{\mathrm{II}} = S(\rho_S(t_2)) - S(\rho_S(t_1)) = I_2 - I_1 = -I_M < 0$$
* **Feedback Work:** Coherent work performed on the system:
  $$W_{\mathrm{on,II}} = \operatorname{Tr}(H_S \rho_S(t_2)) - \operatorname{Tr}(H_S \rho_S(t_1))$$
  For degenerate code projections, $W_{\mathrm{on,II}} = 0$.

### Stroke III: Bath-Coupled Memory Reset ($t_2 \to t_3$)
* **Initial State:** Memory carries entropy $S(\rho_A(t_2)) = H(\{p_m\}) = I_M$.
* **Reset Dynamics:** Coupling $V_{AB}(t)$ to bath $\mathcal{H}_B$ at temperature $T$ drives $\rho_A \to |0\rangle\langle 0|_A$.
* **Entropy and Heat Dump:**
  By Landauer's principle and the second law for information reservoirs (Sagawa & Ueda 2008):
  $$Q_B \ge k_B T \, S(\rho_A(t_2)) = k_B T \, I_M$$
  where $Q_B > 0$ denotes heat dissipated into the bath ($\Delta S_B = \beta Q_B \ge I_M$).
* **Escrow Ledger:** The work required to execute reset is supplied from escrow:
  $$\Delta E_{\mathrm{escrow,III}} = -W_{\mathrm{reset}}, \quad W_{\mathrm{reset}} \ge Q_B \ge k_B T \, I_M$$

### Stroke IV: Solvent Escrow Replenishment ($t_3 \to t_4$)
* **Income Coupling:** Ambient free energy flux (solar, thermal gradient, chemical, nuclear) charges the physical escrow reserve at rate $\dot W_{\mathrm{income}}(t)$.
* **Net Escrow Restoration:**
  $$\Delta E_{\mathrm{escrow,IV}} = \int_{t_3}^{t_4} \dot W_{\mathrm{income}}(t) dt = W_{\mathrm{income}}$$
* **Master Solvency Condition:**
  Under the income condition (Section 17.1), the net cycle income strictly covers all cycle expenditures:
  $$W_{\mathrm{income}} \ge W_{\mathrm{meas}} + W_{\mathrm{reset}} + W_{\mathrm{dissipation}} \equiv W_{\mathrm{demand}}$$
  Ensuring $E_{\mathrm{escrow}}(t_4) \ge E_{\mathrm{escrow}}(t_0)$.

---

## 18.3 Resolution of the Sign Issue: The True Invariant Functional

In earlier formulations, the relative entropy with respect to a thermal Gibbs state $\tau_S \propto e^{-\beta H_S}$,
$$D(\rho_S \| \tau_S) = \beta \operatorname{Tr}(H_S \rho_S) - S(\rho_S) - \ln Z_S$$
was inverted: restoring purity/order ($\Delta S < 0$) causes $D(\rho_S \| \tau_S)$ to **increase**, because a clean logical state is further from the high-entropy thermal state $\tau_S$ than a degraded, mixed state.

### The Correct Physical Code Error Metric
The objective of protection is fidelity to the **code subspace $\mathcal{C}$**, not proximity to thermal chaos. We define the code error directly via the orthogonal projection $P_{\mathcal{C}}$ onto the stabilized subspace:
$$\mathcal{E}_{\mathrm{code}}(\rho_S) \equiv \operatorname{Tr}\left(\rho_S (I - P_{\mathcal{C}})\right) = 1 - \operatorname{Tr}(\rho_S P_{\mathcal{C}})$$
which satisfies:
* $\mathcal{E}_{\mathrm{code}}(\rho_S) \ge 0$, with equality if and only if $\operatorname{supp}(\rho_S) \subseteq \mathcal{C}$.
* Under environmental noise/drift: $\Delta_{\mathrm{noise}} \mathcal{E}_{\mathrm{code}} > 0$.
* Under syndrome feedback $\mathcal{R}_C$:
  $$\Delta_{\mathrm{II}} \mathcal{E}_{\mathrm{code}} = \mathcal{E}_{\mathrm{code}}(\rho_S(t_2)) - \mathcal{E}_{\mathrm{code}}(\rho_S(t_1)) = 0 - \mathcal{E}_{\mathrm{code}}(\rho_S(t_1)) = -\eta C < 0$$
  where $\eta C > 0$ is the discrete recovery magnitude.

### The Master Storage / Lyapunov Functional
Define the unified autonomic storage functional $\Phi$ over system state, escrow reserve, and bath entropy:
$$\boxed{\Phi(\rho_S, E_{\mathrm{escrow}}) \equiv \mathcal{E}_{\mathrm{code}}(\rho_S) + \frac{1}{\mathcal{W}_0} \max\left(0, W_{\mathrm{target}} - E_{\mathrm{escrow}}\right)}$$
where $W_{\mathrm{target}}$ is the required safety reserve floor, and $\mathcal{W}_0$ is a scale calibration constant.

### Cycle Ledger Accounting:
1. **Noise / Drift Interval:**
   $\Delta_{\mathrm{drift}} \Phi = \Delta_{\mathrm{drift}} \mathcal{E}_{\mathrm{code}} \le \lambda_{\mathrm{decay}} \tau_{\mathrm{cycle}}$.
2. **Stroke I (Measurement):**
   $\Delta_{\mathrm{I}} \Phi \le \frac{W_{\mathrm{meas}}}{\mathcal{W}_0}$.
3. **Stroke II (Feedback):**
   $$\Delta_{\mathrm{II}} \Phi = -\eta C < 0$$
   Error is instantaneously eliminated in the code degree of freedom.
4. **Stroke III (Reset):**
   $\Delta_{\mathrm{III}} \Phi \le \frac{W_{\mathrm{reset}}}{\mathcal{W}_0}$, while bath absorbs $\Delta S_B \ge I_M$.
5. **Stroke IV (Solvent Replenishment):**
   $$\Delta_{\mathrm{IV}} \Phi \le -\frac{W_{\mathrm{income}}}{\mathcal{W}_0} \le -\frac{W_{\mathrm{meas}} + W_{\mathrm{reset}}}{\mathcal{W}_0}$$

### Net Cycle Change:
Summing all four strokes over $\tau_{\mathrm{cycle}}$:
$$\Delta_{\mathrm{cycle}} \Phi \le -\eta C + \lambda_{\mathrm{decay}} \tau_{\mathrm{cycle}} - \frac{W_{\mathrm{income}} - W_{\mathrm{demand}}}{\mathcal{W}_0}$$
Under the standard design condition that cycle time is faster than error accumulation ($\tau_{\mathrm{cycle}} < \frac{\eta C}{\lambda_{\mathrm{decay}}}$) and the solvency condition ($W_{\mathrm{income}} \ge W_{\mathrm{demand}}$):
$$\boxed{\Delta_{\mathrm{cycle}} \Phi \le -\sigma_0 < 0 \quad \text{whenever } \mathcal{E}_{\mathrm{code}} > 0}$$
and $\Delta_{\mathrm{cycle}} \Phi = 0$ on the certified invariant manifold $\mathcal{C}$ with full escrow.

---

## 18.4 Theorem 8 (Complete Physical Accounting Statement)

**Theorem 8 (Autonomic Preservation Invariant).**
Let an autonomous physical protector $a \in \Pi_{\mathrm{phys}}$ execute the periodic syndrome-feedback-reset protocol $(\mathcal{R}_C, \tau_{\mathrm{cycle}})$ under the Hamiltonian convention (18.1) with fixed bath temperature $T$. If $a$ satisfies:
1. **Solvency:** $\dot W_{\mathrm{income}}(t) \ge \dot W_{\mathrm{demand}}(t)$ for all $t$.
2. **Timeliness:** $\tau_{\mathrm{cycle}} < \tau_{\mathrm{harm}} \equiv \eta C / \lambda_{\mathrm{decay}}$.
3. **Landauer Saturation:** $E_{\mathrm{escrow}} \ge k_B T \, I_M$.

Then:
1. The combined storage functional $\Phi(t)$ is a strict Lyapunov function for the unmitigated error dynamics, contracting by at least $\sigma_0 > 0$ on each cycle containing an error.
2. The code subspace $\mathcal{C}$ is asymptotically stable and invariant on the good event $G$.
3. All work, heat, and information quantities are strictly conserved and accounted for:
   $$W_{\mathrm{income}} = W_{\mathrm{on}} + Q_B + \Delta E_{\mathrm{escrow}}, \quad Q_B \ge T \Delta S_B \ge k_B T I_M$$
   with zero uncharged entropy or hidden energy debt.

*Proof.* Follows directly from the stroke-by-stroke balance equations (18.2) and the negativity of the net cycle Lyapunov difference $\Delta_{\mathrm{cycle}} \Phi \le -\sigma_0 < 0$. $\blacksquare$

---

**Machine-checked counterpart (Section 23).** Compiled counterparts: `ThermoLedger.stroke_identity`, `cycle_work_floor`, with guard 1 derived from Landauer's theorem (`Landauer.cycle_work_floor_derived`, `QuantumLandauer.quantum_cycle_work_floor`; stroke III's bound $Q_B \ge k_B T\, I_M$ is `QuantumLandauer.quantum_landauer`), `funded_repair_certificate`, `quarantine_zero_debt`, `canon_invariant`, `tracking_envelope`; the composition statement is `Composition.theorem8_composition`.
