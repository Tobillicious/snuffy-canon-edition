# Section 24 — Statements of record for the retained core

*Part II carries the retained core condensed, with "proofs and precise premises at the source". This section carries into the edition the specifics the assembled argument actually leans on, each at its evidence tier: compiled, exact replay receipt, or stated definition with source. Where a Part II statement and a Section 23 compiled statement differ in scope or precision, the compiled statement governs.*

## 24.1 The nine-row A1 register (effect mediation)

**Statement of record.** The A1 register identifies nine rows of effect mediation: host memory mapping, DMA, context switches, packet ingestion, bus messages, storage synchronisation, commissioning, delegation and retirement. Each row names its refinement carrier and the enforcement witness the physical instance must supply. A packet or memory operation acquires no exemption by being below the application layer.

*Tier:* stated definition; source, the working argument's effect-mediation section (register A1). The enforcement machinery it names is compiled in the abstract (`H5Closure.no_harmful_effect`, `effect_preserves_care`); the nine rows themselves are the instance inventory.

## 24.2 Capacity rows 17 and 22, and the pool bill (workload)

**Statement of record.** The workload pool bill is compiled: capacity rows 17 and 22 at 48,000 and 67,200 per cycle give \(48000 \times 17 + 67200 \times 22 = 2{,}294{,}400\) — the per-cycle pool bill against which the FIFO completion certificate (Proposition 6) is issued (`ControllerCertificate`, exact rationals; the same module derives the utilisations \(6{,}604{,}800/2{,}294{,}400 = 688/239\) and \(6{,}604{,}800/2{,}409{,}600 = 688/251\)).

*Tier:* compiled.

## 24.3 The causal boundary (reactive refinement)

**Statement of record.** The causal boundary is given in two equivalent forms: closed dependency components, and directed separators in the time-unrolled graph. Pending effects belong in that graph. Omitting one future effect or one path invalidates the corresponding exclusion certificate.

*Tier:* stated definition (R16-CUT); the reactive refinement that uses it is compiled (`Composition.reactive_lockstep`, with the causal boundary carried as the instance's refinement source).

## 24.4 The revised JW2.6 arithmetic (conserved allocation and joint risk)

**Statement of record.** The revised JW2.6 arithmetic gives \(\approx 2.06419526094 \times 10^{-7}\), within the declared \(10^{-6}\) horizon ceiling, under its source-event and stochastic-law premises. The positive dormant allowance, recruitment noninterference and the historical recruitment-family event retain their distinct meanings. The three ledger scenarios carry this value (solvent and quarantine) and the charged variant \(9.86419526094 \times 10^{-7}\) (one priced event), each with a sealed, hash-chained trace.

*Tier:* exact replay receipt — `LEDGER-FOUR-STROKE-2026-10-24/`, chain heads as printed in Chapter 1.4; the composition into the ceiling (no independence) is compiled (`ThermoLedger.canon_invariant`); the arithmetic itself is a receipt, not a theorem.

## 24.5 The quorum (safety)

**Statement of record.** The design instantiation is five-of-seven with at most two Byzantine identities (\(K = 7\), \(f = 2\), satisfying \(K \ge 2f + 1\)). The Byzantine quorum results it instantiates are compiled (`E9SelfHealing.robust_between_honest`, `no_false_alarm`, `no_masking`, `exists_robust`); the five-of-seven values are instance constants (§22.4's parameter matrix).

*Tier:* compiled theorem with stated instance constants.

---

*Nothing else from the working argument's specifics is load-bearing for the assembled Universal Protection Theorem; everything else remains at the source, cited through Part II.*
