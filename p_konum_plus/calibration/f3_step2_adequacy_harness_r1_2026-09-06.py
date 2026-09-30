"""F3 STEP-2 adequacy-evaluation harness r1 (2026-09-06).

CLASS_C implementation of the frozen F3 STEP-1 contract (r4 5e594136... AS
RATIFIED BY freeze record r1 7055f186...) on predeclared synthetic fixtures
only. PATH_COVERAGE_ONLY: no adequacy evidence, no generator selection; the
D-P04 result is `mechanism_outcome`, never a winner.

Engines are REUSED, never re-implemented:
  PIN-F2-LOADER     : frozen F2 r3 engine (01714752...) loaded via importlib
                      (file is __main__-guarded); hash verified before load.
  PIN-SPLINE-LOADER : qualified SOLVER-B (b31e5a6b...) loaded by a
                      definition-only AST loader (see load_spline_ns).

A.5 condition (i) has no exact frozen data-level definition
(F3-STEP2-EXACT-01): the C4a determination on real fixtures returns
STOP_EXACTNESS_PENDING; no partial A.5 rule is put in force.
"""
from __future__ import annotations
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"                                    # PIN-THREADS
import ast
import csv
import hashlib
import importlib.util
import json
import math
import platform
import sys
from contextlib import contextmanager
from fractions import Fraction

import numpy as np
import scipy

REPO = "G:/PycharmProjects/pkp-worktree"
os.chdir(REPO)

OPENED_FILES = []


def sha256_of(path):
    OPENED_FILES.append(path)
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ------------------------- ratified literals (read-only) -------------------
C_COV = 0.90; C_COMPLETE = 0.90; C_IDENT = 0.85; C_STAB = 0.10
DELTA_2 = 0.05; DELTA_3 = 0.05; DELTA_4_RMSE = 0.10
TAU = dict(C1=0.01, C2=0.005, C3=0.01, C4a=0.01, C4b=0.02, C5=0.01, C6=0.0)
E_MASK = 15; K_FOLDS = 5; T = 146; DF_SPLINE = 8; K_F = 4
FOLD_BOUNDS = [0, 29, 58, 87, 116, 146]
LEFT_PROBE_O = np.arange(15, 146)          # LEFT mask = indices [0,15) masked
RIGHT_PROBE_O = np.arange(0, 131)          # RIGHT mask = indices [131,146) masked
FULL_O = np.arange(146)
W_C5 = {"P-01": [3.0, 3.0, 123.43902548550072, 123.43902548550072],
        "P-02": [3.0, 2.9843062202305717, 2.9843062202305717, 5.0]}

F2_PATH = "p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py"
F2_HASH = "01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077"
SPL_PATH = "p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py"
SPL_HASH = "b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d"
SPL_RESULTS_PATH = "p_konum_plus/calibration/f3_spline_solver_qualification_results_r2_2026-09-03.csv"
F2_TELEMETRY_PATH = "p_konum_plus/calibration/f2_step2_feasibility_telemetry_r3_2026-09-01.csv"
F2_NR_HASH = "6f197b74e3d42248393e5534efd25ef937d394d7fa50c7bcb81558cfcddd5403"

MANIFEST_PATH = "p_konum_plus/calibration/f3_step2_fixture_manifest_2026-09-06.csv"
TELEMETRY_PATH = "p_konum_plus/calibration/f3_step2_telemetry_r1_2026-09-06.csv"
RESULTS_PATH = "p_konum_plus/calibration/f3_step2_results_r1_2026-09-06.json"

FORBIDDEN_RESULT_KEYS = ("winner", "selected", "generator_selected")


