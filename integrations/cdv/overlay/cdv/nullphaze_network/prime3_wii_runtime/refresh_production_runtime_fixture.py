# Regenerate the source fixture text from the selected runtime description. A refreshed
# fixture is build metadata, not evidence that a new runtime passed gameplay or hardware
# tests. Boundary names here: build_fixture_text, parse_args, main.
from __future__ import annotations

import argparse
import base64
import io
import zipfile
from pathlib import Path

FIXTURE_MEMBERS = ("payload.bin", "payload.json")
FIXTURE_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def build_fixture_text(asset_directory: Path) -> str:
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_STORED) as output:
        for name in FIXTURE_MEMBERS:
            source = asset_directory.joinpath(name)
            if not source.is_file():
                raise FileNotFoundError(f"Canonical production runtime asset is missing: {source}")
            info = zipfile.ZipInfo(name, date_time=FIXTURE_TIMESTAMP)
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            output.writestr(info, source.read_bytes())
    return base64.b64encode(archive.getvalue()).decode("ascii")


def parse_args() -> argparse.Namespace:
    repository_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Refresh the self-contained CP3W TCP production test fixture.")
    parser.add_argument(
        "--asset-directory",
        type=Path,
        default=repository_root.joinpath("build", "prime3_wii_runtime", "production"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repository_root.joinpath(
            "test", "games", "prime3", "exporter", "fixtures", "cp3w_production_runtime.zip.b64"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.write_text(build_fixture_text(args.asset_directory), encoding="ascii", newline="\n")


if __name__ == "__main__":
    main()
