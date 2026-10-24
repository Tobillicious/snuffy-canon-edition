# Section 22 — The Physical Parameter Ledger: Instantiation, Rates, and Fault Ceilings

*This section instantiates the income condition for concrete hardware, bounds the charged fault accounts, and tabulates the engineering parameters. Every figure is either sourced (bracketed references, §22.5) or marked as a design value.*

---

## 22.1 The Master Income Condition

Section 17.1's Income-or-Irrelevance theorem makes solvency a necessary condition for an agent to remain a viable protector. The master solvency inequality balances income against four additive demand rates:

$$\boxed{\operatorname{Income}(t) \;\ge\; \dot W_{\mathrm{demand}}(t) \;=\; \dot W_{\mathrm{Landauer}} + \dot W_{\mathrm{boundary}} + \dot W_{\mathrm{holding}} + \dot W_{\mathrm{emulation}}}$$

1. **Thermal and adversarial dissipation floor:**
   $$\dot W_{\mathrm{Landauer}} = k_B T \cdot \left(\dot D_{\mathrm{damage}} + \dot D_{\mathrm{adv,sub-thresh}} + \gamma_{\mathrm{leak\_export}}\right)$$
   * $\dot D_{\mathrm{damage}}$: entropy rate injected by thermal and environmental noise.
   * $\dot D_{\mathrm{adv,sub-thresh}}$: worst-case adversarial entropy injection beneath the sensor threshold $\varepsilon_{\mathrm{sens}}$.
   * $\gamma_{\mathrm{leak\_export}}$: boundary loss rate of carrier modes escaping the enclosure.

   This floor is Landauer's bound, now a compiled theorem (`Landauer.landauer`, `QuantumLandauer.quantum_landauer`; Section 23.2).
2. **Boundary containment ($\dot W_{\mathrm{boundary}}$):** $\dot W_{\mathrm{boundary}} = \omega_0 \cdot R(t)^{d_G - 1}$, the work to maintain the boundary enclosing radius $R(t)$ in $d_G$ spatial dimensions.
3. **Holding drain ($\dot W_{\mathrm{holding}}$):** the baseline power of the sensor lattice, clocks, QND readout and consensus comparators.
4. **Emulation overhead ($\dot W_{\mathrm{emulation}}$):** the energy for concurrent rival simulation ($P\text{-emu}(c)$) within the surplus.

---

## 22.2 Reference Physical Instantiations

### Reference Implementation A: superconducting transmon lattice in a dilution refrigerator

A dilution refrigerator has a separate cooling budget at each temperature stage, and each stage must carry its own load. Implementation A is therefore certified stage by stage, using the measured cooling powers and per-line heat loads of a Bluefors XLD400 cabled for a 50-qubit processor with individual drive and flux lines and 124 RF lines [S2].

| Stage | Cooling power, measured [S2, S3] | Load of the 50-qubit processor, measured per line [S2] | Headroom |
| --- | --- | --- | --- |
| 50 K | 30 W at 45 K | ≈ 20 %, mostly passive (shield radiation is within the specified cooling power) | ≈ 5× |
| 4 K | 1.5 W at 4.2 K | ≈ 10 %, mostly passive; includes the HEMT amplifiers at 7.8 mW each [S4] | ≈ 10× |
| Still | 40 mW at 1.2 K | negligible | ≫ 10× |
| Cold plate | 200 µW at 140 mK | ≈ 30 % | ≈ 3.3× |
| Mixing chamber | 19 µW at 20 mK | ≈ 30 % (operation at 14 mK) | ≈ 3.3× |

