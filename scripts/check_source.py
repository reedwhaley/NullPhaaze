"""Check the source allowlist and its per-file notation before a local build."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = {'.exe', '.dll', '.so', '.dylib', '.pyc', '.pyo', '.o', '.obj', '.elf', '.bin',
             '.iso', '.wbfs', '.pak', '.ntwk', '.db', '.sqlite3', '.pem', '.key', '.zip', '.gz', '.tar'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh-hashes', action='store_true', help='After reviewing local edits and updating their notes, record the new hashes')
    args = parser.parse_args()
    index = ROOT / 'SOURCE_MANIFEST.json'
    manifest = json.loads(index.read_text(encoding='utf-8'))
    seen = set()
    for row in manifest['files']:
        name = row['path']
        path = (ROOT / name).resolve()
        if name in seen or not path.is_relative_to(ROOT) or not path.is_file() or path.suffix.lower() in FORBIDDEN:
            raise ValueError(f'Invalid source entry: {name}')
        seen.add(name)
        if not row.get('note') or not row.get('notation'):
            raise ValueError(f'Missing technical notation: {name}')
        # The inventory's self-entry has an explicit null hash. Its integrity is
        # bound by the source ZIP checksum, avoiding a recursive self-hash claim.
        if name == 'SOURCE_MANIFEST.json':
            if row['sha256'] is not None:
                raise ValueError('The source inventory cannot hash itself')
            continue
        data = path.read_bytes()
        actual = hashlib.sha256(data).hexdigest()
        if args.refresh_hashes:
            row.update(bytes=len(data), sha256=actual)
        elif actual != row['sha256'] or len(data) != row['bytes']:
            raise ValueError(f'Source hash/size differs: {name}')
    # Refreshing hashes never discovers and admits a new file implicitly. Add a
    # deliberate entry and technical note before making new source a build input.
    if args.refresh_hashes:
        index.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Checked {len(seen)} source entries; every entry has technical notation')


if __name__ == '__main__':
    main()
