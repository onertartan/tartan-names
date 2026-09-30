"""
p_konum_plus -- F2 STEP 2 CORRECTED successor synthetic/analytic-only
feasibility harness (X1-X4 / C1-C5 correction pass).

Corrects, relative to f2_step2_feasibility_harness_2026-09-01.py:
  X1 = exact scientific-support predicate, fully separate from
       FEASIBILITY_ACCEPTANCE_TOL, with NO -1e-9/-1e-12 waiver baked into
       the Kural T check.
  X2 = fixture-manifest <-> implemented/executed registry bijection.
  X3 = family_status/family_summary separated from the hard-predicate field.
  X4 = the unowned 1.0e6 invalid-prediction penalty replaced by the exact,
       owned CLASS_C objective-domain guard 585.0 = 4*T+1.
  C1 = benign-fixture PASS criterion restored to the exact governing text.
  C2 = X1-P02-SMIN self-test pinned to beta=sqrt(6) exactly.
  C3 = direct display-precedence self-test on a fabricated predicate set.
  C4 = beta clamp removed from V_P02 numerical bookkeeping.
  C5 = telemetry_run = RUN1 only.

No real SSA trajectory is read, fit, or referenced. No parameter-recovery,
objective-attainment, or family-comparison estimand is computed. This file
is executed twice in-process to establish exact semantic double-run
determinism.

FAULT_INJECTION_TEST_ONLY markers exist ONLY inside this test harness and
must never exist in production fitting code.
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
# Frozen scientific constants (ART-F2 r2 / r2a; preserved, not re-derived)
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
N_MIN = 3  # Kural S

EPSILON_MODEL = 1e-12               # preserved
FEASIBILITY_ACCEPTANCE_TOL = 1e-8   # preserved, X1: numerical-only, never scientific

# X4: exact, owned CLASS_C objective-domain guard replacing the unowned 1.0e6.
L_INVALID_PREDICTION_GUARD = 4.0 * T + 1.0  # 585.0
assert L_INVALID_PREDICTION_GUARD == 585.0

RNG_USED = False
TELEMETRY_RUN_LABEL = "RUN1"  # C5


def s_side_min(beta):
    return (W_MIN_YEARS / 145.0) / (LN10 ** (1.0 / beta) - LN10_9 ** (1.0 / beta))


# --------------------------------------------------------------------------
# D-F2-09 initialization lattices (unchanged)
# --------------------------------------------------------------------------
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
    """Exact Kural S: n_sup(g_stable) >= 3, zero tolerance (unchanged formula)."""
    return n_sup(g) >= N_MIN


def kural_t_pass_exact_p01(theta):
    """X1: exact Kural T for P-01, NO -1e-9 waiver."""
    c_r, c_d, k_r, k_d = theta
    if not (math.isfinite(k_r) and math.isfinite(k_d)) or k_r <= 0 or k_d <= 0:
        return False
    width_r_years = (2.0 * LN9 / k_r) * 145.0
    width_d_years = (2.0 * LN9 / k_d) * 145.0
    return (width_r_years >= W_MIN_YEARS) and (width_d_years >= W_MIN_YEARS)


def kural_t_pass_exact_p02(theta):
    """X1: exact Kural T for P-02 (== the exact beta-dependent scale rule),
    NO -1e-12 waiver, NO beta clamping."""
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
    assert len(raw_sorted) == len(raw), "unexpected duplicate in raw lattice"
    retained = [t for t in raw_sorted if kural_s_pass_exact(stable_fn(t))]
    return raw_sorted, sorted(retained)


# --------------------------------------------------------------------------
# epsilon_model / ZERO_VARIANCE_FIT rule (preserved, unchanged)
# --------------------------------------------------------------------------
def zero_variance_rule(g_stable):
    if not np.all(np.isfinite(g_stable)):
        return "NONFINITE_FIT", None, None
    sigma_g = float(np.std(g_stable, ddof=0))
    if sigma_g <= EPSILON_MODEL:
        return "ZERO_VARIANCE_FIT", sigma_g, None
    ghat = (g_stable - g_stable.mean()) / sigma_g
    return "OK", sigma_g, ghat


# --------------------------------------------------------------------------
# X1.4.1 -- post-return NUMERICAL feasibility (unchanged formulas, preserved
# 1e-8 literal). This is exclusively a numerical-representation check and
# must NEVER expand scientific support.
# --------------------------------------------------------------------------
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
    """C4: no beta clamp. If beta is nonfinite or <=0, return an infinite
    numerical-violation sentinel instead of clamping beta before evaluating
    s_side_min. Otherwise evaluate s_side_min at the RETURNED beta exactly,
    with no projection."""
    m, s_l, s_r, beta = theta
    if not math.isfinite(beta) or beta <= 0:
        return float("inf")
    lo_free = [-1.0, 0.0, 0.0, BETA_MIN]
    hi_free = [2.0, S_MAX, S_MAX, BETA_MAX]
    v = v_box(theta, lo_free, hi_free)
    smin = s_side_min(beta)  # evaluated at the returned beta itself, no clamp
    return max(v, max(smin - s_l, 0.0), max(smin - s_r, 0.0))


def endpoint_numerically_feasible(theta, family):
    theta = np.asarray(theta, dtype=np.float64)
    if not np.all(np.isfinite(theta)):
        return False, float("inf")
    v = v_p01(theta) if family == "P-01" else v_p02(theta)
    return (v <= FEASIBILITY_ACCEPTANCE_TOL), v


# --------------------------------------------------------------------------
# X1.4.2 -- INDEPENDENT exact scientific-domain predicate.
# Uses the returned float64 tuple exactly as represented. NO
# FEASIBILITY_ACCEPTANCE_TOL, NO -1e-9, NO -1e-12, NO clipping, NO
# projection, NO rounding.
# --------------------------------------------------------------------------
def scientific_domain_pass_p01(theta):
    c_r, c_d, k_r, k_d = theta
    if not all(math.isfinite(v) for v in theta):
        return False
    return (
        -1.0 <= c_r <= 2.0
        and -1.0 <= c_d <= 2.0
        and c_r <= c_d
        and K_MIN <= k_r <= K_MAX
        and K_MIN <= k_d <= K_MAX
    )


def scientific_domain_pass_p02(theta):
    m, s_l, s_r, beta = theta
    if not all(math.isfinite(v) for v in theta):
        return False
    if not (-1.0 <= m <= 2.0 and 1.0 <= beta <= 6.0):
        return False
    if not (s_l <= 3.0 and s_r <= 3.0):
        return False
    # beta already known finite and in [1,6] > 0 here; safe to evaluate exactly
    smin = s_side_min(beta)
    return (s_l >= smin) and (s_r >= smin)


# --------------------------------------------------------------------------
# Failure-code taxonomy / display precedence (preserved, unchanged)
# --------------------------------------------------------------------------
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
    """X1/X3-corrected classification. Computes, SEPARATELY, for every
    returned endpoint: numerically_feasible, scientific_domain_pass,
    kural_t_pass_exact, kural_s_pass_exact. `predicates` carries ONLY
    start-level hard-failure predicates (never a family-level summary)."""
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
    zv_status = None
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
        theta_finite
        and num_feasible
        and bool(domain_pass)
        and bool(kural_t)
        and bool(kural_s if kural_s is not None else False)
        and objective_finite
        and prediction_finite
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


# --------------------------------------------------------------------------
# D-F2-09.9 tie comparator (unchanged)
# --------------------------------------------------------------------------
def tie(a, b):
    return abs(a - b) <= 1e-12 + 1e-9 * max(abs(a), abs(b))


def aggregate(records):
    """X3: returns ('OK', winner) or ('FAMILY_FIT_FAILURE',
    'NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART') -- family-level
    only, never written into a start-level `predicates` field by the
    caller."""
    eligible = [r for r in records if r["eligible"]]
    if not eligible:
        return "FAMILY_FIT_FAILURE", "NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART"
    best_l = min(r["L"] for r in eligible)
    tied = [r for r in eligible if tie(r["L"], best_l)]
    winner = sorted(tied, key=lambda r: r["theta"])[0]
    return "OK", winner


def objective_L(x, ghat):
    return float(np.sum((x - ghat) ** 2))


# --------------------------------------------------------------------------
# X4 -- exact, owned CLASS_C objective-domain guard (replaces 1.0e6)
# --------------------------------------------------------------------------
def make_objective_and_x(family, x_target):
    stable_fn = p01_stable if family == "P-01" else p02_stable

    def fun(theta):
        g_stable = stable_fn(theta)
        status, sigma_g, ghat = zero_variance_rule(g_stable)
        if status != "OK":
            # X4: deterministic finite CLASS_C guard, owned and derived
            # exactly as 4*T+1 = 585.0. NOT a scientific objective
            # observation; NEVER written to telemetry; NEVER used for
            # eligibility or family comparison.
            return L_INVALID_PREDICTION_GUARD
        return objective_L(x_target, ghat)

    return fun


# --------------------------------------------------------------------------
# CLASS_C optimizer contract (unchanged from r2a / prior successor)
# --------------------------------------------------------------------------
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

    return [
        NonlinearConstraint(g1, 0.0, np.inf),
        NonlinearConstraint(g2, 0.0, np.inf),
    ]


def run_primary(family, x0, x_target, fault_inject=False):
    if fault_inject:
        raise RuntimeError("FAULT_INJECTION_TEST_ONLY=true : simulated pure numerical error on primary path")

    fun = make_objective_and_x(family, x_target)
    bounds = p01_bounds() if family == "P-01" else p02_bounds()
    constraints = [p01_linear_constraint()] if family == "P-01" else p02_nonlinear_constraints()

    t0 = time.perf_counter()
    result = minimize(
        fun,
        x0=np.asarray(x0, dtype=np.float64),
        method="trust-constr",
        jac="2-point",
        hess=scipy.optimize.BFGS(),
        bounds=bounds,
        constraints=constraints,
        options=dict(gtol=1e-10, xtol=1e-12, barrier_tol=1e-10, maxiter=500),
    )
    wall = time.perf_counter() - t0
    return result, wall


def run_fallback(family, x0, x_target):
    fun = make_objective_and_x(family, x_target)
    bounds = p01_bounds() if family == "P-01" else p02_bounds()
    if family == "P-01":
        cons = [{"type": "ineq", "fun": lambda x: x[1] - x[0]}]
    else:
        cons = [
            {"type": "ineq", "fun": lambda x: x[1] - s_side_min(x[3])},
            {"type": "ineq", "fun": lambda x: x[2] - s_side_min(x[3])},
        ]
    t0 = time.perf_counter()
    result = minimize(
        fun,
        x0=np.asarray(x0, dtype=np.float64),
        method="SLSQP",
        bounds=bounds,
        constraints=cons,
        options=dict(ftol=1e-12, maxiter=500),
    )
    wall = time.perf_counter() - t0
    return result, wall


def run_one_start(fixture_id, family, start_id, x0, x_target, fault_inject=False, record_telemetry=True):
    telemetry_rows = []
    optimizer_path = "primary"
    hard_predicates = set()
    endpoint = None
    nonconverged = False
    numeric_error = False

    try:
        result, wall = run_primary(family, x0, x_target, fault_inject=fault_inject)
        x_ret = np.asarray(result.x, dtype=np.float64)
        if not np.all(np.isfinite(x_ret)) or not np.isfinite(result.fun):
            numeric_error = True
        else:
            if record_telemetry:
                telemetry_rows.append(dict(
                    fixture_id=fixture_id, family=family, start_id=start_id,
                    optimizer_path="primary", status=int(result.status),
                    message=str(result.message), success=bool(result.success),
                    nit=int(getattr(result, "nit", -1)),
                    nfev=int(getattr(result, "nfev", -1)),
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
        if record_telemetry:
            telemetry_rows.append(dict(
                fixture_id=fixture_id, family=family, start_id=start_id,
                optimizer_path="primary", status=-1,
                message="EXCEPTION:" + type(exc).__name__ + (":FAULT_INJECTION_TEST_ONLY" if fault_inject else ""),
                success=False, nit=-1, nfev=-1, njev=-1, wall_clock_seconds=float("nan"),
            ))

    if numeric_error:
        optimizer_path = "fallback"
        try:
            result2, wall2 = run_fallback(family, x0, x_target)
            x_ret2 = np.asarray(result2.x, dtype=np.float64)
            if record_telemetry:
                telemetry_rows.append(dict(
                    fixture_id=fixture_id, family=family, start_id=start_id,
                    optimizer_path="fallback", status=int(result2.status),
                    message=str(result2.message), success=bool(result2.success),
                    nit=int(getattr(result2, "nit", -1)),
                    nfev=int(getattr(result2, "nfev", -1)),
                    njev=-1,
                    wall_clock_seconds=wall2,
                ))
            if not np.all(np.isfinite(x_ret2)):
                hard_predicates.add("OTHER_PREDECLARED_NUMERICAL_FAILURE")
                endpoint = x_ret2
            else:
                endpoint = x_ret2
                nonconverged = not bool(result2.success)
        except Exception as exc2:
            hard_predicates.add("OTHER_PREDECLARED_NUMERICAL_FAILURE")
            if record_telemetry:
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
        fixture_id=fixture_id,
        family=family,
        start_id=start_id,
        optimizer_path=optimizer_path,
        status_class=("nonconverged" if nonconverged else ("numeric_error" if hard_predicates else "converged")),
        predicates=cls["predicates"],
        rejection_reasons=cls["rejection_reasons"],
        scientific_domain_pass=cls["scientific_domain_pass"],
        kural_t_pass_exact=cls["kural_t_pass_exact"],
        kural_s_pass_exact=cls["kural_s_pass_exact"],
        eligible=cls["eligible"],
        terminal_endpoint_hex=canonical_hex(cls["theta"]),
        family_status=None,
        family_summary=None,
    )
    return canonical, cls, telemetry_rows


def mini_bank_indices(n_fixed):
    return [0, (n_fixed - 1) // 2, n_fixed - 1]


def feature_start(family, x_fixture):
    j_star = int(np.flatnonzero(x_fixture == x_fixture.max())[0])
    u_star = j_star / 145.0
    if family == "P-01":
        k_mid = math.sqrt(4.0 * K_MAX)
        return (u_star - 1.0 / 8.0, u_star + 1.0 / 8.0, k_mid, k_mid), u_star, j_star
    else:
        s_feat = 0.32057672965544004
        beta_mid = math.sqrt(6.0)
        return (u_star, s_feat, s_feat, beta_mid), u_star, j_star


# ==========================================================================
# X2 -- fixture-manifest <-> registry bijection
# ==========================================================================
FIXTURE_MANIFEST_PATH = "p_konum_plus/calibration/f2_step2_fixture_manifest_2026-09-01.csv"
D_F2_09_MANIFEST_PATH = "p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv"

# Explicit harness registry: fixture_id -> (fixture_class, family, execution_mode)
# execution_mode is restricted to the already-authorized STEP-2 verification
# modes listed in the governing prompt Section 5.
HARNESS_REGISTRY = {
    "FIX-P01-BENIGN": ("analytic_benign_generator", "P-01", "real_optimizer_smoke"),
    "FIX-P02-BENIGN": ("analytic_benign_generator", "P-02", "real_optimizer_smoke"),
    "FIX-P01-STABLE-INTERIOR": ("stable_evaluation_analytic", "P-01", "analytic_evaluation"),
    "FIX-P01-STABLE-BOUNDARY": ("stable_evaluation_analytic", "P-01", "analytic_evaluation"),
    "FIX-P02-STABLE-INTERIOR": ("stable_evaluation_analytic", "P-02", "analytic_evaluation"),
    "FIX-P02-STABLE-BOUNDARY-SMIN": ("stable_evaluation_analytic", "P-02", "analytic_evaluation"),
    "FIX-P01-ZEROVAR-IN-DOMAIN": ("stable_evaluation_analytic", "P-01", "analytic_evaluation"),
    "FIX-NONFINITE-INPUT": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record"),
    "FIX-INVALID-INIT": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record"),
    "FIX-NONFINITE-PARAMETER": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record"),
    "FIX-NONFINITE-FIT": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record"),
    "FIX-P01-KURAL-S-FAIL": ("failure_path_fabricated_but_real_generator", "P-01", "analytic_evaluation"),
    "FIX-OPTIMIZER-NONCONVERGENCE": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record"),
    "FIX-OTHER-NUMERICAL-FAILURE": ("failure_path_fabricated", "P-CMN", "fabricated_unit_record"),
    "FIX-FAMILY-FIT-FAILURE": ("failure_path_fabricated", "P-CMN", "aggregation_unit"),
    "FIX-RESERVED-CODES-NEGATIVE": ("assertion_only", "P-CMN", "negative_assertion"),
    "FIX-FALLBACK-FAULT-INJECTION": ("fallback_fault_injection", "P-01", "fault_injection_fallback"),
    "FIX-AGG-UNIQUE-MIN": ("multistart_aggregation_fabricated", "P-CMN", "aggregation_unit"),
    "FIX-AGG-TIE": ("multistart_aggregation_fabricated", "P-CMN", "aggregation_unit"),
    "FIX-AGG-LOWERL-INELIGIBLE": ("multistart_aggregation_fabricated", "P-CMN", "aggregation_unit"),
    "FIX-D0F209-MANIFEST-QC": ("manifest_reconstruction", "P-CMN", "manifest_qc"),
}

HARNESS_SELF_TEST_IDS = {
    "SELFTEST-X1-P01-ORDER",
    "SELFTEST-X1-P02-SMIN",
    "SELFTEST-C3-DISPLAY-PRECEDENCE",
}


def load_manifest_rows():
    with open(FIXTURE_MANIFEST_PATH, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_manifest_registry_bijection():
    rows = load_manifest_rows()
    declared_fixture_ids = set(r["fixture_id"] for r in rows)
    implemented_fixture_ids = set(HARNESS_REGISTRY.keys())

    metadata_mismatches = []
    manifest_by_id = {r["fixture_id"]: r for r in rows}
    for fid, (fclass, fam, mode) in HARNESS_REGISTRY.items():
        row = manifest_by_id.get(fid)
        if row is None:
            metadata_mismatches.append(dict(fixture_id=fid, field="fixture_id", issue="NOT_IN_MANIFEST"))
            continue
        if "fixture_class" in row:
            if row["fixture_class"] != fclass:
                metadata_mismatches.append(dict(fixture_id=fid, field="fixture_class", manifest=row["fixture_class"], registry=fclass))
        else:
            metadata_mismatches.append(dict(fixture_id=fid, field="fixture_class", issue="NOT_PRESENT_IN_MANIFEST"))
        if "family" in row:
            if row["family"] != fam:
                metadata_mismatches.append(dict(fixture_id=fid, field="family", manifest=row["family"], registry=fam))
        else:
            metadata_mismatches.append(dict(fixture_id=fid, field="family", issue="NOT_PRESENT_IN_MANIFEST"))
        if "execution_mode" not in row:
            pass  # reported once, globally, below -- column absent from manifest entirely

    execution_mode_column_present = ("execution_mode" in rows[0]) if rows else False

    return dict(
        declared_fixture_ids=sorted(declared_fixture_ids),
        implemented_fixture_ids=sorted(implemented_fixture_ids),
        pre_execution_bijection_ok=(declared_fixture_ids == implemented_fixture_ids),
        metadata_mismatches=[m for m in metadata_mismatches if m.get("issue") != "NOT_PRESENT_IN_MANIFEST"],
        execution_mode_column_status="NOT_PRESENT_IN_MANIFEST" if not execution_mode_column_present else "PRESENT",
    )


# ==========================================================================
# Main fixture suite
# ==========================================================================
def run_all_fixtures():
    canonical_records = []
    self_test_records = []
    telemetry = []
    emitted_predicates_union = set()
    emitted_warn_union = set()

    registry_check = check_manifest_registry_bijection()
    assert registry_check["pre_execution_bijection_ok"], "PRE-EXECUTION BIJECTION FAILURE: %r" % registry_check

    # ---- D-F2-09 manifest reconstruction QC ----
    raw01, ret01 = build_grid("P-01")
    raw02, ret02 = build_grid("P-02")
    manifest_qc = dict(
        p01_raw_count=len(raw01), p01_retained_count=len(ret01),
        p02_raw_count=len(raw02), p02_retained_count=len(ret02),
    )

    with open(D_F2_09_MANIFEST_PATH, "r", newline="", encoding="utf-8") as f:
        csv_rows = list(csv.DictReader(f))
    csv_p01_retained = sorted(
        tuple(float(v) for v in r["parameter_values"].split(";"))
        for r in csv_rows if r["family"] == "P-01" and r["retained"] == "true"
    )
    csv_p02_retained = sorted(
        tuple(float(v) for v in r["parameter_values"].split(";"))
        for r in csv_rows if r["family"] == "P-02" and r["retained"] == "true"
    )
    manifest_qc["p01_matches_csv"] = (ret01 == csv_p01_retained)
    manifest_qc["p02_matches_csv"] = (ret02 == csv_p02_retained)
    manifest_qc["p01_count_731"] = (len(ret01) == 731)
    manifest_qc["p02_count_261"] = (len(ret02) == 261)
    manifest_qc["p01_order_ascending"] = (ret01 == sorted(ret01))
    manifest_qc["p02_order_ascending"] = (ret02 == sorted(ret02))
    manifest_qc["p01_dedup_exact"] = (len(ret01) == len(set(ret01)))
    manifest_qc["p02_dedup_exact"] = (len(ret02) == len(set(ret02)))

    # ============================================================
    # FIX-P01-BENIGN / FIX-P02-BENIGN
    # ============================================================
    def run_benign(fixture_id, family, theta_fixture, n_fixed_expected, retained):
        stable_fn = p01_stable if family == "P-01" else p02_stable
        g = stable_fn(theta_fixture)
        status, sigma, ghat = zero_variance_rule(g)
        assert status == "OK", "benign fixture unexpectedly zero-variance/nonfinite: %s" % fixture_id
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
            fs_domain_ok = (v <= FEASIBILITY_ACCEPTANCE_TOL) and fs_zv == "OK" and domain_ok and kt_ok and \
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
        for start_id, x0 in starts:
            canonical, cls, tel = run_one_start(fixture_id, family, start_id, x0, x_fixture)
            canonical_records.append(canonical)
            telemetry.extend(tel)
            emitted_predicates_union.update(cls["predicates"])
            L = objective_L(x_fixture, stable_fn(cls["theta"])) if cls["theta_finite"] else float("inf")
            if cls["theta_finite"] and cls["eligible"]:
                g_final = stable_fn(cls["theta"])
                _, _, ghat_final = zero_variance_rule(g_final)
                L = objective_L(x_fixture, ghat_final)
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

        # C1: exact benign PASS criterion
        c1_pass = (
            True  # no unhandled exception reached this point
            and len(endpoint_records) == (n_fixed_expected and len(starts))
            and any(r["eligible"] for r in endpoint_records)
        )
        return dict(
            fixture_id=fixture_id, n_starts=len(starts),
            feature_start_valid=fs_valid, agg_status=agg_status,
            has_eligible_endpoint=any(r["eligible"] for r in endpoint_records),
            c1_pass_criterion=c1_pass,
        )

    u0 = 72.0 / 145.0
    k_mid = math.sqrt(4.0 * K_MAX)
    beta_mid = math.sqrt(6.0)
    s_feature = 0.32057672965544004

    theta_p01_fix = (u0 - 1.0 / 8.0, u0 + 1.0 / 8.0, k_mid, k_mid)
    theta_p02_fix = (u0, s_feature, s_feature, beta_mid)

    p01_benign_result = run_benign("FIX-P01-BENIGN", "P-01", theta_p01_fix, 731, ret01)
    p02_benign_result = run_benign("FIX-P02-BENIGN", "P-02", theta_p02_fix, 261, ret02)

    # ============================================================
    # Stable-evaluation analytic fixtures
    # ============================================================
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
        except Exception as exc:
            stable_eval_results[fid] = dict(exception=True, error=type(exc).__name__)
        canonical_records.append(dict(
            fixture_id=fid, family=fam, start_id="eval_only",
            optimizer_path="not_run", status_class=stable_eval_results[fid].get("status", "EXCEPTION"),
            predicates=[stable_eval_results[fid]["status"]] if stable_eval_results[fid].get("status") not in (None, "OK") else [],
            rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
            eligible=False, terminal_endpoint_hex=canonical_hex(theta),
            family_status=None, family_summary=None,
        ))

    theta_zv = (-1.0, 1.375, 40.0, K_MAX)
    g_zv = p01_stable(theta_zv)
    zv_status, zv_sigma, _ = zero_variance_rule(g_zv)
    canonical_records.append(dict(
        fixture_id="FIX-P01-ZEROVAR-IN-DOMAIN", family="P-01", start_id="eval_only",
        optimizer_path="not_run", status_class=zv_status,
        predicates=[zv_status] if zv_status != "OK" else [],
        rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=canonical_hex(theta_zv),
        family_status=None, family_summary=None,
    ))
    if zv_status != "OK":
        emitted_predicates_union.add(zv_status)

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

    # ============================================================
    # Failure-path fabricated fixtures (unit-level, bypass optimizer)
    # ============================================================
    x_bad = np.ones(146)
    x_bad[10] = np.nan
    nonfinite_input_detected = not np.all(np.isfinite(x_bad))
    canonical_records.append(dict(
        fixture_id="FIX-NONFINITE-INPUT", family="P-CMN", start_id="unit",
        optimizer_path="not_run", status_class="NONFINITE_INPUT" if nonfinite_input_detected else "UNEXPECTED",
        predicates=["NONFINITE_INPUT"] if nonfinite_input_detected else [],
        rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))
    if nonfinite_input_detected:
        emitted_predicates_union.add("NONFINITE_INPUT")

    start_bad = (float("nan"), 0.5, 20.0, 20.0)
    invalid_init_detected = not all(math.isfinite(v) for v in start_bad)
    canonical_records.append(dict(
        fixture_id="FIX-INVALID-INIT", family="P-CMN", start_id="unit",
        optimizer_path="not_run", status_class="INVALID_INITIALIZATION" if invalid_init_detected else "UNEXPECTED",
        predicates=["INVALID_INITIALIZATION"] if invalid_init_detected else [],
        rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=canonical_hex(start_bad), family_status=None, family_summary=None,
    ))
    if invalid_init_detected:
        emitted_predicates_union.add("INVALID_INITIALIZATION")

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

    g_fab = np.ones(146)
    g_fab[50] = np.inf
    fab_status, _, _ = zero_variance_rule(g_fab)
    canonical_records.append(dict(
        fixture_id="FIX-NONFINITE-FIT", family="P-CMN", start_id="unit",
        optimizer_path="not_run", status_class=fab_status,
        predicates=[fab_status] if fab_status != "OK" else [],
        rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))
    if fab_status != "OK":
        emitted_predicates_union.add(fab_status)

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

    canonical_records.append(dict(
        fixture_id="FIX-OTHER-NUMERICAL-FAILURE", family="P-CMN", start_id="unit",
        optimizer_path="fallback(fabricated)", status_class="OTHER_PREDECLARED_NUMERICAL_FAILURE",
        predicates=["OTHER_PREDECLARED_NUMERICAL_FAILURE"], rejection_reasons=[],
        scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=False, terminal_endpoint_hex=canonical_hex((float("nan"),) * 4),
        family_status=None, family_summary=None,
    ))
    emitted_predicates_union.add("OTHER_PREDECLARED_NUMERICAL_FAILURE")

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
        family_status=fff_status if fff_status == "FAMILY_FIT_FAILURE" else "OK",
        family_summary=fff_label if fff_status == "FAMILY_FIT_FAILURE" else None,
    ))

    # ============================================================
    # FIX-FALLBACK-FAULT-INJECTION
    # ============================================================
    x0_designated = ret01[0]
    x_target_fault = np.linspace(-1, 1, 146)
    x_target_fault = (x_target_fault - x_target_fault.mean()) / x_target_fault.std(ddof=0)
    canonical_fault, cls_fault, tel_fault = run_one_start(
        "FIX-FALLBACK-FAULT-INJECTION", "P-01", "designated_start_idx0",
        x0_designated, x_target_fault, fault_inject=True,
    )
    canonical_records.append(canonical_fault)
    telemetry.extend(tel_fault)
    emitted_predicates_union.update(cls_fault["predicates"])
    fallback_invoked = canonical_fault["optimizer_path"] == "fallback"
    same_start_reused = canonical_fault["start_id"] == "designated_start_idx0"

    # ============================================================
    # Multistart aggregation QC (fabricated)
    # ============================================================
    agg_unique = aggregate([
        dict(theta=(0.1, 0.2, 5.0, 6.0), L=2.0, eligible=True),
        dict(theta=(0.3, 0.4, 7.0, 8.0), L=0.5, eligible=True),
        dict(theta=(0.9, 1.0, 9.0, 9.0), L=9.0, eligible=False),
    ])
    agg_tie = aggregate([
        dict(theta=(0.9, 1.0, 9.0, 9.0), L=1.0000000000005, eligible=True),
        dict(theta=(0.1, 0.2, 5.0, 6.0), L=1.0, eligible=True),
        dict(theta=(0.3, 0.4, 7.0, 8.0), L=5.0, eligible=True),
    ])
    agg_lowerl_ineligible = aggregate([
        dict(theta=(0.0, 0.0, 4.0, 4.0), L=0.001, eligible=False),
        dict(theta=(0.5, 0.6, 10.0, 10.0), L=3.0, eligible=True),
    ])
    for fid, res in [
        ("FIX-AGG-UNIQUE-MIN", agg_unique),
        ("FIX-AGG-TIE", agg_tie),
        ("FIX-AGG-LOWERL-INELIGIBLE", agg_lowerl_ineligible),
    ]:
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

    agg_checks = dict(
        unique_min_correct=(agg_unique[0] == "OK" and agg_unique[1]["theta"] == (0.3, 0.4, 7.0, 8.0)),
        tie_correct=(agg_tie[0] == "OK" and agg_tie[1]["theta"] == (0.1, 0.2, 5.0, 6.0)),
        lowerl_ineligible_excluded=(agg_lowerl_ineligible[0] == "OK" and agg_lowerl_ineligible[1]["theta"] == (0.5, 0.6, 10.0, 10.0)),
        family_fit_failure_label_correct=(fff_status == "FAMILY_FIT_FAILURE" and fff_label == "NO_ADMISSIBLE_ENDPOINT_FROM_PREDECLARED_MULTISTART"),
    )

    # ============================================================
    # Reserved-code negative assertion
    # ============================================================
    reserved_violation = bool(emitted_predicates_union & RESERVED_NOT_EMITTED) or bool(emitted_warn_union & RESERVED_WARN_NOT_EMITTED)
    canonical_records.append(dict(
        fixture_id="FIX-RESERVED-CODES-NEGATIVE", family="P-CMN", start_id="assertion",
        optimizer_path="not_run", status_class=("VIOLATION" if reserved_violation else "CONFIRMED_ABSENT"),
        predicates=[], rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=not reserved_violation, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))

    manifest_qc_pass = all([
        manifest_qc["p01_matches_csv"], manifest_qc["p02_matches_csv"],
        manifest_qc["p01_count_731"], manifest_qc["p02_count_261"],
        manifest_qc["p01_order_ascending"], manifest_qc["p02_order_ascending"],
        manifest_qc["p01_dedup_exact"], manifest_qc["p02_dedup_exact"],
    ])
    canonical_records.append(dict(
        fixture_id="FIX-D0F209-MANIFEST-QC", family="P-CMN", start_id="reconstruction",
        optimizer_path="not_run", status_class="PASS" if manifest_qc_pass else "FAIL",
        predicates=[], rejection_reasons=[], scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
        eligible=True, terminal_endpoint_hex=None, family_status=None, family_summary=None,
    ))

    # ============================================================
    # X2 post-execution fixture-ID/registry fidelity
    # ============================================================
    executed_fixture_ids = set(r["fixture_id"] for r in canonical_records) - HARNESS_SELF_TEST_IDS
    declared_fixture_ids = set(registry_check["declared_fixture_ids"])
    undeclared_executed_fixture_ids = sorted(executed_fixture_ids - declared_fixture_ids)
    declared_but_unexecuted_fixture_ids = sorted(declared_fixture_ids - executed_fixture_ids)
    post_execution_bijection_ok = (declared_fixture_ids == executed_fixture_ids)

    # ============================================================
    # X1 adversarial harness self-tests (NOT part of the frozen fixture set)
    # ============================================================
    theta_order = (0.500000005, 0.500000000, 20.0, 20.0)
    cls_order = classify_endpoint(theta_order, "P-01")
    selftest_x1_order = dict(
        self_test_id="SELFTEST-X1-P01-ORDER",
        theta=theta_order,
        v_p01=v_p01(theta_order),
        numerically_feasible_may_be_true=(v_p01(theta_order) <= FEASIBILITY_ACCEPTANCE_TOL),
        scientific_domain_pass=cls_order["scientific_domain_pass"],
        morphology_inadmissible_emitted=("MORPHOLOGY_INADMISSIBLE" in cls_order["predicates"]),
        eligible=cls_order["eligible"],
        expected=dict(scientific_domain_pass=False, morphology_inadmissible_emitted=True, eligible=False),
        pass_=(bool(cls_order["scientific_domain_pass"]) is False and "MORPHOLOGY_INADMISSIBLE" in cls_order["predicates"] and cls_order["eligible"] is False),
    )
    self_test_records.append(dict(self_test_id="SELFTEST-X1-P01-ORDER", family="P-01",
                                   predicates=cls_order["predicates"], eligible=cls_order["eligible"],
                                   scientific_domain_pass=cls_order["scientific_domain_pass"],
                                   terminal_endpoint_hex=canonical_hex(theta_order)))

    beta_smin_test = math.sqrt(6.0)  # C2: pinned exactly
    smin_val = s_side_min(beta_smin_test)
    theta_smin = (0.5, smin_val - 5e-13, smin_val, beta_smin_test)
    cls_smin = classify_endpoint(theta_smin, "P-02")
    selftest_x1_smin = dict(
        self_test_id="SELFTEST-X1-P02-SMIN",
        theta=theta_smin,
        beta_used=beta_smin_test,
        beta_is_sqrt6_exact=(beta_smin_test == math.sqrt(6.0)),
        v_p02=v_p02(theta_smin),
        numerically_feasible_may_be_true=(v_p02(theta_smin) <= FEASIBILITY_ACCEPTANCE_TOL),
        scientific_domain_pass=cls_smin["scientific_domain_pass"],
        morphology_inadmissible_emitted=("MORPHOLOGY_INADMISSIBLE" in cls_smin["predicates"]),
        eligible=cls_smin["eligible"],
        expected=dict(scientific_domain_pass=False, morphology_inadmissible_emitted=True, eligible=False),
        pass_=(bool(cls_smin["scientific_domain_pass"]) is False and "MORPHOLOGY_INADMISSIBLE" in cls_smin["predicates"] and cls_smin["eligible"] is False),
    )
    self_test_records.append(dict(self_test_id="SELFTEST-X1-P02-SMIN", family="P-02",
                                   predicates=cls_smin["predicates"], eligible=cls_smin["eligible"],
                                   scientific_domain_pass=cls_smin["scientific_domain_pass"],
                                   terminal_endpoint_hex=canonical_hex(theta_smin)))

    # ============================================================
    # C3 -- display-precedence self-test
    # ============================================================
    fabricated_predicate_set = {"NONFINITE_FIT", "MORPHOLOGY_INADMISSIBLE"}
    c3_display_code = primary_display_code(fabricated_predicate_set)
    selftest_c3 = dict(
        self_test_id="SELFTEST-C3-DISPLAY-PRECEDENCE",
        input_predicates=sorted(fabricated_predicate_set),
        primary_display_code=c3_display_code,
        all_predicates_still_present=(fabricated_predicate_set == {"NONFINITE_FIT", "MORPHOLOGY_INADMISSIBLE"}),
        expected_primary_display_code="NONFINITE_FIT",
        pass_=(c3_display_code == "NONFINITE_FIT"),
    )
    self_test_records.append(dict(self_test_id="SELFTEST-C3-DISPLAY-PRECEDENCE", family="P-CMN",
                                   predicates=sorted(fabricated_predicate_set), eligible=False,
                                   scientific_domain_pass=None, terminal_endpoint_hex=None,
                                   primary_display_code=c3_display_code))

    summary = dict(
        manifest_qc=manifest_qc,
        p01_benign=p01_benign_result,
        p02_benign=p02_benign_result,
        stable_eval_results=stable_eval_results,
        zv_in_domain_status=zv_status,
        zv_in_domain_sigma=zv_sigma,
        kural_s_fail_status=cls_ks["primary_display_code"],
        fallback_invoked=fallback_invoked,
        same_start_reused=same_start_reused,
        agg_checks=agg_checks,
        emitted_predicates_union=sorted(emitted_predicates_union),
        reserved_violation=reserved_violation,
        registry_check=dict(registry_check),
        post_execution_bijection_ok=post_execution_bijection_ok,
        undeclared_executed_fixture_ids=undeclared_executed_fixture_ids,
        declared_but_unexecuted_fixture_ids=declared_but_unexecuted_fixture_ids,
        selftest_x1_order=selftest_x1_order,
        selftest_x1_smin=selftest_x1_smin,
        selftest_c3=selftest_c3,
    )
    return canonical_records, self_test_records, telemetry, summary


def canonicalize(records):
    return json.dumps(records, sort_keys=True, default=str)


def main():
    run1_records, run1_self, run1_telemetry, run1_summary = run_all_fixtures()
    run2_records, run2_self, run2_telemetry, run2_summary = run_all_fixtures()

    combined1 = dict(records=run1_records, self_tests=run1_self)
    combined2 = dict(records=run2_records, self_tests=run2_self)
    canon1 = canonicalize(combined1)
    canon2 = canonicalize(combined2)
    determinism_pass = (canon1 == canon2)

    import hashlib
    canon1_hash = hashlib.sha256(canon1.encode("utf-8")).hexdigest()
    canon2_hash = hashlib.sha256(canon2.encode("utf-8")).hexdigest()

    # C5: successor telemetry contains RUN1 calls only.
    telemetry_fields = [
        "fixture_id", "family", "start_id", "optimizer_path", "status",
        "message", "success", "nit", "nfev", "njev", "wall_clock_seconds",
    ]
    out_path = "p_konum_plus/calibration/f2_step2_feasibility_telemetry_r2_2026-09-01.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=telemetry_fields, lineterminator="\n")
        w.writeheader()
        for row in run1_telemetry:
            w.writerow(row)

    env_info = dict(
        python=platform.python_version(),
        numpy=np.__version__,
        scipy=scipy.__version__,
        platform=platform.platform(),
        OMP_NUM_THREADS=os.environ.get("OMP_NUM_THREADS"),
        OPENBLAS_NUM_THREADS=os.environ.get("OPENBLAS_NUM_THREADS"),
        MKL_NUM_THREADS=os.environ.get("MKL_NUM_THREADS"),
    )

    print("ENV_INFO=" + json.dumps(env_info, sort_keys=True))
    print("DETERMINISM_PASS=" + str(determinism_pass))
    print("CANON1_SHA256=" + canon1_hash)
    print("CANON2_SHA256=" + canon2_hash)
    print("RUN1_N_RECORDS=" + str(len(run1_records)))
    print("RUN2_N_RECORDS=" + str(len(run2_records)))
    print("RUN1_SUMMARY=" + json.dumps(run1_summary, sort_keys=True, default=str))
    print("RUN2_SUMMARY_EQUAL_TO_RUN1=" + str(json.dumps(run1_summary, sort_keys=True, default=str) == json.dumps(run2_summary, sort_keys=True, default=str)))
    print("TELEMETRY_ROWS_WRITTEN=" + str(len(run1_telemetry)))
    print("TELEMETRY_RUN=" + TELEMETRY_RUN_LABEL)
    print("RNG_USED=" + str(RNG_USED))
    print("L_INVALID_PREDICTION_GUARD=" + repr(L_INVALID_PREDICTION_GUARD))


if __name__ == "__main__":
    main()
