"""F3 spline solver qualification r2 - schema-safe manifest + synthetic-only rerun.

Binding control flow (mechanically enforced below, in this order):
  1. construct complete r2 manifest in memory
  2. serialize schema-safely (csv.writer, ascii, LF)
  3. write manifest r2
  4. reopen and schema-validate
  5. compute SHA256 from exact file bytes
  6. print/log manifest path + SHA256
  7. write pre-execution custody record (manifest SHA256 + harness SHA256)
  8. ONLY THEN execute the first synthetic solver case

No SSA/F1 access. No P-01/P-02 fitting. No candidate adequacy code.
Fixture constructions are byte-for-byte the same rules/coefficients/seeds/
masks/mode rules as the original executed harness (ecda07d0...).
"""
from __future__ import annotations
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import csv
import hashlib
import sys
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import minimize, nnls, LinearConstraint

REPO = "G:/PycharmProjects/pkp-worktree"
MANIFEST_PATH = REPO + "/p_konum_plus/calibration/f3_spline_solver_qualification_manifest_r2_2026-09-03.csv"
RESULTS_PATH = REPO + "/p_konum_plus/calibration/f3_spline_solver_qualification_results_r2_2026-09-03.csv"
CUSTODY_PATH = REPO + "/p_konum_plus/provenance/f3_spline_solver_qualification_preexecution_custody_r2_2026-09-03.md"

# ---------------- predeclared literals (identical to original run) ----------------
T = 146
U = np.linspace(0.0, 1.0, T)
DEG = 3
KNOTS = np.array([0.0, 0.0, 0.0, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0, 1.0, 1.0])
NBASIS = 8
KAPPA = 0.1
FEAS_TOL = 1e-8            # spline_feasibility_acceptance_tol
REF_ACT_TOL = 1e-8         # reference_active_set_identification_tol
POLISH_TOL = 1e-8          # postpolish_primary_active_set_tol
EXPAND_TOL = 1e-6          # postpolish_expansion_tol
KKT_TOL = 1e-8             # spline_kkt_stationarity_tol
TC_OPTS = dict(gtol=1e-10, xtol=1e-14, barrier_tol=1e-12, maxiter=1000)
SLSQP_OPTS = dict(ftol=1e-12, maxiter=500)

B = BSpline.design_matrix(U, KNOTS, DEG).toarray()
assert B.shape == (T, NBASIS)
assert np.allclose(B.sum(axis=1), 1.0, atol=1e-12)

D1 = np.zeros((T - 1, T))
for t in range(T - 1):
    D1[t, t] = -1.0
    D1[t, t + 1] = 1.0

def amat(mode_idx):
    s = np.ones(T - 1)
    s[mode_idx:] = -1.0
    return (s[:, None] * D1) @ B  # (145, 8), orientation A c >= 0

def zddof0(v):
    return (v - v.mean()) / v.std(ddof=0)

C_INT = np.array([0.0, 0.4, 1.2, 2.4, 1.6, 0.8, 0.3, 0.05])
C_DEC = np.array([3.0, 2.2, 1.5, 1.0, 0.6, 0.35, 0.15, 0.0])
C_INC = C_DEC[::-1].copy()
C_RIGHT = np.array([0.0, 0.05, 0.1, 0.3, 0.7, 1.6, 2.4, 0.9])

def bump(u):
    return np.exp(-(((u - 0.55) / 0.12) ** 2))

MASKS = {
    "full": np.arange(T),
    "interior_mask": np.concatenate([np.arange(0, 58), np.arange(87, T)]),
    "left_edge_mask": np.arange(15, T),
    "right_edge_mask": np.arange(0, 131),
}
MASK_RULE = {"full": "all 146 indices", "interior_mask": "indices [0,58) union [87,146)",
             "left_edge_mask": "indices [15,146)", "right_edge_mask": "indices [0,131)"}

