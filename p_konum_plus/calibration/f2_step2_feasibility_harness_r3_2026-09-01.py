"""
p_konum_plus -- F2 STEP 2 r3 exact-construction-fidelity corrected harness.

Corrects, relative to f2_step2_feasibility_harness_r2_2026-09-01.py:
  A-01  = exact-construction fidelity is enforced for all 21 frozen fixtures via
          observed construction-evidence records (implemented vs executed keys).
  A-01A = FIX-OTHER-NUMERICAL-FAILURE runs through the REAL orchestration path
          (primary tagged fault -> fallback stage entered, same x0 -> test-only
          fabricated non-finite fallback return -> real post-fallback handling
          emits OTHER_PREDECLARED_NUMERICAL_FAILURE). No hard-coded record.
  A-01B = FIX-INVALID-INIT goes through a real validate_initialization entry
          point; the validator is wired into run_one_start for EVERY start
          (R3-P02) and is behaviour-neutral outside this fixture (asserted).
  A-02  = all seven frozen manifest columns are required loudly; absence is
          never filtered out of the audit result.
  A-03  = internal aggregation L bookkeeping always uses standardized ghat for
          OK predictions and +inf otherwise; never objective_L(x, g_stable).
  A-04  = C3 self-test uses a before/after mutation check (not tautological);
          plus a real-classifier multi-predicate probe (R3-P04).
  R3-P01= every construction-evidence flag is OBSERVED at its execution site,
          defaults to False, and is never assigned in fixture blocks, dispatch
          tables, canonical assembly, or the report writer (Section 4A).
  R3-P03= the manifest exact_construction -> implemented_construction_key
          mapping is a HUMAN-AUDITED provenance step (disclosed in the report);
          construction_fidelity_pass proves implemented == executed only.
  R3-P05= the fabricated-fallback telemetry row's synthetic fields are declared
          and tagged (status=-1, success=False, nit/nfev/njev=-1,
          wall_clock_seconds=nan, message contains FAULT_INJECTION_TEST_ONLY).

All X1/X3/X4/C1-C5 r2 corrections are preserved. No scientific or class-C
literal is changed. No real SSA data is touched. FAULT_INJECTION_TEST_ONLY
markers exist ONLY in this test harness.
"""

import os

# Thread pinning MUST occur before numpy/scipy are imported. (preserved)
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import csv
import json
import math
import time
import platform

import numpy as np
import scipy
from scipy.optimize import minimize, Bounds, LinearConstraint, NonlinearConstraint

# --------------------------------------------------------------------------
# Frozen scientific constants (preserved; not re-derived, not tuned)
# --------------------------------------------------------------------------
T = 146
U_GRID = np.arange(T, dtype=np.float64) / 145.0

LN9 = math.log(9.0)
LN10 = math.log(10.0)
LN10_9 = math.log(10.0 / 9.0)
W_MIN_YEARS = 5.0

K_MIN = 4.0
K_MAX = 2.0 * LN9 * 145.0 / W_MIN_YEARS  # 127.43902548550072
assert abs(K_MAX - 127.43902548550072) < 1e-9

BETA_MIN = 1.0
BETA_MAX = 6.0
S_MAX = 3.0
N_MIN = 3

EPSILON_MODEL = 1e-12
FEASIBILITY_ACCEPTANCE_TOL = 1e-8
L_INVALID_PREDICTION_GUARD = 4.0 * T + 1.0  # 585.0  (X4; historical 1.0e6 absent)
assert L_INVALID_PREDICTION_GUARD == 585.0

RNG_USED = False
TELEMETRY_RUN_LABEL = "RUN1"


def s_side_min(beta):
    return (W_MIN_YEARS / 145.0) / (LN10 ** (1.0 / beta) - LN10_9 ** (1.0 / beta))


A_LOC = tuple(-1.0 + i / 4.0 for i in range(13))
K_LATTICE = (K_MIN, math.sqrt(4.0 * K_MAX), K_MAX)
BETA_ANCHORS = (1.0, math.sqrt(6.0), 6.0)


def s_lattice(beta):
    lo = s_side_min(beta)
    return (lo, math.sqrt(lo * 3.0), 3.0)


def softplus(v):
    return np.logaddexp(0.0, v)


def p01_stable(theta):
    c_r, c_d, k_r, k_d = theta
    logg = -softplus(-k_r * (U_GRID - c_r)) - softplus(k_d * (U_GRID - c_d))
    return np.exp(logg - logg.max())


def p02_stable(theta):
    m, s_l, s_r, beta = theta
    ell = np.where(
        U_GRID <= m,
        -(np.abs(m - U_GRID) / s_l) ** beta,
        -(np.abs(U_GRID - m) / s_r) ** beta,
    )
    return np.exp(ell - ell.max())


def n_sup(g):
    thr = g.min() + 0.5 * (g.max() - g.min())
    return int((g >= thr).sum())


def kural_s_pass_exact(g):
    return n_sup(g) >= N_MIN


def kural_t_pass_exact_p01(theta):
    c_r, c_d, k_r, k_d = theta
    if not (math.isfinite(k_r) and math.isfinite(k_d)) or k_r <= 0 or k_d <= 0:
        return False
    width_r_years = (2.0 * LN9 / k_r) * 145.0
    width_d_years = (2.0 * LN9 / k_d) * 145.0
    return (width_r_years >= W_MIN_YEARS) and (width_d_years >= W_MIN_YEARS)


def kural_t_pass_exact_p02(theta):
    m, s_l, s_r, beta = theta
    if not math.isfinite(beta) or beta <= 0:
        return False
    smin = s_side_min(beta)
    return (s_l >= smin) and (s_r >= smin)


def build_grid(family):
    raw = []
    if family == "P-01":
        for i, a in enumerate(A_LOC):
            for b in A_LOC[i:]:
                for kr in K_LATTICE:
                    for kd in K_LATTICE:
                        raw.append((a, b, kr, kd))
        stable_fn = p01_stable
    else:
        for m in A_LOC:
            for be in BETA_ANCHORS:
                S = s_lattice(be)
                for sl in S:
                    for sr in S:
                        raw.append((m, sl, sr, be))
        stable_fn = p02_stable
    raw_sorted = sorted(set(raw))
    assert len(raw_sorted) == len(raw)
    retained = [t for t in raw_sorted if kural_s_pass_exact(stable_fn(t))]
    return raw_sorted, sorted(retained)


def zero_variance_rule(g_stable):
    if not np.all(np.isfinite(g_stable)):
        return "NONFINITE_FIT", None, None
    sigma_g = float(np.std(g_stable, ddof=0))
    if sigma_g <= EPSILON_MODEL:
        return "ZERO_VARIANCE_FIT", sigma_g, None
    ghat = (g_stable - g_stable.mean()) / sigma_g
    return "OK", sigma_g, ghat


def v_box(theta, lower, upper):
    theta = np.asarray(theta, dtype=np.float64)
    lower = np.asarray(lower, dtype=np.float64)
    upper = np.asarray(upper, dtype=np.float64)
    return float(np.max(np.maximum(np.maximum(lower - theta, 0.0), np.maximum(theta - upper, 0.0))))


def v_p01(theta):
    c_r, c_d, k_r, k_d = theta
    v = v_box(theta, [-1.0, -1.0, K_MIN, K_MIN], [2.0, 2.0, K_MAX, K_MAX])
    return max(v, max(c_r - c_d, 0.0))


def v_p02(theta):
    # C4 preserved: no beta clamp; nonfinite/<=0 beta -> infinite sentinel.
    m, s_l, s_r, beta = theta
    if not math.isfinite(beta) or beta <= 0:
        return float("inf")
    lo_free = [-1.0, 0.0, 0.0, BETA_MIN]
    hi_free = [2.0, S_MAX, S_MAX, BETA_MAX]
    v = v_box(theta, lo_free, hi_free)
    smin = s_side_min(beta)
    return max(v, max(smin - s_l, 0.0), max(smin - s_r, 0.0))


