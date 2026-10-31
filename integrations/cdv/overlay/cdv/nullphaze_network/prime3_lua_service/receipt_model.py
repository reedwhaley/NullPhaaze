# Executable design model, NOT a game/save implementation or runtime service. Boundary names
# here: Snapshot, Model, fault_matrix, main.
"""Executable design model, NOT a game/save implementation or runtime service.

Atomic replacement here is an explicit assumption that still needs to be proven
for the retail save container. No model state is written into a game or save.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)


@dataclasses.dataclass(frozen=True)
class Snapshot:
    identity: str
    cursor: int = 0
    expansions: int = 0


class Model:
    def __init__(self, saved: Snapshot):
        self.saved = saved
        self.current = saved
        self.pending: Snapshot | None = None

    def begin(self, identity: str, sequence: int) -> str:
        if identity != self.current.identity:
            return "WRONG_SAVE"
        if self.pending is not None:
            return "BUSY"
        if sequence <= 0:
            return "INVALID_SEQUENCE"
        if sequence <= self.current.cursor:
            return "ALREADY_APPLIED"
        if sequence != self.current.cursor + 1:
            return "SEQUENCE_GAP"
        self.pending = dataclasses.replace(self.current, cursor=sequence, expansions=self.current.expansions + 1)
        return "PREPARED"

    def finish(self) -> str:
        if self.pending is None:
            raise ValueError("No prepared transaction")
        self.current, self.pending = self.pending, None
        return "APPLIED_VOLATILE"

    def save(self, success: bool = True) -> str:
        if self.pending is not None:
            return "BUSY"
        if not success:
            return "SAVE_FAILED"
        # Assumed atomic co-save commit; this is not evidence of native behavior.
        self.saved = self.current
        return "SAVED"

    def reload(self) -> None:
        self.current, self.pending = self.saved, None


def fault_matrix() -> dict:
    """Enumerate recovery cuts, retaining the host's immutable ordered history."""
    cases = []
    for cut in ("before_prepare", "after_prepare", "after_apply", "save_failure", "after_save", "after_ack"):
        model = Model(Snapshot("campaign/slot"))
        if cut != "before_prepare":
            assert model.begin("campaign/slot", 1) == "PREPARED"
        if cut not in {"before_prepare", "after_prepare"}:
            assert model.finish() == "APPLIED_VOLATILE"
        if cut == "save_failure":
            assert model.save(False) == "SAVE_FAILED"
        if cut in {"after_save", "after_ack"}:
            assert model.save() == "SAVED"
        model.reload()
        status = model.begin("campaign/slot", 1)
        if status == "PREPARED":
            model.finish()
            model.save()
        assert model.saved.cursor == model.saved.expansions == 1
        cases.append({"cut": cut, "replay_status": status, "saved_expansions_after_recovery": 1})
    # Separate persistent writes admit both mismatch states regardless of order.
    counterexamples = [
        {"write_order": "sidecar_first", "crash_state": {"receipt": 1, "inventory": 0}, "outcome": "lost_grant"},
        {
            "write_order": "inventory_first",
            "crash_state": {"receipt": 0, "inventory": 1},
            "outcome": "duplicate_on_replay",
        },
    ]
    return {
        "scope": "abstract model only, no game/save/network IO",
        "assumptions": [
            "inventory effects and ledger are one atomic durable snapshot",
            "save serialization cannot interleave a partial grant",
            "each campaign/slot has an immutable host-retained ordered history",
            "actual native save identity, format, integrity and commit boundary remain unimplemented",
        ],
        "co_save_crash_cuts": cases,
        "independent_sidecar_counterexamples": counterexamples,
        "native_save_atomicity_verified": False,
        "production_grants_enabled": False,
        "hardware_verified": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = fault_matrix()
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
