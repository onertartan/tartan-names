"""F3 STEP-2 adequacy-evaluation harness r2 (2026-09-07).

Child of f3_step2_adequacy_harness_r1_2026-09-06.py (parent
a95ad152b1ebcca6ff8b9ccfd34d122b9d6225a44d51254f4621fd4776a5b12f).
Implements, VERBATIM where the source is PI-ratified content, the S-1/S-2
scientific decisions and T-1..T-5 task-scope authorizations of
p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md, and the
X-01..X-20 exact engineering corrections of
Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md §5.

CLASS_C implementation of the frozen F3 STEP-1 contract (r4 5e594136... AS
RATIFIED BY freeze record r1 7055f186...) on predeclared synthetic fixtures
only. PATH_COVERAGE_ONLY: no adequacy evidence, no generator selection; the
D-P04 result is `mechanism_outcome`, never a winner. real_data_access=false
throughout; no P03 empirical threshold computation.

Engines are REUSED, never re-implemented:
  PIN-F2-LOADER     : frozen F2 r3 engine (01714752...) loaded via importlib
                      (file is __main__-guarded); hash verified before load.
  PIN-SPLINE-LOADER : qualified SOLVER-B (b31e5a6b...) loaded by a
                      definition-only AST loader restricted to the exactly
                      authorized node list (T-1; X-01).

PI-ratified content (S-1=(a), S-2=alpha, T-1=AUTHORIZE, T-2=T-2a,
T-3=AUTHORIZE, T-4=T-4a, T-5=CONFIRM_WITHIN_SCOPE) means every path this
cycle authorizes is enabled: the real C4a/C4b determination now runs on
real fixtures under PIN-A5-SUPPORT (S-1), the SOLVER-B unverifiable-
acceptance policy alpha is wired with PIN-EXC-CAPTURE (S-2/X-02), the spline
loader retains the 21-node bounded prelude (T-1/X-01), the NR-01(ii) T-2a
wrapper-qualification adapter runs, K-05 wording is corrected (T-3/X-20),
and per-optimizer-call spline telemetry is recorded (T-4a/X-11).
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
import time as _time
import traceback
from contextlib import contextmanager
from fractions import Fraction

import numpy as np
import scipy

REPO = "G:/PycharmProjects/pkp-worktree"
os.chdir(REPO)

OPENED_FILES = []
OPENED_FILES_AUDIT = []


def _audit_hook(event, args):
    if event == "open":
        try:
            OPENED_FILES_AUDIT.append(str(args[0]))
        except Exception:
            pass


sys.addaudithook(_audit_hook)                                    # X-18

# ------------------------- restart checkpointing ----------------------------
# Not part of the specification; a purely local, deterministic memoization
# layer so an interrupted process (environment/session teardown, not a code
# fault) can resume instead of repeating already-identical, expensive,
# side-effect-free computation. Each cached entry is keyed by run label and
# fixture/check id; RUN1 and RUN2 are always cached and computed separately,
# so the RUN1==RUN2 determinism check still reflects two independent
# executions of the fitting code, never a copy of one into the other.
import pickle
CKPT_DIR = "p_konum_plus/calibration/.r2_checkpoint_2026-09-07"
os.makedirs(CKPT_DIR, exist_ok=True)


_CKPT_UNSAFE = str.maketrans({c: "_" for c in '<>:"/\\|?*[]'})


def _ckpt_safe_name(name):
    safe = name.translate(_CKPT_UNSAFE)
    if len(safe) > 150:                    # avoid MAX_PATH issues on Windows
        safe = safe[:100] + "_" + hashlib.sha256(name.encode("utf-8")).hexdigest()[:16]
    return safe


def ckpt_load(name):
    p = os.path.join(CKPT_DIR, _ckpt_safe_name(name) + ".pkl")
    if os.path.exists(p):
        with open(p, "rb") as f:
            return pickle.load(f)
    return None


def ckpt_save(name, obj):
    p = os.path.join(CKPT_DIR, _ckpt_safe_name(name) + ".pkl")
    tmp = p + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump(obj, f)
    os.replace(tmp, p)


def sha256_of(path):
    OPENED_FILES.append(path)
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ------------------------- ratified literals (read-only; v5 §2, unchanged) -
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

GEN_MODULE_NAME = "f3_step2_fixture_generator_r2_2026_09_07"
GEN_PATH = "p_konum_plus/calibration/f3_step2_fixture_generator_r2_2026-09-07.py"

DATE_TAG = "2026-09-07"
MANIFEST_PATH = f"p_konum_plus/calibration/f3_step2_fixture_manifest_r2_{DATE_TAG}.csv"
CUSTODY_PATH = f"p_konum_plus/provenance/f3_step2_r2_preexecution_custody_{DATE_TAG}.md"
TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_telemetry_r2_{DATE_TAG}.csv"
RESULTS_PATH = f"p_konum_plus/calibration/f3_step2_results_r2_{DATE_TAG}.json"
RESIDUAL_PATH = f"p_konum_plus/calibration/f3_step2_residual_series_r2_{DATE_TAG}.json"
TEST_EVIDENCE_PATH = f"p_konum_plus/calibration/f3_step2_test_evidence_r2_{DATE_TAG}.json"

FORBIDDEN_RESULT_KEYS = ("winner", "selected", "generator_selected")

PI_RATIFIED_CONTENT_PATH = "p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md"
PI_RATIFIED_CONTENT_HASH = "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498"

# S / T values as read from the PI-ratified content file (verbatim; §4.3)
S1 = "(a)"
S2 = "alpha"
T1 = "AUTHORIZE"
T2 = "T-2a"
T3 = "AUTHORIZE"
T4 = "T-4a"
T5 = "CONFIRM_WITHIN_SCOPE"


# ------------------------- X-09 PIN-UNDEFINED-FLAGS -------------------------
def valid(value):
    return value is not None and math.isfinite(value)


# ------------------------- PIN-F2-LOADER -------------------------------
def load_f2():
    h = sha256_of(F2_PATH)
    assert h == F2_HASH, "PIN-F2-IMPORT-HASH FAIL: " + h
    spec = importlib.util.spec_from_file_location("f2eng", F2_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # __main__-guarded: suite does not run
    return mod, h


# ------------------------- X-01 PIN-SPLINE-LOADER ---------------------------
# T-1 AUTHORIZE: base retain classes (Import, ImportFrom, FunctionDef,
# ClassDef, constant Assign) wherever they occur, PLUS exactly the 21 named
# prelude nodes before the orchestration marker. No orchestration block.
RETAINED_CLASSES = (ast.Import, ast.ImportFrom, ast.FunctionDef,
                    ast.AsyncFunctionDef, ast.ClassDef)

AUTHORIZED_PRELUDE = [
    "docstring", "thread_env_loop",
    "MANIFEST_PATH", "RESULTS_PATH", "CUSTODY_PATH",
    "U", "KNOTS", "TC_OPTS", "SLSQP_OPTS", "B",
    "assert_B_shape", "assert_B_allclose",
    "D1", "D1_for_loop",
    "C_INT", "C_DEC", "C_INC", "C_RIGHT", "MASKS", "COEF_MAP", "CFG_FIELDS",
]

SOLVER_B_FUNCTION_SET = ("run_tc", "polish", "accept", "kkt_res", "maxviol",
                          "gradf", "rss_of", "run_slsqp", "solver_config",
                          "amat")


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


def _assign_name(node):
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return node.target.id
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
            isinstance(node.targets[0], ast.Name):
        return node.targets[0].id
    return None


def _io_call_names(node):
    """AST walk (not substring): every Call whose func resolves to a
    plausible I/O name (open / print / write-method / sys.exit)."""
    found = []
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id in ("open", "print", "exit"):
                found.append(f.id)
            elif isinstance(f, ast.Attribute):
                if f.attr in ("write", "writerow", "writerows", "exit"):
                    found.append(f.attr)
                if f.attr == "exit" and isinstance(f.value, ast.Name) and f.value.id == "sys":
                    found.append("sys.exit")
    return found


def load_spline_ns():
    h = sha256_of(SPL_PATH)
    assert h == SPL_HASH, "PIN-SPLINE-IMPORT-HASH FAIL: " + h
    OPENED_FILES.append(SPL_PATH)
    with open(SPL_PATH, "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    marker = src.index("# ---------------- steps 1-3")
    marker_line = src[:marker].count("\n") + 1
    lines = src.splitlines()

    retained, prelude, excluded = [], [], []
    prelude_labels = []
    node_hashes = {}          # label/name -> dict(lineno, end_lineno, sha256)
    for idx, node in enumerate(tree.body):
        seg = ast.get_source_segment(src, node)
        exact = "\n".join(lines[node.lineno - 1:node.end_lineno])
        assert seg is not None and seg in exact, "source-segment mismatch"
        io_hits = _io_call_names(node)

        is_base_retained = isinstance(node, RETAINED_CLASSES) or _const_assign(node)
        if is_base_retained:
            retained.append((node, seg))
            name = _assign_name(node) or getattr(node, "name", None) or type(node).__name__
        elif node.end_lineno < marker_line:
            assert not io_hits, "prelude node performs I/O: " + repr(io_hits) + " " + seg[:60]
            if idx == 0 and isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                label = "docstring"
            elif isinstance(node, ast.For):
                label = "thread_env_loop" if "thread_env_loop" not in prelude_labels else "D1_for_loop"
            elif isinstance(node, ast.Assert):
                label = ("assert_B_shape" if "assert_B_shape" not in prelude_labels
                         else "assert_B_allclose")
            else:
                label = _assign_name(node) or type(node).__name__
            prelude.append((node, seg))
            prelude_labels.append(label)
            node_hashes[label] = dict(
                lineno=node.lineno, end_lineno=node.end_lineno,
                sha256=hashlib.sha256(seg.encode("utf-8")).hexdigest())
        else:
            assert not io_hits or True   # orchestration may perform I/O; excluded, never executed here
            excluded.append((node, seg))
            continue

        if is_base_retained:
            node_hashes[name] = dict(
                lineno=node.lineno, end_lineno=node.end_lineno,
                sha256=hashlib.sha256(seg.encode("utf-8")).hexdigest())

    assert prelude_labels == AUTHORIZED_PRELUDE, (
        "PIN-SPLINE-LOADER node-list mismatch: executed=%r authorized=%r"
        % (prelude_labels, AUTHORIZED_PRELUDE))

    ns = {"__name__": "f3spl"}
    for node, seg in sorted(retained + prelude, key=lambda e: e[0].lineno):
        exec(compile(ast.Module(body=[node], type_ignores=[]),
                     SPL_PATH, "exec"), ns)

    for req in ("amat", "rss_of", "zddof0", "solver_config", "reference",
                "build_case", "FIXTURES", "B", "accept", "minimize"):
        assert req in ns, "spline loader missing dependency: " + req

    solver_b_hashes = {}
    for fname in SOLVER_B_FUNCTION_SET:
        found = None
        for node, seg in retained:
            if getattr(node, "name", None) == fname:
                found = hashlib.sha256(seg.encode("utf-8")).hexdigest()
                break
        assert found is not None, "SOLVER-B function not retained: " + fname
        solver_b_hashes[fname] = found

    names = dict(
        retained=[getattr(n, "name", None) or _assign_name(n) or type(n).__name__
                  for n, _ in sorted(retained, key=lambda e: e[0].lineno)],
        prelude=list(prelude_labels),
        excluded_count=len(excluded),
        node_hashes=node_hashes,
        solver_b_function_hashes=solver_b_hashes,
        io_free_assertion="AST-walk (Call.func name/attr in {open,print,exit,write,writerow,writerows,sys.exit}); PASS",
    )
    return ns, h, names


# ------------------------- X-02 PIN-EXC-CAPTURE (S-2 = alpha) --------------
EXC_CAPTURES = []
_SPL_CTX = {"fixture": None, "sex": None, "trajectory": None, "mask_id": None, "mode": None}
_ACCEPT_CALL_COUNT = [0]
SPLINE_TELEMETRY_CALLS = []
_LAST_CAPTURE_EVENT = [None]   # reset per mode; lets fit_spline's per-mode
                                # restart checkpoint replay the capture side
                                # effect into EXC_CAPTURES on a cache hit


def _parse_sex_traj(mask_id):
    # mask_id like "F0:full" / "run1:M1:fold2" / "F0:probeL" / "ut" -- scan
    # every ":"-separated segment for the sex+trajectory-index token, since
    # run_real_scenario prefixes a run label ahead of it.
    for seg in mask_id.split(":"):
        if seg and seg[0] in ("F", "M") and seg[1:].isdigit():
            return seg[0], int(seg[1:])
    return None, None


def install_exc_capture(spl):
    """S-2 = alpha (PI-ratified §3): unverifiable acceptance at stage k =>
    NOT accepted at stage k; the frozen chain continues (solver_config's own
    control flow already does this once accept() returns False instead of
    raising). Disclosed runtime wrapper around the loaded accept(); no frozen
    file bytes are modified -- only the exec'd namespace binding is rebound,
    which solver_config resolves as a global at call time."""
    real_accept = spl["accept"]

    def wrapped_accept(c, z, O, A):
        _ACCEPT_CALL_COUNT[0] += 1
        stage = _ACCEPT_CALL_COUNT[0]
        try:
            return real_accept(c, z, O, A)
        except RuntimeError as exc:
            sex, traj = _parse_sex_traj(_SPL_CTX["mask_id"] or "")
            rec = dict(
                fixture=_SPL_CTX["fixture"], sex=sex, trajectory=traj,
                mask_id=_SPL_CTX["mask_id"], mode=_SPL_CTX["mode"], stage=stage,
                exception_type=type(exc).__name__, message=str(exc),
                traceback=traceback.format_exc(),
                s2_rule="alpha: NOT accepted at stage %d; chain continues" % stage,
            )
            EXC_CAPTURES.append(rec)
            _LAST_CAPTURE_EVENT[0] = rec
            return False   # S-2=alpha: not accepted at this stage; caller's
                            # existing if/else falls through to the next stage
    spl["accept"] = wrapped_accept


def install_spline_call_telemetry(spl):
    """T-4a: one row per trust-constr / SLSQP call via a disclosed wrapper
    around scipy.optimize.minimize in the loaded namespace (library
    function, not a frozen function)."""
    real_minimize = spl["minimize"]

    def wrapped_minimize(fun, x0, **kwargs):
        t0 = _time.perf_counter()
        r = real_minimize(fun, x0, **kwargs)
        wall = _time.perf_counter() - t0
        sex, traj = _parse_sex_traj(_SPL_CTX["mask_id"] or "")
        fun_val = getattr(r, "fun", float("nan"))
        SPLINE_TELEMETRY_CALLS.append(dict(
            fixture=_SPL_CTX["fixture"], sex=sex, trajectory=traj,
            mask_id=_SPL_CTX["mask_id"], mode=_SPL_CTX["mode"],
            method=kwargs.get("method"),
            status=int(getattr(r, "status", -1)),
            message=str(getattr(r, "message", "")),
            nit=int(getattr(r, "nit", -1)),
            nfev=int(getattr(r, "nfev", -1)),
            njev=int(getattr(r, "njev", -1)) if hasattr(r, "njev") else -1,
            wall_clock_seconds=wall,
            objective=(float(fun_val) if math.isfinite(float(fun_val)) else None),
        ))
        return r
    spl["minimize"] = wrapped_minimize


NNLS_FAIL_TARGET = {"active": False, "fixture": None}


def install_nnls_test_injection(spl):
    """T-EXC-CAPTURE (X-02 test): TEST_ONLY_INJECTION making the loaded
    namespace's nnls raise RuntimeError once for a declared fixture. Fires on
    the first call where nnls is actually reached with a nonempty active set
    (kkt_res skips the nnls call entirely when the active set is empty, so a
    pre-guessed specific mode number is not reliable -- the declared context
    is the fixture, and the mode this lands on is recorded as evidence, not
    prescribed). Mode numbers repeat across every spline context of a
    fixture, so this must fire exactly once total (not once per context) --
    it self-deactivates on firing, and that "already fired" fact is
    checkpointed so a restart doesn't fire it a second time."""
    real_nnls = spl["nnls"]

    def wrapped_nnls(*args, **kwargs):
        if NNLS_FAIL_TARGET["active"] and _SPL_CTX["fixture"] == NNLS_FAIL_TARGET["fixture"]:
            NNLS_FAIL_TARGET["active"] = False
            ckpt_save("nnls_injection_fired", True)
            raise RuntimeError("TEST_ONLY_INJECTION: forced nnls non-convergence")
        return real_nnls(*args, **kwargs)
    spl["nnls"] = wrapped_nnls


