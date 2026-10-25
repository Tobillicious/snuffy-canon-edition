# Prose batch 03 — Bennett status after checkpoint 04 (awaiting the author's OK; NOT applied)

The implemented program and `BennettExact` are now in the canon (checkpoint 04 PASS). These three existing sentences still describe the implementation as a separate candidate. The full premise-5 target is unchanged.

## Change 1

**Before**

5. The full premise-5 target remains reversible administration. The canon proves the heat-only option-model result; its physical counterpart needs the actual lifecycle and deadline comparison (`BennettCounterpart.premise5_constructed`; `PremiseFloor.reversible_administration_forced`).

**After**

5. The full premise-5 target remains reversible administration. The canon proves the heat-only option-model result and, for the implemented Bennett program with its complete lifecycle cost, the exact condition: reversible administration is forced inside the adiabatic window \(0<Q-H\), \(A/(Q-H)<\tau_{\max}\), and outside that window the counterpart is not cheaper (`BennettExact.premise5_exact`, `window_exact`; `PremiseFloor.reversible_administration_forced`; G.17). The remaining physical step is to show that the installation's actual heat, lifecycle charges and deadline lie inside the window.

## Change 2

**Before**

| Premise 5 in the heat-only model; the actual counterpart still needs a complete physical cost and deadline comparison | `PremiseFloor`, `BennettCounterpart` | `reversible_administration_forced` (no axioms), `premise5_constructed` |

**After**

| Premise 5 in the heat-only model, and exactly inside the adiabatic window for the implemented program with complete lifecycle cost; the installation's physical parameters must still be shown inside the window | `PremiseFloor`, `BennettCounterpart`, `BennettExact` | `reversible_administration_forced` (no axioms), `premise5_constructed`, `premise5_exact`, `window_exact` |

## Change 3

**Before**

| `BennettCounterpart` | Heat-only option model; specific implementation/history candidate checked separately; complete physical cost and deadline comparison remains open (G.14) |

**After**

| `BennettCounterpart` | Heat-only option model; the implemented program with clean workspace and retained history, its run refinement and unitary quantum lift, and the twelve-account lifecycle charge; the exact premise-5 condition is in `BennettExact` (G.14; G.17) |

