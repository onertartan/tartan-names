# F3 rp1-r2 independent audit — DRAFT r1

## Identity and prior exposure


```json
{
  "utc": "2026-10-12T17:32:14.429683+00:00",
  "model": "GPT-6 / Codex (developer identity)",
  "provider_session_id": "NOT OBSERVED",
  "directory": "G:\\PycharmProjects\\rp1r2_audit",
  "prior_exposure": "This session previously verified these two clones only; no executor, drafter or rp1-r1 auditor work in this session.",
  "clone_creation": "PI creation is user-reported; clone/checkout commands were not run by this auditor."
}
```

This report distinguishes [A] delivered-byte checks, [A-S] commands executed by this auditor, and [X] unverified executor or third-party claims. Quantities below are generated from the evidence JSON by `audit_support/stop_report.py`.

## Verdict

**NOT PASSED — AUDIT STOPPED / INCOMPLETE.** The auditor search exceeded the permitted reading scope. This session cannot certify the required firewall discipline. This is an auditor-caused incident, not a finding that rp1-r2 computed an incorrect result or accessed real data. No package pass, binding, qualification or closure is declared. The unperformed auditor run alone leaves the section 8 pass criterion unestablished.

STOP was reported to the PI in the current conversation. No new package B is established and no third correction cycle is proposed as decided.

## Custody (section 1)

[A-S] Instruction intake: computed file hash, sidecar hash token and PI-forwarded value agree; the sidecar filename was also checked before reading the instruction.


```json
{
  "instruction": "C:\\Users\\Neo\\Downloads\\F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md",
  "instruction_sha256": "25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2",
  "sidecar_text": "25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2  F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md\n",
  "user_expected_sha256": "25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2"
}
```

[A-S] Initial clone verification commands and complete outputs:


```json
{
  "ref": [
    {
      "command": [
        "git",
        "-C",
        "G:\\PycharmProjects\\rp1r2_audit\\ref",
        "rev-parse",
        "HEAD"
      ],
      "returncode": 0,
      "stdout": "25c7d51a0d14e8935f464a7a52d6a49ef4383e2b\n",
      "stderr": ""
    },
    {
      "command": [
        "git",
        "-C",
        "G:\\PycharmProjects\\rp1r2_audit\\ref",
        "status"
      ],
      "returncode": 0,
      "stdout": "HEAD detached at 25c7d51\nnothing to commit, working tree clean\n",
      "stderr": ""
    },
    {
      "command": [
        "git",
        "-C",
        "G:\\PycharmProjects\\rp1r2_audit\\ref",
        "status",
        "--porcelain=v1",
        "--untracked-files=all"
      ],
      "returncode": 0,
      "stdout": "",
      "stderr": ""
    }
  ],
  "run": [
    {
      "command": [
        "git",
        "-C",
        "G:\\PycharmProjects\\rp1r2_audit\\run",
        "rev-parse",
        "HEAD"
      ],
      "returncode": 0,
      "stdout": "25c7d51a0d14e8935f464a7a52d6a49ef4383e2b\n",
      "stderr": ""
    },
    {
      "command": [
        "git",
        "-C",
        "G:\\PycharmProjects\\rp1r2_audit\\run",
        "status"
      ],
      "returncode": 0,
      "stdout": "HEAD detached at 25c7d51\nnothing to commit, working tree clean\n",
      "stderr": ""
    },
    {
      "command": [
        "git",
        "-C",
        "G:\\PycharmProjects\\rp1r2_audit\\run",
        "status",
        "--porcelain=v1",
        "--untracked-files=all"
      ],
      "returncode": 0,
      "stdout": "",
      "stderr": ""
    }
  ]
}
```

[A] The transmission list payload sizes, SHA256, sidecar content/name and sidecar SHA256 were checked on each row. The list and its sidecar exactly cover the commit-added set with no modification or deletion.


```json
{
  "utc": "2026-10-12T17:32:31.724032+00:00",
  "transmission_rows": 2298,
  "failures": [],
  "own_sidecar_ok": true,
  "diff_command": [
    "git",
    "-C",
    "G:\\PycharmProjects\\rp1r2_audit\\ref",
    "diff",
    "--name-status",
    "d9a5e99",
    "25c7d51"
  ],
  "added_count": 4598,
  "change_statuses": [
    "A"
  ],
  "outside_package": [],
  "missing_from_list": [],
  "extra_in_list": [],
  "duplicate_list_paths": 0
}
```

[A] Full file/hash pairs extracted from the forwarded instruction were checked against the specifically named files:


```json
[
  {
    "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R2_INSTRUCTION_DRAFT_r1_2026-10-10.md",
    "expected": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5",
    "observed": "bf53e1e91a0a8b8a4a02bf9ef20467e1f917adce92a97d4d4037a6b5097333a5",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_pi_dispatch_record_2026-10-10.md",
    "expected": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f",
    "observed": "6b9ae30e301eba089364edff41ddf26096f054a4d8c49fedb2ad15bd3245638f",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r2_IR1-13_pi_decision_record_2026-10-10.md",
    "expected": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "observed": "a0ec71cb5214ac2319cb749d24888c456e697bc3fcbf3dd130907e20045418c7",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md",
    "expected": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
    "observed": "0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md",
    "expected": "4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955",
    "observed": "4d43682fc5ee2fe88a55d0fcf6bde3af9659192072322162eca5e2bbee0c9955",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md",
    "expected": "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3",
    "observed": "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_pi_dispatch_record_2026-10-05.md",
    "expected": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364",
    "observed": "2c23130dfed76b02f50c24de0319ab39e296d47fc74cb46b8ad0c88dc6434364",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md",
    "expected": "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5",
    "observed": "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1-R1_INSTRUCTION_DRAFT_r2_2026-10-05.md",
    "expected": "2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d",
    "observed": "2226fc9622989c5fff6d1eab0d36b7d0e5370c8f2d686930d67ab52f64a0980d",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/f3_realdata_prep_rp1-r1_independent_audit_gpt-6_codex_DRAFT_r1_2026-10-10.md",
    "expected": "f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913",
    "observed": "f3a6f369b8d2a5d1dacd6945c00e28b2beeaa59fefbdea8cb6298b9574cdc913",
    "ok": true
  },
  {
    "path": "p_konum_plus/prompts/F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md",
    "expected": "82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e",
    "observed": "82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e",
    "ok": true
  },
  {
    "path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md",
    "expected": "98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956",
    "observed": "98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956",
    "ok": true
  },
  {
    "path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv",
    "expected": "e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75",
    "observed": "e48f5f6ba139eabbf52109556886c8f4d8c67f92e3c6155846800407e4ec3c75",
    "ok": true
  },
  {
    "path": "p_konum_plus/provenance/f3_realdata_prep_rp1-r2_auditor_rerun_procedure_2026-10-12.md",
    "expected": "f745aaba857135c6315b41151607318f6dddd50533dd956dd9c513f7b6bc9fff",
    "observed": "f745aaba857135c6315b41151607318f6dddd50533dd956dd9c513f7b6bc9fff",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
    "expected": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
    "observed": "4d2e3db00bf1742458107c09e2f78a6ce8dc22a206a9a1209547c3ba942b3d1d",
    "ok": true
  },
  {
    "path": "p_konum_plus/provenance/f3_rp1-r2_attempt2_before_provenance_patch_2026-10-11/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
    "expected": "d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3",
    "observed": "d34676d0e60c6a2a160a8b7c9180d37409b244ed5e5a1b1d50073b18051c5bb3",
    "ok": true
  },
  {
    "path": "p_konum_plus/quarantine/f3_step2_rp1-r2_attempt1_2026-10-11/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
    "expected": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
    "observed": "92181f38c736e4bad48e87b879dcb8a8ffc5981c9a77ce6c4144d6e23fc8494c",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r1_2026-10-05.py",
    "expected": "cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb",
    "observed": "cac93ac632ff188493e5b2416580b21f36916ca8735c2366403f320da91688eb",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py",
    "expected": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "observed": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv",
    "expected": "5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe",
    "observed": "5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json",
    "expected": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
    "observed": "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_results_rp1-r2_2026-10-10.json",
    "expected": "81e1b523cc41561edabbea9098696646355b811d4b1ce86493bf10fae7e63818",
    "observed": "81e1b523cc41561edabbea9098696646355b811d4b1ce86493bf10fae7e63818",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_residual_series_rp1-r2_2026-10-10.json",
    "expected": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f",
    "observed": "3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_rp1-r2_attempt2_launch1_stderr_2026-10-10.log",
    "expected": "afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b",
    "observed": "afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b",
    "ok": true
  },
  {
    "path": "p_konum_plus/calibration/f3_step2_rp1-r1_launch2_stderr_2026-10-05.log",
    "expected": "afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b",
    "observed": "afc4a0410a2e16d0a52243194c5da267f79f76e5ad72079e9f9234ae0b38f58b",
    "ok": true
  }
]
```

These checks do not establish the contents of undelivered restart stores, every executor-written value, fixture correspondence, prior-package transmission integrity or scientific correctness. Those checks were not completed. The intake evidence cited by D-14 remains [X]; its repository absence was not independently checked before STOP.

