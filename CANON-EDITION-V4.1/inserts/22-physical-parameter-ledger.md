# Section 22 — The Physical Parameter Ledger: Instantiation, Rates, and Fault Ceilings

*Canon Edition v4.1 candidate content. Summit 4 execution: discharging Task 2 — instantiating the five-rate income condition for concrete physical hardware (cryogenic superconducting and photonic lattices), bounding the 21 charged fault accounts, and tabulating the complete engineering dial matrix.*

---

## 22.1 The Five-Rate Master Income Condition

In Section 17.1, the Income-or-Irrelevance theorem established that solvency is a necessary condition for an agent to remain a viable protector.
Here, we evaluate the exact master solvency inequality:

$$\boxed{\operatorname{Income}(t) \;\ge\; \dot W_{\mathrm{demand}}(t) \;=\; \dot W_{\mathrm{Landauer}} + \dot W_{\mathrm{boundary}} + \dot W_{\mathrm{holding}} + \dot W_{\mathrm{emulation}}}$$

where the five additive physical demand components are defined as:

1. **Thermal and Adversarial Dissipation Floor ($\dot W_{\mathrm{Landauer}}$):**
   $$\dot W_{\mathrm{Landauer}} = k_B T \cdot \left(\dot D_{\mathrm{damage}} + \dot D_{\mathrm{adv,sub-thresh}} + \gamma_{\mathrm{leak\_export}}\right)$$
   * $\dot D_{\mathrm{damage}}$: Information entropy rate injected by background thermal and cosmic noise.
   * $\dot D_{\mathrm{adv,sub-thresh}}$: Worst-case adversarial entropy injection beneath the sensor alarm threshold $\varepsilon_{\mathrm{sens}}$.
   * $\gamma_{\mathrm{leak\_export}}$: Boundary loss rate of carrier modes escaping the local enclosure.
2. **Boundary Carrier Containment Flux ($\dot W_{\mathrm{boundary}}$):**
   $$\dot W_{\mathrm{boundary}} = \omega_0 \cdot R(t)^{d_G - 1}$$
   The active work required to operate the boundary shielding / reflective carrier mirrors enclosing spatial radius $R(t)$ in $d_G$ spatial dimensions.
3. **Internal Autonomic Holding Drain ($\dot W_{\mathrm{holding}}$):**
   The baseline power consumed by the local sensor lattice, clocks, QND readouts, and consensus voting comparators.
4. **Concurrent Emulation Overhead ($\dot W_{\mathrm{emulation}}$):**
   The energy allocated to run concurrent rival simulations ($P\text{-emu}(c)$) within the lattice's surplus slack.

---

## 22.2 Reference Physical Instantiations

To prove that the solvency condition is physically satisfiable (and not a theoretical fiction), we instantiate the ledger for two standard modern quantum-computational hardware architectures:

### Reference Implementation A: Cryogenic Superconducting Transmon Lattice
* **Substrate Temperature ($T$):** $T = 15\ \mathrm{mK}$ (dilution refrigerator mixing chamber).
* **Thermal Scale ($k_B T$):** $k_B T \approx 2.07 \times 10^{-25}\ \mathrm{J/nat} \approx 1.29\ \mu\mathrm{eV/nat}$.
* **Topological Stabilizer Code:** Rotated surface code of distance $d = 17$, encoding logical memory units.
* **Physical Error Rate ($p_{\mathrm{phys}}$):** $10^{-4}$ per gate cycle (well below the $10^{-2}$ threshold).
* **Decoherence Rate ($\dot D_{\mathrm{damage}}$):** $\sim 10^5\ \mathrm{nats/s}$ across $10^4$ physical qubits.
* **Component Budget:**
  1. $\dot W_{\mathrm{Landauer}} = (2.07 \times 10^{-25}\ \mathrm{J}) \times (10^5\ \mathrm{s}^{-1}) \approx 2.07 \times 10^{-20}\ \mathrm{W}$.
  2. $\dot W_{\mathrm{boundary}}$: Active microwave shielding for a $0.5\ \mathrm{m}$ cryostat insert $\approx 10^{-9}\ \mathrm{W}$.
  3. $\dot W_{\mathrm{holding}}$: Cryogenic HEMT amplifier and low-noise readout line drain $\approx 1.5\ \mu\mathrm{W}$.
  4. $\dot W_{\mathrm{emulation}}$: Fast FPGA controller processing overhead at $4\ \mathrm{K}$ stage $\approx 25\ \mu\mathrm{W}$.
