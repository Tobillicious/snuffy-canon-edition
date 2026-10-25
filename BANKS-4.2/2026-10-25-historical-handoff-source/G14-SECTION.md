## G.14 Premise 5 with the Bennett counterpart constructed

`Bennett.premise5_from_bennett` took the counterpart's properties as
hypotheses. Here the counterpart is constructed, and each of those properties
is proved (`BennettCounterpart`).

An option is a policy together with the implementation of its administration.
The implementation is either irreversible or reversible. An irreversible
implementation is a joint register–bath dynamics that leaves the register in
the law of an overwrite \(f\). A reversible implementation is a bijection of
the register alone. The Bennett cycle `Bennett.bennettEquiv` is one; it writes
\(f(a)=h(g(a))\) into a clean output and returns the workspace to zero
(`bennett_counterpart_computes`). An option's cost is its policy's base cost
plus the energy its administration delivers to the bath (`Landauer.heat`). Its
outcome stages before the resource stage \(j\) are the policy's outcomes.
Stage \(j\) reads the residual slack \(B-\mathrm{cost}\) through a strictly
monotone map. The counterpart of an option runs the same policy with
reversible administration.

- *Zero heat.* Reversible administration delivers exactly zero heat
  (`counterpart_heat_zero`, from `Bennett.heat_reversible`).
- *Positive heat.* An irreversible overwrite that merges two register states
  of positive probability delivers strictly positive heat
  (`merging_heat_pos`, from `Bennett.heat_irreversible`).
- *Same earlier outcomes and same base cost.* The counterpart agrees with the
  option before stage \(j\) (`counterpart_same`) and runs the same policy, so
  its base cost is unchanged. Its only cost difference is the delivered heat,
  which is zero.
- *Feasible, with strictly more slack.* Whenever the option is feasible, the
  counterpart is feasible (`counterpart_feasible`) and has strictly more slack
  at stage \(j\) (`counterpart_more_slack`).

Therefore no canonical option has merging irreversible administration
(`premise5_constructed`). The law forces reversible administration from the
Landauer model and the constructed Bennett cycle, with no hypothesis about
the counterpart.
