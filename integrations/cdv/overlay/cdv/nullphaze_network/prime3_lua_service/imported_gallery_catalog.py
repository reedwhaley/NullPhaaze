# Read-only inventory of RDV model catalogs and source availability. Boundary names here:
# prime_models, echoes_models, inspect, audit.
"""Read-only inventory of RDV model catalogs and source availability."""

import argparse
import hashlib
import json
import re
import struct
from pathlib import Path

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.file_provider import IsoFileProvider
from retro_data_structures.game_check import Game


def prime_models(reference):
    text = reference.read_text()
    text = text[text.index("fn raw_pickup_data") :]
    rows = []
    for name, body in re.findall(r"PickupModel::(\w+) => &\[(.*?)\]", text, re.S):
        raw = bytes(int(value, 16) for value in re.findall(r"0x([0-9a-fA-F]{2})\b", body))
        if raw[:4] != struct.pack(">I", 18):
            raise ValueError(f"Unknown pickup property layout: {name}")
        end = raw.index(0, 4) + 1
        model, ancs, character, animation = struct.unpack_from(">IIII", raw, end + 5 * 12 + 6 * 4)
        rows.append(
            {
                "name": name,
                "model": model,
                "ancs": ancs,
                "character": character,
                "animation": animation,
                "pickup_prefix_sha256": hashlib.sha256(raw[: end + 100]).hexdigest(),
            }
        )
    if len(rows) != 47 or next(row for row in rows if row["name"] == "IceBeam")["model"] != 0xDA25B1BE:
        raise ValueError("Reference pickup metadata changed")
    return rows


def echoes_models(path):
    return [
        {
            "name": row["Name"],
            "model": row["Model"],
            "ancs": row["AnimSet"],
            "character": row["Character"],
            "animation": row["DefaultAnim"],
        }
        for row in json.loads(path.read_text())["ModelData"]
    ]


def inspect(rows, manager):
    result = []
    for row in rows:
        record = dict(row)
        required = {"model": "CMDL", "ancs": "ANCS"}
        missing = []
        for key, kind in required.items():
            identity = row[key]
            if identity == 0xFFFFFFFF:
                continue
            if not manager.does_asset_exists(identity):
                missing.append({"field": key, "id": f"{identity:08x}", "type": kind})
            elif manager.get_asset_type(identity) != kind:
                raise ValueError(f"Catalog type mismatch: {row['name']}/{key}")
        record["missing_from_retail"] = missing
        if not missing and row["model"] != 0xFFFFFFFF:
            mesh = manager.get_parsed_asset(row["model"])._raw
            record.update(
                surfaces=len(mesh.surfaces),
                materials=len(mesh.material_sets[0].materials),
                textures=len(mesh.material_sets[0].texture_file_ids),
                vertices=len(mesh.attrib_arrays.positions),
            )
        result.append(record)
    return result


def audit(prime_iso, echoes_iso, reference, echoes_catalog, output):
    sources = [
        (Game.PRIME, prime_iso, prime_models(reference)),
        (Game.ECHOES, echoes_iso, echoes_models(echoes_catalog)),
    ]
    report = {
        "read_only": True,
        "include_variants_and_placeholders": True,
        "conversion_to_Corruption": "not_performed",
        "games": {},
    }
    for game, path, rows in sources:
        manager = AssetManager(IsoFileProvider(path), game)
        models = inspect(rows, manager)
        report["games"][game.name] = {
            "catalog_entries": len(models),
            "models": models,
            "entries_needing_custom_assets": sum(bool(r["missing_from_retail"]) for r in models),
        }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2))
    print(
        json.dumps(
            {
                game: {key: value for key, value in data.items() if key != "models"}
                for game, data in report["games"].items()
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("prime-iso", "echoes-iso", "reference", "echoes-catalog", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    audit(args.prime_iso, args.echoes_iso, args.reference, args.echoes_catalog, args.output)