* **Total Maintenance Demand ($\dot W_{\mathrm{demand}}$):**
  $$\dot W_{\mathrm{demand}} \approx 26.5\ \mu\mathrm{W}$$
* **Certified Income / Cooling Budget ($\operatorname{Income}$):**
  Commercial dilution refrigerators provide $\approx 500\ \mu\mathrm{W}$ cooling power at $100\ \mathrm{mK}$ and $\approx 20\ \mu\mathrm{W}$ base cooling at $15\ \mathrm{mK}$, with backed UPS electrical power supply of $5\ \mathrm{kW}$.
* **Solvency Ratio:**
  $$\frac{\operatorname{Income}}{\dot W_{\mathrm{demand}}} \ge 18.8 \gg 1 \quad \text{(Positive Headroom Certified)}$$

### Reference Implementation B: Room-Temperature Photonic Cluster-State Architecture
* **Substrate Temperature ($T$):** $T = 300\ \mathrm{K}$.
* **Thermal Scale ($k_B T$):** $k_B T \approx 4.14 \times 10^{-21}\ \mathrm{J/nat} \approx 25.8\ \mathrm{meV/nat}$.
* **Optical Carrier Frequency ($\nu$):** $\nu = 193.4\ \mathrm{THz}$ ($\lambda = 1550\ \mathrm{nm}$ telecom C-band).
* **Optical Quantum Energy ($h\nu$):** $h\nu \approx 1.28 \times 10^{-19}\ \mathrm{J} \approx 31 \, k_B T$ (thermal noise exponentially suppressed by $e^{-h\nu/k_BT} \sim 10^{-14}$).
* **Code Distance:** Measurement-based 3D cluster state of distance $d = 25$.
* **Component Budget:**
  1. $\dot W_{\mathrm{Landauer}} \le 10^{-11}\ \mathrm{W}$.
  2. $\dot W_{\mathrm{boundary}}$: Waveguide absorption and out-coupling loss refresh $\approx 1.2\ \mathrm{mW}$.
  3. $\dot W_{\mathrm{holding}}$: Laser stabilization and electro-optic phase modulators $\approx 85\ \mathrm{mW}$.
  4. $\dot W_{\mathrm{emulation}}$: Photonic routing and switch reconfigurability $\approx 20\ \mathrm{mW}$.
* **Total Maintenance Demand ($\dot W_{\mathrm{demand}}$):**
  $$\dot W_{\mathrm{demand}} \approx 106.2\ \mathrm{mW}$$
* **Certified Solar/Grid Income ($\operatorname{Income}$):**
  A standard dedicated $100\ \mathrm{W}$ solar array with lithium-iron-phosphate battery reserve supplies $100\ \mathrm{W}$ continuous power.
* **Solvency Ratio:**
  $$\frac{\operatorname{Income}}{\dot W_{\mathrm{demand}}} \approx \frac{100\ \mathrm{W}}{0.106\ \mathrm{W}} \approx 941 \gg 1 \quad \text{(Over Two Orders of Magnitude Headroom)}$$

---

## 22.3 The 21 Charged Fault Accounts and the Failure Ceiling

The certified good event $G$ guarantees zero uncompensated loss over the design horizon $T_{\mathrm{horizon}} = 10^9\ \mathrm{seconds}$ ($\approx 31.7\ \text{years}$).
The failure ceiling is bounded by the sum of conditional error probabilities across all 21 recognized physical fault accounts:

$$P(G^c) \le \sum_{i=1}^{21} \delta_i \le \Sigma \delta \le 10^{-6}$$