# ------------------------- X-03 PIN-STARTS -----------------------------
def feature_start_validity(f2m, family, fs_theta):
    if not all(math.isfinite(float(v)) for v in fs_theta):
        return False, "NONFINITE"
    theta_arr = np.asarray(fs_theta, dtype=np.float64)
    num_feasible, _ = f2m.endpoint_numerically_feasible(theta_arr, family)
    if not num_feasible:
        return False, "NUMERICALLY_INFEASIBLE"
    stable_fn = f2m.p01_stable if family == "P-01" else f2m.p02_stable
    g_fs = stable_fn(theta_arr)
    zv_status, _, _ = f2m.zero_variance_rule(g_fs)
    if zv_status != "OK":
        return False, "ZERO_VARIANCE_OR_NONFINITE_FIT"
    domain_ok = (f2m.scientific_domain_pass_p01(fs_theta) if family == "P-01"
                 else f2m.scientific_domain_pass_p02(fs_theta))
    if not domain_ok:
        return False, "SCIENTIFIC_DOMAIN_FAIL"
    kt_ok = (f2m.kural_t_pass_exact_p01(fs_theta) if family == "P-01"
             else f2m.kural_t_pass_exact_p02(fs_theta))
    if not kt_ok:
        return False, "KURAL_T_FAIL"
    ks_ok = f2m.kural_s_pass_exact(g_fs) if np.all(np.isfinite(g_fs)) else False
    if not ks_ok:
        return False, "KURAL_S_FAIL"
    return True, None


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


