"""F3 STEP 1 r1 - synthetic-only spline solver qualification harness.

Custody order: (1) construct full fixture manifest, (2) serialize deterministically,
(3) SHA256, (4) print hash, (5) only then execute solver qualification.
No F1/SSA data, no P-01/P-02 fitting, no candidate comparison.
"""
from __future__ import annotations
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import hashlib
import time
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import minimize, nnls, LinearConstraint
from scipy.linalg import cho_factor, cho_solve

REPO = "G:/PycharmProjects/pkp-worktree"
MANIFEST_PATH = REPO + "/p_konum_plus/calibration/f3_spline_solver_qualification_manifest_2026-09-02.csv"

# ---------------- frozen-for-this-run literals (predeclared) ----------------
T = 146
U = np.linspace(0.0, 1.0, T)
DEG = 3
KNOTS = np.array([0.0, 0.0, 0.0, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0, 1.0, 1.0])
NBASIS = 8
KAPPA = 0.1
FEAS_TOL = 1e-8            # spline_feasibility_acceptance_tol
ACT_TOL = 1e-8             # active_set_identification_tol
ACT_TOL_EXPAND = 1e-6      # single predeclared expansion step for SOLVER-B polish
KKT_TOL = 1e-8             # spline_kkt_stationarity_tol
TC_OPTS = dict(gtol=1e-10, xtol=1e-14, barrier_tol=1e-12, maxiter=1000)
SLSQP_OPTS = dict(ftol=1e-12, maxiter=500)

B = BSpline.design_matrix(U, KNOTS, DEG).toarray()
assert B.shape == (T, NBASIS)
assert np.allclose(B.sum(axis=1), 1.0, atol=1e-12), "partition of unity failed"

D1 = np.zeros((T - 1, T))
for t in range(T - 1):
    D1[t, t] = -1.0
    D1[t, t + 1] = 1.0

def amat(mode_idx: int) -> np.ndarray:
    s = np.ones(T - 1)
    s[mode_idx:] = -1.0          # t < mode: rise (+diff>=0); t >= mode: fall (-diff>=0)
    return (s[:, None] * D1) @ B  # (145, 8), orientation A c >= 0

def zddof0(v: np.ndarray) -> np.ndarray:
    sd = v.std(ddof=0)
    return (v - v.mean()) / sd

# ---------------- fixture constructions (all literals predeclared) ----------------
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

def raw_of(kind):
    if kind == "spline_c_int":
        return B @ C_INT
    if kind == "spline_c_dec":
        return B @ C_DEC
    if kind == "spline_c_inc":
        return B @ C_INC
    if kind == "spline_c_right":
        return B @ C_RIGHT
    if kind == "analytic_bump":
        return bump(U)
    raise ValueError(kind)

def modeidx_of(kind):
    q = raw_of(kind)
    return int(np.argmax(q))  # deterministic; smallest index on exact tie via argmax