* **Demand components.** The boundary term is the radiation-shield load, which falls on the 50 K and 4 K stage budgets. The holding term is the wiring's passive and active loads and the amplifiers, which the table carries stage by stage. The Landauer floor is negligible: with one nat per error event and an error rate of order $N/T_1$ ($N = 50$, $T_1 = 68\ \mu\mathrm{s}$ [S6]), $\dot W_{\mathrm{Landauer}} \approx 2.07 \times 10^{-25}\ \mathrm{J} \times 7 \times 10^{5}\ \mathrm{s}^{-1} \approx 1.5 \times 10^{-19}\ \mathrm{W}$ at 15 mK, against microwatts of cooling. The emulation term (classical control and decoding) runs at room temperature on the electrical income.
* **Electrical income.** Each pulse-tube compressor draws 9.2 kW at 50 Hz or 10.7 kW at 60 Hz [S3], and the reference system uses two. The electrical income must therefore be at least about 20 kW plus the gas handling and room-temperature electronics, which are not sourced here. A three-phase utility connection of a few tens of kW, with backup sized to match, supplies it.
* **Solvency ratio.** The binding stages run at about 30 % of capacity, so
  $$\frac{\operatorname{Income}}{\dot W_{\mathrm{demand}}}\Big|_{\text{binding stage}} \approx 3.3 > 1 \quad \text{(measured, 50-qubit scale [S2])}.$$
* **Scale.** [S2] states that the same thermal budget supports about 150 qubits once line capacity is tripled, and about 400 with 0.047″ cables and suppressed flux offsets. Larger installations need cooling and electrical income in proportion to the qubit count, which is a sizing requirement. No installation of 10⁴ qubits has published stage loads, so solvency at that scale is not yet a measured certificate.

### Reference Implementation B: photonic cluster-state architecture

* **Optical layer.** At 193.4 THz (1550 nm), $h\nu = 1.28 \times 10^{-19}\ \mathrm{J} = 30.9\,k_B T$ at 300 K, so thermal photons in the waveguides are suppressed by $e^{-h\nu/k_BT} \approx 3.7 \times 10^{-14}$.
* **Detector layer.** The fault-tolerant photonic architectures in the literature detect photons with superconducting detectors [S8], which need cryogenic cabinets; the vendor states about 30 W of cooling per cabinet. A sourced ledger for Implementation B therefore carries a cryogenic detector stage, and its electrical income includes the cryocoolers.
* **Error rate.** The demonstrated two-qubit fusion fidelity is 99.22 % [S8]. The surface-code threshold of [S5] does not transfer directly to fusion-based architectures; the architecture's own threshold applies and is not sourced here.
* **Budget (design estimates).** Waveguide loss refresh ≈ 1.2 mW, laser stabilisation and phase modulators ≈ 85 mW, and photonic routing ≈ 20 mW are design estimates with no published installation source. Implementation B is therefore not yet certified. Its solvency ratio awaits a sourced budget that includes the detector stage.

---

## 22.3 The Charged Fault Accounts and the Failure Ceiling

The certified good event $G$ carries zero uncompensated loss over the design horizon $T_{\mathrm{horizon}} = 10^9\ \mathrm{s}$ (≈ 31.7 years). The failure ceiling is the sum of the conditional error probabilities of the charged accounts,

$$P(G^c) \le \sum_{i=1}^{21} \delta_i \le 10^{-6},$$

and the composition holds with no independence assumed (`ThermoLedger.canon_invariant`, compiled). The allocations below are the design budget. The status column records what present hardware certifies.