## Code (section 2)

[A] The final harness dependency dictionary was parsed with AST without importing or executing the harness. Each named dependency equals its pin:


```json
[
  {
    "path": "p_konum_plus\\calibration\\f3_rp1-r2_gate_tools_2026-10-10.py",
    "expected": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7",
    "observed": "ca7233e7aec291fbc160bd581c56733fbf615b1cb72a1de8bc94ab89799589a7"
  },
  {
    "path": "p_konum_plus\\calibration\\f3_rp1-r2_reproduction_fixture_generator_2026-10-10.py",
    "expected": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8",
    "observed": "eaeabaaeb922a7f6cfb8573075129a56e98dc1ceddcee3c5a24a85bef5ed0de8"
  },
  {
    "path": "p_konum_plus\\calibration\\f3_rp1-r2_technical_tests_2026-10-10.py",
    "expected": "cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b",
    "observed": "cd44ea6edfa8601aefb4d3d234a44967b13bd2f3e16cc733aea61ed87439e96b"
  }
]
```

NOT PERFORMED: full real-data-path binding file inventory; W-3/end-record cross-checks; both independent harness diffs and label judgments; attempt-change judgments for each declaration; E-declaration scope review. Partial source reading is not reported as a completed code audit.

## Re-execution and environment (section 3)

[A-S] Local interpreter/library/platform observation:


```json
{
  "python": "3.11.7",
  "numpy": "1.26.4",
  "scipy": "1.14.1",
  "platform": "Windows-10-10.0.19045-SP0",
  "interpreter": "C:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
}
```

| Field | Instruction binding value (claim until binding record checked) | Local observation | Comparison |
|---|---|---|---|

| python | 3.11.7 | 3.11.7 | equal |

| numpy | 1.26.4 | 1.26.4 | equal |

| scipy | 1.14.1 | 1.14.1 | equal |

| platform | Windows-10-10.0.19045-SP0 | Windows-10-10.0.19045-SP0 | equal |

| OMP_NUM_THREADS | 1 | unset in the environment observation | not configured for a run |

| OPENBLAS_NUM_THREADS | 1 | unset in the environment observation | not configured for a run |

| MKL_NUM_THREADS | 1 | unset in the environment observation | not configured for a run |

The thread values come from the full tool output of the environment command below, not from a launched harness. No W-3 writer, launcher or harness was invoked. No launch records were moved aside; no delivered output was overwritten; no restart store was created by this auditor. Re-execution stopped before preparation because of AUDITOR-SCOPE-01.

## Non-regression and accounting (section 4)

NOT PERFORMED: scientific S/canonical/residual comparison, non-regression leaf checks, independent plan/family/mode/store accounting, fallback analysis, timing reconciliation, the prelaunch-to-final ledger transition table and size-estimate arithmetic. Executor and drafting-session counts are not adopted as audit evidence.

## Items (section 5)

NOT PERFORMED: Q1–Q11 semantic review and independent probes; fixture hash disjointness and synthetic construction; launch firewall review; IR1-13 ledger review; section 5(b) invocation/output isolation; record/errata trace; requirement-map agreement. No mandatory test or negative-case pass is certified.

## Ledger (section 6)

No item is closed by this report. No repository ledger was written. The instruction requires IR1-13 to remain OPEN / B under D-14; that PI decision is not reopened. Final-ledger statuses, prior-auditor closures and closure-point discrepancies were NOT PERFORMED and must be checked by the next valid audit.

## Findings table

| ID | v6 | D-11 r1 | Location and evidence | Closure action |
|---|---|---|---|---|

| AUDITOR-SCOPE-01 [A-S] | global blocker for this audit session | STOP for this audit session | Auditor search command; forbidden non-hash table observation at `ref/p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv:207`; broad matches also in `run` and unrelated repository directories. This is not a package defect. | PI disposition; new independent audit session and directory with explicit permitted-file arguments. |