# ------------------------- PIN-F2-LOADER -----------------------------------
def load_f2():
    h = sha256_of(F2_PATH)
    assert h == F2_HASH, "PIN-F2-IMPORT-HASH FAIL: " + h
    spec = importlib.util.spec_from_file_location("f2eng", F2_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # __main__-guarded: suite does not run
    return mod, h


# ------------------------- PIN-SPLINE-LOADER -------------------------------
RETAINED_CLASSES = (ast.Import, ast.ImportFrom, ast.FunctionDef,
                    ast.AsyncFunctionDef, ast.ClassDef)


def _const_assign(node):
    if not isinstance(node, (ast.Assign, ast.AnnAssign)):
        return False
    val = node.value
    def ok(v):
        if isinstance(v, ast.Constant):
            return True
        if isinstance(v, (ast.Tuple, ast.List)):
            return all(ok(e) for e in v.elts)
        if isinstance(v, ast.Dict):
            return all(ok(k) and ok(x) for k, x in zip(v.keys, v.values))
        return False
    return val is not None and ok(val)


def load_spline_ns():
    h = sha256_of(SPL_PATH)
    assert h == SPL_HASH, "PIN-SPLINE-IMPORT-HASH FAIL: " + h
    OPENED_FILES.append(SPL_PATH)
    with open(SPL_PATH, "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    marker = src.index("# ---------------- steps 1-3")
    marker_line = src[:marker].count("\n") + 1
    retained, prelude, excluded = [], [], []
    for node in tree.body:
        seg = ast.get_source_segment(src, node)
        lines = src.splitlines()
        exact = "\n".join(lines[node.lineno - 1:node.end_lineno])
        assert seg is not None and seg in exact, "source-segment mismatch"
        entry = (node, seg)
        if isinstance(node, RETAINED_CLASSES) or _const_assign(node):
            retained.append(entry)
        elif node.end_lineno < marker_line:
            assert "open(" not in seg and "print(" not in seg, \
                "prelude node performs I/O: " + seg[:60]
            prelude.append(entry)              # definitional support state only
        else:
            excluded.append(entry)             # orchestration / file I/O
    ns = {"__name__": "f3spl"}
    for node, seg in sorted(retained + prelude, key=lambda e: e[0].lineno):
        exec(compile(ast.Module(body=[node], type_ignores=[]),
                     SPL_PATH, "exec"), ns)
    names = dict(
        retained=[getattr(n, "name", None) or
                  ",".join(t.id for t in getattr(n, "targets", [])
                           if isinstance(t, ast.Name)) or type(n).__name__
                  for n, _ in retained],
        prelude=[",".join(t.id for t in getattr(n, "targets", [])
                          if isinstance(t, ast.Name)) or type(n).__name__
                 for n, _ in prelude],
        excluded_count=len(excluded),
    )
    for req in ("amat", "rss_of", "zddof0", "solver_config", "reference",
                "build_case", "FIXTURES", "B"):
        assert req in ns, "spline loader missing dependency: " + req
    return ns, h, names


# ------------------------- masked machinery --------------------------------
def make_masked_moax(f2m, obs_idx):
    def moax(family, x_target):
        stable_fn = f2m.p01_stable if family == "P-01" else f2m.p02_stable
        def fun(theta):
            g_stable = stable_fn(theta)
            status, sigma_g, ghat = f2m.zero_variance_rule(g_stable)
            if status != "OK":
                return f2m.L_INVALID_PREDICTION_GUARD
            d = x_target[obs_idx] - ghat[obs_idx]
            return float(np.sum(d * d))
        return fun
    return moax


@contextmanager
def masked_objective(f2m, obs_idx):
    if obs_idx is None or len(obs_idx) == T:      # FULL: frozen path untouched
        yield
        return
    orig = f2m.make_objective_and_x
    f2m.make_objective_and_x = make_masked_moax(f2m, np.asarray(obs_idx))
    try:
        yield
    finally:
        f2m.make_objective_and_x = orig


def masked_internal_L(f2m, x, theta, family, obs_idx):
    theta_arr = np.asarray(theta, dtype=np.float64)
    if not np.all(np.isfinite(theta_arr)):
        return float("inf")
    stable_fn = f2m.p01_stable if family == "P-01" else f2m.p02_stable
    status, sigma_g, ghat = f2m.zero_variance_rule(stable_fn(theta_arr))
    if status != "OK":
        return float("inf")
    d = x[obs_idx] - ghat[obs_idx]
    return float(np.sum(d * d))


def feature_start_masked(f2m, family, x, obs_idx):
    pad = np.full(T, -np.inf)
    pad[obs_idx] = x[obs_idx]
    return f2m.feature_start(family, pad)         # frozen min-index argmax rule


def ghat_of(f2m, family, theta):
    stable_fn = f2m.p01_stable if family == "P-01" else f2m.p02_stable
    status, sigma_g, ghat = f2m.zero_variance_rule(stable_fn(np.asarray(theta)))
    return ghat if status == "OK" else None


# ------------------------- family fit driver -------------------------------
def fit_family(f2m, grids, fixture_id, family, x, obs_idx, telemetry,
               mask_id, inject_fault=False, inject_fs_reject=False):
    obs = np.asarray(obs_idx)
    full = len(obs) == T
    starts = []
    fs, u_star, j_star = feature_start_masked(f2m, family, x, obs)
    fs_valid = all(math.isfinite(float(v)) for v in fs)
    if inject_fs_reject:
        fs_valid = False                          # TEST_ONLY_INJECTION
    if fs_valid:
        starts.append(("feature", fs))
    retained = grids[family]
    for i in f2m.mini_bank_indices(len(retained)):
        starts.append((f"grid{i}", retained[i]))
    records = []
    for sid, x0 in starts:
        with masked_objective(f2m, None if full else obs):
            canonical, cls, tel, ev = f2m.run_one_start(
                fixture_id, family, sid, x0, x,
                fault_inject_primary=inject_fault,
                fault_inject_fallback_nonfinite=inject_fault)
        for row in tel:
            telemetry.append(dict(row, fixture=fixture_id, mask_id=mask_id,
                                  fitter=family))
        L_masked = (masked_internal_L(f2m, x, cls["theta"], family, obs)
                    if cls["eligible"] else float("inf"))
        if cls["eligible"] and not full:
            L_full = f2m.internal_L(x, cls["theta"], family)
            assert L_masked <= L_full + 0.0, \
                "MASKED OBJECTIVE VIOLATION L_O > L_FULL"   # binding assert
        records.append(dict(eligible=cls["eligible"], L=L_masked,
                            theta=cls["theta"],
                            predicates=cls["predicates"]))
    status, best = f2m.aggregate(records)         # frozen tie comparator
    out = dict(eligible=status == "OK",
               feature_start_rejected=not fs_valid,
               failure_codes=sorted({p for r in records for p in r["predicates"]
                                     if not r["eligible"]}) if status != "OK" else [])
    if status == "OK":
        out["theta"] = [float(v) for v in best["theta"]]
        out["L"] = best["L"]
        out["ghat"] = ghat_of(f2m, family, best["theta"])
    return out


# ------------------------- spline fit driver -------------------------------
def spline_valid_from_tel(tel):
    src = tel["final_endpoint_source"]
    if src in ("POLISH", "POLISH_EXPANDED"):
        return True
    if src == "FALLBACK":
        return tel["fallback_status"] == "True"
    return False


SPL_CTX_DONE = [0]


def fit_spline(spl, fixture_id, x, obs_idx, telemetry, mask_id,
               inject_failure=False):
    SPL_CTX_DONE[0] += 1
    print("PROGRESS SPL ctx %d %s %s" % (SPL_CTX_DONE[0], fixture_id, mask_id),
          flush=True)
    if inject_failure:                            # TEST_ONLY_INJECTION
        telemetry.append(dict(fixture=fixture_id, mask_id=mask_id, fitter="SPL",
                              start_id="INJECTED_FAILURE", optimizer_path="none",
                              status="TEST_ONLY_INJECTION", success=False,
                              nit=-1, nfev=-1, njev=-1,
                              wall_clock_seconds=0.0, message="injected"))
        return dict(valid=False, failure="TEST_ONLY_INJECTION_SPLINE_FAILURE")
    obs = np.asarray(obs_idx)
    per_mode = []
    for m in range(T):
        A = spl["amat"](m)
        try:
            c, tel = spl["solver_config"]("SOLVER-B", x, obs, A)
            valid = spline_valid_from_tel(tel)
            src, pst = tel["final_endpoint_source"], tel["primary_status"]
        except RuntimeError as exc:
            # Frozen acceptance rule: an endpoint is acceptable ONLY IF all
            # acceptance conditions are shown to hold; an NNLS non-convergence
            # inside accept() means they cannot be shown => not accepted =>
            # mode numerically invalid. No frozen code modified (ENG note in
            # the report).
            c, valid = None, False
            src, pst = "ACCEPTANCE_UNVERIFIABLE", "EXC:" + type(exc).__name__
        rss = spl["rss_of"](c, x, obs) if valid else float("inf")
        per_mode.append((m, valid, rss, c))
        telemetry.append(dict(fixture=fixture_id, mask_id=mask_id, fitter="SPL",
                              start_id=f"mode{m}",
                              optimizer_path=src,
                              status=pst, success=valid,
                              nit=-1, nfev=-1, njev=-1, wall_clock_seconds=0.0,
                              message="RSS=" + repr(rss)))
    valid_modes = [(m, rss, c) for m, v, rss, c in per_mode if v]
    if not valid_modes:
        return dict(valid=False, failure="NO_VALID_MODE")
    rss_min = min(r for _, r, _ in valid_modes)
    eq = [(m, r, c) for m, r, c in valid_modes
          if abs(r - rss_min) <= 1e-12 + 1e-9 * max(abs(r), abs(rss_min))]
    m_win, rss_win, c_win = min(eq, key=lambda t: t[0])
    q = spl["B"] @ c_win
    sd = q.std(ddof=0)
    if not np.all(np.isfinite(q)) or sd == 0.0:
        return dict(valid=False, failure="ZERO_VARIANCE_OR_NONFINITE")
    return dict(valid=True, mode=m_win, rss=float(rss_win),
                ghat=(q - q.mean()) / sd)


# ------------------------- statistic pins ----------------------------------
def acf_classical(r):                             # PIN-ACF implementation A
    n = len(r)
    s = 0.0
    for t in range(n):
        s = s + float(r[t])
    r_bar = s / float(n)
    num = 0.0
    for t in range(n - 1):
        num = num + (float(r[t]) - r_bar) * (float(r[t + 1]) - r_bar)
    den = 0.0
    for t in range(n):
        den = den + (float(r[t]) - r_bar) * (float(r[t]) - r_bar)
    if den == 0.0:
        return None
    phi = abs(num / den)
    return phi if math.isfinite(phi) else None


def acf_classical_b(r):                           # independent 2nd implementation
    n = len(r); i = 0; acc = 0.0
    while i < n:
        acc += float(r[i]); i += 1
    mean_v = acc / float(n)
    i = 0; num = 0.0
    while i < n - 1:
        num += (float(r[i]) - mean_v) * (float(r[i + 1]) - mean_v); i += 1
    i = 0; den = 0.0
    while i < n:
        den += (float(r[i]) - mean_v) * (float(r[i]) - mean_v); i += 1
    if den == 0.0:
        return None
    phi = abs(num / den)
    return phi if math.isfinite(phi) else None


def acf_alt_c(r):                                 # alternative (c) - prohibited impl
    return abs(float(np.corrcoef(np.asarray(r)[:-1], np.asarray(r)[1:])[0, 1]))


def acf_frac_ulp(r, phi):                         # informational exact-rational check
    fr = [Fraction(float(v)) for v in r]
    n = len(fr)
    rb = sum(fr, Fraction(0)) / n
    a = [v - rb for v in fr]
    num = sum((a[t] * a[t + 1] for t in range(n - 1)), Fraction(0))
    den = sum((v * v for v in a), Fraction(0))
    if den == 0:
        return None
    exact = abs(num / den)
    fx = float(exact)
    return abs(fx - phi) / math.ulp(phi) if phi != 0 else 0.0


def acf_verify(vectors):
    out = []
    for name, r in vectors:
        pa, pb = acf_classical(r), acf_classical_b(r)
        rec = dict(vector=name,
                   bitwise_equal=(pa is None and pb is None) or
                                 (pa is not None and pb is not None and
                                  pa.hex() == pb.hex()),
                   undefined=pa is None)
        if pa is not None:
            alt_c = acf_alt_c(r)
            alt_b = pa * 146.0 / 145.0
            rec.update(phi=pa.hex(),
                       strict_vs_alt_c=bool(pa != alt_c),
                       strict_vs_alt_b=bool(pa != alt_b),
                       ulp_dev_vs_exact=acf_frac_ulp(r, pa))
        out.append(rec)
    return out


def rho_cv_pin(z, ghat_cv):                       # PIN-RHOCV
    return float(np.corrcoef(z, ghat_cv)[0, 1])


def rmse_edge_pin(probe_pred, ref_pred, edge_idx):  # PIN-RMSE-EDGE
    d = probe_pred[edge_idx] - ref_pred[edge_idx]
    return float(np.sqrt(np.sum(d * d) / float(E_MASK)))


def s_stab_pin(thetas, family):                   # PIN-SSTAB-W
    arr = np.asarray(thetas, dtype=np.float64)    # (5, 4)
    q = np.quantile(arr, [0.25, 0.75], axis=0, method="linear")
    iqr = q[1] - q[0]
    return float(np.max(iqr / np.asarray(W_C5[family])))


def median_pin(vals):                             # PIN-MEDIAN
    return float(np.median(np.asarray(vals, dtype=np.float64)))


# ------------------------- evaluation layer --------------------------------
SEXES = ("F", "M")
FAM_KEYS = {"P-01": "P01", "P-02": "P02"}
DIRECTION = dict(C1="higher", C2="higher", C3="lower", C4a="higher",
                 C4b="lower", C5="lower", C6="lower")
WORSE_SEX = dict(higher=min, lower=max)


def crit_stats(recs, n_s):
    """recs: per-fitter dict of per-trajectory lists (generator grammar)."""
    def med_over(vals, idxs):
        sel = [vals[i] for i in idxs]
        return median_pin(sel) if sel else None
    out = {}
    for fk in ("P01", "P02", "SPL"):
        d = recs[fk]
        cov = sum(1 for b in d["full"] if b) / n_s
        cc_idx = [i for i in range(n_s) if d["cc"][i] and d["rho"][i] is not None]
        phi_idx = [i for i in range(n_s) if d["full"][i] and d["phi"][i] is not None]
        probes_ok = [i for i in range(n_s) if d["pL"][i] and d["pR"][i]
                     and d["rL"][i] is not None and d["rR"][i] is not None]
        ident = (sum(1 for i in range(n_s) if d["pL"][i]) +
                 sum(1 for i in range(n_s) if d["pR"][i])) / (2.0 * n_s)
        sst_idx = [i for i in range(n_s) if d["cc"][i] and d["sst"][i] is not None]
        out[fk] = dict(cov=cov, cc_idx=cc_idx, phi_idx=phi_idx,
                       probes_idx=probes_ok, ident=ident, sst_idx=sst_idx,
                       med_over=med_over, d=d)
    return out


def evaluate_fixture(fx_id, strata, n_s, c4_source, flags, stops):
    """strata: sex -> fitter grammar dicts. Returns evaluation dict."""
    ev = dict(fixture_id=fx_id, interpretation="PATH_COVERAGE_ONLY",
              c4_source=c4_source, sexes={}, criteria={}, dp04=None,
              mechanism_outcome=None)
    S = {sx: crit_stats(strata[sx], n_s) for sx in SEXES}
    fam_pass, fam_detail = {}, {}
    for fam in ("P01", "P02"):
        detail, passed, pending = {}, True, False
        for crit in ("C1", "C2", "C3", "C4a", "C4b", "C5", "C6"):
            per_sex = {}
            for sx in SEXES:
                st, sp = S[sx][fam], S[sx]["SPL"]
                d, dS = st["d"], sp["d"]
                if crit == "C1":
                    val, thr, ok = st["cov"], C_COV, st["cov"] >= C_COV
                elif crit == "C2":
                    V2 = [i for i in st["cc_idx"] if i in sp["cc_idx"]]
                    mf = st["med_over"](d["rho"], V2)
                    ms = sp["med_over"](dS["rho"], V2)
                    share = len(V2) / n_s
                    ok = (mf is not None and ms is not None and
                          mf >= ms - DELTA_2 and share >= C_COMPLETE)
                    val, thr = mf, (None if ms is None else ms - DELTA_2)
                    per_sex[sx] = dict(stat=val, threshold_FIXTURE_ONLY=thr,
                                       share=share, n_valid=len(V2),
                                       spline_stat=ms, passed=bool(ok),
                                       undefined=mf is None)
                    continue
                elif crit == "C3":
                    V3 = [i for i in st["phi_idx"] if i in sp["phi_idx"]]
                    mf = st["med_over"]([abs(v) if v is not None else None
                                         for v in d["phi"]], V3)
                    ms = sp["med_over"]([abs(v) if v is not None else None
                                         for v in dS["phi"]], V3)
                    share = len(V3) / n_s
                    ok = (mf is not None and ms is not None and
                          mf <= ms + DELTA_3 and share >= C_COMPLETE)
                    per_sex[sx] = dict(stat=mf, threshold_FIXTURE_ONLY=(
                        None if ms is None else ms + DELTA_3), share=share,
                        n_valid=len(V3), spline_stat=ms, passed=bool(ok),
                        undefined=mf is None)
                    continue
                elif crit == "C4a":
                    if c4_source == "REAL":
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING"
                                                  "(F3-STEP2-EXACT-01)")
                        continue
                    val, thr, ok = st["ident"], C_IDENT, st["ident"] >= C_IDENT
                elif crit == "C4b":
                    if c4_source == "REAL":
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING"
                                                  "(F3-STEP2-EXACT-01)")
                        continue
                    V4 = [i for i in st["probes_idx"] if i in sp["probes_idx"]]
                    r_f = st["med_over"]([max(d["rL"][i], d["rR"][i])
                                          if d["rL"][i] is not None and
                                          d["rR"][i] is not None else None
                                          for i in range(n_s)], V4)
                    r_s = sp["med_over"]([max(dS["rL"][i], dS["rR"][i])
                                          if dS["rL"][i] is not None and
                                          dS["rR"][i] is not None else None
                                          for i in range(n_s)], V4)
                    share = len(V4) / n_s
                    c4a_ok = st["ident"] >= C_IDENT
                    if share >= C_COMPLETE:                     # PIN-K05-INVARIANT
                        assert st["ident"] >= C_COMPLETE >= C_IDENT or c4a_ok, \
                            "K-05 INVARIANT VIOLATION"
                    ok = (r_f is not None and r_s is not None and
                          r_f <= r_s + DELTA_4_RMSE and share >= C_COMPLETE
                          and c4a_ok)
                    per_sex[sx] = dict(stat=r_f, spline_stat=r_s,
                                       threshold_FIXTURE_ONLY=(
                                           None if r_s is None
                                           else r_s + DELTA_4_RMSE),
                                       share=share, n_valid=len(V4),
                                       medL=st["med_over"](d["rL"], V4),
                                       medR=st["med_over"](d["rR"], V4),
                                       spline_medL=sp["med_over"](dS["rL"], V4),
                                       spline_medR=sp["med_over"](dS["rR"], V4),
                                       passed=bool(ok), undefined=r_f is None)
                    continue
                elif crit == "C5":
                    mf = st["med_over"](d["sst"], st["sst_idx"])
                    share = len(st["sst_idx"]) / n_s
                    ok = mf is not None and mf <= C_STAB and share >= C_COMPLETE
                    per_sex[sx] = dict(stat=mf, threshold=C_STAB, share=share,
                                       passed=bool(ok), undefined=mf is None)
                    continue
                else:  # C6
                    val, thr, ok = float(K_F), float(DF_SPLINE), K_F <= DF_SPLINE
                per_sex[sx] = dict(stat=val, threshold=thr, passed=bool(ok))
            detail[crit] = per_sex
            statuses = [per_sex[sx].get("status") for sx in SEXES]
            if any(s is not None and "PENDING" in str(s) for s in statuses):
                pending = True
                continue
            crit_ok = all(per_sex[sx]["passed"] for sx in SEXES)
            if passed and not pending and not crit_ok:
                passed = False       # first failed criterion; keep measuring
        fam_detail[fam] = detail
        fam_pass[fam] = ("PENDING" if pending and passed else
                         ("PASS" if passed else "FAIL"))
    ev["criteria"] = fam_detail
    ev["p03"] = dict(fam_pass)
    p1, p2 = fam_pass["P01"], fam_pass["P02"]
    if "PENDING" in (p1, p2):
        ev["mechanism_outcome"] = "PENDING_EXACTNESS(F3-STEP2-EXACT-01)"
    elif p1 == "FAIL" and p2 == "FAIL":
        ev["mechanism_outcome"] = "STOP_BOTH_FAIL_REDESIGN"
        stops.append(dict(fixture=fx_id, stop="BOTH_FAIL_REDESIGN"))
    elif p1 == "PASS" and p2 == "FAIL":
        ev["mechanism_outcome"] = "ONLY_P01_PASSES"
    elif p2 == "PASS" and p1 == "FAIL":
        ev["mechanism_outcome"] = "ONLY_P02_PASSES"
    else:
        ev["dp04"] = run_dp04(fx_id, S, n_s, flags, stops)
        ev["mechanism_outcome"] = ev["dp04"]["mechanism_outcome"]
    # DISC-F3-03 complement sets
    comp = {}
    for sx in SEXES:
        for fam in ("P01", "P02"):
            st, sp = S[sx][fam], S[sx]["SPL"]
            idx = [i for i in sp["cc_idx"] if i not in st["cc_idx"]]
            comp[f"{sx}:{fam}:C2"] = dict(
                size=len(idx),
                spline_stat=sp["med_over"](sp["d"]["rho"], idx))
    ev["disc_f3_03_complement"] = comp
    for k in FORBIDDEN_RESULT_KEYS:               # labelling pin
        assert k not in ev, "forbidden key emitted"
    return ev