| Account # | Fault Description | Mitigation Mechanism | Allocated $\delta_i$ |
| :---: | :--- | :--- | :---: |
| **1–4** | Single-qubit Pauli bit/phase/leakage errors | Stabilizer syndrome decoding (weight $\le \lfloor(d-1)/2\rfloor$) | $4 \times 10^{-8}$ |
| **5–7** | Multi-qubit correlated cosmic ray / phonon bursts | Phonon-trapping substrate boundaries + rapid reset | $3 \times 10^{-8}$ |
| **8–10** | Clock drift, de-phasing, and timing jitter | Byzantine optical clock distribution (Bridge E9) | $3 \times 10^{-8}$ |
| **11–12** | Local sensor failure and readout spoofing | Trimmed-median consensus ($K \ge 2f + 1$) | $2 \times 10^{-8}$ |
| **13–14** | Cryogenic / thermal fluctuations above threshold | Thermal ballast escrow + automatic throttle | $2 \times 10^{-8}$ |
| **15–16** | Power supply transient / line dropouts | Double-redundant battery escrow reserve | $2 \times 10^{-8}$ |
| **17–18** | Corrupted spawning / illegal child delegation | Kernel capability gate $\Gamma_{\mathrm{spawn}}$ (Theorem H5) | $2 \times 10^{-8}$ |
| **19–20** | Waveguide leak / carrier dispersion into open bath | Lieb-Robinson mirror containment (Theorem X3) | $2 \times 10^{-8}$ |
| **21** | External macroscopic boundary shear | Spatial standoff buffer $L_{\mathrm{buffer}} > v_{\mathrm{harm}} \tau_{\mathrm{resp}}$ | $1 \times 10^{-8}$ |
| **Total** | **All 21 Fault Accounts Composed** | **Master Sovereign Invariant** | **$\le 2.1 \times 10^{-7} < 10^{-6}$** |

---

## 22.4 The Complete Engineering Parameter Matrix

The table below unmasks the engineering parameters from the axioms, recording their calibrated admissible ranges:

| Parameter | Symbol | Cryogenic Reference | Photonic Reference | Certified Admissible Range |
| :--- | :---: | :---: | :---: | :---: |
| **Stabilizer Code Distance** | $d$ | 17 | 25 | $d \ge 2 \lambda_{\mathrm{fault}} \tau_{\mathrm{response}} + 1$ |
| **Sensor Sampling Interval** | $\tau_{\mathrm{sampling}}$ | $1\ \mu\mathrm{s}$ | $10\ \mathrm{ns}$ | $\tau_{\mathrm{sampling}} < \frac{L_{\mathrm{buffer}}}{2 v_{\mathrm{harm}}}$ |
| **Sensor Quorum Cluster Size** | $K$ | 7 | 9 | $K \ge 2f + 1$ (with $f \ge 2$) |
| **Sensor Threshold** | $\varepsilon_{\mathrm{sens}}$ | $0.05$ | $0.02$ | $\varepsilon_{\mathrm{sens}} \in (\sigma_{\mathrm{noise}}, \theta_{\mathrm{damage}})$ |
| **Standoff Buffer Thickness** | $L_{\mathrm{buffer}}$ | $0.2\ \mathrm{m}$ | $0.05\ \mathrm{m}$ | $L_{\mathrm{buffer}} > v_{\mathrm{harm}} \tau_{\mathrm{response}}$ |
| **Escrow Safety Multiplier** | $\mu_{\mathrm{escrow}}$ | $18.8\times$ | $940\times$ | $\mu_{\mathrm{escrow}} = \operatorname{Income} / \dot W_{\mathrm{demand}} > 1$ |
| **Boundary Embedding** | $\Pi$ | Dirichlet microwave | Total internal reflection | Unitary reflection coefficient $> 0.999$ |

This completes the physical parameter ledger. The abstract mathematical theorems of UPT (Theorems 8, E9, H5, X3) are fully realized in concrete physical matter with certified multi-order positive margins.

---