| Account | Fault | Mitigation | Allocated $\delta$ | Status |
| :---: | :--- | :--- | :---: | :--- |
| **1–4** | Single-qubit Pauli and leakage errors | Stabilizer decoding | $4 \times 10^{-8}$ | Met at **d = 25** for p = 10⁻⁴, or d = 41 for p = 5 × 10⁻⁴ (§22.5.2), once the correlated floor of accounts 5–7 is removed |
| **5–7** | Correlated bursts (high-energy impacts, phonon events) | Gap engineering, rapid reset | $3 \times 10^{-8}$ | **Not yet met.** The measured logical floor is ≈ 10⁻¹⁰ per cycle [S6]; the target is ≤ 3.7 × 10⁻²⁴ per cycle per logical qubit (§22.5.2) |
| **8–10** | Clock drift, dephasing, timing jitter | Byzantine clock distribution (E9) | $3 \times 10^{-8}$ | Design allocation; no installation measurement sourced |
| **11–12** | Sensor failure and readout spoofing | Trimmed-median consensus, $K \ge 2f + 1$ | $2 \times 10^{-8}$ | Design allocation; the consensus logic is compiled (`E9SelfHealing`) |
| **13–14** | Thermal fluctuations above threshold | Thermal ballast escrow, automatic throttle | $2 \times 10^{-8}$ | Design allocation |
| **15–16** | Power transients and dropouts | Redundant battery escrow | $2 \times 10^{-8}$ | Design allocation |
| **17–18** | Corrupted spawning, illegal delegation | Kernel capability gate (H5) | $2 \times 10^{-8}$ | Design allocation; the gate logic is compiled (`H5Closure`) |
| **19–20** | Carrier leakage into the open bath | Lieb–Robinson containment (X3) | $2 \times 10^{-8}$ | Design allocation |
| **21** | External macroscopic boundary shear | Standoff buffer $L_{\mathrm{buffer}} > v_{\mathrm{harm}} \tau_{\mathrm{resp}}$ | $1 \times 10^{-8}$ | Design allocation |
| **Total** | | | $\le 2.1 \times 10^{-7} < 10^{-6}$ | Certified when each account is |

**Correlated errors.** Gap-engineered junctions remove the high-energy-impact T₁ bursts [S9]. The remaining correlated events occur about once per hour, "whose origins are not yet understood", and they set the floor of 10⁻¹⁰ per cycle with a deviation from exponential suppression at d ≥ 15 [S6]. The threshold theorem's geometric decay (§23.8) holds for the noise it assumes, local and weakly correlated. Present hardware satisfies that assumption up to d ≈ 11–15, and removing the floor is the open engineering requirement of accounts 1–7.

**Achievability, as a theorem.** That the ceiling is attainable in physical matter is a compiled theorem.
* `Threshold.family_ceiling`: for any code family under local stochastic noise of rate p (every set S of locations is entirely faulty with probability at most $p^{\lvert S\rvert}$), with 2Δ√p < 1 and polynomially many failure witnesses of each length, every target ceiling is met at some code distance and at every larger one. The 10⁻⁶ ceiling over the horizon is included.
* `Threshold.repetition_ceiling`: the repetition code end to end, below p = 1/4.

Any installation whose noise meets the local stochastic condition below threshold therefore attains the ceiling. The rigorous threshold from path counting is conservative, and the distances in §22.5.2 use the simulated threshold of [S5]. What present hardware does not yet supply is the noise condition itself at the 10⁻¹⁰ level [S6].

---

## 22.4 The Engineering Parameter Matrix

| Parameter | Symbol | Superconducting | Photonic | Admissible range |
| :--- | :---: | :---: | :---: | :---: |
| Code distance | $d$ | 25 at p = 10⁻⁴; 41 at p = 5 × 10⁻⁴ (computed, §22.5.2) | architecture-specific (not sourced) | target met at some $d$ (`ceiling_achievable`, `Threshold.family_ceiling`) |
| Syndrome cycle | $\tau_{\mathrm{cycle}}$ | 1.1 µs (measured [S6]) | — | $\tau_{\mathrm{sampling}} < L_{\mathrm{buffer}}/(2 v_{\mathrm{harm}})$ |
| Sensor quorum size | $K$ | 7 (design) | 9 (design) | $K \ge 2f + 1$, $f \ge 2$ |
| Sensor threshold | $\varepsilon_{\mathrm{sens}}$ | 0.05 (design) | 0.02 (design) | $\varepsilon_{\mathrm{sens}} \in (\sigma_{\mathrm{noise}}, \theta_{\mathrm{damage}})$ |
| Standoff buffer | $L_{\mathrm{buffer}}$ | 0.2 m (design) | 0.05 m (design) | $L_{\mathrm{buffer}} > v_{\mathrm{harm}} \tau_{\mathrm{response}}$ |
| Escrow multiplier | $\mu_{\mathrm{escrow}}$ | ≈ 3.3× at the binding stage (measured [S2]) | not yet certified | $\mu_{\mathrm{escrow}} = \operatorname{Income}/\dot W_{\mathrm{demand}} > 1$ |
| Boundary embedding | $\Pi$ | radiation shields, Dirichlet microwave enclosure | total internal reflection | reflection coefficient $> 0.999$ (design) |

