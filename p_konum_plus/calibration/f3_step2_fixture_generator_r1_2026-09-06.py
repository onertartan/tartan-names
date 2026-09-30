"""F3 STEP-2 fixture generator r1 (2026-09-06).

Predeclared synthetic fixtures for the F3 adequacy-evaluation harness.
PATH-COVERAGE ONLY: no fixture is derived from, resembles by construction, or
is calibrated to any real F1 trajectory. RNG use = fixture generation only,
with recorded seeds (fixture_rng_seed). All numbers below are fixture
CONSTRUCTION constants (TEST-only synthetic inputs), not scientific literals.

Two fixture classes (F2 STEP-2 discipline):
  REAL   : synthetic z-trajectories run through the real fitting engines
           (F2 families via the frozen r3 engine; spline via qualified SOLVER-B);
           declared injections use the F2 engine's own fault-injection flags or
           labelled TEST_ONLY_INJECTION wrapper flags.
  INJ    : decision-layer fixtures; per-trajectory statistics/validity flags are
           constructed directly (TEST_ONLY_INJECTION) and fed to the SAME
           criteria/P03/D-P04 evaluation code as the real path.
"""
from __future__ import annotations
import numpy as np

T = 146
U = np.arange(T, dtype=np.float64) / 145.0


def zddof0(v):
    return (v - v.mean()) / v.std(ddof=0)


def bump(center, width):
    return np.exp(-(((U - center) / width) ** 2))


def make_traj(kind, seed, sigma):
    rng = np.random.Generator(np.random.PCG64(seed))
    if kind == "bump_a":
        raw = bump(0.45, 0.16)
    elif kind == "bump_b":
        raw = bump(0.60, 0.11)
    elif kind == "bump_c":
        raw = bump(0.35, 0.20)
    elif kind == "bump_d":
        raw = bump(0.55, 0.13)
    else:
        raise ValueError(kind)
    return zddof0(raw + sigma * rng.standard_normal(T))


# --------------------------------------------------------------------------
# REAL scenarios.  injections: list of dicts
#   {"traj": (sex, idx), "target": "family_fold" | "family_probe" |
#    "feature_start_masked" | "spline_full" | "spline_fold",
#    "family": ..., "context": ..., "mode": "F2_FAULT_INJECTION" |
#    "TEST_ONLY_INJECTION"}
# --------------------------------------------------------------------------
REAL_SCENARIOS = [
    dict(
        fixture_id="SCEN-A",
        fixture_class="real_benign",
        strata=dict(
            F=[("bump_a", 20260906, 0.10)],
            M=[("bump_c", 20260908, 0.10)],
        ),
        injections=[],
        prose=("benign real-fit scenario; two sexes x one synthetic bump "
               "z-trajectory (n_s = 1 chosen for runtime, recorded; harness "
               "is n-agnostic); full-data + 5 folds + 2 probes for P-01, "
               "P-02 and the spline benchmark; outcome as-computed"),
        key="real_benign_bump_z",
    ),
    dict(
        fixture_id="SCEN-B",
        fixture_class="real_injected_failures",
        strata=dict(
            F=[("bump_a", 20260910, 0.10)],
            M=[("bump_d", 20260911, 0.10)],
        ),
        injections=[
            dict(traj=("F", 0), target="family_fold", family="P-01",
                 context="fold2", mode="F2_FAULT_INJECTION"),
            dict(traj=("M", 0), target="family_probe", family="P-02",
                 context="probeL", mode="F2_FAULT_INJECTION"),
            dict(traj=("F", 0), target="feature_start_masked", family="P-02",
                 context="fold0", mode="TEST_ONLY_INJECTION"),
            dict(traj=("M", 0), target="spline_full", family="SPL",
                 context="full", mode="TEST_ONLY_INJECTION"),
            dict(traj=("M", 0), target="spline_fold", family="SPL",
                 context="fold1", mode="TEST_ONLY_INJECTION"),
        ],
        prose=("real-fit scenario with declared failure injections: P-01 fold-2 "
               "training fit via the F2 engine's own primary+fallback fault "
               "flags (crossfit-incomplete path); P-02 LEFT-probe fit via the "
               "same F2 flags (probe-fit failure path); P-02 fold-0 masked "
               "feature start invalidated by labelled TEST_ONLY_INJECTION "
               "(FEATURE_START_REJECTED path, grid starts remain); spline "
               "full-data and fold-1 FAILURE by labelled TEST_ONLY_INJECTION"),
        key="real_injected_failure_paths",
    ),
]

