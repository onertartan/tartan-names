"""Standalone W-3 custody writer for the rp1-r1 cycle (runs OUTSIDE the run
process; the harness only VERIFIES the record it produces).

R41A-02(a) (adopted unchanged by D-11 r1 / rp1 instruction S6): ONE custody
file PER ATTEMPT. The attempt number comes from the harness constant, the
file name carries it, and an existing file is NEVER overwritten -- the
writer refuses and stops. R-4 (rp1-r1, RP1A-07): the repo root is
overridable via F3_REPO_ROOT, so an auditor can run this unchanged against
a disposable copy. Temporary helper; not a deliverable.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import csv
import hashlib
import importlib.util
import io
import platform
import re
import sys

import numpy as np
import scipy

REPO = os.environ.get("F3_REPO_ROOT", "G:/PycharmProjects/pkp-worktree")
os.chdir(REPO)

HARNESS_PATH = "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py"
GEN_PATH = "p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py"
MANIFEST_PATH = "p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv"
F2_HASH = "01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077"
SPL_HASH = "b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d"


def sha256_of(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            h.update(b)
    return h.hexdigest()


src = open(HARNESS_PATH, encoding="utf-8").read()


def const(name):
    m = re.search(r"^%s = (.+)$" % name, src, re.M)
    return m.group(1).strip() if m else None


attempt = int(const("ATTEMPT_NUMBER"))
launch = "env-driven (F3_RP1R1_LAUNCH; first launch of this attempt = %d)" % attempt
restart_active = const("RESTART_LAYER_ACTIVE") == "True"
sup_harness = const("SUPERSEDES_HARNESS_SHA256").strip('"')
sup_custody = const("SUPERSEDES_CUSTODY_SHA256").strip('"')
sup_note = const("SUPERSEDES_NOTE_PATH").strip('"')
CUSTODY_PATH = ("p_konum_plus/provenance/"
                "f3_step2_rp1-r1_preexecution_custody_attempt%d_2026-10-05.md" % attempt)

# R41A-02(a): never overwrite a custody record.
if os.path.exists(CUSTODY_PATH):
    print("REFUSE: custody record already exists, not overwriting:", CUSTODY_PATH)
    sys.exit(1)

INSTR = [
    ("p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
     "5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5", "D-3"),
    ("p_konum_plus/prompts/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md",
     "e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387", "r4_instruction"),
    ("p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md",
     "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851", "D-5"),
    ("p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md",
     "283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330", "r4-1_instruction"),
    ("p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md",
     "a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0", "D-6"),
    ("p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md",
     "d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe", "r4-2_instruction"),
    ("p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md",
     "a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb", "D-7"),
    ("p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md",
     "aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae", "D-8"),
    ("p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md",
     "9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575", "A-5"),
    ("p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md",
     "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3", "D-9"),
    ("p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md",
     "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5", "rp1_instruction"),
    ("p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md",
     "4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34", "D-10"),
    ("p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md",
     "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639", "D-11_r1"),
    ("p_konum_plus/provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md",
     "858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9", "rp1_transmission_list"),
    ("p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py",
     "39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09", "rp1_harness"),
    ("p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md",
     "2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d", "rp1-r1_instruction"),
    ("p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md",
     "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364", "D-12"),
    ("p_konum_plus/prompts/f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md",
     "2fa28e2ad8f312bde4ddbf688364bd431ea3843904108494e2bcc4a5f5320989", "rp1_audit"),
    ("p_konum_plus/prompts/RP1-R1_Talimat_Taslagi_Degerlendirmesi_2026-10-05.md",
     "aa9fcaa9dc2cd7f32c6a11714c69771902354d8ae7c6083072a6275e4f97e0ef", "rp1-r1_review"),
    ("p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md",
     "5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0", "F1_freeze_record"),
]

harness_h = sha256_of(HARNESS_PATH)
gen_h = sha256_of(GEN_PATH)
man_h = sha256_of(MANIFEST_PATH)

# the manifest is REUSED: regenerate in memory and prove equality here too
spec = importlib.util.spec_from_file_location("gen_rp1r1_w3", GEN_PATH)
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
buf = io.StringIO()
w = csv.writer(buf, lineterminator="\n")
w.writerow(gen.MANIFEST_HEADER)
w.writerows(gen.manifest_rows())
regen_h = hashlib.sha256(buf.getvalue().encode("ascii")).hexdigest()
assert regen_h == man_h, "manifest regeneration differs: %s != %s" % (regen_h, man_h)

pyver = platform.python_version()
npver = np.__version__
scver = scipy.__version__
plat = platform.platform()
fp = hashlib.sha256("|".join([
    harness_h, gen_h, man_h, F2_HASH, SPL_HASH,
    pyver, npver, scver, plat, "1", "1", "1",
]).encode()).hexdigest()[:16]

lines = []
for path, pin, label in INSTR:
    obs = sha256_of(path)
    lines.append("%s_path = %s" % (label, path))
    lines.append("%s_sha256_observed = %s" % (label, obs))
    lines.append("%s_sha256_pinned = %s" % (label, pin))
    lines.append("%s_values_equal = %s" % (label, "EQUAL" if obs == pin else "MISMATCH"))
    assert obs == pin, "%s MISMATCH: %s != %s" % (label, obs, pin)
instr_block = "\n".join(lines)

doc = """# p_konum_plus - F3 real-data preparation rp1-r1 - Pre-Execution Custody Record - attempt {attempt}

