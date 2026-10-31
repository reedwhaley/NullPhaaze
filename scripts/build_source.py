"""Build the private RDS and backend wheels from a verified lean source tree."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(*arguments, cwd=None, environment=None):
    # Use this interpreter throughout. Picking up another pip on PATH can install
    # the public RDS build while the backend expects our exact private version.
    subprocess.run([str(value) for value in arguments], cwd=cwd, env=environment, check=True)


def verify_source():
    manifest = json.loads((ROOT / 'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    for row in manifest['files']:
        path = (ROOT / row['path']).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise ValueError(f"Source entry escaped or disappeared: {row['path']}")
        if row['sha256'] is not None and hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
            raise ValueError(f"Source changed since the package was assembled: {row['path']}")
    # SOURCE_MANIFEST describes itself without a recursive self-hash. The ZIP's
    # adjacent checksum binds that file along with every other archived byte.
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if sys.version_info[:2] != (3, 12) or sys.maxsize <= 2**32:
        raise RuntimeError('Use 64-bit Python 3.12 for this source snapshot')
    output = args.output.resolve()
    if output.is_relative_to(ROOT) or ROOT.is_relative_to(output):
        raise ValueError('Build output must be disjoint from the source tree')
    manifest = verify_source()
    output.mkdir(parents=True, exist_ok=False)
    stage = output / 'source'
    # Copy the manifest allowlist, not a live checkout walk. A user may keep a
    # .venv or prior build beside these sources; neither belongs in the build input.
    stage.mkdir()
    for row in manifest['files']:
        destination = stage / row['path']
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / row['path'], destination)
    environment = dict(os.environ, SOURCE_DATE_EPOCH='1793318400', PYTHONDONTWRITEBYTECODE='1')
    wheels = output / 'dist'
    # The private reader wheel is built first. Backend dependency resolution is
    # deliberately disabled here so a package-index lookup cannot replace it.
    for project in (stage / 'vendor/retro-data-structures', stage):
        run(sys.executable, '-m', 'pip', 'wheel', '--no-deps', '--no-build-isolation',
            '--wheel-dir', wheels, project, environment=environment)
    print(f'Built RDS and backend wheels in {wheels}')


if __name__ == '__main__':
    main()