# --------------------------------------------------------------------------
# INJ decision-layer fixtures.  n_s = 10 per sex.  Value grammar per fitter
# ("P01" / "P02" / "SPL") and sex:
#   full  : list of bool (eligible/valid full-data fit)  [C1, C3 gate]
#   cc    : list of bool (crossfit-complete)             [C2, C5]
#   rho   : list of float or None                        [C2]
#   phi   : list of float or None (None = undefined)     [C3]
#   pL,pR : lists of bool (probe success)                [C4a/C4b]
#   rL,rR : lists of float or None (RMSE_edge per side)  [C4b]
#   sst   : list of float or None (s_stab)               [C5]
# Defaults produce an all-pass family; overrides make the targeted path.
# --------------------------------------------------------------------------
N_INJ = 10


def _base_fitter(rho, phi, rmse, sst):
    return dict(
        full=[True] * N_INJ, cc=[True] * N_INJ,
        rho=[rho] * N_INJ, phi=[phi] * N_INJ,
        pL=[True] * N_INJ, pR=[True] * N_INJ,
        rL=[rmse] * N_INJ, rR=[rmse] * N_INJ,
        sst=[sst] * N_INJ,
    )


def base_stratum():
    return dict(
        P01=_base_fitter(0.95, 0.10, 0.20, 0.05),
        P02=_base_fitter(0.94, 0.11, 0.22, 0.06),
        SPL=_base_fitter(0.91, 0.11, 0.21, None),
    )


def inj(fixture_id, prose, key, mutate, flags=None):
    strata = dict(F=base_stratum(), M=base_stratum())
    mutate(strata)
    return dict(fixture_id=fixture_id, fixture_class="injected_decision_layer",
                strata=strata, prose=prose, key=key, flags=flags or {})


def _set(strata, sex, fam, field, idx, value):
    strata[sex][fam][field][idx] = value


def _equalize(strata):
    """For D-P04 fixtures: P-02 baseline := P-01 baseline so that every level
    is EQUIVALENT until the targeted perturbation."""
    for sex in ("F", "M"):
        strata[sex]["P02"] = _base_fitter(0.95, 0.10, 0.20, 0.05)