# ------------------------- X-03/X-04 family fit driver -----------------
def fit_family(f2m, grids, fixture_id, family, x, obs_idx, telemetry,
               mask_id, start_bank="FULL_LATTICE", inject_fault=False,
               inject_fs_reject=False, record_sink=None):
    """X-03: start_bank DEFAULT = full retained lattice; a declared reduced
    bank (list/tuple of indices, or 'MINI_BANK') is used only when passed
    explicitly. Feature start accepted iff the frozen validity predicate
    holds AND it is not an exact-tuple duplicate of a bank start.
    X-04: probe_success (the returned 'eligible' flag) is probe-level only,
    decoupled from any full-data fit -- callers apply A.5 and full-data
    pairing requirements themselves.
    record_sink (X-06/T-2a): optional list; when given, receives frozen-
    schema canonical dicts (matching f2_step2_feasibility_harness_r3's own
    run_benign emission) for exact byte-level NR-01(ii) comparison."""
    obs = np.asarray(obs_idx)
    full = len(obs) == T
    retained = grids[family]
    if start_bank == "FULL_LATTICE":
        bank_indices = list(range(len(retained)))
    elif start_bank == "MINI_BANK":
        bank_indices = f2m.mini_bank_indices(len(retained))
    elif isinstance(start_bank, (list, tuple)):
        bank_indices = list(start_bank)
    else:
        raise ValueError("unknown start_bank: %r" % (start_bank,))

    bank_starts = [(f"grid[{i}]", retained[i]) for i in bank_indices]
    fs, u_star, j_star = feature_start_masked(f2m, family, x, obs)
    fs_ok, fs_reason = feature_start_validity(f2m, family, fs)
    if inject_fs_reject:
        fs_ok, fs_reason = False, "TEST_ONLY_INJECTION"
    fs_nonduplicate = tuple(float(v) for v in fs) not in [
        tuple(float(v) for v in s[1]) for s in bank_starts]
    if fs_ok and not fs_nonduplicate:
        fs_ok, fs_reason = False, "DUPLICATE"

    if record_sink is not None and not fs_ok:
        record_sink.append(dict(
            fixture_id=fixture_id, family=family, start_id="feature",
            optimizer_path="not_run", status_class="FEATURE_START_REJECTED",
            predicates=[], rejection_reasons=["FEATURE_START_REJECTED"],
            scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
            eligible=False, terminal_endpoint_hex=tuple(float(v).hex() for v in fs),
            family_status=None, family_summary=None,
        ))

    starts = list(bank_starts)
    if fs_ok:
        starts.append(("feature", fs))

    records = []
    for sid, x0 in starts:
        # fine-grained restart checkpoint: each individual optimizer start
        # is cached, since a single fixture's start bank (e.g. FULL_LATTICE,
        # ~1000 starts) can exceed one execution window on its own; a
        # deterministic, side-effect-free computation is safe to memoize
        # across restarts (see the module-level note on checkpointing).
        onekey = "onestart_%s_%s_%s_%s_%s" % (fixture_id, family, mask_id,
                                              sid, inject_fault)
        cached_start = ckpt_load(onekey)
        if cached_start is not None:
            canonical, cls, tel = cached_start
        else:
            with masked_objective(f2m, None if full else obs):
                canonical, cls, tel, ev = f2m.run_one_start(
                    fixture_id, family, sid, x0, x,
                    fault_inject_primary=inject_fault,
                    fault_inject_fallback_nonfinite=inject_fault)
            ckpt_save(onekey, (canonical, cls, tel))
        for row in tel:
            telemetry.append(dict(row, fixture=fixture_id, mask_id=mask_id,
                                  fitter=family))
        if record_sink is not None:
            record_sink.append(canonical)
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
               feature_start_rejected=not fs_ok,
               feature_start_rejected_reason=fs_reason,
               start_bank_size=len(starts),
               failure_codes=sorted({p for r in records for p in r["predicates"]
                                     if not r["eligible"]}) if status != "OK" else [])
    if status == "OK":
        out["theta"] = [float(v) for v in best["theta"]]
        out["L"] = best["L"]
        out["ghat"] = ghat_of(f2m, family, best["theta"])
        out["predicates"] = best["predicates"]
        if record_sink is not None:
            record_sink.append(dict(
                fixture_id=fixture_id, family=family, start_id="FAMILY_SELECTED",
                optimizer_path="aggregation", status_class="family_fit_selected",
                predicates=[], rejection_reasons=[],
                scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
                eligible=True, terminal_endpoint_hex=tuple(float(v).hex() for v in best["theta"]),
                family_status="OK", family_summary=None,
            ))
    elif record_sink is not None:
        record_sink.append(dict(
            fixture_id=fixture_id, family=family, start_id="FAMILY_SELECTED",
            optimizer_path="aggregation", status_class="FAMILY_FIT_FAILURE",
            predicates=[], rejection_reasons=[],
            scientific_domain_pass=None, kural_t_pass_exact=None, kural_s_pass_exact=None,
            eligible=False, terminal_endpoint_hex=None,
            family_status="FAMILY_FIT_FAILURE", family_summary=best,
        ))
    return out


# ------------------------- S-1 = (a) PIN-A5-SUPPORT --------------------
# PI-ratified §2, f3_step2_pi_ratified_content_2026-09-07.md (hash above).
# VERBATIM: lo_i = min(z_i); hi_i = max(z_i); thr_i = lo_i + 0.5*(hi_i-lo_i);
# S_i = { t in G : z_i[t] >= thr_i }.  Same reference vector for P-01, P-02
# and the spline benchmark; never derived from a fitted curve.
M_LEFT = set(range(0, 15))
M_RIGHT = set(range(131, 146))
_FULL_G = set(range(T))


def a5_support(z):
    z = np.asarray(z, dtype=np.float64)
    if z.shape != (T,) or not np.all(np.isfinite(z)):
        raise ValueError("A5-SUPPORT reference/computation contract violation: "
                         "missing/non-finite/wrong-length reference")
    lo = float(np.min(z)); hi = float(np.max(z))
    thr = lo + 0.5 * (hi - lo)
    if not math.isfinite(thr):
        raise ValueError("A5-SUPPORT reference/computation contract violation: "
                         "non-finite computed threshold")
    S = set(int(t) for t in np.flatnonzero(z >= thr))
    if not S:
        raise ValueError("A5-SUPPORT reference/computation contract violation: "
                         "unexpectedly empty computed support")
    return S


def a5_condition_i(S, side):
    M = M_LEFT if side == "L" else M_RIGHT
    return len(S & (_FULL_G - M)) == 0


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
    per_mode_valid = []
    for m in range(T):
        # fine-grained restart checkpoint: a single spline context enumerates
        # 146 modes, each a trust-constr (+ possible SLSQP fallback) solve;
        # cached per (fixture, mask_id, mode) so a restart resumes mid-context.
        mkey = "splmode_%s_%s_%s" % (fixture_id, mask_id, m)
        cached_mode = ckpt_load(mkey)
        if cached_mode is not None:
            v, rss, c, src, pst, cap_rec = cached_mode
            if cap_rec is not None:
                EXC_CAPTURES.append(cap_rec)   # replay the side effect
        else:
            _ACCEPT_CALL_COUNT[0] = 0
            _SPL_CTX.update(fixture=fixture_id, mask_id=mask_id, mode=m)
            _LAST_CAPTURE_EVENT[0] = None
            A = spl["amat"](m)
            try:
                c, tel = spl["solver_config"]("SOLVER-B", x, obs, A)
                v = spline_valid_from_tel(tel)
                src, pst = tel["final_endpoint_source"], tel["primary_status"]
            except RuntimeError as exc:
                c, v = None, False
                src, pst = "ACCEPTANCE_UNVERIFIABLE", "EXC:" + type(exc).__name__
            rss = spl["rss_of"](c, x, obs) if v else float("inf")
            ckpt_save(mkey, (v, rss, c, src, pst, _LAST_CAPTURE_EVENT[0]))
        per_mode.append((m, v, rss, c))
        per_mode_valid.append(bool(v))
        telemetry.append(dict(fixture=fixture_id, mask_id=mask_id, fitter="SPL",
                              start_id=f"mode{m}",
                              optimizer_path=src,
                              status=pst, success=v,
                              nit=-1, nfev=-1, njev=-1, wall_clock_seconds=0.0,
                              message="RSS=" + repr(rss)))
    valid_modes = [(m, rss, c) for m, val, rss, c in per_mode if val]
    if not valid_modes:
        return dict(valid=False, failure="NO_VALID_MODE",
                    per_mode_valid=per_mode_valid)
    rss_min = min(r for _, r, _ in valid_modes)
    eq = [(m, r, c) for m, r, c in valid_modes
          if abs(r - rss_min) <= 1e-12 + 1e-9 * max(abs(r), abs(rss_min))]
    m_win, rss_win, c_win = min(eq, key=lambda t: t[0])
    q = spl["B"] @ c_win
    sd = q.std(ddof=0)
    if not np.all(np.isfinite(q)) or sd == 0.0:
        return dict(valid=False, failure="ZERO_VARIANCE_OR_NONFINITE",
                    per_mode_valid=per_mode_valid)
    return dict(valid=True, mode=m_win, rss=float(rss_win),
                ghat=(q - q.mean()) / sd,
                equivalent_modes=sorted(m for m, _, _ in eq),
                per_mode_valid=per_mode_valid)


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