def run_dp04(fx_id, S, n_s, flags, stops):
    order = ["C1", "C2", "C3", "C4a", "C4b", "C5", "C6"]
    subsetdef = {"C2", "C3", "C4b", "C5"}
    recompute_counts = {c: 0 for c in order}
    consulted, disclosure = [], []
    outcome, resolved_level = None, None
    for crit in order:
        consulted.append(crit)
        tau = TAU[crit]
        if crit in subsetdef:
            recompute_counts[crit] += 1
            scal, per_sex_disc = {}, {}
            empty_hit = False
            for fam in ("P01", "P02"):
                vals = {}
                for sx in SEXES:
                    st1, st2, sp = S[sx]["P01"], S[sx]["P02"], S[sx]["SPL"]
                    if crit == "C2":
                        U = [i for i in st1["cc_idx"] if i in st2["cc_idx"]
                             and i in sp["cc_idx"]]
                        if flags.get("inject_empty_U2"):
                            U = []                # TEST_ONLY_INJECTION
                        src = S[sx][fam]
                        v = src["med_over"](src["d"]["rho"], U)
                    elif crit == "C3":
                        U = [i for i in st1["phi_idx"] if i in st2["phi_idx"]
                             and i in sp["phi_idx"]]
                        src = S[sx][fam]
                        v = src["med_over"]([abs(x) if x is not None else None
                                             for x in src["d"]["phi"]], U)
                    elif crit == "C4b":
                        U = [i for i in st1["probes_idx"]
                             if i in st2["probes_idx"] and i in sp["probes_idx"]]
                        src = S[sx][fam]
                        dd = src["d"]
                        v = src["med_over"]([max(dd["rL"][i], dd["rR"][i])
                                             if dd["rL"][i] is not None and
                                             dd["rR"][i] is not None else None
                                             for i in range(n_s)], U)
                    else:  # C5
                        U = [i for i in st1["cc_idx"] if i in st2["cc_idx"]]
                        src = S[sx][fam]
                        v = src["med_over"](src["d"]["sst"],
                                            [i for i in U
                                             if src["d"]["sst"][i] is not None])
                    if not U:
                        empty_hit = True
                    vals[sx] = v
                    per_sex_disc.setdefault(sx, dict(U_size=len(U), n_s=n_s,
                                                     share=len(U) / n_s))
                    per_sex_disc[sx][fam] = v
                scal[fam] = WORSE_SEX[DIRECTION[crit]](
                    v for v in vals.values() if v is not None) \
                    if all(v is not None for v in vals.values()) else None
            if empty_hit:
                stops.append(dict(fixture=fx_id,
                                  stop="CONTRACT_VIOLATION_EMPTY_U",
                                  level=crit))
                return dict(consulted_path=consulted,
                            mechanism_outcome="STOP_CONTRACT_VIOLATION_EMPTY_U",
                            disclosure=disclosure,
                            recompute_counts=recompute_counts)
        else:
            scal = {}
            for fam in ("P01", "P02"):
                if crit == "C1":
                    scal[fam] = min(S[sx][fam]["cov"] for sx in SEXES)
                elif crit == "C4a":
                    scal[fam] = min(S[sx][fam]["ident"] for sx in SEXES)
                else:  # C6
                    scal[fam] = float(K_F)
            per_sex_disc = None
        if scal["P01"] is None or scal["P02"] is None:
            return dict(consulted_path=consulted,
                        mechanism_outcome="STOP_UNDEFINED_CONSULTED_SCALAR",
                        disclosure=disclosure,
                        recompute_counts=recompute_counts)
        delta = scal["P01"] - scal["P02"]
        equivalent = abs(delta) <= tau
        block = dict(level=crit, scalars=dict(scal), signed_delta=delta,
                     tau=tau,
                     outcome="EQUIVALENT" if equivalent else "RESOLVED")
        if per_sex_disc is not None:
            block["per_sex"] = per_sex_disc
        disclosure.append(block)
        if not equivalent:
            better_p01 = delta > 0 if DIRECTION[crit] == "higher" else delta < 0
            outcome = ("RESOLVED_MECHANISM_P01" if better_p01
                       else "RESOLVED_MECHANISM_P02")
            resolved_level = crit
            block["resolved_for"] = "P-01" if better_p01 else "P-02"
            break
    if outcome is None:
        outcome = "TERMINAL_FALLBACK_MECHANISM_P01"   # "P-01" < "P-02"
    return dict(consulted_path=consulted, resolved_level=resolved_level,
                mechanism_outcome=outcome, disclosure=disclosure,
                recompute_counts=recompute_counts,
                terminal_fallback=resolved_level is None)


