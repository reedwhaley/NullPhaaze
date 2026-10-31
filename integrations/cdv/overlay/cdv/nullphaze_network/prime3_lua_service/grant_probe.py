# Build a narrowly gated one-shot missile-expansion test for a disposable save. Boundary
# names here: probe_source, main.
"""Build a narrowly gated one-shot missile-expansion test for a disposable save."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from retro_data_structures.enums.corruption import State

from nullphaze_network.prime3_lua_service import bridge

PROFILE = {
    "schema": 1,
    "kind": "one_shot_missile_expansion_disposable_save",
    "item_id": 4,
    "capacity_before_required": 15,
    "capacity_delta": 5,
    "amount_delta": 5,
    "percentage_id": 21,
    "percentage_delta": 1,
    "world_id": "c133f919c108bdf9",
    "area_index": 2,
    "receipt_scope": "volatile_emulator_boot_only_not_durable_or_production",
    "automatic_after_inventory_samples": 4,
    "network_operations": 0,
}
MESSAGES = bridge.MESSAGES + (
    ("ProbeGrantPassed", State.InternalState10, "TEST MISSILE EXPANSION GRANTED\nDISPOSABLE SAVE ONLY"),
    ("ProbeGrantFailed", State.InternalState11, "TEST GRANT SKIPPED OR FAILED\nNO AUTOMATIC RETRY"),
    ("ProbeGrantAlready", State.InternalState12, "NO REPEAT GRANT THIS BOOT\nVOLATILE TEST RECEIPT"),
)


def probe_source() -> str:
    source = bridge.probe_source()
    replacements = {
        "    location_changes = 0,": (
            '    location_changes = 0,\n    grant_status = "WAITING",\n    grant_attempts = 0,'
        ),
        '"ProbeLocationChanged", "ProbeLocationUnavailable"}': (
            '"ProbeLocationChanged", "ProbeLocationUnavailable", "ProbeGrantPassed",\n'
            '        "ProbeGrantFailed", "ProbeGrantAlready"}'
        ),
        "    CP3WProbe.snapshots = CP3WProbe.snapshots + 1": (
            "    CP3WProbe.snapshots = CP3WProbe.snapshots + 1\n"
            '    if CP3WProbe.snapshots >= 4 and CP3WProbe.grant_status == "WAITING"\n'
            "        and CP3WProbe.location.available and CP3WProbe.location.area_index == 2 then\n"
            "        CP3WProbe.grant_attempts = CP3WProbe.grant_attempts + 1\n"
            "        local grant_ok, status = pcall(CP3WGrantMissileExpansion)\n"
            '        if not grant_ok then status = "FAILED" end\n'
            '        if status ~= "DEFERRED" then\n'
            "            CP3WProbe.grant_status = status\n"
            '            if status == "GRANTED" then CP3WProbe.notices.ProbeGrantPassed = true\n'
            '            elseif status == "ALREADY_GRANTED" then CP3WProbe.notices.ProbeGrantAlready = true\n'
            "            else CP3WProbe.notices.ProbeGrantFailed = true end\n"
            "        end\n"
            "    end"
        ),
    }
    for before, after in replacements.items():
        if source.count(before) != 1:
            raise ValueError("Grant-probe Lua template drift")
        source = source.replace(before, after)
    return source


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--wit", type=Path, required=True)
    parser.add_argument("--disposable-save-test", action="store_true", required=True)
    args = parser.parse_args()
    result = bridge.build(args.source_data, args.output, args.wit, grant_probe=True)
    print(f"Built disposable-save write probe {result['probe_id']}; not a production grant service.")


if __name__ == "__main__":
    main()
