# Inventory of the author's/Gemini supplies in the 25 October Codex session

Source: `CODEX-EXPORT-25-OCT.txt` (the author's export, copied from Downloads)
and the Codex session file
`~/.codex/sessions/2026/10/25/rollout-2026-10-25T15-56-04-…jsonl`.
Checked by Claude, 25 October 2026. Each supply is mapped to where it is
already incorporated, so that none is rebuilt or dropped.

| Session msg | Supply | Preserved verbatim | Incorporated in the 4.2 master |
| --- | --- | --- | --- |
| 041 (attachment 187e…) | W_min ≤ C t^{d_G} single-shot feedforward | `2026-10-25-4.2-stronger-argument/inputs/GEMINI-X3-UPPER-BOUND.txt` (hash match) | §21.7.1–21.7.2 (telescoping shells) |
| 042 (inline) | TIWA guard ring, gauge-fixed boundary, single-shot projection | `codex-inline-supplies/MSG-042.txt` (new) | §21.7.4; `TIWA-PATCH-REQUIREMENTS.md`; `TIWASource`/`TIWAGuard`/`TIWARecovery`/`TIWAWork` |
| 063 (inline answer) | `G3_ValidWorkBill` construction, amortised reset | `MSG-063.txt` (new) | §21.7.5; `G3CompleteBill` (meters a rollback on every wave, stronger than an expected decay) |
| 065 (inline) | Internal existence from bounded work | `MSG-065.txt` (new) | III-F.3–F.4; `nonvanishing_of_continuation`, `finite_code_self_grounding` |
| 066 (inline answer) | Boundary encoder: accumulator, then relative homology | `MSG-066.txt` (new); homology part also `beam-late-eight-integration/inputs/HOMOLOGICAL-BOUNDARY-PROPOSAL.txt` | III-F.2; exact encoder/recovery compiled in III-G (`coordinateBoundaryEncoder`, `coordinate_boundary_roundtrip`, `adjoint_decodes_isometry`) |
| 068 (attachment 70c5…) | Homological lossless boundary proof | `HOMOLOGICAL-BOUNDARY-PROPOSAL.txt` (hash match) | III-F.2 |
| 071 (attachment 2dcd…) | Three pillars | `boundary-work-history-wiring/inputs/THREE-PILLARS.txt` (hash match) | III-G.1–G.4 |
| 072 (inline) | Work algebra, capacity–work, charge pumping, Lagrangian, smearing kernel | `MSG-072.txt` (new) | III-G.4–G.6 (`decoder_work_*`, `funded_decoder_entropy_bound`, `exchange_*`, `historical_dual_kernel`, Gram kernel) |
| 073 (attachment 02da…) | Comprehensive proof of the master theorem | `COMPREHENSIVE-MASTER-PROPOSAL.txt` (hash match) | III-G.7 |
| (attachment 0e11…) | Unified working ledger | `UNIFIED-WORKING-LEDGER-PROPOSAL.txt` (hash match) | III-F.1 |
| 076 (inline answer) | Age-independent holding bound | `historical-handoff-source/inputs/AGE-INDEPENDENT-HOLDING-SUBMISSION.md` | §G.8; `syndrome_stock_bound`, `syndrome_flux_balance`, `cumulative_maintenance_bound` |

## Under-credit found in the master

§22.3 marks correlated-burst accounts 5–7 "Not yet met" and does not cite
`CorrelatedStress.correlated_stress` (bridge 6). That theorem proves that
shocks with bounded footprint k, local stochastic at rate q, damage a set S
with probability at most C(|N(S)|, ⌊|S|/k⌋) q^⌊|S|/k⌋. Correlated,
common-cause damage is therefore exponentially suppressed, and the threshold
route attains the ceiling at a sufficient distance. A before/after for §22.3
is proposed to the author.
