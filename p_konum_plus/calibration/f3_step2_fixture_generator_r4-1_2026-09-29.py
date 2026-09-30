"""F3 STEP-2 fixture generator r4 (2026-09-24).

Child of f3_step2_fixture_generator_r3_2026-09-22.py (parent hash
cc23c9b5ef658bb2b1612dce0ec2a5930f9aa33eda55d590e98812f3ef5fa2b8; the r3
file is historical and read-only). r4 changes ONLY: (1) S-R2-1 = PI_RULE
expectations pinned from D-5 S3 for SCEN-B / INJ-C1-FAIL / INJ-DP04-C1 /
INJ-C4B-NOREF (r4 instruction S4(e)); (2) the INJ-C4B-NOREF prose corrected
per S4(f) (construction was right, prose wrong); (3) coverage rows: K-05 row
adopts the content S6 wording verbatim (T-3), "D-P04 resolve at C1" covered
by INJ-DP04-C1 (D-5 S4(d)), "C4b pass/fail (real)" takes its fail-side
evidence from SCEN-B (D-5 S4(d)); (4) UT_USET_CASES carry an SPL fitter and
case (d) tests the PI_RULE architecture (R3A-10). Everything below this
docstring is otherwise the r3 generator byte-for-byte in structure.
--- r3 header, kept for provenance: ---
Child of f3_step2_fixture_generator_r2_2026-09-07.py (parent hash
a1e6068c0868e7594242fcc6d588cc255f3b0f4bdf21d1e93851e5bafcf98e25).
Every r2 fixture id is retained (construction unchanged) EXCEPT three rebuilt
per prompt DRAFT v2 S7: INJ-U2-RHO-INVALID, INJ-U5-C2-INDEPENDENT,
INJ-U5-SST-INVALID. New fixtures per S7: INJ-U-CCFALSE-FINITE,
INJ-NAN-STAT-C4B, INJ-NAN-STAT-C5, INJ-NAN-STAT-SPL, INJ-C4B-NOREF,
UT-USET-CONSTRUCTION (a)-(e), INJ-EXC-CAPTURE-S1/S2, INJ-EXC-UNRELATED-TYPE,
UT-EXC-UNRELATED-REFERENCE, FIX-A5-TRUE.

PATH-COVERAGE ONLY: no fixture is derived from, resembles by construction, or
is calibrated to any real F1 trajectory. RNG use = fixture generation only,
with recorded seeds. All numbers below are fixture CONSTRUCTION constants
(TEST-only synthetic inputs), not scientific literals.
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


def make_step(where):
    """TEST_CONSTANT (deterministic, no RNG): a step function, 1.0 on the
    named index range and 0.0 elsewhere. Half-range affine normalization
    (zddof0) preserves which raw indices are >= the half-range threshold, so
    the A5 support of the normalized series equals the named range exactly:
    lo=0, hi=1, thr=0.5, and only the named range has raw value 1.0 >= 0.5."""
    raw = np.zeros(T)
    if where == "left":
        raw[0:15] = 1.0          # M_LEFT = {0..14}
    elif where == "right":
        raw[131:146] = 1.0       # M_RIGHT = {131..145}
    else:
        raise ValueError(where)
    return zddof0(raw)


# --------------------------------------------------------------------------
# REAL scenarios. Unchanged from r2 (parent_fixture_id = r2:<id>).
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
               "z-trajectory; full-data + 5 folds + 2 probes for P-01, P-02 "
               "and the spline benchmark; outcome as-computed; "
               "start_bank = MINI_BANK (r1-preserved, declared per D-04)"),
        key="real_benign_bump_z",
        run_scope="both",
        # T-EXPECT-ALL (independent audit 2026-09-23, P-6): deliberately NO
        # expect= here. SCEN-A has zero injections -- its outcome is a
        # genuinely emergent property of the real numerical optimization,
        # not something derivable from construction alone. Declaring an
        # expectation for it would be circular (checking the code's actual
        # output against a number that could only itself have come from
        # running the code once and copying the answer down).
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
        prose=("real-fit scenario with declared failure injections: P-01 "
               "fold-2 (F2 fault flags); P-02 LEFT-probe (F2 fault flags); "
               "P-02 fold-0 masked feature start (TEST_ONLY_INJECTION); "
               "spline full-data and fold-1 FAILURE (TEST_ONLY_INJECTION). "
               "The spline full-data FAILURE at M0 while both spline probes "
               "succeed is also the S-R2-1 state for the spline at M0 "
               "(section 5) -- under DEFERRED_THIS_CYCLE, C4b in M is PENDING for "
               "both families; start_bank = MINI_BANK"),
        key="real_injected_failure_paths",
        run_scope="both",
        # T-EXPECT-ALL: unlike SCEN-A, this IS structurally derivable, not
        # copied from a prior run's output. n_s=1 (one trajectory per sex),
        # so a single forced fold/probe failure deterministically zeroes
        # out the relevant valid-set share for that sex regardless of the
        # other, non-injected sex's real numerical outcome: P-01's fold-2
        # F2_FAULT_INJECTION on the sole F trajectory forces P-01's F-sex
        # C2 share to 0/1 (< C_COMPLETE=0.90) -> P-01 C2 fails -> P-01
        # p03=FAIL regardless of M. P-02's probeL F2_FAULT_INJECTION on the
        # sole M trajectory forces pL=False there -> ident=(0+1)/2=0.5 for
        # M (< C_IDENT=0.85) -> P-02 C4a fails -> P-02 p03=FAIL regardless
        # of F. Both fail on independent, injection-forced grounds ->
        # STOP_BOTH_FAIL_REDESIGN.
        # r4 (S-R2-1 = PI_RULE, D-5 S3 pinned): M0 absent from both
        # families' V4 in M (spline full fit fails by the declared
        # injection while both spline probes succeed) -> V4 empty in M ->
        # C4b undefined and not passed in M for both families; both
        # families still FAIL on their definite failures; mechanism
        # unchanged from r3.
        expect=dict(p03=("FAIL", "FAIL"), mechanism="STOP_BOTH_FAIL_REDESIGN",
                   stops="BOTH_FAIL_REDESIGN",
                   undefined={"P01:C4b:M": True, "P02:C4b:M": True}),
    ),
]

STARTS_FULL_TRAJ = dict(
    fixture_id="FIX-STARTS-FULL", fixture_class="start_bank_default_proof",
    start_bank="FULL_LATTICE", evidence_class="real_fit",
    kind="bump_e", seed=20260907, sigma=0.10,
    prose=("one real-fit trajectory, both families, start_bank = "
           "FULL_LATTICE (731 P-01 / 261 P-02 + feature): proves the X-03 "
           "default bank; telemetry start count asserted"),
    key="starts_full_lattice_default_proof", run_scope="once",
)

STARTS_DUP_TRAJ = dict(
    fixture_id="FIX-STARTS-DUP", fixture_class="feature_start_duplicate_proof",
    start_bank="FULL_LATTICE", evidence_class="real_fit",
    directions=("down", "up"),
    prose=("P-02 real-fit trajectories with observed maximum at index 0 "
           "and 145 (TEST_CONSTANT monotone z-vectors): feature start theta "
           "duplicates a lattice point exactly -> "
           "FEATURE_START_REJECTED(duplicate) on the real path"),
    key="starts_dup_feature_rejection_proof", run_scope="once",
)

FIX_A5_TRUE = dict(
    fixture_id="FIX-A5-TRUE", fixture_class="a5_condition_true_proof",
    start_bank="MINI_BANK", evidence_class="real_fit",
    sides=("left", "right"),
    prose=("real-fit fixture on TEST_CONSTANT step trajectories whose "
           "half-range support lies wholly inside the LEFT mask {0..14} "
           "(one trajectory) and wholly inside the RIGHT mask {131..145} "
           "(one trajectory): full-data fits and the two probes of P-01, "
           "P-02 and the spline; no folds; A.5(i) true on the matching "
           "side -> that probe fails C4a (numerator excluded, denominator "
           "retained) and is absent from the C4b paired-valid set, for all "
           "three fitters; no P03 status, no mechanism outcome for this "
           "fixture (Y-05)"),
    key="a5_condition_i_true_proof", run_scope="once",
)


# --------------------------------------------------------------------------
# INJ decision-layer fixtures.
# --------------------------------------------------------------------------
N_INJ = 10


def _base_fitter(rho, phi, rmse, sst):
    return dict(
        full=[True] * N_INJ, cc=[True] * N_INJ,
        rho=[rho] * N_INJ, phi=[phi] * N_INJ,
        pL=[True] * N_INJ, pR=[True] * N_INJ,
        rL=[rmse] * N_INJ, rR=[rmse] * N_INJ,
        sst=[sst] * N_INJ,
        # R4A-01 (r4-1): per-context spline-pending flags -- default all
        # False, so no existing fixture's outcome changes (non-regression).
        # Set True on the SPL fitter by the R4A-01 TEST_ONLY fixtures to mark
        # a spline context (full/fold/probe) as unverifiable (an UNRELATED
        # solver event that fit_spline returned as STOP_EXACTNESS_PENDING);
        # the decision layer then routes the criteria that read that context
        # to STOP_EXACTNESS_PENDING, exactly as a5v routes C4a/C4b.
        spl_pending_full=[False] * N_INJ,
        spl_pending_fold=[False] * N_INJ,
        spl_pending_probe=[False] * N_INJ,
    )


def base_stratum():
    return dict(
        P01=_base_fitter(0.95, 0.10, 0.20, 0.05),
        P02=_base_fitter(0.94, 0.11, 0.22, 0.06),
        SPL=_base_fitter(0.91, 0.11, 0.21, None),
    )


def inj(fixture_id, prose, key, mutate, flags=None, expect=None, parent="NEW"):
    strata = dict(F=base_stratum(), M=base_stratum())
    mutate(strata)
    return dict(fixture_id=fixture_id, fixture_class="injected_decision_layer",
                strata=strata, prose=prose, key=key, flags=flags or {},
                expect=expect or {}, parent_fixture_id=parent)


def _set(strata, sex, fam, field, idx, value):
    strata[sex][fam][field][idx] = value


def _equalize(strata):
    for sex in ("F", "M"):
        strata[sex]["P02"] = _base_fitter(0.95, 0.10, 0.20, 0.05)


_R2_RETAINED_IDS = {
    "INJ-C1-FAIL", "INJ-C2-MARGIN-FAIL", "INJ-C2-FLOOR-FAIL", "INJ-C3-FAIL",
    "INJ-C3-PHI-UNDEF", "INJ-C4A-FAIL", "INJ-C4B-FAIL", "INJ-C4B-FLOOR-FAIL",
    "INJ-C5-FAIL", "INJ-SEX-SPLIT", "INJ-ONLY-P01", "INJ-BOTH-FAIL",
    "INJ-DP04-C1", "INJ-DP04-C2-DIVERGE", "INJ-DP04-C3", "INJ-DP04-4A",
    "INJ-DP04-4B", "INJ-DP04-C5", "INJ-DP04-TERMINAL", "INJ-DP04-EMPTY-U",
}


def build_inj_fixtures():
    out = []

    def m_c1(s):
        for i in range(3):
            _set(s, "F", "P01", "full", i, False)
    out.append(inj("INJ-C1-FAIL", "P-01 C1 coverage failure (7/10 in F); "
                   "those 3 observations are also the S-R2-1 state for "
                   "P-01 in F (full=False, both probes still True) -> "
                   "under DEFERRED_THIS_CYCLE P-01 C4b is PENDING in F too; "
                   "P-01 p03 = FAIL (first failure C1 regardless); "
                   "P-02 all-pass; expected mechanism ONLY_P02_PASSES",
                   "inj_c1_fail", m_c1,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C1-FAIL"))

    def m_c2m(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["rho"] = [0.80] * N_INJ
    out.append(inj("INJ-C2-MARGIN-FAIL", "P-01 C2 spline-relative margin "
                   "failure in both sexes; expected ONLY_P02_PASSES",
                   "inj_c2_margin_fail", m_c2m,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C2-MARGIN-FAIL"))

    def m_c2f(s):
        for i in range(2):
            _set(s, "M", "P01", "cc", i, False)
    out.append(inj("INJ-C2-FLOOR-FAIL", "P-01 C2 completeness-floor failure "
                   "(V2 share 8/10 in M); expected ONLY_P02_PASSES",
                   "inj_c2_floor_fail", m_c2f,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C2-FLOOR-FAIL"))

    def m_c3(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["phi"] = [0.30] * N_INJ
    out.append(inj("INJ-C3-FAIL", "P-01 C3 excess residual-structure "
                   "failure; expected ONLY_P02_PASSES", "inj_c3_fail", m_c3,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C3-FAIL"))

    def m_c3u(s):
        for i in range(2):
            _set(s, "F", "P01", "phi", i, None)
    out.append(inj("INJ-C3-PHI-UNDEF", "two P-01 phi values undefined in F "
                   "(V3 share 8/10 < 0.90 via CL-F3-04, n_s retained); "
                   "expected ONLY_P02_PASSES",
                   "inj_c3_phi_undefined", m_c3u,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES",
                              undefined={"P01:C3:F": False}),
                   parent="r2:INJ-C3-PHI-UNDEF"))

    def m_c4a(s):
        for i in range(4):
            _set(s, "F", "P01", "pL", i, False)
    out.append(inj("INJ-C4A-FAIL", "P-01 C4a probe-success failure (ident "
                   "0.80 in F); expected ONLY_P02_PASSES", "inj_c4a_fail",
                   m_c4a, expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C4A-FAIL"))

    def m_c4b(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["rL"] = [0.40] * N_INJ
            s[sex]["P01"]["rR"] = [0.40] * N_INJ
    out.append(inj("INJ-C4B-FAIL", "P-01 C4b spline-relative failure; "
                   "expected ONLY_P02_PASSES", "inj_c4b_fail", m_c4b,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C4B-FAIL"))

    def m_c4bf(s):
        for i in range(2):
            _set(s, "M", "P01", "pR", i, False)
            _set(s, "M", "P01", "rR", i, None)
    out.append(inj("INJ-C4B-FLOOR-FAIL", "P-01 C4b completeness-floor "
                   "failure with C4a still passing (K-05 invariant "
                   "direction); expected ONLY_P02_PASSES",
                   "inj_c4b_floor_fail", m_c4bf,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C4B-FLOOR-FAIL"))

    def m_c5(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["sst"] = [0.20] * N_INJ
    out.append(inj("INJ-C5-FAIL", "P-01 C5 stability failure; expected "
                   "ONLY_P02_PASSES", "inj_c5_fail", m_c5,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-C5-FAIL"))

    def m_sex(s):
        s["M"]["P01"]["rho"] = [0.80] * N_INJ
    out.append(inj("INJ-SEX-SPLIT", "P-01 passes in F, fails C2 in M; "
                   "expected ONLY_P02_PASSES", "inj_sex_split_fail", m_sex,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES"),
                   parent="r2:INJ-SEX-SPLIT"))

    def m_p01(s):
        for sex in ("F", "M"):
            s[sex]["P02"]["rho"] = [0.80] * N_INJ
    out.append(inj("INJ-ONLY-P01", "P-02 C2 failure; expected ONLY_P01_PASSES",
                   "inj_only_p01", m_p01,
                   expect=dict(p03=("PASS", "FAIL"), mechanism="ONLY_P01_PASSES"),
                   parent="r2:INJ-ONLY-P01"))

    def m_both(s):
        for sex in ("F", "M"):
            s[sex]["P01"]["rho"] = [0.80] * N_INJ
            s[sex]["P02"]["rho"] = [0.80] * N_INJ
    out.append(inj("INJ-BOTH-FAIL", "both families fail C2; expected STOP "
                   "BOTH_FAIL_REDESIGN", "inj_both_fail_redesign", m_both,
                   expect=dict(p03=("FAIL", "FAIL"),
                              mechanism="STOP_BOTH_FAIL_REDESIGN",
                              stops="BOTH_FAIL_REDESIGN"),
                   parent="r2:INJ-BOTH-FAIL"))

    def m_d1(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["full"] = [True] * 9 + [False]
    out.append(inj("INJ-DP04-C1", "r4 (S-R2-1 = PI_RULE, D-5 S3): "
                   "observation 9 of P-02 has full = False (no full-data "
                   "reference), both sexes -- under the rule this is a "
                   "MEMBERSHIP condition: obs 9 is absent from V3 and V4 of "
                   "P-02 (shares 0.9, floors met at equality); p03 = "
                   "(PASS, PASS); D-P04 consulted path [C1]; C1 coverage "
                   "1.0 vs 0.9, delta 0.1 > tau_1 -> RESOLVED at C1 for "
                   "P-01. Expectation pinned in D-5 S3 BEFORE the run",
                   "inj_dp04_resolve_c1", m_d1,
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="RESOLVED_MECHANISM_P01",
                              resolved_level="C1"),
                   parent="r2:INJ-DP04-C1"))

    def m_d2(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "P01", "cc", 9, False)
            _set(s, sex, "P02", "cc", 0, False)
            s[sex]["P01"]["rho"] = [0.80, 0.90, 0.90, 0.90, 0.90,
                                    0.96, 0.96, 0.96, 0.96, 0.90]
            s[sex]["P02"]["rho"] = [0.92] * N_INJ
    out.append(inj("INJ-DP04-C2-DIVERGE", "C1 equivalent; C2 consulted: "
                   "membership-first construction (Y-02) -- both "
                   "candidates' valid-set membership by crossfit-"
                   "completeness flags, not by finiteness of the resulting "
                   "median. P-01 excluded at obs 9 (cc False), P-02 "
                   "excluded at obs 0 (cc False) -> U2 = {1..8}, |U2| = 8, "
                   "share 0.8; common-set medians (P-01 0.93 vs P-02 0.92, "
                   "delta 0.01 > tau_2) -> RESOLVED at C2 for P-01",
                   "inj_dp04_c2_common_set_diverge", m_d2,
                   expect=dict(p03=("PASS", "PASS"), mechanism="RESOLVED_MECHANISM_P01",
                              resolved_level="C2", U2=8),
                   parent="r2:INJ-DP04-C2-DIVERGE"))

    def m_d3(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["phi"] = [0.14] * N_INJ
    out.append(inj("INJ-DP04-C3", "C1-C2 equivalent; C3 consulted and "
                   "RESOLVED for P-01 (0.10 vs 0.14, delta 0.04 > tau_3)",
                   "inj_dp04_resolve_c3", m_d3,
                   expect=dict(p03=("PASS", "PASS"), mechanism="RESOLVED_MECHANISM_P01",
                              resolved_level="C3"),
                   parent="r2:INJ-DP04-C3"))

    def m_d4a(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "P02", "pL", 0, False)
    out.append(inj("INJ-DP04-4A", "C1-C3 equivalent; 4a consulted and "
                   "RESOLVED for P-01 (1.0 vs 0.95, delta 0.05 > tau_4a)",
                   "inj_dp04_resolve_4a", m_d4a,
                   expect=dict(p03=("PASS", "PASS"), mechanism="RESOLVED_MECHANISM_P01",
                              resolved_level="C4a"),
                   parent="r2:INJ-DP04-4A"))

    def m_d4b(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["rL"] = [0.30] * N_INJ
            s[sex]["P02"]["rR"] = [0.30] * N_INJ
    out.append(inj("INJ-DP04-4B", "C1-4a equivalent; 4b consulted on U4 and "
                   "RESOLVED for P-01 (0.20 vs 0.30, delta 0.10 > tau_4b)",
                   "inj_dp04_resolve_4b", m_d4b,
                   expect=dict(p03=("PASS", "PASS"), mechanism="RESOLVED_MECHANISM_P01",
                              resolved_level="C4b"),
                   parent="r2:INJ-DP04-4B"))

    def m_d5(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["sst"] = [0.09] * N_INJ
    out.append(inj("INJ-DP04-C5", "C1-4b equivalent; C5 consulted on U5 and "
                   "RESOLVED for P-01 (0.05 vs 0.09, delta 0.04 > tau_5)",
                   "inj_dp04_resolve_c5", m_d5,
                   expect=dict(p03=("PASS", "PASS"), mechanism="RESOLVED_MECHANISM_P01",
                              resolved_level="C5"),
                   parent="r2:INJ-DP04-C5"))

    def m_dt(s):
        _equalize(s)
    out.append(inj("INJ-DP04-TERMINAL", "all seven levels EQUIVALENT -> "
                   "TERMINAL_FALLBACK_MECHANISM_P01",
                   "inj_dp04_terminal_fallback", m_dt,
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="TERMINAL_FALLBACK_MECHANISM_P01"),
                   parent="r2:INJ-DP04-TERMINAL"))

    def m_du(s):
        _equalize(s)
        for sex in ("F", "M"):
            s[sex]["P02"]["rho"] = [0.93] * N_INJ
    out.append(inj("INJ-DP04-EMPTY-U", "U2 forcibly emptied at consult time "
                   "-> CONTRACT_VIOLATION_EMPTY_U", "inj_dp04_empty_u_violation",
                   m_du, flags=dict(inject_empty_U2=True),
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="STOP_CONTRACT_VIOLATION_EMPTY_U",
                              stops="CONTRACT_VIOLATION_EMPTY_U"),
                   parent="r2:INJ-DP04-EMPTY-U"))

    # ---- rebuilt (Y-02): invalidity through the frozen valid-set rule ----

    def m_u2_invalid(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "SPL", "cc", 0, False)
            _set(s, sex, "SPL", "rho", 0, None)
    out.append(inj("INJ-U2-RHO-INVALID", "RE-BUILT (Y-02): the invalid C2 "
                   "statistic is produced through the frozen valid-set rule "
                   "-- the SPLINE is not crossfit-complete at observation 0 "
                   "(cc False, rho absent), both sexes; everything else "
                   "valid; equalized. Expectation: P03 PASS+PASS (V2 share "
                   "0.9); |U2|=9, |U3|=|U4|=|U5|=10 both sexes; every level "
                   "EQUIVALENT; no STOP; TERMINAL_FALLBACK_MECHANISM_P01",
                   "inj_u2_rho_invalid_exclude_v2", m_u2_invalid,
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="TERMINAL_FALLBACK_MECHANISM_P01",
                              U2=9, U3=10, U4=10, U5=10),
                   parent="r2:INJ-U2-RHO-INVALID (rebuilt)"))

    def m_u5_independent(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "SPL", "cc", 3, False)
            _set(s, sex, "SPL", "rho", 3, None)
    out.append(inj("INJ-U5-C2-INDEPENDENT", "RE-BUILT (Y-02): as the row "
                   "above, at observation 3. Expectation: |U5|=10 while "
                   "|U2|=9, both sexes; C5 disclosure names its basis as "
                   "C5-statistic validity of P-01 and P-02 (no spline "
                   "term); TERMINAL_FALLBACK_MECHANISM_P01",
                   "inj_u5_independent_of_c2_v2", m_u5_independent,
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="TERMINAL_FALLBACK_MECHANISM_P01",
                              U2=9, U5=10),
                   parent="r2:INJ-U5-C2-INDEPENDENT (rebuilt)"))

    def m_u5_sst_invalid(s):
        _equalize(s)
        _set(s, "F", "P01", "cc", 0, False)
        _set(s, "F", "P01", "rho", 0, None)
        _set(s, "F", "P01", "sst", 0, None)
    out.append(inj("INJ-U5-SST-INVALID", "RE-BUILT (Y-02): P-01 is not "
                   "crossfit-complete at observation 0 in F (cc False; rho "
                   "and sst absent there); equalized. Expectation: P03 "
                   "PASS+PASS (shares 0.9); F: |U2|=9, |U5|=9 with both "
                   "medians on those same nine; M: |U2|=|U5|=10; "
                   "|U3|=|U4|=10 both sexes; no STOP; "
                   "TERMINAL_FALLBACK_MECHANISM_P01",
                   "inj_u5_sst_invalid_exclude_v2", m_u5_sst_invalid,
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="TERMINAL_FALLBACK_MECHANISM_P01",
                              U2={"F": 9, "M": 10}, U3=10, U4=10,
                              U5={"F": 9, "M": 10}),
                   parent="r2:INJ-U5-SST-INVALID (rebuilt)"))

    def m_u_post(s):
        _equalize(s)
    out.append(inj("INJ-U-POST-CONSTRUCTION-INVALID", "the injection alters "
                   "a member's statistic AFTER the set is built and BEFORE "
                   "the data-driven re-validation of Y-03 (ii); the STOP "
                   "comes from that check re-reading the (now-corrupted) "
                   "data, not from the flag alone",
                   "inj_u_post_construction_invalid", m_u_post,
                   flags=dict(inject_post_construction_invalid_C2=0),
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="STOP_CONTRACT_VIOLATION_INCONSISTENT_U",
                              stops="CONTRACT_VIOLATION_INCONSISTENT_U"),
                   parent="r2:INJ-U-POST-CONSTRUCTION-INVALID"))

    def m_nan(s):
        for sex in ("F", "M"):
            _set(s, sex, "P01", "rho", 0, float("nan"))
    out.append(inj("INJ-NAN-STAT", "P-01 rho at observation 0 = NaN (both "
                   "sexes, crossfit-complete) -> undefined=True via section-8.1, "
                   "not a failed comparison; P-01 p03=FAIL; D-P04 not "
                   "entered; ONLY_P02_PASSES",
                   "inj_nan_stat", m_nan,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES",
                              undefined={"P01:C2:F": True, "P01:C2:M": True}),
                   parent="r2:INJ-NAN-STAT"))

    # ---- new (Y-03 (i) membership rule for C2/C4b/C5; Y-02 (b)) ----

    def m_ccfalse_finite(s):
        _equalize(s)
        _set(s, "F", "P01", "cc", 0, False)
        # rho and sst stay finite -- membership excludes by flag, not value
    out.append(inj("INJ-U-CCFALSE-FINITE", "P-01 cc flag false at "
                   "observation 0 in F while a finite rho and sst are left "
                   "in place. Expectation: P03 PASS+PASS; the observation "
                   "is outside V2 and the C5 valid set of P-01, and outside "
                   "U2 and U5 -- F: |U2|=|U5|=9, M: 10; "
                   "TERMINAL_FALLBACK_MECHANISM_P01. Membership decides, "
                   "not finiteness", "inj_u_ccfalse_finite", m_ccfalse_finite,
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="TERMINAL_FALLBACK_MECHANISM_P01",
                              U2={"F": 9, "M": 10}, U5={"F": 9, "M": 10}),
                   parent="NEW"))

    def m_nan_c4b(s):
        for sex in ("F", "M"):
            _set(s, sex, "P01", "rR", 0, float("nan"))
            # rL stays finite -- the RIGHT side, where max(rL, nan) would
            # silently drop the NaN if combined in that argument order
    out.append(inj("INJ-NAN-STAT-C4B", "P-01 rR = NaN at observation 0, "
                   "rL finite (RIGHT side deliberately, Y-03(i)); both "
                   "sexes, both probes successful, full-data reference "
                   "present. Expectation: P-01 C4b undefined=True, "
                   "passed=False; no comparison evaluated; ONLY_P02_PASSES",
                   "inj_nan_stat_c4b", m_nan_c4b,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES",
                              undefined={"P01:C4b:F": True, "P01:C4b:M": True}),
                   parent="NEW"))

    def m_nan_c5(s):
        for sex in ("F", "M"):
            _set(s, sex, "P01", "sst", 0, float("nan"))
    out.append(inj("INJ-NAN-STAT-C5", "P-01 sst = NaN at the crossfit-"
                   "complete observation 0, both sexes. Expectation: P-01 "
                   "C5 undefined, not passed; ONLY_P02_PASSES",
                   "inj_nan_stat_c5", m_nan_c5,
                   expect=dict(p03=("FAIL", "PASS"), mechanism="ONLY_P02_PASSES",
                              undefined={"P01:C5:F": True, "P01:C5:M": True}),
                   parent="NEW"))

    def m_nan_spl(s):
        for sex in ("F", "M"):
            _set(s, sex, "SPL", "rho", 0, float("nan"))
    out.append(inj("INJ-NAN-STAT-SPL", "the SPLINE's rho = NaN at the "
                   "crossfit-complete observation 0, both sexes. "
                   "Expectation: C2 undefined and not passed for BOTH "
                   "families (the benchmark statistic is required by "
                   "both); STOP_BOTH_FAIL_REDESIGN",
                   "inj_nan_stat_spl", m_nan_spl,
                   expect=dict(p03=("FAIL", "FAIL"), mechanism="STOP_BOTH_FAIL_REDESIGN",
                              stops="BOTH_FAIL_REDESIGN",
                              undefined={"P01:C2:F": True, "P01:C2:M": True,
                                        "P02:C2:F": True, "P02:C2:M": True}),
                   parent="NEW"))

    def m_c4b_noref(s):
        _equalize(s)
        for sex in ("F", "M"):
            _set(s, sex, "P01", "full", 0, False)
            _set(s, sex, "P02", "full", 1, False)
            # pL, pR stay True at those observations for the fitter
            # concerned (default) -- this IS the S-R2-1 state
    out.append(inj("INJ-C4B-NOREF", "the auditor's case T1: equalized; all "
                   "probes successful; P-01 has no full-data reference at "
                   "observation 0 and P-02 none at observation 1 (only the "
                   "full flag is set False there; phi, rL, rR are LEFT "
                   "FINITE -- r4 instruction S4(f): membership must come "
                   "from the flag, not from the value), both sexes; the "
                   "spline complete. r4 (S-R2-1 = PI_RULE, D-5 S3): the "
                   "state is a MEMBERSHIP condition -- obs 0 absent from "
                   "P-01's V3/V4, obs 1 from P-02's (flags), shares 0.9, "
                   "floors met at equality; every P03 criterion PASS; p03 "
                   "= (PASS, PASS); D-P04 all seven levels EQUIVALENT "
                   "(signed delta 0; equalized) -> "
                   "TERMINAL_FALLBACK_MECHANISM_P01; no stops record. "
                   "|U2| = |U5| = 10/10, |U3| = |U4| = 8/10 per sex. "
                   "Expectation pinned in D-5 S3 BEFORE the run",
                   "inj_c4b_noref_s_r2_1", m_c4b_noref,
                   expect=dict(p03=("PASS", "PASS"),
                              mechanism="TERMINAL_FALLBACK_MECHANISM_P01",
                              U2=10, U3=8, U4=8, U5=10),
                   parent="NEW"))

    def m_p03_c4pending_c5fail(s):
        s["F"]["P01"]["sst"] = [0.20] * N_INJ
    out.append(inj("INJ-P03-C4PENDING-C5FAIL", "C4 PENDING (REAL-type "
                   "evaluation, forced); P-01 C5 definitely fails in F, "
                   "P-02 otherwise all-pass -> P-01 p03=FAIL (definite "
                   "dominates), c4 stays PENDING; P-02 p03=PENDING -> "
                   "mechanism = MECHANISM_UNDETERMINED_PENDING_EXACTNESS; "
                   "X-08 T-P03-STATUS-A", "inj_p03_c4pending_c5fail",
                   m_p03_c4pending_c5fail,
                   expect=dict(p03=("FAIL", "PENDING"),
                              mechanism="MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_FORCED_C4_PENDING)"),
                   parent="r2:INJ-P03-C4PENDING-C5FAIL"))

    def m_p03_bothfail_c4pending(s):
        s["F"]["P01"]["sst"] = [0.20] * N_INJ
        s["M"]["P02"]["sst"] = [0.20] * N_INJ
    out.append(inj("INJ-P03-BOTHFAIL-C4PENDING", "C4 PENDING for both "
                   "families; each has a definite C5 failure in one sex -> "
                   "both p03=FAIL -> STOP_BOTH_FAIL_REDESIGN; "
                   "X-08 T-P03-STATUS-C", "inj_p03_bothfail_c4pending",
                   m_p03_bothfail_c4pending,
                   expect=dict(p03=("FAIL", "FAIL"), mechanism="STOP_BOTH_FAIL_REDESIGN",
                              stops="BOTH_FAIL_REDESIGN"),
                   parent="r2:INJ-P03-BOTHFAIL-C4PENDING"))

    # ---- R4A-01 (r4-1): spline-context UNRELATED-pending fixtures --------
    # Three decision-layer TEST_ONLY fixtures (executor's choice, disclosed:
    # three fixtures, one per context), each setting the SPL fitter's
    # per-context pending flag in sex F on an otherwise all-pass base. The
    # decision layer must route the criteria that read that context to
    # STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED), yielding p03 (PENDING,
    # PENDING) and mechanism MECHANISM_UNDETERMINED_PENDING_EXACTNESS(
    # TEST_ONLY_INJECTED). Outcomes predeclared in expect= (manifest
    # expected_* columns) BEFORE the run; a differing result is
    # EXPECTATION_FAIL. Code-derived criterion-per-context mapping (R4A-01(b)):
    #   full  -> C3 (spline phi benchmark + dS.full membership), C4b (dS.full in V4)
    #   fold  -> C2 (spline rho benchmark + dS.cc membership)
    #   probe -> C4b (dS.pL/pR membership + dS.rL/rR edge benchmark)
    # C4a reads NO spline context (ident is family-only) -> never routed.
    def m_spl_full(s):
        s["F"]["SPL"]["spl_pending_full"] = [True] + [False] * (N_INJ - 1)
    out.append(inj("INJ-SPL-PENDING-FULL", "R4A-01: the spline FULL-data "
                   "context is UNRELATED-unverifiable in F (spl_pending_full). "
                   "C3 (spline phi benchmark) and C4b (dS.full membership) in "
                   "F route to STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED) for "
                   "both families; C4a is family-only (no spline context) and "
                   "stays PASS. p03 (PENDING, PENDING); mechanism UNDETERMINED "
                   "(TEST_ONLY_INJECTED); no stops (pending is not a stop)",
                   "inj_spl_pending_full", m_spl_full,
                   expect=dict(p03=("PENDING", "PENDING"),
                              mechanism="MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"),
                   parent="NEW"))

    def m_spl_fold(s):
        s["F"]["SPL"]["spl_pending_fold"] = [True] + [False] * (N_INJ - 1)
    out.append(inj("INJ-SPL-PENDING-FOLD", "R4A-01: the spline FOLD "
                   "(cross-fit) context is UNRELATED-unverifiable in F "
                   "(spl_pending_fold). C2 (spline rho benchmark) in F routes "
                   "to STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED) for both "
                   "families. p03 (PENDING, PENDING); mechanism UNDETERMINED "
                   "(TEST_ONLY_INJECTED); no stops",
                   "inj_spl_pending_fold", m_spl_fold,
                   expect=dict(p03=("PENDING", "PENDING"),
                              mechanism="MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"),
                   parent="NEW"))

    def m_spl_probe(s):
        s["F"]["SPL"]["spl_pending_probe"] = [True] + [False] * (N_INJ - 1)
    out.append(inj("INJ-SPL-PENDING-PROBE", "R4A-01: the spline PROBE "
                   "context is UNRELATED-unverifiable in F "
                   "(spl_pending_probe). C4b (dS.pL/pR membership + dS.rL/rR "
                   "edge benchmark) in F routes to STOP_EXACTNESS_PENDING("
                   "TEST_ONLY_INJECTED) for both families. p03 (PENDING, "
                   "PENDING); mechanism UNDETERMINED (TEST_ONLY_INJECTED); "
                   "no stops",
                   "inj_spl_pending_probe", m_spl_probe,
                   expect=dict(p03=("PENDING", "PENDING"),
                              mechanism="MECHANISM_UNDETERMINED_PENDING_EXACTNESS(TEST_ONLY_INJECTED)"),
                   parent="NEW"))

    return out


INJ_FIXTURES = build_inj_fixtures()

FORCE_C4_PENDING_FIXTURE_IDS = {
    "INJ-P03-C4PENDING-C5FAIL", "INJ-P03-BOTHFAIL-C4PENDING",
}

# fixture ids that deliberately embody the S-R2-1 state (S5) so the harness
# knows to apply the S-R2-1-aware C4b rule to them (real path and decision
# layer alike); every other fixture's pL/pR/full combinations do not exhibit
# the state and are evaluated under the ordinary C4b rule.
S_R2_1_STATE_FIXTURE_IDS = {"SCEN-B", "INJ-C1-FAIL", "INJ-DP04-C1", "INJ-C4B-NOREF"}


# --------------------------------------------------------------------------
# UT-USET-CONSTRUCTION (Y-02 (b)): pure unit tests on the construction
# functions, called directly by the harness -- function-level evidence,
# no fixture outcome, no mechanism outcome, no reachability claim.
# Each returns (P01_dict_for_one_sex, P02_dict_for_one_sex) built the same
# grammar as the INJ fixtures, n_s = 10, so the harness's own U-set
# construction functions can be called on them directly.
# --------------------------------------------------------------------------
def uset_construction_cases():
    """r4 (R3A-10): each case now carries an SPL fitter too, because the
    unit test calls the REAL crit_stats + pure uset_* functions (the
    product path), which name the spline for U2/U3/U4 -- the r3 test
    re-typed the rules without the cc flag and without the spline, which
    is exactly what the audit flagged as evidence-about-the-test-only."""
    cases = {}

    def base_triple():
        return (_base_fitter(0.95, 0.10, 0.20, 0.05),
                _base_fitter(0.95, 0.10, 0.20, 0.05),
                _base_fitter(0.95, 0.10, 0.20, 0.05))

    # (a) all crossfit-complete, P-01 rho = None at observation 0
    p1, p2, ps = base_triple()
    p1["rho"][0] = None
    cases["a"] = dict(P01=p1, P02=p2, SPL=ps, expect=dict(U2=9, U5=10))

    # (b) P-01 sst = None at a crossfit-complete observation
    p1, p2, ps = base_triple()
    p1["sst"][0] = None
    cases["b"] = dict(P01=p1, P02=p2, SPL=ps, expect=dict(U5=9))

    # (c) P-01 rho = NaN at a crossfit-complete observation
    p1, p2, ps = base_triple()
    p1["rho"][0] = float("nan")
    cases["c"] = dict(P01=p1, P02=p2, SPL=ps, expect=dict(U2_excludes=0))

    # (d) P-01 rR = NaN with rL finite, both probes successful, full-data
    # reference present. S-R2-1 = PI_RULE (D-5 S4(1)(4)): U4 membership is
    # by the flags pL/pR/full ONLY -- so observation 0 IS a U4 member; the
    # NaN is caught by the post-construction data-driven re-validation
    # (Y-03(ii), INCONSISTENT_U), NOT by silent membership exclusion. The
    # expectation changed accordingly from the r3 (pre-rule) U4_excludes.
    p1, p2, ps = base_triple()
    p1["rR"][0] = float("nan")
    cases["d"] = dict(P01=p1, P02=p2, SPL=ps,
                      expect=dict(U4_includes=0, revalidation_flags_member=0))

    # (e) P-01 cc flag false with a finite rho and sst in place
    p1, p2, ps = base_triple()
    p1["cc"][0] = False
    cases["e"] = dict(P01=p1, P02=p2, SPL=ps,
                      expect=dict(U2_excludes=0, U5_excludes=0))

    return cases


UT_USET_CASES = uset_construction_cases()

COVERAGE_ROWS = [
    ("C1 pass", "SCEN-A/INJ all-pass families", "real_fit;decision_layer_injection", "covered"),
    ("C1 fail", "INJ-C1-FAIL", "decision_layer_injection", "covered"),
    ("C2 pass", "INJ-DP04-TERMINAL / INJ-DP04-C3 / INJ-DP04-4A (C2 PASS both families)", "decision_layer_injection", "covered"),
    ("C2 fail margin", "INJ-C2-MARGIN-FAIL", "decision_layer_injection", "covered"),
    ("C2 completeness-floor fail", "INJ-C2-FLOOR-FAIL + SCEN-B fold failure", "decision_layer_injection;real_fit", "covered"),
    ("C3 pass", "INJ-DP04-TERMINAL / INJ-DP04-4A / INJ-DP04-4B (C3 PASS both families)", "decision_layer_injection", "covered"),
    ("C3 fail", "INJ-C3-FAIL", "decision_layer_injection", "covered"),
    ("C3 phi-undefined path", "INJ-C3-PHI-UNDEF + PIN-ACF den=0 vector", "decision_layer_injection;unit_test", "covered"),
    ("C4a pass (real probe computation)", "SCEN-A/SCEN-B/FIX-STARTS-FULL/FIX-A5-TRUE probes", "real_fit", "covered"),
    ("C4a fail (real probe computation)", "SCEN-B injected probe failure", "real_fit", "covered"),
    ("C4a/C4b decision layer", "INJ-C4A-FAIL / INJ-C4B-FAIL / INJ-C4B-FLOOR-FAIL / INJ-DP04-4A / INJ-DP04-4B", "decision_layer_injection", "covered_injection_only"),
    ("A.5 (i) support-region condition, FALSE branch", "PIN-A5-SUPPORT on every real trajectory (SCEN-A/SCEN-B/FIX-STARTS-*)", "real_fit;assertion", "covered"),
    ("A.5 (i) support-region condition, TRUE branch", "FIX-A5-TRUE", "real_fit", "covered"),
    ("A.5 (ii) feature-start rejected + bank starts", "unit test UT-A5-II + real path via SCEN-B TEST_ONLY_INJECTION", "unit_test;real_fit", "covered"),
    ("A.5 (iii) inadmissible refit", "UNCOVERED(no construction of a numerically-complete inadmissible refit without touching frozen code -- Y-16)", "n/a", "UNCOVERED(no construction possible without touching frozen code)"),
    ("C4b pass/fail (real)", "SCEN-A paired probes (pass side); SCEN-B "
     "(fail side -- r4, S-R2-1 = PI_RULE, D-5 S4(d): 'the real-path row "
     "C4b fail takes its evidence from SCEN-B'; V4 empty in M -> C4b "
     "undefined and not passed, a definite real-path fail, no PENDING)",
     "real_fit", "covered"),
    # r4 (T-3, content S6 wording adopted VERBATIM -- R3A-08/Y-11):
    ("K-05 invariant: C4b completeness PASS implies C4a PASS. "
     "The excluded combination is C4b-completeness-PASS + C4a-FAIL. "
     "C4b-completeness-FAIL + C4a-PASS is a legitimate case (INJ-C4B-FLOOR-FAIL).",
     "PIN-K05-INVARIANT assert on every fixture + INJ-C4B-FLOOR-FAIL",
     "assertion;decision_layer_injection", "covered"),
    ("C5 pass", "SCEN-A / INJ baselines", "real_fit;decision_layer_injection", "covered"),
    ("C5 fail", "INJ-C5-FAIL", "decision_layer_injection", "covered"),
    ("C6 structural pass", "asserted constants (every fixture)", "assertion", "covered"),
    ("fold failure -> crossfit-incomplete", "SCEN-B F0 (F2 fault flags)", "real_fit", "covered"),
    ("probe failure (fitter path)", "SCEN-B M0 (F2 fault flags)", "real_fit", "covered"),
    ("spline FAILURE full-data", "SCEN-B M0 (TEST_ONLY_INJECTION)", "real_fit", "covered"),
    ("spline FAILURE masked", "SCEN-B M0 fold-1 (TEST_ONLY_INJECTION)", "real_fit", "covered"),
    ("FEATURE_START_REJECTED under mask", "SCEN-B F0 fold-0 (TEST_ONLY_INJECTION)", "real_fit", "covered"),
    ("F2 failure codes reachable through wrapper", "NR-01 (ii) T-2a wrapper adapter only (NOT NR-01(i)'s native engine replay)", "real_fit", "covered"),
    ("sex-split fail", "INJ-SEX-SPLIT", "decision_layer_injection", "covered"),
    ("both pass -> D-P04 mechanism", "INJ-DP04-* family", "decision_layer_injection", "covered"),
    ("exactly one passes -> ONLY_P01/ONLY_P02", "INJ-ONLY-P01 / INJ-C1..C5-FAIL", "decision_layer_injection", "covered"),
    ("both fail -> BOTH_FAIL_REDESIGN", "INJ-BOTH-FAIL", "decision_layer_injection", "covered"),
    # r4 (S-R2-1 = PI_RULE, D-5 S4(d)): the row is covered by INJ-DP04-C1.
    ("D-P04 resolve at C1", "INJ-DP04-C1 (r4: PI_RULE membership -> p03 PASS/PASS -> D-P04 RESOLVED at C1 for P-01)", "decision_layer_injection", "covered"),
    ("D-P04 resolve at C2 + common-set-vs-candidate-specific divergence", "INJ-DP04-C2-DIVERGE", "decision_layer_injection", "covered"),
    ("D-P04 resolve at C3", "INJ-DP04-C3", "decision_layer_injection", "covered"),
    ("D-P04 resolve at 4a / 4b (decision layer)", "INJ-DP04-4A / INJ-DP04-4B", "decision_layer_injection", "covered_injection_only"),
    ("D-P04 resolve at C5", "INJ-DP04-C5", "decision_layer_injection", "covered"),
    ("D-P04 terminal fallback", "INJ-DP04-TERMINAL", "decision_layer_injection", "covered"),
    ("unconsulted levels not recomputed (evidence)", "recompute counters asserted in INJ-DP04-C2-DIVERGE (C4b/C5 = 0) and in INJ-DP04-C1 (r4: RESOLVED at C1 -> every subset level 0)", "assertion", "covered"),
    ("CONTRACT_VIOLATION_EMPTY_U", "INJ-DP04-EMPTY-U", "decision_layer_injection", "covered"),
    ("U2/U4/U5 membership-first construction (Y-02)", "INJ-U2-RHO-INVALID / INJ-U5-C2-INDEPENDENT / INJ-U5-SST-INVALID (rebuilt) + UT-USET-CONSTRUCTION", "decision_layer_injection;unit_test", "covered"),
    ("U-set membership decided by flag, not finiteness of a retained value", "INJ-U-CCFALSE-FINITE + UT-USET-CONSTRUCTION (e)", "decision_layer_injection;unit_test", "covered"),
    ("CONTRACT_VIOLATION_INCONSISTENT_U (post-construction, data-driven)", "INJ-U-POST-CONSTRUCTION-INVALID", "decision_layer_injection", "covered"),
    ("finite-valued validity / NaN handling in P03: C2", "INJ-NAN-STAT", "decision_layer_injection", "covered"),
    ("finite-valued validity / NaN handling in P03: C4b (order-dependent max)", "INJ-NAN-STAT-C4B", "decision_layer_injection", "covered"),
    ("finite-valued validity / NaN handling in P03: C5", "INJ-NAN-STAT-C5", "decision_layer_injection", "covered"),
    ("finite-valued validity / NaN handling in P03: spline (both families)", "INJ-NAN-STAT-SPL", "decision_layer_injection", "covered"),
    ("D-P04 comparator never RESOLVED/EQUIVALENT on NaN", "T-COMPARATOR-NAN (function-level)", "unit_test", "covered"),
    ("S-R2-1 state: real path", "SCEN-B (M0, spline)", "real_fit", "covered"),
    ("S-R2-1 state: decision layer, ALREADY_BINDING-shaped construction reused under DEFERRED", "INJ-C1-FAIL, INJ-DP04-C1", "decision_layer_injection", "covered"),
    ("S-R2-1 state: dedicated fixture, both families", "INJ-C4B-NOREF", "decision_layer_injection", "covered"),
    ("P03 status: definite failure with a PENDING criterion", "INJ-P03-C4PENDING-C5FAIL", "decision_layer_injection", "covered"),
    ("P03 status: both families definite-fail while C4 PENDING", "INJ-P03-BOTHFAIL-C4PENDING", "decision_layer_injection", "covered"),
    ("start-bank default (FULL_LATTICE, 731/261+feature)", "FIX-STARTS-FULL", "real_fit", "covered"),
    ("start-bank duplicate feature start", "FIX-STARTS-DUP", "real_fit", "covered"),
    ("probe_success decoupled from full-data fit", "UT-PROBE-DECOUPLE (unit test)", "unit_test", "covered"),
    ("SOLVER-B unverifiable-acceptance capture, stage 1", "INJ-EXC-CAPTURE-S1", "unit_test", "covered"),
    ("SOLVER-B unverifiable-acceptance capture, stage 2", "INJ-EXC-CAPTURE-S2", "unit_test", "covered"),
    ("SOLVER-B unrelated exception NOT converted (fit context)", "INJ-EXC-UNRELATED-TYPE", "unit_test", "covered"),
    ("SOLVER-B unrelated exception NOT converted (reference/no accept)", "UT-EXC-UNRELATED-REFERENCE (1a, 1b)", "unit_test", "covered"),
    ("exception wrapper restoration", "T-WRAPPER-RESTORE (assertion)", "assertion", "covered"),
    ("reporting fields populated / undefined flags", "all fixtures (schema check)", "assertion", "covered"),
    ("clean execution / process provenance disclosed", "T-CALLCOUNT (per-phase/per-pid) + process block + attempt log (Y-01)", "assertion", "covered"),
    # R4A-01 (r4-1): spline-context UNRELATED-pending routing into the
    # decision grammar, one row per context.
    ("spline FULL context pending -> C3/C4b PENDING (R4A-01)", "INJ-SPL-PENDING-FULL + T-EXC-UNRELATED-TYPE (eval-level)", "decision_layer_injection;unit_test", "covered"),
    ("spline FOLD context pending -> C2 PENDING (R4A-01)", "INJ-SPL-PENDING-FOLD + T-EXC-UNRELATED-TYPE (eval-level)", "decision_layer_injection;unit_test", "covered"),
    ("spline PROBE context pending -> C4b PENDING (R4A-01)", "INJ-SPL-PENDING-PROBE + T-EXC-UNRELATED-TYPE (eval-level)", "decision_layer_injection;unit_test", "covered"),
]

MANIFEST_HEADER = [
    "fixture_id", "fixture_class", "exact_construction", "implemented_construction_key",
    "n_per_sex", "fixture_rng_seed", "injection_modes", "interpretation",
    "start_bank", "evidence_class", "injection_sites", "expected_outcome",
    "parent_fixture_id", "run_scope",
    "expected_p03", "expected_mechanism_outcome", "expected_resolved_level",
    "expected_U_sizes", "expected_stops", "expected_undefined",
]


def _fmt_expect(fx):
    """T-EXPECT-ALL (P-6, independent audit 2026-09-23): serialize a
    fixture's expect= dict into the manifest's six expected_* columns.
    p03 = (P01_status, P02_status). U2..U5 values are either a plain int
    (both sexes share it) or {"F":.., "M":..} (per-sex). undefined is
    {"family:criterion:sex": bool}. stops is the bare stop-type string
    (e.g. "BOTH_FAIL_REDESIGN"), matching results['stops'][i]['stop']."""
    e = fx.get("expect", {})
    p03 = e.get("p03", "")
    p03s = ";".join(p03) if isinstance(p03, tuple) else str(p03)
    mech = e.get("mechanism", "")
    lvl = e.get("resolved_level", "")
    usize_parts = []
    for k in ("U2", "U3", "U4", "U5"):
        if k not in e:
            continue
        v = e[k]
        if isinstance(v, dict):
            usize_parts.append(";".join(f"{k}:{sx}={v[sx]}" for sx in sorted(v)))
        else:
            usize_parts.append(f"{k}={v}")
    usizes = ";".join(usize_parts)
    stops = e.get("stops", "")
    undef = ";".join(f"{k}={v}" for k, v in sorted(e.get("undefined", {}).items()))
    return p03s, mech, lvl, usizes, stops, undef


def manifest_rows():
    rows = []
    for sc in REAL_SCENARIOS:
        seeds = ";".join(str(t[1]) for sx in ("F", "M") for t in sc["strata"][sx])
        n = len(sc["strata"]["F"])
        injm = ";".join(f'{i["target"]}:{i["family"]}:{i["context"]}:{i["mode"]}'
                        for i in sc["injections"]) or "none"
        inj_sites = ";".join(f'{i["target"]}:{i["context"]}' for i in sc["injections"]) or "none"
        p03s, mech, lvl, usizes, stops, undef = _fmt_expect(sc)
        rows.append([sc["fixture_id"], sc["fixture_class"], sc["prose"], sc["key"],
                     str(n), seeds, injm, "PATH_COVERAGE_ONLY",
                     sc["start_bank"], sc["evidence_class"], inj_sites,
                     "as-computed", "r2:" + sc["fixture_id"], sc["run_scope"],
                     p03s, mech, lvl, usizes, stops, undef])
    for traj in (STARTS_FULL_TRAJ, STARTS_DUP_TRAJ):
        n = "1" if traj is STARTS_FULL_TRAJ else "2"
        seed = str(traj.get("seed", "")) if traj is STARTS_FULL_TRAJ else "none(TEST_CONSTANT)"
        expected = "start_count==retained+feature" if traj is STARTS_FULL_TRAJ else "FEATURE_START_REJECTED(duplicate)"
        rows.append([traj["fixture_id"], traj["fixture_class"], traj["prose"],
                     traj["key"], n, seed, "none", "PATH_COVERAGE_ONLY",
                     traj["start_bank"], traj["evidence_class"], "none",
                     expected, "r2:" + traj["fixture_id"], traj["run_scope"],
                     "", "", "", "", "", ""])
    rows.append([FIX_A5_TRUE["fixture_id"], FIX_A5_TRUE["fixture_class"],
                 FIX_A5_TRUE["prose"], FIX_A5_TRUE["key"], "2", "none(TEST_CONSTANT)",
                 "none", "PATH_COVERAGE_ONLY", FIX_A5_TRUE["start_bank"],
                 FIX_A5_TRUE["evidence_class"], "none",
                 "A5(i)=true both sides; probe excluded from C4a/C4b", "NEW",
                 FIX_A5_TRUE["run_scope"], "", "", "", "", "", ""])
    for fx in INJ_FIXTURES:
        flg = ";".join(f"{k}={v}" for k, v in fx["flags"].items()) or "none"
        p03s, mech, lvl, usizes, stops, undef = _fmt_expect(fx)
        rows.append([fx["fixture_id"], fx["fixture_class"], fx["prose"], fx["key"],
                     str(N_INJ), "none", "TEST_ONLY_INJECTION;" + flg,
                     "PATH_COVERAGE_ONLY", "NOT_APPLICABLE",
                     "decision_layer_injection", "constructed_directly",
                     "as-described", fx["parent_fixture_id"], "both",
                     p03s, mech, lvl, usizes, stops, undef])
    for key in sorted(UT_USET_CASES):
        rows.append([f"UT-USET-CONSTRUCTION-{key}", "unit_test_construction",
                     "pure function call on Y-02(b) construction functions",
                     f"uset_construction_case_{key}", "1", "none", "none",
                     "PATH_COVERAGE_ONLY", "NOT_APPLICABLE", "unit_test",
                     "function_call", "function-level; no fixture outcome",
                     "NEW", "once", "", "", "", "", "", ""])
    for fid, prose in (
        ("INJ-EXC-CAPTURE-S1", "stage-1 nnls RuntimeError injection on a TEST_CONSTANT full-data spline fit; arming rule per Y-04(c)"),
        ("INJ-EXC-CAPTURE-S2", "stage-1 and stage-2 nnls RuntimeError injections, each firing once, on a TEST_CONSTANT full-data spline fit"),
        ("INJ-EXC-UNRELATED-TYPE", "a ValueError raised at the covered call site at stage 1 on a TEST_CONSTANT full-data spline fit; must classify UNRELATED, not converted"),
    ):
        rows.append([fid, "injected_exception_context", prose, fid.lower(),
                     "1", "none", "TEST_ONLY_INJECTION", "PATH_COVERAGE_ONLY",
                     "NOT_APPLICABLE", "unit_test", "declared arming rule (Y-04(c))",
                     "see Y-04 test contracts", "NEW",
                     "both(two full deterministic passes in the unit_tests "
                     "phase, results asserted identical -- R3A-03)",
                     "", "", "", "", "", ""])
    rows.append(["UT-EXC-UNRELATED-REFERENCE", "unit_test", "two unit tests "
                "calling the loaded reference function directly, never "
                "inside NR-SPL: (1a) nnls raises inside reference itself, "
                "neither kkt_res nor accept on the stack; (1b) nnls raises "
                "inside kkt_res while reference calls it, accept not on "
                "the stack", "ut_exc_unrelated_reference", "1", "none",
                "none", "PATH_COVERAGE_ONLY", "NOT_APPLICABLE", "unit_test",
                "function_call", "classifier says UNRELATED both times",
                "NEW", "once", "", "", "", "", "", ""])
    return rows