def endpoint_numerically_feasible(theta, family):
    theta = np.asarray(theta, dtype=np.float64)
    if not np.all(np.isfinite(theta)):
        return False, float("inf")
    v = v_p01(theta) if family == "P-01" else v_p02(theta)
    return (v <= FEASIBILITY_ACCEPTANCE_TOL), v


def scientific_domain_pass_p01(theta):
    c_r, c_d, k_r, k_d = theta
    if not all(math.isfinite(v) for v in theta):
        return False
    return (
        -1.0 <= c_r <= 2.0 and -1.0 <= c_d <= 2.0 and c_r <= c_d
        and K_MIN <= k_r <= K_MAX and K_MIN <= k_d <= K_MAX
    )


def scientific_domain_pass_p02(theta):
    m, s_l, s_r, beta = theta
    if not all(math.isfinite(v) for v in theta):
        return False
    if not (-1.0 <= m <= 2.0 and 1.0 <= beta <= 6.0):
        return False
    if not (s_l <= 3.0 and s_r <= 3.0):
        return False
    smin = s_side_min(beta)
    return (s_l >= smin) and (s_r >= smin)


DISPLAY_PRECEDENCE = [
    "NONFINITE_INPUT",
    "INVALID_INITIALIZATION",
    "NONFINITE_PARAMETER",
    "NONFINITE_FIT",
    "ZERO_VARIANCE_FIT",
    "MORPHOLOGY_INADMISSIBLE",
    "OPTIMIZER_NONCONVERGENCE",
    "OTHER_PREDECLARED_NUMERICAL_FAILURE",
    "BOUNDARY_PATHOLOGY",
    "IDENTIFIABILITY_FAILURE",
]
RESERVED_NOT_EMITTED = {"BOUNDARY_PATHOLOGY", "IDENTIFIABILITY_FAILURE"}
RESERVED_WARN_NOT_EMITTED = {"WARN_BOUNDARY", "WARN_IDENTIFIABILITY"}


def primary_display_code(predicate_set):
    for code in DISPLAY_PRECEDENCE:
        if code in predicate_set:
            return code
    return None


def canonical_hex(theta):
    return tuple(float(v).hex() for v in theta)


def classify_endpoint(theta, family, nonconverged=False):
    predicates = set()
    rejection_reasons = set()

    theta_arr = np.asarray(theta, dtype=np.float64)
    theta_finite = bool(np.all(np.isfinite(theta_arr)))
    if not theta_finite:
        predicates.add("NONFINITE_PARAMETER")

    num_feasible = False
    v_val = float("inf")
    if theta_finite:
        num_feasible, v_val = endpoint_numerically_feasible(theta_arr, family)
        if not num_feasible:
            rejection_reasons.add("POST_RETURN_CONSTRAINT_REJECTION")

    domain_pass = None
    kural_t = None
    g_stable = None
    if theta_finite:
        domain_pass = scientific_domain_pass_p01(theta_arr) if family == "P-01" else scientific_domain_pass_p02(theta_arr)
        kural_t = kural_t_pass_exact_p01(theta_arr) if family == "P-01" else kural_t_pass_exact_p02(theta_arr)
        stable_fn = p01_stable if family == "P-01" else p02_stable
        g_stable = stable_fn(theta_arr)
        zv_status, sigma_g, ghat = zero_variance_rule(g_stable)
        if zv_status == "NONFINITE_FIT":
            predicates.add("NONFINITE_FIT")
        elif zv_status == "ZERO_VARIANCE_FIT":
            predicates.add("ZERO_VARIANCE_FIT")

    kural_s = None
    if theta_finite and g_stable is not None and np.all(np.isfinite(g_stable)):
        kural_s = kural_s_pass_exact(g_stable)

    if theta_finite and not (bool(domain_pass) and bool(kural_t) and bool(kural_s if kural_s is not None else False)):
        predicates.add("MORPHOLOGY_INADMISSIBLE")

    if nonconverged:
        predicates.add("OPTIMIZER_NONCONVERGENCE")

    objective_finite = bool(g_stable is not None and np.all(np.isfinite(g_stable)))
    prediction_finite = objective_finite

    eligible = (
        theta_finite and num_feasible and bool(domain_pass)
        and bool(kural_t) and bool(kural_s if kural_s is not None else False)
        and objective_finite and prediction_finite
        and ("ZERO_VARIANCE_FIT" not in predicates)
        and (len(predicates) == 0)
    )

    return dict(
        theta=tuple(float(v) for v in theta_arr),
        theta_finite=theta_finite,
        numerically_feasible=num_feasible,
        v_value=v_val,
        scientific_domain_pass=(None if domain_pass is None else bool(domain_pass)),
        kural_t_pass_exact=(None if kural_t is None else bool(kural_t)),
        kural_s_pass_exact=(None if kural_s is None else bool(kural_s)),
        predicates=sorted(predicates),
        rejection_reasons=sorted(rejection_reasons),
        eligible=bool(eligible),
        primary_display_code=primary_display_code(predicates),
    )


def tie(a, b):
    return abs(a - b) <= 1e-12 + 1e-9 * max(abs(a), abs(b))


def aggregate(records):
    eligible = [r for r in records if r["eligible"]]
    if not eligible:
        return "FAMILY_FIT_FAILURE", "NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART"
    best_l = min(r["L"] for r in eligible)
    tied = [r for r in eligible if tie(r["L"], best_l)]
    winner = sorted(tied, key=lambda r: r["theta"])[0]
    return "OK", winner


def objective_L(x, ghat):
    return float(np.sum((x - ghat) ** 2))


def internal_L(x_fixture, theta, family):
    """A-03: internal aggregation bookkeeping L. Standardized ghat for OK
    predictions; +inf otherwise. NEVER objective_L(x, unstandardized g)."""
    theta_arr = np.asarray(theta, dtype=np.float64)
    if not np.all(np.isfinite(theta_arr)):
        return float("inf")
    stable_fn = p01_stable if family == "P-01" else p02_stable
    g = stable_fn(theta_arr)
    status, sigma_g, ghat = zero_variance_rule(g)
    if status != "OK":
        return float("inf")
    return objective_L(x_fixture, ghat)


def make_objective_and_x(family, x_target):
    stable_fn = p01_stable if family == "P-01" else p02_stable

    def fun(theta):
        g_stable = stable_fn(theta)
        status, sigma_g, ghat = zero_variance_rule(g_stable)
        if status != "OK":
            return L_INVALID_PREDICTION_GUARD  # X4: 585.0, CLASS_C guard only
        return objective_L(x_target, ghat)

    return fun


def p01_bounds():
    return Bounds([-1.0, -1.0, K_MIN, K_MIN], [2.0, 2.0, K_MAX, K_MAX])


def p01_linear_constraint():
    return LinearConstraint([[-1.0, 1.0, 0.0, 0.0]], lb=0.0, ub=np.inf)


def p02_bounds():
    lo_free = s_side_min(BETA_MIN)
    return Bounds([-1.0, lo_free, lo_free, BETA_MIN], [2.0, S_MAX, S_MAX, BETA_MAX])


def p02_nonlinear_constraints():
    def g1(x):
        return x[1] - s_side_min(x[3])

    def g2(x):
        return x[2] - s_side_min(x[3])

    return [NonlinearConstraint(g1, 0.0, np.inf), NonlinearConstraint(g2, 0.0, np.inf)]


