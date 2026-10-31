# MP3-024: show mapped room geometry without marking rooms visited. Boundary names here:
# reveal_mapa, install.
"""MP3-024: show mapped room geometry without marking rooms visited.

Corruption stores identical MAPA assets in Worlds.pak and gameplay PAKs.
Update every supported alias, preserving explicitly hidden (Never) maps.
"""
from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from nullphaze_core.archives import Archive

ARCHIVES = ("Worlds.pak", "Metroid1.pak", "Metroid3.pak", "Metroid4.pak",
            "Metroid5.pak", "Metroid6.pak", "Metroid7.pak", "Metroid8.pak")


def reveal_mapa(raw: bytes, identity: int) -> tuple[bytes, int]:
    if len(raw) < 16:
        raise ValueError(f"Full map: truncated MAPA {identity:016X}")
    magic, version, kind, visibility = struct.unpack_from(">4I", raw)
    if (magic, version, kind) != (0xDEADD00D, 5, 0) or visibility not in (0, 1, 2, 3):
        raise ValueError(f"Full map: unsupported MAPA header {identity:016X}: "
                         f"{magic:08X}/{version}/{kind}/{visibility}")
    # 3 = explicitly hidden, used by transition-only and ship interiors.
    # 1 and 2 are regular map/visit-gated room geometries. Only this
    # visibility field changes: no world, visit, landing or progression flags.
    if visibility in (1, 2):
        return raw[:12] + bytes(4) + raw[16:], visibility
    return raw, visibility


def install(files: Path, output: Path) -> dict:
    files, output = Path(files), Path(output)
    if output.exists() or files.resolve() == output.resolve():
        raise ValueError("Full map: requires a new staging directory")
    archives = {name: Archive(files / name) for name in ARCHIVES}
    canonical = {}
    for resource in archives["Worlds.pak"].resources:
        if resource.kind != b"MAPA":
            continue
        raw = resource.read()
        if resource.identity in canonical and canonical[resource.identity] != raw:
            raise ValueError(f"Full map: conflicting Worlds.pak MAPA {resource.identity:016X}")
        reveal_mapa(raw, resource.identity)
        canonical[resource.identity] = raw
    if not canonical:
        raise ValueError("Full map: Worlds.pak has no MAPA resources")
    # Validate all aliases before creating outputs, so unsupported structures fail closed.
    for name, archive in archives.items():
        for resource in archive.resources:
            if resource.kind != b"MAPA":
                continue
            raw = resource.read()
            if resource.identity not in canonical or canonical[resource.identity] != raw:
                raise ValueError(f"Full map: missing or conflicting MAPA {resource.identity:016X} in {name}")
    output.mkdir(parents=True)
    report = {"archives": {}, "revealed_ids": [], "preserved_hidden_ids": [],
              "visit_flags_modified": False, "gameplay_verified": False}
    for name, archive in archives.items():
        rows = []
        changed = 0
        for resource in archive.resources:
            if resource.kind == b"MAPA":
                raw = resource.read()
                patched, mode = reveal_mapa(raw, resource.identity)
                if name == "Worlds.pak":
                    key = "preserved_hidden_ids" if mode == 3 else "revealed_ids"
                    value = f"{resource.identity:016X}"
                    if value not in report[key]:
                        report[key].append(value)
                if patched != raw:
                    resource = resource.updated(patched)
                    changed += 1
            rows.append(resource)
        if not changed:
            continue
        destination = output / name
        archive.write(destination, rows)
        actual = Archive(destination).resources
        if len(actual) != len(rows) or any(
            (a.kind, a.identity, a.read()) != (b.kind, b.identity, b.read())
            for a, b in zip(actual, rows, strict=True)
        ):
            raise ValueError(f"Full map: archive readback mismatch in {name}")
        report["archives"][name] = str(destination)
    (output / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report