```text
artifact_role = pre-execution custody record for ATTEMPT {attempt} of the rp1-r1
                B-correction cycle (deliverable 4; R41A-02(a) adopted unchanged:
                one record per attempt, never overwritten)
status        = NON-NORMATIVE
date          = 2026-10-05
written_by    = a standalone W-3 writer OUTSIDE the run process (R3A-07);
                the harness VERIFIES this record at start and never writes it

harness_path = {HARNESS_PATH}
harness_sha256 = {harness_h}

generator_path = {GEN_PATH}
generator_sha256 = {gen_h}
generator_provenance = REUSED UNCHANGED from the r4-1 package (rp1 instruction S4,
                       carried unchanged into rp1-r1); no rp1-r1 copy exists

manifest_path = {MANIFEST_PATH}
manifest_sha256 = {man_h}
manifest_provenance = REUSED UNCHANGED from the r4-1 package; regenerated in memory
                      from the reused generator by this writer AND by main(), verified
                      equal both times; the file itself is never rewritten
manifest_regenerated_sha256 = {regen_h}

dispatch_preconditions = every value below is OBSERVED (computed by this
                               writer on the repository files), not a stamped literal
{instr_block}

S1 = (a)
S2 = alpha
T1 = AUTHORIZE
T2 = T-2a
T3 = AUTHORIZE
T4 = T-4a
T5 = CONFIRM_WITHIN_SCOPE
S_R2_1 = PI_RULE (rule text in D-5 section 3, carried unchanged through D-6/D-7/D-10/D-12,
         implemented word for word; EXACT-03 closed with D-5 as source per D-5 S4(d))
T_R2_2 = AUTHORIZE_RESTART (as read from D-5, carried unchanged)
T-RP-1 = ACTIVE_FROM_START (carried from D-10 S2 into rp1-r1: the restart layer is active
         from attempt 1 of THIS cycle too)
PI-a = RP1A-01/02/03 are B (D-11 r1 S5(iii); first B correction of rp1)
PI-b = family is part of every real-mode (fixture_id, mask_id); synthetic-path ids unchanged
PI-c = run_real_scenario changes only where it takes a scenario's trajectory/mask ids
PI-d = RP1A-04 and RP1A-06 close in this package
PI_dispatch_record_for_this_cycle = D-12 (end_state.PI_dispatch_record_hash; D-12 S4)

restart_layer_active_at_this_W3 = {restart_active} (T-RP-1 = ACTIVE_FROM_START, carried
         from the rp1 cycle. Attempt 1 ran the entire computation successfully and
         stopped at T-NONREG-R4-2 on three bugs in the R-3 comparison logic itself
         (COUNT double-canonicalization, an exc_injection_fixtures declaration
         collision, three capture-record fields declared EQUAL instead of
         provenance-stripped); none touched any computation; fixed for this attempt --
         see the attempt-1 supersession note. The rp1-r1 store is its own directory,
         EMPTY at this attempt's first launch. The rp1/r4-2/r4-1/r4 stores stay where
         they are, untouched and unread.)
code_env_fingerprint = {fp}
environment = python {pyver} ; numpy {npver} ; scipy {scver} ; {plat} ; OMP/OPENBLAS/MKL = 1

attempt_number = {attempt}
launch_number_of_first_launch_under_these_bytes = {launch}
supersedes_harness_sha256 = {sup_harness}
supersedes_custody_sha256 = {sup_custody}
supersedes_note_path = {sup_note}
rp1_package = historical, read-only (harness 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09,
              transmission list 858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9);
              the r4-2, r4-1, r4 and r3 packages likewise. Nothing of them is overwritten,
              renamed or moved by the rp1-r1 cycle
real_data_access = false ; REAL_DATA_MODE (harness switch) = False in every rp1-r1 launch
F3_REPO_ROOT = {REPO} (this writer's and this attempt's repo root; R-4/RP1A-07 -- an
               auditor may override this environment variable to run against a
               disposable copy, with the unchanged harness)

declaration = this record is written AFTER the rp1-r1 harness exists and is hashed, with
the reused generator and manifest named at their delivered hashes, and BEFORE the first
test or run of attempt {attempt}. It names the exact bytes that are then executed. No W-4
process has yet been started under these three hashes. Because this record is written
outside the run process, a resumed launch does NOT re-stamp it, and because its name
carries the attempt number it is never overwritten by a later attempt.

commit = false
```
""".format(**dict(globals(), **locals()))

with open(CUSTODY_PATH, "w", encoding="ascii", newline="\n") as f:
    f.write(doc)

print("W3_WRITTEN =", CUSTODY_PATH)
print("attempt =", attempt, "; launch =", launch, "; restart_layer =", restart_active)
print("harness_sha256 =", harness_h)
print("generator_sha256 =", gen_h, "(reused)")
print("manifest_sha256 =", man_h, "(reused; regen equal)")
print("code_env_fingerprint =", fp)
print("custody_sha256 =", sha256_of(CUSTODY_PATH))