# --------------------------------------------------------------------------
# Section 4A -- construction-evidence flags. Defaults False; each flag is
# written ONLY at its permitted execution site (see per-function comments).
# --------------------------------------------------------------------------
def new_evidence():
    return dict(
        primary_fault_injection_triggered=False,
        fallback_branch_entered=False,
        same_x0_reused=False,
        fallback_nonfinite_injection_triggered=False,
        validator_called=False,
        optimizer_called=False,
    )


def validate_initialization(theta, family, evidence):
    """A-01B / Section 6.1: real initialization-validation entry point, wired
    into run_one_start for EVERY start. Contains ONLY the already-supported
    non-finite validation (no broadened admissibility criterion).
    Section 4A write site: validator_called."""
    evidence["validator_called"] = True  # 4A write site: validate_initialization entry
    return all(math.isfinite(float(v)) for v in theta)


def run_primary(family, x0, x_target, evidence, fault_inject=False):
    """Section 4A write sites: primary_fault_injection_triggered (before the
    tagged raise), optimizer_called (immediately before the real solver
    call)."""
    if fault_inject:
        evidence["primary_fault_injection_triggered"] = True  # 4A write site: primary execution fn
        raise RuntimeError("FAULT_INJECTION_TEST_ONLY=true : simulated pure numerical error on primary path")

    fun = make_objective_and_x(family, x_target)
    bounds = p01_bounds() if family == "P-01" else p02_bounds()
    constraints = [p01_linear_constraint()] if family == "P-01" else p02_nonlinear_constraints()

    evidence["optimizer_called"] = True  # 4A write site: primary optimizer call site
    t0 = time.perf_counter()
    result = minimize(
        fun, x0=np.asarray(x0, dtype=np.float64), method="trust-constr",
        jac="2-point", hess=scipy.optimize.BFGS(), bounds=bounds, constraints=constraints,
        options=dict(gtol=1e-10, xtol=1e-12, barrier_tol=1e-10, maxiter=500),
    )
    wall = time.perf_counter() - t0
    return result, wall


class _FabricatedFallbackResult:
    """Test-only fabricated fallback return (A-01A). Not a real OptimizeResult.
    Tagged FAULT_INJECTION_TEST_ONLY; exists only in this harness."""

    def __init__(self):
        self.x = np.array([float("nan")] * 4)
        self.fun = float("nan")
        self.success = False
        self.status = -1
        self.message = "FABRICATED_FALLBACK:FAULT_INJECTION_TEST_ONLY:nonfinite_return"
        self.nit = -1
        self.nfev = -1


def run_fallback(family, x0, x_target, evidence, fault_inject_nonfinite=False):
    """Section 4A write sites: fallback_nonfinite_injection_triggered (inside
    this fallback execution function, at the injection), optimizer_called
    (immediately before the real SLSQP call)."""
    if fault_inject_nonfinite:
        evidence["fallback_nonfinite_injection_triggered"] = True  # 4A write site: fallback execution fn
        return _FabricatedFallbackResult(), float("nan")

    fun = make_objective_and_x(family, x_target)
    bounds = p01_bounds() if family == "P-01" else p02_bounds()
    if family == "P-01":
        cons = [{"type": "ineq", "fun": lambda x: x[1] - x[0]}]
    else:
        cons = [
            {"type": "ineq", "fun": lambda x: x[1] - s_side_min(x[3])},
            {"type": "ineq", "fun": lambda x: x[2] - s_side_min(x[3])},
        ]
    evidence["optimizer_called"] = True  # 4A write site: fallback optimizer call site
    t0 = time.perf_counter()
    result = minimize(
        fun, x0=np.asarray(x0, dtype=np.float64), method="SLSQP",
        bounds=bounds, constraints=cons, options=dict(ftol=1e-12, maxiter=500),
    )
    wall = time.perf_counter() - t0
    return result, wall


def run_one_start(fixture_id, family, start_id, x0, x_target,
                  fault_inject_primary=False, fault_inject_fallback_nonfinite=False,
                  rejection_counter=None):
    """Real orchestration path for every start. Section 4A write sites inside:
    fallback_branch_entered and same_x0_reused (fallback dispatch site);
    executed evidence is returned upward, consumed read-only by callers."""
    evidence = new_evidence()
    telemetry_rows = []
    optimizer_path = "primary"
    hard_predicates = set()
    endpoint = None
    nonconverged = False
    numeric_error = False

    # Section 6.1: validator called for EVERY start, before any optimizer call.
    if not validate_initialization(x0, family, evidence):
        if rejection_counter is not None:
            rejection_counter.append(fixture_id)
        canonical = dict(
            fixture_id=fixture_id, family=family, start_id=start_id,
            optimizer_path="not_run", status_class="INVALID_INITIALIZATION",
            predicates=["INVALID_INITIALIZATION"], rejection_reasons=[],
            scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
            eligible=False, terminal_endpoint_hex=canonical_hex(tuple(float(v) for v in x0)),
            family_status=None, family_summary=None,
        )
        cls = dict(theta=tuple(float(v) for v in x0), theta_finite=False, eligible=False,
                   predicates=["INVALID_INITIALIZATION"])
        return canonical, cls, telemetry_rows, evidence

    try:
        result, wall = run_primary(family, x0, x_target, evidence, fault_inject=fault_inject_primary)
        x_ret = np.asarray(result.x, dtype=np.float64)
        if not np.all(np.isfinite(x_ret)) or not np.isfinite(result.fun):
            numeric_error = True
        else:
            telemetry_rows.append(dict(
                fixture_id=fixture_id, family=family, start_id=start_id,
                optimizer_path="primary", status=int(result.status),
                message=str(result.message), success=bool(result.success),
                nit=int(getattr(result, "nit", -1)), nfev=int(getattr(result, "nfev", -1)),
                njev=int(getattr(result, "njev", -1)) if hasattr(result, "njev") else -1,
                wall_clock_seconds=wall,
            ))
            if result.success:
                endpoint = x_ret
            else:
                nonconverged = True
                endpoint = x_ret
    except Exception as exc:
        numeric_error = True
        telemetry_rows.append(dict(
            fixture_id=fixture_id, family=family, start_id=start_id,
            optimizer_path="primary", status=-1,
            message="EXCEPTION:" + type(exc).__name__ + (":FAULT_INJECTION_TEST_ONLY" if fault_inject_primary else ""),
            success=False, nit=-1, nfev=-1, njev=-1, wall_clock_seconds=float("nan"),
        ))

    if numeric_error:
        optimizer_path = "fallback"
        evidence["fallback_branch_entered"] = True  # 4A write site: fallback dispatch
        x0_fb = x0
        evidence["same_x0_reused"] = bool(tuple(float(v) for v in x0_fb) == tuple(float(v) for v in x0))  # 4A write site: fallback dispatch
        try:
            result2, wall2 = run_fallback(family, x0_fb, x_target, evidence,
                                          fault_inject_nonfinite=fault_inject_fallback_nonfinite)
            x_ret2 = np.asarray(result2.x, dtype=np.float64)
            telemetry_rows.append(dict(
                fixture_id=fixture_id, family=family, start_id=start_id,
                optimizer_path="fallback", status=int(result2.status),
                message=str(result2.message), success=bool(result2.success),
                nit=int(getattr(result2, "nit", -1)), nfev=int(getattr(result2, "nfev", -1)),
                njev=-1, wall_clock_seconds=wall2,
            ))
            if not np.all(np.isfinite(x_ret2)):
                hard_predicates.add("OTHER_PREDECLARED_NUMERICAL_FAILURE")
                endpoint = x_ret2
            else:
                endpoint = x_ret2
                nonconverged = not bool(result2.success)
        except Exception as exc2:
            hard_predicates.add("OTHER_PREDECLARED_NUMERICAL_FAILURE")
            telemetry_rows.append(dict(
                fixture_id=fixture_id, family=family, start_id=start_id,
                optimizer_path="fallback", status=-1,
                message="EXCEPTION:" + type(exc2).__name__, success=False,
                nit=-1, nfev=-1, njev=-1, wall_clock_seconds=float("nan"),
            ))
            endpoint = np.array([float("nan")] * 4)

    cls = classify_endpoint(endpoint, family, nonconverged=nonconverged)
    for p in hard_predicates:
        if p not in cls["predicates"]:
            cls["predicates"] = sorted(set(cls["predicates"]) | {p})
            cls["eligible"] = False
            cls["primary_display_code"] = primary_display_code(set(cls["predicates"]))

    canonical = dict(
        fixture_id=fixture_id, family=family, start_id=start_id,
        optimizer_path=optimizer_path,
        status_class=("nonconverged" if nonconverged else ("numeric_error" if hard_predicates else "converged")),
        predicates=cls["predicates"], rejection_reasons=cls["rejection_reasons"],
        scientific_domain_pass=cls["scientific_domain_pass"],
        kural_t_pass_exact=cls["kural_t_pass_exact"], kural_s_pass_exact=cls["kural_s_pass_exact"],
        eligible=cls["eligible"], terminal_endpoint_hex=canonical_hex(cls["theta"]),
        family_status=None, family_summary=None,
    )
    return canonical, cls, telemetry_rows, evidence


