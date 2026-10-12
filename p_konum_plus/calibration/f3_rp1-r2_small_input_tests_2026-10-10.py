"""Logged, isolated small-input checks; outputs never enter the W-3 attempt.

Two trajectories traverse the real consumer with explicit TEST_ONLY fitter
spies. These exercise intake, IDs, phase, restoration and event reconciliation,
not frozen optimizer performance. Real optimizer handoff remains the full run's
mandatory test. Q3 uses six synthetic eligible rows on the frozen year axis.
"""
from __future__ import annotations

import os
for _pin in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_pin] = "1"

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from typing import Any


def main() -> None:
    root = Path(os.environ["F3_REPO_ROOT"]).resolve()
    quarantine = Path(os.environ["F3_RP1R2_PREFLIGHT_ROOT"]).resolve()
    assert root not in quarantine.parents and quarantine != root
    assert quarantine.is_dir()
    harness_path = root / "p_konum_plus/calibration/f3_step2_adequacy_harness_rp1-r2_2026-10-10.py"
    spec = importlib.util.spec_from_file_location("rp2_logged_small_input_harness", harness_path)
    harness = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(harness)
    g = harness.__dict__
    authority = harness.authorize_rp2_launch()
    actual_store = root / harness.RESTART_STORE_DIR
    assert not actual_store.exists(), "ATTEMPT_STORE_MUST_STAY_ABSENT"
    harness.RESTART_STORE_DIR = str(quarantine / "small_test_store")
    assert root not in Path(harness.RESTART_STORE_DIR).parents
    harness._CODE_ENV_FINGERPRINT[0] = "TEST_ONLY_SMALL_INPUT_NO_W3"
    # The consumer's real-array branch never calls this synthetic generator.
    def prohibited_generation(*args: Any, **kwargs: Any) -> None:
        raise AssertionError("REAL_CONSUMER_CALLED_GENERATOR")
    sys.modules[harness.GEN_MODULE_NAME] = SimpleNamespace(make_traj=prohibited_generation)
    loader, all_scenarios = harness.t_f1_loader_synth(str(quarantine / "loader_inputs"))
    (quarantine / "loader_test_results.json").write_text(json.dumps(loader, indent=2) + "\n", encoding="ascii")
    assert loader["pass_"], "SMALL_LOADER_CHECK_FAILED"
    scenario = copy.deepcopy(all_scenarios[0])
    scenario["strata"] = {sex: rows[:1] for sex, rows in scenario["strata"].items()}
    scenario["real_x"] = {key: value for key, value in scenario["real_x"].items() if key[1] == 0}
    scenario["real_mask_ids"] = {key: value for key, value in scenario["real_mask_ids"].items() if key[1] == 0}
    # These spies retain real consumer call sites and their actual IDs, and
    # construct deliberately labelled tiny store payloads for accounting tests.
    def family_spy(f2m: Any, grids: Any, fixture: str, family: str, x: Any,
                   obs: Any, telemetry: list[dict[str, Any]], mask_id: str, **kwargs: Any) -> dict[str, Any]:
        key = "onestart_TEST_ONLY_" + hashlib.sha256(mask_id.encode("ascii")).hexdigest()
        event = dict(fixture=fixture, fitter=family, mask_id=mask_id, start_id=0,
                     optimizer_path="primary", status=0, nit=0, nfev=0, wall_clock_seconds=0.0,
                     phase=harness.CURRENT_PHASE[0], source="fresh", unit_key=harness.KEY_SCOPE[0] + key,
                     method="TEST_ONLY_SPY_NO_OPTIMIZER")
        telemetry.append(event)
        harness.ckpt_save(key, (None, None, [event]))
        return dict(eligible=False, ghat=None, start_bank_size=1, feature_start_rejected=0, failure_codes=[])
    def spline_spy(spl: Any, fixture: str, x: Any, obs: Any, telemetry: list[dict[str, Any]],
                   mask_id: str, **kwargs: Any) -> dict[str, Any]:
        event = dict(fixture=fixture, mask_id=mask_id, mode=0, method="TEST_ONLY_SPY_NO_OPTIMIZER",
                     status=0, nit=0, nfev=0, wall_clock_seconds=0.0,
                     phase=harness.CURRENT_PHASE[0], source="fresh")
        harness.SPLINE_TELEMETRY_CALLS.append(event)
        key = "splmode_TEST_ONLY_" + hashlib.sha256(mask_id.encode("ascii")).hexdigest()
        harness.ckpt_save(key, (False, float("inf"), None, "TEST_ONLY", 0, [], [event], False))
        return dict(valid=False, ghat=None, failure=None)
    harness.fit_family = family_spy
    harness.fit_spline = spline_spy
    handoff = harness.t_f1_handoff_synth(None, None, {}, [scenario])
    assert handoff["pass_"], "SMALL_CONSUMER_HANDOFF_FAILED " + str(handoff["exception"])
    reproduction = harness.RP2_TESTS.reproduction_cases(g, str(quarantine / "reproduction_inputs"))
    observed = harness.RP2_TESTS.technical_cases(g, [scenario], handoff, reproduction)
    # D-14 negatives cannot be authorized by a descriptive flag or a new hash
    # written into a tampered record's sidecar.
    tools = harness.RP2_TOOLS
    authority_cases = [dict(name="signed_record", got=authority["pi_record_sha256"], expected=tools.D14_SHA256,
                            ok=authority["pi_record_sha256"] == tools.D14_SHA256)]
    for name in ("flag_without_record", "changed_signed_record"):
        test_root = quarantine / "authority_negatives" / name
        path = test_root / tools.D14_PATH
        path.parent.mkdir(parents=True)
        if name == "flag_without_record":
            descriptor = test_root / "p_konum_plus/provenance/f3_realdata_prep_rp1-r2_launch_authorization_2026-10-10.json"
            descriptor.parent.mkdir(parents=True)
            descriptor.write_text('{"launch_authorized": true}\n', encoding="ascii")
            expected = "D14_RECORD_OR_SIDECAR_MISSING"
        else:
            data = (root / tools.D14_PATH).read_bytes() + b"\nTEST_ONLY_MUTATION\n"
            path.write_bytes(data)
            Path(str(path) + ".sha256").write_text(hashlib.sha256(data).hexdigest() + "  " + path.name + "\n", encoding="ascii")
            expected = "D14_HASH_STOP"
        try:
            tools.authorize_ir1_13(test_root)
        except ValueError as error:
            got = str(error)
        else:
            got = "UNEXPECTED_AUTHORIZATION"
        authority_cases.append(dict(name=name, got=got, expected=expected, ok=got == expected))
    payload = dict(scope="OUTSIDE_W3_SMALL_INPUT_ONLY; TEST_ONLY fitter spies, zero optimizer calls",
        scientific_outputs_eligible_for_deliverables=False, attempt_store_used=False,
        test_store=str(harness.RESTART_STORE_DIR), loader=loader,
        technical_tests=observed, D14_authorization_cases=authority_cases)
    output = quarantine / "small_test_results.json"
    output.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="ascii")
    failed = [name for name, result in observed.items() if not result["pass_"]]
    failed += ["D14:" + row["name"] for row in authority_cases if not row["ok"]]
    assert not actual_store.exists(), "SMALL_OUTPUT_ENTERED_ATTEMPT_STORE"
    print(json.dumps(dict(scope=payload["scope"], requirements=list(observed),
                          case_count=sum(len(result["cases"]) for result in observed.values()) + len(authority_cases),
                          failed=failed, result=str(output))))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
