# Read-only live acceptance for a private seed runtime; never sends delivery. Boundary names
# here: ReadOnlySeedClient, observe.
"""Read-only live acceptance for a private seed runtime; never sends delivery."""

import argparse
import asyncio
import dataclasses
import json
import time
from pathlib import Path

from randovania.game_connection.prime3_multiworld_client import Prime3MultiworldClient


class ReadOnlySeedClient(Prime3MultiworldClient):
    def _request(self, command, request_id, payload):
        if command not in (1, 3, 4, 9, 10):
            raise ValueError("Private seed observer cannot deliver items or write memory")
        return super()._request(command, request_id, payload)


async def observe(root, manifest_path, output, address):
    manifest = json.loads(manifest_path.read_text())
    client = ReadOnlySeedClient(address, manifest)
    baseline_save = root / "disposable-checkpoint.bin"
    original = baseline_save.read_bytes()
    output.mkdir(parents=True, exist_ok=False)
    report = {"read_only": True, "delivery_commands": 0, "snapshots": 0,
              "status": "waiting_for_save_load", "hardware_modified": False}
    (output / "result.json").write_text(json.dumps(report, indent=2))
    try:
        await client.connect()
        started = time.monotonic()
        with (output / "transcript.jsonl").open("x") as transcript:
            while time.monotonic() - started < 15 * 60:
                status = await client.status()
                snapshot = await client.snapshot()
                row = {"elapsed": time.monotonic() - started,
                       "status": dataclasses.asdict(status), "snapshot": dataclasses.asdict(snapshot)}
                transcript.write(json.dumps(row, default=lambda value: value.hex() if isinstance(value, bytes)
                                            else sorted(value) if isinstance(value, frozenset) else str(value)) + "\n")
                transcript.flush()
                if status.cursor or status.saved_cursor or status.pending:
                    raise ValueError("Read-only test observed an unexpected incoming delivery")
                if status.ready and snapshot.available:
                    report["snapshots"] += 1
                    report["status"] = "live_seed_status_and_telemetry"
                    report["generation"] = status.generation
                    report["local_locations"] = sorted(status.locations)
                    report["missiles"] = snapshot.records[4]
                    report["health"] = snapshot.health
                    report["area"] = f"{snapshot.area:016x}"
                    (output / "result.json").write_text(json.dumps(report, indent=2))
                await asyncio.sleep(2)
        report["status"] = "completed" if report["snapshots"] else "no_live_snapshot"
    except Exception as error:
        report["status"] = "failed"
        report["error"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        client.close()
        report["fixture_unchanged"] = baseline_save.read_bytes() == original
        (output / "result.json").write_text(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--address", default="127.0.0.1")
    args = parser.parse_args()
    asyncio.run(observe(args.root, args.manifest, args.output, args.address))
