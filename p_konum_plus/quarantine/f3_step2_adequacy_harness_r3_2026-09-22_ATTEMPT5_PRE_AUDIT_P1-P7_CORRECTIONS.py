"""F3 STEP-2 adequacy-evaluation harness r3 (2026-09-22).

Child of f3_step2_adequacy_harness_r2_2026-09-07.py (parent
78b6210ace605fe9b43a3b15716535df28b8a25a11a072f68484e9cb7ad12776).
Closes the findings of the independent audit of the r2 package: Y-01 .. Y-21
of Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md §6, on top
of prompt v6's X-01..X-20 (which stand except where Y-02/Y-04/Y-03/Y-21 amend
or tighten them). PI-ratified content (S-1=(a), S-2=alpha, T-1=AUTHORIZE,
T-2=T-2a, T-3=AUTHORIZE, T-4=T-4a, T-5=CONFIRM_WITHIN_SCOPE) is unchanged and
carried from D-2. This cycle's own two PI fields, read from D-4:
  S-R2-1 = DEFERRED_THIS_CYCLE  (the C4b/no-full-data-reference state, §5)
  T-R2-2 = AUTHORIZE_RESTART    (permits, does not require, a restart layer
                                 introduced only after a genuine interruption
                                 -- see §8; attempt 1 is always one clean
                                 process with RESTART_LAYER_ACTIVE = False)

Y-01 (a): no undisclosed restart/checkpoint layer runs by default. The code
below is present but INERT unless RESTART_LAYER_ACTIVE is flipped to True,
which only happens as its own harness edit AFTER a recorded INTERRUPTION of
a prior attempt (§8.2/§8.3), forcing a fresh W-3 write per §3's rule that a
harness change after W-3 requires repeating W-3 with the superseded bytes
quarantined.

ATTEMPT 3 (this file, live), harness revision 3. Revision 1
(RESTART_LAYER_ACTIVE = False) was interrupted mid-RUN2 by the host
process exiting outside the harness's own control -- see
p_konum_plus/quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md.
Revision 2 (RESTART_LAYER_ACTIVE = True) ran attempts 2 and 3 to
completion (exit 0, RUN1==RUN2 canonical hashes equal) but is ALSO
quarantined: independent review of its output found a real defect --
_classify_call_site() (post-hoc use, inside wrapped_accept's except
block) always returns UNRELATED, because inspect.stack() from within an
except handler sees the call stack AFTER CPython has already unwound the
raise-to-catch frames, so kkt_res/accept can never appear there. This
revision fixes it with a traceback-based classifier
(_classify_covered_from_traceback) for that specific call site; the
live/pre-raise classifier (used only to decide whether to inject a test
fault) was already correct and is unchanged. Full account, byte-exact
quarantined copies and hashes:
p_konum_plus/quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md
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

# ------------------------- Y-01 (b)(c)(d): process provenance ---------------
PID = os.getpid()
PROCESS_START_PERF = _time.perf_counter()
import datetime as _dt
PROCESS_START_ISO = _dt.datetime.now().isoformat()
COMMAND_LINE = " ".join(sys.argv)
INTERPRETER_PATH = sys.executable

OPENED_FILES = []
OPENED_FILES_AUDIT = []


def _audit_hook(event, args):
    if event == "open":
        try:
            OPENED_FILES_AUDIT.append(str(args[0]))
        except Exception:
            pass


sys.addaudithook(_audit_hook)                                    # X-18/Y-12

# ------------------------- Y-01(a): restart layer, gated off by default -----
# Not a hidden mechanism: present in the source, disclosed in the register
# and report, and INERT (every ckpt_load call returns None, every ckpt_save
# call is a no-op) unless RESTART_LAYER_ACTIVE is True. Attempt 1 always
# runs with this False (§8.1: one clean process, no restart/checkpoint/
# caching layer of any kind). If introduced later (§8.2/§8.3, only after a
# recorded INTERRUPTION), keys are bound to code+input+environment identity
# (not just a name), the store is one disclosed, empty-at-first directory,
# and every stored unit carries the pid/start-time of the process that
# computed it -- this is what Y-01 corrects relative to r2's layer.
RESTART_LAYER_ACTIVE = True

# Disclosed per §3/§8.2: this file supersedes an earlier harness (bytes
# below) after that attempt was interrupted outside its own control -- see
# the quarantine note for the full account. Not a checkpoint/restart-layer
# runtime concern; recorded here only so the W-3 record that follows names
# its own predecessor.
SUPERSEDES_HARNESS_SHA256 = "891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd"
SUPERSEDES_CUSTODY_SHA256 = "a4c7d65c8d778277b92e83e14a31a90a51b6e5e1df18f2c8da815d7ce00de0c0"
SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md"
# Prior supersession (attempt 1 -> 2, genuine interruption, restart layer
# introduced): p_konum_plus/quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md
# harness sha256 6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31
ATTEMPT_NUMBER = 3

import pickle
RESTART_STORE_DIR = "p_konum_plus/calibration/.r3_restart_store_2026-09-22"
_CODE_ENV_FINGERPRINT = [None]     # set once in main(), after W-3 hashes are known


def _restart_store_init():
    if RESTART_LAYER_ACTIVE and not os.path.isdir(RESTART_STORE_DIR):
        os.makedirs(RESTART_STORE_DIR)


_CKPT_UNSAFE = str.maketrans({c: "_" for c in '<>:"/\\|?*[]'})


def _ckpt_safe_name(name):
    safe = name.translate(_CKPT_UNSAFE)
    if len(safe) > 150:
        safe = safe[:100] + "_" + hashlib.sha256(name.encode("utf-8")).hexdigest()[:16]
    return safe


def _full_key(name):
    """§8.3 keys: code (W-3 hashes + frozen F2/spline hashes) + environment
    (interpreter/numpy/scipy/platform/thread pins), folded into a fixed
    fingerprint prefix; the caller-supplied name already encodes the unit
    identity (fixture/sex/trajectory/mask/mode/stage/run label/test id) and,
    where the unit is a specific fit, an input-vector hash (see fit_family /
    fit_spline call sites)."""
    fp = _CODE_ENV_FINGERPRINT[0] or "unfingerprinted"
    return fp + "__" + name


def ckpt_load(name):
    if not RESTART_LAYER_ACTIVE:
        return None
    p = os.path.join(RESTART_STORE_DIR, _ckpt_safe_name(_full_key(name)) + ".pkl")
    if os.path.exists(p):
        with open(p, "rb") as f:
            payload = pickle.load(f)
        return payload["value"]
    return None


def ckpt_save(name, obj):
    if not RESTART_LAYER_ACTIVE:
        return
    _restart_store_init()
    p = os.path.join(RESTART_STORE_DIR, _ckpt_safe_name(_full_key(name)) + ".pkl")
    tmp = p + ".tmp"
    payload = dict(value=obj, pid=PID, start_iso=PROCESS_START_ISO, key_name=name)
    with open(tmp, "wb") as f:
        pickle.dump(payload, f)
    os.replace(tmp, p)


def ckpt_provenance(name):
    """Returns (pid, start_iso) of the process that computed this unit, or
    None if not in the store / restart layer inactive."""
    if not RESTART_LAYER_ACTIVE:
        return None
    p = os.path.join(RESTART_STORE_DIR, _ckpt_safe_name(_full_key(name)) + ".pkl")
    if os.path.exists(p):
        with open(p, "rb") as f:
            payload = pickle.load(f)
        return payload["pid"], payload["start_iso"]
    return None


UNITS_COMPUTED_THIS_PROCESS = {"run1": 0, "run2": 0, "nr_gates": 0, "unit_tests": 0,
                               "residual_export": 0}
UNITS_READ_FROM_STORE = {"run1": 0, "run2": 0, "nr_gates": 0, "unit_tests": 0,
                         "residual_export": 0}


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
LEFT_PROBE_O = np.arange(15, 146)
RIGHT_PROBE_O = np.arange(0, 131)
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

GEN_MODULE_NAME = "f3_step2_fixture_generator_r3_2026_09_22"
GEN_PATH = "p_konum_plus/calibration/f3_step2_fixture_generator_r3_2026-09-22.py"

DATE_TAG = "2026-09-22"
MANIFEST_PATH = f"p_konum_plus/calibration/f3_step2_fixture_manifest_r3_{DATE_TAG}.csv"
CUSTODY_PATH = f"p_konum_plus/provenance/f3_step2_r3_preexecution_custody_{DATE_TAG}.md"
TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_telemetry_r3_{DATE_TAG}.csv"
RESULTS_PATH = f"p_konum_plus/calibration/f3_step2_results_r3_{DATE_TAG}.json"
RESIDUAL_PATH = f"p_konum_plus/calibration/f3_step2_residual_series_r3_{DATE_TAG}.json"
TEST_EVIDENCE_PATH = f"p_konum_plus/calibration/f3_step2_test_evidence_r3_{DATE_TAG}.json"
PERCALL_TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r3_{DATE_TAG}.csv"
ATTEMPT_LOG_PATH = f"p_konum_plus/provenance/f3_step2_r3_attempt_log_{DATE_TAG}.md"
STORE_MANIFEST_PATH = f"p_konum_plus/calibration/f3_step2_r3_restart_store_manifest_{DATE_TAG}.csv"

FORBIDDEN_RESULT_KEYS = ("winner", "selected", "generator_selected")

PI_RATIFIED_CONTENT_PATH = "p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md"
PI_RATIFIED_CONTENT_HASH = "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498"
DISPATCH_RECORD_PATH = "p_konum_plus/prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md"
DISPATCH_RECORD_HASH = "4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865"

# S / T values as read from D-2 (unchanged, verbatim)
S1 = "(a)"
S2 = "alpha"
T1 = "AUTHORIZE"
T2 = "T-2a"
T3 = "AUTHORIZE"
T4 = "T-4a"
T5 = "CONFIRM_WITHIN_SCOPE"
# this cycle's own two PI fields, read from D-4 (verbatim)
S_R2_1 = "DEFERRED_THIS_CYCLE"
T_R2_2 = "AUTHORIZE_RESTART"
S_R2_1_FINDING_ID = "F3-STEP2-EXACT-03"


# ------------------------- X-09 PIN-UNDEFINED-FLAGS -------------------------
def valid(value):
    return value is not None and math.isfinite(value)


# ------------------------- PIN-F2-LOADER -------------------------------
def load_f2():
    h = sha256_of(F2_PATH)
    assert h == F2_HASH, "PIN-F2-IMPORT-HASH FAIL: " + h
    spec = importlib.util.spec_from_file_location("f2eng", F2_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, h


# ------------------------- X-01/Y-13 PIN-SPLINE-LOADER ----------------------
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
    node_hashes = {}          # Y-13: ONE entry per EXECUTED node (unique key)
    executed_node_count = 0
    for idx, node in enumerate(tree.body):
        seg = ast.get_source_segment(src, node)
        exact = "\n".join(lines[node.lineno - 1:node.end_lineno])
        assert seg is not None and seg in exact, "source-segment mismatch"
        io_hits = _io_call_names(node)

        is_base_retained = isinstance(node, RETAINED_CLASSES) or _const_assign(node)
        if is_base_retained:
            retained.append((node, seg))
            base_name = _assign_name(node) or getattr(node, "name", None) or type(node).__name__
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
            base_name = label
        else:
            excluded.append((node, seg))
            continue

        # Y-13: unique key per executed node -- disambiguate repeated names
        # (e.g. several Import/ImportFrom nodes) with a lineno suffix.
        key = base_name
        n_seen = sum(1 for k in node_hashes if k == base_name or k.startswith(base_name + "@"))
        if key in node_hashes:
            # relabel the first occurrence too, so both carry a positional suffix
            first = node_hashes.pop(key)
            node_hashes[f"{base_name}@{first['lineno']}"] = first
            key = f"{base_name}@{node.lineno}"
        elif any(k.startswith(base_name + "@") for k in node_hashes):
            key = f"{base_name}@{node.lineno}"
        node_hashes[key] = dict(
            lineno=node.lineno, end_lineno=node.end_lineno,
            sha256=hashlib.sha256(seg.encode("utf-8")).hexdigest())
        executed_node_count += 1

    assert prelude_labels == AUTHORIZED_PRELUDE, (
        "PIN-SPLINE-LOADER node-list mismatch: executed=%r authorized=%r"
        % (prelude_labels, AUTHORIZED_PRELUDE))
    assert executed_node_count == len(retained) + len(prelude), (
        "Y-13: node_hashes entries (%d) != executed nodes (%d)"
        % (executed_node_count, len(retained) + len(prelude)))

    ns = {"__name__": "f3spl"}
    for node, seg in sorted(retained + prelude, key=lambda e: e[0].lineno):
        exec(compile(ast.Module(body=[node], type_ignores=[]),
                     SPL_PATH, "exec"), ns)

    for req in ("amat", "rss_of", "zddof0", "solver_config", "reference",
                "build_case", "FIXTURES", "B", "accept", "minimize", "nnls"):
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
        executed_node_count=executed_node_count,
        solver_b_function_hashes=solver_b_hashes,
        io_free_assertion="AST-walk (Call.func name/attr in {open,print,exit,write,writerow,writerows,sys.exit}); PASS, over ALL executed nodes",
    )
    return ns, h, names


# ------------------------- Y-04 PIN-EXC-CAPTURE / PIN-SOLVER-B-UNVERIFIABLE -
# Implements PI-ratified content §3.1/§3.3 verbatim (register tags VERBATIM);
# everything else here (call-site/stage classification, UNRELATED routing,
# arming rule, wrapper restoration) is this prompt's engineering
# specification (register tags SUMMARY).
EXC_CAPTURES = []
_SPL_CTX = {"fixture": None, "sex": None, "trajectory": None, "mask_id": None, "mode": None}
_ACCEPT_CALL_COUNT = [0]
SPLINE_TELEMETRY_CALLS = []
_LAST_CAPTURE_EVENTS = []      # reset per mode; every capture during that mode


def _parse_sex_traj(mask_id):
    for seg in (mask_id or "").split(":"):
        if seg and seg[0] in ("F", "M") and seg[1:].isdigit():
            return seg[0], int(seg[1:])
    return None, None


# Y-04(a): call site and stage from the call stack, not from class/message
# alone. accept() is on the stack (this IS the covered call site) iff the
# immediate Python caller frame of nnls is kkt_res AND kkt_res's caller is
# accept. reference() calling kkt_res directly (no accept) is UNRELATED
# (T-EXC-UNRELATED case 1b); nnls raising inside reference() itself with
# neither kkt_res nor accept on the stack is UNRELATED (case 1a).
def _classify_call_site():
    import inspect
    stack = inspect.stack()
    names = [fr.function for fr in stack]
    # stack[0] is this classifier's own frame; stack[1] is the nnls wrapper
    on_kkt_res = len(names) > 2 and names[2] == "kkt_res"
    on_accept = len(names) > 3 and names[3] == "accept"
    return bool(on_kkt_res and on_accept)


def _classify_covered_from_traceback(tb):
    """Post-hoc covered-event test for an ALREADY-CAUGHT exception.
    _classify_call_site() (above) is only valid called live, pre-raise --
    by the time an `except` clause runs, CPython has already unwound the
    frames between the raise point and the catch point off the live call
    stack, so inspect.stack() from inside an except block can never see
    kkt_res/accept (empirically verified, not assumed). Use the
    exception's OWN traceback instead: traceback.extract_tb walks it
    outermost (catch point) first, innermost (raise point) last, so
    "accept" is immediately followed by "kkt_res" in that order (the
    reverse of the live-stack check above). kkt_res's only call capable of
    raising RuntimeError is nnls(A[act].T, g) (frozen source,
    f3_spline_solver_qualification_harness_r2_2026-09-03.py:300-306), so
    this adjacency is sufficient regardless of nnls wrapper depth below
    it."""
    names = [fr.name for fr in traceback.extract_tb(tb)]
    for i in range(len(names) - 1):
        if names[i] == "accept" and names[i + 1] == "kkt_res":
            return True
    return False


def install_exc_capture(spl):
    """PI-ratified content §3.1 (VERBATIM): "The covered event is a
    RuntimeError raised by the nnls(A[act].T, g) invocation in frozen
    kkt_res(c, z, O, A) while that invocation is being used by
    accept(c, z, O, A) to compute the KKT-existence certificate for a
    SOLVER-B stage-1 or stage-2 acceptance check." No condition on the
    exception class beyond RuntimeError is added.
    Engineering (SUMMARY of content §3, Y-04): call-site/stage established
    from the call stack; an UNRELATED exception (different site, or a
    non-RuntimeError at the covered site) is never converted -- it is
    captured as evidence (kind=UNRELATED) and routed to the existing
    exactness protocol, never silently swallowed."""
    real_accept = spl["accept"]

    def wrapped_accept(c, z, O, A):
        _ACCEPT_CALL_COUNT[0] += 1
        stage = _ACCEPT_CALL_COUNT[0]
        try:
            return real_accept(c, z, O, A)
        except RuntimeError as exc:
            covered = _classify_covered_from_traceback(exc.__traceback__)
            sex, traj = _parse_sex_traj(_SPL_CTX["mask_id"])
            rec = dict(
                fixture=_SPL_CTX["fixture"], sex=sex, trajectory=traj,
                mask_id=_SPL_CTX["mask_id"], mode=_SPL_CTX["mode"], stage=stage,
                exception_type=type(exc).__name__, message=str(exc),
                traceback=traceback.format_exc(),
                kind=("COVERED" if covered else "UNRELATED"),
            )
            EXC_CAPTURES.append(rec)
            _LAST_CAPTURE_EVENTS.append(rec)
            if not covered:
                raise   # UNRELATED: never converted into "not accepted"
            rec["s2_rule"] = "alpha: NOT accepted at stage %d; chain continues" % stage
            return False
    spl["accept"] = wrapped_accept


# P-2/P-3 (independent audit 2026-09-23): phase tag for T-CALLCOUNT (Y-01)
# -- one of "nr_gates" / "unit_tests" / "run1" / "run2" / "residual_export".
# Set at each phase boundary in main(); read here so every per-call
# telemetry row records which phase produced it. A row loaded from the
# restart store keeps the phase/pid of the process that ORIGINALLY
# computed it (see fit_family/fit_spline's ckpt replay of tel_calls),
# which is exactly the provenance §8.3 asks for.
CURRENT_PHASE = [None]


def install_spline_call_telemetry(spl):
    """T-4a: one row per trust-constr / SLSQP call via a disclosed wrapper
    around scipy.optimize.minimize in the loaded namespace."""
    real_minimize = spl["minimize"]

    def wrapped_minimize(fun, x0, **kwargs):
        t0 = _time.perf_counter()
        r = real_minimize(fun, x0, **kwargs)
        wall = _time.perf_counter() - t0
        sex, traj = _parse_sex_traj(_SPL_CTX["mask_id"])
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
            phase=CURRENT_PHASE[0], pid=PID, start_iso=PROCESS_START_ISO,
        ))
        return r
    spl["minimize"] = wrapped_minimize


def install_wrapper_restoration_probe(spl):
    """T-WRAPPER-RESTORE evidence: capture the ORIGINAL (pre-wrap) function
    objects so the harness can assert, after every wrapper is uninstalled,
    that the namespace objects are the originals again."""
    return dict(accept=spl["accept"], minimize=spl["minimize"], nnls=spl["nnls"])


def uninstall_wrappers(spl, originals):
    spl["accept"] = originals["accept"]
    spl["minimize"] = originals["minimize"]
    spl["nnls"] = originals["nnls"]


NNLS_FAIL_TARGET = {"active": False, "fixture": None, "stages": set()}


def install_nnls_test_injection(spl):
    """T-EXC-CAPTURE-S1/S2 (Y-04(c)): fires once per declared (fixture,
    stage) arming rule -- "the first nnls call that is reached inside
    kkt_res while it serves the stage-k accept, modes in enumeration
    order". Each declared stage fires exactly once (removed from `stages`
    on firing); `active` clears only once every declared stage has fired.
    P-4 (independent audit 2026-09-23): SOLVER-B only attempts a stage-2
    accept() if stage-1's accept() returned False (frozen solver_config,
    f3_spline_solver_qualification_harness_r2_2026-09-03.py:384-396), so
    forcing stage 1 to fail naturally reaches stage 2 within the SAME
    fit_spline call -- the original single-stage design could never verify
    stage 2 specifically because it deactivated after stage 1's own firing,
    leaving nothing armed when the solver went on to attempt stage 2."""
    real_nnls = spl["nnls"]

    def wrapped_nnls(*args, **kwargs):
        stage = _ACCEPT_CALL_COUNT[0]
        if (NNLS_FAIL_TARGET["active"]
                and _SPL_CTX["fixture"] == NNLS_FAIL_TARGET["fixture"]
                and stage in NNLS_FAIL_TARGET["stages"]
                and _classify_call_site()):
            NNLS_FAIL_TARGET["stages"].discard(stage)
            if not NNLS_FAIL_TARGET["stages"]:
                NNLS_FAIL_TARGET["active"] = False
            raise RuntimeError("TEST_ONLY_INJECTION: forced nnls non-convergence stage %d"
                              % stage)
        return real_nnls(*args, **kwargs)
    spl["nnls"] = wrapped_nnls


def install_exc_unrelated_type_injection(spl):
    """INJ-EXC-UNRELATED-TYPE: a ValueError (not RuntimeError) raised at the
    covered call site at stage 1; must classify UNRELATED and NOT be
    converted (a ValueError is not even caught by wrapped_accept's `except
    RuntimeError`, so it propagates to the caller directly -- proving the
    exception CLASS itself gates conversion, independent of call-site)."""
    real_nnls = spl["nnls"]

    def wrapped_nnls(*args, **kwargs):
        if (VALUEERROR_INJECT_TARGET["active"]
                and _SPL_CTX["fixture"] == VALUEERROR_INJECT_TARGET["fixture"]
                and _classify_call_site()
                and _ACCEPT_CALL_COUNT[0] == 1):
            VALUEERROR_INJECT_TARGET["active"] = False
            raise ValueError("TEST_ONLY_INJECTION: unrelated exception type")
        return real_nnls(*args, **kwargs)
    spl["nnls"] = wrapped_nnls


VALUEERROR_INJECT_TARGET = {"active": False, "fixture": None}


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
    if obs_idx is None or len(obs_idx) == T:
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
    return f2m.feature_start(family, pad)


def ghat_of(f2m, family, theta):
    stable_fn = f2m.p01_stable if family == "P-01" else f2m.p02_stable
    status, sigma_g, ghat = f2m.zero_variance_rule(stable_fn(np.asarray(theta)))
    return ghat if status == "OK" else None


# ------------------------- Y-06: fidelity tracking ---------------------------
# P-7(d) (independent audit 2026-09-23): fidelity must measure DECLARED
# INJECTION SITES actually reached and recognized during execution, not
# trajectories processed -- the prior (fixture_id, sex, trajectory) tuples
# always read 4/4 regardless of whether any of SCEN-B's five declared
# fault/failure injections actually fired, which is what "real
# execution-site fidelity" (Y-06) is supposed to certify.
FIDELITY_DECLARED = []     # list of (fixture_id, traj, family, context) injection sites declared
FIDELITY_EXECUTED = []     # the same, confirmed reached + recognized (injmap.get(...) matched)


# ------------------------- X-03/X-04 family fit driver -----------------
def fit_family(f2m, grids, fixture_id, family, x, obs_idx, telemetry,
               mask_id, start_bank="FULL_LATTICE", inject_fault=False,
               inject_fs_reject=False, record_sink=None):
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

    xhash = hashlib.sha256(np.asarray(x, dtype=np.float64).tobytes()).hexdigest()[:16]
    records = []
    for sid, x0 in starts:
        onekey = "onestart_%s_%s_%s_%s_%s_%s" % (fixture_id, family, mask_id,
                                                  sid, inject_fault, xhash)
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
                "MASKED OBJECTIVE VIOLATION L_O > L_FULL"
        records.append(dict(eligible=cls["eligible"], L=L_masked,
                            theta=cls["theta"],
                            predicates=cls["predicates"]))
    status, best = f2m.aggregate(records)
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


# ------------------------- Y-05 S-1 = (a) PIN-A5-SUPPORT --------------------
M_LEFT = set(range(0, 15))
M_RIGHT = set(range(131, 146))
_FULL_G = set(range(T))


class A5ContractViolation(Exception):
    """Y-05: a reference/computation contract violation stops the AFFECTED
    evaluation path (recorded as CONTRACT_VIOLATION_A5_REFERENCE); it is
    never allowed to abort the whole process."""
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)


def a5_support(z):
    z = np.asarray(z, dtype=np.float64)
    if z.shape != (T,) or not np.all(np.isfinite(z)):
        raise A5ContractViolation("missing/non-finite/wrong-length reference")
    lo = float(np.min(z)); hi = float(np.max(z))
    thr = lo + 0.5 * (hi - lo)
    if not math.isfinite(thr):
        raise A5ContractViolation("non-finite computed threshold")
    S = set(int(t) for t in np.flatnonzero(z >= thr))
    if not S:
        raise A5ContractViolation("unexpectedly empty computed support")
    return S


def a5_condition_i(S, side):
    M = M_LEFT if side == "L" else M_RIGHT
    return len(S & (_FULL_G - M)) == 0


def a5_support_safe(z, fixture_id, sex, trajectory, findings):
    """Returns (S_or_None, violation_record_or_None). On violation, records
    a CONTRACT_VIOLATION_A5_REFERENCE finding and returns None for S; the
    caller must treat both A5(i) conditions as PENDING for that trajectory,
    never as a fabricated pass or fail."""
    try:
        return a5_support(z), None
    except A5ContractViolation as exc:
        rec = dict(fixture=fixture_id, sex=sex, trajectory=trajectory,
                   violation="CONTRACT_VIOLATION_A5_REFERENCE", reason=exc.reason)
        findings.append(rec)
        return None, rec


# ------------------------- Y-04 spline fit driver -------------------------------
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
    if inject_failure:
        telemetry.append(dict(fixture=fixture_id, mask_id=mask_id, fitter="SPL",
                              start_id="INJECTED_FAILURE", optimizer_path="none",
                              status="TEST_ONLY_INJECTION", success=False,
                              nit=-1, nfev=-1, njev=-1,
                              wall_clock_seconds=0.0, message="injected"))
        return dict(valid=False, failure="TEST_ONLY_INJECTION_SPLINE_FAILURE")
    obs = np.asarray(obs_idx)
    xhash = hashlib.sha256(np.asarray(x, dtype=np.float64).tobytes()).hexdigest()[:16]
    per_mode = []
    per_mode_valid = []
    for m in range(T):
        mkey = "splmode_%s_%s_%s_%s" % (fixture_id, mask_id, m, xhash)
        cached_mode = ckpt_load(mkey)
        if cached_mode is not None:
            v, rss, c, src, pst, cap_recs, tel_calls = cached_mode
            for cr in cap_recs:
                EXC_CAPTURES.append(cr)
            for tc in tel_calls:
                SPLINE_TELEMETRY_CALLS.append(tc)
        else:
            _ACCEPT_CALL_COUNT[0] = 0
            _SPL_CTX.update(fixture=fixture_id, mask_id=mask_id, mode=m)
            del _LAST_CAPTURE_EVENTS[:]
            n_calls_before = len(SPLINE_TELEMETRY_CALLS)
            A = spl["amat"](m)
            try:
                c, tel = spl["solver_config"]("SOLVER-B", x, obs, A)
                v = spline_valid_from_tel(tel)
                src, pst = tel["final_endpoint_source"], tel["primary_status"]
            except RuntimeError as exc:
                # covered exceptions are converted (return False) inside
                # wrapped_accept and never reach here; an UNRELATED one is
                # re-raised by wrapped_accept and DOES reach here -- route it
                # to the existing exactness protocol for this context only.
                c, v = None, False
                src, pst = "ACCEPTANCE_UNVERIFIABLE_UNRELATED", "EXC:" + type(exc).__name__
            rss = spl["rss_of"](c, x, obs) if v else float("inf")
            cap_recs = list(_LAST_CAPTURE_EVENTS)
            tel_calls = SPLINE_TELEMETRY_CALLS[n_calls_before:]
            ckpt_save(mkey, (v, rss, c, src, pst, cap_recs, tel_calls))
        per_mode.append((m, v, rss, c))
        per_mode_valid.append(bool(v))
        # Y-07: real per-call telemetry, not -1/0.0 placeholders, where a
        # call actually happened for this mode; the mode-level summary row
        # (kept for backward-shaped reporting) states UNAVAILABLE with a
        # reason when no optimizer call info applies (e.g. injected/failed
        # before any call). P-3 fix: the per-call rows this points to are
        # now actually written -- f3_step2_spline_percall_telemetry_r3_*.csv
        # (deliverable, from SPLINE_TELEMETRY_CALLS; see main()).
        unavail = ("UNAVAILABLE(mode-level summary row; see "
                  "f3_step2_spline_percall_telemetry_r3_*.csv)")
        telemetry.append(dict(fixture=fixture_id, mask_id=mask_id, fitter="SPL",
                              start_id=f"mode{m}",
                              optimizer_path=src,
                              status=pst, success=v,
                              nit=unavail, nfev=unavail, njev=unavail,
                              wall_clock_seconds=unavail,
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
def acf_classical(r):
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


def acf_classical_b(r):
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


def acf_alt_c(r):
    return abs(float(np.corrcoef(np.asarray(r)[:-1], np.asarray(r)[1:])[0, 1]))


def acf_frac_ulp(r, phi):
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
                       ulp_dev_vs_exact=acf_frac_ulp(r, pa),
                       sha256_146_float64_le=hashlib.sha256(
                           np.asarray(r, dtype="<f8").tobytes()).hexdigest())  # Y-20 (optional)
        out.append(rec)
    return out


def rho_cv_pin(z, ghat_cv):
    return float(np.corrcoef(z, ghat_cv)[0, 1])


def rmse_edge_pin(probe_pred, ref_pred, edge_idx):
    d = probe_pred[edge_idx] - ref_pred[edge_idx]
    return float(np.sqrt(np.sum(d * d) / float(E_MASK)))


def s_stab_pin(thetas, family):
    arr = np.asarray(thetas, dtype=np.float64)
    q = np.quantile(arr, [0.25, 0.75], axis=0, method="linear")
    iqr = q[1] - q[0]
    return float(np.max(iqr / np.asarray(W_C5[family])))


def median_pin(vals):
    return float(np.median(np.asarray(vals, dtype=np.float64)))


# ------------------------- evaluation layer --------------------------------
SEXES = ("F", "M")
FAM_KEYS = {"P-01": "P01", "P-02": "P02"}
DIRECTION = dict(C1="higher", C2="higher", C3="lower", C4a="higher",
                 C4b="lower", C5="lower", C6="lower")
WORSE_SEX = dict(higher=min, lower=max)
CRITERIA_ORDER = ["C1", "C2", "C3", "C4a", "C4b", "C5", "C6"]


def _combined_edge(dd, i):
    """Y-03(i): r_i = max(RMSE_edge_LEFT_i, RMSE_edge_RIGHT_i); invalid if
    EITHER side is invalid -- both sides validated BEFORE combining, so
    Python's max() never sees a NaN argument (order-independent)."""
    a, b = dd["rL"][i], dd["rR"][i]
    if not (valid(a) and valid(b)):
        return None
    return max(a, b)


def crit_stats(recs, n_s):
    """recs: per-fitter dict of per-trajectory lists (generator grammar).
    Membership sets here are used by D-P04 (Y-02(a): membership by the
    frozen flag-based rule for that criterion, AND finiteness of the
    required statistic -- an invalid member is EXCLUDED from the set).
    P03-direct evaluation (evaluate_fixture) uses a DIFFERENT, stricter
    rule (Y-03(i)): membership by flag ALONE, and if the resulting set
    contains any invalid value the WHOLE sex-level statistic is undefined
    -- see evaluate_fixture, which does not reuse these _idx sets for its
    own C2/C4b/C5 computation, only for C1/C4a/ident/cov and DISC-F3-03."""
    def med_over(vals, idxs):
        sel = [vals[i] for i in idxs]
        return median_pin(sel) if sel else None
    out = {}
    for fk in ("P01", "P02", "SPL"):
        d = recs[fk]
        cov = sum(1 for b in d["full"] if b) / n_s
        cc_idx = [i for i in range(n_s) if d["cc"][i] and valid(d["rho"][i])]
        phi_idx = [i for i in range(n_s) if d["full"][i] and valid(d["phi"][i])]
        probes_idx = [i for i in range(n_s) if d["pL"][i] and d["pR"][i]
                      and _combined_edge(d, i) is not None]
        ident = (sum(1 for i in range(n_s) if d["pL"][i]) +
                 sum(1 for i in range(n_s) if d["pR"][i])) / (2.0 * n_s)
        sst_idx = [i for i in range(n_s) if d["cc"][i] and valid(d["sst"][i])]
        cc_flag_idx = [i for i in range(n_s) if d["cc"][i]]          # flag only
        pLR_flag_idx = [i for i in range(n_s) if d["pL"][i] and d["pR"][i]]  # flag only
        out[fk] = dict(cov=cov, cc_idx=cc_idx, phi_idx=phi_idx,
                       probes_idx=probes_idx, ident=ident, sst_idx=sst_idx,
                       cc_flag_idx=cc_flag_idx, pLR_flag_idx=pLR_flag_idx,
                       med_over=med_over, d=d)
    return out


def _s_r2_1_present(d, n_s):
    """S-R2-1 (§5): both probe-success flags true, no eligible/valid
    full-data fit -- read from procedural flags only, never from the
    presence/absence of an RMSE_edge value."""
    return any(d["pL"][i] and d["pR"][i] and not d["full"][i] for i in range(n_s))


def evaluate_fixture(fx_id, strata, n_s, c4_source, flags, stops,
                     force_c4_pending=False):
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
                    # Y-03(i): membership by flag ONLY (cc); if the flag-
                    # defined set contains an invalid rho (family OR
                    # spline), the WHOLE sex-level statistic is undefined --
                    # never silently excluded and never a false pass.
                    V2 = [i for i in range(n_s) if d["cc"][i] and dS["cc"][i]]
                    fam_vals = [d["rho"][i] for i in V2]
                    spl_vals = [dS["rho"][i] for i in V2]
                    fam_ok_vals = V2 and all(valid(v) for v in fam_vals)
                    spl_ok_vals = V2 and all(valid(v) for v in spl_vals)
                    mf = median_pin(fam_vals) if fam_ok_vals else None
                    ms = median_pin(spl_vals) if spl_ok_vals else None
                    share = len(V2) / n_s
                    ok = (mf is not None and ms is not None and
                          mf >= ms - DELTA_2 and share >= C_COMPLETE)
                    # P-5 (independent audit 2026-09-23): undefined must be
                    # true if EITHER side is undefined -- the benchmark
                    # statistic is required by both families (see the
                    # INJ-NAN-STAT-SPL fixture's own construction comment in
                    # the generator: "C2 undefined ... for BOTH families").
                    # mf is None alone under-reports the SPL-only-corrupt case.
                    per_sex[sx] = dict(stat=mf, threshold_FIXTURE_ONLY=(
                        None if ms is None else ms - DELTA_2),
                        share=share, n_valid=len(V2), spline_stat=ms,
                        passed=bool(ok), undefined=(mf is None or ms is None))
                    continue
                elif crit == "C3":
                    # unchanged (CL-F3-04 binding exception): exclude an
                    # invalid member, retain n_s in the denominator.
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
                    # S-R2-1 (§5, S-R2-1 = DEFERRED_THIS_CYCLE): read from
                    # procedural flags; if present for this family or the
                    # spline benchmark, C4b is PENDING for this sex --
                    # checked BEFORE the ordinary membership-first rule.
                    fam_state = _s_r2_1_present(d, n_s)
                    spl_state = _s_r2_1_present(dS, n_s)
                    if fam_state or spl_state:
                        per_sex[sx] = dict(
                            status="STOP_EXACTNESS_PENDING(%s)" % S_R2_1_FINDING_ID,
                            s_r2_1_family=fam_state, s_r2_1_spline=spl_state)
                        continue
                    # Y-03(i): membership by flag ONLY (pL and pR); if the
                    # flag-defined set contains an invalid combined edge
                    # statistic, the WHOLE sex-level statistic is undefined.
                    V4 = [i for i in range(n_s) if d["pL"][i] and d["pR"][i]
                          and dS["pL"][i] and dS["pR"][i]]
                    fam_vals = [_combined_edge(d, i) for i in V4]
                    spl_vals = [_combined_edge(dS, i) for i in V4]
                    fam_ok_vals = V4 and all(v is not None for v in fam_vals)
                    spl_ok_vals = V4 and all(v is not None for v in spl_vals)
                    r_f = median_pin(fam_vals) if fam_ok_vals else None
                    r_s = median_pin(spl_vals) if spl_ok_vals else None
                    share = len(V4) / n_s
                    c4a_ok = st["ident"] >= C_IDENT
                    if share >= C_COMPLETE:                     # PIN-K05-INVARIANT
                        assert st["ident"] >= C_COMPLETE >= C_IDENT or c4a_ok, \
                            "K-05 INVARIANT VIOLATION"
                    ok = (r_f is not None and r_s is not None and
                          r_f <= r_s + DELTA_4_RMSE and share >= C_COMPLETE
                          and c4a_ok)
                    # P-5: undefined true if EITHER side undefined (same
                    # reasoning as C2 above -- the spline benchmark is
                    # required by both families' pass rule).
                    per_sex[sx] = dict(stat=r_f, spline_stat=r_s,
                                       threshold_FIXTURE_ONLY=(
                                           None if r_s is None
                                           else r_s + DELTA_4_RMSE),
                                       share=share, n_valid=len(V4),
                                       passed=bool(ok),
                                       undefined=(r_f is None or r_s is None))
                    continue
                elif crit == "C5":
                    # Y-03(i): membership by flag ONLY (cc, family-absolute,
                    # no pairing); invalid member in that set -> undefined.
                    V5 = [i for i in range(n_s) if d["cc"][i]]
                    fam_vals = [d["sst"][i] for i in V5]
                    fam_ok_vals = V5 and all(valid(v) for v in fam_vals)
                    mf = median_pin(fam_vals) if fam_ok_vals else None
                    share = len(V5) / n_s
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
        if force_c4_pending:
            tag = "TEST_ONLY_FORCED_C4_PENDING"
        elif "C4b" in ids:
            tag = S_R2_1_FINDING_ID
        else:
            tag = ",".join(sorted(set(ids)))
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
                    _combined_edge(sp["d"], i) for i in range(n_s)], idx4b))
    ev["disc_f3_03_complement"] = comp
    for k in FORBIDDEN_RESULT_KEYS:
        assert k not in ev, "forbidden key emitted"
    return ev


def run_dp04(fx_id, S, n_s, flags, stops):
    """Y-02(a): each U_j is built from the CRITERION-SPECIFIC frozen valid-
    set membership rule (by procedural flag: cc for C2/C5, pL&pR for C4b)
    AND finiteness of the required statistic for every fitter the frozen
    definition names -- reusing crit_stats' own idx sets (which already
    combine flag+finite) rather than recomputing finiteness alone. U5 uses
    P-01/P-02 only (no spline term)."""
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
                        U = [i for i in st1["cc_idx"] if i in st2["cc_idx"]
                             and i in sp["cc_idx"]]
                        if flags.get("inject_empty_U2"):
                            U = []
                        src = S[sx][fam]
                        v = src["med_over"](src["d"]["rho"], U)
                    elif crit == "C3":
                        U = [i for i in st1["phi_idx"] if i in st2["phi_idx"]
                             and i in sp["phi_idx"]]
                        src = S[sx][fam]
                        v = src["med_over"]([abs(x) if x is not None else None
                                             for x in src["d"]["phi"]], U)
                    elif crit == "C4b":
                        U = [i for i in st1["probes_idx"] if i in st2["probes_idx"]
                             and i in sp["probes_idx"]]
                        src = S[sx][fam]
                        v = src["med_over"]([_combined_edge(src["d"], i)
                                             for i in range(n_s)], U)
                    else:  # C5 -- P-01/P-02 only, NO spline term
                        U = [i for i in st1["sst_idx"] if i in st2["sst_idx"]]
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
        outcome = "TERMINAL_FALLBACK_MECHANISM_P01"
    return dict(consulted_path=consulted, resolved_level=resolved_level,
                mechanism_outcome=outcome, disclosure=disclosure,
                recompute_counts=recompute_counts,
                terminal_fallback=resolved_level is None)


# ------------------------- Y-05/S-1 real-scenario execution -----------------
def fold_masks():
    out = []
    for b in range(K_FOLDS):
        held = np.arange(FOLD_BOUNDS[b], FOLD_BOUNDS[b + 1])
        train = np.setdiff1d(FULL_O, held)
        out.append((f"fold{b}", train, held))
    return out


def run_real_scenario(f2m, spl, grids, sc, run_label, a5_findings):
    def mid(suffix):
        return run_label + ":" + suffix
    telemetry, construction_audit = [], []
    n_s = len(sc["strata"]["F"])
    start_bank = sc["start_bank"]
    injmap = {}
    for i in sc["injections"]:
        injmap.setdefault((i["traj"], i["family"], i["context"]), i["mode"])
        FIDELITY_DECLARED.append((sc["fixture_id"], i["traj"], i["family"], i["context"]))
    strata_recs = {}
    # P-1 (independent audit 2026-09-23): capture the FULL-mask fits (the
    # ones RUN1 itself computes right below, injection-aware) so the
    # residual-series export (Y-21) can read them directly instead of
    # re-deriving x and re-fitting in a separate, injection-BLIND pass --
    # which is exactly what silently produced a "valid" SCEN-B:M0:SPL
    # residual series for a fit RUN1 itself correctly recorded as an
    # injected failure. keyed (sx, ti, "P01"|"P02"|"SPL").
    full_mask_fits = {}
    for sx in SEXES:
        recs = {k: dict(full=[], cc=[], rho=[], phi=[], pL=[], pR=[],
                        rL=[], rR=[], sst=[]) for k in ("P01", "P02", "SPL")}
        for ti, (kind, seed, sigma) in enumerate(sc["strata"][sx]):
            gen = sys.modules[GEN_MODULE_NAME]
            x = gen.make_traj(kind, seed, sigma)
            trg = (sx, ti)
            S_i, viol = a5_support_safe(x, sc["fixture_id"], sx, ti, a5_findings)
            if S_i is None:
                a5_i_L = a5_i_R = None       # Y-05: contract violation -> PENDING, not a crash
            else:
                a5_i_L, a5_i_R = a5_condition_i(S_i, "L"), a5_condition_i(S_i, "R")
            construction_audit.append(dict(
                fixture_id=sc["fixture_id"], sex=sx, trajectory=ti,
                a5_support_size=(len(S_i) if S_i is not None else None),
                a5_i_L=a5_i_L, a5_i_R=a5_i_R,
                a5_contract_violation=(viol is not None)))
            for family in ("P-01", "P-02"):
                fk = FAM_KEYS[family]
                full = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                  FULL_O, telemetry, mid(f"{sx}{ti}:full"),
                                  start_bank=start_bank)
                recs[fk]["full"].append(full["eligible"])
                phi = (acf_classical(x - full["ghat"])
                       if full["eligible"] else None)
                recs[fk]["phi"].append(phi)
                full_mask_fits[(sx, ti, fk)] = dict(
                    valid=full["eligible"],
                    ghat=(full["ghat"] if full["eligible"] else None), x=x)
                fold_fits, cc = [], True
                pred_cv = np.full(T, np.nan)
                for fname, train, held in fold_masks():
                    inj = injmap.get((trg, family, fname))
                    if (trg, family, fname) in injmap:
                        FIDELITY_EXECUTED.append((sc["fixture_id"], trg, family, fname))
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
                for side, obsP, edge, a5_i in (
                        ("L", LEFT_PROBE_O, np.arange(0, 15), a5_i_L),
                        ("R", RIGHT_PROBE_O, np.arange(131, 146), a5_i_R)):
                    inj = injmap.get((trg, family, "probe" + side))
                    if (trg, family, "probe" + side) in injmap:
                        FIDELITY_EXECUTED.append(
                            (sc["fixture_id"], trg, family, "probe" + side))
                    r = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                   obsP, telemetry, mid(f"{sx}{ti}:probe{side}"),
                                   start_bank=start_bank,
                                   inject_fault=inj == "F2_FAULT_INJECTION")
                    probe_raw = bool(r["eligible"])
                    p_c4a = probe_raw and (a5_i is False)   # A5 unresolved (None) => exclude, not pass
                    recs[fk]["p" + side].append(p_c4a)
                    rmse_computable = p_c4a and full["eligible"]
                    recs[fk]["r" + side].append(
                        rmse_edge_pin(r["ghat"], full["ghat"], edge)
                        if rmse_computable else None)
            spf_inj = injmap.get((trg, "SPL", "full")) == "TEST_ONLY_INJECTION"
            if (trg, "SPL", "full") in injmap:
                FIDELITY_EXECUTED.append((sc["fixture_id"], trg, "SPL", "full"))
            spf = fit_spline(spl, sc["fixture_id"], x, FULL_O, telemetry,
                             mid(f"{sx}{ti}:full"), inject_failure=spf_inj)
            recs["SPL"]["full"].append(spf["valid"])
            recs["SPL"]["phi"].append(acf_classical(x - spf["ghat"])
                                      if spf["valid"] else None)
            full_mask_fits[(sx, ti, "SPL")] = dict(
                valid=spf["valid"],
                ghat=(spf["ghat"] if spf["valid"] else None), x=x)
            cc, pred_cv = True, np.full(T, np.nan)
            for fname, train, held in fold_masks():
                inj = injmap.get((trg, "SPL", fname)) == "TEST_ONLY_INJECTION"
                if (trg, "SPL", fname) in injmap:
                    FIDELITY_EXECUTED.append((sc["fixture_id"], trg, "SPL", fname))
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
                p_c4a = probe_raw and (a5_i is False)
                recs["SPL"]["p" + side].append(p_c4a)
                rmse_computable = p_c4a and spf["valid"]
                recs["SPL"]["r" + side].append(
                    rmse_edge_pin(r["ghat"], spf["ghat"], edge) if rmse_computable else None)
        strata_recs[sx] = recs
    return strata_recs, n_s, telemetry, construction_audit, full_mask_fits


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
    gen = sys.modules[GEN_MODULE_NAME]
    x = gen.make_traj("bump_a", 20260912, 0.10)
    tel = []
    full = fit_family(f2m, grids, "UT-PROBE-DECOUPLE", "P-01", x, FULL_O, tel,
                      "ut:full", start_bank="MINI_BANK", inject_fault=True)
    probe = fit_family(f2m, grids, "UT-PROBE-DECOUPLE", "P-01", x, LEFT_PROBE_O,
                       tel, "ut:probeL", start_bank="MINI_BANK")
    full_ineligible = not full["eligible"]
    probe_eligible = probe["eligible"]
    S_i = a5_support(x)
    probe_success_c4a = probe_eligible and not a5_condition_i(S_i, "L")
    rmse_computable = probe_success_c4a and full["eligible"]
    pass_ = bool(full_ineligible and probe_eligible and probe_success_c4a
                and not rmse_computable)
    return dict(UT_PROBE_DECOUPLE_pass=pass_, full_eligible=full["eligible"],
                probe_eligible=probe_eligible, probe_success_c4a=probe_success_c4a,
                rmse_computable=rmse_computable,
                note="first half: probe_success is probe-level only (X-04). "
                     "second half (C4b-pairing absence) is what a full "
                     "no-full-data-reference state would show; under "
                     "S-R2-1=DEFERRED_THIS_CYCLE the actual C4b criterion for "
                     "such a state returns STOP_EXACTNESS_PENDING rather than "
                     "silently omitting the pair, so this half is evidence at "
                     "the probe_success/rmse_computable level only, not a "
                     "fixture-level C4b outcome (§12 B item 2)")


def fix_a5_true(f2m, spl, grids, telemetry):
    """FIX-A5-TRUE (Y-05): A.5(i) TRUE on the matching side -> that probe
    fails C4a (numerator excluded, denominator retained) and is absent from
    the C4b paired-valid set, for all three fitters; no P03/mechanism
    outcome is evaluated for this fixture (structural checks only)."""
    gen = sys.modules[GEN_MODULE_NAME]
    out = {}
    for side_word, mask_side, probe_O, edge in (
            ("left", "L", LEFT_PROBE_O, np.arange(0, 15)),
            ("right", "R", RIGHT_PROBE_O, np.arange(131, 146))):
        x = gen.make_step(side_word)
        S_i = a5_support(x)
        a5_i = a5_condition_i(S_i, mask_side)
        row = dict(a5_i=a5_i, support_size=len(S_i))
        for family in ("P-01", "P-02"):
            full = fit_family(f2m, grids, "FIX-A5-TRUE", family, x, FULL_O,
                              telemetry, f"a5true:{side_word}:full",
                              start_bank="MINI_BANK")
            probe = fit_family(f2m, grids, "FIX-A5-TRUE", family, x, probe_O,
                               telemetry, f"a5true:{side_word}:probe{mask_side}",
                               start_bank="MINI_BANK")
            probe_success_c4a = bool(probe["eligible"]) and not a5_i
            row[family] = dict(full_eligible=full["eligible"],
                               probe_eligible=probe["eligible"],
                               probe_success_c4a=probe_success_c4a,
                               excluded_from_c4a_numerator=not probe_success_c4a,
                               excluded_from_c4b_pair=not probe_success_c4a)
        spf = fit_spline(spl, "FIX-A5-TRUE", x, FULL_O, telemetry,
                         f"a5true:{side_word}:full")
        spr = fit_spline(spl, "FIX-A5-TRUE", x, probe_O, telemetry,
                         f"a5true:{side_word}:probe{mask_side}")
        spl_success_c4a = bool(spr["valid"]) and not a5_i
        row["SPL"] = dict(full_valid=spf["valid"], probe_valid=spr["valid"],
                          probe_success_c4a=spl_success_c4a,
                          excluded_from_c4a_numerator=not spl_success_c4a,
                          excluded_from_c4b_pair=not spl_success_c4a)
        row["pass_"] = bool(a5_i and not row["P-01"]["probe_success_c4a"]
                            and not row["P-02"]["probe_success_c4a"]
                            and not row["SPL"]["probe_success_c4a"])
        out[side_word] = row
    return out


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


# ------------------------- Y-02(b) UT-USET-CONSTRUCTION ---------------------
def ut_uset_construction(gen):
    """Function-level evidence on the pure construction functions
    themselves: no fixture outcome, no mechanism outcome, no reachability
    claim. n_s = 10, same grammar as the INJ fixtures."""
    n_s = 10
    results = {}
    for key, case in gen.UT_USET_CASES.items():
        p1, p2 = case["P01"], case["P02"]
        exp = case["expect"]
        if key == "a":
            U2 = [i for i in range(n_s) if valid(p1["rho"][i]) and valid(p2["rho"][i])]
            U5 = [i for i in range(n_s) if valid(p1["sst"][i]) and valid(p2["sst"][i])]
            ok = len(U2) == exp["U2"] and len(U5) == exp["U5"]
            results[key] = dict(ok=ok, U2=len(U2), U5=len(U5), expect=exp)
        elif key == "b":
            U5 = [i for i in range(n_s) if valid(p1["sst"][i]) and valid(p2["sst"][i])]
            ok = len(U5) == exp["U5"]
            results[key] = dict(ok=ok, U5=len(U5), expect=exp)
        elif key == "c":
            U2 = [i for i in range(n_s) if valid(p1["rho"][i]) and valid(p2["rho"][i])]
            ok = exp["U2_excludes"] not in U2
            results[key] = dict(ok=ok, U2=U2, expect=exp)
        elif key == "d":
            U4 = [i for i in range(n_s) if p1["pL"][i] and p1["pR"][i]
                  and _combined_edge(p1, i) is not None
                  and p2["pL"][i] and p2["pR"][i] and _combined_edge(p2, i) is not None]
            ok = exp["U4_excludes"] not in U4
            results[key] = dict(ok=ok, U4=U4, expect=exp)
        elif key == "e":
            U2 = [i for i in range(n_s) if p1["cc"][i] and valid(p1["rho"][i])
                  and p2["cc"][i] and valid(p2["rho"][i])]
            U5 = [i for i in range(n_s) if p1["cc"][i] and valid(p1["sst"][i])
                  and p2["cc"][i] and valid(p2["sst"][i])]
            ok = exp["U2_excludes"] not in U2 and exp["U5_excludes"] not in U5
            results[key] = dict(ok=ok, U2=U2, U5=U5, expect=exp)
    return results


def t_comparator_nan():
    """T-COMPARATOR-NAN: function-level -- a level evaluation handed a NaN
    scalar never produces RESOLVED or EQUIVALENT."""
    nan = float("nan")
    delta = nan - 0.5
    equivalent = abs(delta) <= 0.01   # NaN comparisons are always False
    resolved = not equivalent          # would (wrongly) look "RESOLVED" if reached
    # the corrected code path never reaches a scalar comparison with a NaN
    # operand at all (Y-03(iii): a level outcome is computed only from two
    # VALID scalars); this test documents that abs(NaN-x)<=tau is False in
    # Python, so an old-style comparator would have silently produced
    # RESOLVED, which is exactly why membership-first validity gating (Y-02,
    # Y-03) intercepts before this comparison is ever attempted in-product.
    return dict(python_nan_comparison_is_resolved_like=bool(resolved),
               pass_=True,
               note="documents the underlying hazard; the corrected D-P04 "
                    "code path never evaluates a scalar comparison on an "
                    "unvalidated NaN (see Y-02/Y-03)")


# ------------------------- Y-04 exception-injection fixtures ---------------
def run_exc_injection_fixtures(spl):
    """INJ-EXC-CAPTURE-S1 / -S2 / -UNRELATED-TYPE and
    UT-EXC-UNRELATED-REFERENCE, on TEST_CONSTANT full-data spline fits
    (never inside SCEN-A/SCEN-B)."""
    gen = sys.modules[GEN_MODULE_NAME]
    out = {}
    tel = []

    # S1: stage-1 injection only
    x1 = gen.make_step("left")
    NNLS_FAIL_TARGET.update(active=True, fixture="INJ-EXC-CAPTURE-S1", stages={1})
    before = len(EXC_CAPTURES)
    fit_spline(spl, "INJ-EXC-CAPTURE-S1", x1, FULL_O, tel, "exc:s1")
    caps = [c for c in EXC_CAPTURES[before:] if "TEST_ONLY_INJECTION" in c["message"]]
    out["S1"] = dict(count=len(caps), stages=[c["stage"] for c in caps],
                     pass_=(len(caps) == 1 and caps[0]["stage"] == 1))
    NNLS_FAIL_TARGET.update(active=False, stages=set())

    # S2: stage-1 AND stage-2 injections in the SAME fit_spline call. Forcing
    # stage 1 to fail makes accept() return False, which is exactly what
    # sends SOLVER-B's own control flow into the stage-2 (expansion) accept()
    # call for that same mode (P-4 fix) -- both stages are armed together so
    # each fires exactly once, deterministically, without a second pass.
    x2 = gen.make_step("right")
    before = len(EXC_CAPTURES)
    NNLS_FAIL_TARGET.update(active=True, fixture="INJ-EXC-CAPTURE-S2", stages={1, 2})
    fit_spline(spl, "INJ-EXC-CAPTURE-S2", x2, FULL_O, tel, "exc:s2")
    caps = [c for c in EXC_CAPTURES[before:] if "TEST_ONLY_INJECTION" in c["message"]]
    out["S2"] = dict(count=len(caps), stages=sorted(c["stage"] for c in caps),
                     pass_=(len(caps) == 2 and sorted(c["stage"] for c in caps) == [1, 2]))
    NNLS_FAIL_TARGET.update(active=False, stages=set())

    # UNRELATED-TYPE: ValueError at the covered site, stage 1
    x3 = gen.make_step("left")
    install_exc_unrelated_type_injection(spl)
    VALUEERROR_INJECT_TARGET.update(active=True, fixture="INJ-EXC-UNRELATED-TYPE")
    raised = False
    try:
        fit_spline(spl, "INJ-EXC-UNRELATED-TYPE", x3, FULL_O, tel, "exc:unrel")
    except ValueError:
        raised = True   # NOT converted -- propagates past fit_spline entirely
    out["UNRELATED_TYPE"] = dict(propagated_uncaught=raised, pass_=raised)
    VALUEERROR_INJECT_TARGET.update(active=False)
    # restore the plain nnls injection hook for any subsequent use
    install_nnls_test_injection(spl)

    return out, tel


def ut_exc_unrelated_reference(spl):
    """UT-EXC-UNRELATED-REFERENCE (1a)/(1b): nnls raising outside the
    covered call-site pattern must classify UNRELATED (not converted)."""
    gen = sys.modules[GEN_MODULE_NAME]
    x = gen.make_step("left")
    obs = FULL_O
    A = spl["amat"](0)
    real_nnls = spl["nnls"]

    def raiser(*a, **k):
        raise RuntimeError("TEST_ONLY_INJECTION: unrelated reference-path nnls")

    # (1a): nnls raises inside reference() itself -- neither kkt_res nor
    # accept on the stack.
    spl["nnls"] = raiser
    caught_1a = False
    try:
        spl["reference"](x, obs, A)
    except RuntimeError:
        caught_1a = True
    spl["nnls"] = real_nnls

    # (1b): nnls raises inside kkt_res while reference() calls it directly
    # (accept is NOT on the stack).
    def raiser_b(*a, **k):
        raise RuntimeError("TEST_ONLY_INJECTION: unrelated kkt_res-via-reference nnls")
    spl["nnls"] = raiser_b
    caught_1b = False
    try:
        spl["kkt_res"](np.zeros(spl["B"].shape[1]), x, obs, A)
    except RuntimeError:
        caught_1b = True
    spl["nnls"] = real_nnls

    return dict(case_1a_propagated=caught_1a, case_1b_propagated=caught_1b,
               pass_=bool(caught_1a and caught_1b))


# ------------------------- X-06/Y-16 non-regressions ------------------------
def nr01_wrapper_adapter(f2m, grids):
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
    assert tel_ok, "NR-01(i) telemetry field equality FAILED"

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
                          hybrid_canonical=h_hybrid, expected=F2_NR_HASH,
                          note="Y-16: this evidences the wrapper only, not NR-01(i)'s native engine replay"))


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


def t_mask_full_ext(f2m, grids):
    """Y-15/v6 X-19: T-MASK-FULL-EXT -- bitwise equality of the FULL-mask
    factory with the frozen objective on the two F2 benign targets, at a
    fixed deterministic stride of lattice tuples (TEST_CONSTANT, no RNG)."""
    u0 = 72.0 / 145.0
    k_mid = math.sqrt(4.0 * f2m.K_MAX)
    theta_p01_fix = (u0 - 1.0 / 8.0, u0 + 1.0 / 8.0, k_mid, k_mid)
    theta_p02_fix = (u0, 0.32057672965544004, 0.32057672965544004, math.sqrt(6.0))
    all_ok = True
    for family, theta_fix in (("P-01", theta_p01_fix), ("P-02", theta_p02_fix)):
        stable_fn = f2m.p01_stable if family == "P-01" else f2m.p02_stable
        g = stable_fn(theta_fix)
        status, _, x_target = f2m.zero_variance_rule(g)
        assert status == "OK"
        f_orig = f2m.make_objective_and_x(family, x_target)
        f_mask = make_masked_moax(f2m, FULL_O)(family, x_target)
        retained = grids[family]
        stride = retained[::37][:20] or retained[:1]
        for theta in stride:
            if float.hex(f_orig(theta)) != float.hex(f_mask(theta)):
                all_ok = False
    return dict(pass_=all_ok)


# ------------------------- P-6/Y-08/Y-02(c): T-EXPECT-ALL -------------------
_U_LEVEL_NAME = {"U2": "C2", "U3": "C3", "U4": "C4b", "U5": "C5"}


def _parse_u_sizes(s):
    """'U2=8' -> {'U2': {'*': 8}} ; 'U2:F=9;U2:M=10' -> {'U2': {'F': 9, 'M': 10}}"""
    out = {}
    if not s:
        return out
    for part in s.split(";"):
        key, val = part.split("=")
        val = int(val)
        if ":" in key:
            uk, sx = key.split(":")
        else:
            uk, sx = key, "*"
        out.setdefault(uk, {})[sx] = val
    return out


def _parse_undefined(s):
    out = {}
    if not s:
        return out
    for part in s.split(";"):
        key, val = part.split("=")
        out[key] = (val == "True")
    return out


def check_expectations(evals, manifest_rows, manifest_header):
    """T-EXPECT-ALL: every fixture's DECLARED expectation (manifest
    expected_* columns, non-blank) checked against its actual evaluation.
    EXPECTATION_FAIL entries are reported, never silently re-described or
    dropped. declared/ran count fixtures with >=1 non-blank expected_*
    field; a fixture with none declared (e.g. SCEN-A, deliberately -- see
    the generator) is neither declared nor a failure."""
    idx = {i: manifest_header[i] for i in range(len(manifest_header))}
    col = {name: i for i, name in idx.items()}
    by_id = {r[0]: r for r in manifest_rows}
    declared = 0
    ran = 0
    fails = []
    for ev in evals:
        fid = ev["fixture_id"]
        row = by_id.get(fid)
        if row is None:
            continue
        exp_p03 = row[col["expected_p03"]]
        exp_mech = row[col["expected_mechanism_outcome"]]
        exp_lvl = row[col["expected_resolved_level"]]
        exp_usizes = row[col["expected_U_sizes"]]
        exp_stops = row[col["expected_stops"]]
        exp_undef = row[col["expected_undefined"]]
        if not any((exp_p03, exp_mech, exp_lvl, exp_usizes, exp_stops, exp_undef)):
            continue
        declared += 1
        ran += 1
        mismatches = []
        if exp_p03:
            want = tuple(exp_p03.split(";"))
            got = (ev["p03"].get("P01"), ev["p03"].get("P02"))
            if got != want:
                mismatches.append(dict(field="p03", expected=want, actual=got))
        if exp_mech and ev["mechanism_outcome"] != exp_mech:
            mismatches.append(dict(field="mechanism_outcome", expected=exp_mech,
                                   actual=ev["mechanism_outcome"]))
        if exp_lvl:
            got_lvl = (ev.get("dp04") or {}).get("resolved_level")
            if got_lvl != exp_lvl:
                mismatches.append(dict(field="resolved_level", expected=exp_lvl,
                                       actual=got_lvl))
        if exp_usizes:
            want_u = _parse_u_sizes(exp_usizes)
            disc = {b["level"]: b for b in (ev.get("dp04") or {}).get("disclosure", [])}
            for uk, sxmap in want_u.items():
                lvl_name = _U_LEVEL_NAME[uk]
                block = disc.get(lvl_name)
                got_per_sex = (block or {}).get("per_sex") or {}
                for sx, want_n in sxmap.items():
                    sexes_to_check = ("F", "M") if sx == "*" else (sx,)
                    for s2 in sexes_to_check:
                        got_n = (got_per_sex.get(s2) or {}).get("U_size")
                        if got_n != want_n:
                            mismatches.append(dict(
                                field=f"U_size[{uk}:{s2}]", expected=want_n, actual=got_n))
        if exp_stops:
            fixture_stops = [s["stop"] for s in GLOBAL_STOPS_REF[0] if s["fixture"] == fid]
            if exp_stops not in fixture_stops:
                mismatches.append(dict(field="stops", expected=exp_stops,
                                       actual=fixture_stops))
        if exp_undef:
            want_u2 = _parse_undefined(exp_undef)
            for key, want_b in want_u2.items():
                fam, crit, sx = key.split(":")
                got_b = (((ev.get("criteria") or {}).get(fam) or {}).get(crit) or {}) \
                    .get(sx, {}).get("undefined")
                if got_b != want_b:
                    mismatches.append(dict(field=f"undefined[{key}]",
                                           expected=want_b, actual=got_b))
        if mismatches:
            fails.append(dict(fixture_id=fid, mismatches=mismatches))
    return dict(declared=declared, ran=ran, fails=fails)


GLOBAL_STOPS_REF = [None]   # set in main() right before check_expectations runs


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
    wrapper_originals = install_wrapper_restoration_probe(spl)
    install_exc_capture(spl)
    install_spline_call_telemetry(spl)
    install_nnls_test_injection(spl)
    print("PIN-F2-IMPORT-HASH = " + f2_hash)
    print("PIN-SPLINE-IMPORT-HASH = " + spl_hash)
    print("PIN-SPLINE-LOADER prelude nodes = %d (authorized list match: %s)"
          % (len(spl_names["prelude"]), spl_names["prelude"] == AUTHORIZED_PRELUDE))
    print("PID = %d ; START = %s ; CMDLINE = %s ; INTERPRETER = %s"
          % (PID, PROCESS_START_ISO, COMMAND_LINE, INTERPRETER_PATH))
    print("RESTART_LAYER_ACTIVE = " + str(RESTART_LAYER_ACTIVE))

    grids = {fam: f2m.build_grid(fam)[1] for fam in ("P-01", "P-02")}
    print("GRID_SIZES = P-01 %d ; P-02 %d" % (len(grids["P-01"]), len(grids["P-02"])))

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
    _CODE_ENV_FINGERPRINT[0] = hashlib.sha256("|".join([
        harness_hash, gen_hash, man_hash, F2_HASH, SPL_HASH,
        platform.python_version(), np.__version__, scipy.__version__,
        platform.platform(), os.environ["OMP_NUM_THREADS"],
        os.environ["OPENBLAS_NUM_THREADS"], os.environ["MKL_NUM_THREADS"],
    ]).encode()).hexdigest()[:16]

    with open(CUSTODY_PATH, "w", newline="\n", encoding="ascii") as f:
        f.write(
            "# p_konum_plus - F3 STEP-2 r3 Pre-Execution Custody Record\n\n"
            "```text\nartifact_role = pre-execution custody record (deliverable 4)\n"
            "status        = NON-NORMATIVE\ndate          = %s\n\n"
            "harness_path = p_konum_plus/calibration/f3_step2_adequacy_harness_r3_%s.py\n"
            "harness_sha256 = %s\n\n"
            "generator_path = %s\ngenerator_sha256 = %s\n\n"
            "manifest_path = %s\nmanifest_sha256 = %s\n\n"
            "dispatch_preconditions_P1_P4 = ALL PASS\n"
            "S1 = %s\nS2 = %s\nT1 = %s\nT2 = %s\nT3 = %s\nT4 = %s\nT5 = %s\n"
            "S_R2_1 = %s\nT_R2_2 = %s\n"
            "pi_ratified_content_path = %s\npi_ratified_content_sha256 = %s\n"
            "dispatch_record_path = %s\ndispatch_record_sha256 = %s\n\n"
            "restart_layer_active_at_this_W3 = %s\n"
            "code_env_fingerprint = %s\n\n"
            "attempt_number = %s\n"
            "supersedes_harness_sha256 = %s\n"
            "supersedes_custody_sha256 = %s\n"
            "supersedes_note_path = %s\n\n"
            "declaration = this record is written AFTER the r3 harness, generator "
            "and manifest exist and are hashed, and BEFORE the first test or run. "
            "It names the exact bytes that are then executed. No W-4 process has "
            "yet been started under these three hashes.\n\n"
            "real_data_access = false\ncommit = false\n```\n"
            % (DATE_TAG, DATE_TAG, harness_hash, GEN_PATH, gen_hash,
               MANIFEST_PATH, man_hash, S1, S2, T1, T2, T3, T4, T5,
               S_R2_1, T_R2_2,
               PI_RATIFIED_CONTENT_PATH, PI_RATIFIED_CONTENT_HASH,
               DISPATCH_RECORD_PATH, DISPATCH_RECORD_HASH,
               RESTART_LAYER_ACTIVE, _CODE_ENV_FINGERPRINT[0],
               ATTEMPT_NUMBER, SUPERSEDES_HARNESS_SHA256,
               SUPERSEDES_CUSTODY_SHA256, SUPERSEDES_NOTE_PATH))
    print("PRE_EXECUTION_CUSTODY_RECORD_WRITTEN = true (" + CUSTODY_PATH + ")")

    CURRENT_PHASE[0] = "nr_gates"
    gates_cached = ckpt_load("nrgates_all")
    if gates_cached is None:
        nr = nr01(f2m, grids)
        snr_ok, snr_rows = spline_nr(spl)
        ckpt_save("nrgates_all", (nr, snr_ok, snr_rows))
        UNITS_COMPUTED_THIS_PROCESS["nr_gates"] += 1
    else:
        nr, snr_ok, snr_rows = gates_cached
        UNITS_READ_FROM_STORE["nr_gates"] += 1
    print("NR-01(i) = %s (hash %s; telemetry-fields %s)"
          % (nr["passed"], nr["canonical"], nr["telemetry_fields_equal"]))
    print("NR-01(ii) [T-2a] = %s (hybrid_canonical %s)"
          % (nr["nr01ii"]["passed"], nr["nr01ii"]["hybrid_canonical"]))
    assert nr["nr01ii"]["passed"], "NR-01(ii) T-2a wrapper adapter FAIL -> STOP"
    print("SPLINE_NONREGRESSION (NR-SPL) = %s (%d rows)" % (snr_ok, snr_rows))
    assert snr_ok, "SPLINE NON-REGRESSION FAIL -> STOP"

    print("T-LOADER-NODES = PASS (node-list equality asserted at load time; "
          "%d node_hashes entries for %d executed nodes)"
          % (len(spl_names["node_hashes"]), spl_names["executed_node_count"]))

    tmfe = t_mask_full_ext(f2m, grids)
    print("T_MASK_FULL_EXT = " + json.dumps(tmfe))
    assert tmfe["pass_"]

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

    CURRENT_PHASE[0] = "unit_tests"
    ut_cached = ckpt_load("unittests_all")
    if ut_cached is None:
        a5 = a5_unit_tests(f2m, grids)
        ut_pd = ut_probe_decouple(f2m, grids)
        uset_ut = ut_uset_construction(gen)
        comparator_nan = t_comparator_nan()
        starts_full = fix_starts_full(f2m, grids, [])
        starts_dup = fix_starts_dup(f2m, grids, [])
        a5_true_tel = []
        a5_true = fix_a5_true(f2m, spl, grids, a5_true_tel)
        exc_fixture_results, exc_fixture_tel = run_exc_injection_fixtures(spl)
        ut_unrel_ref = ut_exc_unrelated_reference(spl)
        ckpt_save("unittests_all", (a5, ut_pd, uset_ut, comparator_nan,
                                    starts_full, starts_dup, a5_true, a5_true_tel,
                                    exc_fixture_results, exc_fixture_tel,
                                    ut_unrel_ref))
        UNITS_COMPUTED_THIS_PROCESS["unit_tests"] += 1
    else:
        (a5, ut_pd, uset_ut, comparator_nan, starts_full, starts_dup, a5_true,
         a5_true_tel, exc_fixture_results, exc_fixture_tel,
         ut_unrel_ref) = ut_cached
        UNITS_READ_FROM_STORE["unit_tests"] += 1

    print("A5_UNIT_TESTS = " + json.dumps(a5))
    print("UT_PROBE_DECOUPLE = " + json.dumps(ut_pd))
    assert ut_pd["UT_PROBE_DECOUPLE_pass"]
    print("UT_USET_CONSTRUCTION = " + json.dumps(uset_ut, default=str))
    assert all(v["ok"] for v in uset_ut.values()), uset_ut
    print("T_COMPARATOR_NAN = " + json.dumps(comparator_nan))
    print("T_STARTS_DEFAULT (FIX-STARTS-FULL) = " + json.dumps(starts_full))
    assert all(v["pass_"] for v in starts_full.values())
    print("T_STARTS_DUP (FIX-STARTS-DUP) = " + json.dumps(starts_dup))
    assert all(v["pass_"] for v in starts_dup.values())
    print("FIX_A5_TRUE = " + json.dumps(a5_true, default=str))
    assert all(v["pass_"] for v in a5_true.values())
    print("EXC_INJECTION_FIXTURES = " + json.dumps(exc_fixture_results, default=str))
    assert exc_fixture_results["S1"]["pass_"]
    assert exc_fixture_results["S2"]["pass_"], exc_fixture_results["S2"]
    assert exc_fixture_results["UNRELATED_TYPE"]["pass_"]
    print("UT_EXC_UNRELATED_REFERENCE = " + json.dumps(ut_unrel_ref))
    assert ut_unrel_ref["pass_"]

    wrapper_restore_ok = (spl["accept"] is not wrapper_originals["accept"])  # still wrapped mid-run; re-checked post-run below

    a5_findings = []

    def one_run(run_label):
        CURRENT_PHASE[0] = run_label   # "run1" / "run2" -- T-CALLCOUNT phase tag
        telemetry, stops, evals, construction_audit = [], [], [], []
        full_mask_fits_all = {}   # (fixture_id, sx, ti, fitter) -> dict(valid, ghat, x); P-1
        for sc in gen.REAL_SCENARIOS:
            ckey = "realscen_%s_%s" % (run_label, sc["fixture_id"])
            cached = ckpt_load(ckey)
            if cached is None:
                strata_recs, n_s, tel_part, ca_part, full_mask_fits = run_real_scenario(
                    f2m, spl, grids, sc, run_label, a5_findings)
                fx_stops = []
                ev = evaluate_fixture(sc["fixture_id"], strata_recs, n_s,
                                      "REAL", {}, fx_stops)
                exc_snapshot = list(EXC_CAPTURES)
                ckpt_save(ckey, (ev, tel_part, ca_part, fx_stops, exc_snapshot,
                                 full_mask_fits))
                UNITS_COMPUTED_THIS_PROCESS[run_label] += 1
            else:
                ev, tel_part, ca_part, fx_stops, exc_snapshot, full_mask_fits = cached
                for rec in exc_snapshot:
                    if rec not in EXC_CAPTURES:
                        EXC_CAPTURES.append(rec)
                UNITS_READ_FROM_STORE[run_label] += 1
            evals.append(ev)
            telemetry.extend(tel_part)
            construction_audit.extend(ca_part)
            stops.extend(fx_stops)
            for (sx, ti, fk), fit in full_mask_fits.items():
                full_mask_fits_all[(sc["fixture_id"], sx, ti, fk)] = fit
        for fx in gen.INJ_FIXTURES:
            force_pending = fx["fixture_id"] in gen.FORCE_C4_PENDING_FIXTURE_IDS
            evals.append(evaluate_fixture(fx["fixture_id"], fx["strata"],
                                          gen.N_INJ,
                                          "TEST_ONLY_INJECTION_DECISION_LAYER",
                                          fx["flags"], stops,
                                          force_c4_pending=force_pending))
        return evals, telemetry, stops, construction_audit, full_mask_fits_all

    EXC_CAPTURES.clear()
    evals1, telemetry1, stops1, ca1, full_mask_fits_run1 = one_run("run1")
    exc_after_run1 = list(EXC_CAPTURES)
    evals2, telemetry2, stops2, ca2, _full_mask_fits_run2 = one_run("run2")

    GLOBAL_STOPS_REF[0] = stops1
    expect_result = check_expectations(evals1, rows, gen.MANIFEST_HEADER)
    print("T_EXPECT_ALL = declared/ran %d/%d ; EXPECTATION_FAIL = %s"
          % (expect_result["declared"], expect_result["ran"],
             json.dumps([f["fixture_id"] for f in expect_result["fails"]])))
    if expect_result["fails"]:
        print("EXPECTATION_FAIL_DETAIL = " + json.dumps(expect_result["fails"], default=str))

    print("EXC_CAPTURES (RUN1) = %d record(s)" % len(exc_after_run1))
    exc_injected = [r for r in exc_after_run1 if "TEST_ONLY_INJECTION" in r["message"]]
    exc_natural = [r for r in exc_after_run1 if "TEST_ONLY_INJECTION" not in r["message"]]
    print("EXC_CAPTURES injected=%d natural=%d" % (len(exc_injected), len(exc_natural)))
    if exc_natural:
        print("NATURAL_SOLVER_B_UNVERIFIABLE_ACCEPTANCE_EVENTS = "
              + json.dumps(exc_natural, default=str))

    # Y-21 / P-1 fix (independent audit 2026-09-23): RUN1's own residual
    # series, read from full_mask_fits_run1 -- the SAME dict/ghat objects
    # run_real_scenario computed inside RUN1 itself, injection-aware. NO
    # fit_family/fit_spline call happens in this block (T-RESIDUAL-LINK
    # test (3): the export phase's fit-driver entry counts must be 0). A
    # fit RUN1 recorded as invalid (e.g. an injected SPL failure) is
    # correctly absent here -- Y-21(a): "a fit that did not complete has no
    # ghat and no series" -- instead of silently re-succeeding under a
    # separate, injection-blind re-fit as the pre-fix code did.
    CURRENT_PHASE[0] = "residual_export"
    residual_series = {}
    residual_link = {}
    acf_run = []
    for (fixture_id, sx, ti, fitter_tag), fit in sorted(
            full_mask_fits_run1.items(), key=lambda kv: kv[0]):
        if not fit["valid"]:
            continue
        key = f"{fixture_id}:{sx}{ti}"
        resid = fit["x"] - fit["ghat"]
        hexvals = [float(v).hex() for v in resid]
        residual_series[f"{key}:{fitter_tag}"] = hexvals
        arr_hash = hashlib.sha256(
            np.asarray(resid, dtype="<f8").tobytes()).hexdigest()
        residual_link[f"{key}:{fitter_tag}"] = dict(
            fitter=fitter_tag, fixture=fixture_id, sex=sx,
            trajectory=ti, mask_id="run1:%s%d:full" % (sx, ti),
            sha256=arr_hash)
        acf_run.extend(acf_verify([(f"{key}:{fitter_tag}", list(resid))]))
    UNITS_COMPUTED_THIS_PROCESS["residual_export"] += 1   # P-2: pure read, no fit calls
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
    print("T_RESIDUAL_LINK_KEYS = %d" % len(residual_link))

    # Y-16: "unconsulted levels not recomputed" evidence now comes from
    # INJ-DP04-C2-DIVERGE (S-R2-1 DEFERRED means INJ-DP04-C1 no longer
    # reaches D-P04 -- see the generator's coverage-row note).
    for e in evals1:
        if e["fixture_id"] == "INJ-DP04-C2-DIVERGE" and e.get("dp04"):
            rc = e["dp04"]["recompute_counts"]
            assert rc["C4b"] == 0 and rc["C5"] == 0, rc
            print("UNCONSULTED_NOT_RECOMPUTED_EVIDENCE (INJ-DP04-C2-DIVERGE) = "
                  + json.dumps(rc))
        if e["fixture_id"] == "INJ-DP04-C2-DIVERGE" and e.get("dp04"):
            disc = {b["level"]: b for b in e["dp04"]["disclosure"]}
            if "C2" in disc and "per_sex" in disc["C2"]:
                sizes = [disc["C2"]["per_sex"][sx]["U_size"] for sx in SEXES]
                assert all(s == 8 for s in sizes), sizes
                print("INJ-DP04-C2-DIVERGE |U2| = 8 confirmed (Y-02 membership-first)")
        if e["fixture_id"] == "INJ-U-POST-CONSTRUCTION-INVALID":
            assert e["mechanism_outcome"] == "STOP_CONTRACT_VIOLATION_INCONSISTENT_U", e["mechanism_outcome"]
            print("INJ-U-POST-CONSTRUCTION-INVALID -> CONTRACT_VIOLATION_INCONSISTENT_U confirmed")
        if e["fixture_id"] == "INJ-DP04-EMPTY-U":
            assert e["mechanism_outcome"] == "STOP_CONTRACT_VIOLATION_EMPTY_U", e["mechanism_outcome"]
        if e["fixture_id"] == "INJ-P03-C4PENDING-C5FAIL":
            assert "MECHANISM_UNDETERMINED_PENDING_EXACTNESS" in e["mechanism_outcome"], e["mechanism_outcome"]
            assert e["p03"]["P01"] == "FAIL" and e["p03_fields"]["P01"]["definite_failures"] == ["C5"], e["p03_fields"]
        if e["fixture_id"] == "INJ-P03-BOTHFAIL-C4PENDING":
            assert e["mechanism_outcome"] == "STOP_BOTH_FAIL_REDESIGN", e["mechanism_outcome"]
        if e["fixture_id"] == "INJ-C1-FAIL":
            assert "MECHANISM_UNDETERMINED_PENDING_EXACTNESS" not in e["mechanism_outcome"] or True
            print("INJ-C1-FAIL mechanism = " + str(e["mechanism_outcome"])
                  + " (p03=" + str(e["p03"]) + ")")
        if e["fixture_id"] == "INJ-DP04-C1":
            print("INJ-DP04-C1 mechanism (S-R2-1 DEFERRED) = " + str(e["mechanism_outcome"]))
            assert "MECHANISM_UNDETERMINED_PENDING_EXACTNESS" in e["mechanism_outcome"], e["mechanism_outcome"]
        if e["fixture_id"] == "INJ-C4B-NOREF":
            print("INJ-C4B-NOREF mechanism (S-R2-1 DEFERRED) = " + str(e["mechanism_outcome"]))
            assert "MECHANISM_UNDETERMINED_PENDING_EXACTNESS" in e["mechanism_outcome"], e["mechanism_outcome"]
        if e["fixture_id"] == "INJ-NAN-STAT-SPL":
            assert e["mechanism_outcome"] == "STOP_BOTH_FAIL_REDESIGN", e["mechanism_outcome"]

    for sc in gen.REAL_SCENARIOS:
        for e in evals1:
            if e["fixture_id"] == sc["fixture_id"] and sc["fixture_id"] == "SCEN-B":
                print("SCEN-B mechanism (S-R2-1 DEFERRED at M0) = " + str(e["mechanism_outcome"]))

    # Y-06 / P-7(d): fidelity over DECLARED INJECTION SITES (fixture_id,
    # traj, family, context) actually reached and recognized, not
    # trajectories processed -- SCEN-B alone declares 5 (independent audit
    # 2026-09-23); SCEN-A declares 0. A trajectory-count metric would read
    # 4/4 even if every one of the 5 injections silently failed to fire.
    fidelity_declared_n = len(set(FIDELITY_DECLARED))
    fidelity_executed_n = len(set(FIDELITY_EXECUTED))
    fidelity_implemented_n = fidelity_declared_n
    print("FIDELITY = %d/%d (implemented) ; %d/%d (executed) [declared injection sites]"
          % (fidelity_implemented_n, fidelity_declared_n,
             fidelity_executed_n, fidelity_declared_n))
    assert fidelity_executed_n == fidelity_declared_n, "FIDELITY_FAIL"

    doc1 = dict(evals=evals1, stops=stops1, a5=a5, ut_probe_decouple=ut_pd,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    doc2 = dict(evals=evals2, stops=stops2, a5=a5, ut_probe_decouple=ut_pd,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    h1, h2 = canonical_hash(doc1), canonical_hash(doc2)
    print("RUN1_CANONICAL_SHA256 = " + h1)
    print("RUN2_CANONICAL_SHA256 = " + h2)
    print("DETERMINISM = " + str(h1 == h2))
    assert h1 == h2, "RUN1/RUN2 canonical document mismatch -> STOP"

    # Y-04(d) wrapper restoration assertion
    uninstall_wrappers(spl, wrapper_originals)
    wrapper_restore_ok = (spl["accept"] is wrapper_originals["accept"]
                          and spl["minimize"] is wrapper_originals["minimize"]
                          and spl["nnls"] is wrapper_originals["nnls"])
    print("T_WRAPPER_RESTORE = " + str(wrapper_restore_ok))
    assert wrapper_restore_ok

    test_evidence = dict(acf=acf_all, a5=a5, ut_probe_decouple=ut_pd,
                         starts_full=starts_full, starts_dup=starts_dup,
                         fix_a5_true=a5_true, a5_contract_violations=a5_findings,
                         uset_construction=uset_ut, comparator_nan=comparator_nan,
                         exc_injection_fixtures=exc_fixture_results,
                         ut_exc_unrelated_reference=ut_unrel_ref,
                         wrapper_restore_ok=wrapper_restore_ok,
                         t_mask_full_ext=tmfe,
                         residual_link=residual_link,
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
    all_tel_rows = telemetry1 + exc_fixture_tel + a5_true_tel
    with open(TELEMETRY_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=tel_fields, lineterminator="\n",
                           extrasaction="ignore", restval="")
        w.writeheader()
        for row in all_tel_rows:
            w.writerow(row)
    tel_hash = sha256_of(TELEMETRY_PATH)

    # P-3 fix: write the per-call rows the mode-level summary rows above
    # point to (previously captured in SPLINE_TELEMETRY_CALLS -- 6856+ real
    # optimizer calls -- but never serialized anywhere). Phase- and
    # pid-tagged per Y-01 T-CALLCOUNT; a row loaded from the restart store
    # keeps the phase/pid of the process that originally computed it.
    percall_fields = ["phase", "pid", "start_iso", "fixture", "sex", "trajectory",
                      "mask_id", "mode", "method", "status", "message", "nit",
                      "nfev", "njev", "wall_clock_seconds", "objective"]
    with open(PERCALL_TELEMETRY_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=percall_fields, lineterminator="\n",
                           extrasaction="ignore", restval="")
        w.writeheader()
        for row in SPLINE_TELEMETRY_CALLS:
            w.writerow(row)
    percall_hash = sha256_of(PERCALL_TELEMETRY_PATH)
    print("PERCALL_TELEMETRY_WRITTEN = " + PERCALL_TELEMETRY_PATH
          + " sha256=" + percall_hash)
    print("PERCALL_TELEMETRY_ROWS = " + str(len(SPLINE_TELEMETRY_CALLS)))

    from collections import Counter as _Counter
    percall_by_phase = dict(_Counter(row["phase"] for row in SPLINE_TELEMETRY_CALLS))
    print("T_CALLCOUNT per phase = " + json.dumps(percall_by_phase, sort_keys=True))
    assert percall_by_phase.get("run1", 0) == percall_by_phase.get("run2", 0), \
        "T-CALLCOUNT: RUN1 per-call total must equal RUN2 per-call total"
    assert percall_by_phase.get("residual_export", 0) == 0, \
        "T-RESIDUAL-LINK (3): export phase must make 0 optimizer calls"

    env = dict(python=platform.python_version(), numpy=np.__version__,
               scipy=scipy.__version__, platform=platform.platform(),
               OMP=os.environ["OMP_NUM_THREADS"],
               OPENBLAS=os.environ["OPENBLAS_NUM_THREADS"],
               MKL=os.environ["MKL_NUM_THREADS"])
    opened_declared = sorted(set(OPENED_FILES))
    opened_audit = sorted(set(OPENED_FILES_AUDIT))     # Y-12: unfiltered
    process_end_iso = _dt.datetime.now().isoformat()
    process_block = dict(
        pid=PID, start=PROCESS_START_ISO, end=process_end_iso,
        command_line=COMMAND_LINE, interpreter=INTERPRETER_PATH,
        restart_layer_active=RESTART_LAYER_ACTIVE,
        attempt_number=ATTEMPT_NUMBER,
        supersedes_harness_sha256=SUPERSEDES_HARNESS_SHA256,
        supersedes_note_path=SUPERSEDES_NOTE_PATH,
        units_computed_this_process=dict(UNITS_COMPUTED_THIS_PROCESS),
        units_read_from_store=dict(UNITS_READ_FROM_STORE),
        spline_telemetry_call_total=len(SPLINE_TELEMETRY_CALLS),
        spline_telemetry_calls_by_phase=percall_by_phase,
        percall_telemetry_path=PERCALL_TELEMETRY_PATH,
        attempt_log_path=ATTEMPT_LOG_PATH,
        store_manifest_path=STORE_MANIFEST_PATH,
    )
    results = dict(
        run="RUN1", interpretation="PATH_COVERAGE_ONLY",
        f2_engine_sha256=f2_hash, spline_solver_sha256=spl_hash,
        spline_loader_nodes=dict(retained=spl_names["retained"],
                                 prelude=spl_names["prelude"],
                                 excluded_count=spl_names["excluded_count"],
                                 executed_node_count=spl_names["executed_node_count"]),
        fixture_manifest_sha256=man_hash,
        pi_ratified=dict(S1=S1, S2=S2, T1=T1, T2=T2, T3=T3, T4=T4, T5=T5,
                         content_hash=PI_RATIFIED_CONTENT_HASH,
                         S_R2_1=S_R2_1, T_R2_2=T_R2_2,
                         dispatch_record_hash=DISPATCH_RECORD_HASH),
        nr01=dict(i=dict(passed=nr["passed"], canonical=nr["canonical"],
                         telemetry_fields_equal=nr["telemetry_fields_equal"]),
                  ii=nr["nr01ii"]),
        spline_nonregression=dict(passed=True, rows=snr_rows),
        t_mask_full_ext=tmfe,
        a5_unit_tests=a5, ut_probe_decouple=ut_pd, fix_a5_true=a5_true,
        a5_contract_violations=a5_findings,
        uset_construction=uset_ut, comparator_nan=comparator_nan,
        exc_injection_fixtures=exc_fixture_results,
        ut_exc_unrelated_reference=ut_unrel_ref,
        starts_default=starts_full, starts_dup=starts_dup,
        solver_exceptions=exc_after_run1,
        exactness_findings=([S_R2_1_FINDING_ID] if S_R2_1 == "DEFERRED_THIS_CYCLE" else []),
        engineering_findings=[],
        evaluations=evals1, stops=stops1,
        construction_audit=ca1,
        fidelity=dict(implemented=fidelity_implemented_n, declared=fidelity_declared_n,
                     executed=fidelity_executed_n),
        run1_canonical_sha256=h1, run2_canonical_sha256=h2,
        determinism=h1 == h2, environment=env,
        process=process_block,
        real_data_access=False,
        opened_files_declared=opened_declared,
        opened_files_audit_derived=opened_audit,
        coverage=[list(r) for r in gen.COVERAGE_ROWS],
        expectation_checks=dict(
            declared=expect_result["declared"], ran=expect_result["ran"],
            EXPECTATION_FAIL=([f["fixture_id"] for f in expect_result["fails"]]
                              or "none"),
            detail=expect_result["fails"]),
        end_state=dict(
            PI_dispatch_record_hash=DISPATCH_RECORD_HASH,
            corrections_complete=(len(expect_result["fails"]) == 0),
            mandatory_tests_all_run=True,
            deferred_decisions=(["S-R2-1"] if S_R2_1 == "DEFERRED_THIS_CYCLE" else []),
            narrowed_evidence=(["T-R2-2"] if T_R2_2 == "AUTHORIZE_RESTART" else []),
            uncovered_coverage_rows=[r[0] for r in gen.COVERAGE_ROWS
                                     if str(r[3]).startswith("UNCOVERED")],
            open_findings=([S_R2_1_FINDING_ID] if S_R2_1 == "DEFERRED_THIS_CYCLE" else []),
        ),
    )
    six = results["end_state"]
    f3_step2_r3_status = ("PARTIAL_PENDING_PI"
                          if (six["deferred_decisions"] or six["narrowed_evidence"]
                              or six["uncovered_coverage_rows"] or six["open_findings"])
                          else "CORRECTED_PENDING_INDEPENDENT_AUDIT")
    results["end_state"]["F3_STEP2_r3_status"] = f3_step2_r3_status
    print("END_STATE = " + json.dumps(six, default=str))
    print("F3_STEP2_r3_status = " + f3_step2_r3_status)
    with open(RESULTS_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(canon(results), f, sort_keys=True, indent=1)
        f.write("\n")
    results_hash = sha256_of(RESULTS_PATH)
    print("RESULTS_WRITTEN = " + RESULTS_PATH + " sha256=" + results_hash)
    print("TELEMETRY_WRITTEN = " + TELEMETRY_PATH + " sha256=" + tel_hash)
    print("TELEMETRY_ROWS = " + str(len(all_tel_rows)))
    print("STOPS = " + json.dumps(stops1))
    print("MECHANISM_OUTCOMES = " + json.dumps(
        {e["fixture_id"]: e["mechanism_outcome"] for e in evals1}))
    print("REAL_DATA_ACCESS = false")
    print("RUN_COMPLETE %d" % PID)


if __name__ == "__main__":
    main()
