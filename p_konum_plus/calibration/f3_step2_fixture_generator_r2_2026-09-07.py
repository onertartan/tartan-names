"""F3 STEP-2 fixture generator r2 (2026-09-07).

Child of f3_step2_fixture_generator_r1_2026-09-06.py (parent hash
03f3ac07e354342f41493b3ed771cdef10e3ba373d3bde92020ec6a730cdcdc3).
Every r1 fixture and its construction is retained byte-for-byte; this file
adds fixtures required by §7 of Claude_Code_F3_STEP2_CORRECTION_EXECUTION_
PROMPT_DRAFT_v6.md: FIX-STARTS-FULL, FIX-STARTS-DUP, INJ-U2-RHO-INVALID,
INJ-U5-C2-INDEPENDENT, INJ-U5-SST-INVALID, INJ-U-POST-CONSTRUCTION-INVALID,
INJ-NAN-STAT, INJ-P03-C4PENDING-C5FAIL, INJ-P03-BOTHFAIL-C4PENDING.
(INJ-EXC-CAPTURE and UT-PROBE-DECOUPLE are exercised directly by the r2
harness, not as manifest-declared strata fixtures, since they target the
spline solver_config call chain and a single fit_family call respectively.)

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
    elif kind == "bump_e":
        raw = bump(0.50, 0.14)
    else:
        raise ValueError(kind)
    return zddof0(raw + sigma * rng.standard_normal(T))


def make_monotone(direction):
    """TEST_CONSTANT (deterministic, no RNG): strictly monotone so argmax is
    unique at index 0 (direction='down') or index 145 (direction='up')."""
    if direction == "down":
        raw = np.array([float(T - t) for t in range(T)])
    else:
        raw = np.array([float(t) for t in range(T)])
    return zddof0(raw)


# --------------------------------------------------------------------------
# REAL scenarios.  injections: list of dicts
#   {"traj": (sex, idx), "target": "family_fold" | "family_probe" |
#    "feature_start_masked" | "spline_full" | "spline_fold",
#    "family": ..., "context": ..., "mode": "F2_FAULT_INJECTION" |
#    "TEST_ONLY_INJECTION"}
# start_bank (X-03/D-04): declared per fixture; MINI_BANK matches the r1
# behaviour (preserved byte-for-byte); FULL_LATTICE proves the F3 default.
# --------------------------------------------------------------------------
REAL_SCENARIOS = [
    dict(
        fixture_id="SCEN-A",
        fixture_class="real_benign",
        start_bank="MINI_BANK",
        evidence_class="real_fit",
        strata=dict(
            F=[("bump_a", 20260906, 0.10)],
            M=[("bump_c", 20260908, 0.10)],
        ),
        injections=[],
        prose=("benign real-fit scenario; two sexes x one synthetic bump "
               "z-trajectory (n_s = 1 chosen for runtime, recorded; harness "
               "is n-agnostic); full-data + 5 folds + 2 probes for P-01, "
               "P-02 and the spline benchmark; outcome as-computed; "
               "start_bank = MINI_BANK (r1-preserved, now declared per D-04)"),
        key="real_benign_bump_z",
    ),
    dict(
        fixture_id="SCEN-B",
        fixture_class="real_injected_failures",
        start_bank="MINI_BANK",
        evidence_class="real_fit",
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
               "(FEATURE_START_REJECTED path, bank starts remain); spline "
               "full-data and fold-1 FAILURE by labelled TEST_ONLY_INJECTION; "
               "start_bank = MINI_BANK (r1-preserved, now declared per D-04)"),
        key="real_injected_failure_paths",
    ),
]

# --------------------------------------------------------------------------
# FIX-STARTS-FULL / FIX-STARTS-DUP (X-03): real-fit trajectories exercised
# directly by the r2 harness (not through run_real_scenario's fold/probe
# machinery -- their purpose is narrowly the start-bank default and the
# duplicate-feature-start rule, per §7).
# --------------------------------------------------------------------------
STARTS_FULL_TRAJ = dict(
    fixture_id="FIX-STARTS-FULL",
    fixture_class="start_bank_default_proof",
    start_bank="FULL_LATTICE",
    evidence_class="real_fit",
    kind="bump_e", seed=20260907, sigma=0.10,
    prose=("one real-fit trajectory, both families, start_bank = FULL_LATTICE "
           "(731 P-01 / 261 P-02 retained grid points + feature start): "
           "proves the X-03 default bank; telemetry start count asserted "
           "against build_grid's retained counts"),
    key="starts_full_lattice_default_proof",
)

STARTS_DUP_TRAJ = dict(
    fixture_id="FIX-STARTS-DUP",
    fixture_class="feature_start_duplicate_proof",
    start_bank="FULL_LATTICE",
    evidence_class="real_fit",
    directions=("down", "up"),  # max at index 0, then max at index 145
    prose=("P-02 real-fit trajectories with observed maximum at index 0 and "
           "at index 145 (TEST_CONSTANT monotone z-vectors): feature start "
           "theta duplicates a P-02 lattice point exactly at u_star in "
           "{0.0, 1.0} -> FEATURE_START_REJECTED(duplicate) exercised on "
           "the real path (X-03 T-STARTS-DUP)"),
    key="starts_dup_feature_rejection_proof",
)


# --------------------------------------------------------------------------
# INJ decision-layer fixtures.  n_s = 10 per sex (unless noted).  Value
# grammar per fitter ("P01" / "P02" / "SPL") and sex:
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
                   "(ident 0.80 in F); decision-layer injection; expected "
                   "ONLY_P02_PASSES", "inj_c4a_fail", m_c4a))

    def m_c4b(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["rL"] = [0.40] * N_INJ
            s[sex]["P01"]["rR"] = [0.40] * N_INJ    # 0.40 > 0.21 + 0.10
    out.append(inj("INJ-C4B-FAIL", "P-01 C4b spline-relative failure; "
                   "decision-layer injection; expected "
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
                   "decision-layer injection",
                   "inj_dp04_resolve_4a", m_d4a))

    def m_d4b(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["rL"] = [0.30] * N_INJ
            s[sex]["P02"]["rR"] = [0.30] * N_INJ     # 0.20 vs 0.30; both pass
    out.append(inj("INJ-DP04-4B", "C1-4a equivalent; 4b consulted on the "
                   "common set U4 and RESOLVED for P-01 (0.20 vs 0.30, "
                   "delta 0.10 > tau_4b_RMSE); decision-layer injection",
                   "inj_dp04_resolve_4b", m_d4b))

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

    # ---- new in r2 (X-07 / X-08 / X-09 corrected-evaluation-layer proofs) ----

    def m_u2_invalid(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "P01", "rho", 0, None)   # C2 stat invalid for P-01 @0
    out.append(inj("INJ-U2-RHO-INVALID", "C1 equivalent; P-01's required C2 "
                   "statistic (rho) invalid at observation 0 (all other "
                   "statistics valid, P03 entry conditions satisfied) -> "
                   "observation 0 excluded from U2 at construction (NOT a "
                   "STOP); both candidates compared on the remaining 9; "
                   "X-07 T-U2-RHO-INVALID-EXCLUDE",
                   "inj_u2_rho_invalid_exclude", m_u2_invalid))

    def m_u5_independent(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "P01", "rho", 0, None)   # C2 invalid; C5 (sst) still valid
    out.append(inj("INJ-U5-C2-INDEPENDENT", "every required C5 statistic "
                   "(sst) valid for both candidates on all 10 observations; "
                   "one rho (C2 statistic) invalid at observation 0 -> "
                   "|U5| = n_s = 10, justified by C5 (sst) validity for both "
                   "candidates, NOT by fold completion and NOT by C2/rho "
                   "validity; X-07 T-U5-INDEPENDENT-OF-C2",
                   "inj_u5_independent_of_c2", m_u5_independent))

    def m_u5_sst_invalid(s):
        _equalize(s)
        _set(s, "F", "P01", "sst", 0, None)   # C5 stat invalid for P-01 @0 (F only)
    out.append(inj("INJ-U5-SST-INVALID", "P-01's required C5 statistic (sst) "
                   "invalid on 1 of 10 observations in F -> |U5| = 9 in F "
                   "with both candidates' medians computed on those same "
                   "nine; NO STOP for this ordinary exclusion; "
                   "X-07 T-U5-SST-INVALID-EXCLUDE",
                   "inj_u5_sst_invalid_exclude", m_u5_sst_invalid, flags=dict(
                       post_construction_nan_target=None)))

    def m_u_post(s):
        _equalize(s)   # both families pass their own P03 checks; C1 EQUIVALENT
                        # by construction, matching INJ-DP04-TERMINAL's baseline;
                        # the STOP fires from the injection flag alone at the C2
                        # consulted level, not from any data-level divergence
    out.append(inj("INJ-U-POST-CONSTRUCTION-INVALID", "C1 equivalent; C2 "
                   "consulted with an otherwise well-formed |U2| = 10 common "
                   "set; a TEST_ONLY_INJECTION invalidates one member's "
                   "required statistic AFTER the set is already built -> "
                   "CONTRACT_VIOLATION_INCONSISTENT_U (kept distinct from "
                   "ordinary construction-time exclusion); X-07 "
                   "T-U-POST-CONSTRUCTION-INVALID",
                   "inj_u_post_construction_invalid", m_u_post,
                   flags=dict(inject_post_construction_invalid_C2=0)))

    def m_nan(s):
        for sex in ("F", "M"):
            _set(s, sex, "P01", "rho", 0, float("nan"))
    out.append(inj("INJ-NAN-STAT", "TEST_ONLY_INJECTION: P-01 rho at "
                   "observation 0 set to NaN (both sexes) -> undefined flag "
                   "= True and C2 not passed via section-8.1 governance (not via a "
                   "failed numeric comparison); its D-P04 consequence "
                   "(when consulted) is exclusion at construction, kept "
                   "distinct from the post-construction case; X-09 "
                   "T-FINITE-P03 / T-FINITE-DP04", "inj_nan_stat", m_nan))

    def m_p03_c4pending_c5fail(s):
        # C4 stays PENDING (c4_source == REAL is only set at evaluate_fixture
        # call time for this fixture -- see build below); P-01 C5 fails
        # definitely in one sex; P-02 all-pass.
        for sex in ("F", "M"):
            pass
        s["F"]["P01"]["sst"] = [0.20] * N_INJ   # definite C5 fail in F
    out.append(inj("INJ-P03-C4PENDING-C5FAIL", "C4 PENDING (REAL-type "
                   "evaluation, S-1 not consulted for this fixture); P-01 C5 "
                   "definitely fails in F, P-02 otherwise all-pass -> P-01 "
                   "p03 = FAIL (definite failure dominates), c4 stays "
                   "PENDING, first_failed_criterion = "
                   "UNDETERMINED_PENDING_C4a, definite_failures = [C5]; "
                   "P-02 p03 = PENDING -> mechanism = "
                   "MECHANISM_UNDETERMINED_PENDING_EXACTNESS; "
                   "X-08 T-P03-STATUS-A", "inj_p03_c4pending_c5fail",
                   m_p03_c4pending_c5fail))

    def m_p03_bothfail_c4pending(s):
        s["F"]["P01"]["sst"] = [0.20] * N_INJ   # definite C5 fail, P-01
        s["M"]["P02"]["sst"] = [0.20] * N_INJ   # definite C5 fail, P-02
    out.append(inj("INJ-P03-BOTHFAIL-C4PENDING", "C4 PENDING for both "
                   "families (REAL-type evaluation); each family has a "
                   "definite C5 failure in one sex -> both p03 = FAIL "
                   "(a definite failure is dispositive regardless of the "
                   "pending C4 criterion) -> mechanism = "
                   "STOP_BOTH_FAIL_REDESIGN (no PENDING remains once both "
                   "are FAIL); X-08 T-P03-STATUS-C",
                   "inj_p03_bothfail_c4pending", m_p03_bothfail_c4pending))

    return out


INJ_FIXTURES = build_inj_fixtures()

# fixture_ids whose c4_source is forced to "REAL" at evaluation time even
# though they are decision-layer constructions -- i.e. C4a/C4b are left
# genuinely PENDING (not decided by injected pL/pR values) so that the P03
# status / mechanism-outcome split (X-08) can be exercised independently of
# whichever S-1 value governs the true real-fixture C4 path.
FORCE_C4_PENDING_FIXTURE_IDS = {
    "INJ-P03-C4PENDING-C5FAIL", "INJ-P03-BOTHFAIL-C4PENDING",
}

COVERAGE_ROWS = [
    ("C1 pass", "SCEN-A/INJ all-pass families", "real_fit;decision_layer_injection", "covered"),
    ("C1 fail", "INJ-C1-FAIL", "decision_layer_injection", "covered"),
    ("C2 pass", "INJ baselines", "decision_layer_injection", "covered"),
    ("C2 fail margin", "INJ-C2-MARGIN-FAIL", "decision_layer_injection", "covered"),
    ("C2 completeness-floor fail", "INJ-C2-FLOOR-FAIL + SCEN-B fold failure", "decision_layer_injection;real_fit", "covered"),
    ("C3 pass", "INJ baselines", "decision_layer_injection", "covered"),
    ("C3 fail", "INJ-C3-FAIL", "decision_layer_injection", "covered"),
    ("C3 phi-undefined path", "INJ-C3-PHI-UNDEF (TEST_ONLY_INJECTION) + PIN-ACF den=0 vector", "decision_layer_injection;unit_test", "covered"),
    ("C4a pass (real probe computation)", "SCEN-A/SCEN-B/FIX-STARTS-FULL probes, S-1=(a)", "real_fit", "covered"),
    ("C4a fail (real probe computation)", "SCEN-B injected probe failure (F2 fault flags)", "real_fit", "covered"),
    ("C4a/C4b decision layer", "INJ-C4A-FAIL / INJ-C4B-FAIL / INJ-C4B-FLOOR-FAIL / INJ-DP04-4A / INJ-DP04-4B (TEST_ONLY_INJECTION)", "decision_layer_injection", "covered_injection_only"),
    ("A.5 (i) support-region condition", "PIN-A5-SUPPORT on every real trajectory (SCEN-A/SCEN-B/FIX-STARTS-*)", "real_fit;assertion", "covered"),
    ("A.5 (ii) feature-start rejected + bank starts", "unit test UT-A5-II + real path via SCEN-B TEST_ONLY_INJECTION", "unit_test;real_fit", "covered"),
    ("A.5 (iii) inadmissible refit", "unit test UT-A5-III + UT-PROBE-DECOUPLE", "unit_test", "covered"),
    ("C4b pass/fail (real)", "SCEN-A/SCEN-B paired probes, S-1=(a)", "real_fit", "covered"),
    ("C4b completeness fail with C4a pass impossible (K-05)", "PIN-K05-INVARIANT assert on every fixture + INJ-C4B-FLOOR-FAIL", "assertion;decision_layer_injection", "covered"),
    ("C5 pass", "SCEN-A / INJ baselines", "real_fit;decision_layer_injection", "covered"),
    ("C5 fail", "INJ-C5-FAIL", "decision_layer_injection", "covered"),
    ("C6 structural pass", "asserted constants (every fixture)", "assertion", "covered"),
    ("fold failure -> crossfit-incomplete", "SCEN-B F0 (F2 fault flags)", "real_fit", "covered"),
    ("probe failure (fitter path)", "SCEN-B M0 (F2 fault flags)", "real_fit", "covered"),
    ("spline FAILURE full-data", "SCEN-B M0 (TEST_ONLY_INJECTION)", "real_fit", "covered"),
    ("spline FAILURE masked", "SCEN-B M0 fold-1 (TEST_ONLY_INJECTION)", "real_fit", "covered"),
    ("FEATURE_START_REJECTED under mask", "SCEN-B F0 fold-0 (TEST_ONLY_INJECTION)", "real_fit", "covered"),
    ("F2 failure codes reachable through wrapper", "NR-01 (all 21 F2 fixtures incl. its fault constructions, mask=FULL)", "real_fit", "covered"),
    ("sex-split fail", "INJ-SEX-SPLIT", "decision_layer_injection", "covered"),
    ("both pass -> D-P04 mechanism", "INJ-DP04-* family", "decision_layer_injection", "covered"),
    ("exactly one passes -> ONLY_P01/ONLY_P02", "INJ-ONLY-P01 / INJ-C1..C5-FAIL", "decision_layer_injection", "covered"),
    ("both fail -> BOTH_FAIL_REDESIGN", "INJ-BOTH-FAIL", "decision_layer_injection", "covered"),
    ("D-P04 resolve at C1", "INJ-DP04-C1", "decision_layer_injection", "covered"),
    ("D-P04 resolve at C2 + same-set divergence demo", "INJ-DP04-C2-DIVERGE", "decision_layer_injection", "covered"),
    ("D-P04 resolve at C3", "INJ-DP04-C3", "decision_layer_injection", "covered"),
    ("D-P04 resolve at 4a / 4b (decision layer)", "INJ-DP04-4A / INJ-DP04-4B", "decision_layer_injection", "covered_injection_only"),
    ("D-P04 resolve at C5", "INJ-DP04-C5", "decision_layer_injection", "covered"),
    ("D-P04 terminal fallback", "INJ-DP04-TERMINAL", "decision_layer_injection", "covered"),
    ("unconsulted levels not recomputed (evidence)", "recompute counters asserted in INJ-DP04-C1", "assertion", "covered"),
    ("CONTRACT_VIOLATION_EMPTY_U", "INJ-DP04-EMPTY-U (TEST_ONLY_INJECTION)", "decision_layer_injection", "covered"),
    ("U2 ordinary construction-time exclusion (rho invalid)", "INJ-U2-RHO-INVALID", "decision_layer_injection", "covered"),
    ("U5 independence from C2/rho", "INJ-U5-C2-INDEPENDENT", "decision_layer_injection", "covered"),
    ("U5 sst-invalid exclusion", "INJ-U5-SST-INVALID", "decision_layer_injection", "covered"),
    ("CONTRACT_VIOLATION_INCONSISTENT_U (post-construction)", "INJ-U-POST-CONSTRUCTION-INVALID", "decision_layer_injection", "covered"),
    ("finite-valued validity / NaN handling", "INJ-NAN-STAT", "decision_layer_injection", "covered"),
    ("P03 status: definite failure with a PENDING criterion", "INJ-P03-C4PENDING-C5FAIL", "decision_layer_injection", "covered"),
    ("P03 status: both families definite-fail while C4 PENDING", "INJ-P03-BOTHFAIL-C4PENDING", "decision_layer_injection", "covered"),
    ("start-bank default (FULL_LATTICE, 731/261+feature)", "FIX-STARTS-FULL", "real_fit", "covered"),
    ("start-bank duplicate feature start", "FIX-STARTS-DUP", "real_fit", "covered"),
    ("probe_success decoupled from full-data fit", "UT-PROBE-DECOUPLE (unit test)", "unit_test", "covered"),
    ("SOLVER-B unverifiable-acceptance capture (S-2)", "INJ-EXC-CAPTURE (TEST_ONLY_INJECTION on nnls)", "unit_test", "covered"),
    ("reporting fields populated / undefined flags", "all fixtures (schema check)", "assertion", "covered"),
]

MANIFEST_HEADER = [
    "fixture_id", "fixture_class", "exact_construction", "implemented_construction_key",
    "n_per_sex", "fixture_rng_seed", "injection_modes", "interpretation",
    "start_bank", "evidence_class", "injection_sites", "expected_outcome",
    "parent_fixture_id",
]


def manifest_rows():
    rows = []
    for sc in REAL_SCENARIOS:
        seeds = ";".join(str(t[1]) for sx in ("F", "M") for t in sc["strata"][sx])
        n = len(sc["strata"]["F"])
        injm = ";".join(f'{i["target"]}:{i["family"]}:{i["context"]}:{i["mode"]}'
                        for i in sc["injections"]) or "none"
        inj_sites = ";".join(f'{i["target"]}:{i["context"]}' for i in sc["injections"]) or "none"
        rows.append([sc["fixture_id"], sc["fixture_class"], sc["prose"], sc["key"],
                     str(n), seeds, injm, "PATH_COVERAGE_ONLY",
                     sc["start_bank"], sc["evidence_class"], inj_sites,
                     "as-computed", "r1:" + sc["fixture_id"]])
    rows.append([STARTS_FULL_TRAJ["fixture_id"], STARTS_FULL_TRAJ["fixture_class"],
                 STARTS_FULL_TRAJ["prose"], STARTS_FULL_TRAJ["key"], "1",
                 str(STARTS_FULL_TRAJ["seed"]), "none", "PATH_COVERAGE_ONLY",
                 STARTS_FULL_TRAJ["start_bank"], STARTS_FULL_TRAJ["evidence_class"],
                 "none", "start_count==retained+feature", "NEW"])
    rows.append([STARTS_DUP_TRAJ["fixture_id"], STARTS_DUP_TRAJ["fixture_class"],
                 STARTS_DUP_TRAJ["prose"], STARTS_DUP_TRAJ["key"], "2",
                 "none(TEST_CONSTANT)", "none", "PATH_COVERAGE_ONLY",
                 STARTS_DUP_TRAJ["start_bank"], STARTS_DUP_TRAJ["evidence_class"],
                 "none", "FEATURE_START_REJECTED(duplicate)", "NEW"])
    for fx in INJ_FIXTURES:
        flg = ";".join(f"{k}={v}" for k, v in fx["flags"].items()) or "none"
        parent = "r1:" + fx["fixture_id"] if fx["fixture_id"] in {
            "INJ-C1-FAIL", "INJ-C2-MARGIN-FAIL", "INJ-C2-FLOOR-FAIL", "INJ-C3-FAIL",
            "INJ-C3-PHI-UNDEF", "INJ-C4A-FAIL", "INJ-C4B-FAIL", "INJ-C4B-FLOOR-FAIL",
            "INJ-C5-FAIL", "INJ-SEX-SPLIT", "INJ-ONLY-P01", "INJ-BOTH-FAIL",
            "INJ-DP04-C1", "INJ-DP04-C2-DIVERGE", "INJ-DP04-C3", "INJ-DP04-4A",
            "INJ-DP04-4B", "INJ-DP04-C5", "INJ-DP04-TERMINAL", "INJ-DP04-EMPTY-U",
        } else "NEW"
        rows.append([fx["fixture_id"], fx["fixture_class"], fx["prose"], fx["key"],
                     str(N_INJ), "none", "TEST_ONLY_INJECTION;" + flg,
                     "PATH_COVERAGE_ONLY", "NOT_APPLICABLE",
                     "decision_layer_injection", "constructed_directly",
                     "as-described", parent])
    return rows