def raw_of(kind):
    return {"spline_c_int": lambda: B @ C_INT, "spline_c_dec": lambda: B @ C_DEC,
            "spline_c_inc": lambda: B @ C_INC, "spline_c_right": lambda: B @ C_RIGHT,
            "analytic_bump": lambda: bump(U)}[kind]()

def modeidx_of(kind):
    return int(np.argmax(raw_of(kind)))

FIXTURES = [
    ("Q01", "near_noiseless_spline_representable", "spline_c_int", 0.0, None, "argmax_raw", "full"),
    ("Q02", "low_rss_spline_representable", "spline_c_int", 0.02, 20260903, "argmax_raw", "full"),
    ("Q03", "moderate_rss_analytic", "analytic_bump", 0.2, 20260904, "argmax_raw", "full"),
    ("Q04", "high_rss_analytic", "analytic_bump", 1.0, 20260905, "argmax_raw", "full"),
    ("Q05", "boundary_mode_0", "spline_c_dec", 0.05, 20260906, "fixed:0", "full"),
    ("Q06", "boundary_mode_145", "spline_c_inc", 0.05, 20260907, "fixed:145", "full"),
    ("Q07", "interior_masked_context", "analytic_bump", 0.2, 20260908, "argmax_raw", "interior_mask"),
    ("Q08", "left_edge_masked_context", "analytic_bump", 0.2, 20260909, "argmax_raw", "left_edge_mask"),
    ("Q09", "right_edge_masked_context", "analytic_bump", 0.2, 20260910, "argmax_raw", "right_edge_mask"),
    ("Q10", "degenerate_many_active", "spline_c_right", 0.2, 20260911, "fixed:10", "full"),
]
COEF_MAP = {"spline_c_int": C_INT, "spline_c_dec": C_DEC, "spline_c_inc": C_INC,
            "spline_c_right": C_RIGHT}
CONFIGS = ["SOLVER-A", "SOLVER-B", "SOLVER-C"]

def fixture_mode(mrule, kind):
    return int(mrule.split(":")[1]) if mrule.startswith("fixed:") else modeidx_of(kind)

# ---------------- shared literal rule strings (stated literally, not by code reference) ----------------
ACCEPT_RULE = ("accept(c) = all coordinates finite AND max(0, -min(A @ c)) <= 1e-8 "
               "AND NNLS_KKT_existence_residual(c, active_set_tol=1e-8) <= 1e-8")
STAGE3_ACCEPT = ("stage3_acceptance = SLSQP success flag AND finite endpoint AND finite objective "
                 "AND max_linear_constraint_violation <= 1e-8; stage3_nnls_kkt_required = false")
MODE_REJECT = ("if stage3_acceptance == false: mode_idx = NUMERICALLY_INVALID, excluded from "
               "equivalent_mode_set; if no numerically valid mode exists: spline_fit_status = FAILURE")
REF_RULE = ("dual-NNLS convex QP: H = B_O^T B_O = L L^T; w = L^-1 b; G = L^-1 A^T; "
            "lambda* = NNLS(G, -w); c_ref = H^-1 (b + A^T lambda*)")
CASE_ACCEPT = ("case_acceptance_pass = reference_certified AND objective_accuracy_pass AND feasibility_pass; "
               "semantic repeatability: each reference and each tested configuration solved twice in-process, "
               "exact repr equality of RSS required")
SUITE_ACCEPT = "qualification_pass = ALL predeclared cases pass; no averaging, no pass fraction"
OBJ_RULE = "objective_accuracy_pass = |RSS_solver - RSS_ref| <= kappa_solver * mode_tolerance"
MODE_TOL_RULE = "mode_tolerance = 1e-12 + 1e-9 * abs(RSS_ref)"