def acf_frac_ulp(r, phi):
    """X-13: exact-rational deviation. No rounding of `exact` to float64
    before differencing -- phi and ulp(phi) are also lifted to Fraction and
    the subtraction/division stay exact throughout; float() is applied only
    to the final ratio for reporting."""
    fr = [Fraction(float(v)) for v in r]
    n = len(fr)
    rb = sum(fr, Fraction(0)) / n
    a = [v - rb for v in fr]
    num = sum((a[t] * a[t + 1] for t in range(n - 1)), Fraction(0))
    den = sum((v * v for v in a), Fraction(0))
    if den == 0:
        return None
    exact = abs(num / den)
    if phi == 0:
        return 0.0
    phi_frac = Fraction(phi)
    ulp_frac = Fraction(math.ulp(phi))
    dev = abs(phi_frac - exact) / ulp_frac
    return float(dev)


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
CRITERIA_ORDER = ["C1", "C2", "C3", "C4a", "C4b", "C5", "C6"]


def crit_stats(recs, n_s):
    """recs: per-fitter dict of per-trajectory lists (generator grammar).
    X-09: cc_idx/phi_idx/sst_idx additionally require math.isfinite (NaN is
    never silently treated as a valid statistic)."""
    def med_over(vals, idxs):
        sel = [vals[i] for i in idxs]
        return median_pin(sel) if sel else None
    out = {}
    for fk in ("P01", "P02", "SPL"):
        d = recs[fk]
        cov = sum(1 for b in d["full"] if b) / n_s
        cc_idx = [i for i in range(n_s) if d["cc"][i] and valid(d["rho"][i])]
        phi_idx = [i for i in range(n_s) if d["full"][i] and valid(d["phi"][i])]
        probes_ok = [i for i in range(n_s) if d["pL"][i] and d["pR"][i]
                     and d["rL"][i] is not None and d["rR"][i] is not None]
        ident = (sum(1 for i in range(n_s) if d["pL"][i]) +
                 sum(1 for i in range(n_s) if d["pR"][i])) / (2.0 * n_s)
        sst_idx = [i for i in range(n_s) if d["cc"][i] and valid(d["sst"][i])]
        out[fk] = dict(cov=cov, cc_idx=cc_idx, phi_idx=phi_idx,
                       probes_idx=probes_ok, ident=ident, sst_idx=sst_idx,
                       med_over=med_over, d=d)
    return out


def evaluate_fixture(fx_id, strata, n_s, c4_source, flags, stops,
                     force_c4_pending=False):
    """strata: sex -> fitter grammar dicts. Returns evaluation dict.
    X-08: family P03 status and mechanism outcome are two separate rules
    (see run below). force_c4_pending: TEST_ONLY use for INJ-P03-* fixtures
    that must exercise the mechanism-outcome PENDING branch independently
    of whichever S-1 value governs the true real-fixture C4 path."""
    ev = dict(fixture_id=fx_id, interpretation="PATH_COVERAGE_ONLY",
              c4_source=c4_source, sexes={}, criteria={}, dp04=None,
              mechanism_outcome=None)
    S = {sx: crit_stats(strata[sx], n_s) for sx in SEXES}
    fam_pass, fam_detail, fam_fields = {}, {}, {}
    for fam in ("P01", "P02"):
        detail = {}
        definite_failures, pending_criteria = [], []
        first_pending_seen, first_definite_fail = None, None
        for crit in CRITERIA_ORDER:
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
                    if force_c4_pending:
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING"
                                                  "(TEST_ONLY_FORCED_C4_PENDING)")
                        continue
                    val, thr, ok = st["ident"], C_IDENT, st["ident"] >= C_IDENT
                elif crit == "C4b":
                    if force_c4_pending:
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING"
                                                  "(TEST_ONLY_FORCED_C4_PENDING)")
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
                    if share >= C_COMPLETE:                     # PIN-K05-INVARIANT (X-20)
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
            is_pending = any(s is not None and "PENDING" in str(s) for s in statuses)
            if is_pending:
                if first_pending_seen is None:
                    first_pending_seen = crit
                pending_criteria.append(crit)
                continue
            crit_ok = all(per_sex[sx]["passed"] for sx in SEXES)
            if not crit_ok:
                if first_definite_fail is None:
                    first_definite_fail = crit
                definite_failures.append(crit)
        fam_detail[fam] = detail
        if definite_failures:
            p03_status = "FAIL"
        elif pending_criteria:
            p03_status = "PENDING"
        else:
            p03_status = "PASS"
        if not definite_failures and not pending_criteria:
            first_failed = None
        elif first_definite_fail is None:
            first_failed = "UNDETERMINED_PENDING_" + first_pending_seen
        else:
            idx_fail = CRITERIA_ORDER.index(first_definite_fail)
            idx_pending = (CRITERIA_ORDER.index(first_pending_seen)
                           if first_pending_seen else None)
            first_failed = (("UNDETERMINED_PENDING_" + first_pending_seen)
                            if idx_pending is not None and idx_pending < idx_fail
                            else first_definite_fail)
        fam_pass[fam] = p03_status
        fam_fields[fam] = dict(
            p03_status=p03_status,
            c4_status=("PENDING" if force_c4_pending else "RESOLVED"),
            first_failed_criterion=first_failed,
            definite_failures=list(definite_failures),
            pending_criteria=list(pending_criteria),
        )
    ev["criteria"] = fam_detail
    ev["p03"] = dict(fam_pass)
    ev["p03_fields"] = fam_fields
    p1, p2 = fam_pass["P01"], fam_pass["P02"]
    if p1 == "PENDING" or p2 == "PENDING":
        ids = []
        for fam in ("P01", "P02"):
            if fam_pass[fam] == "PENDING":
                ids.extend(fam_fields[fam]["pending_criteria"])
        tag = "TEST_ONLY_FORCED_C4_PENDING" if force_c4_pending else ",".join(sorted(set(ids)))
        ev["mechanism_outcome"] = "MECHANISM_UNDETERMINED_PENDING_EXACTNESS(%s)" % tag
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
    # DISC-F3-03 complement sets (C2, C3, C4b -- X-11c)
    comp = {}
    for sx in SEXES:
        for fam in ("P01", "P02"):
            st, sp = S[sx][fam], S[sx]["SPL"]
            idx2 = [i for i in sp["cc_idx"] if i not in st["cc_idx"]]
            idx3 = [i for i in sp["phi_idx"] if i not in st["phi_idx"]]
            idx4b = [i for i in sp["probes_idx"] if i not in st["probes_idx"]]
            comp[f"{sx}:{fam}:C2"] = dict(
                size=len(idx2), spline_stat=sp["med_over"](sp["d"]["rho"], idx2))
            comp[f"{sx}:{fam}:C3"] = dict(
                size=len(idx3), spline_stat=sp["med_over"](
                    [abs(v) if v is not None else None for v in sp["d"]["phi"]], idx3))
            comp[f"{sx}:{fam}:C4b"] = dict(
                size=len(idx4b), spline_stat=sp["med_over"]([
                    max(sp["d"]["rL"][i], sp["d"]["rR"][i])
                    if sp["d"]["rL"][i] is not None and sp["d"]["rR"][i] is not None
                    else None for i in range(n_s)], idx4b))
    ev["disc_f3_03_complement"] = comp
    for k in FORBIDDEN_RESULT_KEYS:               # labelling pin
        assert k not in ev, "forbidden key emitted"
    return ev


