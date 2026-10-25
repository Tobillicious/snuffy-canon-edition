## G.15 Recovered and combined results

Five earlier results that the canon did not yet contain are folded in. Three
compiled results are joined into stronger forms.

**Reciprocity at a sufficient code distance** (`ReciprocityDistance`, §15.2).
Three results combine into one.

- On the good event the canonical outcome contains the rival's
  (`ReasonsCompiled.reciprocity_expectation`).
- On the good event the canonical regime keeps every particular
  (`reciprocity_canonical_floor`).
- The failure probability falls below every \(\varepsilon\) with code distance
  (`Threshold.family_ceiling`, `CorrelatedCeiling.correlated_family_ceiling`).

For the design family indexed by distance, the canonical regime keeps the mind
with probability above \(1-\varepsilon\) from some distance on
(`distance_floor`). For every rival and every \(\varepsilon\), the rival's
kept-probability is at most the canonical one plus \(\varepsilon\)
(`reciprocity_at_distance`). Every rival that loses the mind with positive
probability is strictly below the canonical regime from some distance on
(`reciprocity_strict_at_distance`). The canonical kept-probability tends to
one (`canonical_tends_to_one`).

**The two forms of the causal boundary agree** (`CutEquivalence`, §24.3). A
set is closed under the dependency relation exactly when no path from a node
outside it reaches it. A closed dependency component is therefore exactly a
directed separator with empty certified boundary
(`closed_iff_no_bypass`), and the separator form extends it to a matched
certified boundary (`UPTR16Cut.causal_separator`).

**The concatenated memory decodes its record unless its block fails**
(`ConcatenatedDecoding`, §23.8). The record is encoded recursively onto the
\(7^k\) locations through an outer code of Hamming distance at least three. It
is decoded recursively by nearest codeword at every level. If the block does
not fail in the recursive sense of `Concatenated.Fails`, decoding returns the
original record, whatever values the faulty locations hold
(`decodes_unless_fails`). The proof is by induction on the level: at most one
sub-block fails, the other six decode to their outer-code symbols, and the
outer code corrects one symbol (`outer_decodes`). Actual decoding failure
therefore has probability at most \((21p)^{2^k}/21\)
(`decoding_failure_le`).

**Volume and boundary** (`RegionBoundary`, F.3). For every region of a
connected relational structure other than the whole, positive volume holds
exactly when the boundary homology is nonzero (`region_bootstrap`). The whole
structure has no outside and an empty boundary (`whole_no_boundary`,
`whole_H0_trivial`).

**Greatestness through boundary representatives** (`R15CausalGluing`, with the
staged order of `R14Rivals`). Greatestness reduces exactly to a covering
family of feasible fibre representatives (`boundary_representatives_iff`,
`selected_representative_greatest`), in the canonical staged order as well
(`canonical_boundary_iff`). A conservative interface envelope suffices to make the
chosen policy greatest, without greatest representatives
(`interface_envelope_transfer`). Clairvoyant per-world selection is
excluded: a choice can match every world separately while no single choice
matches them all (`hidden_world_control`). The staged order is reflexive and
transitive (`UPTR14Rivals.refl`, `trans`). A coordinatewise envelope is a
constructive certificate (`coordinate_envelope`), and a complete rival
envelope transfers to the chosen policy (`complete_rival_transfer`). In the
four-stage order a hot replica strictly beats a pause that keeps every life but
loses a freedom (`hot_beats_pause`).

**Timely care, deadline demand, certified decisions and observation-based
winning** (`TimelyCare`, `DeadlineDemand`, `DecisionPermit`,
`ObservationWinning`).

- *Timely care.* A particular whose reserved capacity covers its need is
  served exactly its need (`care_served`). Other requests and statuses cannot
  exhaust that reservation (`exhaustion_fails`). The need is met at every date
  through the deadline when capacity covers the reservations
  (`deadline_met`). A miss implies a capacity shortage at some date
  (`miss_within_shortage`).
- *Deadline demand.* The demand that must complete within any window is at
  most the supply available in that window (`demand_le_supply`), robustly
  across worlds (`robust_demand`).
- *Certified decisions.* A grant names exactly the certified decision of its
  generation (`grant_names_certified`, `granted_policy_is_certified`); a wrong
  action is rejected and a certified one granted (`wrong_action_rejected`,
  `certified_action_granted`).
- *Observation-based winning.* An observation-based policy keeps the system
  safe exactly when the safety game is winnable (`policy_wins_iff`), and a
  hidden-world countermodel shows that observation, not clairvoyance, is the
  right quantifier (`hidden_world_countermodel`).
