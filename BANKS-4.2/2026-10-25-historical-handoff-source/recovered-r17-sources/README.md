# Recovered R17 source modules

Source: `BANKS/2026-10-23-r17-fifo-verification/inputs/received/r17fifo_work/sources/`.
These contain results absent from the 4.2 canon (semantic review, 26 October).
Changes for the canon: import path `ControllerFence` → `Snuffy.ControllerFence`;
in-file `#print axioms` lines removed (the canon audit prints every theorem);
`rw [if_pos h]`/`rw [if_neg h]` replaced by `ite_eq_left_of_eq_true`/
`ite_eq_right_of_eq_false` (the pinned Mathlib deprecates the former). No
statement changed. Each compiles with zero output and passes `leanchecker`.
`R15CausalGluing` is not included: it imports `R14Rivals`, found only in the
superseded WHOLE-EDITION-3.8 tree; that is the author's decision.