**What this section certifies.**
* The income condition is physically satisfiable, with measured positive headroom (≈ 3.3× at the binding stage), for a superconducting installation at the 50-qubit scale, with electrical income sized at a few tens of kW.
* The code distance the §22.3 allocation requires is computable from [S5]: d = 25 at p = 10⁻⁴.
* The composition of the accounts into the ceiling is a compiled theorem.
* The ceiling is attainable as a theorem: under local stochastic noise below threshold, every target, 10⁻⁶ included, is met at some code distance (`Threshold.family_ceiling`).

**What it does not yet certify.**
* The 10⁻⁶ failure ceiling over 10⁹ s on present hardware. The measured correlated floor [S6] is the open engineering requirement, stated here with its size.
* Implementation B, whose budget awaits a published installation source.
* Solvency at installations of 10⁴ qubits and above, which is a sizing requirement without published stage loads.

---

## 22.5 Sources and Derivations

**Sources.**
[S1] Bluefors, XLD dilution refrigerator specifications (XLD450sl: > 14 µW at 20 mK, > 450 µW at 100 mK; XLD1000sl: > 30 µW at 20 mK, > 1000 µW at 100 mK; guaranteed values, measured at the mixing-chamber experimental flange). bluefors.com/products/xld-dilution-refrigerator/.
[S2] S. Krinner et al., "Engineering cryogenic setups for 100-qubit scale superconducting circuit systems", *EPJ Quantum Technology* 6, 2 (2019), arXiv:1806.07862. Measured stage cooling powers of a Bluefors XLD400 (Table 1) and measured passive and active heat loads per line.
[S3] Cryomech PT415 pulse tube: 1.5 W at 4.2 K (nominal; CUORE cryostat paper, arXiv:1603.03306, and [S2] Table 1). Compressor input with the CPA1110: 9.2 kW at 50 Hz, 10.7 kW at 60 Hz (Bluefors PT415 sheet).
[S4] Low Noise Factory LNF-LNC4_8G cryogenic HEMT amplifier datasheet (2026-02-03): typical bias 0.6 V, 13 mA, i.e. 7.8 mW at the 4 K stage.
[S5] A. G. Fowler, M. Mariantoni, J. M. Martinis, A. N. Cleland, "Surface codes: Towards practical large-scale quantum computation", *Phys. Rev. A* 86, 032324 (2012), arXiv:1208.0928. Eq. (11): $P_L \approx 0.03\,(p/p_{\mathrm{th}})^{d_e}$, $d_e = (d+1)/2$, with $p_{\mathrm{th}} = 0.57\,\%$ for the circuit simulated. Physical qubits per logical qubit: (2d − 1)².
[S6] Google Quantum AI (R. Acharya et al.), "Quantum error correction below the surface code threshold", *Nature* (2024), doi:10.1038/s41586-024-08449-y, arXiv:2408.13687. Distance-7 surface code at 0.143 % error per cycle, Λ = 2.14 ± 0.02, cycle time 1.1 µs, mean T₁ = 68 µs. Repetition codes to distance 29: Λ = 8.4 for d = 5–11, a deviation from exponential suppression at d ≥ 15, and "an apparent logical error floor of 10⁻¹⁰" set by correlated events about once per hour (3 × 10⁹ cycles) "whose origins are not yet understood".
[S7] Best reported two-qubit gate errors: trapped ions, estimated 8.4(7) × 10⁻⁵ (A. C. Hughes et al., arXiv:2510.17286, preprint); superconducting transmons, CZ fidelity 99.93 % averaged over 40 h, 99.95 % maximum (IQM, company-reported).
[S8] PsiQuantum, "Omega" chipset, *Nature* (2025), doi:10.1038/s41586-025-08820-7: superconducting single-photon detectors integrated on silicon; two-qubit fusion fidelity 99.22 %; the vendor states cryogenic cabinets of about 30 W cooling power each.
[S9] M. McEwen et al., "Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits", *Nature Physics* 18, 107 (2022); M. McEwen et al., "Resisting high-energy impact events through gap engineering in superconducting qubit arrays", *Phys. Rev. Lett.* 133, 240601 (2024), arXiv:2402.15644.