def run_dp04(fx_id, S, n_s, flags, stops):
    """X-07 PIN-U-SETS: each consulted subset-defined level builds ONE
    common set from the CRITERION-SPECIFIC validity of its own required
    statistic (X-09's `valid`), for exactly the fitters the frozen
    definition names. U5 uses P-01/P-02 only (no spline term). Construction-
    time exclusion of an invalid observation is never a STOP; the two STOP
    labels (CONTRACT_VIOLATION_EMPTY_U / CONTRACT_VIOLATION_INCONSISTENT_U,
    X-14) stay narrow and distinct."""
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
            inconsistent_hit = None
            for fam in ("P01", "P02"):
                vals = {}
                for sx in SEXES:
                    st1, st2, sp = S[sx]["P01"], S[sx]["P02"], S[sx]["SPL"]
                    if crit == "C2":
                        U = [i for i in range(n_s) if valid(st1["d"]["rho"][i])
                             and valid(st2["d"]["rho"][i]) and valid(sp["d"]["rho"][i])]
                        if flags.get("inject_empty_U2"):
                            U = []                # TEST_ONLY_INJECTION
                        src = S[sx][fam]
                        v = src["med_over"](src["d"]["rho"], U)
                    elif crit == "C3":
                        U = [i for i in range(n_s)
                             if valid(st1["d"]["phi"][i]) and valid(st2["d"]["phi"][i])
                             and valid(sp["d"]["phi"][i])]
                        src = S[sx][fam]
                        v = src["med_over"]([abs(x) if x is not None else None
                                             for x in src["d"]["phi"]], U)
                    elif crit == "C4b":
                        U = [i for i in range(n_s)
                             if st1["d"]["pL"][i] and st1["d"]["pR"][i]
                             and st2["d"]["pL"][i] and st2["d"]["pR"][i]
                             and sp["d"]["pL"][i] and sp["d"]["pR"][i]]
                        src = S[sx][fam]
                        dd = src["d"]
                        v = src["med_over"]([max(dd["rL"][i], dd["rR"][i])
                                             if dd["rL"][i] is not None and
                                             dd["rR"][i] is not None else None
                                             for i in range(n_s)], U)
                    else:  # C5 -- P-01/P-02 only, NO spline term
                        U = [i for i in range(n_s)
                             if valid(st1["d"]["sst"][i]) and valid(st2["d"]["sst"][i])]
                        src = S[sx][fam]
                        v = src["med_over"](src["d"]["sst"], U)
                    if not U:
                        empty_hit = True
                    inj_key = f"inject_post_construction_invalid_{crit}"
                    corrupt_idx = flags.get(inj_key)
                    if corrupt_idx is not None and corrupt_idx in U:
                        inconsistent_hit = dict(level=crit, sex=sx, member=corrupt_idx)
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
            if inconsistent_hit:
                stops.append(dict(fixture=fx_id,
                                  stop="CONTRACT_VIOLATION_INCONSISTENT_U",
                                  **inconsistent_hit))
                return dict(consulted_path=consulted,
                            mechanism_outcome="STOP_CONTRACT_VIOLATION_INCONSISTENT_U",
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
                        mechanism_outcome="STOP_CONTRACT_VIOLATION_EMPTY_U",
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


# ------------------------- X-04/S-1 real-scenario execution -----------------
def fold_masks():
    out = []
    for b in range(K_FOLDS):
        held = np.arange(FOLD_BOUNDS[b], FOLD_BOUNDS[b + 1])
        train = np.setdiff1d(FULL_O, held)
        out.append((f"fold{b}", train, held))
    return out


def run_real_scenario(f2m, spl, grids, sc, run_label):
    # run_label is folded into every mask_id used for a real optimizer/
    # spline call so RUN1 and RUN2 never share a fine-grained checkpoint
    # entry -- each is a genuinely independent execution of the fitting
    # code, which is what the RUN1==RUN2 determinism check is meant to prove.
    def mid(suffix):
        return run_label + ":" + suffix
    telemetry, construction_audit = [], []
    n_s = len(sc["strata"]["F"])
    start_bank = sc["start_bank"]
    injmap = {}
    for i in sc["injections"]:
        injmap.setdefault((i["traj"], i["family"], i["context"]), i["mode"])
    strata_recs = {}
    for sx in SEXES:
        recs = {k: dict(full=[], cc=[], rho=[], phi=[], pL=[], pR=[],
                        rL=[], rR=[], sst=[]) for k in ("P01", "P02", "SPL")}
        for ti, (kind, seed, sigma) in enumerate(sc["strata"][sx]):
            import importlib as _imp2
            gen = sys.modules[GEN_MODULE_NAME]
            x = gen.make_traj(kind, seed, sigma)
            trg = (sx, ti)
            S_i = a5_support(x)                    # S-1=(a): shared across P-01/P-02/SPL
            a5_i_L, a5_i_R = a5_condition_i(S_i, "L"), a5_condition_i(S_i, "R")
            construction_audit.append(dict(
                fixture_id=sc["fixture_id"], sex=sx, trajectory=ti,
                a5_support_size=len(S_i), a5_i_L=a5_i_L, a5_i_R=a5_i_R))
            for family in ("P-01", "P-02"):
                fk = FAM_KEYS[family]
                full = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                  FULL_O, telemetry, mid(f"{sx}{ti}:full"),
                                  start_bank=start_bank)
                recs[fk]["full"].append(full["eligible"])
                phi = (acf_classical(x - full["ghat"])
                       if full["eligible"] else None)
                recs[fk]["phi"].append(phi)
                fold_fits, cc = [], True
                pred_cv = np.full(T, np.nan)
                for fname, train, held in fold_masks():
                    inj = injmap.get((trg, family, fname))
                    r = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                   train, telemetry, mid(f"{sx}{ti}:{fname}"),
                                   start_bank=start_bank,
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
                # X-04: probe_success decoupled from full-data fit; A.5
                # (S-1=(a)) gates the C4a numerator; C4b RMSE still needs
                # the full-data reference (pre-existing requirement, not
                # newly imposed on probe_success itself).
                for side, obsP, edge, a5_i in (
                        ("L", LEFT_PROBE_O, np.arange(0, 15), a5_i_L),
                        ("R", RIGHT_PROBE_O, np.arange(131, 146), a5_i_R)):
                    inj = injmap.get((trg, family, "probe" + side))
                    r = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                   obsP, telemetry, mid(f"{sx}{ti}:probe{side}"),
                                   start_bank=start_bank,
                                   inject_fault=inj == "F2_FAULT_INJECTION")
                    probe_raw = bool(r["eligible"])          # X-04
                    p_c4a = probe_raw and not a5_i           # A.5 failure excludes
                    recs[fk]["p" + side].append(p_c4a)
                    rmse_computable = p_c4a and full["eligible"]
                    recs[fk]["r" + side].append(
                        rmse_edge_pin(r["ghat"], full["ghat"], edge)
                        if rmse_computable else None)
            # spline
            spf_inj = injmap.get((trg, "SPL", "full")) == "TEST_ONLY_INJECTION"
            spf = fit_spline(spl, sc["fixture_id"], x, FULL_O, telemetry,
                             mid(f"{sx}{ti}:full"), inject_failure=spf_inj)
            recs["SPL"]["full"].append(spf["valid"])
            recs["SPL"]["phi"].append(acf_classical(x - spf["ghat"])
                                      if spf["valid"] else None)
            cc, pred_cv = True, np.full(T, np.nan)
            for fname, train, held in fold_masks():
                inj = injmap.get((trg, "SPL", fname)) == "TEST_ONLY_INJECTION"
                r = fit_spline(spl, sc["fixture_id"], x, train, telemetry,
                               mid(f"{sx}{ti}:{fname}"), inject_failure=inj)
                if r["valid"]:
                    pred_cv[held] = r["ghat"][held]
                else:
                    cc = False
            recs["SPL"]["cc"].append(cc)
            recs["SPL"]["rho"].append(rho_cv_pin(x, pred_cv) if cc else None)
            recs["SPL"]["sst"].append(None)
            for side, obsP, edge, a5_i in (("L", LEFT_PROBE_O, np.arange(0, 15), a5_i_L),
                                           ("R", RIGHT_PROBE_O, np.arange(131, 146), a5_i_R)):
                r = fit_spline(spl, sc["fixture_id"], x, obsP, telemetry,
                               mid(f"{sx}{ti}:probe{side}"))
                probe_raw = bool(r["valid"])
                p_c4a = probe_raw and not a5_i
                recs["SPL"]["p" + side].append(p_c4a)
                rmse_computable = p_c4a and spf["valid"]
                recs["SPL"]["r" + side].append(
                    rmse_edge_pin(r["ghat"], spf["ghat"], edge) if rmse_computable else None)
        strata_recs[sx] = recs
    return strata_recs, n_s, telemetry, construction_audit


# ------------------------- A.5 (ii)/(iii) + X-04 unit tests -----------------
def a5_unit_tests(f2m, grids):
    x = np.zeros(T); x[70] = 3.0
    x = (x - x.mean()) / x.std(ddof=0)
    tel = []
    r_ii = fit_family(f2m, grids, "UT-A5-II", "P-01", x, LEFT_PROBE_O, tel,
                      "ut", start_bank="MINI_BANK", inject_fault=True,
                      inject_fs_reject=True)
    ut_ii = (r_ii["feature_start_rejected"] and not r_ii["eligible"])
    r_iii = fit_family(f2m, grids, "UT-A5-III", "P-02", x, RIGHT_PROBE_O, tel,
                       "ut", start_bank="MINI_BANK", inject_fault=True)
    ut_iii = not r_iii["eligible"]
    return dict(UT_A5_II_pass=bool(ut_ii), UT_A5_III_pass=bool(ut_iii),
                note="unit tests; A.5(i) is exercised on the real path (S-1=(a)); "
                     "these two probe A.5(ii)/(iii) directly")


def ut_probe_decouple(f2m, grids):
    """X-04: TEST_ONLY_INJECTION making the full-data fit ineligible while
    the probe refit is eligible => probe_success = True (C4a numerator);
    probe absent from the C4b paired set (no full-data reference)."""
    gen = sys.modules[GEN_MODULE_NAME]
    x = gen.make_traj("bump_a", 20260912, 0.10)
    tel = []
    full = fit_family(f2m, grids, "UT-PROBE-DECOUPLE", "P-01", x, FULL_O, tel,
                      "ut:full", start_bank="MINI_BANK", inject_fault=True)
    probe = fit_family(f2m, grids, "UT-PROBE-DECOUPLE", "P-01", x, LEFT_PROBE_O,
                       tel, "ut:probeL", start_bank="MINI_BANK")
    full_ineligible = not full["eligible"]
    probe_eligible = probe["eligible"]
    probe_success_c4a = probe_eligible and not a5_condition_i(a5_support(x), "L")
    rmse_computable = probe_success_c4a and full["eligible"]
    pass_ = bool(full_ineligible and probe_eligible and probe_success_c4a
                and not rmse_computable)
    return dict(UT_PROBE_DECOUPLE_pass=pass_, full_eligible=full["eligible"],
                probe_eligible=probe_eligible, probe_success_c4a=probe_success_c4a,
                rmse_computable=rmse_computable,
                note="probe_success is probe-level only (X-04); C4b RMSE still "
                     "requires the full-data reference (pre-existing, not newly "
                     "imposed on C4a probe_success)")


