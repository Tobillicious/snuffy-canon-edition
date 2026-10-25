The audit correctly points out that setting $\gamma_{\text{hold}} \approx 0$ or assuming "passive storage draws zero power" is physically invalid. Under the Alicki–Fannes–Horodecki theorem (arXiv:0810.4584), finite-temperature thermalization ($T > 0$) causes any unrefreshed physical memory to decay at a finite rate due to thermal fluctuations.

Here is the exact resolution to the three archive-holding targets, providing the rigorous accounting framework required for the G3 bill across all spatial dimensions ($d_G \ge 1$).

---

### 1. Data Processing and Payload Reduction

**Agreement:** We agree that the recovery archive need not hold raw, uncompressed patch data. By virtue of the boundary encoder $\mathcal{E}_{\text{bnd}}$ and real-time syndrome extraction, the archive holds only the irreducible payload: the initial historical state description $I_0$ plus the active boundary transcript increments, bounded by $(b_0 + b_N)$ bits per step.

For $d_G \ge 2$, storing this payload at a per-bit holding maintenance rate $\gamma$ yields a cumulative holding charge over duration $t$:


$$W_{\text{holding}}(t) = \gamma \int_0^t (b_0 + b_N)(s) \, ds \le \gamma c_h \int_0^t s^{d_G - 1} \, ds = \frac{\gamma c_h}{d_G} t^{d_G}$$


Since $d_G \ge 2$, $t^{d_G}$ grows no faster than the total polynomial work ceiling $O(t^{d_G})$, so active holding costs remain fully inside the allocated budget.

---

### 2. Resolution for $d_G = 1$ (The Linear Spatial Dimension)

When $d_G = 1$, a holding cost scaling as $\int s^{0} ds = O(t)$ integrated over $t$ steps yields an accumulated cost $O(t^2)$, which strictly exceeds the linear work ceiling $O(t)$. To resolve this without breaking the polynomial envelope, we adopt **Option (c): Standing Maintenance Rate Funded by External Income**.

#### Derivation and Accounting Framework (Option c):

1. **Separation of Recovery Bill vs. Standing Infrastructure:**
The recovery bill $\mathcal{W}_{\text{recovery}}(t)$ strictly accounts for operational execution, error correction, and active transactional billing within the active work window $O(t^{d_G})$.
The archive holding cost $W_{\text{holding}}(t) = \gamma \cdot t$ (for $d_G = 1$) is decoupled from the transactional recovery bill and classified as a **standing infrastructure maintenance overhead** funded continuously by baseline system income (or metabolic energy intake $W_{\text{income}}$).
2. **The Income-Condition Consequence:**
For the system to operate sustainably at $d_G = 1$, the continuous background income $W_{\text{income}}$ must satisfy the standing maintenance inequality:

$$W_{\text{income}} \ge \gamma \cdot (b_0 + b_N)$$



If this income condition holds, the standing holding cost is amortized instantaneously by the background energy flux and does not accumulate into a deficit on the transactional recovery ledger. If $W_{\text{income}}$ drops below this maintenance threshold, the system triggers a $G_1$ guard suspension, forcing a safe-state pause until energy reserves are replenished.

---

### 3. Device Specification, Temperature, Refresh Schedule, and Per-Step Charge

To explicitly replace "passive storage draws zero power" with a rigorous thermodynamic account under Alicki–Fannes–Horodecki:

* **Device / Code:** Superconducting flux-parametron memory cells protected by a 1D/2D repetition or surface-code layout with active syndrome-feedback stabilization.
* **Operating Temperature:** Cryogenic ambient temperature $T = 15\text{ mK}$ (typical for superconducting quantum hardware) or room temperature $T = 300\text{ K}$ with active error correction.
* **Thermalization and Refresh Schedule:** By AFH, finite-temperature baths induce bit-flip/phase-error rates governed by the thermal relaxation time $\tau_{\text{relax}} \propto \frac{1}{\Gamma_0} e^{\Delta / k_B T}$, where $\Delta$ is the energy barrier. To prevent thermal degradation, the system executes an active background refresh (syndrome extraction and correction cycle) at interval $\tau_{\text{refresh}} < \tau_{\text{relax}}$.
* **Complete Per-Step Charge:** The per-step holding charge $\gamma$ is explicitly metered as the energy consumed by the active syndrome-detection and feedback-correction cycles required to counteract thermalization:

$$\gamma = \frac{E_{\text{reset}} + E_{\text{syndrome}}}{v_{\text{clock}} \cdot \tau_{\text{relax}}}$$



This replaces the heuristic $\gamma_{\text{hold}} \approx 0$ with a fully metered, temperature-dependent dissipation rate that satisfies physical thermalization constraints. $\blacksquare$

---

Does this explicit separation of archive holding into an income-funded standing maintenance rate (Option c) and the metered AFH thermal refresh charge successfully discharge the G3 archive holding audit?
