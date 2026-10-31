# This command assembles an explicitly selected diagnostic DOL. Keep its requested probe
# options and output path separate from normal seed export and existing game images.
# Boundary names here: parse_args, main.
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = Path(__file__).resolve().parents[2]
    _repository_root_str = os.fspath(_repository_root)
    if _repository_root_str not in sys.path:
        sys.path.insert(0, _repository_root_str)

from randovania.games.prime3.exporter.probe_delivery import build_unhooked_probe_dol
from randovania.games.prime3.exporter.runtime_payload import Prime3RuntimePayloadManifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--original-dol", type=Path, required=True)
    parser.add_argument("--output-dol", type=Path, required=True)
    parser.add_argument("--payload-bin", type=Path, required=True)
    parser.add_argument("--payload-manifest", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--payload-address")
    parser.add_argument("--halt-at-address")
    parser.add_argument("--expected-halt-word")
    parser.add_argument("--checkpoint-name")
    parser.add_argument("--halt-at-entry", action="store_true")
    parser.add_argument("--install-entry-bootstrap", action="store_true")
    parser.add_argument("--install-relocated-runtime", action="store_true")
    parser.add_argument("--install-recurring-poll-hook", action="store_true")
    parser.add_argument("--enable-ios-udp-diagnostic", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.original_dol.resolve() == args.output_dol.resolve():
        raise RuntimeError("Input and output DOL paths must differ for probe builds.")
    manifest = Prime3RuntimePayloadManifest.from_json_text(args.payload_manifest.read_text(encoding="utf-8"))
    result = build_unhooked_probe_dol(
        args.original_dol.read_bytes(),
        args.payload_bin.read_bytes(),
        manifest,
        payload_virtual_address=None if args.payload_address is None else int(args.payload_address, 0),
        halt_at_address=None if args.halt_at_address is None else int(args.halt_at_address, 0),
        expected_halt_word=None if args.expected_halt_word is None else int(args.expected_halt_word, 0),
        checkpoint_name=args.checkpoint_name,
        halt_at_entry=args.halt_at_entry,
        install_entry_bootstrap=args.install_entry_bootstrap,
        install_relocated_runtime=args.install_relocated_runtime,
        install_recurring_poll_hook=args.install_recurring_poll_hook,
        enable_ios_udp_diagnostic=args.enable_ios_udp_diagnostic,
    )
    args.output_dol.parent.mkdir(parents=True, exist_ok=True)
    args.output_dol.write_bytes(result.probe_dol_bytes)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    report: dict[str, object] = {"probe_section": result.probe_section.to_json_dict()}
    if result.checkpoint_gate is not None:
        report["checkpoint_gate"] = result.checkpoint_gate.to_json_dict()
    if result.entry_bootstrap is not None:
        report["entry_bootstrap"] = result.entry_bootstrap.to_json_dict()
    if result.relocated_runtime is not None:
        report["relocated_runtime"] = result.relocated_runtime.to_json_dict()
    if result.recurring_poll_hook is not None:
        report["recurring_poll_hook"] = result.recurring_poll_hook.to_json_dict()
    if args.enable_ios_udp_diagnostic:
        report["ios_udp_diagnostic_enabled"] = True
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