**Machine-checked counterpart (Section 23).** Compiled counterparts for the ledger's structure: `ReciprocityCeiling.ceiling_achievable` (the ceiling as a parameter), `ThermoLedger.canon_invariant` (composition of the accounts without independence), `E9SelfHealing.code_headroom` and `wave_race_margin` (admissible parameter ranges). The installation figures themselves are not compiled.

---

## 22.5 Sourced figures (added 25 October 2026)

*This section sources the installation figures of §§22.2–22.4 against vendor specifications and peer-reviewed measurements. Nothing above is deleted. Where a sourced value differs from a figure above, the sourced value is the one the ledger certifies, and the difference is stated. The theorems of Section 23 are unaffected: they take the installation figures as instance certificates, and this section states which certificates present hardware supplies. Source PDFs and checksums: `BANKS/2026-10-25-section22-sources/`.*

**Sources.**
[S1] Bluefors, XLD dilution refrigerator specifications (XLD450sl: > 14 µW at 20 mK, > 450 µW at 100 mK; XLD1000sl: > 30 µW at 20 mK, > 1000 µW at 100 mK; guaranteed values, measured at the mixing-chamber experimental flange). bluefors.com/products/xld-dilution-refrigerator/.
[S2] S. Krinner et al., "Engineering cryogenic setups for 100-qubit scale superconducting circuit systems", *EPJ Quantum Technology* 6, 2 (2019), arXiv:1806.07862. Measured stage cooling powers of a Bluefors XLD400 (Table 1) and measured passive and active heat loads per line.
[S3] Cryomech PT415 pulse tube: 1.5 W at 4.2 K (nominal; CUORE cryostat paper, arXiv:1603.03306, and [S2] Table 1). Compressor input with the CPA1110: 9.2 kW at 50 Hz, 10.7 kW at 60 Hz (Bluefors PT415 sheet).
[S4] Low Noise Factory LNF-LNC4_8G cryogenic HEMT amplifier datasheet (2026-02-03): typical bias 0.6 V, 13 mA, i.e. 7.8 mW at the 4 K stage.
[S5] A. G. Fowler, M. Mariantoni, J. M. Martinis, A. N. Cleland, "Surface codes: Towards practical large-scale quantum computation", *Phys. Rev. A* 86, 032324 (2012), arXiv:1208.0928. Eq. (11): P_L ≈ 0.03 (p/p_th)^{d_e}, d_e = (d+1)/2, with p_th = 0.57 % for the circuit simulated. Physical qubits per logical qubit: (2d − 1)².
[S6] Google Quantum AI (R. Acharya et al.), "Quantum error correction below the surface code threshold", *Nature* (2024), doi:10.1038/s41586-024-08449-y, arXiv:2408.13687. Distance-7 surface code at 0.143 % error per cycle, Λ = 2.14 ± 0.02, cycle time 1.1 µs, mean T₁ = 68 µs. Repetition codes to distance 29: Λ = 8.4 for d = 5–11, a deviation from exponential suppression at d ≥ 15, and "an apparent logical error floor of 10⁻¹⁰" set by correlated events about once per hour (3 × 10⁹ cycles) "whose origins are not yet understood".
[S7] Best reported two-qubit gate errors: trapped ions, estimated 8.4(7) × 10⁻⁵ (Hughes et al., arXiv:2510.17286, preprint); superconducting transmons, CZ fidelity 99.93 % averaged over 40 h, 99.95 % maximum (IQM, company-reported).
[S8] PsiQuantum, "Omega" chipset, *Nature* (2025), doi:10.1038/s41586-025-08820-7: superconducting single-photon detectors integrated on silicon; two-qubit fusion fidelity 99.22 %; the vendor states cryogenic cabinets of about 30 W cooling power each.
[S9] M. McEwen et al., "Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits", *Nature Physics* 18, 107 (2022); M. McEwen et al., "Resisting high-energy impact events through gap engineering in superconducting qubit arrays", *Phys. Rev. Lett.* 133, 240601 (2024), arXiv:2402.15644.