# ------------------------- real-scenario execution -------------------------
def fold_masks():
    out = []
    for b in range(K_FOLDS):
        held = np.arange(FOLD_BOUNDS[b], FOLD_BOUNDS[b + 1])
        train = np.setdiff1d(FULL_O, held)
        out.append((f"fold{b}", train, held))
    return out


def run_real_scenario(f2m, spl, grids, sc, telemetry):
    n_s = len(sc["strata"]["F"])
    injmap = {}
    for i in sc["injections"]:
        injmap.setdefault((i["traj"], i["family"], i["context"]), i["mode"])
    strata_recs = {}
    for sx in SEXES:
        recs = {k: dict(full=[], cc=[], rho=[], phi=[], pL=[], pR=[],
                        rL=[], rR=[], sst=[]) for k in ("P01", "P02", "SPL")}
        for ti, (kind, seed, sigma) in enumerate(sc["strata"][sx]):
            import f3_step2_fixture_generator_r1_2026_09_06 as gen
            x = gen.make_traj(kind, seed, sigma)
            trg = (sx, ti)
            for family in ("P-01", "P-02"):
                fk = FAM_KEYS[family]
                full = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                  FULL_O, telemetry, f"{sx}{ti}:full")
                recs[fk]["full"].append(full["eligible"])
                phi = (acf_classical(x - full["ghat"])
                       if full["eligible"] else None)
                recs[fk]["phi"].append(phi)
                fold_fits, cc = [], True
                pred_cv = np.full(T, np.nan)
                for fname, train, held in fold_masks():
                    inj = injmap.get((trg, family, fname))
                    r = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                   train, telemetry, f"{sx}{ti}:{fname}",
                                   inject_fault=inj == "F2_FAULT_INJECTION",
                                   inject_fs_reject=inj == "TEST_ONLY_INJECTION")
                    fold_fits.append(r)
                    if r["eligible"]:
                        pred_cv[held] = r["ghat"][held]
                    else:
                        cc = False
                recs[fk]["cc"].append(cc)
                recs[fk]["rho"].append(rho_cv_pin(x, pred_cv) if cc else None)
                recs[fk]["sst"].append(
                    s_stab_pin([f["theta"] for f in fold_fits], family)
                    if cc else None)
                for side, obsP, edge in (("L", LEFT_PROBE_O, np.arange(0, 15)),
                                         ("R", RIGHT_PROBE_O,
                                          np.arange(131, 146))):
                    inj = injmap.get((trg, family, "probe" + side))
                    r = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                   obsP, telemetry, f"{sx}{ti}:probe{side}",
                                   inject_fault=inj == "F2_FAULT_INJECTION")
                    fit_ok = r["eligible"] and full["eligible"]
                    recs[fk]["p" + side].append(
                        "STOP_EXACTNESS_PENDING" if fit_ok else False)
                    recs[fk]["r" + side].append(
                        rmse_edge_pin(r["ghat"], full["ghat"], edge)
                        if fit_ok else None)
            # spline
            spf_inj = injmap.get((trg, "SPL", "full")) == "TEST_ONLY_INJECTION"
            spf = fit_spline(spl, sc["fixture_id"], x, FULL_O, telemetry,
                             f"{sx}{ti}:full", inject_failure=spf_inj)
            recs["SPL"]["full"].append(spf["valid"])
            recs["SPL"]["phi"].append(acf_classical(x - spf["ghat"])
                                      if spf["valid"] else None)
            cc, pred_cv = True, np.full(T, np.nan)
            for fname, train, held in fold_masks():
                inj = injmap.get((trg, "SPL", fname)) == "TEST_ONLY_INJECTION"
                r = fit_spline(spl, sc["fixture_id"], x, train, telemetry,
                               f"{sx}{ti}:{fname}", inject_failure=inj)
                if r["valid"]:
                    pred_cv[held] = r["ghat"][held]
                else:
                    cc = False
            recs["SPL"]["cc"].append(cc)
            recs["SPL"]["rho"].append(rho_cv_pin(x, pred_cv) if cc else None)
            recs["SPL"]["sst"].append(None)
            for side, obsP, edge in (("L", LEFT_PROBE_O, np.arange(0, 15)),
                                     ("R", RIGHT_PROBE_O, np.arange(131, 146))):
                r = fit_spline(spl, sc["fixture_id"], x, obsP, telemetry,
                               f"{sx}{ti}:probe{side}")
                ok = r["valid"] and spf["valid"]
                recs["SPL"]["p" + side].append(
                    "STOP_EXACTNESS_PENDING" if ok else False)
                recs["SPL"]["r" + side].append(
                    rmse_edge_pin(r["ghat"], spf["ghat"], edge) if ok else None)
        strata_recs[sx] = recs
    return strata_recs, n_s


