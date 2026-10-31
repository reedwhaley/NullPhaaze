"""Apply the recognized .14r2 integration to an explicitly selected source copy."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bounded(root, relative):
    name = PurePosixPath(relative)
    if name.is_absolute() or '..' in name.parts or '\\' in relative:
        raise ValueError('Invalid overlay path')
    path = root.joinpath(*name.parts)
    # Refuse junctions/symlinks even when their present destination is inside the
    # target. The preimage being checked must be the file we later replace.
    for part in (path, *path.parents):
        if part == root.parent:
            break
        if part.is_symlink() or part.is_junction():
            raise ValueError(f'Reparse path in overlay target: {part}')
    if not path.resolve().is_relative_to(root):
        raise ValueError('Overlay path escaped its root')
    return path


def preflight(target):
    manifest = json.loads((ROOT / 'integrations/cdv/overlay-manifest.json').read_text(encoding='utf-8'))
    changes = []
    for row in manifest['files']:
        source = bounded(ROOT, row['source'])
        destination = bounded(target, row['target'])
        if not source.is_file() or digest(source) != row['result_sha256']:
            raise ValueError(f"Overlay payload changed: {row['source']}")
        if destination.exists() and not destination.is_file():
            raise ValueError(f"Overlay destination is not a file: {row['target']}")
        actual = digest(destination) if destination.is_file() else None
        if actual not in row['accepted_existing_sha256']:
            raise ValueError(f"Unrecognized local edit; no files written: {row['target']}")
        if actual != row['result_sha256']:
            changes.append((source, destination, actual))
    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True, help='An isolated .14r2 repository root, containing cdv/')
    parser.add_argument('--apply', action='store_true', help='Write after every preimage passes; default is check only')
    args = parser.parse_args()
    target = args.target.resolve()
    if not (target / 'cdv/randovania').is_dir():
        raise ValueError('Select the repository root containing cdv/randovania')
    if target == ROOT or target.is_relative_to(ROOT) or ROOT.is_relative_to(target):
        raise ValueError('The target must be separate from this source package')
    changes = preflight(target)
    if args.apply:
        # Check the entire set first, then check each preimage again immediately
        # before replacing it. An unknown edit never becomes an accepted baseline.
        for source, destination, before in changes:
            if (digest(destination) if destination.is_file() else None) != before:
                raise ValueError(f'Target changed during overlay application: {destination}')
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination = bounded(target, destination.relative_to(target).as_posix())
            descriptor, temporary_name = tempfile.mkstemp(prefix='.nullphaze-overlay-', dir=destination.parent)
            temporary = Path(temporary_name)
            try:
                # Replace one complete file at a time. An interrupted apply can
                # resume from recognized old/new hashes without a truncated file
                # becoming an unrecognized local edit.
                with os.fdopen(descriptor, 'wb') as stream:
                    stream.write(source.read_bytes())
                    stream.flush()
                    os.fsync(stream.fileno())
                if (digest(destination) if destination.is_file() else None) != before:
                    raise ValueError(f'Target changed while staging overlay file: {destination}')
                os.replace(temporary, destination)
            finally:
                if temporary.exists():
                    temporary.unlink()
        print(f'Applied {len(changes)} integration/source files. Rebuild native templates from this exact source.')
    else:
        print(f'All preimages recognized; {len(changes)} files would change. Use --apply to write this set.')


if __name__ == '__main__':
    main()