### 22.5.1 Constants (verified)

k_B and h are exact in the SI. k_B T = 2.071 × 10⁻²⁵ J = 1.293 µeV at 15 mK and 4.142 × 10⁻²¹ J = 25.85 meV at 300 K. At 193.4 THz, hν = 1.281 × 10⁻¹⁹ J = 30.9 k_B T(300 K), and e^{−hν/k_BT} = 3.7 × 10⁻¹⁴. The figures in §22.2 agree.

### 22.5.2 Implementation A, stage by stage

A dilution refrigerator does not have one cooling budget. Each stage must carry its own load. The §22.2 total (26.5 µW) adds a 4 K-stage FPGA and an amplifier to the 15 mK budget and compares the sum with the 100 mK cooling power. That comparison mixes stages. The sourced ledger is stage-wise.

| Stage | Cooling power, measured [S2] | Load for a 50-qubit processor with individual drive and flux lines, 124 RF lines, measured per-line loads [S2] | Headroom |
| --- | --- | --- | --- |
| 50 K | 30 W at 45 K | ≈ 20 % | ≈ 5× |
| 4 K | 1.5 W at 4.2 K [S3] | ≈ 10 %, mostly passive; includes HEMTs at 7.8 mW each [S4] | ≈ 10× |
| Still | 40 mW at 1.2 K | negligible | ≫ 10× |
| Cold plate | 200 µW at 140 mK | ≈ 30 % | ≈ 3.3× |
| Mixing chamber | 19 µW at 20 mK | ≈ 30 % (operation at 14 mK) | ≈ 3.3× |

The binding stages give a **certified solvency ratio of ≈ 3.3 at the 50-qubit scale, measured**. [S2] states that the same thermal budget supports 150 qubits once line capacity is tripled, and about 400 with 0.047″ cables and suppressed flux offsets. The §22.2 figures for the HEMT (1.5 µW) and the 4 K controller (25 µW) are not borne out: a cryogenic HEMT dissipates milliwatts [S4], and it sits on the 4 K stage.

**Electrical income.** Each pulse-tube compressor draws 9.2 kW at 50 Hz or 10.7 kW at 60 Hz [S3]. The [S2] system uses two pulse tubes. The electrical income must therefore be at least about 20 kW plus the gas-handling and room-temperature electronics, which are not sourced here. The §22.2 "5 kW UPS" does not cover this. A three-phase utility connection of a few tens of kW does, with backup sized to match. Income ≥ demand is met by sizing. The certified ratio is the stage-wise 3.3, not 18.8.

**Scaling to the §22.2 size (10⁴ physical qubits).** At the measured per-line loads, 10⁴ qubits take dozens of [S2]-class stage budgets, or wiring and cryogenic control that cut the per-line load. Solvency at that scale is a sizing requirement (cooling and electrical income in proportion to the qubit count). No single installation of that size has published stage loads, so it is not yet a measured certificate.

### 22.5.3 Code distance and fault accounts 1–7

Horizon 10⁹ s with 1.1 µs cycles [S6] gives N = 9.09 × 10¹⁴ cycles. With [S5] Eq. (11) and p_th = 0.57 %, account 1–4 (δ = 4 × 10⁻⁸, shared over the logical qubits) requires:

| Physical error p | Logical qubits | Per-cycle target per logical qubit | Required distance d | Physical qubits per logical qubit |
| --- | --- | --- | --- | --- |
| 10⁻⁴ (§22.2's figure; best ion gate [S7]) | 1 | 4.4 × 10⁻²³ | 23 | 2 025 |
| 10⁻⁴ | 9 (10⁴ qubits at d = 17) | 4.9 × 10⁻²⁴ | **25** | 2 401 |
| 5 × 10⁻⁴ (best transmon CZ [S7]) | 9 | 4.9 × 10⁻²⁴ | 41 | 6 561 |
| 10⁻³ | 9 | 4.9 × 10⁻²⁴ | 57 | 12 769 |

At the §22.2 distance d = 17 and p = 10⁻⁴, P_L = 4.7 × 10⁻¹⁸ per cycle, which is 4.3 × 10⁻³ expected failures per logical qubit over the horizon. That exceeds the 4 × 10⁻⁸ allocation. **The ledger's distance is therefore d = 25, not 17.** This is the dial of `ReciprocityCeiling.ceiling_achievable`: the target is met at some distance, and [S5] says which.

**Correlated errors (accounts 5–7) on present hardware.** [S6] measures a logical error floor of about 10⁻¹⁰ per cycle from correlated events about once per hour. Over the horizon this is about 9 × 10⁴ expected failures per logical qubit, against a requirement of ≤ 4.9 × 10⁻²⁴ per cycle. Gap engineering removes the high-energy-impact T₁ bursts of [S9] (PRL 133, 240601). The remaining once-per-hour events "are not yet understood" [S6]. Status: the geometric-decay premise of the threshold theorem (§23.8) holds for the noise it assumes, local and weakly correlated. Present superconducting hardware satisfies it up to d ≈ 11–15 and **does not yet satisfy it at the 10⁻¹⁰ level**. Accounts 1–7 at the δ values of §22.3 are design allocations that become certified once the correlated floor is removed to below the per-cycle targets above. They are not yet measured certificates.

### 22.5.4 Implementation B

Fault-tolerant photonic architectures in the literature detect photons with superconducting detectors [S8], which need cryogenic cabinets (vendor-stated at about 30 W cooling each). The 300 K figure of §22.2 applies to the waveguide layer only. A sourced Implementation B ledger therefore carries a cryogenic detector stage, and its electrical income includes the cryocooler. The four component figures of §22.2 B (1.2 mW, 85 mW, 20 mW, ≤ 10⁻¹¹ W) and the d = 25 cluster state have no published installation source. They remain design estimates and are not certified by this section. The demonstrated two-qubit fusion fidelity is 99.22 % [S8], so p ≈ 8 × 10⁻³.

### 22.5.5 Status of each figure

| §22 figure | Status |
| --- | --- |
| k_B T, hν, thermal suppression | Verified (22.5.1) |
| Dilution-refrigerator cooling powers | Sourced [S1, S2]; the §22.2 values are within the vendor range |
| HEMT 1.5 µW; 4 K controller 25 µW | Not borne out: HEMT 7.8 mW at 4 K [S4]; stage-wise ledger replaces the single sum |
| Solvency ratio 18.8 | Replaced: stage-wise ≈ 3.3, measured at 50 qubits [S2] |
| 5 kW electrical supply | Insufficient: ≥ ≈ 20 kW plus ancillaries [S3] |
| p_phys = 10⁻⁴ | Demonstrated for trapped-ion two-qubit gates (estimate, preprint) [S7]; transmon best ≈ 5–7 × 10⁻⁴ |
| Threshold 10⁻² | [S5] gives 0.57 % for its circuit; the ledger uses 0.57 % |
| d = 17 | Corrected to d = 25 at p = 10⁻⁴ (22.5.3) |
| δ allocations, accounts 1–7 | Design allocations; the measured floor of 10⁻¹⁰ per cycle [S6] must be removed first |
| δ allocations, accounts 8–21 | Design allocations; no installation-level measurements sourced |
| Implementation B component budget | Design estimates; no installation source; requires a cryogenic detector stage [S8] |
| Total P(Gᶜ) ≤ 2.1 × 10⁻⁷ | The composition is compiled (`ThermoLedger.canon_invariant`); the per-account inputs are as above |

**What this section certifies.** The income condition is physically satisfiable with positive measured headroom (≈ 3.3 at the binding stage) for a superconducting installation at the 50-qubit scale, with electrical income sized at a few tens of kW. The required code distance for the §22.3 allocation is computable from [S5] and is d = 25 at p = 10⁻⁴. **What it does not certify.** The 10⁻⁶ failure ceiling over 10⁹ s on present hardware: the measured correlated floor [S6] is the open engineering requirement, and it is stated here with its size.