CFG_FIELDS = {
    "SOLVER-A": dict(
        primary_solver="SLSQP",
        primary_solver_options="ftol=1e-12, maxiter=500, x0 = zero vector of length 8 (feasible origin)",
        primary_success_rule="SLSQP success flag AND finite endpoint AND finite objective AND max(0, -min(A @ c)) <= 1e-8",
        stage1_postpolish_rule="NOT_APPLICABLE", postpolish_primary_active_set_tol="NOT_APPLICABLE",
        expansion_trigger="NOT_APPLICABLE", stage2_postpolish_rule="NOT_APPLICABLE",
        postpolish_expansion_tol="NOT_APPLICABLE",
        stage3_fallback_solver="trust-constr",
        stage3_fallback_options="gtol=1e-10, xtol=1e-14, barrier_tol=1e-12, maxiter=1000",
        stage3_fallback_x0="zero vector of length 8 (feasible origin)",
        stage3_trigger="NOT primary_success_rule",
        stage3_acceptance_rule="trust-constr status in {1,2} AND finite endpoint AND finite objective AND max(0, -min(A @ c)) <= 1e-8",
    ),
    "SOLVER-B": dict(
        primary_solver="trust-constr",
        primary_solver_options="gtol=1e-10, xtol=1e-14, barrier_tol=1e-12, maxiter=1000",
        primary_success_rule="trust-constr status in {1,2} AND finite endpoint AND finite objective; endpoint c_tc delivered to stage 1 unconditionally (polish consumes c_tc only through active-set identification)",
        stage1_postpolish_rule="equality-KKT post-polish using stage1_active_set = {i : |(A @ c_tc)_i| <= 1e-8}",
        postpolish_primary_active_set_tol="1e-08",
        expansion_trigger="NOT accept(stage1_postpolish_endpoint), where " + ACCEPT_RULE,
        stage2_postpolish_rule="equality-KKT post-polish using stage2_active_set = {i : |(A @ c_tc)_i| <= 1e-6}; re-identified from the SAME c_tc, not from the stage-1 endpoint",
        postpolish_expansion_tol="1e-06",
        stage3_fallback_solver="SLSQP",
        stage3_fallback_options="ftol=1e-12, maxiter=500",
        stage3_fallback_x0="zero vector of length 8 (feasible origin)",
        stage3_trigger="NOT accept(stage2_postpolish_endpoint), where " + ACCEPT_RULE,
        stage3_acceptance_rule=STAGE3_ACCEPT,
    ),
    "SOLVER-C": dict(
        primary_solver="trust-constr",
        primary_solver_options="gtol=1e-10, xtol=1e-14, barrier_tol=1e-12, maxiter=1000",
        primary_success_rule="trust-constr status in {1,2} AND finite endpoint AND finite objective AND max(0, -min(A @ c)) <= 1e-8",
        stage1_postpolish_rule="NOT_APPLICABLE", postpolish_primary_active_set_tol="NOT_APPLICABLE",
        expansion_trigger="NOT_APPLICABLE", stage2_postpolish_rule="NOT_APPLICABLE",
        postpolish_expansion_tol="NOT_APPLICABLE",
        stage3_fallback_solver="NOT_APPLICABLE", stage3_fallback_options="NOT_APPLICABLE",
        stage3_fallback_x0="NOT_APPLICABLE", stage3_trigger="NOT_APPLICABLE",
        stage3_acceptance_rule="NOT_APPLICABLE",
    ),
}

MANIFEST_HEADER = [
    "fixture_id", "fixture_class", "construction_rule", "coefficients_or_parameters",
    "noise_rule", "noise_sigma", "noise_seed", "standardization_rule", "mode_idx",
    "mask_context", "observed_index_rule", "tested_solver_configuration_id",
    "primary_solver", "primary_solver_options", "primary_success_rule",
    "stage1_postpolish_rule", "postpolish_primary_active_set_tol",
    "expansion_trigger", "stage2_postpolish_rule", "postpolish_expansion_tol",
    "stage3_fallback_solver", "stage3_fallback_options", "stage3_fallback_x0",
    "stage3_trigger", "stage3_acceptance_rule", "mode_rejection_rule",
    "reference_construction_rule", "reference_certificate_method",
    "reference_active_set_identification_tol", "constraint_orientation_convention",
    "multiplier_orientation_convention", "spline_kkt_stationarity_tol",
    "spline_feasibility_acceptance_tol", "kappa_solver", "mode_tolerance_rule",
    "objective_accuracy_rule", "qualification_case_acceptance_rule",
    "qualification_suite_acceptance_rule",
]