# ------------------------- A.5 (ii)/(iii) unit tests (no C4 outcome) --------
def a5_unit_tests(f2m, grids):
    x = np.zeros(T); x[70] = 3.0
    x = (x - x.mean()) / x.std(ddof=0)
    tel = []
    r_ii = fit_family(f2m, grids, "UT-A5-II", "P-01", x, LEFT_PROBE_O, tel,
                      "ut", inject_fault=True, inject_fs_reject=True)
    ut_ii = (r_ii["feature_start_rejected"] and not r_ii["eligible"])
    r_iii = fit_family(f2m, grids, "UT-A5-III", "P-02", x, RIGHT_PROBE_O, tel,
                       "ut", inject_fault=True)
    ut_iii = not r_iii["eligible"]
    return dict(UT_A5_II_pass=bool(ut_ii), UT_A5_III_pass=bool(ut_iii),
                note="unit tests only; A.5 not applied; no C4 fixture outcome")


# ------------------------- non-regressions ---------------------------------
def nr01(f2m):
    OPENED_FILES.append(f2m.FIXTURE_MANIFEST_PATH)
    OPENED_FILES.append(f2m.D_F2_09_MANIFEST_PATH)
    r1 = f2m.run_all_fixtures()
    doc1 = dict(records=r1[0], self_tests=r1[1], construction_audit=r1[3],
                special_evidence=r1[4]["special_evidence"],
                falsifiability=r1[4]["falsifiability"],
                rejections_outside_invalid_init=r1[4]
                ["rejections_outside_invalid_init"])
    h = hashlib.sha256(f2m.canonicalize(doc1).encode("utf-8")).hexdigest()
    tel_ok = None
    OPENED_FILES.append(F2_TELEMETRY_PATH)
    with open(F2_TELEMETRY_PATH, newline="", encoding="utf-8") as f:
        frozen = list(csv.DictReader(f))
    if len(frozen) == len(r1[2]):
        tel_ok = all(
            all(str(row.get(k)) == frozen[i][k] for k in frozen[i]
                if k != "wall_clock_seconds")
            for i, row in enumerate(r1[2]))
    return h == F2_NR_HASH, h, bool(tel_ok)