Source PDFs and checksums: `BANKS/2026-10-25-section22-sources/`. The published source list with links is `SOURCES-22.md`.

### 22.5.1 Constants

$k_B$ and $h$ are exact in the SI. $k_B T = 2.071 \times 10^{-25}$ J = 1.293 µeV at 15 mK and $4.142 \times 10^{-21}$ J = 25.85 meV at 300 K. At 193.4 THz, $h\nu = 1.281 \times 10^{-19}$ J = 30.9 $k_B T$(300 K), and $e^{-h\nu/k_BT} = 3.7 \times 10^{-14}$.

### 22.5.2 Code distance for the fault allocation

Horizon $10^9$ s at 1.1 µs per cycle [S6] gives $N = 9.09 \times 10^{14}$ cycles. Ten thousand physical qubits at the [S5] footprint $(2d-1)^2$ hold about 9 logical qubits. With [S5] Eq. (11) and $p_{\mathrm{th}} = 0.57\,\%$, account 1–4 ($\delta = 4 \times 10^{-8}$, shared over the logical qubits) requires:

| Physical error p | Logical qubits | Per-cycle target per logical qubit | Required distance d | Physical qubits per logical qubit |
| --- | --- | --- | --- | --- |
| 10⁻⁴ (best ion gate [S7]) | 1 | 4.4 × 10⁻²³ | 23 | 2 025 |
| 10⁻⁴ | 9 | 4.9 × 10⁻²⁴ | **25** | 2 401 |
| 5 × 10⁻⁴ (best transmon CZ [S7]) | 9 | 4.9 × 10⁻²⁴ | 41 | 6 561 |
| 10⁻³ | 9 | 4.9 × 10⁻²⁴ | 57 | 12 769 |

At d = 17 and p = 10⁻⁴, $P_L = 4.7 \times 10^{-18}$ per cycle, which is 4.3 × 10⁻³ expected failures per logical qubit over the horizon, so d = 17 does not meet the allocation and d = 25 does. Accounts 5–7 ($\delta = 3 \times 10^{-8}$) set a per-cycle target of $3 \times 10^{-8} / (9N) = 3.7 \times 10^{-24}$ per logical qubit. At the measured floor of $10^{-10}$ per cycle [S6], the expected number of correlated failures over the horizon is about $9 \times 10^{4}$ per logical qubit.

---

**Machine-checked counterpart (Section 23).** Compiled counterparts of the ledger's structure:
* `ReciprocityCeiling.ceiling_achievable`: the ceiling as a parameter, met at some code distance.
* `ThermoLedger.canon_invariant`: composition of the accounts without independence.
* `E9SelfHealing.code_headroom` and `wave_race_margin`: admissible parameter ranges.
* `Landauer.landauer` and `QuantumLandauer.quantum_landauer`: the dissipation floor of 22.1.
* `Threshold.family_ceiling` and `Threshold.repetition_ceiling`: the ceiling attained below threshold under local stochastic noise.

The installation figures themselves are sourced measurements and design values, not compiled theorems.
