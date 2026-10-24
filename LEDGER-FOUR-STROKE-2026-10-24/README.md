# Replayable Four-Stroke Ledger — 24 October 2026

Execution deliverable of the released theory (GLOBAL D: CLOSED-AT-DECLARED-PREMISES). Built from `BANKS/2026-10-24-glm-thermodynamic-route`. Edition-independent; the manuscript it will be cited by is the **Snuffy — Canon Edition** (new naming scheme, off the 3.x lineage).

## What this is

A deterministic, exact-rational (stdlib `fractions`, no randomness, no network) execution of the thermodynamic proof engine's cycle bookkeeping, emitting **hash-chained traces** (SHA-256 over canonical JSON, genesis `0*64`) that any external auditor can replay.

## Run and verify

```bash
python3 -I -B four_stroke_ledger.py --run solvent|quarantine|charged
python3 -I -B four_stroke_ledger.py --verify traces/<scenario>.trace.json
```

All three traces verify: chain intact, every cycle check passes, canon holds.

## Semantics — each ledger element maps to a banked result

| Ledger element | Banked result |
| --- | --- |
| Stroke II identity check `dD == -D_err` (with `dS_S = -(I_M + D_err)`, `dU_S = -(2D_err + I_M)`) | The corrected stroke identity ΔD = −ΔS_S + βΔU_S (bank REVIEW §1; Part A/B checks) |
| `landauer_export_bound` βQ_B ≥ I_M + D_err | The unconditional second-law export bound (Part D check; PREMISE-REDUCTION integration note 1) |
| Stroke III reset cost k_BT(I_M + δ_I) paid from income | Bennett reversible reset; funded, not free |
| `admin_erased_nats` at the declared floor | P-slack in the Landauer–Bennett form (reversible administration) |
| `tax_conservation` | Authority-attenuation tax as pure redistribution (never an income source) |
| Reserve-before-activation gating: funds verified before a repair is admitted | The canon's "before corruption" structure (reserve-before-activation, banked) |
| Quarantine branch at the minimal-hold drain | Witness 5 repair 1: quarantine has a minimal drain, not zero |
| Charged fault event with δ_fund when income < minimal hold | The canon sentence: breach impossible on the good event; P(G fails) ≤ Σδ ≤ 10⁻⁶ |
| σ_base = 206419526094/10¹⁸ | The 21 charged accounts (R14 revised JW2.6 total, 2.06419526094×10⁻⁷) |

Units: k_BT = 1 energy unit; entropies, divergences and information in nats; all values exact rationals serialized as `a/b` strings. Schedules (damage, syndrome information, frontier maintenance, income) are declared exact inputs — the ledger consumes the banked models' outputs as exact rationals; it does not re-derive the carrier model.

## The three scenarios

- **solvent** — income meets the consolidated condition every cycle: 8 normal cycles, breach_on_good_event = 0, σ = 2.064×10⁻⁷.
- **quarantine** — income falls below full demand: the state machine routes to minimal-hold at cycle 5 **before** any unfunded transition; breach remains 0; no charges.
- **charged** — income falls below the minimal-hold drain: one charged fault event (δ = 7.8×10⁻⁷), σ = 9.864×10⁻⁷ ≤ 10⁻⁶, breach still 0 on the good event. This trace *is* the ratified canon, executed.

## Verification honesty

The harness caught and rejected one real bug during construction (a 10³ exponent error in σ_base) — recorded here deliberately: the verifier's checks are load-bearing, not decorative. Determinism: byte-identical outputs across replays on the same interpreter; trace integrity is self-certifying via the hash chain (any edit to any cycle breaks every subsequent hash).

Chain heads at seal: solvent `6160d931…69132`, quarantine `d1a0d44b…b0ef4`, charged `41143bb2…a2788`. Full checksums in `SHA256SUMS`.