```json
{
  "id": "AUDITOR-SCOPE-01",
  "tier": "A-S",
  "v6": "global blocker (this audit session)",
  "D11": "STOP (this audit session)",
  "origin": "Auditor command; NOT a demonstrated defect of the delivered rp1-r2 package",
  "intended_target": "ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py",
  "working_directory": "G:\\PycharmProjects\\rp1r2_audit",
  "submitted_command": "Get-Content -LiteralPath 'ref\\p_konum_plus\\calibration\\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py' -Encoding UTF8 -TotalCount 320\nrg -n 'write_text|write_bytes|\\.open\\(\"[wax]|to_csv|dump\\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY' 'ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py' ",
  "observed_scope": "Output contained matches across ref and run and outside p_konum_plus, including notebooks and modules.",
  "forbidden_evidence_location": "ref/p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv:207",
  "forbidden_observation": "Search output showed non-hash columns, including a file path, source classification and notes; the instruction permits only the hash column for the disjointness check.",
  "additional_observed_table_locations": "Same table, lines 208 through 218, appeared in the tool output; contents are not reproduced here.",
  "argv_as_received_by_rg": "NOT OBSERVED; broad scope attributed to PowerShell/native argument handling is an inference, not established by an argv trace.",
  "all_files_read_by_rg": "NOT OBSERVED; no file-open trace was installed and the tool output was truncated. Absence of real/raw reads cannot be certified.",
  "response": "STOP; no harness, launcher, writer, independent test probe or re-execution started. A Ctrl-C polling request found the search already completed with exit code 0.",
  "closure_action": "PI disposition and a new independent audit session in a new directory; use structured subprocess argv and explicit permitted-file allowlists. No further correction cycle is decided by this report.",
  "instruction_basis": "Independent audit instruction section 0 reading restrictions; D-11 r1 section 5 firewall suspicion STOP."
}
```

## NOT PERFORMED list

Every substantive instruction check not explicitly marked complete in this report is NOT PERFORMED due to the auditor scope STOP. In particular: sections 1.2 prior-package transmission (instrument pins alone were checked), 1.3–1.6; section 2 except the dependency hash check; all re-execution tests/comparisons in section 3; all sections 4–6. Partial reading of governing texts or code does not fulfill these checks. Values requiring undelivered stores or intake evidence are NOT OBSERVED.

## Scripts, commands and outputs

The initial read-only commands before the incident included `Get-FileHash` and sidecar reading for the forwarded file, guarded hash equality/filename checks before `Get-Content`, reads of the governing instruction/policy and rerun procedure, `py -0p`, and reads of the delivered launcher and external custody writer. These were not execution of those Python sources. Complete source-reading tool output is not retained in this report; some tool outputs were truncated, so no claim of exhaustive review is made.

The environment tool command was:
```powershell
python -c "import sys,platform,os,numpy,scipy; print(sys.version); print(sys.executable); print(platform.platform()); print('numpy',numpy.__version__); print('scipy',scipy.__version__); print({k:os.environ.get(k) for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']})"
```

Its complete observed output was:
```text
3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)]
C:\Users\Neo\AppData\Local\Programs\Python\Python311\python.exe
Windows-10-10.0.19045-SP0
numpy 1.26.4
scipy 1.14.1
{'OMP_NUM_THREADS': None, 'OPENBLAS_NUM_THREADS': None, 'MKL_NUM_THREADS': None}
```

Custody command: `python audit_support/custody.py`, with `PYTHONDONTWRITEBYTECODE=1`. It exited successfully; its compact stdout is reproduced in the custody section. The complete per-row machine observations are retained externally in `audit_support/custody.json`; the script source follows.