FIXTURES = [
    # id, class, kind, sigma, seed, mode_rule, mask
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

def fixture_mode(mode_rule, kind):
    if mode_rule.startswith("fixed:"):
        return int(mode_rule.split(":")[1])
    return modeidx_of(kind)

# ---------------- phase 1: manifest ----------------
hdr = ("fixture_id,fixture_class,construction_rule,coefficients_or_parameters,"
       "noise_rule,noise_sigma,noise_seed,standardization_rule,mode_idx,mask_context,"
       "observed_index_rule,tested_solver_configurations,fallback_rule,"
       "reference_construction_rule,reference_certificate_method,"
       "constraint_orientation_convention,kappa_solver,mode_tol_rule,"
       "spline_feasibility_acceptance_tol,active_set_identification_tol,"
       "active_set_expansion_tol,spline_kkt_stationarity_tol,acceptance_rule")
rows = [hdr]
coef_map = {"spline_c_int": C_INT, "spline_c_dec": C_DEC, "spline_c_inc": C_INC,
            "spline_c_right": C_RIGHT}
maskrule = {"full": "all 146 indices", "interior_mask": "[0.58)+[87.146)",
            "left_edge_mask": "[15.146)", "right_edge_mask": "[0.131)"}
for fid, fcls, kind, sigma, seed, mrule, mask in FIXTURES:
    coefs = ("c=" + " ".join(repr(float(x)) for x in coef_map[kind])) if kind in coef_map \
        else "bump: exp(-(((u-0.55)/0.12)^2))"
    m = fixture_mode(mrule, kind)
    rows.append(",".join([
        fid, fcls,
        "z=z_ddof0(raw+noise); raw=B@c (clamped cubic; knots 0^4 .2 .4 .6 .8 1^4)"
        if kind in coef_map else "z=z_ddof0(raw+noise); raw=analytic bump on u-grid",
        '"' + coefs + '"',
        "none" if seed is None else "PCG64(seed) standard normal * sigma added to raw pre-standardization",
        repr(float(sigma)), "none" if seed is None else str(seed),
        "z_ddof0 (mean 0; ddof=0 sd 1)", str(m), mask, '"' + maskrule[mask] + '"',
        "SOLVER-A(SLSQP primary; trust-constr fallback);SOLVER-B(trust-constr primary; "
        "active-set equality-KKT post-polish tol 1e-8 with single expansion to 1e-6; "
        "SLSQP fallback);SOLVER-C(trust-constr only)",
        "fallback endpoint subject to identical criteria",
        "dual-NNLS convex QP: lambda*=NNLS(G[,] -w); G=L^-1 A^T; w=L^-1 b; H=B_O^T B_O=LL^T; "
        "c_ref=H^-1(b+A^T lambda*)",
        "NNLS existence certificate",
        "A c >= 0 ; lambda >= 0", repr(KAPPA),
        "mode_tol=1e-12+1e-9*abs(RSS_ref); accept |RSS_solver-RSS_ref|<=kappa*mode_tol",
        repr(FEAS_TOL), repr(ACT_TOL), repr(ACT_TOL_EXPAND), repr(KKT_TOL),
        "ALL cases must pass objective-accuracy AND feasibility; no averaging",
    ]))
manifest_text = "\n".join(rows) + "\n"
with open(MANIFEST_PATH, "w", newline="\n", encoding="ascii") as f:
    f.write(manifest_text)
man_hash = hashlib.sha256(manifest_text.encode("ascii")).hexdigest()
print("MANIFEST_WRITTEN_BEFORE_EXECUTION = true")
print("qualification_suite_manifest_sha256 = " + man_hash)

# ---------------- phase 2: execution ----------------
def build_case(fid):
    for f in FIXTURES:
        if f[0] == fid:
            _, fcls, kind, sigma, seed, mrule, mask = f
            raw = raw_of(kind)
            if seed is not None and sigma > 0:
                rng = np.random.Generator(np.random.PCG64(seed))
                raw = raw + sigma * rng.standard_normal(T)
            z = zddof0(raw)
            O = MASKS[mask]
            m = fixture_mode(mrule, kind)
            return z, O, m
    raise KeyError(fid)

def rss_of(c, z, O):
    r = B[O] @ c - z[O]
    return float(r @ r)

def gradf(c, z, O):
    return 2.0 * (B[O].T @ (B[O] @ c - z[O]))

def maxviol(A, c):
    return float(max(0.0, -np.min(A @ c)))

def reference(z, O, A):
    BO = B[O]
    H = BO.T @ BO
    b = BO.T @ z[O]
    L = np.linalg.cholesky(H)
    w = np.linalg.solve(L, b)
    G = np.linalg.solve(L, A.T)          # 8 x 145 = L^-1 A^T
    lam, _ = nnls(G, -w)
    cref = cho_solve((L, True), b + A.T @ lam)
    # certification
    Ac = A @ cref
    feas_viol = float(max(0.0, -np.min(Ac)))
    act = np.where(np.abs(Ac) <= ACT_TOL)[0]
    g = gradf(cref, z, O)
    if act.size:
        lam2, res = nnls(A[act].T, g)
        rank = int(np.linalg.matrix_rank(A[act]))
    else:
        res = float(np.linalg.norm(g))
        rank = 0
    certified = (feas_viol <= FEAS_TOL) and (res <= KKT_TOL)
    return cref, dict(ref_viol=feas_viol, act_n=int(act.size), act_rank=rank,
                      kkt_res=float(res), feas_pass=feas_viol <= FEAS_TOL,
                      kkt_pass=res <= KKT_TOL, certified=bool(certified))

def run_slsqp(z, O, A, x0):
    r = minimize(lambda c: rss_of(c, z, O), x0, jac=lambda c: gradf(c, z, O),
                 method="SLSQP",
                 constraints=[{"type": "ineq", "fun": lambda c: A @ c,
                               "jac": lambda c: A}],
                 options=SLSQP_OPTS)
    ok = bool(r.success) and np.all(np.isfinite(r.x)) and np.isfinite(r.fun)
    return r.x, ok

def run_tc(z, O, A, x0):
    BO = B[O]
    H2 = 2.0 * (BO.T @ BO)
    r = minimize(lambda c: rss_of(c, z, O), x0, jac=lambda c: gradf(c, z, O),
                 hess=lambda c: H2, method="trust-constr",
                 constraints=[LinearConstraint(A, 0.0, np.inf)], options=TC_OPTS)
    ok = r.status in (1, 2) and np.all(np.isfinite(r.x)) and np.isfinite(r.fun)
    return r.x, ok

def polish(c_in, z, O, A, tol):
    Ac = A @ c_in
    act = np.where(np.abs(Ac) <= tol)[0]
    BO = B[O]
    H2 = 2.0 * (BO.T @ BO)
    b2 = 2.0 * (BO.T @ z[O])
    n = NBASIS
    if act.size == 0:
        cp = np.linalg.lstsq(H2, b2, rcond=None)[0]
    else:
        Aa = A[act]
        K = np.block([[H2, Aa.T], [Aa, np.zeros((act.size, act.size))]])
        rhs = np.concatenate([b2, np.zeros(act.size)])
        sol = np.linalg.lstsq(K, rhs, rcond=None)[0]
        cp = sol[:n]
    # acceptance: primal feasibility + NNLS KKT existence at cp
    viol = maxviol(A, cp)
    Acp = A @ cp
    act2 = np.where(np.abs(Acp) <= ACT_TOL)[0]
    g = gradf(cp, z, O)
    if act2.size:
        _, res = nnls(A[act2].T, g)
    else:
        res = float(np.linalg.norm(g))
    ok = (viol <= FEAS_TOL) and (res <= KKT_TOL) and np.all(np.isfinite(cp))
    return cp, ok, float(res)

def solver_config(name, z, O, A):
    x0 = np.zeros(NBASIS)  # feasible: A@0 = 0 >= 0
    src = "PRIMARY"
    fb = False
    kkt_pass = None
    if name == "SOLVER-A":
        c, ok = run_slsqp(z, O, A, x0)
        if not (ok and maxviol(A, c) <= FEAS_TOL):
            c, ok = run_tc(z, O, A, x0)
            src, fb = "FALLBACK", True
    elif name == "SOLVER-C":
        c, ok = run_tc(z, O, A, x0)
    elif name == "SOLVER-B":
        c1, ok1 = run_tc(z, O, A, x0)
        cp, okp, kres = polish(c1, z, O, A, ACT_TOL)
        if okp:
            c, src, kkt_pass = cp, "POLISH", True
        else:
            cp, okp, kres = polish(c1, z, O, A, ACT_TOL_EXPAND)
            if okp:
                c, src, kkt_pass = cp, "POLISH_EXPANDED", True
            else:
                c, okf = run_slsqp(z, O, A, x0)
                src, fb, kkt_pass = "FALLBACK", True, False
    else:
        raise ValueError(name)
    return c, src, fb, kkt_pass

print("")
print("case  cfg       endpoint         RSS_ref            abs_err    err/tol  viol      A-pass B-pass ref_cert(actN,rank,kkt)")
summary = {s: True for s in ("SOLVER-A", "SOLVER-B", "SOLVER-C")}
ref_cert_all = True
repeat_ok = True
for fid, *_ in [(f[0],) for f in FIXTURES]:
    z, O, m = build_case(fid)
    A = amat(m)
    cref, cert = reference(z, O, A)
    rss_ref = rss_of(cref, z, O)
    # semantic repeatability of reference
    cref2, _ = reference(z, O, A)
    if repr(rss_of(cref2, z, O)) != repr(rss_ref):
        repeat_ok = False
    ref_cert_all &= cert["certified"]
    tol_q = 1e-12 + 1e-9 * abs(rss_ref)
    for cfg in ("SOLVER-A", "SOLVER-B", "SOLVER-C"):
        c, src, fb, _ = solver_config(cfg, z, O, A)
        c2, _, _, _ = solver_config(cfg, z, O, A)
        if repr(rss_of(c2, z, O)) != repr(rss_of(c, z, O)):
            repeat_ok = False
        rss_s = rss_of(c, z, O)
        err = abs(rss_s - rss_ref)
        viol = maxviol(A, c)
        a_pass = err <= KAPPA * tol_q
        b_pass = viol <= FEAS_TOL
        summary[cfg] &= (a_pass and b_pass)
        print("%s  %-8s %-16s %.12e  %.2e  %7.3f  %.2e  %-5s  %-5s  %s(%d,%d,%.1e)" % (
            fid, cfg, src, rss_ref, err, err / (KAPPA * tol_q), viol,
            a_pass, b_pass, cert["certified"], cert["act_n"], cert["act_rank"],
            cert["kkt_res"]))
print("")
print("reference_certification_all = %s" % ref_cert_all)
print("semantic_repeatability_all = %s" % repeat_ok)
for cfg in ("SOLVER-A", "SOLVER-B", "SOLVER-C"):
    print("qualification_pass[%s] = %s" % (cfg, summary[cfg]))
print("")
print("W_s check: 3 - s_side_min(1) = " + repr(3.0 - 0.01569377976942823))
sm1 = (5.0 / 145.0) / (np.log(10.0) - np.log(10.0 / 9.0))
print("s_side_min(1) recomputed    = " + repr(float(sm1)))
print("structural count 906*146*8  = " + str(906 * 146 * 8))