def build_manifest_rows():
    rows = []
    for fid, fcls, kind, sigma, seed, mrule, mask in FIXTURES:
        m = fixture_mode(mrule, kind)
        if kind in COEF_MAP:
            coefs = "c = " + ", ".join(repr(float(x)) for x in COEF_MAP[kind])
            cons = ("z = z_ddof0(raw + noise); raw = B @ c; B = clamped cubic B-spline design, "
                    "knot vector [0,0,0,0, 0.2,0.4,0.6,0.8, 1,1,1,1], 8 basis, 146-point u-grid")
        else:
            coefs = "analytic bump: exp(-(((u - 0.55) / 0.12)^2)) on the 146-point u-grid"
            cons = "z = z_ddof0(raw + noise); raw = analytic bump on u-grid"
        for cfg in CONFIGS:
            f = CFG_FIELDS[cfg]
            rows.append([
                fid, fcls, cons, coefs,
                "none" if seed is None else "numpy PCG64(seed) standard normal * sigma, added to raw before standardization",
                repr(float(sigma)), "none" if seed is None else str(seed),
                "z_ddof0: (v - mean(v)) / std(v, ddof=0)", str(m), mask, MASK_RULE[mask], cfg,
                f["primary_solver"], f["primary_solver_options"], f["primary_success_rule"],
                f["stage1_postpolish_rule"], f["postpolish_primary_active_set_tol"],
                f["expansion_trigger"], f["stage2_postpolish_rule"], f["postpolish_expansion_tol"],
                f["stage3_fallback_solver"], f["stage3_fallback_options"], f["stage3_fallback_x0"],
                f["stage3_trigger"], f["stage3_acceptance_rule"], MODE_REJECT,
                REF_RULE, "NNLS existence certificate", repr(REF_ACT_TOL),
                "A c >= 0", "lambda >= 0", repr(KKT_TOL), repr(FEAS_TOL), repr(KAPPA),
                MODE_TOL_RULE, OBJ_RULE, CASE_ACCEPT, SUITE_ACCEPT,
            ])
    return rows