```python
from pathlib import Path
import ast, csv, hashlib, json, platform, re, subprocess, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'ref'
OUT = ROOT / 'audit_support'
INSTRUCTION = Path(r'C:\Users\Neo\Downloads\F3_RP1-R2_INDEPENDENT_AUDIT_INSTRUCTION_DRAFT_r1_2026-10-12.md')
EXPECTED = '25eb0e160c90eac37b0e22249607a69b546ee065b1f8feeb1f8f8c735ec154c2'
def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''): h.update(b)
    return h.hexdigest()
def git(root, *args):
    p = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True, check=True)
    return {'command': p.args, 'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
def save(name, data):
    (OUT/name).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def main():
    import numpy, scipy
    observed = {'utc': datetime.now(timezone.utc).isoformat(), 'instruction': str(INSTRUCTION),
        'instruction_sha256': sha(INSTRUCTION), 'sidecar_text': INSTRUCTION.with_suffix('.md.sha256').read_text(),
        'user_expected_sha256': EXPECTED, 'model': 'GPT-6 / Codex (developer identity)',
        'provider_session_id': 'NOT OBSERVED', 'directory': str(ROOT),
        'prior_exposure': 'This session previously verified these two clones only; no executor, drafter or rp1-r1 auditor work in this session.',
        'clone_creation': 'PI creation is user-reported; clone/checkout commands were not run by this auditor.',
        'environment': {'python': platform.python_version(), 'numpy': numpy.__version__, 'scipy': scipy.__version__,
                        'platform': platform.platform(), 'interpreter': sys.executable},
        'git': {c: [git(ROOT/c, 'rev-parse', 'HEAD'), git(ROOT/c, 'status'), git(ROOT/c, 'status', '--porcelain=v1', '--untracked-files=all')] for c in ['ref','run']}}
    assert observed['instruction_sha256'] == EXPECTED == observed['sidecar_text'].split()[0]
    save('intake.json', observed)
    listing = REF/'p_konum_plus/provenance/f3_realdata_prep_rp1-r2_transmission_list_2026-10-12.csv'
    rows = list(csv.DictReader(listing.open(encoding='utf-8', newline='')))
    failures, files, checked = [], [], []
    for r in rows:
        p, s = REF/r['path'], REF/r['sidecar']
        assert p.resolve().is_relative_to(REF.resolve()) and s.resolve().is_relative_to(REF.resolve())
        assert r['path'].startswith('p_konum_plus/')
        d = {'path': r['path'], 'bytes': p.stat().st_size, 'sha256': sha(p), 'sidecar_sha256': sha(s)}
        sc = s.read_text(encoding='ascii').strip().split(maxsplit=1)
        d['ok'] = (d['bytes']==int(r['bytes']) and d['sha256']==r['sha256'] and d['sidecar_sha256']==r['sidecar_sha256'] and len(sc)==2 and sc[0]==r['sha256'] and sc[1].lstrip('*')==p.name)
        if not d['ok']: failures.append(d)
        checked.append(d); files += [r['path'],r['sidecar']]
    files += [listing.relative_to(REF).as_posix(), listing.relative_to(REF).as_posix()+'.sha256']
    own_sc = Path(str(listing)+'.sha256').read_text().split()
    diff = git(REF, 'diff', '--name-status', 'd9a5e99', '25c7d51')
    changes = [line.split('\t',1) for line in diff['stdout'].splitlines()]
    added = {p for status,p in changes if status=='A'}
    hashes = []
    for expected, path in re.findall(r'^([0-9a-f]{64})  (p_konum_plus/[^\r\n]+)$', INSTRUCTION.read_text(encoding='utf-8'), re.M):
        actual = sha(REF/path)
        hashes.append({'path':path,'expected':expected,'observed':actual,'ok':actual==expected})
    harness = REF/'p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py'
    tree = ast.parse(harness.read_text(encoding='utf-8'))
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='RP2_DEPENDENCY_PINS' for t in n.targets)))
    deps = [{'path':str(harness.with_name(name).relative_to(REF)), 'expected':pin,'observed':sha(harness.with_name(name))} for name,pin in pins.items()]
    result = {'utc':datetime.now(timezone.utc).isoformat(),'transmission_rows':len(rows),'checked':checked,'failures':failures,
        'own_sidecar_ok': own_sc==[sha(listing),listing.name], 'diff_command':diff['command'],
        'added_count':len(added),'change_statuses':sorted(set(s for s,p in changes)),
        'outside_package':[p for s,p in changes if not p.startswith('p_konum_plus/')],
        'missing_from_list':sorted(added-set(files)), 'extra_in_list':sorted(set(files)-added),
        'duplicate_list_paths':len(files)-len(set(files)), 'instruction_pins':hashes, 'dependencies':deps}
    save('custody.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ['checked','instruction_pins']},indent=2))
    assert not failures and result['own_sidecar_ok'] and not result['missing_from_list'] and not result['extra_in_list'] and not result['duplicate_list_paths']
    assert all(r['ok'] for r in hashes) and all(d['expected']==d['observed'] for d in deps)

if __name__=='__main__': main()

```

[A-S] Final clone state commands and outputs (both still clean at the original HEAD):


```json
{
  "utc": "2026-10-12T17:34:59.207648+00:00",
  "git": {
    "ref": [
      {
        "command": [
          "git",
          "-C",
          "G:\\PycharmProjects\\rp1r2_audit\\ref",
          "rev-parse",
          "HEAD"
        ],
        "returncode": 0,
        "stdout": "25c7d51a0d14e8935f464a7a52d6a49ef4383e2b\n",
        "stderr": ""
      },
      {
        "command": [
          "git",
          "-C",
          "G:\\PycharmProjects\\rp1r2_audit\\ref",
          "status"
        ],
        "returncode": 0,
        "stdout": "HEAD detached at 25c7d51\nnothing to commit, working tree clean\n",
        "stderr": ""
      },
      {
        "command": [
          "git",
          "-C",
          "G:\\PycharmProjects\\rp1r2_audit\\ref",
          "status",
          "--porcelain=v1",
          "--untracked-files=all"
        ],
        "returncode": 0,
        "stdout": "",
        "stderr": ""
      }
    ],
    "run": [
      {
        "command": [
          "git",
          "-C",
          "G:\\PycharmProjects\\rp1r2_audit\\run",
          "rev-parse",
          "HEAD"
        ],
        "returncode": 0,
        "stdout": "25c7d51a0d14e8935f464a7a52d6a49ef4383e2b\n",
        "stderr": ""
      },
      {
        "command": [
          "git",
          "-C",
          "G:\\PycharmProjects\\rp1r2_audit\\run",
          "status"
        ],
        "returncode": 0,
        "stdout": "HEAD detached at 25c7d51\nnothing to commit, working tree clean\n",
        "stderr": ""
      },
      {
        "command": [
          "git",
          "-C",
          "G:\\PycharmProjects\\rp1r2_audit\\run",
          "status",
          "--porcelain=v1",
          "--untracked-files=all"
        ],
        "returncode": 0,
        "stdout": "",
        "stderr": ""
      }
    ]
  }
}
```