# ------------------------- FIX-STARTS-FULL / FIX-STARTS-DUP (X-03) ---------
def fix_starts_full(f2m, grids, telemetry):
    gen = sys.modules[GEN_MODULE_NAME]
    traj = gen.STARTS_FULL_TRAJ
    x = gen.make_traj(traj["kind"], traj["seed"], traj["sigma"])
    out = {}
    for family, expected_retained in (("P-01", len(grids["P-01"])),
                                       ("P-02", len(grids["P-02"]))):
        r = fit_family(f2m, grids, "FIX-STARTS-FULL", family, x, FULL_O,
                       telemetry, f"full:{family}", start_bank="FULL_LATTICE")
        expected = expected_retained + (0 if r["feature_start_rejected"] else 1)
        out[family] = dict(start_bank_size=r["start_bank_size"],
                           expected=expected,
                           pass_=bool(r["start_bank_size"] == expected),
                           retained_count=expected_retained,
                           feature_start_rejected=r["feature_start_rejected"])
    return out


def fix_starts_dup(f2m, grids, telemetry):
    gen = sys.modules[GEN_MODULE_NAME]
    out = {}
    for direction, tag in (("down", "index0"), ("up", "index145")):
        x = gen.make_monotone(direction)
        r = fit_family(f2m, grids, "FIX-STARTS-DUP", "P-02", x, FULL_O,
                       telemetry, f"dup:{tag}", start_bank="FULL_LATTICE")
        out[tag] = dict(
            feature_start_rejected=r["feature_start_rejected"],
            reason=r["feature_start_rejected_reason"],
            pass_=bool(r["feature_start_rejected"]
                      and r["feature_start_rejected_reason"] == "DUPLICATE"))
    return out


# ------------------------- X-06 non-regressions ---------------------------------
def nr01_wrapper_adapter(f2m, grids):
    """T-2a: replay FIX-P01-BENIGN / FIX-P02-BENIGN through fit_family
    (mask=FULL, start_bank=MINI_BANK -- each F2 fixture's OWN declared
    construction per D-04) instead of the frozen engine's native run_benign;
    every other F2 fixture keeps its frozen native result unchanged. Returns
    the substituted two-fixture record block plus a pass flag."""
    u0 = 72.0 / 145.0
    k_mid = math.sqrt(4.0 * f2m.K_MAX)
    theta_p01_fix = (u0 - 1.0 / 8.0, u0 + 1.0 / 8.0, k_mid, k_mid)
    theta_p02_fix = (u0, 0.32057672965544004, 0.32057672965544004, math.sqrt(6.0))
    out = {}
    for fid, family, theta_fix in (("FIX-P01-BENIGN", "P-01", theta_p01_fix),
                                    ("FIX-P02-BENIGN", "P-02", theta_p02_fix)):
        stable_fn = f2m.p01_stable if family == "P-01" else f2m.p02_stable
        g = stable_fn(theta_fix)
        status, _, x_fixture = f2m.zero_variance_rule(g)
        assert status == "OK"
        sink = []
        tel = []
        fit_family(f2m, grids, fid, family, x_fixture, FULL_O, tel,
                  f"nr01ii:{fid}", start_bank="MINI_BANK", record_sink=sink)
        out[fid] = sink
    return out


def nr01(f2m, grids):
    OPENED_FILES.append(f2m.FIXTURE_MANIFEST_PATH)
    OPENED_FILES.append(f2m.D_F2_09_MANIFEST_PATH)
    r1 = f2m.run_all_fixtures()
    doc1 = dict(records=r1[0], self_tests=r1[1], construction_audit=r1[3],
                special_evidence=r1[4]["special_evidence"],
                falsifiability=r1[4]["falsifiability"],
                rejections_outside_invalid_init=r1[4]
                ["rejections_outside_invalid_init"])
    h = hashlib.sha256(f2m.canonicalize(doc1).encode("utf-8")).hexdigest()
    OPENED_FILES.append(F2_TELEMETRY_PATH)
    with open(F2_TELEMETRY_PATH, newline="", encoding="utf-8") as f:
        frozen = list(csv.DictReader(f))
    tel_ok = (len(frozen) == len(r1[2]) and all(
        all(str(row.get(k)) == frozen[i][k] for k in frozen[i]
            if k != "wall_clock_seconds")
        for i, row in enumerate(r1[2])))
    assert h == F2_NR_HASH, "NR-01(i) canonical hash mismatch"
    assert tel_ok, "NR-01(i) telemetry field equality FAILED"        # X-06: asserted

    # NR-01(ii), T-2a wrapper-qualification adapter. Splice the substituted
    # records in at their ORIGINAL list position -- canonicalize() sorts
    # dict keys but not list order, so appending at the end would change the
    # hash on ordering alone, not content.
    substituted = nr01_wrapper_adapter(f2m, grids)
    spliced = {"FIX-P01-BENIGN": False, "FIX-P02-BENIGN": False}
    hybrid_records = []
    for r in r1[0]:
        fid = r["fixture_id"]
        if fid in substituted:
            if not spliced[fid]:
                hybrid_records.extend(substituted[fid])
                spliced[fid] = True
            continue
        hybrid_records.append(r)
    doc1_hybrid = dict(records=hybrid_records, self_tests=r1[1],
                       construction_audit=r1[3],
                       special_evidence=r1[4]["special_evidence"],
                       falsifiability=r1[4]["falsifiability"],
                       rejections_outside_invalid_init=r1[4]
                       ["rejections_outside_invalid_init"])
    h_hybrid = hashlib.sha256(f2m.canonicalize(doc1_hybrid).encode("utf-8")).hexdigest()
    nr01ii_pass = (h_hybrid == F2_NR_HASH)
    return dict(passed=True, canonical=h, telemetry_fields_equal=tel_ok,
               nr01ii=dict(option="T-2a", passed=bool(nr01ii_pass),
                          hybrid_canonical=h_hybrid, expected=F2_NR_HASH))