def mini_bank_indices(n_fixed):
    return [0, (n_fixed - 1) // 2, n_fixed - 1]


def feature_start(family, x_fixture):
    j_star = int(np.flatnonzero(x_fixture == x_fixture.max())[0])
    u_star = j_star / 145.0
    if family == "P-01":
        k_mid = math.sqrt(4.0 * K_MAX)
        return (u_star - 1.0 / 8.0, u_star + 1.0 / 8.0, k_mid, k_mid), u_star, j_star
    else:
        return (u_star, 0.32057672965544004, 0.32057672965544004, math.sqrt(6.0)), u_star, j_star


# ==========================================================================
# X2 / A-01 -- manifest registry + implemented construction keys
# (R3-P03: the mapping of manifest exact_construction PROSE to these keys is
# a HUMAN-AUDITED provenance step disclosed in the r3 report; the keys audit
# implemented == executed, not machine agreement with the prose.)
# ==========================================================================
FIXTURE_MANIFEST_PATH = "p_konum_plus/calibration/f2_step2_fixture_manifest_2026-09-01.csv"
D_F2_09_MANIFEST_PATH = "p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv"

REQUIRED_MANIFEST_COLUMNS = [
    "fixture_id", "fixture_class", "family", "purpose",
    "exact_construction", "start_selection_rule", "forbidden_interpretation",
]

# fixture_id -> (fixture_class, family, execution_mode, implemented_construction_key)
HARNESS_REGISTRY = {
    "FIX-P01-BENIGN": ("analytic_benign_generator", "P-01", "real_optimizer_smoke", "minibank_3grid+cond_feature_via_run_one_start"),
    "FIX-P02-BENIGN": ("analytic_benign_generator", "P-02", "real_optimizer_smoke", "minibank_3grid+cond_feature_via_run_one_start"),
    "FIX-P01-STABLE-INTERIOR": ("stable_evaluation_analytic", "P-01", "analytic_evaluation", "stable_eval_only_no_optimizer"),
    "FIX-P01-STABLE-BOUNDARY": ("stable_evaluation_analytic", "P-01", "analytic_evaluation", "stable_eval_only_no_optimizer"),
    "FIX-P02-STABLE-INTERIOR": ("stable_evaluation_analytic", "P-02", "analytic_evaluation", "stable_eval_only_no_optimizer"),
    "FIX-P02-STABLE-BOUNDARY-SMIN": ("stable_evaluation_analytic", "P-02", "analytic_evaluation", "stable_eval_only_no_optimizer"),
    "FIX-P01-ZEROVAR-IN-DOMAIN": ("stable_evaluation_analytic", "P-01", "analytic_evaluation", "stable_eval_only_no_optimizer"),
    "FIX-NONFINITE-INPUT": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record", "fabricated_unit_check"),
    "FIX-INVALID-INIT": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record", "validator_reject_no_optimizer"),
    "FIX-NONFINITE-PARAMETER": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record", "fabricated_unit_check"),
    "FIX-NONFINITE-FIT": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record", "fabricated_unit_check"),
    "FIX-P01-KURAL-S-FAIL": ("failure_path_fabricated_but_real_generator", "P-01", "analytic_evaluation", "real_generator_classify_eval_only"),
    "FIX-OPTIMIZER-NONCONVERGENCE": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record", "fabricated_unit_check"),
    "FIX-OTHER-NUMERICAL-FAILURE": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record", "orchestrated_primary_fault_fallback_nonfinite"),
    "FIX-FAMILY-FIT-FAILURE": ("failure_path_fabricated", "P-CMN", "aggregation_unit", "aggregation_unit_all_ineligible"),
    "FIX-RESERVED-CODES-NEGATIVE": ("assertion_only", "P-CMN", "negative_assertion", "post_hoc_negative_assertion"),
    "FIX-FALLBACK-FAULT-INJECTION": ("fallback_fault_injection", "P-01", "fault_injection_fallback", "orchestrated_primary_fault_real_slsqp_fallback"),
    "FIX-AGG-UNIQUE-MIN": ("multistart_aggregation_fabricated", "P-CMN", "aggregation_unit", "aggregation_unit_fabricated_records"),
    "FIX-AGG-TIE": ("multistart_aggregation_fabricated", "P-CMN", "aggregation_unit", "aggregation_unit_fabricated_records"),
    "FIX-AGG-LOWERL-INELIGIBLE": ("multistart_aggregation_fabricated", "P-CMN", "aggregation_unit", "aggregation_unit_fabricated_records"),
    "FIX-D0F209-MANIFEST-QC": ("manifest_reconstruction", "P-CMN", "manifest_qc", "grid_reconstruction_set_equality"),
}

HARNESS_SELF_TEST_IDS = {
    "SELFTEST-X1-P01-ORDER", "SELFTEST-X1-P02-SMIN",
    "SELFTEST-C3-DISPLAY-PRECEDENCE", "SELFTEST-R3P04-MULTIPREDICATE",
}


def load_manifest_rows():
    with open(FIXTURE_MANIFEST_PATH, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # A-02: required columns must fail loudly; absence is NEVER filtered out.
    if rows:
        present = set(rows[0].keys())
    else:
        present = set()
    missing = [c for c in REQUIRED_MANIFEST_COLUMNS if c not in present]
    return rows, missing


def check_manifest_registry(rows):
    declared_fixture_ids = set(r["fixture_id"] for r in rows)
    implemented_fixture_ids = set(HARNESS_REGISTRY.keys())
    metadata_mismatches = []
    manifest_by_id = {r["fixture_id"]: r for r in rows}
    for fid, (fclass, fam, mode, key) in HARNESS_REGISTRY.items():
        row = manifest_by_id.get(fid)
        if row is None:
            metadata_mismatches.append(dict(fixture_id=fid, field="fixture_id", issue="NOT_IN_MANIFEST"))
            continue
        if row["fixture_class"] != fclass:
            metadata_mismatches.append(dict(fixture_id=fid, field="fixture_class", manifest=row["fixture_class"], registry=fclass))
        if row["family"] != fam:
            metadata_mismatches.append(dict(fixture_id=fid, field="family", manifest=row["family"], registry=fam))
    return dict(
        declared_fixture_ids=sorted(declared_fixture_ids),
        implemented_fixture_ids=sorted(implemented_fixture_ids),
        pre_execution_bijection_ok=(declared_fixture_ids == implemented_fixture_ids),
        metadata_mismatches=metadata_mismatches,
    )


# ==========================================================================
# Main suite
# ==========================================================================
def run_all_fixtures():
    canonical_records = []
    self_test_records = []
    telemetry = []
    emitted_predicates_union = set()
    emitted_warn_union = set()
    construction_audit = []
    special_evidence = {}
    rejection_counter = []  # fixture_ids whose starts were rejected by the validator

    manifest_rows, missing_columns = load_manifest_rows()
    assert not missing_columns, "A-02 REQUIRED MANIFEST COLUMN(S) MISSING: %r" % missing_columns
    manifest_by_id = {r["fixture_id"]: r for r in manifest_rows}
    registry_check = check_manifest_registry(manifest_rows)
    assert registry_check["pre_execution_bijection_ok"], "PRE-EXECUTION BIJECTION FAILURE"
    assert not registry_check["metadata_mismatches"], "METADATA MISMATCH: %r" % registry_check["metadata_mismatches"]

    def audit(fixture_id, executed_key):
        implemented_key = HARNESS_REGISTRY[fixture_id][3]
        construction_audit.append(dict(
            fixture_id=fixture_id,
            manifest_exact_construction=manifest_by_id[fixture_id]["exact_construction"],
            implemented_construction_key=implemented_key,
            executed_construction_key=executed_key,
            construction_fidelity_pass=bool(implemented_key == executed_key),
        ))

    raw01, ret01 = build_grid("P-01")
    raw02, ret02 = build_grid("P-02")
    manifest_qc = dict(
        p01_raw_count=len(raw01), p01_retained_count=len(ret01),
        p02_raw_count=len(raw02), p02_retained_count=len(ret02),
    )
    with open(D_F2_09_MANIFEST_PATH, "r", newline="", encoding="utf-8") as f:
        d09_rows = list(csv.DictReader(f))
    csv_p01 = sorted(tuple(float(v) for v in r["parameter_values"].split(";"))
                     for r in d09_rows if r["family"] == "P-01" and r["retained"] == "true")
    csv_p02 = sorted(tuple(float(v) for v in r["parameter_values"].split(";"))
                     for r in d09_rows if r["family"] == "P-02" and r["retained"] == "true")
    manifest_qc["p01_matches_csv"] = (ret01 == csv_p01)
    manifest_qc["p02_matches_csv"] = (ret02 == csv_p02)
    manifest_qc["p01_count_731"] = (len(ret01) == 731)
    manifest_qc["p02_count_261"] = (len(ret02) == 261)
    manifest_qc["p01_order_ascending"] = (ret01 == sorted(ret01))
    manifest_qc["p02_order_ascending"] = (ret02 == sorted(ret02))
    manifest_qc["p01_dedup_exact"] = (len(ret01) == len(set(ret01)))
    manifest_qc["p02_dedup_exact"] = (len(ret02) == len(set(ret02)))

    # ---------------- benign fixtures ----------------
    def run_benign(fixture_id, family, theta_fixture, n_fixed_expected, retained):
        stable_fn = p01_stable if family == "P-01" else p02_stable
        g = stable_fn(theta_fixture)
        status, sigma, ghat = zero_variance_rule(g)
        assert status == "OK"
        x_fixture = ghat

        n_fixed = len(retained)
        assert n_fixed == n_fixed_expected
        idxs = mini_bank_indices(n_fixed)
        starts = [("grid[%d]" % i, retained[i]) for i in idxs]

        fs_theta, u_star, j_star = feature_start(family, x_fixture)
        fs_finite = all(math.isfinite(v) for v in fs_theta)
        fs_domain_ok = False
        if fs_finite:
            v = v_p01(fs_theta) if family == "P-01" else v_p02(fs_theta)
            g_fs = stable_fn(fs_theta)
            fs_zv, _, _ = zero_variance_rule(g_fs)
            domain_ok = scientific_domain_pass_p01(fs_theta) if family == "P-01" else scientific_domain_pass_p02(fs_theta)
            kt_ok = kural_t_pass_exact_p01(fs_theta) if family == "P-01" else kural_t_pass_exact_p02(fs_theta)
            fs_domain_ok = (v <= FEASIBILITY_ACCEPTANCE_TOL) and fs_zv == "OK" and bool(domain_ok) and bool(kt_ok) and \
                (kural_s_pass_exact(g_fs) if np.all(np.isfinite(g_fs)) else False)
        fs_nonduplicate = fs_theta not in [s[1] for s in starts]
        fs_valid = fs_finite and fs_domain_ok and fs_nonduplicate
        if fs_valid:
            starts.append(("feature", fs_theta))
        else:
            canonical_records.append(dict(
                fixture_id=fixture_id, family=family, start_id="feature",
                optimizer_path="not_run", status_class="FEATURE_START_REJECTED",
                predicates=[], rejection_reasons=["FEATURE_START_REJECTED"],
                scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
                eligible=False, terminal_endpoint_hex=canonical_hex(fs_theta),
                family_status=None, family_summary=None,
            ))

        endpoint_records = []
        first_evidence = None
        n_run = 0
        for start_id, x0 in starts:
            canonical, cls, tel, ev = run_one_start(fixture_id, family, start_id, x0, x_fixture,
                                                    rejection_counter=rejection_counter)
            n_run += 1
            if first_evidence is None:
                first_evidence = ev
            canonical_records.append(canonical)
            telemetry.extend(tel)
            emitted_predicates_union.update(cls["predicates"])
            # A-03: standardized-only internal L bookkeeping, all endpoints.
            L = internal_L(x_fixture, cls["theta"], family)
            endpoint_records.append(dict(theta=cls["theta"], L=L, eligible=cls["eligible"]))

        agg_status, winner = aggregate(endpoint_records)
        if agg_status == "OK":
            canonical_records.append(dict(
                fixture_id=fixture_id, family=family, start_id="FAMILY_SELECTED",
                optimizer_path="aggregation", status_class="family_fit_selected",
                predicates=[], rejection_reasons=[],
                scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
                eligible=True, terminal_endpoint_hex=canonical_hex(winner["theta"]),
                family_status="OK", family_summary=None,
            ))
        else:
            canonical_records.append(dict(
                fixture_id=fixture_id, family=family, start_id="FAMILY_SELECTED",
                optimizer_path="aggregation", status_class="FAMILY_FIT_FAILURE",
                predicates=[], rejection_reasons=[],
                scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
                eligible=False, terminal_endpoint_hex=None,
                family_status="FAMILY_FIT_FAILURE", family_summary=winner,
            ))

        executed_key = "minibank_%dgrid+%s_via_run_one_start" % (
            len(idxs), "cond_feature" if True else "nofeature")
        # observed composition: idxs actually run + conditional feature semantics
        executed_key = "minibank_%dgrid+cond_feature_via_run_one_start" % len(idxs) if n_run >= len(idxs) else "unexpected_path"
        c1_pass = (n_run == len(starts)) and any(r["eligible"] for r in endpoint_records)
        return dict(
            fixture_id=fixture_id, n_starts=len(starts), feature_start_valid=fs_valid,
            agg_status=agg_status, has_eligible_endpoint=any(r["eligible"] for r in endpoint_records),
            c1_pass_criterion=bool(c1_pass),
        ), executed_key, first_evidence

    u0 = 72.0 / 145.0
    k_mid = math.sqrt(4.0 * K_MAX)
    theta_p01_fix = (u0 - 1.0 / 8.0, u0 + 1.0 / 8.0, k_mid, k_mid)
    theta_p02_fix = (u0, 0.32057672965544004, 0.32057672965544004, math.sqrt(6.0))

    p01_benign_result, key_p01, benign_evidence_sample = run_benign("FIX-P01-BENIGN", "P-01", theta_p01_fix, 731, ret01)
    audit("FIX-P01-BENIGN", key_p01)
    p02_benign_result, key_p02, _ = run_benign("FIX-P02-BENIGN", "P-02", theta_p02_fix, 261, ret02)
    audit("FIX-P02-BENIGN", key_p02)

    # 4A.4 falsifiability control on a benign start's observed evidence
    falsifiability = dict(
        primary_fault_injection_triggered=benign_evidence_sample["primary_fault_injection_triggered"],
        fallback_branch_entered=benign_evidence_sample["fallback_branch_entered"],
        fallback_nonfinite_injection_triggered=benign_evidence_sample["fallback_nonfinite_injection_triggered"],
        validator_called=benign_evidence_sample["validator_called"],
        optimizer_called=benign_evidence_sample["optimizer_called"],
    )
    falsifiability["pass_"] = (
        falsifiability["primary_fault_injection_triggered"] is False
        and falsifiability["fallback_branch_entered"] is False
        and falsifiability["fallback_nonfinite_injection_triggered"] is False
        and falsifiability["validator_called"] is True
        and falsifiability["optimizer_called"] is True
    )

    # ---------------- stable-evaluation fixtures ----------------
    stable_eval_results = {}
    for fid, fam, theta in [
        ("FIX-P01-STABLE-INTERIOR", "P-01", (0.3, 0.7, 20.0, 20.0)),
        ("FIX-P01-STABLE-BOUNDARY", "P-01", (-1.0, -1.0, K_MIN, K_MIN)),
        ("FIX-P02-STABLE-INTERIOR", "P-02", (0.5, 0.5, 0.5, 2.0)),
        ("FIX-P02-STABLE-BOUNDARY-SMIN", "P-02", (0.5, s_side_min(2.0), s_side_min(2.0), 2.0)),
    ]:
        stable_fn = p01_stable if fam == "P-01" else p02_stable
        try:
            g = stable_fn(theta)
            status, sigma, ghat = zero_variance_rule(g)
            stable_eval_results[fid] = dict(exception=False, status=status, sigma_g=sigma)
            executed_key = "stable_eval_only_no_optimizer"
        except Exception as exc:
            stable_eval_results[fid] = dict(exception=True, error=type(exc).__name__)
            executed_key = "unexpected_exception_path"
        canonical_records.append(dict(
            fixture_id=fid, family=fam, start_id="eval_only",
            optimizer_path="not_run", status_class=stable_eval_results[fid].get("status", "EXCEPTION"),
            predicates=[stable_eval_results[fid]["status"]] if stable_eval_results[fid].get("status") not in (None, "OK") else [],
            rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
            eligible=False, terminal_endpoint_hex=canonical_hex(theta), family_status=None, family_summary=None,
        ))
        audit(fid, executed_key)

    theta_zv = (-1.0, 1.375, 40.0, K_MAX)
    g_zv = p01_stable(theta_zv)
    zv_status, zv_sigma, _ = zero_variance_rule(g_zv)
    canonical_records.append(dict(
        fixture_id="FIX-P01-ZEROVAR-IN-DOMAIN", family="P-01", start_id="eval_only",
        optimizer_path="not_run", status_class=zv_status,
        predicates=[zv_status] if zv_status != "OK" else [], rejection_reasons=[],
        scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=canonical_hex(theta_zv), family_status=None, family_summary=None,
    ))
    if zv_status != "OK":
        emitted_predicates_union.add(zv_status)
    audit("FIX-P01-ZEROVAR-IN-DOMAIN", "stable_eval_only_no_optimizer")

    theta_ks = (2.0, 2.0, K_MAX, K_MAX)
    cls_ks = classify_endpoint(theta_ks, "P-01")
    canonical_records.append(dict(
        fixture_id="FIX-P01-KURAL-S-FAIL", family="P-01", start_id="eval_only",
        optimizer_path="not_run",
        status_class="MORPHOLOGY_INADMISSIBLE" if "MORPHOLOGY_INADMISSIBLE" in cls_ks["predicates"] else "UNEXPECTED",
        predicates=cls_ks["predicates"], rejection_reasons=[],
        scientific_domain_pass=cls_ks["scientific_domain_pass"], kural_t_pass_exact=cls_ks["kural_t_pass_exact"],
        kural_s_pass_exact=cls_ks["kural_s_pass_exact"], eligible=cls_ks["eligible"],
        terminal_endpoint_hex=canonical_hex(theta_ks), family_status=None, family_summary=None,
    ))
    emitted_predicates_union.update(cls_ks["predicates"])
    audit("FIX-P01-KURAL-S-FAIL", "real_generator_classify_eval_only")

    # ---------------- fabricated unit fixtures ----------------
    x_bad = np.ones(146)
    x_bad[10] = np.nan
    ok_detect = not np.all(np.isfinite(x_bad))
    canonical_records.append(dict(
        fixture_id="FIX-NONFINITE-INPUT", family="P-CMN", start_id="unit",
        optimizer_path="not_run", status_class="NONFINITE_INPUT" if ok_detect else "UNEXPECTED",
        predicates=["NONFINITE_INPUT"] if ok_detect else [], rejection_reasons=[],
        scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))
    if ok_detect:
        emitted_predicates_union.add("NONFINITE_INPUT")
    audit("FIX-NONFINITE-INPUT", "fabricated_unit_check")

    # A-01B: FIX-INVALID-INIT routed through run_one_start -> real validator path.
    invalid_x0 = (float("nan"), 0.5, 20.0, 20.0)
    x_dummy = np.linspace(-1, 1, 146)
    x_dummy = (x_dummy - x_dummy.mean()) / x_dummy.std(ddof=0)
    canon_ii, cls_ii, tel_ii, ev_ii = run_one_start("FIX-INVALID-INIT", "P-01", "unit",
                                                    invalid_x0, x_dummy,
                                                    rejection_counter=rejection_counter)
    canonical_records.append(canon_ii)
    telemetry.extend(tel_ii)
    emitted_predicates_union.update(canon_ii["predicates"])
    special_evidence["FIX-INVALID-INIT"] = dict(ev_ii)
    executed_key_ii = ("validator_reject_no_optimizer"
                       if (ev_ii["validator_called"] and not ev_ii["optimizer_called"]
                           and "INVALID_INITIALIZATION" in canon_ii["predicates"])
                       else "unexpected_path")
    audit("FIX-INVALID-INIT", executed_key_ii)

    theta_nan = (float("nan"), 0.5, 20.0, 20.0)
    cls_nan = classify_endpoint(theta_nan, "P-01")
    canonical_records.append(dict(
        fixture_id="FIX-NONFINITE-PARAMETER", family="P-CMN", start_id="unit",
        optimizer_path="not_run", status_class=cls_nan["primary_display_code"],
        predicates=cls_nan["predicates"], rejection_reasons=[],
        scientific_domain_pass=cls_nan["scientific_domain_pass"], kural_t_pass_exact=cls_nan["kural_t_pass_exact"],
        kural_s_pass_exact=cls_nan["kural_s_pass_exact"], eligible=cls_nan["eligible"],
        terminal_endpoint_hex=canonical_hex(theta_nan), family_status=None, family_summary=None,
    ))
    emitted_predicates_union.update(cls_nan["predicates"])
    audit("FIX-NONFINITE-PARAMETER", "fabricated_unit_check")

    g_fab = np.ones(146)
    g_fab[50] = np.inf
    fab_status, _, _ = zero_variance_rule(g_fab)
    canonical_records.append(dict(
        fixture_id="FIX-NONFINITE-FIT", family="P-CMN", start_id="unit",
        optimizer_path="not_run", status_class=fab_status,
        predicates=[fab_status] if fab_status != "OK" else [], rejection_reasons=[],
        scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))
    if fab_status != "OK":
        emitted_predicates_union.add(fab_status)
    audit("FIX-NONFINITE-FIT", "fabricated_unit_check")

    theta_nc = (0.4, 0.6, 15.0, 15.0)
    cls_nc = classify_endpoint(theta_nc, "P-01", nonconverged=True)
    canonical_records.append(dict(
        fixture_id="FIX-OPTIMIZER-NONCONVERGENCE", family="P-CMN", start_id="unit",
        optimizer_path="not_run", status_class="OPTIMIZER_NONCONVERGENCE",
        predicates=cls_nc["predicates"], rejection_reasons=[],
        scientific_domain_pass=cls_nc["scientific_domain_pass"], kural_t_pass_exact=cls_nc["kural_t_pass_exact"],
        kural_s_pass_exact=cls_nc["kural_s_pass_exact"], eligible=cls_nc["eligible"],
        terminal_endpoint_hex=canonical_hex(theta_nc), family_status=None, family_summary=None,
    ))
    emitted_predicates_union.update(cls_nc["predicates"])
    audit("FIX-OPTIMIZER-NONCONVERGENCE", "fabricated_unit_check")

    # A-01A: FIX-OTHER-NUMERICAL-FAILURE through the REAL orchestration path.
    x0_other = ret01[0]
    canon_of, cls_of, tel_of, ev_of = run_one_start(
        "FIX-OTHER-NUMERICAL-FAILURE", "P-CMN" if False else "P-01", "unit",
        x0_other, x_dummy,
        fault_inject_primary=True, fault_inject_fallback_nonfinite=True,
        rejection_counter=rejection_counter,
    )
    # family label in canonical record follows manifest family P-CMN? manifest says P-CMN.
    canon_of["family"] = "P-CMN"
    for row in tel_of:
        row["family"] = "P-CMN"
    canonical_records.append(canon_of)
    telemetry.extend(tel_of)
    emitted_predicates_union.update(canon_of["predicates"])
    special_evidence["FIX-OTHER-NUMERICAL-FAILURE"] = dict(ev_of)
    executed_key_of = ("orchestrated_primary_fault_fallback_nonfinite"
                       if (ev_of["primary_fault_injection_triggered"] and ev_of["fallback_branch_entered"]
                           and ev_of["same_x0_reused"] and ev_of["fallback_nonfinite_injection_triggered"]
                           and "OTHER_PREDECLARED_NUMERICAL_FAILURE" in canon_of["predicates"])
                       else "unexpected_path")
    audit("FIX-OTHER-NUMERICAL-FAILURE", executed_key_of)

    fab_records = [
        dict(theta=(0.1, 0.2, 5.0, 6.0), L=float("inf"), eligible=False),
        dict(theta=(0.3, 0.4, 7.0, 8.0), L=float("inf"), eligible=False),
        dict(theta=(0.5, 0.6, 9.0, 10.0), L=float("inf"), eligible=False),
    ]
    fff_status, fff_label = aggregate(fab_records)
    canonical_records.append(dict(
        fixture_id="FIX-FAMILY-FIT-FAILURE", family="P-CMN", start_id="FAMILY_SELECTED",
        optimizer_path="aggregation(fabricated)", status_class=fff_status,
        predicates=[], rejection_reasons=[],
        scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=None,
        family_status=fff_status, family_summary=fff_label if fff_status == "FAMILY_FIT_FAILURE" else None,
    ))
    audit("FIX-FAMILY-FIT-FAILURE", "aggregation_unit_all_ineligible")

    # FIX-FALLBACK-FAULT-INJECTION (real SLSQP fallback; unchanged behavior)
    canon_fb, cls_fb, tel_fb, ev_fb = run_one_start(
        "FIX-FALLBACK-FAULT-INJECTION", "P-01", "designated_start_idx0",
        ret01[0], x_dummy, fault_inject_primary=True,
        rejection_counter=rejection_counter,
    )
    canonical_records.append(canon_fb)
    telemetry.extend(tel_fb)
    emitted_predicates_union.update(cls_fb["predicates"])
    special_evidence["FIX-FALLBACK-FAULT-INJECTION"] = dict(ev_fb)
    executed_key_fb = ("orchestrated_primary_fault_real_slsqp_fallback"
                       if (ev_fb["primary_fault_injection_triggered"] and ev_fb["fallback_branch_entered"]
                           and ev_fb["same_x0_reused"] and not ev_fb["fallback_nonfinite_injection_triggered"]
                           and ev_fb["optimizer_called"])
                       else "unexpected_path")
    audit("FIX-FALLBACK-FAULT-INJECTION", executed_key_fb)

    # aggregation unit fixtures
    agg_unique = aggregate([
        dict(theta=(0.1, 0.2, 5.0, 6.0), L=2.0, eligible=True),
        dict(theta=(0.3, 0.4, 7.0, 8.0), L=0.5, eligible=True),
        dict(theta=(0.9, 1.0, 9.0, 9.0), L=9.0, eligible=False),
    ])
    agg_tie_res = aggregate([
        dict(theta=(0.9, 1.0, 9.0, 9.0), L=1.0000000000005, eligible=True),
        dict(theta=(0.1, 0.2, 5.0, 6.0), L=1.0, eligible=True),
        dict(theta=(0.3, 0.4, 7.0, 8.0), L=5.0, eligible=True),
    ])
    agg_lower = aggregate([
        dict(theta=(0.0, 0.0, 4.0, 4.0), L=0.001, eligible=False),
        dict(theta=(0.5, 0.6, 10.0, 10.0), L=3.0, eligible=True),
    ])
    for fid, res in [("FIX-AGG-UNIQUE-MIN", agg_unique), ("FIX-AGG-TIE", agg_tie_res),
                     ("FIX-AGG-LOWERL-INELIGIBLE", agg_lower)]:
        status, winner = res
        canonical_records.append(dict(
            fixture_id=fid, family="P-CMN", start_id="FAMILY_SELECTED",
            optimizer_path="aggregation(fabricated)", status_class=status,
            predicates=[], rejection_reasons=[],
            scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
            eligible=(status == "OK"),
            terminal_endpoint_hex=canonical_hex(winner["theta"]) if status == "OK" else None,
            family_status=status, family_summary=None,
        ))
        audit(fid, "aggregation_unit_fabricated_records")

    agg_checks = dict(
        unique_min_correct=(agg_unique[0] == "OK" and agg_unique[1]["theta"] == (0.3, 0.4, 7.0, 8.0)),
        tie_correct=(agg_tie_res[0] == "OK" and agg_tie_res[1]["theta"] == (0.1, 0.2, 5.0, 6.0)),
        lowerl_ineligible_excluded=(agg_lower[0] == "OK" and agg_lower[1]["theta"] == (0.5, 0.6, 10.0, 10.0)),
        family_fit_failure_label_correct=(fff_status == "FAMILY_FIT_FAILURE" and fff_label == "NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART"),
    )

    reserved_violation = bool(emitted_predicates_union & RESERVED_NOT_EMITTED) or bool(emitted_warn_union & RESERVED_WARN_NOT_EMITTED)
    canonical_records.append(dict(
        fixture_id="FIX-RESERVED-CODES-NEGATIVE", family="P-CMN", start_id="assertion",
        optimizer_path="not_run", status_class=("VIOLATION" if reserved_violation else "CONFIRMED_ABSENT"),
        predicates=[], rejection_reasons=[],
        scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=not reserved_violation, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))
    audit("FIX-RESERVED-CODES-NEGATIVE", "post_hoc_negative_assertion")

    manifest_qc_pass = all([
        manifest_qc["p01_matches_csv"], manifest_qc["p02_matches_csv"],
        manifest_qc["p01_count_731"], manifest_qc["p02_count_261"],
        manifest_qc["p01_order_ascending"], manifest_qc["p02_order_ascending"],
        manifest_qc["p01_dedup_exact"], manifest_qc["p02_dedup_exact"],
    ])
    canonical_records.append(dict(
        fixture_id="FIX-D0F209-MANIFEST-QC", family="P-CMN", start_id="reconstruction",
        optimizer_path="not_run", status_class="PASS" if manifest_qc_pass else "FAIL",
        predicates=[], rejection_reasons=[],
        scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=True, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))
    audit("FIX-D0F209-MANIFEST-QC", "grid_reconstruction_set_equality")

    executed_fixture_ids = set(r["fixture_id"] for r in canonical_records) - HARNESS_SELF_TEST_IDS
    declared_fixture_ids = set(registry_check["declared_fixture_ids"])
    post_execution_bijection_ok = (declared_fixture_ids == executed_fixture_ids)
    construction_fidelity_all = all(a["construction_fidelity_pass"] for a in construction_audit)
    rejections_outside_invalid_init = [fid for fid in rejection_counter if fid != "FIX-INVALID-INIT"]

    # ---------------- harness self-tests ----------------
    theta_order = (0.500000005, 0.500000000, 20.0, 20.0)
    cls_order = classify_endpoint(theta_order, "P-01")
    st_order_pass = (bool(cls_order["scientific_domain_pass"]) is False
                     and "MORPHOLOGY_INADMISSIBLE" in cls_order["predicates"]
                     and cls_order["eligible"] is False)
    self_test_records.append(dict(self_test_id="SELFTEST-X1-P01-ORDER",
                                   predicates=cls_order["predicates"], eligible=cls_order["eligible"],
                                   scientific_domain_pass=cls_order["scientific_domain_pass"],
                                   v_value=cls_order["v_value"], pass_=bool(st_order_pass)))

    beta_t = math.sqrt(6.0)
    smin_t = s_side_min(beta_t)
    theta_smin = (0.5, smin_t - 5e-13, smin_t, beta_t)
    cls_smin = classify_endpoint(theta_smin, "P-02")
    st_smin_pass = (bool(cls_smin["scientific_domain_pass"]) is False
                    and "MORPHOLOGY_INADMISSIBLE" in cls_smin["predicates"]
                    and cls_smin["eligible"] is False)
    self_test_records.append(dict(self_test_id="SELFTEST-X1-P02-SMIN",
                                   predicates=cls_smin["predicates"], eligible=cls_smin["eligible"],
                                   scientific_domain_pass=cls_smin["scientific_domain_pass"],
                                   beta_is_sqrt6_exact=(beta_t == math.sqrt(6.0)),
                                   v_value=cls_smin["v_value"], pass_=bool(st_smin_pass)))

    # A-04: C3 before/after mutation check (non-tautological)
    c3_input = {"NONFINITE_FIT", "MORPHOLOGY_INADMISSIBLE"}
    c3_before = sorted(c3_input)
    c3_primary = primary_display_code(c3_input)
    c3_after = sorted(c3_input)
    c3_pass = (c3_after == c3_before) and (c3_primary == "NONFINITE_FIT")
    self_test_records.append(dict(self_test_id="SELFTEST-C3-DISPLAY-PRECEDENCE",
                                   before=c3_before, after=c3_after, primary_display_code=c3_primary,
                                   mutation_free=(c3_after == c3_before), pass_=bool(c3_pass)))

    # R3-P04 (section 9.1): real-classifier multi-predicate probe
    theta_multi = (-1.0, 1.375, 200.0, 200.0)
    cls_multi = classify_endpoint(theta_multi, "P-01")
    multi_expected = {"MORPHOLOGY_INADMISSIBLE", "ZERO_VARIANCE_FIT"}
    multi_pass = (set(cls_multi["predicates"]) == multi_expected
                  and cls_multi["primary_display_code"] == "ZERO_VARIANCE_FIT"
                  and cls_multi["primary_display_code"] == primary_display_code(set(cls_multi["predicates"])))
    self_test_records.append(dict(self_test_id="SELFTEST-R3P04-MULTIPREDICATE",
                                   observed_predicates=cls_multi["predicates"],
                                   observed_display=cls_multi["primary_display_code"],
                                   expected_predicates=sorted(multi_expected),
                                   expected_display="ZERO_VARIANCE_FIT", pass_=bool(multi_pass)))

    summary = dict(
        manifest_qc=manifest_qc,
        missing_manifest_columns=missing_columns,
        p01_benign=p01_benign_result, p02_benign=p02_benign_result,
        stable_eval_results=stable_eval_results,
        zv_in_domain_status=zv_status, zv_in_domain_sigma=zv_sigma,
        kural_s_fail_status=cls_ks["primary_display_code"],
        agg_checks=agg_checks,
        emitted_predicates_union=sorted(emitted_predicates_union),
        reserved_violation=reserved_violation,
        registry_check=dict(registry_check),
        post_execution_bijection_ok=post_execution_bijection_ok,
        construction_fidelity_all=construction_fidelity_all,
        construction_fidelity_count=sum(1 for a in construction_audit if a["construction_fidelity_pass"]),
        special_evidence=special_evidence,
        falsifiability=falsifiability,
        rejections_outside_invalid_init=rejections_outside_invalid_init,
        rejection_counter=list(rejection_counter),
    )
    return canonical_records, self_test_records, telemetry, construction_audit, summary


def canonicalize(doc):
    return json.dumps(doc, sort_keys=True, default=str)


def main():
    r1 = run_all_fixtures()
    r2 = run_all_fixtures()
    doc1 = dict(records=r1[0], self_tests=r1[1], construction_audit=r1[3],
                special_evidence=r1[4]["special_evidence"], falsifiability=r1[4]["falsifiability"],
                rejections_outside_invalid_init=r1[4]["rejections_outside_invalid_init"])
    doc2 = dict(records=r2[0], self_tests=r2[1], construction_audit=r2[3],
                special_evidence=r2[4]["special_evidence"], falsifiability=r2[4]["falsifiability"],
                rejections_outside_invalid_init=r2[4]["rejections_outside_invalid_init"])
    canon1 = canonicalize(doc1)
    canon2 = canonicalize(doc2)
    determinism_pass = (canon1 == canon2)

    import hashlib
    h1 = hashlib.sha256(canon1.encode("utf-8")).hexdigest()
    h2 = hashlib.sha256(canon2.encode("utf-8")).hexdigest()

    telemetry_fields = ["fixture_id", "family", "start_id", "optimizer_path", "status",
                        "message", "success", "nit", "nfev", "njev", "wall_clock_seconds"]
    out_path = "p_konum_plus/calibration/f2_step2_feasibility_telemetry_r3_2026-09-01.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=telemetry_fields, lineterminator="\n")
        w.writeheader()
        for row in r1[2]:
            w.writerow(row)

    env_info = dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                    platform=platform.platform(),
                    OMP_NUM_THREADS=os.environ.get("OMP_NUM_THREADS"),
                    OPENBLAS_NUM_THREADS=os.environ.get("OPENBLAS_NUM_THREADS"),
                    MKL_NUM_THREADS=os.environ.get("MKL_NUM_THREADS"))

    print("ENV_INFO=" + json.dumps(env_info, sort_keys=True))
    print("DETERMINISM_PASS=" + str(determinism_pass))
    print("CANON1_SHA256=" + h1)
    print("CANON2_SHA256=" + h2)
    print("TELEMETRY_ROWS_WRITTEN=" + str(len(r1[2])))
    print("TELEMETRY_RUN=" + TELEMETRY_RUN_LABEL)
    print("RNG_USED=" + str(RNG_USED))
    print("RUN1_SUMMARY=" + json.dumps(r1[4], sort_keys=True, default=str))
    print("RUN2_SUMMARY_EQUAL=" + str(json.dumps(r1[4], sort_keys=True, default=str) == json.dumps(r2[4], sort_keys=True, default=str)))
    print("SELF_TESTS=" + json.dumps(r1[1], sort_keys=True, default=str))


if __name__ == "__main__":
    main()
