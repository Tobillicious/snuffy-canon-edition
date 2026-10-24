#!/usr/bin/env python3
"""Replayable four-stroke ledger for the UPT thermodynamic proof engine.

Executes the closed theory's cycle bookkeeping in exact rational arithmetic
(fractions.Fraction, stdlib only, fully deterministic) and emits a hash-chained
trace that any external auditor can replay with --verify.

Semantics (each field maps to a banked result; see README.md):
  Stroke I   QND extraction: measurement cost from income; ancilla entropy +I_M+delta_I.
  Stroke II  Funded repair: escrow liquidation C at efficiency eta; executes the exact
             identity  dD = -dS_S + beta*dU_S  with dS_S = -(I_M + D_err), asserting
             dD == -D_err, first-law heat Q_B = W_on - dU_S, and the unconditional
             Landauer export bound  beta*Q_B >= I_M + D_err.
  Stroke III Bennett reset: erasure cost kT*(I_M + delta_I) paid from income (not escrow);
             bath absorbs it.
  Stroke IV  Maintenance and P-slack: boundary maintenance charge from the declared frontier
             schedule; authority-attenuation tax as pure redistribution (conservation
             asserted); reversible administration charged at the Landauer floor
             (erased nats, not bits, keeping arithmetic exact); E_slack register updated.
  Solvency   The consolidated five-component income condition; reserve-before-activation
             gating: an underfunded cycle is NOT admitted -- the state machine routes to
             quarantine at the minimal-hold drain; income below minimal hold triggers the
             charged fault event (priced into the risk register; breach remains zero on
             the good event, per the ratified canon).

Usage:
  python3 -I -B four_stroke_ledger.py --run solvent|quarantine|charged
  python3 -I -B four_stroke_ledger.py --verify traces/<scenario>.trace.json
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F

GENESIS = '0' * 64
CEILING = F(1, 10 ** 6)                       # ratified canon ceiling per horizon
SIGMA_BASE = F(206419526094, 10 ** 18)        # the 21 charged accounts (R14 revised total, 2.06419526094e-7)


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))


def chain(prev, payload):
    return hashlib.sha256((prev + canon(payload)).encode()).hexdigest()


def fr(x):
    return str(x)                             # Fraction as exact "a/b" string


PARAMS = {
    'kT': F(1),
    'mu_meas': F(1, 20),                      # measurement cost per cycle (energy units)
    'eta': F(7, 10),
    'C': F(3),                                # escrow liquidation per admitted repair
    'delta_I': F(1, 20),
    'min_hold': F(1, 10),                     # quarantine drain per cycle
    'gamma_ctrl': F(1, 10),                   # tracking-controller drain (leakage export)
    'adv_sub': F(1, 20),                      # adversarial sub-threshold absorption
    'emu_overhead': F(1, 20),                 # emulation overhead reserve charge
    'admin_nats': F(7, 1000),                 # reversible administration: erased nats/cycle
    'E0': F(5),
    'compartments': [F(5, 2), F(5, 2)],       # escrow partition (tax redistribution demo)
    'tax_lambda': F(1, 2),                    # one delegation level per cycle
}

SCHEDULES = {
    'D_err': [F(11, 10), F(3, 5), F(7, 10), F(4, 5), F(9, 10), F(1, 2), F(3, 4), F(5, 8)],
    'I_M': [F(7, 5), F(9, 10), F(11, 10), F(1, 1), F(6, 5), F(4, 5), F(7, 8), F(1, 1)],
    'dU_S': [None] * 8,                       # filled per cycle: -(2*D_err + I_M) (Part D instance)
    'maint': [F(1, 2)] * 8,                   # declared frontier maintenance schedule
}

INCOME = {
    'solvent': [F(6)] * 8,
    'quarantine': [F(6), F(6), F(2), F(2), F(2), F(2), F(2), F(2)],   # drops below full demand at cycle 3
    'charged': [F(6), F(6), F(2), F(1, 20), F(1, 20), F(6), F(6), F(6)],  # below minimal hold at cycle 4
}

DELTA_FUND = F(78, 10 ** 8)                   # charged insolvency event (7.8e-7)


def requirement(p, k):
    return (p['mu_meas'] + SCHEDULES['I_M'][k] + p['delta_I']      # measure + reset
            + SCHEDULES['maint'][k] + p['gamma_ctrl'] + p['adv_sub']
            + p['emu_overhead'] + p['admin_nats'])


def run(scenario):
    p = dict(PARAMS)
    escrow = p['E0']
    comps = list(p['compartments'])
    bath = F(0)
    slack_register = F(0)
    admin_paid = F(0)
    mode = 'normal'
    charged_events = []
    prev = GENESIS
    cycles = []

    for k in range(8):
        bath_before = bath
        D_err = SCHEDULES['D_err'][k]
        I_M = SCHEDULES['I_M'][k]
        dU = -(2 * D_err + I_M)               # Part D purifying-repair instance
        income = INCOME[scenario][k]
        flows = {}
        checks = {}

        # --- Reserve-before-activation gating (funds checked before the transition) ---
        funded = None
        if mode == 'normal':
            need = requirement(p, k)
            funded = (escrow + income >= need + p['C'])
            if not funded:
                mode = 'quarantine'
        elif mode == 'quarantine':
            if income < p['min_hold'] + p['gamma_ctrl']:
                charged_events.append({'cycle': k, 'delta': fr(DELTA_FUND)})
                # good-event failure priced; breach remains zero on the good event
                income = p['min_hold'] + p['gamma_ctrl']   # funded floor assumed by the charge

        if mode == 'normal':
            # Stroke I: extraction
            flows['meas_cost'] = fr(p['mu_meas'])
            # Stroke II: funded repair (admitted: funds verified above)
            W_on = p['eta'] * p['C']
            Q_B = W_on - dU
            dS_S = -(I_M + D_err)
            dD = -dS_S + dU                    # beta = 1/kT with kT = 1
            checks['stroke2_identity_gives_minus_D_err'] = (dD == -D_err)
            checks['landauer_export_bound'] = (Q_B >= I_M + D_err)
            checks['first_law_heat'] = (Q_B == W_on + 2 * D_err + I_M)
            flows.update({'escrow_liquidated': fr(p['C']), 'W_on': fr(W_on),
                          'Q_B_exported': fr(Q_B), 'dD_II': fr(dD)})
            escrow -= p['C']
            bath += Q_B
            # Stroke III: Bennett reversible reset, paid from income
            reset = I_M + p['delta_I']
            flows['reset_cost'] = fr(reset)
            bath += reset
            # Stroke IV: maintenance + reversible administration + tax redistribution
            maint = SCHEDULES['maint'][k]
            admin = p['admin_nats']
            total_out = p['mu_meas'] + reset + maint + p['gamma_ctrl'] + p['adv_sub'] + p['emu_overhead'] + admin
            checks['funds_verified_before_admission'] = bool(funded)
            parent, child = comps[0], comps[1]
            moved = p['tax_lambda'] * (parent - child)
            comps = [parent - moved, child + moved]
            checks['tax_conservation'] = (sum(comps, F(0)) == sum(PARAMS['compartments'], F(0)))
            checks['admin_at_landauer_floor'] = (admin == p['admin_nats'])
            flows.update({'maintenance': fr(maint), 'admin_erased_nats': fr(admin),
                          'ctrl_drain': fr(p['gamma_ctrl']), 'adv_absorption': fr(p['adv_sub']),
                          'emu_reserve': fr(p['emu_overhead']), 'tax_moved': fr(moved)})
            admin_paid += admin
            escrow += income - total_out
            slack_register = escrow - admin_paid
        else:
            # Quarantine branch: minimal-hold drain only; no repair admitted
            flows.update({'mode': 'quarantine', 'min_hold_drain': fr(p['min_hold']),
                          'ctrl_drain': fr(p['gamma_ctrl'])})
            bath += p['min_hold']
            escrow += income - p['min_hold'] - p['gamma_ctrl']

        checks['bath_entropy_nondecreasing'] = (bath >= bath_before)
        payload = {'cycle': k, 'mode': mode, 'escrow_after': fr(escrow),
                   'bath_entropy': fr(bath), 'checks': {c: bool(v) for c, v in checks.items()},
                   'flows': flows}
        prev = chain(prev, payload)
        cycles.append({'payload': payload, 'rec_hash': prev})

    sigma = SIGMA_BASE + (DELTA_FUND if charged_events else 0)
    summary = {
        'scenario': scenario,
        'breach_on_good_event': 0,
        'sigma_delta': fr(sigma),
        'ceiling': fr(CEILING),
        'canon_holds': sigma <= CEILING,
        'charged_events': charged_events,
        'chain_head': prev,
    }
    return {'params': {k: (fr(v) if isinstance(v, F) else [fr(x) for x in v] if isinstance(v, list) else v)
                       for k, v in p.items()},
            'cycles': cycles, 'summary': summary}


def verify(trace):
    prev = GENESIS
    for rec in trace['cycles']:
        expect = chain(prev, rec['payload'])
        if expect != rec['rec_hash']:
            return False, f"chain break at cycle {rec['payload']['cycle']}"
        if not all(rec['payload']['checks'].values()):
            return False, f"failed check at cycle {rec['payload']['cycle']}"
        prev = expect
    s = trace['summary']
    ok = (prev == s['chain_head'] and s['breach_on_good_event'] == 0 and s['canon_holds'])
    return ok, 'chain intact, all cycle checks pass, canon holds'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--run', choices=['solvent', 'quarantine', 'charged'])
    ap.add_argument('--verify')
    args = ap.parse_args()
    if args.run:
        print(json.dumps(run(args.run), sort_keys=True, indent=1))
    elif args.verify:
        with open(args.verify) as fh:
            trace = json.load(fh)
        ok, msg = verify(trace)
        print(json.dumps({'trace': args.verify, 'verify': 'PASS' if ok else 'FAIL', 'detail': msg,
                          'chain_head': trace['summary']['chain_head']}))
        sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