def spline_nr(spl):
    man_hash = "e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32"
    har_hash = SPL_HASH
    rows = []
    for fx in spl["FIXTURES"]:
        fid = fx[0]
        z, O, m = spl["build_case"](fid)
        A = spl["amat"](m)
        cref, cert = spl["reference"](z, O, A)
        cref2, _ = spl["reference"](z, O, A)
        rss_ref = spl["rss_of"](cref, z, O)
        ref_repeat = repr(spl["rss_of"](cref2, z, O)) == repr(rss_ref)
        tol_q = 1e-12 + 1e-9 * abs(rss_ref)
        for cfg in ("SOLVER-A", "SOLVER-B", "SOLVER-C"):
            c, tel = spl["solver_config"](cfg, z, O, A)
            c2, _ = spl["solver_config"](cfg, z, O, A)
            rss_s = spl["rss_of"](c, z, O)
            rep_ok = (repr(spl["rss_of"](c2, z, O)) == repr(rss_s)) and ref_repeat
            err = abs(rss_s - rss_ref)
            viol = float(max(0.0, -np.min(A @ c)))
            obj_p, feas_p = err <= 0.1 * tol_q, viol <= 1e-8
            case_p = cert["certified"] and obj_p and feas_p
            rows.append([man_hash, har_hash, fid, cfg,
                         tel["final_endpoint_source"], tel["primary_status"],
                         tel["stage1_accept"], tel["expansion_triggered"],
                         tel["stage2_accept"], tel["fallback_invoked"],
                         tel["fallback_status"], repr(rss_ref), repr(rss_s),
                         repr(err), repr(tol_q), repr(0.1),
                         repr(err / (0.1 * tol_q)), repr(viol), str(obj_p),
                         str(feas_p), repr(cert["viol"]), str(cert["act_n"]),
                         str(cert["act_rank"]), repr(cert["res"]),
                         str(cert["feas_pass"]), str(cert["kkt_pass"]),
                         str(cert["certified"]), str(rep_ok), str(case_p)])
    OPENED_FILES.append(SPL_RESULTS_PATH)
    with open(SPL_RESULTS_PATH, newline="", encoding="ascii") as f:
        frozen = list(csv.reader(f))[1:]
    ok = len(rows) == len(frozen) and all(
        rows[i] == frozen[i] for i in range(len(rows)))
    return ok, len(rows)


