"""Standalone W-3 custody writer for the r4-2 revision (runs OUTSIDE the run
process; the harness only VERIFIES the record it produces).

R41A-02(a): ONE custody file PER ATTEMPT. The attempt number comes from the
harness constant, the file name carries it, and an existing file is NEVER
overwritten -- the writer refuses and stops. From attempt 2 on,
supersedes_custody_sha256 carries the hash of the superseded attempt's record.
Temporary helper; not a deliverable.
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

REPO = "G:/PycharmProjects/pkp-worktree"
os.chdir(REPO)

HARNESS_PATH = "p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py"
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
# R41A-02(c) refinement at attempt 2: LAUNCH_NUMBER is read from the
# environment (F3_R42_LAUNCH) so that resumed launches of one attempt do not
# change the harness bytes / fingerprint. The custody record therefore notes
# the mechanism, not a fixed number.
launch = "env-driven (F3_R42_LAUNCH; first launch of this attempt = 2)"
restart_active = const("RESTART_LAYER_ACTIVE") == "True"
sup_harness = const("SUPERSEDES_HARNESS_SHA256").strip('"')
sup_custody = const("SUPERSEDES_CUSTODY_SHA256").strip('"')
sup_note = const("SUPERSEDES_NOTE_PATH").strip('"')
CUSTODY_PATH = ("p_konum_plus/provenance/"
                "f3_step2_r4-2_preexecution_custody_attempt%d_2026-09-30.md" % attempt)

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
    ("p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md",
     "11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6", "A-1"),
    ("p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md",
     "b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a", "A-2"),
    ("p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md",
     "9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9", "A-3"),
    ("p_konum_plus/prompts/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md",
     "ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82", "A-4"),
    ("p_konum_plus/prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md",
     "17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376", "D-1"),
    ("p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md",
     "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498", "D-2"),
]

harness_h = sha256_of(HARNESS_PATH)
gen_h = sha256_of(GEN_PATH)
man_h = sha256_of(MANIFEST_PATH)

# the manifest is REUSED: regenerate in memory and prove equality here too
spec = importlib.util.spec_from_file_location("gen_r42_w3", GEN_PATH)
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

doc = """# p_konum_plus - F3 STEP-2 r4-2 Pre-Execution Custody Record - attempt {attempt}

```text
artifact_role = pre-execution custody record for ATTEMPT {attempt} of the r4-2 revision
                (deliverable 4; R41A-02(a): one record per attempt, never overwritten)
status        = NON-NORMATIVE
date          = 2026-09-30
written_by    = a standalone W-3 writer OUTSIDE the run process (R3A-07);
                the harness VERIFIES this record at start and never writes it

harness_path = {HARNESS_PATH}
harness_sha256 = {harness_h}

generator_path = {GEN_PATH}
generator_sha256 = {gen_h}
generator_provenance = REUSED UNCHANGED from the r4-1 package (r4-2 instruction section 5
                       item 2); no r4-2 copy exists and none is made

manifest_path = {MANIFEST_PATH}
manifest_sha256 = {man_h}
manifest_provenance = REUSED UNCHANGED from the r4-1 package (section 5 item 3); regenerated
                      in memory from the reused generator by this writer AND by main(),
                      verified equal both times; the file itself is never rewritten
manifest_regenerated_sha256 = {regen_h}

dispatch_preconditions_P1_P4 = every value below is OBSERVED (computed by this
                               writer on the repository files), not a stamped literal
{instr_block}

S1 = (a)
S2 = alpha
T1 = AUTHORIZE
T2 = T-2a
T3 = AUTHORIZE
T4 = T-4a
T5 = CONFIRM_WITHIN_SCOPE
S_R2_1 = PI_RULE (rule text in D-5 section 3, carried unchanged by D-6 and D-7,
         implemented word for word; EXACT-03 closed with D-5 as source per D-5 S4(d))
T_R2_2 = AUTHORIZE_RESTART (as read from D-5, carried unchanged by D-6 and D-7)
PI_dispatch_record_for_this_revision = D-7 (end_state.PI_dispatch_record_hash; R41A-03)

restart_layer_active_at_this_W3 = {restart_active} (r4-2 attempt 1 is ONE process from the
         beginning; a restart layer is introduced only after a recorded interruption of
         THIS revision - D-3 S8.1/S8.2/S8.3. The r4-2 store is its own directory; the r4-1
         and r4 stores stay where they are, untouched and unread.)
code_env_fingerprint = {fp}
environment = python {pyver} ; numpy {npver} ; scipy {scver} ; {plat} ; OMP/OPENBLAS/MKL = 1

attempt_number = {attempt}
launch_number_of_first_launch_under_these_bytes = {launch}
supersedes_harness_sha256 = {sup_harness}
supersedes_custody_sha256 = {sup_custody}
supersedes_note_path = {sup_note}
r4-1_package = historical, read-only (harness 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f,
               results 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385);
               the r4 and r3 packages likewise. Nothing of them is overwritten, renamed or
               moved by the r4-2 revision

declaration = this record is written AFTER the r4-2 harness exists and is hashed, with the
reused generator and manifest named at their delivered hashes, and BEFORE the first test or
run of attempt {attempt}. It names the exact bytes that are then executed. No W-4 process has
yet been started under these three hashes. Because this record is written outside the run
process, a resumed launch does NOT re-stamp it, and because its name carries the attempt
number it is never overwritten by a later attempt.

real_data_access = false
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