# ---------------- steps 1-3: construct + serialize schema-safely + write ----------------
rows = build_manifest_rows()
with open(MANIFEST_PATH, "w", newline="", encoding="ascii") as fh:
    w = csv.writer(fh, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    w.writerow(MANIFEST_HEADER)
    w.writerows(rows)

# ---------------- step 4: reopen and schema-validate ----------------
with open(MANIFEST_PATH, "r", newline="", encoding="ascii") as fh:
    parsed = list(csv.reader(fh))
hdr, data = parsed[0], parsed[1:]
schema_ok = (
    len(hdr) == len(set(hdr))
    and hdr == MANIFEST_HEADER
    and all(len(r) == len(hdr) for r in data)
    and all(all(v != "" for v in r) for r in data)
    and len(data) == len(FIXTURES) * len(CONFIGS)
)
print("r2_manifest_header_count = %d" % len(hdr))
print("r2_manifest_row_count = %d" % len(data))
print("r2_manifest_all_row_field_counts = %s" %
      ("all %d rows have exactly %d fields" % (len(data), len(hdr))
       if all(len(r) == len(hdr) for r in data) else "MISMATCH"))
print("r2_manifest_schema_valid = %s" % schema_ok)
if not schema_ok:
    print("GATE_SPECIFIC_BLOCKER = manifest schema invalid; no solver executed")
    sys.exit(1)
with open(MANIFEST_PATH, "r", newline="", encoding="ascii") as fh:
    dr = csv.DictReader(fh)
    for rec in dr:
        assert None not in rec and None not in rec.values(), "extra/missing field"

# ---------------- steps 5-6: hash exact bytes, log ----------------
man_hash = hashlib.sha256(open(MANIFEST_PATH, "rb").read()).hexdigest()
har_hash = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
print("r2_manifest_sha256 = " + man_hash)
print("r2_harness_sha256 = " + har_hash)

# ---------------- step 7: pre-execution custody record ----------------
custody = (
    "# p_konum_plus - F3 Spline Solver Qualification r2 - Pre-Execution Custody Record\n\n"
    "```text\nartifact_role = pre-execution custody record (Output F)\n"
    "status        = NON-NORMATIVE\ndate          = 2026-09-03\n\n"
    "r2_manifest_path =\np_konum_plus/calibration/f3_spline_solver_qualification_manifest_r2_2026-09-03.csv\n\n"
    "r2_manifest_sha256 =\n" + man_hash + "\n\n"
    "r2_harness_path =\np_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py\n\n"
    "r2_harness_sha256 =\n" + har_hash + "\n\n"
    "r2_manifest_schema_valid = true\n"
    "r2_manifest_header_count = " + str(len(hdr)) + "\n"
    "r2_manifest_row_count = " + str(len(data)) + " (10 fixtures x 3 solver configurations)\n"
    "exact_expansion_trigger_predeclared = true (manifest field expansion_trigger, SOLVER-B rows)\n"
    "stage3_nnls_kkt_required = false (predeclared; code-true reproduction of the defined SOLVER-B configuration)\n\n"
    "declaration =\nthis record is written by the r2 harness AFTER manifest write,\n"
    "schema validation and SHA256 computation, and BEFORE the first synthetic\n"
    "solver case is executed. No qualification result may edit the manifest.\n\n"
    "original_run_status = HISTORICAL_SUPERSEDED_FOR_EXTERNAL_ACCEPTANCE_ONLY\n"
    "original_manifest_sha256 =\n522d35086a93b29190c733ab0eba2cedc843298e57de3cea928e3ebe91b44883\n"
    "original_harness_sha256 =\necda07d0fee36d8988c82c31aeb8e231b812e7a4df400af9c6a80676e4cf5917\n\n"
    "SSA_access = false\nP01_P02_real_fit = false\ncommit = false\n```\n"
)
with open(CUSTODY_PATH, "w", newline="\n", encoding="ascii") as fh:
    fh.write(custody)
print("PRE_EXECUTION_CUSTODY_RECORD_WRITTEN = true")
print("MANIFEST_WRITTEN_BEFORE_EXECUTION = true")

# ---------------- step 8: execution ----------------
def build_case(fid):
    for f in FIXTURES:
        if f[0] == fid:
            _, _, kind, sigma, seed, mrule, mask = f
            raw = raw_of(kind)
            if seed is not None and sigma > 0:
                rng = np.random.Generator(np.random.PCG64(seed))
                raw = raw + sigma * rng.standard_normal(T)
            return zddof0(raw), MASKS[mask], fixture_mode(mrule, kind)
    raise KeyError(fid)

def rss_of(c, z, O):
    r = B[O] @ c - z[O]
    return float(r @ r)

def gradf(c, z, O):
    return 2.0 * (B[O].T @ (B[O] @ c - z[O]))

def maxviol(A, c):
    return float(max(0.0, -np.min(A @ c)))

def kkt_res(c, z, O, A):
    act = np.where(np.abs(A @ c) <= REF_ACT_TOL)[0]
    g = gradf(c, z, O)
    if act.size:
        _, res = nnls(A[act].T, g)
        return float(res), act
    return float(np.linalg.norm(g)), act

def accept(c, z, O, A):
    if not np.all(np.isfinite(c)):
        return False
    if maxviol(A, c) > FEAS_TOL:
        return False
    res, _ = kkt_res(c, z, O, A)
    return res <= KKT_TOL

def reference(z, O, A):
    BO = B[O]
    H = BO.T @ BO
    b = BO.T @ z[O]
    L = np.linalg.cholesky(H)
    w = np.linalg.solve(L, b)
    G = np.linalg.solve(L, A.T)
    lam, _ = nnls(G, -w)
    cref = np.linalg.solve(H, b + A.T @ lam)
    viol = maxviol(A, cref)
    res, act = kkt_res(cref, z, O, A)
    rank = int(np.linalg.matrix_rank(A[act])) if act.size else 0
    feas_pass = viol <= FEAS_TOL
    kkt_pass = res <= KKT_TOL
    return cref, dict(viol=viol, act_n=int(act.size), act_rank=rank, res=res,
                      feas_pass=feas_pass, kkt_pass=kkt_pass,
                      certified=bool(feas_pass and kkt_pass))

def run_slsqp(z, O, A):
    r = minimize(lambda c: rss_of(c, z, O), np.zeros(NBASIS),
                 jac=lambda c: gradf(c, z, O), method="SLSQP",
                 constraints=[{"type": "ineq", "fun": lambda c: A @ c,
                               "jac": lambda c: A}], options=SLSQP_OPTS)
    ok = bool(r.success) and np.all(np.isfinite(r.x)) and np.isfinite(r.fun)
    return r.x, ok

def run_tc(z, O, A):
    BO = B[O]
    H2 = 2.0 * (BO.T @ BO)
    r = minimize(lambda c: rss_of(c, z, O), np.zeros(NBASIS),
                 jac=lambda c: gradf(c, z, O), hess=lambda c: H2,
                 method="trust-constr", constraints=[LinearConstraint(A, 0.0, np.inf)],
                 options=TC_OPTS)
    ok = r.status in (1, 2) and np.all(np.isfinite(r.x)) and np.isfinite(r.fun)
    return r.x, ok

def polish(c_tc, z, O, A, tol):
    act = np.where(np.abs(A @ c_tc) <= tol)[0]
    BO = B[O]
    H2 = 2.0 * (BO.T @ BO)
    b2 = 2.0 * (BO.T @ z[O])
    if act.size == 0:
        return np.linalg.lstsq(H2, b2, rcond=None)[0]
    Aa = A[act]
    K = np.block([[H2, Aa.T], [Aa, np.zeros((act.size, act.size))]])
    rhs = np.concatenate([b2, np.zeros(act.size)])
    return np.linalg.lstsq(K, rhs, rcond=None)[0][:NBASIS]

def solver_config(name, z, O, A):
    tel = dict(stage1_accept="NOT_APPLICABLE", expansion_triggered="NOT_APPLICABLE",
               stage2_accept="NOT_APPLICABLE", fallback_invoked="False",
               fallback_status="NOT_INVOKED")
    if name == "SOLVER-A":
        c, ok = run_slsqp(z, O, A)
        tel["primary_status"] = str(ok)
        if ok and maxviol(A, c) <= FEAS_TOL:
            tel["final_endpoint_source"] = "PRIMARY"
        else:
            c, okf = run_tc(z, O, A)
            tel.update(fallback_invoked="True", fallback_status=str(okf),
                       final_endpoint_source="FALLBACK")
    elif name == "SOLVER-C":
        c, ok = run_tc(z, O, A)
        tel["primary_status"] = str(ok)
        tel["final_endpoint_source"] = "PRIMARY"
    else:  # SOLVER-B
        c_tc, ok0 = run_tc(z, O, A)
        tel["primary_status"] = str(ok0)
        c1 = polish(c_tc, z, O, A, POLISH_TOL)
        ok1 = accept(c1, z, O, A)
        tel["stage1_accept"] = str(ok1)
        if ok1:
            tel.update(expansion_triggered="False", final_endpoint_source="POLISH")
            c = c1
        else:
            tel["expansion_triggered"] = "True"
            c2 = polish(c_tc, z, O, A, EXPAND_TOL)
            ok2 = accept(c2, z, O, A)
            tel["stage2_accept"] = str(ok2)
            if ok2:
                tel["final_endpoint_source"] = "POLISH_EXPANDED"
                c = c2
            else:
                cf, okf = run_slsqp(z, O, A)
                s3 = okf and maxviol(A, cf) <= FEAS_TOL
                tel.update(fallback_invoked="True", fallback_status=str(bool(s3)),
                           final_endpoint_source="FALLBACK")
                c = cf
        if tel["expansion_triggered"] == "False":
            tel["stage2_accept"] = "NOT_REACHED"
    return c, tel

RES_HEADER = [
    "manifest_sha256", "harness_sha256", "fixture_id", "solver_configuration",
    "final_endpoint_source", "primary_status", "stage1_accept", "expansion_triggered",
    "stage2_accept", "fallback_invoked", "fallback_status",
    "RSS_ref", "RSS_solver", "absolute_objective_error", "mode_tolerance",
    "kappa_solver", "error_to_tolerance_ratio", "max_constraint_violation",
    "objective_accuracy_pass", "feasibility_pass",
    "reference_max_constraint_violation", "reference_active_constraint_count",
    "reference_active_constraint_rank", "reference_kkt_stationarity_residual",
    "reference_primal_feasibility_pass", "reference_kkt_existence_pass",
    "reference_certified", "semantic_repeatability_pass", "case_acceptance_pass",
]
res_rows = []
suite = {c: True for c in CONFIGS}
ref_all = True
repeat_all = True
print("")
print("case  cfg       endpoint         RSS_ref            abs_err    err/tol  viol      case_pass")
for fid, *_ in [(f[0],) for f in FIXTURES]:
    z, O, m = build_case(fid)
    A = amat(m)
    cref, cert = reference(z, O, A)
    cref2, _ = reference(z, O, A)
    rss_ref = rss_of(cref, z, O)
    ref_repeat = repr(rss_of(cref2, z, O)) == repr(rss_ref)
    repeat_all &= ref_repeat
    ref_all &= cert["certified"]
    tol_q = 1e-12 + 1e-9 * abs(rss_ref)
    for cfg in CONFIGS:
        c, tel = solver_config(cfg, z, O, A)
        c2, _ = solver_config(cfg, z, O, A)
        rss_s = rss_of(c, z, O)
        rep_ok = repr(rss_of(c2, z, O)) == repr(rss_s) and ref_repeat
        repeat_all &= rep_ok
        err = abs(rss_s - rss_ref)
        viol = maxviol(A, c)
        obj_pass = err <= KAPPA * tol_q
        feas_pass = viol <= FEAS_TOL
        case_pass = cert["certified"] and obj_pass and feas_pass
        suite[cfg] &= case_pass
        res_rows.append([
            man_hash, har_hash, fid, cfg, tel["final_endpoint_source"],
            tel["primary_status"], tel["stage1_accept"], tel["expansion_triggered"],
            tel["stage2_accept"], tel["fallback_invoked"], tel["fallback_status"],
            repr(rss_ref), repr(rss_s), repr(err), repr(tol_q), repr(KAPPA),
            repr(err / (KAPPA * tol_q)), repr(viol), str(obj_pass), str(feas_pass),
            repr(cert["viol"]), str(cert["act_n"]), str(cert["act_rank"]),
            repr(cert["res"]), str(cert["feas_pass"]), str(cert["kkt_pass"]),
            str(cert["certified"]), str(rep_ok), str(case_pass),
        ])
        print("%s  %-8s %-16s %.12e  %.2e  %7.3f  %.2e  %s" % (
            fid, cfg, tel["final_endpoint_source"], rss_ref, err,
            err / (KAPPA * tol_q), viol, case_pass))
with open(RESULTS_PATH, "w", newline="", encoding="ascii") as fh:
    w = csv.writer(fh, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    w.writerow(RES_HEADER)
    w.writerows(res_rows)
print("")
print("reference_certification_all = %s" % ref_all)
print("semantic_repeatability_all = %s" % repeat_all)
for cfg in CONFIGS:
    print("qualification_pass[%s] = %s" % (cfg, suite[cfg]))
res_hash = hashlib.sha256(open(RESULTS_PATH, "rb").read()).hexdigest()
print("r2_results_sha256 = " + res_hash)
print("r2_results_rows = %d" % len(res_rows))