# ------------------------- canonicalization --------------------------------
def canon(o):
    if isinstance(o, float):
        return float.hex(o)
    if isinstance(o, (np.floating,)):
        return float.hex(float(o))
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.ndarray):
        return [canon(v) for v in o.tolist()]
    if isinstance(o, dict):
        return {str(k): canon(v) for k, v in sorted(o.items(), key=lambda kv: str(kv[0]))}
    if isinstance(o, (list, tuple)):
        return [canon(v) for v in o]
    return o


def canonical_hash(doc):
    return hashlib.sha256(json.dumps(canon(doc), sort_keys=True)
                          .encode("utf-8")).hexdigest()


# ------------------------- main --------------------------------------------
def main():
    sys.path.insert(0, "p_konum_plus/calibration")
    import importlib as _imp
    genspec = _imp.util.spec_from_file_location(
        "f3_step2_fixture_generator_r1_2026_09_06",
        "p_konum_plus/calibration/f3_step2_fixture_generator_r1_2026-09-06.py")
    gen = _imp.util.module_from_spec(genspec)
    sys.modules["f3_step2_fixture_generator_r1_2026_09_06"] = gen
    genspec.loader.exec_module(gen)
    OPENED_FILES.append("p_konum_plus/calibration/"
                        "f3_step2_fixture_generator_r1_2026-09-06.py")

    f2m, f2_hash = load_f2()
    spl, spl_hash, spl_names = load_spline_ns()
    print("PIN-F2-IMPORT-HASH = " + f2_hash)
    print("PIN-SPLINE-IMPORT-HASH = " + spl_hash)

    # manifest BEFORE any run
    rows = gen.manifest_rows()
    with open(MANIFEST_PATH, "w", newline="", encoding="ascii") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(gen.MANIFEST_HEADER)
        w.writerows(rows)
    man_hash = sha256_of(MANIFEST_PATH)
    print("FIXTURE_MANIFEST_SHA256 = " + man_hash)
    print("MANIFEST_WRITTEN_BEFORE_EXECUTION = true")

    # non-regressions FIRST
    nr_ok, nr_hash, nr_tel = nr01(f2m)
    print("NR-01 = %s (hash %s; telemetry-fields %s)" % (nr_ok, nr_hash, nr_tel))
    assert nr_ok, "NR-01 FAIL -> STOP"
    snr_ok, snr_rows = spline_nr(spl)
    print("SPLINE_NONREGRESSION = %s (%d rows)" % (snr_ok, snr_rows))
    assert snr_ok, "SPLINE NON-REGRESSION FAIL -> STOP"

    grids = {fam: f2m.build_grid(fam)[1] for fam in ("P-01", "P-02")}
    print("GRID_SIZES = P-01 %d ; P-02 %d" % (len(grids["P-01"]),
                                              len(grids["P-02"])))

    # PIN verification tests (deterministic; closed forms; TEST_CONSTANTs)
    alt = [(-1.0) ** t for t in range(T)]
    lin = [float(t) for t in range(T)]
    const = [1.0] * T
    mix = [math.sin(0.37 * t) + 0.25 * math.cos(1.7 * t) for t in range(T)]
    acf_closed = acf_verify([("alternating", alt), ("linear", lin),
                             ("constant_den0", const), ("mixed_trig", mix)])
    # PIN-MASKED-OBJECTIVE full-mask bitwise test
    xv = np.asarray(mix); xv = (xv - xv.mean()) / xv.std(ddof=0)
    th = (0.3, 0.7, 20.0, 20.0)
    f_orig = f2m.make_objective_and_x("P-01", xv)
    f_mask = make_masked_moax(f2m, FULL_O)("P-01", xv)
    pin_mask_full = float.hex(f_orig(th)) == float.hex(f_mask(th))
    obs = np.arange(20, 120)
    pin_mask_le = make_masked_moax(f2m, obs)("P-01", xv)(th) <= f_orig(th)
    fs_pad = feature_start_masked(f2m, "P-01", xv, obs)
    js = int(min(j for j in obs if xv[j] == max(xv[k] for k in obs)))
    pin_fs = fs_pad[2] == js and abs(fs_pad[0][0] - (js / 145.0 - 0.125)) == 0.0
    print("PIN-MASKED-OBJECTIVE full == frozen: %s ; L_O<=L_FULL: %s ; "
          "PIN-FEATURE-START-MASKED: %s" % (pin_mask_full, bool(pin_mask_le),
                                            pin_fs))
    assert pin_mask_full and pin_mask_le and pin_fs

    a5 = a5_unit_tests(f2m, grids)
    print("A5_UNIT_TESTS = " + json.dumps(a5))

    def one_run():
        telemetry, stops, evals = [], [], []
        residual_series = []
        for sc in gen.REAL_SCENARIOS:
            strata_recs, n_s = run_real_scenario(f2m, spl, grids, sc, telemetry)
            evals.append(evaluate_fixture(sc["fixture_id"], strata_recs, n_s,
                                          "REAL", {}, stops))
        for fx in gen.INJ_FIXTURES:
            evals.append(evaluate_fixture(fx["fixture_id"], fx["strata"],
                                          gen.N_INJ,
                                          "TEST_ONLY_INJECTION_DECISION_LAYER",
                                          fx["flags"], stops))
        return evals, telemetry, stops

    evals1, telemetry1, stops1 = one_run()
    evals2, telemetry2, stops2 = one_run()

    # RUN1 residual-series ACF equality (a): recompute on real scenarios
    acf_run = []
    for sc in gen.REAL_SCENARIOS:
        for sx in SEXES:
            for ti, (kind, seed, sigma) in enumerate(sc["strata"][sx]):
                x = gen.make_traj(kind, seed, sigma)
                acf_run.extend(acf_verify([(f"{sc['fixture_id']}:{sx}{ti}:z",
                                            list(x))]))
    acf_all = acf_closed + acf_run
    acf_ok = all(r["bitwise_equal"] for r in acf_all)
    acf_disc = all(r.get("strict_vs_alt_b", True) and
                   r.get("strict_vs_alt_c", True) for r in acf_all)
    print("PIN-ACF bitwise-equal(all)=%s strict-vs-(b),(c)(all)=%s"
          % (acf_ok, acf_disc))
    assert acf_ok

    # INJ-DP04-C1 unconsulted-not-recomputed evidence
    for e in evals1:
        if e["fixture_id"] == "INJ-DP04-C1":
            rc = e["dp04"]["recompute_counts"]
            assert all(rc[c] == 0 for c in ("C2", "C3", "C4b", "C5")), rc
            print("UNCONSULTED_NOT_RECOMPUTED_EVIDENCE = " + json.dumps(rc))

    doc1 = dict(evals=evals1, stops=stops1, acf=acf_all, a5=a5,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    doc2 = dict(evals=evals2, stops=stops2, acf=acf_all, a5=a5,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    h1, h2 = canonical_hash(doc1), canonical_hash(doc2)
    print("RUN1_CANONICAL_SHA256 = " + h1)
    print("RUN2_CANONICAL_SHA256 = " + h2)
    print("DETERMINISM = " + str(h1 == h2))

    tel_fields = ["fixture", "fitter", "mask_id", "fixture_id", "family",
                  "start_id", "optimizer_path", "status", "message", "success",
                  "nit", "nfev", "njev", "wall_clock_seconds"]
    with open(TELEMETRY_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=tel_fields, lineterminator="\n",
                           extrasaction="ignore", restval="")
        w.writeheader()
        for row in telemetry1:
            w.writerow(row)
    env = dict(python=platform.python_version(), numpy=np.__version__,
               scipy=scipy.__version__, platform=platform.platform(),
               OMP=os.environ["OMP_NUM_THREADS"],
               OPENBLAS=os.environ["OPENBLAS_NUM_THREADS"],
               MKL=os.environ["MKL_NUM_THREADS"])
    results = dict(
        run="RUN1", interpretation="PATH_COVERAGE_ONLY",
        f2_engine_sha256=f2_hash, spline_solver_sha256=spl_hash,
        spline_loader_nodes=spl_names, fixture_manifest_sha256=man_hash,
        nr01=dict(passed=True, canonical=nr_hash, telemetry_fields_equal=nr_tel),
        spline_nonregression=dict(passed=True, rows=snr_rows),
        acf_verification=acf_all, a5_unit_tests=a5,
        exactness_findings=[dict(
            id="F3-STEP2-EXACT-01",
            rule="r4 s3-C4a A.5(i) via record r1; ADDENDUM A r1 NOT_LOCATED in repo",
            gap="no exact frozen data-level definition of a trajectory's "
                "Kural-S support region (F2 n_sup/kural_s_pass_exact are "
                "defined on stabilized fitted curves only)",
            options_observed="(a) PI supplies an operational data-level "
                             "definition; (b) PI declares A.5(i) evaluated on "
                             "a designated fitted curve; (c) PI removes (i)",
            classification="gate-specific blocker",
            wiring="C4a on real fixtures returns STOP_EXACTNESS_PENDING; "
                   "C4a/C4b/D-P04 4a-4b real paths PENDING")],
        evaluations=evals1, stops=stops1,
        run1_canonical_sha256=h1, run2_canonical_sha256=h2,
        determinism=h1 == h2, environment=env,
        real_data_access=False, opened_files=sorted(set(OPENED_FILES)),
        coverage=[list(r) for r in gen.COVERAGE_ROWS],
    )
    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(canon(results), f, sort_keys=True, indent=1)
    print("RESULTS_WRITTEN = " + RESULTS_PATH)
    print("TELEMETRY_ROWS = " + str(len(telemetry1)))
    print("STOPS = " + json.dumps(stops1))
    print("MECHANISM_OUTCOMES = " + json.dumps(
        {e["fixture_id"]: e["mechanism_outcome"] for e in evals1}))
    print("REAL_DATA_ACCESS = false")


if __name__ == "__main__":
    main()
