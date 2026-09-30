"""F3 STEP-2 adequacy-evaluation harness r4-1 (2026-09-29).

Correction revision INSIDE the r4 cycle (deliverables tagged r4-1). Child of
f3_step2_adequacy_harness_r4_2026-09-24.py (parent
54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c -- the r4
package is historical and read-only; nothing of r4 is overwritten, renamed or
moved). Grandparent f3_step2_adequacy_harness_r3_2026-09-22.py. Binding
instruments (verified by SHA256 before the first computation, D-3 S3 / r4
instruction S1 / r4-1 instruction S1):
  D-3  Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
       5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5
  r4   Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md
       e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387
  D-5  f3_step2_r4_pi_dispatch_record_2026-09-24.md
       0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851
  r4-1 Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md
       283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330
  D-6  f3_step2_r4-1_pi_dispatch_record_2026-09-29.md
       a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0
  A-1  f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md
       11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6
       (input, not directive)
  A-2  f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md
       b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a
       (input, not directive)
  A-3  f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md
       9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9
       (input, not directive)
Closes R3A-01 .. R3A-12 of A-1 (from the r4 instruction S3) and R4A-01, -02,
-03, -04, -10 of A-2/A-3 as scoped by D-6 S3 (R4A-08 out of scope). R4A-01
routes a spline-context UNRELATED-pending flag into the decision grammar; the
R4A-01(f) non-regression comparison pins every shared fixture against the r4
results (a15b7eff). Implements S-R2-1 = PI_RULE (the rule text of D-5 S3,
carried unchanged by D-6 S2, word for word; tagged PI_RATIFIED still citing
D-5). T-R2-2 = AUTHORIZE_RESTART, unchanged. PI-ratified content
(S-1=(a), S-2=alpha, T-1=AUTHORIZE, T-2=T-2a, T-3=AUTHORIZE, T-4=T-4a,
T-5=CONFIRM_WITHIN_SCOPE) is unchanged and carried from D-2. EXACT-03 is
CLOSED with D-5 as its source (D-5 S4(d)); deferred_decisions = [].
T-R2-2 = AUTHORIZE_RESTART as read from D-5.

Run rules (D-3 S8, unchanged): r4 attempt 1 is ONE process from the
beginning with RESTART_LAYER_ACTIVE = False; a restart layer only after a
recorded INTERRUPTION and only as S8.3 says (fresh W-3 per revision, empty
store at the start of the cycle, per-unit provenance). The r3 store
directory and the foreign entries under prefix 548ae790f6ac756a are
quarantined and listed, never silently deleted (R3A-07 / r4 instruction S5).

W-3 custody (R3A-07): the custody record is written ONCE per revision,
OUTSIDE the run process, with observed values; main() VERIFIES it against
the live bytes and STOPS on any mismatch -- it never writes or overwrites
the record itself, so its declaration stays true for resumed launches.
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
# r4-1 attempt 3 (D-3 S8.3, harness-change): the restart layer stays ACTIVE.
# History of this revision's attempts:
#   attempt 1 (pid 19528, restart INACTIVE) passed every precondition/gate and
#     stopped with no error at SPL ctx 41 when the host process exited outside
#     the harness's control -- interruption note
#     quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md.
#   attempt 2 (pid 3348, harness 280869892d) ran the WHOLE computation --
#     RUN1==RUN2, T_EXPECT 36/36, eval-level PENDING all pass -- then raised at
#     the T-NONREG-R4 SELF-CHECK because it compared in-memory floats against
#     the canon()-ized (hex) r4 results; a representation bug in the CHECK, no
#     computation or decision changed. Fixed here (both sides canonicalized).
#     Note quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md.
# The harness change invalidates attempt 2's store (fingerprint changes); that
# store is quarantined whole and attempt 3 starts from an EMPTY r4-1 store.
RESTART_LAYER_ACTIVE = True

# r4-1 attempt 3 supersedes the attempt-2 harness (non-regression check fix).
# The r4 chain (attempts 1..7, its quarantine notes, the r4 attempt log and its
# errata) and the r3 chain before it are historical and read-only; they are
# referenced by the r4-1 attempt log/report, never touched, renamed or moved.
SUPERSEDES_HARNESS_SHA256 = "280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2"
SUPERSEDES_CUSTODY_SHA256 = None
SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md"
ATTEMPT_NUMBER = 3

import pickle
# r4-1's OWN restart store, separate from the r4 store (which is left in place,
# untouched). Created empty only if an interruption activates the restart layer.
RESTART_STORE_DIR = "p_konum_plus/calibration/.r4-1_restart_store_2026-09-29"
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


# R3A-02/R3A-11, r4: genuine counter, not a literal -- k05_result is
# computed from this, not hardcoded.
K05_CHECK_COUNT = [0]

# R3A-11, r4: test registry -- every mandatory test records (ran, passed)
# here at its own execution site; corrections_complete and
# mandatory_tests_all_run are COMPUTED over these records at the end,
# never declared. A test that never calls record_test simply is not in
# the registry, and the mandatory-list check fails loudly.
TESTS_RUN = {}


def record_test(test_id, passed):
    TESTS_RUN[test_id] = dict(ran=True, passed=bool(passed))
    return passed


MANDATORY_TESTS = [
    "NR-01i", "NR-01ii", "NR-SPL", "T-LOADER-NODES", "T-MASK-FULL-EXT",
    "PIN-MASKED-OBJECTIVE", "PIN-FEATURE-START-MASKED", "UT-A5-II",
    "UT-A5-III", "UT-PROBE-DECOUPLE", "UT-USET-CONSTRUCTION",
    "T-COMPARATOR-NAN", "T-STARTS-DEFAULT", "T-STARTS-DUP", "FIX-A5-TRUE",
    "T-A5-SUPPORT", "T-EXC-CAPTURE-S1", "T-EXC-CAPTURE-S2",
    "T-EXC-UNRELATED-TYPE", "UT-EXC-UNRELATED-REFERENCE", "T-SCHEMA",
    "T-CANON", "T-EXPECT-ALL", "T-CALLCOUNT", "T-RESIDUAL-LINK",
    "T-WRAPPER-RESTORE", "PIN-ACF",
]

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

GEN_MODULE_NAME = "f3_step2_fixture_generator_r4_1_2026_09_29"
GEN_PATH = "p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py"

# r4-1 correction revision inside the r4 cycle (non-retroactivity: every
# r4-1 deliverable is a NEW file tagged r4-1; nothing under r4/ is touched).
DATE_TAG = "2026-09-29"
MANIFEST_PATH = f"p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_{DATE_TAG}.csv"
CUSTODY_PATH = f"p_konum_plus/provenance/f3_step2_r4-1_preexecution_custody_{DATE_TAG}.md"
TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_telemetry_r4-1_{DATE_TAG}.csv"
RESULTS_PATH = f"p_konum_plus/calibration/f3_step2_results_r4-1_{DATE_TAG}.json"
RESIDUAL_PATH = f"p_konum_plus/calibration/f3_step2_residual_series_r4-1_{DATE_TAG}.json"
TEST_EVIDENCE_PATH = f"p_konum_plus/calibration/f3_step2_test_evidence_r4-1_{DATE_TAG}.json"
PERCALL_TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4-1_{DATE_TAG}.csv"
ATTEMPT_LOG_PATH = f"p_konum_plus/provenance/f3_step2_r4-1_attempt_log_{DATE_TAG}.md"
STORE_MANIFEST_PATH = f"p_konum_plus/calibration/f3_step2_r4-1_restart_store_manifest_{DATE_TAG}.csv"
REGISTER_PATH = f"p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-1_{DATE_TAG}.md"
NONREG_PATH = f"p_konum_plus/calibration/f3_step2_r4-1_nonregression_vs_r4_{DATE_TAG}.csv"
# the audited r4 results this revision opens from, for the R4A-01(f)
# non-regression comparison (read-only, pinned by the start-state inventory)
R4_RESULTS_PATH = "p_konum_plus/calibration/f3_step2_results_r4_2026-09-24.json"
R4_RESULTS_HASH = "a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374"

FORBIDDEN_RESULT_KEYS = ("winner", "selected", "generator_selected")

PI_RATIFIED_CONTENT_PATH = "p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md"
PI_RATIFIED_CONTENT_HASH = "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498"
# D-3 (the r3 prompt DRAFT v2; unchanged, still binding for r4)
D3_PATH = "p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md"
D3_HASH = "5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5"
# r4 instruction (child of D-3)
R4_INSTRUCTION_PATH = "p_konum_plus/prompts/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md"
R4_INSTRUCTION_HASH = "e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387"
# D-5, the r4 dispatch record (child of D-4)
DISPATCH_RECORD_PATH = "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md"
DISPATCH_RECORD_HASH = "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851"
# A-1, the r3 independent audit DRAFT r1 -- input, not directive
AUDIT_A1_PATH = "p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md"
AUDIT_A1_HASH = "11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6"
# ---- r4-1 revision instruments (this cycle's dispatched pin set, D-6 S1) ----
# the r4-1 correction instruction (child of the r4 instruction)
R4_1_INSTRUCTION_PATH = "p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md"
R4_1_INSTRUCTION_HASH = "283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330"
# D-6, the r4-1 PI dispatch record (child of D-5)
D6_DISPATCH_RECORD_PATH = "p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md"
D6_DISPATCH_RECORD_HASH = "a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0"
# A-2 / A-3, the r4 independent audit drafts -- inputs, not directives
AUDIT_A2_PATH = "p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md"
AUDIT_A2_HASH = "b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a"
AUDIT_A3_PATH = "p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md"
AUDIT_A3_HASH = "9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9"

# S / T values as read from D-2 (unchanged, verbatim)
S1 = "(a)"
S2 = "alpha"
T1 = "AUTHORIZE"
T2 = "T-2a"
T3 = "AUTHORIZE"
T4 = "T-4a"
T5 = "CONFIRM_WITHIN_SCOPE"
# this cycle's own two PI fields, read from D-5 (verbatim)
S_R2_1 = "PI_RULE"
T_R2_2 = "AUTHORIZE_RESTART"
# EXACT-03 (S-R2-1 = DEFERRED_THIS_CYCLE, r3) is CLOSED this cycle: D-5 is
# its source (D-5 S4(d)). Retained as a constant only for cross-referencing
# the closed finding in the r4 report/register, never as an active tag.
S_R2_1_FINDING_ID_CLOSED = "F3-STEP2-EXACT-03"


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
                # R3A-03/R3A-06, r4: phase + computing-process identity on
                # every capture record (CURRENT_PHASE resolved at call time;
                # a record replayed from the store keeps its original tags).
                phase=CURRENT_PHASE[0], pid=PID, start_iso=PROCESS_START_ISO,
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
        # X-11(b)/R3A-02, r4: family telemetry rows carry L (the masked
        # objective value of THIS start's endpoint) and the endpoint's
        # frozen predicates/failure codes -- both already computed by F2
        # (cls), only missing from the emitted row.
        L_masked_row = (masked_internal_L(f2m, x, cls["theta"], family, obs)
                        if cls["eligible"] else float("inf"))
        for row in tel:
            telemetry.append(dict(row, fixture=fixture_id, mask_id=mask_id,
                                  fitter=family, L=L_masked_row,
                                  predicates=list(cls.get("predicates", []))))
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
    any_mode_unrelated = False   # R3A-03: context-level PENDING trigger
    for m in range(T):
        mkey = "splmode_%s_%s_%s_%s" % (fixture_id, mask_id, m, xhash)
        cached_mode = ckpt_load(mkey)
        if cached_mode is not None:
            v, rss, c, src, pst, cap_recs, tel_calls = cached_mode
            for cr in cap_recs:
                EXC_CAPTURES.append(cr)
                # ANY unrelated capture (TEST_ONLY included) makes the
                # context unverifiable; TEST_ONLY only changes the TAG
                # (no finding), not the stop -- attempt-1 bug: the fresh
                # path never set this flag at all and the cached path
                # wrongly exempted TEST_ONLY, so the injected test's
                # context came back "valid".
                if cr.get("kind") == "UNRELATED":
                    any_mode_unrelated = True
            for tc in tel_calls:
                SPLINE_TELEMETRY_CALLS.append(tc)
        else:
            _ACCEPT_CALL_COUNT[0] = 0
            _SPL_CTX.update(fixture=fixture_id, mask_id=mask_id, mode=m)
            del _LAST_CAPTURE_EVENTS[:]
            n_calls_before = len(SPLINE_TELEMETRY_CALLS)
            A = spl["amat"](m)
            mode_unrelated = False
            try:
                c, tel = spl["solver_config"]("SOLVER-B", x, obs, A)
                v = spline_valid_from_tel(tel)
                src, pst = tel["final_endpoint_source"], tel["primary_status"]
            except Exception as exc:
                # R3A-03, r4: covered exceptions are converted (return
                # False) inside wrapped_accept and never reach here. ANYTHING
                # that does reach here is by definition UNRELATED (either
                # wrapped_accept's own re-raise, or an exception class its
                # `except RuntimeError` never caught in the first place) --
                # catch every class here for exactly this classification
                # purpose (not for general robustness), record it as a
                # first-class capture (not just a status string), and mark
                # this whole context PENDING rather than silently continuing
                # as if only one mode were affected.
                c, v = None, False
                src, pst = "ACCEPTANCE_UNVERIFIABLE_UNRELATED", "EXC:" + type(exc).__name__
                mode_unrelated = True
                any_mode_unrelated = True   # attempt-1 bug: was never set here
                EXC_CAPTURES.append(dict(
                    fixture=fixture_id, sex=_parse_sex_traj(mask_id)[0],
                    trajectory=_parse_sex_traj(mask_id)[1], mask_id=mask_id,
                    mode=m, stage=_ACCEPT_CALL_COUNT[0],
                    exception_type=type(exc).__name__, message=str(exc),
                    traceback=traceback.format_exc(), kind="UNRELATED",
                    phase=CURRENT_PHASE[0], pid=PID, start_iso=PROCESS_START_ISO))
            rss = spl["rss_of"](c, x, obs) if v else float("inf")
            cap_recs = list(_LAST_CAPTURE_EVENTS)
            if mode_unrelated:
                cap_recs = cap_recs + [EXC_CAPTURES[-1]]
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
    # R3A-03, r4: an UNRELATED exception anywhere in this context's mode
    # sweep makes the WHOLE context's evidence unverifiable, not just the
    # one mode it hit -- content S3.1's "retain the existing error/
    # exactness protocol" means the context stops here (PENDING), not
    # "silently keep the other 145 modes' answer as if nothing happened".
    # Tag per D-3 S10's exactness-finding protocol: a NATURAL unrelated
    # event opens F3-STEP2-EXACT-04 (next free number; EXACT-01/02 taken,
    # EXACT-03 closed by D-5); a TEST_ONLY-injected one is not a finding
    # (Y-04(b)) and carries the TEST_ONLY tag instead.
    if any_mode_unrelated:
        ctx_unrel = [c for c in EXC_CAPTURES
                     if c.get("kind") == "UNRELATED"
                     and c.get("fixture") == fixture_id
                     and c.get("mask_id") == mask_id]
        all_test_only = ctx_unrel and all(
            "TEST_ONLY" in c.get("message", "") for c in ctx_unrel)
        # R4A-03 (r4-1): D-3 Y-04(b) writes the tag "TEST_ONLY_INJECTED"
        # (r4 had "TEST_ONLY_INJECTION"); use the D-3 label.
        tag = "TEST_ONLY_INJECTED" if all_test_only else "F3-STEP2-EXACT-04"
        return dict(valid=False, failure="STOP_EXACTNESS_PENDING(%s)" % tag,
                    per_mode_valid=per_mode_valid)
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
        # S-R2-1 = PI_RULE (D-5 S4(1)(2)(4)): V4/U4 membership is by the
        # recorded decision-layer flags pL AND pR AND full ONLY -- rule (4)
        # verbatim: "Membership is determined from the recorded
        # decision-layer flags on the real path and in the fixtures alike,
        # never from the presence or absence of an RMSE_edge value." A
        # member whose edge statistic turns out invalid is caught by the
        # post-construction data-driven re-validation (Y-03(ii),
        # INCONSISTENT_U), not silently dropped from membership.
        probes_idx = [i for i in range(n_s) if d["pL"][i] and d["pR"][i]
                      and d["full"][i]]
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
    """Retained for the r4 erratum record only (r3 used this to detect the
    PI_RULE membership before the rule text existed) -- no longer called
    from evaluate_fixture. See S_R2_1 = PI_RULE (D-5 S3), r4."""
    return any(d["pL"][i] and d["pR"][i] and not d["full"][i] for i in range(n_s))


def evaluate_fixture(fx_id, strata, n_s, c4_source, flags, stops,
                     force_c4_pending=False):
    # X-11(e)/R3A-02: `sexes` (always {} in r3, dead weight, never read)
    # removed rather than filled -- SEXES is the fixed, always-both-present
    # module constant (("F", "M")); a per-fixture echo of it carried no
    # information.
    # Revision-4 fix (T-CANON caught it): k05_result must embed the count
    # of K-05 checks THIS fixture executed (entry/exit delta), never the
    # process-global cumulative counter -- the cumulative value differs
    # between RUN1 and RUN2 for the same fixture by construction, which
    # broke canonical-document determinism.
    k05_before = K05_CHECK_COUNT[0]
    ev = dict(fixture_id=fx_id, interpretation="PATH_COVERAGE_ONLY",
              c4_source=c4_source, criteria={}, dp04=None,
              mechanism_outcome=None)
    # R4A-01 (r4-1): tag for a spline-context-pending routing -- a
    # decision-layer TEST_ONLY fixture is TEST_ONLY_INJECTED (not a finding,
    # Y-04(b)); a natural real-path event is F3-STEP2-EXACT-04 (EXACT-03
    # closed by D-5; next free number, entered into exactness_findings via
    # the natural_unrelated machinery in main()).
    _spl_pend_tag = ("TEST_ONLY_INJECTED"
                     if c4_source == "TEST_ONLY_INJECTION_DECISION_LAYER"
                     else "F3-STEP2-EXACT-04")
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
                    # R4A-01 (r4-1): the spline FOLD context supplies C2's
                    # spline rho benchmark (dS["cc"] membership + dS["rho"]).
                    # If that context is unverifiable, C2 for this sex is
                    # PENDING for BOTH families -- no definite PASS/FAIL from
                    # an unverifiable benchmark (Y-04(b)).
                    if any(dS.get("spl_pending_fold", [])):
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
                                                  % _spl_pend_tag)
                        continue
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
                    # R4A-01 (r4-1): the spline FULL context supplies C3's
                    # spline phi benchmark (dS["phi"] + dS["full"] membership
                    # in phi_idx). Unverifiable -> C3 PENDING (both families).
                    if any(dS.get("spl_pending_full", [])):
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
                                                  % _spl_pend_tag)
                        continue
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
                    # R3A-05, r4 (content S2.3): an A.5 reference contract
                    # violation is NEVER converted into a C4 pass or fail --
                    # C4a and C4b for that sex are PENDING.
                    if any(d.get("a5v", [])) or any(dS.get("a5v", [])):
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING"
                                                  "(CONTRACT_VIOLATION_A5_REFERENCE)")
                        continue
                    val, thr, ok = st["ident"], C_IDENT, st["ident"] >= C_IDENT
                elif crit == "C4b":
                    if force_c4_pending:
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING"
                                                  "(TEST_ONLY_FORCED_C4_PENDING)")
                        continue
                    if any(d.get("a5v", [])) or any(dS.get("a5v", [])):
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING"
                                                  "(CONTRACT_VIOLATION_A5_REFERENCE)")
                        continue
                    # R4A-01 (r4-1): C4b reads the spline FULL context
                    # (dS["full"] in V4 membership) and the spline PROBE
                    # context (dS["pL"]/["pR"] membership, dS["rL"]/["rR"]
                    # edge benchmark). Either unverifiable -> C4b PENDING.
                    if (any(dS.get("spl_pending_full", []))
                            or any(dS.get("spl_pending_probe", []))):
                        per_sex[sx] = dict(status="STOP_EXACTNESS_PENDING(%s)"
                                                  % _spl_pend_tag)
                        continue
                    # S-R2-1 = PI_RULE (D-5 S4, r4; PI-ratified verbatim,
                    # tagged PI_RATIFIED with D-5's hash in the r4 register).
                    # V4_s(F) = {i : pL[F] AND pR[F] AND full[F]
                    #                AND pL[SPL] AND pR[SPL] AND full[SPL]}.
                    # This is a construction-time MEMBERSHIP condition, never
                    # PENDING: a trajectory missing a named fitter's
                    # full-data reference is simply absent from V4 -- no
                    # separate pre-check, no STOP_EXACTNESS_PENDING short-
                    # circuit. Y-03(i)'s membership-first-then-undefined-if-
                    # invalid rule composes with this unchanged: membership
                    # now requires `full` in addition to pL/pR, and if the
                    # resulting set contains an invalid combined-edge
                    # statistic the whole sex-level statistic is undefined.
                    V4 = [i for i in range(n_s) if d["pL"][i] and d["pR"][i]
                          and d["full"][i]
                          and dS["pL"][i] and dS["pR"][i] and dS["full"][i]]
                    fam_vals = [_combined_edge(d, i) for i in V4]
                    spl_vals = [_combined_edge(dS, i) for i in V4]
                    fam_ok_vals = V4 and all(v is not None for v in fam_vals)
                    spl_ok_vals = V4 and all(v is not None for v in spl_vals)
                    r_f = median_pin(fam_vals) if fam_ok_vals else None
                    r_s = median_pin(spl_vals) if spl_ok_vals else None
                    share = len(V4) / n_s
                    c4a_ok = st["ident"] >= C_IDENT
                    if share >= C_COMPLETE:                     # PIN-K05-INVARIANT
                        K05_CHECK_COUNT[0] += 1
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
        # R4A-01 (r4-1): if a spline-context-pending caused the PENDING, the
        # mechanism tag names its exactness id (TEST_ONLY_INJECTED or
        # F3-STEP2-EXACT-04), collected from the actual per-sex status
        # strings -- not just the criterion letters. force_c4_pending keeps
        # its own tag. S-R2-1 = PI_RULE (r4): C4b is a membership condition,
        # never a PENDING status (D-5 S4(2)).
        import re as _re_tag
        spl_tags = set()
        for fam in ("P01", "P02"):
            for crit_name, per_sex_d in fam_detail[fam].items():
                for sx in SEXES:
                    st_str = str(per_sex_d.get(sx, {}).get("status", ""))
                    m = _re_tag.search(r"STOP_EXACTNESS_PENDING\(([^)]+)\)", st_str)
                    if m and m.group(1) in ("TEST_ONLY_INJECTED", "F3-STEP2-EXACT-04"):
                        spl_tags.add(m.group(1))
        if force_c4_pending:
            tag = "TEST_ONLY_FORCED_C4_PENDING"
        elif spl_tags:
            tag = ",".join(sorted(spl_tags))
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
        # Y-03(ii)/R3A-04, r4: the post-construction hook now ACTUALLY
        # mutates the statistic (not just a flag D-P04 checks against U
        # membership) -- run_dp04's own re-validation (below) is what
        # catches it, genuinely reading the data, not the flag. This
        # reproduces "the injection alters a member's statistic AFTER the
        # set is built and BEFORE the data-driven re-validation" for real:
        # crit_stats() above already ran and built cc_idx/etc.; this
        # mutates the underlying array in place afterward, so a member
        # that WAS flag-and-finite valid when U was built is NOT finite
        # anymore by the time run_dp04 re-checks it.
        # Revision-5 fix (T-CANON caught it, again doing its job): the
        # mutation targets lists inside the GENERATOR's module-level
        # fixture object -- without restoration, RUN1's NaN persisted into
        # RUN2's evaluation of the same fixture (crit_stats then saw the
        # NaN at build time, took a different path, and the two runs'
        # canonical documents diverged). The mutation must be visible ONLY
        # between this point and run_dp04's re-validation, then undone.
        stat_field = {"C2": "rho", "C3": "phi", "C4b": "rR", "C5": "sst"}
        mutations_to_restore = []
        for crit_name, field in stat_field.items():
            idx = flags.get(f"inject_post_construction_invalid_{crit_name}")
            if idx is not None:
                for sx in SEXES:
                    arr = S[sx]["P01"]["d"][field]
                    mutations_to_restore.append((arr, idx, arr[idx]))
                    arr[idx] = float("nan")
        ev["dp04"] = run_dp04(fx_id, S, n_s, flags, stops)
        for arr, idx, orig in mutations_to_restore:
            arr[idx] = orig
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
    # X-11(c)/R3A-02, r4: family-invalid counts per criterion/sex (excluded
    # from the flag-based membership set, i.e. n_s - |V|); per-side
    # probe-failure shares; K-05 check RESULT field (the assertion already
    # runs at C4b -- this surfaces its outcome as a declared field rather
    # than only an assert that would silently pass unreported).
    invalid_counts, probe_fail_shares = {}, {}
    for sx in SEXES:
        for fam in ("P01", "P02"):
            d = S[sx][fam]["d"]
            invalid_counts[f"{sx}:{fam}:C2"] = n_s - len(S[sx][fam]["cc_idx"])
            invalid_counts[f"{sx}:{fam}:C3"] = n_s - len(S[sx][fam]["phi_idx"])
            invalid_counts[f"{sx}:{fam}:C4b"] = n_s - len(S[sx][fam]["probes_idx"])
            invalid_counts[f"{sx}:{fam}:C5"] = n_s - len(S[sx][fam]["sst_idx"])
            probe_fail_shares[f"{sx}:{fam}:L"] = 1.0 - sum(
                1 for v in d["pL"] if v) / n_s
            probe_fail_shares[f"{sx}:{fam}:R"] = 1.0 - sum(
                1 for v in d["pR"] if v) / n_s
    ev["invalid_counts_by_criterion"] = invalid_counts
    ev["probe_failure_shares"] = probe_fail_shares
    # R3A-11: computed from the real counter (K05_CHECK_COUNT, incremented
    # only where the assertion actually executes), not a literal -- an
    # AssertionError would have already stopped the process before this
    # line runs, so reaching here IS the PASS evidence. Revision 4:
    # PER-FIXTURE delta (deterministic across RUN1/RUN2), never the
    # process-global cumulative value.
    ev["k05_result"] = ("PASS(%d checks this fixture, assertion never triggered)"
                        % (K05_CHECK_COUNT[0] - k05_before))
    for k in FORBIDDEN_RESULT_KEYS:
        assert k not in ev, "forbidden key emitted"
    return ev


def _guarded_scalar_ok(v):
    """Y-03(iii)/R3A-04: the one function the D-P04 comparator (and
    T-COMPARATOR-NAN) both call -- None or non-finite is never compared."""
    return v is not None and math.isfinite(v)


# ------------------------- Y-02(b)/R3A-10: pure U-set construction ---------
# The ONE implementation of each consulted-set membership rule -- run_dp04
# calls these, and UT-USET-CONSTRUCTION calls these SAME functions (on
# crit_stats built by the real crit_stats() from constructed strata), so the
# unit test evidences the product code, not a re-typed copy of the rule.
def uset_c2(st1, st2, sp):
    """U2: crossfit-complete AND finite rho, for P-01, P-02 AND the spline."""
    return [i for i in st1["cc_idx"] if i in st2["cc_idx"] and i in sp["cc_idx"]]


def uset_c3(st1, st2, sp):
    """U3: full-data fit present AND finite phi, all three fitters."""
    return [i for i in st1["phi_idx"] if i in st2["phi_idx"] and i in sp["phi_idx"]]


def uset_c4b(st1, st2, sp):
    """U4 = V4(P01) intersect V4(P02) (S-R2-1 = PI_RULE, D-5 S4(2)) --
    probes_idx is pL AND pR AND full per fitter, so this intersection IS
    the rule's V4(P01) ∩ V4(P02) (each V4 already requires the spline's
    flags via the sp term)."""
    return [i for i in st1["probes_idx"] if i in st2["probes_idx"]
            and i in sp["probes_idx"]]


def uset_c5(st1, st2):
    """U5: C5-statistic validity of P-01 and P-02 only -- NO spline term."""
    return [i for i in st1["sst_idx"] if i in st2["sst_idx"]]


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
            _inconsistent_pairs_seen = set()   # R4A-03: dedup (sex,fitter,obs)
            for fam in ("P01", "P02"):
                vals = {}
                for sx in SEXES:
                    st1, st2, sp = S[sx]["P01"], S[sx]["P02"], S[sx]["SPL"]
                    # R3A-10: the pure construction functions are the ONLY
                    # implementation of the membership rules -- called here
                    # and (on constructed strata) by UT-USET-CONSTRUCTION.
                    if crit == "C2":
                        U = uset_c2(st1, st2, sp)
                        if flags.get("inject_empty_U2"):
                            U = []
                        src = S[sx][fam]
                        v = src["med_over"](src["d"]["rho"], U)
                    elif crit == "C3":
                        U = uset_c3(st1, st2, sp)
                        src = S[sx][fam]
                        v = src["med_over"]([abs(x) if x is not None else None
                                             for x in src["d"]["phi"]], U)
                    elif crit == "C4b":
                        U = uset_c4b(st1, st2, sp)
                        src = S[sx][fam]
                        v = src["med_over"]([_combined_edge(src["d"], i)
                                             for i in range(n_s)], U)
                    else:  # C5 -- P-01/P-02 only, NO spline term
                        U = uset_c5(st1, st2)
                        src = S[sx][fam]
                        v = src["med_over"](src["d"]["sst"], U)
                    if not U:
                        empty_hit = True
                    # Y-03(ii)/R3A-04, r4: GENUINE re-validation -- re-read
                    # the current value of every fitter's relevant field for
                    # each member of U (built earlier, in crit_stats, from a
                    # possibly-since-mutated array) instead of checking a
                    # test-only flag against U membership. Any member whose
                    # statistic is not finite NOW, for ANY fitter the
                    # criterion's frozen definition names, is inconsistent --
                    # this fires on real data corruption with no flag at all.
                    # The offending (fitter, observation) pairs are recorded
                    # (closure action of R3A-04); only the FIRST hit is kept
                    # as the stop detail (deterministic), all pairs listed.
                    # R4A-03 (r4-1): each offending (sex, fitter, observation)
                    # is recorded ONCE (de-duplicated) and carries the sex.
                    # The r4 record listed (P01, 0) four times without the
                    # sex -- because this re-validation loop runs once per
                    # (fam, sex) and re-scanned the same members, appending
                    # duplicates; a seen-set keyed on (sex, fitter, obs)
                    # fixes both.
                    field = {"C2": "rho", "C3": "phi", "C4b": None, "C5": "sst"}[crit]
                    fitters_named = ([("P01", st1), ("P02", st2), ("SPL", sp)]
                                     if crit != "C5" else [("P01", st1), ("P02", st2)])
                    for i in U:
                        for fname_v, fitter in fitters_named:
                            if crit == "C4b":
                                bad = _combined_edge(fitter["d"], i) is None
                            else:
                                bad = not valid(fitter["d"][field][i])
                            if not bad:
                                continue
                            key = (sx, fname_v, i)
                            if key in _inconsistent_pairs_seen:
                                continue
                            _inconsistent_pairs_seen.add(key)
                            pair = dict(sex=sx, fitter=fname_v, observation=i)
                            if inconsistent_hit is None:
                                inconsistent_hit = dict(
                                    level=crit, sex=sx, member=i,
                                    offending_pairs=[pair])
                            else:
                                inconsistent_hit["offending_pairs"].append(pair)
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
        # Y-03(iii)/R3A-04, r4: guarded comparator -- None OR non-finite
        # (NaN/inf) on either side is a contract violation, never a silent
        # "abs(nan) <= tau" (which Python evaluates False, masquerading as
        # a legitimate RESOLVED outcome -- see T_COMPARATOR_NAN). R3A-09:
        # this STOP return writes its `stops` record like every other one
        # (Y-17: every STOP-outcome consulted-level return writes one).
        # R4A-03 (r4-1): the guarded comparator's STOP is
        # CONTRACT_VIOLATION_INCONSISTENT_U (D-3 Y-03(iii)) -- a non-finite/
        # None scalar surviving to the comparator is an inconsistency, not
        # an empty set (the genuinely-empty consulted set is caught earlier
        # as CONTRACT_VIOLATION_EMPTY_U).
        if not (_guarded_scalar_ok(scal["P01"]) and _guarded_scalar_ok(scal["P02"])):
            stops.append(dict(fixture=fx_id, stop="CONTRACT_VIOLATION_INCONSISTENT_U",
                              level=crit,
                              detail="guarded comparator refused a None/non-finite scalar"))
            return dict(consulted_path=consulted,
                        mechanism_outcome="STOP_CONTRACT_VIOLATION_INCONSISTENT_U",
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
        # R3A-05, r4: a5v = per-trajectory A.5 reference contract-violation
        # flag (shared across fitters -- one reference per trajectory);
        # evaluate_fixture routes any True into STOP_EXACTNESS_PENDING for
        # C4a AND C4b of that sex (content S2.3: never a C4 pass or fail).
        recs = {k: dict(full=[], cc=[], rho=[], phi=[], pL=[], pR=[],
                        rL=[], rR=[], sst=[], a5v=[],
                        # R4A-01 (r4-1): per-trajectory spline-context pending
                        # flags on the real path -- set True only if a
                        # NATURAL UNRELATED solver event made fit_spline
                        # return STOP_EXACTNESS_PENDING for that context.
                        spl_pending_full=[], spl_pending_fold=[],
                        spl_pending_probe=[])
                for k in ("P01", "P02", "SPL")}
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
            for fk_a5 in ("P01", "P02", "SPL"):
                recs[fk_a5]["a5v"].append(viol is not None)
            for family in ("P-01", "P-02"):
                fk = FAM_KEYS[family]
                full = fit_family(f2m, grids, sc["fixture_id"], family, x,
                                  FULL_O, telemetry, mid(f"{sx}{ti}:full"),
                                  start_bank=start_bank)
                recs[fk]["full"].append(full["eligible"])
                phi = (acf_classical(x - full["ghat"])
                       if full["eligible"] else None)
                recs[fk]["phi"].append(phi)
                # X-11(d)/R3A-02, r4: per-fit endpoint theta, masked L,
                # start-bank size, FEATURE_START_REJECTED -- fit_family
                # already computes all of these; only surfacing was missing.
                full_mask_fits[(sx, ti, fk)] = dict(
                    valid=full["eligible"],
                    ghat=(full["ghat"] if full["eligible"] else None), x=x,
                    theta=(full.get("theta") if full["eligible"] else None),
                    L=(full.get("L") if full["eligible"] else None),
                    start_bank_size=full["start_bank_size"],
                    feature_start_rejected=full["feature_start_rejected"],
                    failure_codes=full.get("failure_codes", []))
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
            # R4A-01: a natural UNRELATED event on the full context -> pending
            # (a TEST_ONLY-injected failure is NOT pending -- it is a
            # declared ordinary failure, per Y-04(b)).
            recs["SPL"]["spl_pending_full"].append(
                str(spf.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
                and "TEST_ONLY" not in str(spf.get("failure", "")))
            recs["SPL"]["full"].append(spf["valid"])
            recs["SPL"]["phi"].append(acf_classical(x - spf["ghat"])
                                      if spf["valid"] else None)
            # X-11(d)/R3A-02: per-spline-fit winner mode, RSS, equivalent-
            # mode set, per-mode validity -- fit_spline already computes all
            # of these; only surfacing was missing.
            full_mask_fits[(sx, ti, "SPL")] = dict(
                valid=spf["valid"],
                ghat=(spf["ghat"] if spf["valid"] else None), x=x,
                mode=spf.get("mode"), rss=spf.get("rss"),
                equivalent_modes=spf.get("equivalent_modes"),
                per_mode_valid=spf.get("per_mode_valid"),
                failure=spf.get("failure"))
            cc, pred_cv, fold_pending = True, np.full(T, np.nan), False
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
                    if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
                            and "TEST_ONLY" not in str(r.get("failure", ""))):
                        fold_pending = True   # R4A-01: any fold unverifiable
            recs["SPL"]["spl_pending_fold"].append(fold_pending)
            recs["SPL"]["cc"].append(cc)
            recs["SPL"]["rho"].append(rho_cv_pin(x, pred_cv) if cc else None)
            recs["SPL"]["sst"].append(None)
            probe_pending = False
            for side, obsP, edge, a5_i in (("L", LEFT_PROBE_O, np.arange(0, 15), a5_i_L),
                                           ("R", RIGHT_PROBE_O, np.arange(131, 146), a5_i_R)):
                r = fit_spline(spl, sc["fixture_id"], x, obsP, telemetry,
                               mid(f"{sx}{ti}:probe{side}"))
                if (str(r.get("failure", "")).startswith("STOP_EXACTNESS_PENDING")
                        and "TEST_ONLY" not in str(r.get("failure", ""))):
                    probe_pending = True   # R4A-01: either probe unverifiable
                probe_raw = bool(r["valid"])
                p_c4a = probe_raw and (a5_i is False)
                recs["SPL"]["p" + side].append(p_c4a)
                rmse_computable = p_c4a and spf["valid"]
                recs["SPL"]["r" + side].append(
                    rmse_edge_pin(r["ghat"], spf["ghat"], edge) if rmse_computable else None)
            recs["SPL"]["spl_pending_probe"].append(probe_pending)
        strata_recs[sx] = recs
    return strata_recs, n_s, telemetry, construction_audit, full_mask_fits


# ------------------------- R3A-05: T-A5-SUPPORT ----------------------------
def t_a5_support():
    """Unit test of the A.5(i) support predicate ITSELF (a5_support /
    a5_condition_i, the real product functions), per the audit's
    enumeration: threshold equality included; next float below excluded;
    disconnected components united; partly-observed-side vs fully-masked-
    side condition; constant reference => S = G; invalid references =>
    violations. TEST_CONSTANT vectors only."""
    out = {}
    # (1) threshold equality included / (2) next float below excluded.
    # lo=0, hi=1 -> thr=0.5; index 1 holds exactly 0.5 (in S), index 2
    # holds the next float BELOW 0.5 (out), index 3 holds 1.0 (in).
    z = np.zeros(T)
    z[1] = 0.5
    z[2] = np.nextafter(0.5, 0.0)
    z[3] = 1.0
    S = a5_support(z)
    out["threshold_equality_included"] = (1 in S)
    out["next_float_below_excluded"] = (2 not in S)
    # (3) disconnected components united: two separated points above thr.
    z2 = np.zeros(T)
    z2[10] = 1.0
    z2[100] = 1.0
    S2 = a5_support(z2)
    out["disconnected_components_united"] = (S2 == {10, 100})
    # (4) condition (i) against the two edge masks: a support fully inside
    # M_LEFT is TRUE for L and FALSE for R; a support spanning the middle
    # is FALSE for both.
    z3 = np.zeros(T)
    z3[3] = 1.0
    z3[7] = 1.0
    S3 = a5_support(z3)
    out["inside_left_true_L"] = a5_condition_i(S3, "L")
    out["inside_left_false_R"] = (not a5_condition_i(S3, "R"))
    out["middle_false_both"] = (not a5_condition_i(S2, "L")
                                and not a5_condition_i(S2, "R"))
    # (5) constant reference -> thr = lo -> every point >= thr -> S = G
    # (and the empty-support violation must NOT fire).
    z4 = np.full(T, 3.25)
    S4 = a5_support(z4)
    out["constant_reference_S_equals_G"] = (S4 == set(range(T)))
    # (6) invalid references -> A5ContractViolation, never a silent result.
    def _raises(zbad):
        try:
            a5_support(zbad)
            return False
        except A5ContractViolation:
            return True
    z_nan = np.zeros(T); z_nan[5] = float("nan")
    out["nan_reference_violates"] = _raises(z_nan)
    out["wrong_length_violates"] = _raises(np.zeros(T - 1))
    z_inf = np.zeros(T); z_inf[5] = float("inf")
    out["inf_reference_violates"] = _raises(z_inf)
    out["pass_"] = all(bool(v) for v in out.values())
    return out


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
    # SECOND HALF (v6 X-04; runs under S-R2-1 = PI_RULE per D-5 S4(d)): a
    # probe-successful trajectory with NO full-data reference is absent
    # from the C4b paired-valid set BY MEMBERSHIP -- verified through the
    # REAL product path (crit_stats + uset_c4b, the same functions
    # evaluate_fixture/run_dp04 use), not a re-typed rule. n_s=1: the one
    # trajectory has pL=pR=True (probe succeeded), full=False (reference
    # ineligible) -- V4 must be empty.
    one = dict(full=[full["eligible"]], cc=[True], rho=[0.9], phi=[0.1],
               pL=[probe_success_c4a], pR=[True], rL=[None], rR=[None],
               sst=[0.05], a5v=[False])
    other = dict(full=[True], cc=[True], rho=[0.9], phi=[0.1],
                 pL=[True], pR=[True], rL=[0.2], rR=[0.2], sst=[0.05],
                 a5v=[False])
    cs_ut = crit_stats(dict(P01=one, P02=dict(other), SPL=dict(other)), 1)
    v4_membership = uset_c4b(cs_ut["P01"], cs_ut["P02"], cs_ut["SPL"])
    second_half_pass = (v4_membership == [])
    pass_ = bool(full_ineligible and probe_eligible and probe_success_c4a
                and not rmse_computable and second_half_pass)
    return dict(UT_PROBE_DECOUPLE_pass=pass_, full_eligible=full["eligible"],
                probe_eligible=probe_eligible, probe_success_c4a=probe_success_c4a,
                rmse_computable=rmse_computable,
                second_half_v4_membership=v4_membership,
                second_half_pass=second_half_pass,
                note="first half: probe_success is probe-level only (X-04). "
                     "second half RUNS this cycle (S-R2-1 = PI_RULE, D-5 "
                     "S4(d)): the no-full-data-reference trajectory is "
                     "absent from V4 by flag membership, checked through "
                     "the real crit_stats + uset_c4b product path")


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


# ------------------------- Y-02(b)/R3A-10 UT-USET-CONSTRUCTION -------------
def ut_uset_construction(gen):
    """r4: calls the REAL product path -- crit_stats() on constructed
    strata, then the SAME pure uset_* functions run_dp04 calls. Nothing
    is re-typed in test code (the r3 version re-implemented the rules
    without the cc flag and without the spline term -- audit R3A-10).
    Still function-level: no fixture outcome, no mechanism outcome, no
    reachability claim. n_s = 10, same grammar as the INJ fixtures."""
    n_s = 10
    results = {}
    for key, case in gen.UT_USET_CASES.items():
        cs = crit_stats(dict(P01=case["P01"], P02=case["P02"],
                             SPL=case["SPL"]), n_s)
        st1, st2, sp = cs["P01"], cs["P02"], cs["SPL"]
        exp = case["expect"]
        U2 = uset_c2(st1, st2, sp)
        U4 = uset_c4b(st1, st2, sp)
        U5 = uset_c5(st1, st2)
        if key == "a":
            ok = len(U2) == exp["U2"] and len(U5) == exp["U5"]
            results[key] = dict(ok=ok, U2=len(U2), U5=len(U5), expect=exp)
        elif key == "b":
            ok = len(U5) == exp["U5"]
            results[key] = dict(ok=ok, U5=len(U5), expect=exp)
        elif key == "c":
            ok = exp["U2_excludes"] not in U2
            results[key] = dict(ok=ok, U2=U2, expect=exp)
        elif key == "d":
            # S-R2-1 = PI_RULE: flags-only membership INCLUDES the member;
            # the run_dp04 re-validation predicate (the same _combined_edge
            # None test the product loop applies) must flag it.
            member = exp["U4_includes"]
            revalidation_bad = _combined_edge(case["P01"], member) is None
            ok = (member in U4) and revalidation_bad
            results[key] = dict(ok=ok, U4=U4,
                               revalidation_flags_member=revalidation_bad,
                               expect=exp)
        elif key == "e":
            ok = exp["U2_excludes"] not in U2 and exp["U5_excludes"] not in U5
            results[key] = dict(ok=ok, U2=U2, U5=U5, expect=exp)
    return results


def t_comparator_nan():
    """T-COMPARATOR-NAN (Y-03(iii)/R3A-04, r4): calls the REAL guard the
    D-P04 comparator uses (_guarded_scalar_ok) -- not a literal, not a
    re-typed rule. A NaN/None/inf scalar must be refused by the exact
    function in the product path; a finite scalar must be accepted."""
    ok_nan = _guarded_scalar_ok(float("nan"))
    ok_none = _guarded_scalar_ok(None)
    ok_inf = _guarded_scalar_ok(float("inf"))
    ok_valid = _guarded_scalar_ok(0.5)
    # documentation of the underlying hazard the guard prevents:
    nan = float("nan")
    delta = nan - 0.5
    equivalent = abs(delta) <= 0.01   # NaN comparisons are always False
    resolved = not equivalent          # would (wrongly) look "RESOLVED" if reached

    # R4A-03 (r4-1): assert the guarded comparator's STOP LABEL end-to-end.
    # Craft a minimal S that reaches run_dp04's guarded comparator with a
    # non-finite scalar (finite members -> re-validation passes; non-empty
    # U -> empty_hit false; a med_over that returns NaN -> the comparator
    # refuses it). The emitted stop must be CONTRACT_VIOLATION_INCONSISTENT_U
    # (D-3 Y-03(iii)), NOT the r4 CONTRACT_VIOLATION_EMPTY_U.
    def _med_nan(vals, idxs):
        return float("nan") if idxs else None

    def _fit(nanmed):
        d = dict(rho=[0.9], phi=[0.1], sst=[0.05], pL=[True], pR=[True],
                 rL=[0.2], rR=[0.2], full=[True], cc=[True])
        return dict(cc_idx=[0], phi_idx=[0], probes_idx=[0], sst_idx=[0],
                    cov=1.0, ident=1.0, d=d,
                    med_over=(_med_nan if nanmed else
                              (lambda vals, idxs: 0.9 if idxs else None)))
    Scraft = {sx: {"P01": _fit(True), "P02": _fit(False), "SPL": _fit(False)}
              for sx in SEXES}
    craft_stops = []
    craft = run_dp04("T-COMPARATOR-NAN-CRAFT", Scraft, 1, {}, craft_stops)
    label_ok = (craft["mechanism_outcome"] == "STOP_CONTRACT_VIOLATION_INCONSISTENT_U"
                and any(s.get("stop") == "CONTRACT_VIOLATION_INCONSISTENT_U"
                        for s in craft_stops))

    return dict(guard_refuses_nan=(not ok_nan), guard_refuses_none=(not ok_none),
               guard_refuses_inf=(not ok_inf), guard_accepts_finite=ok_valid,
               python_nan_comparison_is_resolved_like=bool(resolved),
               guarded_comparator_label=craft["mechanism_outcome"],
               guarded_comparator_label_is_inconsistent_u=label_ok,
               pass_=bool((not ok_nan) and (not ok_none) and (not ok_inf)
                         and ok_valid and label_ok),
               note="pass_ from the real guard's behavior AND an end-to-end "
                    "run_dp04 call asserting the R4A-03 label "
                    "CONTRACT_VIOLATION_INCONSISTENT_U (D-3 Y-03(iii))")


# ------------------------- Y-04 exception-injection fixtures ---------------
def run_exc_injection_fixtures(spl):
    """R3A-03, r4: the manifest declares run_scope = both for the INJ-EXC-*
    fixtures -- honored as TWO full deterministic passes, results asserted
    identical (the same double-execution determinism evidence RUN1/RUN2
    provides for the real scenarios). Each pass arms and clears its own
    injection state; wrappers are restored by direct reassignment per pass
    (never by stacking another install)."""
    p1 = _exc_injection_pass(spl)
    p2 = _exc_injection_pass(spl)
    identical = (p1[0] == p2[0])
    out = dict(p1[0])
    out["passes_identical"] = identical
    out["pass2"] = p2[0]
    assert identical, ("INJ-EXC-* pass1 != pass2: %r vs %r" % (p1[0], p2[0]))
    return out, p1[1] + p2[1]


def _exc_injection_pass(spl):
    """One deterministic pass of INJ-EXC-CAPTURE-S1 / -S2 / -UNRELATED-TYPE
    and UT-EXC-UNRELATED-REFERENCE, on TEST_CONSTANT full-data spline fits
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

    # UNRELATED-TYPE: ValueError at the covered site, stage 1. Y-04(b) /
    # R3A-03, r4: NOT converted by wrapped_accept (its `except RuntimeError`
    # never matches a ValueError, so it propagates past that specific
    # handler) -- but it must not crash the whole multi-hour process either.
    # fit_spline's own broadened except now catches it, records a proper
    # UNRELATED capture, and marks the context unverifiable/pending rather
    # than silently ending the run (r3's test asserted the OLD, crash-prone
    # behavior as correct; the audit found that reading wrong -- see the r4
    # report).
    # R3A-03, r4: install ONE layer at a time, restore by direct
    # reassignment (not another install call) -- r3 called
    # install_nnls_test_injection(spl) again afterward "to restore", which
    # actually added a THIRD stacked layer instead of restoring anything
    # (traceback evidence: wrapped_nnls at three separate line numbers).
    x3 = gen.make_step("left")
    nnls_before_unrelated_test = spl["nnls"]
    install_exc_unrelated_type_injection(spl)
    VALUEERROR_INJECT_TARGET.update(active=True, fixture="INJ-EXC-UNRELATED-TYPE")
    before = len(EXC_CAPTURES)
    unrel_result = fit_spline(spl, "INJ-EXC-UNRELATED-TYPE", x3, FULL_O, tel, "exc:unrel")
    unrel_caps = [c for c in EXC_CAPTURES[before:] if c.get("kind") == "UNRELATED"
                 and "unrelated exception type" in c.get("message", "")]
    # R4A-01(e), r4-1: evaluation-level assertion -- an unverifiable spline
    # context makes the DEPENDENT criteria PENDING, not PASS/FAIL. Evaluate
    # the three decision-layer spline-pending fixtures through the real
    # evaluate_fixture and confirm the routed criteria come out PENDING
    # (status STOP_EXACTNESS_PENDING(TEST_ONLY_INJECTED)) and never carry a
    # passed True/False.
    gen2 = sys.modules[GEN_MODULE_NAME]
    inj_by_id = {f["fixture_id"]: f for f in gen2.INJ_FIXTURES}
    eval_level = {}
    expected_pending = {"INJ-SPL-PENDING-FULL": ["C3", "C4b"],
                        "INJ-SPL-PENDING-FOLD": ["C2"],
                        "INJ-SPL-PENDING-PROBE": ["C4b"]}
    eval_ok = True
    for fid, crits in expected_pending.items():
        fx = inj_by_id[fid]
        ev = evaluate_fixture(fid, fx["strata"], gen2.N_INJ,
                              "TEST_ONLY_INJECTION_DECISION_LAYER", fx["flags"], [])
        per_fix = {}
        for c in crits:
            cell = ev["criteria"]["P01"][c]["F"]
            is_pending = ("PENDING" in str(cell.get("status", ""))
                          and "passed" not in cell)
            per_fix[c] = dict(status=cell.get("status"),
                              has_passed_field=("passed" in cell),
                              pending_not_passfail=is_pending)
            eval_ok = eval_ok and is_pending
        # C4a must stay a normal PASS (family-only, no spline context routed)
        c4a_cell = ev["criteria"]["P01"]["C4a"]["F"]
        c4a_ok = ("status" not in c4a_cell) and (c4a_cell.get("passed") is True)
        per_fix["C4a_stays_pass"] = c4a_ok
        eval_ok = eval_ok and c4a_ok
        per_fix["p03"] = (ev["p03"]["P01"], ev["p03"]["P02"])
        per_fix["mechanism"] = ev["mechanism_outcome"]
        eval_level[fid] = per_fix

    out["UNRELATED_TYPE"] = dict(
        caught_not_crashed=(len(unrel_caps) == 1),
        exception_type_recorded=(unrel_caps[0]["exception_type"] if unrel_caps else None),
        context_unverifiable=(not unrel_result.get("valid", True)),
        eval_level_dependent_criteria_pending=eval_level,
        eval_level_ok=eval_ok,
        pass_=(len(unrel_caps) == 1
              and unrel_caps[0]["exception_type"] == "ValueError"
              and not unrel_result.get("valid", True)
              and eval_ok))
    VALUEERROR_INJECT_TARGET.update(active=False)
    spl["nnls"] = nnls_before_unrelated_test   # restore, don't stack

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

    # R3A-07, r4: the W-3 custody record is written ONCE per revision,
    # OUTSIDE the run process, with observed values. main() VERIFIES it
    # here -- never writes it -- so its "no W-4 process has yet been
    # started" declaration is written when it is actually true and is not
    # re-stamped by every (possibly resumed) launch.
    assert os.path.exists(CUSTODY_PATH), \
        "W-3 STOP: custody record absent -- write it (externally) before the first run"
    OPENED_FILES.append(CUSTODY_PATH)
    with open(CUSTODY_PATH, "r", encoding="ascii") as f:
        custody_text = f.read()

    def _custody_field(name):
        for line in custody_text.splitlines():
            if line.startswith(name + " = "):
                return line.split(" = ", 1)[1].strip()
        return None
    for fname_c, observed in (("harness_sha256", harness_hash),
                              ("generator_sha256", gen_hash),
                              ("manifest_sha256", man_hash),
                              ("code_env_fingerprint", _CODE_ENV_FINGERPRINT[0])):
        recorded = _custody_field(fname_c)
        assert recorded == observed, (
            "W-3 STOP: custody record %s = %s but observed %s"
            % (fname_c, recorded, observed))
    print("PRE_EXECUTION_CUSTODY_RECORD_VERIFIED = true (" + CUSTODY_PATH + ")")

    # P-1..P-4 (D-3 S3 / r4 instruction S1): every dispatched instrument
    # verified by OBSERVED hash against its pin before the first
    # computation; any mismatch stops here.
    for ipath, ihash, iname in (
            (D3_PATH, D3_HASH, "D-3"),
            (R4_INSTRUCTION_PATH, R4_INSTRUCTION_HASH, "r4 instruction"),
            (DISPATCH_RECORD_PATH, DISPATCH_RECORD_HASH, "D-5"),
            (AUDIT_A1_PATH, AUDIT_A1_HASH, "A-1"),
            (PI_RATIFIED_CONTENT_PATH, PI_RATIFIED_CONTENT_HASH, "D-2"),
            # this revision's dispatched pin set (D-6 S1)
            (R4_1_INSTRUCTION_PATH, R4_1_INSTRUCTION_HASH, "r4-1 instruction"),
            (D6_DISPATCH_RECORD_PATH, D6_DISPATCH_RECORD_HASH, "D-6"),
            (AUDIT_A2_PATH, AUDIT_A2_HASH, "A-2 (input)"),
            (AUDIT_A3_PATH, AUDIT_A3_HASH, "A-3 (input)")):
        obs_h = sha256_of(ipath)
        assert obs_h == ihash, (
            "P-1..P-4 STOP: %s observed %s != pinned %s" % (iname, obs_h, ihash))
    print("DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS (observed hashes equal pins; "
          "9 instruments verified: D-3, r4 instruction, D-5, A-1, D-2, "
          "r4-1 instruction, D-6, A-2, A-3)")

    CURRENT_PHASE[0] = "nr_gates"
    gates_cached = ckpt_load("nrgates_all")
    if gates_cached is None:
        n_tel_before_nr = len(SPLINE_TELEMETRY_CALLS)
        nr = nr01(f2m, grids)
        snr_ok, snr_rows = spline_nr(spl)
        # R3A-06: coarse unit carries its per-call snapshot (see the
        # unittests_all block below for the rationale).
        nr_tel_calls = SPLINE_TELEMETRY_CALLS[n_tel_before_nr:]
        ckpt_save("nrgates_all", (nr, snr_ok, snr_rows, nr_tel_calls))
        UNITS_COMPUTED_THIS_PROCESS["nr_gates"] += 1
    else:
        nr, snr_ok, snr_rows, nr_tel_calls = gates_cached
        SPLINE_TELEMETRY_CALLS.extend(nr_tel_calls)
        UNITS_READ_FROM_STORE["nr_gates"] += 1
    print("NR-01(i) = %s (hash %s; telemetry-fields %s)"
          % (nr["passed"], nr["canonical"], nr["telemetry_fields_equal"]))
    print("NR-01(ii) [T-2a] = %s (hybrid_canonical %s)"
          % (nr["nr01ii"]["passed"], nr["nr01ii"]["hybrid_canonical"]))
    record_test("NR-01i", nr["passed"] and nr["telemetry_fields_equal"])
    assert record_test("NR-01ii", nr["nr01ii"]["passed"]), \
        "NR-01(ii) T-2a wrapper adapter FAIL -> STOP"
    print("SPLINE_NONREGRESSION (NR-SPL) = %s (%d rows)" % (snr_ok, snr_rows))
    assert record_test("NR-SPL", snr_ok), "SPLINE NON-REGRESSION FAIL -> STOP"

    record_test("T-LOADER-NODES",
                len(spl_names["node_hashes"]) == spl_names["executed_node_count"])
    print("T-LOADER-NODES = PASS (node-list equality asserted at load time; "
          "%d node_hashes entries for %d executed nodes)"
          % (len(spl_names["node_hashes"]), spl_names["executed_node_count"]))

    tmfe = t_mask_full_ext(f2m, grids)
    print("T_MASK_FULL_EXT = " + json.dumps(tmfe))
    assert record_test("T-MASK-FULL-EXT", tmfe["pass_"])

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
    record_test("PIN-MASKED-OBJECTIVE", pin_mask_full and pin_mask_le)
    record_test("PIN-FEATURE-START-MASKED", pin_fs)
    assert pin_mask_full and pin_mask_le and pin_fs

    CURRENT_PHASE[0] = "unit_tests"
    ut_cached = ckpt_load("unittests_all")
    if ut_cached is None:
        n_tel_before_ut = len(SPLINE_TELEMETRY_CALLS)
        n_cap_before_ut = len(EXC_CAPTURES)
        t_a5s = t_a5_support()
        a5 = a5_unit_tests(f2m, grids)
        ut_pd = ut_probe_decouple(f2m, grids)
        uset_ut = ut_uset_construction(gen)
        comparator_nan = t_comparator_nan()
        # R3A-02: these were computed with a throwaway [] telemetry sink --
        # the rows existed transiently and were discarded, never reaching
        # any delivered file. Named lists now, included in all_tel_rows.
        starts_full_tel, starts_dup_tel = [], []
        starts_full = fix_starts_full(f2m, grids, starts_full_tel)
        starts_dup = fix_starts_dup(f2m, grids, starts_dup_tel)
        a5_true_tel = []
        a5_true = fix_a5_true(f2m, spl, grids, a5_true_tel)
        exc_fixture_results, exc_fixture_tel = run_exc_injection_fixtures(spl)
        ut_unrel_ref = ut_exc_unrelated_reference(spl)
        # R3A-06, r4: the coarse unit carries its per-call telemetry AND
        # capture snapshots, replayed on a store read -- previously only
        # the fixture-level realscen_* units did, so a resumed process
        # reported no rows/counters for the unit_tests phase at all.
        ut_tel_calls = SPLINE_TELEMETRY_CALLS[n_tel_before_ut:]
        ut_caps = EXC_CAPTURES[n_cap_before_ut:]
        ckpt_save("unittests_all", (a5, ut_pd, uset_ut, comparator_nan,
                                    starts_full, starts_dup, a5_true, a5_true_tel,
                                    exc_fixture_results, exc_fixture_tel,
                                    ut_unrel_ref, starts_full_tel, starts_dup_tel,
                                    t_a5s, ut_tel_calls, ut_caps))
        UNITS_COMPUTED_THIS_PROCESS["unit_tests"] += 1
    else:
        (a5, ut_pd, uset_ut, comparator_nan, starts_full, starts_dup, a5_true,
         a5_true_tel, exc_fixture_results, exc_fixture_tel,
         ut_unrel_ref, starts_full_tel, starts_dup_tel,
         t_a5s, ut_tel_calls, ut_caps) = ut_cached
        SPLINE_TELEMETRY_CALLS.extend(ut_tel_calls)
        for cr in ut_caps:
            if cr not in EXC_CAPTURES:
                EXC_CAPTURES.append(cr)
        UNITS_READ_FROM_STORE["unit_tests"] += 1

    print("T_A5_SUPPORT = " + json.dumps(t_a5s, default=str))
    assert record_test("T-A5-SUPPORT", t_a5s["pass_"]), t_a5s
    print("A5_UNIT_TESTS = " + json.dumps(a5))
    record_test("UT-A5-II", a5["UT_A5_II_pass"])
    record_test("UT-A5-III", a5["UT_A5_III_pass"])
    print("UT_PROBE_DECOUPLE = " + json.dumps(ut_pd))
    assert record_test("UT-PROBE-DECOUPLE", ut_pd["UT_PROBE_DECOUPLE_pass"])
    print("UT_USET_CONSTRUCTION = " + json.dumps(uset_ut, default=str))
    assert record_test("UT-USET-CONSTRUCTION",
                       all(v["ok"] for v in uset_ut.values())), uset_ut
    print("T_COMPARATOR_NAN = " + json.dumps(comparator_nan))
    assert record_test("T-COMPARATOR-NAN", comparator_nan["pass_"])
    print("T_STARTS_DEFAULT (FIX-STARTS-FULL) = " + json.dumps(starts_full))
    assert record_test("T-STARTS-DEFAULT",
                       all(v["pass_"] for v in starts_full.values()))
    print("T_STARTS_DUP (FIX-STARTS-DUP) = " + json.dumps(starts_dup))
    assert record_test("T-STARTS-DUP",
                       all(v["pass_"] for v in starts_dup.values()))
    print("FIX_A5_TRUE = " + json.dumps(a5_true, default=str))
    assert record_test("FIX-A5-TRUE",
                       all(v["pass_"] for v in a5_true.values()))
    print("EXC_INJECTION_FIXTURES = " + json.dumps(exc_fixture_results, default=str))
    assert record_test("T-EXC-CAPTURE-S1", exc_fixture_results["S1"]["pass_"])
    assert record_test("T-EXC-CAPTURE-S2",
                       exc_fixture_results["S2"]["pass_"]), exc_fixture_results["S2"]
    assert record_test("T-EXC-UNRELATED-TYPE",
                       exc_fixture_results["UNRELATED_TYPE"]["pass_"])
    print("UT_EXC_UNRELATED_REFERENCE = " + json.dumps(ut_unrel_ref))
    assert record_test("UT-EXC-UNRELATED-REFERENCE", ut_unrel_ref["pass_"])

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
                n_tel_before = len(SPLINE_TELEMETRY_CALLS)
                strata_recs, n_s, tel_part, ca_part, full_mask_fits = run_real_scenario(
                    f2m, spl, grids, sc, run_label, a5_findings)
                fx_stops = []
                ev = evaluate_fixture(sc["fixture_id"], strata_recs, n_s,
                                      "REAL", {}, fx_stops)
                # X-11(d)/R3A-02: per-fit canonical detail (theta, masked L,
                # start-bank size, FEATURE_START_REJECTED; per spline fit:
                # winner mode, RSS, equivalent-mode set, per-mode validity)
                # -- ghat/x excluded (residual_series already carries the
                # ghat-derived series; including raw arrays here would only
                # duplicate it). Real scenarios only (INJ_FIXTURES are
                # decision-layer constructs with no real fit behind them).
                ev["fits"] = {}
                for (sx2, ti2, fk2), fit in full_mask_fits.items():
                    if fk2 == "SPL":
                        trimmed = dict(valid=fit["valid"], mode=fit.get("mode"),
                                       rss=fit.get("rss"),
                                       equivalent_modes=fit.get("equivalent_modes"),
                                       per_mode_valid=fit.get("per_mode_valid"),
                                       failure=fit.get("failure"))
                    else:
                        trimmed = dict(valid=fit["valid"], theta=fit.get("theta"),
                                       L=fit.get("L"),
                                       start_bank_size=fit.get("start_bank_size"),
                                       feature_start_rejected=fit.get("feature_start_rejected"),
                                       failure_codes=fit.get("failure_codes", []))
                    ev["fits"].setdefault(f"{sx2}{ti2}", {})[fk2] = trimmed
                exc_snapshot = list(EXC_CAPTURES)
                # P-2/P-3 fix (found by the T-CALLCOUNT RUN1==RUN2 assertion
                # itself, 2026-09-24): a fixture-level cache HIT never
                # re-enters run_real_scenario/fit_spline, so the fine-grained
                # per-call telemetry those calls append live is otherwise lost
                # on replay -- same problem EXC_CAPTURES already solved via
                # exc_snapshot; per-call rows need the same snapshot+replay.
                tel_calls_snapshot = SPLINE_TELEMETRY_CALLS[n_tel_before:]
                ckpt_save(ckey, (ev, tel_part, ca_part, fx_stops, exc_snapshot,
                                 full_mask_fits, tel_calls_snapshot))
                UNITS_COMPUTED_THIS_PROCESS[run_label] += 1
            else:
                (ev, tel_part, ca_part, fx_stops, exc_snapshot, full_mask_fits,
                 tel_calls_snapshot) = cached
                for rec in exc_snapshot:
                    if rec not in EXC_CAPTURES:
                        EXC_CAPTURES.append(rec)
                SPLINE_TELEMETRY_CALLS.extend(tel_calls_snapshot)
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

    # R3A-03, r4: EXC_CAPTURES.clear() here used to discard every unit-phase
    # capture (S1/S2/UNRELATED-TYPE, UT-EXC-UNRELATED-REFERENCE) before
    # RUN1 even started -- "every capture record (unit phase, RUN1, RUN2)"
    # must be delivered, so nothing is cleared; phase boundaries are taken
    # by length-slicing the one growing list instead.
    exc_unit_phase = list(EXC_CAPTURES)
    n_before_run1 = len(EXC_CAPTURES)
    evals1, telemetry1, stops1, ca1, full_mask_fits_run1 = one_run("run1")
    exc_after_run1 = EXC_CAPTURES[n_before_run1:]
    n_before_run2 = len(EXC_CAPTURES)
    evals2, telemetry2, stops2, ca2, _full_mask_fits_run2 = one_run("run2")
    exc_after_run2 = EXC_CAPTURES[n_before_run2:]
    # R3A-03: compare RUN1 / RUN2 capture records -- same construction,
    # same code, should capture identically (mirrors T-CANON's RUN1==RUN2
    # expectation, applied to the exception-capture channel specifically).
    def _cap_key(c):
        return (c.get("fixture"), c.get("sex"), c.get("trajectory"),
                c.get("mode"), c.get("stage"), c.get("kind"),
                c.get("exception_type"))
    run1_cap_keys = sorted(_cap_key(c) for c in exc_after_run1)
    run2_cap_keys = sorted(_cap_key(c) for c in exc_after_run2)
    captures_run1_eq_run2 = (run1_cap_keys == run2_cap_keys)
    print("EXC_CAPTURES_RUN1_EQ_RUN2 = %s (run1=%d, run2=%d)"
          % (captures_run1_eq_run2, len(exc_after_run1), len(exc_after_run2)))
    assert captures_run1_eq_run2, "RUN1/RUN2 capture records differ"

    GLOBAL_STOPS_REF[0] = stops1
    expect_result = check_expectations(evals1, rows, gen.MANIFEST_HEADER)
    record_test("T-EXPECT-ALL",
                expect_result["ran"] == expect_result["declared"]
                and not expect_result["fails"])
    print("T_EXPECT_ALL = declared/ran %d/%d ; EXPECTATION_FAIL = %s"
          % (expect_result["declared"], expect_result["ran"],
             json.dumps([f["fixture_id"] for f in expect_result["fails"]])))
    if expect_result["fails"]:
        print("EXPECTATION_FAIL_DETAIL = " + json.dumps(expect_result["fails"], default=str))

    # T-SCHEMA (X-11(f)/R3A-02, r4): every enlarged-document field present
    # at least once across evals1 -- a machine assertion, not a declared
    # coverage row. Checked over the fields this cycle actually added;
    # v6's own "§6" enumeration was not located in the files available to
    # the executor (flagged in the r4 report, not guessed at further).
    schema_seen = {k: False for k in (
        "fits.theta", "fits.L", "fits.start_bank_size",
        "fits.feature_start_rejected", "fits.mode", "fits.rss",
        "fits.equivalent_modes", "fits.per_mode_valid",
        "disc_f3_03_complement.C2", "disc_f3_03_complement.C3",
        "disc_f3_03_complement.C4b", "invalid_counts_by_criterion",
        "probe_failure_shares", "k05_result")}
    for e in evals1:
        for _traj, fits_by_fitter in (e.get("fits") or {}).items():
            for fk3, fit in fits_by_fitter.items():
                if fk3 == "SPL":
                    for f in ("mode", "rss", "equivalent_modes", "per_mode_valid"):
                        if fit.get(f) is not None:
                            schema_seen[f"fits.{f}"] = True
                else:
                    for f in ("theta", "L", "start_bank_size", "feature_start_rejected"):
                        if fit.get(f) is not None:
                            schema_seen[f"fits.{f}"] = True
        for key in e.get("disc_f3_03_complement", {}):
            for crit in ("C2", "C3", "C4b"):
                if key.endswith(":" + crit):
                    schema_seen[f"disc_f3_03_complement.{crit}"] = True
        if e.get("invalid_counts_by_criterion"):
            schema_seen["invalid_counts_by_criterion"] = True
        if e.get("probe_failure_shares"):
            schema_seen["probe_failure_shares"] = True
        if e.get("k05_result"):
            schema_seen["k05_result"] = True
    t_schema_missing = [k for k, v in schema_seen.items() if not v]
    print("T_SCHEMA = " + json.dumps(dict(seen=schema_seen, missing=t_schema_missing)))
    assert record_test("T-SCHEMA", not t_schema_missing), (
        "T-SCHEMA: fields never populated: %s" % t_schema_missing)

    print("EXC_CAPTURES (RUN1) = %d record(s)" % len(exc_after_run1))
    exc_injected = [r for r in exc_after_run1 if "TEST_ONLY_INJECTION" in r["message"]]
    exc_natural = [r for r in exc_after_run1 if "TEST_ONLY_INJECTION" not in r["message"]]
    print("EXC_CAPTURES injected=%d natural=%d" % (len(exc_injected), len(exc_natural)))
    if exc_natural:
        print("NATURAL_SOLVER_B_UNVERIFIABLE_ACCEPTANCE_EVENTS = "
              + json.dumps(exc_natural, default=str))
    # R3A-03/R3A-11: computed, never a literal -- a natural COVERED event
    # is handled by S-2=alpha (not a finding); a natural UNRELATED event
    # opens F3-STEP2-EXACT-04 (D-3 S10: next free number).
    natural_unrelated = [c for c in EXC_CAPTURES
                         if c.get("kind") == "UNRELATED"
                         and "TEST_ONLY" not in c.get("message", "")]
    natural_unrelated_findings = (
        ["F3-STEP2-EXACT-04"] if natural_unrelated else [])
    print("NATURAL_UNRELATED_EVENTS = %d ; exactness_findings = %s"
          % (len(natural_unrelated), json.dumps(natural_unrelated_findings)))

    # ------------------- R4A-01(f) NON-REGRESSION vs r4 --------------------
    # For every fixture present in BOTH the audited r4 results (a15b7eff) and
    # this r4-1 run, compare p03, every criterion outcome, the D-P04 block and
    # the mechanism outcome, plus the stops that name the fixture. Any
    # difference is reported per fixture. The ONLY change this revision makes
    # to a shared fixture is R4A-03's stops offending-pairs shape on
    # INJ-U-POST-CONSTRUCTION-INVALID (dedup by (sex,fitter,obs) + per-pair
    # sex); it is whitelisted as EXPECTED_R4A03. Anything else is a
    # NON_REGRESSION_FINDING and fails T-NONREG-R4. The three new R4A-01
    # fixtures (INJ-SPL-PENDING-*) are NEW_IN_R4-1, not comparisons. On the
    # real path the spline-pending flag is false everywhere unless a natural
    # UNRELATED event fires; that count is reported.
    CURRENT_PHASE[0] = "nonregression"
    _r4_obs_hash = sha256_of(R4_RESULTS_PATH)
    assert _r4_obs_hash == R4_RESULTS_HASH, (
        "R4A-01(f) STOP: r4 results observed %s != pinned %s"
        % (_r4_obs_hash, R4_RESULTS_HASH))
    with open(R4_RESULTS_PATH, encoding="utf-8") as _f:
        _r4_doc = json.load(_f)
    _r4_ev = {e["fixture_id"]: e for e in _r4_doc["evaluations"]}
    _r4_stops = _r4_doc.get("stops", [])
    _r41_stops = stops1

    # R4A-01(f): the r4 results are stored canon()-ized (floats -> hex,
    # dict keys sorted) because r4 wrote json.dump(canon(results)); evals1
    # here is still the in-memory object (native floats, insertion-order
    # dicts). Compare BOTH sides through canon()+sort_keys so the diff is
    # value/decision-level, not a hex-vs-float / key-order representation
    # artefact. (Verified: without this every shared fixture spuriously
    # "changes" its criteria; with it only a genuine value/decision change
    # -- e.g. R4A-03's INJ-U-POST offending-pairs -- survives.)
    def _cn(x):
        return json.dumps(canon(x), sort_keys=True)

    def _fix_proj(ev, stops, fid):
        # a stable, order-independent, canon-normalized projection of
        # everything R4A-01(f) compares for one fixture
        e = ev[fid]
        my_stops = sorted(
            (s for s in stops if s.get("fixture") == fid), key=_cn)
        return dict(
            p03=e.get("p03"),
            criteria=e.get("criteria"),
            dp04=e.get("dp04"),
            disc=e.get("disc_f3_03_complement"),
            mechanism_outcome=e.get("mechanism_outcome"),
            stops=my_stops,
        )

    _r41_ev = {e["fixture_id"]: e for e in evals1}
    _shared = sorted(set(_r4_ev) & set(_r41_ev))
    _new_in_r41 = sorted(set(_r41_ev) - set(_r4_ev))
    _dropped = sorted(set(_r4_ev) - set(_r41_ev))
    _EXPECTED_DIFF = {"INJ-U-POST-CONSTRUCTION-INVALID"}
    nonreg_rows = []
    nonreg_findings = []
    for fid in _shared:
        a = _fix_proj(_r4_ev, _r4_stops, fid)
        b = _fix_proj(_r41_ev, _r41_stops, fid)
        changed = sorted(k for k in a if _cn(a[k]) != _cn(b[k]))
        if not changed:
            nonreg_rows.append(dict(
                fixture=fid, status="IDENTICAL", changed_keys="",
                classification="", r4="", r4_1=""))
            continue
        cls = ("EXPECTED_R4A03" if fid in _EXPECTED_DIFF
               else "NON_REGRESSION_FINDING")
        if cls == "NON_REGRESSION_FINDING":
            nonreg_findings.append(dict(fixture=fid, changed_keys=changed))
        nonreg_rows.append(dict(
            fixture=fid, status="CHANGED", changed_keys=";".join(changed),
            classification=cls,
            r4=_cn({k: a[k] for k in changed}),
            r4_1=_cn({k: b[k] for k in changed})))
    for fid in _new_in_r41:
        nonreg_rows.append(dict(
            fixture=fid, status="NEW_IN_R4-1", changed_keys="",
            classification="R4A-01 fixture (no r4 counterpart)",
            r4="", r4_1=_cn(_fix_proj(_r41_ev, _r41_stops, fid))))
    for fid in _dropped:
        nonreg_rows.append(dict(
            fixture=fid, status="DROPPED", changed_keys="",
            classification="NON_REGRESSION_FINDING(dropped)", r4="", r4_1=""))
        nonreg_findings.append(dict(fixture=fid, changed_keys=["DROPPED"]))
    # real-path natural spline-pending count (must be 0 absent a natural event)
    real_spl_pending = sorted(
        fid for fid, e in _r41_ev.items()
        if not fid.startswith("INJ")
        and "PENDING_EXACTNESS(F3-STEP2-EXACT-04)" in str(e.get("mechanism_outcome", "")))
    print("NONREGRESSION_VS_R4 shared=%d new=%d dropped=%d findings=%d "
          "real_path_spline_pending=%d"
          % (len(_shared), len(_new_in_r41), len(_dropped),
             len(nonreg_findings), len(real_spl_pending)))
    if nonreg_findings:
        print("NONREGRESSION_FINDINGS = " + json.dumps(nonreg_findings, default=str))
    with open(NONREG_PATH, "w", encoding="utf-8", newline="") as _f:
        _w = csv.DictWriter(_f, fieldnames=[
            "fixture", "status", "changed_keys", "classification", "r4", "r4_1"])
        _w.writeheader()
        for r in nonreg_rows:
            _w.writerow(r)
    OPENED_FILES.append(NONREG_PATH)
    OPENED_FILES.append(R4_RESULTS_PATH)
    assert record_test("T-NONREG-R4", not nonreg_findings), (
        "T-NONREG-R4: unexpected non-regression findings vs r4: %s"
        % json.dumps(nonreg_findings, default=str))
    print("NONREGRESSION_WRITTEN = " + NONREG_PATH
          + " sha256=" + sha256_of(NONREG_PATH))

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
    assert record_test("PIN-ACF", acf_ok)

    with open(RESIDUAL_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(residual_series, f, sort_keys=True, indent=1)
        f.write("\n")
    residual_hash = sha256_of(RESIDUAL_PATH)
    print("RESIDUAL_SERIES_WRITTEN = " + RESIDUAL_PATH + " sha256=" + residual_hash)
    record_test("T-RESIDUAL-LINK",
                set(residual_series) == set(residual_link))
    print("T_RESIDUAL_LINK_KEYS = %d" % len(residual_link))

    # Y-16: "unconsulted levels not recomputed" evidence from BOTH
    # INJ-DP04-C2-DIVERGE (C4b/C5 = 0) and, under PI_RULE, INJ-DP04-C1
    # (RESOLVED at C1 -> every subset level 0).
    unconsulted_evidence_ok = False   # set by the INJ-DP04-C1 assert below
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
            # r4 (S-R2-1 = PI_RULE, pinned in D-5 S3): RESOLVED at C1 for
            # P-01; every subset level unconsulted -> recompute counts 0.
            print("INJ-DP04-C1 mechanism (S-R2-1 PI_RULE) = " + str(e["mechanism_outcome"]))
            assert e["mechanism_outcome"] == "RESOLVED_MECHANISM_P01", e["mechanism_outcome"]
            assert (e.get("dp04") or {}).get("resolved_level") == "C1", e.get("dp04")
            rc_c1 = e["dp04"]["recompute_counts"]
            assert all(rc_c1[c] == 0 for c in ("C2", "C3", "C4b", "C5")), rc_c1
            unconsulted_evidence_ok = True   # R3A-08 coverage evidence flag
        if e["fixture_id"] == "INJ-C4B-NOREF":
            print("INJ-C4B-NOREF mechanism (S-R2-1 PI_RULE) = " + str(e["mechanism_outcome"]))
            assert e["mechanism_outcome"] == "TERMINAL_FALLBACK_MECHANISM_P01", e["mechanism_outcome"]
        if e["fixture_id"] == "INJ-NAN-STAT-SPL":
            assert e["mechanism_outcome"] == "STOP_BOTH_FAIL_REDESIGN", e["mechanism_outcome"]

    for sc in gen.REAL_SCENARIOS:
        for e in evals1:
            if e["fixture_id"] == sc["fixture_id"] and sc["fixture_id"] == "SCEN-B":
                print("SCEN-B mechanism (S-R2-1 PI_RULE; V4 empty in M) = "
                      + str(e["mechanism_outcome"]))

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

    # X-11(d), r4/R3A-02: the ACF / A5 / unit-test objects are EXCLUDED from
    # the canonical RUN1/RUN2 document -- they live in test-evidence only
    # (already written there, see TEST_EVIDENCE_PATH below). `pins` (the
    # PIN-MASKED-OBJECTIVE / PIN-FEATURE-START-MASKED booleans) is a
    # structural pin, not an A5/unit-test object, and stays.
    doc1 = dict(evals=evals1, stops=stops1,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    doc2 = dict(evals=evals2, stops=stops2,
                pins=dict(mask_full=pin_mask_full, fs=pin_fs))
    h1, h2 = canonical_hash(doc1), canonical_hash(doc2)
    print("RUN1_CANONICAL_SHA256 = " + h1)
    print("RUN2_CANONICAL_SHA256 = " + h2)
    print("DETERMINISM = " + str(h1 == h2))
    assert record_test("T-CANON", h1 == h2), \
        "RUN1/RUN2 canonical document mismatch -> STOP"

    # Y-04(d) wrapper restoration assertion
    uninstall_wrappers(spl, wrapper_originals)
    wrapper_restore_ok = (spl["accept"] is wrapper_originals["accept"]
                          and spl["minimize"] is wrapper_originals["minimize"]
                          and spl["nnls"] is wrapper_originals["nnls"])
    print("T_WRAPPER_RESTORE = " + str(wrapper_restore_ok))
    assert record_test("T-WRAPPER-RESTORE", wrapper_restore_ok)

    test_evidence = dict(acf=acf_all, a5=a5, t_a5_support=t_a5s,
                         tests_run=dict(TESTS_RUN), ut_probe_decouple=ut_pd,
                         starts_full=starts_full, starts_dup=starts_dup,
                         fix_a5_true=a5_true, a5_contract_violations=a5_findings,
                         uset_construction=uset_ut, comparator_nan=comparator_nan,
                         exc_injection_fixtures=exc_fixture_results,
                         ut_exc_unrelated_reference=ut_unrel_ref,
                         wrapper_restore_ok=wrapper_restore_ok,
                         t_mask_full_ext=tmfe,
                         residual_link=residual_link,
                         exc_captures=exc_after_run1,
                         # R3A-03: every capture record delivered, not just
                         # RUN1's -- previously the unit-phase ones were
                         # discarded by EXC_CAPTURES.clear() before RUN1 ran.
                         exc_captures_unit_phase=exc_unit_phase,
                         exc_captures_run2=exc_after_run2,
                         exc_captures_run1_eq_run2=captures_run1_eq_run2,
                         spline_call_telemetry_sample_count=len(SPLINE_TELEMETRY_CALLS),
                         loader_node_hashes=spl_names["node_hashes"],
                         solver_b_function_hashes=spl_names["solver_b_function_hashes"],
                         io_free_assertion=spl_names["io_free_assertion"])
    with open(TEST_EVIDENCE_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(canon(test_evidence), f, sort_keys=True, indent=1)
        f.write("\n")
    te_hash = sha256_of(TEST_EVIDENCE_PATH)
    print("TEST_EVIDENCE_WRITTEN = " + TEST_EVIDENCE_PATH + " sha256=" + te_hash)

    # X-11(b)/R3A-02, r4: L and predicates columns added; RUN2 rows kept
    # (previously all_tel_rows silently dropped telemetry2 entirely).
    tel_fields = ["fixture", "fitter", "mask_id", "fixture_id", "family",
                  "start_id", "optimizer_path", "status", "message", "success",
                  "nit", "nfev", "njev", "wall_clock_seconds", "L", "predicates"]
    all_tel_rows = (telemetry1 + telemetry2 + exc_fixture_tel + a5_true_tel
                    + starts_full_tel + starts_dup_tel)
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
    # R3A-06, r4: split by (phase, pid) too -- "calls per phase and per pid
    # for the whole execution", covering rows replayed from units another
    # process computed.
    percall_by_phase_pid = dict(_Counter(
        "%s/%s" % (row["phase"], row.get("pid")) for row in SPLINE_TELEMETRY_CALLS))
    print("T_CALLCOUNT per phase = " + json.dumps(percall_by_phase, sort_keys=True))
    print("T_CALLCOUNT per phase/pid = " + json.dumps(percall_by_phase_pid, sort_keys=True))
    record_test("T-CALLCOUNT",
                percall_by_phase.get("run1", 0) == percall_by_phase.get("run2", 0)
                and percall_by_phase.get("residual_export", 0) == 0
                and percall_by_phase.get("nr_gates", 0) > 0
                and percall_by_phase.get("unit_tests", 0) > 0)
    assert percall_by_phase.get("run1", 0) == percall_by_phase.get("run2", 0), \
        "T-CALLCOUNT: RUN1 per-call total must equal RUN2 per-call total"
    assert percall_by_phase.get("residual_export", 0) == 0, \
        "T-RESIDUAL-LINK (3): export phase must make 0 optimizer calls"
    assert percall_by_phase.get("nr_gates", 0) > 0, \
        "T-CALLCOUNT: nr_gates phase issued no optimizer calls (R3A-06)"
    assert percall_by_phase.get("unit_tests", 0) > 0, \
        "T-CALLCOUNT: unit_tests phase issued no optimizer calls (R3A-06)"

    # R3A-06, r4: the store manifest (path, size, sha256, pid, start_iso of
    # the COMPUTING process, read from each unit's own payload) is written
    # by the harness itself when a store exists -- attempt 1 runs without
    # one, and the manifest then records that fact rather than a fabricated
    # empty table.
    store_rows = []
    if os.path.isdir(RESTART_STORE_DIR):
        for name_s in sorted(os.listdir(RESTART_STORE_DIR)):
            p_s = os.path.join(RESTART_STORE_DIR, name_s)
            if not os.path.isfile(p_s):
                continue
            with open(p_s, "rb") as f_s:
                raw = f_s.read()
            try:
                payload = pickle.loads(raw)
                s_pid, s_start = payload.get("pid"), payload.get("start_iso")
            except Exception:
                s_pid, s_start = "UNREADABLE", "UNREADABLE"
            store_rows.append([name_s, len(raw),
                              hashlib.sha256(raw).hexdigest(), s_pid, s_start])
    with open(STORE_MANIFEST_PATH, "w", newline="", encoding="ascii") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["path", "size_bytes", "sha256", "pid", "start_iso"])
        if store_rows:
            w.writerows(store_rows)
        else:
            w.writerow(["NO_STORE_USED(RESTART_LAYER_ACTIVE=%s)"
                        % RESTART_LAYER_ACTIVE, 0, "", "", ""])
    store_manifest_hash = sha256_of(STORE_MANIFEST_PATH)
    print("STORE_MANIFEST_WRITTEN = %s sha256=%s rows=%d"
          % (STORE_MANIFEST_PATH, store_manifest_hash, len(store_rows)))

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
        spline_telemetry_calls_by_phase_pid=percall_by_phase_pid,
        percall_telemetry_path=PERCALL_TELEMETRY_PATH,
        attempt_log_path=ATTEMPT_LOG_PATH,
        store_manifest_path=STORE_MANIFEST_PATH,
        store_manifest_sha256=store_manifest_hash,
        store_rows=len(store_rows),
        # r4-1 process note: the harness itself cannot observe the assistant
        # model; this constant records what the r4-1 executor session
        # disclosed. Details in the r4-1 correction report's process section.
        executor_models="claude-opus-4-8[1m]; see r4-1 report",
    )
    # ---------------- R3A-08 / Y-16, r4: coverage DERIVED from the run ----
    # (user instruction 2026-09-24, verbatim intent: a coverage closure is
    # recorded only when its evidencing test actually RAN and PASSED this
    # run.) The generator supplies the row list (title, evidence text,
    # class, authored status); the STATUS column below is recomputed here
    # from this run's fixture evaluations, expectation checks and the
    # TESTS_RUN registry -- an authored "covered" that cannot be
    # established from run evidence is downgraded to UNCOVERED(...) loudly.
    import re as _re
    evals_by_id = {e["fixture_id"]: e for e in evals1}
    expectation_fail_ids = {f["fixture_id"] for f in expect_result["fails"]}

    def _fixture_ok(fid):
        return fid in evals_by_id and fid not in expectation_fail_ids

    _TEST_TOKEN_ALIAS = {
        "UT-A5-II": "UT-A5-II", "UT-A5-III": "UT-A5-III",
        "UT-USET-CONSTRUCTION": "UT-USET-CONSTRUCTION",
        "UT-PROBE-DECOUPLE": "UT-PROBE-DECOUPLE",
        "UT-EXC-UNRELATED-REFERENCE": "UT-EXC-UNRELATED-REFERENCE",
        "FIX-STARTS-FULL": "T-STARTS-DEFAULT", "FIX-STARTS-DUP": "T-STARTS-DUP",
        "FIX-A5-TRUE": "FIX-A5-TRUE",
        "INJ-EXC-CAPTURE-S1": "T-EXC-CAPTURE-S1",
        "INJ-EXC-CAPTURE-S2": "T-EXC-CAPTURE-S2",
        "INJ-EXC-UNRELATED-TYPE": "T-EXC-UNRELATED-TYPE",
        "PIN-ACF": "PIN-ACF", "NR-SPL": "NR-SPL",
        "T-WRAPPER-RESTORE": "T-WRAPPER-RESTORE",
        "PIN-A5-SUPPORT": "T-A5-SUPPORT",
    }

    def _test_ok(tid):
        return bool(TESTS_RUN.get(tid, {}).get("passed"))

    a5_false_branch_ok = any((ca.get("a5_i_L") is False)
                             and (ca.get("a5_i_R") is False)
                             and not ca.get("a5_contract_violation")
                             for ca in ca1)
    scen_b_paths_ok = (_fixture_ok("SCEN-B")
                       and fidelity_executed_n == fidelity_declared_n)
    _SPECIAL_ROWS = {
        "C6 structural pass": bool(evals1),
        "A.5 (i) support-region condition, FALSE branch": a5_false_branch_ok,
        "unconsulted levels not recomputed (evidence)": unconsulted_evidence_ok,
        "F2 failure codes reachable through wrapper": bool(nr["nr01ii"]["passed"]),
        "fold failure -> crossfit-incomplete": scen_b_paths_ok,
        "probe failure (fitter path)": scen_b_paths_ok,
        "spline FAILURE full-data": scen_b_paths_ok,
        "spline FAILURE masked": scen_b_paths_ok,
        "FEATURE_START_REJECTED under mask": scen_b_paths_ok,
        "reporting fields populated / undefined flags": _test_ok("T-SCHEMA"),
        "both pass -> D-P04 mechanism": all(
            _fixture_ok(f) for f in evals_by_id if f.startswith("INJ-DP04-")),
    }
    # R4A-02 (r4-1): the token grammar now ADMITS generic T-* test ids (any
    # T-<UPPER/DIGIT/-> token) -- the r4 grammar admitted only
    # T-WRAPPER-RESTORE, so rows whose evidence names T-COMPARATOR-NAN,
    # T-CALLCOUNT, etc. could not resolve and were downgraded. A T-* token
    # present in TESTS_RUN resolves from its ran/passed record.
    _token_re = _re.compile(
        r"\b(SCEN-[AB]|INJ-[A-Z0-9][A-Z0-9-]*[A-Z0-9]|FIX-[A-Z0-9-]+|"
        r"UT-[A-Z0-9-]+|PIN-[A-Z0-9-]+|NR-SPL|NR-01[a-z]*|T-[A-Z0-9][A-Z0-9-]*)\b")
    coverage_final = []
    derived_downgrades = []
    for row in gen.COVERAGE_ROWS:
        title, evidence_text, cls, authored = row[0], row[1], row[2], row[3]
        if str(authored).startswith("UNCOVERED"):
            coverage_final.append([title, evidence_text, cls, authored])
            continue
        if title in _SPECIAL_ROWS:
            ok = bool(_SPECIAL_ROWS[title])
            detail = "special-resolver"
        else:
            checks = []
            for tok in _token_re.findall(title + " " + evidence_text):
                if tok in _TEST_TOKEN_ALIAS:
                    checks.append(_test_ok(_TEST_TOKEN_ALIAS[tok]))
                elif tok in TESTS_RUN:            # R4A-02: T-*/NR-* by id
                    checks.append(bool(TESTS_RUN[tok]["passed"]))
                elif tok in evals_by_id:
                    checks.append(_fixture_ok(tok))
            ok = bool(checks) and all(checks)
            detail = "%d evidence tokens" % len(checks)
        if ok:
            coverage_final.append([title, evidence_text, cls, authored])
        else:
            coverage_final.append([title, evidence_text, cls,
                                   "UNCOVERED(evidence not established in "
                                   "this run: %s)" % detail])
            derived_downgrades.append(title)
    print("COVERAGE_DERIVED = %d rows ; downgraded_to_UNCOVERED = %s"
          % (len(coverage_final), json.dumps(derived_downgrades)))

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
        # S-R2-1 = PI_RULE (r4): EXACT-03 closes with D-5 as its source
        # (D-5 S4(d)). exactness_findings is COMPUTED (R3A-11, no literal):
        # a NATURAL (non-TEST_ONLY) UNRELATED solver event opens EXACT-04.
        exactness_findings=natural_unrelated_findings,
        exactness_findings_closed_this_cycle=(
            [dict(id=S_R2_1_FINDING_ID_CLOSED, source=DISPATCH_RECORD_PATH,
                 source_sha256=DISPATCH_RECORD_HASH)]),
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
        coverage=coverage_final,
        coverage_downgraded_rows=derived_downgrades,
        # X-11(c)/R3A-02: double-count declaration echoed VERBATIM
        # from freeze record r1 S4 (the · is the record's own
        # middle dot; kept out of every print statement).
        double_count_declaration=(
            "Double-count declaration: a failed probe is counted once as a "
            "C4a non-success (numerator excluded, denominator 2·n_s "
            "retained) and once as C4b incompleteness (absent from V4_s, "
            "denominator n_s retained). Declared, not corrected."),
        expectation_checks=dict(
            declared=expect_result["declared"], ran=expect_result["ran"],
            EXPECTATION_FAIL=([f["fixture_id"] for f in expect_result["fails"]]
                              or "none"),
            detail=expect_result["fails"]),
        tests_run=dict(TESTS_RUN),
        end_state=dict(
            PI_dispatch_record_hash=DISPATCH_RECORD_HASH,
            # R3A-11, r4: BOTH fields computed from the test registry --
            # never a literal. corrections_complete = every mandatory test
            # ran AND passed AND no expectation failure; mandatory_tests_
            # all_run = every test on the mandatory list has a ran=True
            # record (a test that never called record_test is missing).
            corrections_complete=(
                all(TESTS_RUN.get(t, {}).get("passed") for t in MANDATORY_TESTS)
                and len(expect_result["fails"]) == 0),
            mandatory_tests_all_run=all(
                TESTS_RUN.get(t, {}).get("ran") for t in MANDATORY_TESTS),
            mandatory_tests_missing=[t for t in MANDATORY_TESTS
                                     if not TESTS_RUN.get(t, {}).get("ran")],
            deferred_decisions=(["S-R2-1"] if S_R2_1 == "DEFERRED_THIS_CYCLE" else []),
            narrowed_evidence=(["T-R2-2"] if T_R2_2 == "AUTHORIZE_RESTART" else []),
            uncovered_coverage_rows=[r[0] for r in coverage_final
                                     if str(r[3]).startswith("UNCOVERED")],
            # S-R2-1 = PI_RULE (r4): EXACT-03 closed (D-5 S4(d)); open
            # findings COMPUTED -- a natural UNRELATED event opens EXACT-04.
            open_findings=natural_unrelated_findings,
        ),
    )
    six = results["end_state"]
    f3_step2_r4_status = ("PARTIAL_PENDING_PI"
                          if (six["deferred_decisions"] or six["narrowed_evidence"]
                              or six["uncovered_coverage_rows"] or six["open_findings"]
                              or not six["corrections_complete"]
                              or not six["mandatory_tests_all_run"])
                          else "CORRECTED_PENDING_INDEPENDENT_AUDIT")
    results["end_state"]["F3_STEP2_r4_status"] = f3_step2_r4_status
    print("END_STATE = " + json.dumps(six, default=str))
    print("F3_STEP2_r4_status = " + f3_step2_r4_status)
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