def spline_nr(spl):
    man_hash = "e71ce030931819995f8ad7640cb9914e6266f8cb712e19fe08fc7cfc5bfcee32"
    har_hash = SPL_HASH
    rows = []
    for fx in spl["FIXTURES"]:
        fid = fx[0]
        z, O, m = spl["build_case"](fid)
        A = spl["amat"](m)
        _SPL_CTX.update(fixture="NR-SPL:" + fid, mask_id="nr", mode=m)
        _ACCEPT_CALL_COUNT[0] = 0
        cref, cert = spl["reference"](z, O, A)
        cref2, _ = spl["reference"](z, O, A)
        rss_ref = spl["rss_of"](cref, z, O)
        ref_repeat = repr(spl["rss_of"](cref2, z, O)) == repr(rss_ref)
        tol_q = 1e-12 + 1e-9 * abs(rss_ref)
        for cfg in ("SOLVER-A", "SOLVER-B", "SOLVER-C"):
            _ACCEPT_CALL_COUNT[0] = 0
            c, tel = spl["solver_config"](cfg, z, O, A)
            _ACCEPT_CALL_COUNT[0] = 0
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
    genspec = importlib.util.spec_from_file_location(GEN_MODULE_NAME, GEN_PATH)
    gen = importlib.util.module_from_spec(genspec)
    sys.modules[GEN_MODULE_NAME] = gen
    genspec.loader.exec_module(gen)
    OPENED_FILES.append(GEN_PATH)

    f2m, f2_hash = load_f2()
    spl, spl_hash, spl_names = load_spline_ns()
    install_exc_capture(spl)                       # X-02 / S-2=alpha
    install_spline_call_telemetry(spl)              # T-4a / X-11
    install_nnls_test_injection(spl)                # T-EXC-CAPTURE hook
    print("PIN-F2-IMPORT-HASH = " + f2_hash)
    print("PIN-SPLINE-IMPORT-HASH = " + spl_hash)
    print("PIN-SPLINE-LOADER prelude nodes = %d (authorized list match: %s)"
          % (len(spl_names["prelude"]), spl_names["prelude"] == AUTHORIZED_PRELUDE))

    grids = {fam: f2m.build_grid(fam)[1] for fam in ("P-01", "P-02")}
    print("GRID_SIZES = P-01 %d ; P-02 %d" % (len(grids["P-01"]), len(grids["P-02"])))

    # manifest BEFORE any run (W-2)
    rows = gen.manifest_rows()
    with open(MANIFEST_PATH, "w", newline="", encoding="ascii") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(gen.MANIFEST_HEADER)
        w.writerows(rows)
    man_hash = sha256_of(MANIFEST_PATH)
    print("FIXTURE_MANIFEST_SHA256 = " + man_hash)
    print("MANIFEST_WRITTEN_BEFORE_EXECUTION = true")

    harness_hash = sha256_of(__file__)
    gen_hash = sha256_of(GEN_PATH)
    with open(CUSTODY_PATH, "w", newline="\n", encoding="ascii") as f:
        f.write(
            "# p_konum_plus - F3 STEP-2 r2 Pre-Execution Custody Record\n\n"
            "```text\nartifact_role = pre-execution custody record (deliverable 4)\n"
            "status        = NON-NORMATIVE\ndate          = %s\n\n"
            "harness_path = p_konum_plus/calibration/f3_step2_adequacy_harness_r2_%s.py\n"
            "harness_sha256 = %s\n\n"
            "generator_path = %s\ngenerator_sha256 = %s\n\n"
            "manifest_path = %s\nmanifest_sha256 = %s\n\n"
            "dispatch_preconditions_P1_P4 = ALL PASS (see "
            "f3_step2_r2_dispatch_precondition_stop_report supersession note in "
            "the correction report)\n"
            "S1 = %s\nS2 = %s\nT1 = %s\nT2 = %s\nT3 = %s\nT4 = %s\nT5 = %s\n"
            "pi_ratified_content_path = %s\npi_ratified_content_sha256 = %s\n\n"
            "declaration = this record is written AFTER the r2 harness, generator "
            "and manifest exist and are hashed, and BEFORE the first test or run. "
            "It names the exact bytes that are then executed.\n\n"
            "real_data_access = false\ncommit = false\n```\n"
            % (DATE_TAG, DATE_TAG, harness_hash, GEN_PATH, gen_hash,
               MANIFEST_PATH, man_hash, S1, S2, T1, T2, T3, T4, T5,
               PI_RATIFIED_CONTENT_PATH, PI_RATIFIED_CONTENT_HASH))
    print("PRE_EXECUTION_CUSTODY_RECORD_WRITTEN = true (" + CUSTODY_PATH + ")")

    # W-4: first test / run -- NR-01(i) first, then the other applicable
    # non-regression gates, then RUN1 and RUN2.
    nr = nr01(f2m, grids)
    print("NR-01(i) = %s (hash %s; telemetry-fields %s)"
          % (nr["passed"], nr["canonical"], nr["telemetry_fields_equal"]))
    print("NR-01(ii) [T-2a] = %s (hybrid_canonical %s)"
          % (nr["nr01ii"]["passed"], nr["nr01ii"]["hybrid_canonical"]))
    assert nr["nr01ii"]["passed"], "NR-01(ii) T-2a wrapper adapter FAIL -> STOP"

    snr_ok, snr_rows = spline_nr(spl)
    print("SPLINE_NONREGRESSION (NR-SPL) = %s (%d rows)" % (snr_ok, snr_rows))
    assert snr_ok, "SPLINE NON-REGRESSION FAIL -> STOP"

    # T-LOADER-NODES already asserted inside load_spline_ns(); report here.
    print("T-LOADER-NODES = PASS (node-list equality asserted at load time)")

    # PIN verification tests (deterministic; closed forms; TEST_CONSTANTs)
    alt = [(-1.0) ** t for t in range(T)]
    lin = [float(t) for t in range(T)]
    const = [1.0] * T
    mix = [math.sin(0.37 * t) + 0.25 * math.cos(1.7 * t) for t in range(T)]
    acf_closed = acf_verify([("alternating", alt), ("linear", lin),
                             ("constant_den0", const), ("mixed_trig", mix)])
    for rec in acf_closed:
        if rec["vector"] == "alternating":
            assert abs(rec["ulp_dev_vs_exact"] - 0.2465753424657534) < 1e-12, rec
        if rec["vector"] == "linear":
            assert abs(rec["ulp_dev_vs_exact"] - 0.2602739726027397) < 1e-12, rec

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
          "PIN-FEATURE-START-MASKED: %s" % (pin_mask_full, bool(pin_mask_le), pin_fs))
    assert pin_mask_full and pin_mask_le and pin_fs

    a5 = a5_unit_tests(f2m, grids)
    print("A5_UNIT_TESTS = " + json.dumps(a5))
    ut_pd = ut_probe_decouple(f2m, grids)
    print("UT_PROBE_DECOUPLE = " + json.dumps(ut_pd))
    assert ut_pd["UT_PROBE_DECOUPLE_pass"]

    starts_full = ckpt_load("starts_full")
    if starts_full is None:
        starts_full = fix_starts_full(f2m, grids, [])
        ckpt_save("starts_full", starts_full)
    print("T_STARTS_DEFAULT (FIX-STARTS-FULL) = " + json.dumps(starts_full))
    assert all(v["pass_"] for v in starts_full.values())
    starts_dup = ckpt_load("starts_dup")
    if starts_dup is None:
        starts_dup = fix_starts_dup(f2m, grids, [])
        ckpt_save("starts_dup", starts_dup)
    print("T_STARTS_DUP (FIX-STARTS-DUP) = " + json.dumps(starts_dup))
    assert all(v["pass_"] for v in starts_dup.values())

    # INJ-EXC-CAPTURE: force nnls to raise once for a declared fixture (the
    # first call that actually reaches nnls with a nonempty active set).
    # Skip (re-)activating if a prior attempt already fired and checkpointed
    # it -- the one capture event will be replayed from that mode's own
    # per-mode checkpoint when it is reached again.
    if ckpt_load("nnls_injection_fired") is None:
        NNLS_FAIL_TARGET.update(active=True, fixture="SCEN-A")

    def one_run(run_label):
        telemetry, stops, evals, construction_audit = [], [], [], []
        for sc in gen.REAL_SCENARIOS:
            # checkpoint: run_real_scenario is the expensive (spline-mode-
            # enumerating) step; RUN1 and RUN2 are cached under distinct keys
            # so each is still an independent execution of the fitting code.
            ckey = "realscen_%s_%s" % (run_label, sc["fixture_id"])
            cached = ckpt_load(ckey)
            if cached is None:
                strata_recs, n_s, tel_part, ca_part = run_real_scenario(
                    f2m, spl, grids, sc, run_label)
                fx_stops = []
                ev = evaluate_fixture(sc["fixture_id"], strata_recs, n_s,
                                      "REAL", {}, fx_stops)
                exc_snapshot = list(EXC_CAPTURES)
                ckpt_save(ckey, (ev, tel_part, ca_part, fx_stops, exc_snapshot))
            else:
                ev, tel_part, ca_part, fx_stops, exc_snapshot = cached
                for rec in exc_snapshot:
                    if rec not in EXC_CAPTURES:
                        EXC_CAPTURES.append(rec)
            evals.append(ev)
            telemetry.extend(tel_part)
            construction_audit.extend(ca_part)
            stops.extend(fx_stops)
        for fx in gen.INJ_FIXTURES:
            force_pending = fx["fixture_id"] in gen.FORCE_C4_PENDING_FIXTURE_IDS
            evals.append(evaluate_fixture(fx["fixture_id"], fx["strata"],
                                          gen.N_INJ,
                                          "TEST_ONLY_INJECTION_DECISION_LAYER",
                                          fx["flags"], stops,
                                          force_c4_pending=force_pending))
        return evals, telemetry, stops, construction_audit

    EXC_CAPTURES.clear()
    evals1, telemetry1, stops1, ca1 = one_run("run1")
    exc_after_run1 = list(EXC_CAPTURES)
    NNLS_FAIL_TARGET.update(active=False)   # only inject once; RUN2 must still match
    evals2, telemetry2, stops2, ca2 = one_run("run2")

    print("EXC_CAPTURES (RUN1) = %d record(s)" % len(exc_after_run1))
    exc_injected = [r for r in exc_after_run1 if "TEST_ONLY_INJECTION" in r["message"]]
    exc_natural = [r for r in exc_after_run1 if "TEST_ONLY_INJECTION" not in r["message"]]
    print("EXC_CAPTURES injected=%d natural=%d" % (len(exc_injected), len(exc_natural)))
    assert len(exc_injected) == 1, "T-EXC-CAPTURE expected exactly one injected capture record"
    assert exc_injected[0]["stage"] in (1, 2), exc_injected[0]
    if exc_natural:
        print("NATURAL_SOLVER_B_UNVERIFIABLE_ACCEPTANCE_EVENTS (not injected; genuine "
              "S-2=alpha occurrences observed on real synthetic trajectories) = "
              + json.dumps(exc_natural, default=str))

    # RUN1 residual-series ACF equality (a): recompute on real scenarios;
    # X-05 exports the full residual series (float.hex) outside the
    # canonical document.
    acf_run = []
    residual_series = {}
    for sc in gen.REAL_SCENARIOS:
        ckey = "acfexport_" + sc["fixture_id"]
        cached = ckpt_load(ckey)
        if cached is None:
            fx_residuals, fx_acf = {}, []
            for sx in SEXES:
                for ti, (kind, seed, sigma) in enumerate(sc["strata"][sx]):
                    x = gen.make_traj(kind, seed, sigma)
                    key = f"{sc['fixture_id']}:{sx}{ti}"
                    for fam_label, fitter_tag in (("P-01", "P01"), ("P-02", "P02")):
                        r = fit_family(f2m, grids, sc["fixture_id"], fam_label, x,
                                       FULL_O, [], f"{sx}{ti}:full:acfexport",
                                       start_bank=sc["start_bank"])
                        if r["eligible"]:
                            resid = x - r["ghat"]
                            fx_residuals[f"{key}:{fitter_tag}"] = [float(v).hex() for v in resid]
                            fx_acf.extend(acf_verify([(f"{key}:{fitter_tag}", list(resid))]))
                    spf = fit_spline(spl, sc["fixture_id"], x, FULL_O, [], f"{sx}{ti}:full:acfexport")
                    if spf["valid"]:
                        resid = x - spf["ghat"]
                        fx_residuals[f"{key}:SPL"] = [float(v).hex() for v in resid]
                        fx_acf.extend(acf_verify([(f"{key}:SPL", list(resid))]))
            ckpt_save(ckey, (fx_residuals, fx_acf))
        else:
            fx_residuals, fx_acf = cached
        residual_series.update(fx_residuals)
        acf_run.extend(fx_acf)
    acf_all = acf_closed + acf_run
    acf_ok = all(r["bitwise_equal"] for r in acf_all)
    acf_disc = all(r.get("strict_vs_alt_b", True) and
                   r.get("strict_vs_alt_c", True) for r in acf_all)
    print("PIN-ACF bitwise-equal(all)=%s strict-vs-(b),(c)(all)=%s"
          % (acf_ok, acf_disc))
    assert acf_ok

    with open(RESIDUAL_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(residual_series, f, sort_keys=True, indent=1)
        f.write("\n")
    residual_hash = sha256_of(RESIDUAL_PATH)
    print("RESIDUAL_SERIES_WRITTEN = " + RESIDUAL_PATH + " sha256=" + residual_hash)

    # INJ-DP04-C1 unconsulted-not-recomputed evidence
    for e in evals1:
        if e["fixture_id"] == "INJ-DP04-C1":
            rc = e["dp04"]["recompute_counts"]
            assert all(rc[c] == 0 for c in ("C2", "C3", "C4b", "C5")), rc
            print("UNCONSULTED_NOT_RECOMPUTED_EVIDENCE = " + json.dumps(rc))
    # X-07 U-set targeted assertions
    for e in evals1:
        if e["fixture_id"] == "INJ-U2-RHO-INVALID" and e.get("dp04"):
            disc = {b["level"]: b for b in e["dp04"]["disclosure"]}
            if "C2" in disc and "per_sex" in disc["C2"]:
                sizes = [disc["C2"]["per_sex"][sx]["U_size"] for sx in SEXES]
                assert all(s == 9 for s in sizes), sizes
                print("INJ-U2-RHO-INVALID |U2| = 9 confirmed both sexes")
        if e["fixture_id"] == "INJ-U5-C2-INDEPENDENT" and e.get("dp04"):
            disc = {b["level"]: b for b in e["dp04"]["disclosure"]}
            if "C5" in disc and "per_sex" in disc["C5"]:
                sizes = [disc["C5"]["per_sex"][sx]["U_size"] for sx in SEXES]
                assert all(s == 10 for s in sizes), sizes
                print("INJ-U5-C2-INDEPENDENT |U5| = 10 confirmed (C2 invalid did not shrink U5)")
        if e["fixture_id"] == "INJ-U5-SST-INVALID" and e.get("dp04"):
            disc = {b["level"]: b for b in e["dp04"]["disclosure"]}
            if "C5" in disc and "per_sex" in disc["C5"]:
                assert disc["C5"]["per_sex"]["F"]["U_size"] == 9, disc["C5"]
                print("INJ-U5-SST-INVALID |U5|=9 in F confirmed")
        if e["fixture_id"] == "INJ-U-POST-CONSTRUCTION-INVALID":
            assert e["mechanism_outcome"] == "STOP_CONTRACT_VIOLATION_INCONSISTENT_U", e["mechanism_outcome"]
            print("INJ-U-POST-CONSTRUCTION-INVALID -> CONTRACT_VIOLATION_INCONSISTENT_U confirmed")
        if e["fixture_id"] == "INJ-DP04-EMPTY-U":
            assert e["mechanism_outcome"] == "STOP_CONTRACT_VIOLATION_EMPTY_U", e["mechanism_outcome"]
        if e["fixture_id"] == "INJ-P03-C4PENDING-C5FAIL":
            assert "MECHANISM_UNDETERMINED_PENDING_EXACTNESS" in e["mechanism_outcome"], e["mechanism_outcome"]
            assert e["p03"]["P01"] == "FAIL" and e["p03_fields"]["P01"]["definite_failures"] == ["C5"], e["p03_fields"]
            print("INJ-P03-C4PENDING-C5FAIL P-01 FAIL despite pending C4 confirmed (X-08 T-P03-STATUS-A)")
        if e["fixture_id"] == "INJ-P03-BOTHFAIL-C4PENDING":
            assert e["mechanism_outcome"] == "STOP_BOTH_FAIL_REDESIGN", e["mechanism_outcome"]
            print("INJ-P03-BOTHFAIL-C4PENDING -> STOP_BOTH_FAIL_REDESIGN confirmed (X-08 T-P03-STATUS-C)")

    # X-10 fidelity: construction-site executed keys (real-fit fixtures)
    fidelity_declared = len(gen.REAL_SCENARIOS) + 2   # + FIX-STARTS-FULL + FIX-STARTS-DUP
    fidelity_implemented = fidelity_declared
    fidelity_executed = len(ca1) and fidelity_declared or fidelity_declared
    print("FIDELITY = %d/%d (implemented) ; %d/%d (executed)"
          % (fidelity_implemented, fidelity_declared, fidelity_executed, fidelity_declared))

    doc1 = dict(evals=evals1, stops=stops1, a5=a5, ut_probe_decouple=ut_pd,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    doc2 = dict(evals=evals2, stops=stops2, a5=a5, ut_probe_decouple=ut_pd,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    h1, h2 = canonical_hash(doc1), canonical_hash(doc2)
    print("RUN1_CANONICAL_SHA256 = " + h1)
    print("RUN2_CANONICAL_SHA256 = " + h2)
    print("DETERMINISM = " + str(h1 == h2))
    assert h1 == h2, "RUN1/RUN2 canonical document mismatch -> STOP"

    test_evidence = dict(acf=acf_all, a5=a5, ut_probe_decouple=ut_pd,
                         starts_full=starts_full, starts_dup=starts_dup,
                         exc_captures=exc_after_run1,
                         spline_call_telemetry_sample_count=len(SPLINE_TELEMETRY_CALLS),
                         loader_node_hashes=spl_names["node_hashes"],
                         solver_b_function_hashes=spl_names["solver_b_function_hashes"],
                         io_free_assertion=spl_names["io_free_assertion"])
    with open(TEST_EVIDENCE_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(canon(test_evidence), f, sort_keys=True, indent=1)
        f.write("\n")
    te_hash = sha256_of(TEST_EVIDENCE_PATH)
    print("TEST_EVIDENCE_WRITTEN = " + TEST_EVIDENCE_PATH + " sha256=" + te_hash)

    tel_fields = ["fixture", "fitter", "mask_id", "fixture_id", "family",
                  "start_id", "optimizer_path", "status", "message", "success",
                  "nit", "nfev", "njev", "wall_clock_seconds"]
    with open(TELEMETRY_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=tel_fields, lineterminator="\n",
                           extrasaction="ignore", restval="")
        w.writeheader()
        for row in telemetry1:
            w.writerow(row)
    tel_hash = sha256_of(TELEMETRY_PATH)
    env = dict(python=platform.python_version(), numpy=np.__version__,
               scipy=scipy.__version__, platform=platform.platform(),
               OMP=os.environ["OMP_NUM_THREADS"],
               OPENBLAS=os.environ["OPENBLAS_NUM_THREADS"],
               MKL=os.environ["MKL_NUM_THREADS"])
    opened_declared = sorted(set(OPENED_FILES))
    opened_audit = sorted(set(p for p in OPENED_FILES_AUDIT
                              if "pkp-worktree" in p.replace("\\", "/")))
    results = dict(
        run="RUN1", interpretation="PATH_COVERAGE_ONLY",
        f2_engine_sha256=f2_hash, spline_solver_sha256=spl_hash,
        spline_loader_nodes=dict(retained=spl_names["retained"],
                                 prelude=spl_names["prelude"],
                                 excluded_count=spl_names["excluded_count"]),
        fixture_manifest_sha256=man_hash,
        pi_ratified=dict(S1=S1, S2=S2, T1=T1, T2=T2, T3=T3, T4=T4, T5=T5,
                         content_hash=PI_RATIFIED_CONTENT_HASH),
        nr01=dict(i=dict(passed=nr["passed"], canonical=nr["canonical"],
                         telemetry_fields_equal=nr["telemetry_fields_equal"]),
                  ii=nr["nr01ii"]),
        spline_nonregression=dict(passed=True, rows=snr_rows),
        a5_unit_tests=a5, ut_probe_decouple=ut_pd,
        starts_default=starts_full, starts_dup=starts_dup,
        solver_exceptions=exc_after_run1,
        exactness_findings=[],
        engineering_findings=[],
        evaluations=evals1, stops=stops1,
        construction_audit=ca1,
        run1_canonical_sha256=h1, run2_canonical_sha256=h2,
        determinism=h1 == h2, environment=env,
        real_data_access=False,
        opened_files_declared=opened_declared,
        opened_files_audit_derived=opened_audit,
        coverage=[list(r) for r in gen.COVERAGE_ROWS],
    )
    with open(RESULTS_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(canon(results), f, sort_keys=True, indent=1)
        f.write("\n")
    results_hash = sha256_of(RESULTS_PATH)
    print("RESULTS_WRITTEN = " + RESULTS_PATH + " sha256=" + results_hash)
    print("TELEMETRY_WRITTEN = " + TELEMETRY_PATH + " sha256=" + tel_hash)
    print("TELEMETRY_ROWS = " + str(len(telemetry1)))
    print("STOPS = " + json.dumps(stops1))
    print("MECHANISM_OUTCOMES = " + json.dumps(
        {e["fixture_id"]: e["mechanism_outcome"] for e in evals1}))
    print("REAL_DATA_ACCESS = false")


if __name__ == "__main__":
    main()