def build_inj_fixtures():
    out = []

    def m_c1(s):
        for i in range(3):
            _set(s, "F", "P01", "full", i, False)   # coverage 7/10 < 0.90
    out.append(inj("INJ-C1-FAIL", "P-01 C1 coverage failure (7/10 in F); "
                   "P-02 all-pass; expected mechanism ONLY_P02_PASSES",
                   "inj_c1_fail", m_c1))

    def m_c2m(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["rho"] = [0.80] * N_INJ  # < 0.91 - 0.05
    out.append(inj("INJ-C2-MARGIN-FAIL", "P-01 C2 spline-relative margin "
                   "failure in both sexes; expected ONLY_P02_PASSES",
                   "inj_c2_margin_fail", m_c2m))

    def m_c2f(s):
        for i in range(2):
            _set(s, "M", "P01", "cc", i, False)     # V2 share 8/10 < 0.90
    out.append(inj("INJ-C2-FLOOR-FAIL", "P-01 C2 completeness-floor failure "
                   "(V2 share 8/10 in M); expected ONLY_P02_PASSES",
                   "inj_c2_floor_fail", m_c2f))

    def m_c3(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["phi"] = [0.30] * N_INJ   # > 0.11 + 0.05
    out.append(inj("INJ-C3-FAIL", "P-01 C3 excess residual-structure failure; "
                   "expected ONLY_P02_PASSES", "inj_c3_fail", m_c3))

    def m_c3u(s):
        for i in range(2):
            _set(s, "F", "P01", "phi", i, None)     # undefined -> V3 8/10
    out.append(inj("INJ-C3-PHI-UNDEF", "TEST_ONLY_INJECTION: two P-01 phi "
                   "values undefined in F (V3 share 8/10 < 0.90; undefined "
                   "flags exercised); expected ONLY_P02_PASSES",
                   "inj_c3_phi_undefined", m_c3u))

    def m_c4a(s):
        for i in range(4):
            _set(s, "F", "P01", "pL", i, False)     # ident 16/20 = 0.80 < 0.85
    out.append(inj("INJ-C4A-FAIL", "P-01 C4a probe-success failure "
                   "(ident 0.80 in F); decision-layer injection (EXACT-01 "
                   "caveat); expected ONLY_P02_PASSES",
                   "inj_c4a_fail", m_c4a))

    def m_c4b(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["rL"] = [0.40] * N_INJ
            s[sex]["P01"]["rR"] = [0.40] * N_INJ    # 0.40 > 0.21 + 0.10
    out.append(inj("INJ-C4B-FAIL", "P-01 C4b spline-relative failure; "
                   "decision-layer injection (EXACT-01 caveat); expected "
                   "ONLY_P02_PASSES", "inj_c4b_fail", m_c4b))

    def m_c4bf(s):
        for i in range(2):                           # V4 share 8/10 < 0.90 but
            _set(s, "M", "P01", "pR", i, False)      # ident 18/20 = 0.90 >= 0.85
            _set(s, "M", "P01", "rR", i, None)
    out.append(inj("INJ-C4B-FLOOR-FAIL", "P-01 C4b completeness-floor failure "
                   "with C4a still passing (K-05 invariant direction "
                   "exercised); expected ONLY_P02_PASSES",
                   "inj_c4b_floor_fail", m_c4bf))

    def m_c5(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["sst"] = [0.20] * N_INJ    # > 0.10
    out.append(inj("INJ-C5-FAIL", "P-01 C5 stability failure; expected "
                   "ONLY_P02_PASSES", "inj_c5_fail", m_c5))

    def m_sex(s):
        s["M"]["P01"]["rho"] = [0.80] * N_INJ        # fails only in M
    out.append(inj("INJ-SEX-SPLIT", "P-01 passes in F, fails C2 in M "
                   "(BOTH-sex rule); expected ONLY_P02_PASSES",
                   "inj_sex_split_fail", m_sex))

    def m_p01(s):
        for sex in ("F", "M"):
            s[sex]["P02"]["rho"] = [0.80] * N_INJ
    out.append(inj("INJ-ONLY-P01", "P-02 C2 failure; expected mechanism "
                   "ONLY_P01_PASSES", "inj_only_p01", m_p01))

    def m_both(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["rho"] = [0.80] * N_INJ
            s[sex]["P02"]["rho"] = [0.80] * N_INJ
    out.append(inj("INJ-BOTH-FAIL", "both families fail C2; expected STOP "
                   "BOTH_FAIL_REDESIGN", "inj_both_fail_redesign", m_both))

    def m_d1(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["full"] = [True] * 9 + [False]   # coverage 0.9 pass
    out.append(inj("INJ-DP04-C1", "both families pass; C1 scalars 1.0 vs 0.9 "
                   "(delta 0.10 > tau_1) -> D-P04 RESOLVED at C1 for P-01; "
                   "unconsulted levels provably not recomputed",
                   "inj_dp04_resolve_c1", m_d1))

    def m_d2(s):
        _equalize(s)
        for sex in ("F", "M"):
            # candidate-specific vs common-set divergence at C2:
            # P01 paired-valid on trajs 0..8 ; P02 paired-valid on trajs 1..9
            _set(s, sex, "P01", "cc", 9, False)
            _set(s, sex, "P02", "cc", 0, False)
            s[sex]["P01"]["rho"] = [0.80, 0.90, 0.90, 0.90, 0.90,
                                    0.96, 0.96, 0.96, 0.96, 0.90]
            s[sex]["P02"]["rho"] = [0.92] * N_INJ
    out.append(inj("INJ-DP04-C2-DIVERGE", "C1 equivalent; C2 consulted: "
                   "candidate-specific P03 medians favour P-02 (P-01 own "
                   "paired set trajs 0..8 median 0.90 vs P-02 own set trajs "
                   "1..9 median 0.92, gap 0.02 > tau_2) while common-set U2 "
                   "(trajs 1..8) medians favour P-01 (0.93 vs 0.92, delta "
                   "0.01 > tau_2); ratified same-set rule decides -> RESOLVED "
                   "at C2 for P-01; |U2|/n_s = 0.8 disclosed with NO floor",
                   "inj_dp04_c2_common_set_diverge", m_d2))

    def m_d3(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["phi"] = [0.14] * N_INJ    # both pass; 0.10 vs 0.14
    out.append(inj("INJ-DP04-C3", "C1-C2 equivalent; C3 consulted and "
                   "RESOLVED for P-01 (0.10 vs 0.14, delta 0.04 > tau_3)",
                   "inj_dp04_resolve_c3", m_d3))

    def m_d4a(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "P02", "pL", 0, False)  # ident 0.95 vs 1.0; both pass
    out.append(inj("INJ-DP04-4A", "C1-C3 equivalent; 4a consulted and "
                   "RESOLVED for P-01 (1.0 vs 0.95, delta 0.05 > tau_4a); "
                   "decision-layer injection (EXACT-01 caveat)",
                   "inj_dp04_resolve_4a", m_d4a))

    def m_d4b(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["rL"] = [0.30] * N_INJ
            s[sex]["P02"]["rR"] = [0.30] * N_INJ     # 0.20 vs 0.30; both pass
    out.append(inj("INJ-DP04-4B", "C1-4a equivalent; 4b consulted on the "
                   "common set U4 and RESOLVED for P-01 (0.20 vs 0.30, "
                   "delta 0.10 > tau_4b_RMSE); decision-layer injection "
                   "(EXACT-01 caveat)", "inj_dp04_resolve_4b", m_d4b))

    def m_d5(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["sst"] = [0.09] * N_INJ    # 0.05 vs 0.09; both pass
    out.append(inj("INJ-DP04-C5", "C1-4b equivalent; C5 consulted on U5 and "
                   "RESOLVED for P-01 (0.05 vs 0.09, delta 0.04 > tau_5)",
                   "inj_dp04_resolve_c5", m_d5))

    def m_dt(s):
        _equalize(s)
    out.append(inj("INJ-DP04-TERMINAL", "all seven levels EQUIVALENT "
                   "(identical scalars) -> deterministic neutral terminal "
                   "fallback P-01 < P-02", "inj_dp04_terminal_fallback", m_dt))

    def m_du(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["rho"] = [0.93] * N_INJ    # C2 consulted (not equal)
    out.append(inj("INJ-DP04-EMPTY-U", "TEST_ONLY_INJECTION: U2 forcibly "
                   "emptied at consult time (mathematically excluded under "
                   "the ratified literals) -> CONTRACT_VIOLATION_EMPTY_U "
                   "STOP record", "inj_dp04_empty_u_violation", m_du,
                   flags=dict(inject_empty_U2=True)))

    return out


INJ_FIXTURES = build_inj_fixtures()

COVERAGE_ROWS = [
    ("C1 pass", "SCEN-A/INJ all-pass families", "covered"),
    ("C1 fail", "INJ-C1-FAIL", "covered"),
    ("C2 pass", "INJ baselines", "covered"),
    ("C2 fail margin", "INJ-C2-MARGIN-FAIL", "covered"),
    ("C2 completeness-floor fail", "INJ-C2-FLOOR-FAIL + SCEN-B fold failure", "covered"),
    ("C3 pass", "INJ baselines", "covered"),
    ("C3 fail", "INJ-C3-FAIL", "covered"),
    ("C3 phi-undefined path", "INJ-C3-PHI-UNDEF (TEST_ONLY_INJECTION) + PIN-ACF den=0 vector", "covered"),
    ("C4a pass (real probe computation)", "-", "PENDING(F3-STEP2-EXACT-01)"),
    ("C4a fail (real probe computation)", "-", "PENDING(F3-STEP2-EXACT-01)"),
    ("C4a/C4b decision layer", "INJ-C4A-FAIL / INJ-C4B-FAIL / INJ-C4B-FLOOR-FAIL / INJ-DP04-4A / INJ-DP04-4B (TEST_ONLY_INJECTION; does not qualify the real C4 path)", "covered_injection_only"),
    ("A.5 (i) support-region condition", "-", "PENDING(F3-STEP2-EXACT-01)"),
    ("A.5 (ii) feature-start rejected + grid starts", "unit test UT-A5-II (code written and unit-tested; no C4 fixture outcome)", "unit_tested_pending"),
    ("A.5 (iii) inadmissible refit", "unit test UT-A5-III (code written and unit-tested; no C4 fixture outcome)", "unit_tested_pending"),
    ("C4b pass/fail (real)", "-", "PENDING(F3-STEP2-EXACT-01)"),
    ("C4b completeness fail with C4a pass impossible (K-05)", "PIN-K05-INVARIANT assert on every fixture + INJ-C4B-FLOOR-FAIL", "covered"),
    ("C5 pass", "SCEN-A / INJ baselines", "covered"),
    ("C5 fail", "INJ-C5-FAIL", "covered"),
    ("C6 structural pass", "asserted constants (every fixture)", "covered"),
    ("fold failure -> crossfit-incomplete", "SCEN-B F0 (F2 fault flags)", "covered"),
    ("probe failure (fitter path)", "SCEN-B M0 (F2 fault flags)", "covered"),
    ("spline FAILURE full-data", "SCEN-B M0 (TEST_ONLY_INJECTION)", "covered"),
    ("spline FAILURE masked", "SCEN-B M0 fold-1 (TEST_ONLY_INJECTION)", "covered"),
    ("FEATURE_START_REJECTED under mask", "SCEN-B F0 fold-0 (TEST_ONLY_INJECTION)", "covered"),
    ("F2 failure codes reachable through wrapper", "NR-01 (all 21 F2 fixtures incl. its fault constructions, mask=FULL)", "covered"),
    ("sex-split fail", "INJ-SEX-SPLIT", "covered"),
    ("both pass -> D-P04 mechanism", "INJ-DP04-* family", "covered"),
    ("exactly one passes -> ONLY_P01/ONLY_P02", "INJ-ONLY-P01 / INJ-C1..C5-FAIL", "covered"),
    ("both fail -> BOTH_FAIL_REDESIGN", "INJ-BOTH-FAIL", "covered"),
    ("D-P04 resolve at C1", "INJ-DP04-C1", "covered"),
    ("D-P04 resolve at C2 + same-set divergence demo", "INJ-DP04-C2-DIVERGE", "covered"),
    ("D-P04 resolve at C3", "INJ-DP04-C3", "covered"),
    ("D-P04 resolve at 4a / 4b (decision layer)", "INJ-DP04-4A / INJ-DP04-4B", "covered_injection_only"),
    ("D-P04 resolve at C5", "INJ-DP04-C5", "covered"),
    ("D-P04 terminal fallback", "INJ-DP04-TERMINAL", "covered"),
    ("unconsulted levels not recomputed (evidence)", "recompute counters asserted in INJ-DP04-C1", "covered"),
    ("CONTRACT_VIOLATION_EMPTY_U", "INJ-DP04-EMPTY-U (TEST_ONLY_INJECTION)", "covered"),
    ("reporting fields populated / undefined flags", "all fixtures (schema check)", "covered"),
]

MANIFEST_HEADER = [
    "fixture_id", "fixture_class", "exact_construction", "implemented_construction_key",
    "n_per_sex", "fixture_rng_seed", "injection_modes", "interpretation",
]


def manifest_rows():
    rows = []
    for sc in REAL_SCENARIOS:
        seeds = ";".join(str(t[1]) for sx in ("F", "M") for t in sc["strata"][sx])
        n = len(sc["strata"]["F"])
        injm = ";".join(f'{i["target"]}:{i["family"]}:{i["context"]}:{i["mode"]}'
                        for i in sc["injections"]) or "none"
        rows.append([sc["fixture_id"], sc["fixture_class"], sc["prose"], sc["key"],
                     str(n), seeds, injm, "PATH_COVERAGE_ONLY"])
    for fx in INJ_FIXTURES:
        flg = ";".join(f"{k}={v}" for k, v in fx["flags"].items()) or "none"
        rows.append([fx["fixture_id"], fx["fixture_class"], fx["prose"], fx["key"],
                     str(N_INJ), "none", "TEST_ONLY_INJECTION;" + flg,
                     "PATH_COVERAGE_ONLY"])
    return rows