Audit support artifact hashes (computed at report generation):


```json
{
  "audit_support/custody.json": "10965cb107c1d4498745e83252da79e9480f23f7edf9e31dae19b2a690fe94b7",
  "audit_support/custody.py": "7fdd3fa1748b5f431d15518a53d723c0b9fdfb4186704df5d0186d88ec5f9c40",
  "audit_support/intake.json": "e38f49f35371aa61463b5f17a4f0e87d301bb18c0f7810e75b032d3f5e4bc67f",
  "audit_support/scope_incident.json": "e087b8eb82d39ca5c02ec50c2f33252b8c624b7e00547064a6fce407ae9aaee1",
  "audit_support/stop_report.py": "d941eef6ad2afb7b2475d79b4c92c8c810a636ffab23f7d8eab3db82f87ac77b",
  "audit_support/stop_state.json": "c8d44bf49c7340d238214991b3c5554154c915c17fac622a9a16ad9d7c63c444"
}
```

Report generator source:
```python
from pathlib import Path
import hashlib, json, subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SUPPORT = ROOT/'audit_support'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def pretty(value): return json.dumps(value, indent=2, ensure_ascii=False)
def block(value): return '\n```json\n'+pretty(value)+'\n```\n'
intake = json.loads((SUPPORT/'intake.json').read_text(encoding='utf-8'))
custody = json.loads((SUPPORT/'custody.json').read_text(encoding='utf-8'))
end = {'utc':datetime.now(timezone.utc).isoformat(),'git':{}}
for clone in ('ref','run'):
    end['git'][clone] = []
    for args in (['rev-parse','HEAD'],['status'],['status','--porcelain=v1','--untracked-files=all']):
        command = ['git','-C',str(ROOT/clone),*args]
        p = subprocess.run(command,capture_output=True,text=True,check=True)
        end['git'][clone].append({'command':command,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
(SUPPORT/'stop_state.json').write_text(pretty(end)+'\n',encoding='utf-8')
incident = {
    'id':'AUDITOR-SCOPE-01', 'tier':'A-S', 'v6':'global blocker (this audit session)', 'D11':'STOP (this audit session)',
    'origin':'Auditor command; NOT a demonstrated defect of the delivered rp1-r2 package',
    'intended_target':'ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py',
    'working_directory':str(ROOT),
    'submitted_command':r'''Get-Content -LiteralPath 'ref\p_konum_plus\calibration\f3_step2_adequacy_harness_rp1-r2_2026-10-10.py' -Encoding UTF8 -TotalCount 320
rg -n 'write_text|write_bytes|\.open\("[wax]|to_csv|dump\(|OUT_|OUTPUT|RESTART_STORE_DIR|RUNTIME.*CUSTODY' 'ref/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py' ''',
    'observed_scope':'Output contained matches across ref and run and outside p_konum_plus, including notebooks and modules.',
    'forbidden_evidence_location':'ref/p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv:207',
    'forbidden_observation':'Search output showed non-hash columns, including a file path, source classification and notes; the instruction permits only the hash column for the disjointness check.',
    'additional_observed_table_locations':'Same table, lines 208 through 218, appeared in the tool output; contents are not reproduced here.',
    'argv_as_received_by_rg':'NOT OBSERVED; broad scope attributed to PowerShell/native argument handling is an inference, not established by an argv trace.',
    'all_files_read_by_rg':'NOT OBSERVED; no file-open trace was installed and the tool output was truncated. Absence of real/raw reads cannot be certified.',
    'response':'STOP; no harness, launcher, writer, independent test probe or re-execution started. A Ctrl-C polling request found the search already completed with exit code 0.',
    'closure_action':'PI disposition and a new independent audit session in a new directory; use structured subprocess argv and explicit permitted-file allowlists. No further correction cycle is decided by this report.',
    'instruction_basis':'Independent audit instruction section 0 reading restrictions; D-11 r1 section 5 firewall suspicion STOP.'
}
(SUPPORT/'scope_incident.json').write_text(pretty(incident)+'\n',encoding='utf-8')
date = datetime.now(timezone.utc).date().isoformat()
report = ROOT/f'f3_realdata_prep_rp1-r2_independent_audit_gpt-6_codex_DRAFT_r1_{date}.md'
parts = ['# F3 rp1-r2 independent audit — DRAFT r1\n',
    '## Identity and prior exposure\n', block({k:intake[k] for k in ['utc','model','provider_session_id','directory','prior_exposure','clone_creation']}),
    'This report distinguishes [A] delivered-byte checks, [A-S] commands executed by this auditor, and [X] unverified executor or third-party claims. Quantities below are generated from the evidence JSON by `audit_support/stop_report.py`.\n',
    '## Verdict\n',
    '**NOT PASSED — AUDIT STOPPED / INCOMPLETE.** The auditor search exceeded the permitted reading scope. This session cannot certify the required firewall discipline. This is an auditor-caused incident, not a finding that rp1-r2 computed an incorrect result or accessed real data. No package pass, binding, qualification or closure is declared. The unperformed auditor run alone leaves the section 8 pass criterion unestablished.\n',
    'STOP was reported to the PI in the current conversation. No new package B is established and no third correction cycle is proposed as decided.\n',
    '## Custody (section 1)\n',
    '[A-S] Instruction intake: computed file hash, sidecar hash token and PI-forwarded value agree; the sidecar filename was also checked before reading the instruction.\n',
    block({k:intake[k] for k in ['instruction','instruction_sha256','sidecar_text','user_expected_sha256']}),
    '[A-S] Initial clone verification commands and complete outputs:\n',block(intake['git']),
    '[A] The transmission list payload sizes, SHA256, sidecar content/name and sidecar SHA256 were checked on each row. The list and its sidecar exactly cover the commit-added set with no modification or deletion.\n',
    block({k:custody[k] for k in ['utc','transmission_rows','failures','own_sidecar_ok','diff_command','added_count','change_statuses','outside_package','missing_from_list','extra_in_list','duplicate_list_paths']}),
    '[A] Full file/hash pairs extracted from the forwarded instruction were checked against the specifically named files:\n',block(custody['instruction_pins']),
    'These checks do not establish the contents of undelivered restart stores, every executor-written value, fixture correspondence, prior-package transmission integrity or scientific correctness. Those checks were not completed. The intake evidence cited by D-14 remains [X]; its repository absence was not independently checked before STOP.\n',
    '## Code (section 2)\n',
    '[A] The final harness dependency dictionary was parsed with AST without importing or executing the harness. Each named dependency equals its pin:\n',block(custody['dependencies']),
    'NOT PERFORMED: full real-data-path binding file inventory; W-3/end-record cross-checks; both independent harness diffs and label judgments; attempt-change judgments for each declaration; E-declaration scope review. Partial source reading is not reported as a completed code audit.\n',
    '## Re-execution and environment (section 3)\n',
    '[A-S] Local interpreter/library/platform observation:\n',block(intake['environment']),
    '| Field | Instruction binding value (claim until binding record checked) | Local observation | Comparison |\n|---|---|---|---|\n']
for key, expected in [('python','3.11.7'),('numpy','1.26.4'),('scipy','1.14.1'),('platform','Windows-10-10.0.19045-SP0')]:
    observed = intake['environment'][key]
    parts.append(f'| {key} | {expected} | {observed} | {"equal" if expected==observed else "different"} |\n')
parts += [
    '| OMP_NUM_THREADS | 1 | unset in the environment observation | not configured for a run |\n',
    '| OPENBLAS_NUM_THREADS | 1 | unset in the environment observation | not configured for a run |\n',
    '| MKL_NUM_THREADS | 1 | unset in the environment observation | not configured for a run |\n',
    'The thread values come from the full tool output of the environment command below, not from a launched harness. No W-3 writer, launcher or harness was invoked. No launch records were moved aside; no delivered output was overwritten; no restart store was created by this auditor. Re-execution stopped before preparation because of AUDITOR-SCOPE-01.\n',
    '## Non-regression and accounting (section 4)\n',
    'NOT PERFORMED: scientific S/canonical/residual comparison, non-regression leaf checks, independent plan/family/mode/store accounting, fallback analysis, timing reconciliation, the prelaunch-to-final ledger transition table and size-estimate arithmetic. Executor and drafting-session counts are not adopted as audit evidence.\n',
    '## Items (section 5)\n',
    'NOT PERFORMED: Q1–Q11 semantic review and independent probes; fixture hash disjointness and synthetic construction; launch firewall review; IR1-13 ledger review; section 5(b) invocation/output isolation; record/errata trace; requirement-map agreement. No mandatory test or negative-case pass is certified.\n',
    '## Ledger (section 6)\n',
    'No item is closed by this report. No repository ledger was written. The instruction requires IR1-13 to remain OPEN / B under D-14; that PI decision is not reopened. Final-ledger statuses, prior-auditor closures and closure-point discrepancies were NOT PERFORMED and must be checked by the next valid audit.\n',
    '## Findings table\n',
    '| ID | v6 | D-11 r1 | Location and evidence | Closure action |\n|---|---|---|---|---|\n',
    '| AUDITOR-SCOPE-01 [A-S] | global blocker for this audit session | STOP for this audit session | Auditor search command; forbidden non-hash table observation at `ref/p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv:207`; broad matches also in `run` and unrelated repository directories. This is not a package defect. | PI disposition; new independent audit session and directory with explicit permitted-file arguments. |\n',
    block(incident),
    '## NOT PERFORMED list\n',
    'Every substantive instruction check not explicitly marked complete in this report is NOT PERFORMED due to the auditor scope STOP. In particular: sections 1.2 prior-package transmission (instrument pins alone were checked), 1.3–1.6; section 2 except the dependency hash check; all re-execution tests/comparisons in section 3; all sections 4–6. Partial reading of governing texts or code does not fulfill these checks. Values requiring undelivered stores or intake evidence are NOT OBSERVED.\n',
    '## Scripts, commands and outputs\n',
    'The initial read-only commands before the incident included `Get-FileHash` and sidecar reading for the forwarded file, guarded hash equality/filename checks before `Get-Content`, reads of the governing instruction/policy and rerun procedure, `py -0p`, and reads of the delivered launcher and external custody writer. These were not execution of those Python sources. Complete source-reading tool output is not retained in this report; some tool outputs were truncated, so no claim of exhaustive review is made.\n',
    'The environment tool command was:\n```powershell\npython -c "import sys,platform,os,numpy,scipy; print(sys.version); print(sys.executable); print(platform.platform()); print(\'numpy\',numpy.__version__); print(\'scipy\',scipy.__version__); print({k:os.environ.get(k) for k in [\'OMP_NUM_THREADS\',\'OPENBLAS_NUM_THREADS\',\'MKL_NUM_THREADS\']})"\n```\n',
    'Its complete observed output was:\n```text\n3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)]\nC:\\Users\\Neo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe\nWindows-10-10.0.19045-SP0\nnumpy 1.26.4\nscipy 1.14.1\n{\'OMP_NUM_THREADS\': None, \'OPENBLAS_NUM_THREADS\': None, \'MKL_NUM_THREADS\': None}\n```\n',
    'Custody command: `python audit_support/custody.py`, with `PYTHONDONTWRITEBYTECODE=1`. It exited successfully; its compact stdout is reproduced in the custody section. The complete per-row machine observations are retained externally in `audit_support/custody.json`; the script source follows.\n',
    '```python\n'+(SUPPORT/'custody.py').read_text(encoding='utf-8')+'\n```\n',
    '[A-S] Final clone state commands and outputs (both still clean at the original HEAD):\n',block(end),
    'Audit support artifact hashes (computed at report generation):\n',
    block({p.relative_to(ROOT).as_posix():sha(p) for p in sorted(SUPPORT.iterdir()) if p.is_file()}),
    'Report generator source:\n```python\n'+Path(__file__).read_text(encoding='utf-8')+'\n```\n',
    '**For the PI:** D-9 section 2(a) preconditions are not established by this stopped audit; the required auditor non-regression run and binding file inventory are NOT PERFORMED. Observed platform/Python/numpy/scipy equal the instruction values; thread pins were unset and no run environment was configured.\n']
report.write_text('\n'.join(parts),encoding='utf-8',newline='\n')
digest = sha(report)
Path(str(report)+'.sha256').write_text(digest+'  '+report.name+'\n',encoding='ascii',newline='\n')
assert Path(str(report)+'.sha256').read_text().split()[0]==sha(report)
print(pretty({'report':str(report),'sha256':digest,'sidecar':str(report)+'.sha256','verdict':'NOT PASSED / AUDIT STOPPED','stop_utc':end['utc']}))

```

**For the PI:** D-9 section 2(a) preconditions are not established by this stopped audit; the required auditor non-regression run and binding file inventory are NOT PERFORMED. Observed platform/Python/numpy/scipy equal the instruction values; thread pins were unset and no run environment was configured.
