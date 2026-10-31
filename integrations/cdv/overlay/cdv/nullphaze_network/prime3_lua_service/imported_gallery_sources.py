# Private, read-only source overlays for the cross-game model gallery. Boundary names here:
# file_hash, snapshot_cache, add_raw, sources, audit.
"""Private, read-only source overlays for the cross-game model gallery."""

import copy
import hashlib
import json
import shutil
import zlib

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.base_resource import RawResource
from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.conversion.conversions import converter_for
from retro_data_structures.file_provider import IsoFileProvider
from retro_data_structures.formats import format_for
from retro_data_structures.game_check import Game

from nullphaze_network.prime3_lua_service.imported_gallery_catalog import echoes_models, prime_models

SUPPORTED = {"ANCS", "ANIM", "CMDL", "CINF", "CSKR", "EVNT", "TXTR", "PART"}


def file_hash(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def snapshot_cache(source, output):
    """Require a complete stable cache before using any exported payloads."""
    metadata = json.loads((source / "meta.json").read_text())
    expected = ["meta.json"] + [f"{row['new_id']}.{row['type']}" for row in metadata["new_assets"]]
    if output.exists():
        raise ValueError("Use a new private cache snapshot")
    output.mkdir(parents=True)
    hashes = {}
    for name in expected:
        src, dst = source / name, output / name
        before = file_hash(src)
        shutil.copyfile(src, dst)
        if file_hash(src) != before or file_hash(dst) != before:
            raise ValueError(f"RDV cache changed during snapshot: {name}")
        hashes[name] = before
    (output / "snapshot-hashes.json").write_text(json.dumps(hashes, indent=2))
    return metadata


def add_raw(manager, identity, kind, raw):
    data = RawResource(kind, raw)
    if manager.does_asset_exists(identity):
        manager.replace_asset(identity, data)
    else:
        name = f"gallery-source-{identity:08x}"
        manager.register_custom_asset_name(name, identity)
        if manager.add_new_asset(name, data) != identity:
            raise ValueError("Source overlay identity changed")


def sources(prime_iso, echoes_iso, custom, cache, reference, echoes_catalog):
    prime = AssetManager(IsoFileProvider(prime_iso), Game.PRIME)
    for path in custom.iterdir():
        kind = path.suffix[1:]
        if kind not in SUPPORTED:
            continue
        raw = path.read_bytes()
        if len(raw) > 6 and raw[4] == 0x78:
            try:
                decoded = zlib.decompress(raw[4:])
            except zlib.error:
                pass
            else:
                if len(decoded) != int.from_bytes(raw[:4], "big"):
                    raise ValueError("Compressed asset length mismatch")
                raw = decoded
        add_raw(prime, int(path.stem, 16), kind, raw)
    metadata = json.loads((cache / "meta.json").read_text())
    for row in metadata["new_assets"]:
        kind, identity = row["type"], row["new_id"]
        if kind not in SUPPORTED:
            raise ValueError(f"Unaudited RDV cache dependency type: {kind}")
        add_raw(prime, identity, kind, (cache / f"{identity}.{kind}").read_bytes())
    rows = [dict(row, game="Prime") for row in prime_models(reference)]
    echoes = AssetManager(IsoFileProvider(echoes_iso), Game.ECHOES)
    next_id = 0xFFFE0000

    def generate_id(_):
        nonlocal next_id
        result = next_id
        next_id += 1
        return result

    converter = AssetConverter(Game.PRIME, {Game.ECHOES: echoes}, generate_id, converter_for)
    gamecube = next(row for row in rows if row["name"] == "RandovaniaGamecube")
    for original in echoes_models(echoes_catalog):
        row = dict(original, game="Echoes")
        cached = metadata["items"].get("prime2_" + row["name"])
        if cached:
            row.update(model=cached["cmdl"], ancs=cached["ancs"], character=cached["character"])
            row["provenance"] = "RDV exported model cache"
        elif row["model"] == 0xFFFFFFFF:
            row.update(
                model=gamecube["model"],
                ancs=gamecube["ancs"],
                character=0,
                provenance="RDV Gamecube placeholder for absent source model",
            )
        else:
            row["model"] = converter.convert_id(row["model"], Game.ECHOES)
            row["provenance"] = "Retail static model via RDV's RDS conversion backend"
        rows.append(row)
    for asset in converter.converted_assets.values():
        raw = format_for(asset.type).build(asset.resource, target_game=Game.PRIME)
        add_raw(prime, asset.id, asset.type, raw)
    for row in rows:
        if row["ancs"] != 0xFFFFFFFF:
            if prime.get_asset_type(row["ancs"]) != "ANCS":
                candidates = []
                for path in custom.glob("*.ANCS"):
                    identity = int(path.stem, 16)
                    chars = prime.get_parsed_asset(identity)._raw.character_set.characters
                    if row["character"] < len(chars) and chars[row["character"]].model_id == row["model"]:
                        candidates.append(identity)
                if len(candidates) != 1:
                    raise ValueError(f"Ambiguous backend-version ANCS mapping for {row['name']}: {candidates}")
                row["catalog_ancs_before_backend_resolution"] = row["ancs"]
                row["ancs"] = candidates[0]
            ancs = prime.get_parsed_asset(row["ancs"])._raw
            if "character_set" not in ancs:
                raise ValueError(f"Invalid ANCS overlay: {row['game']} {row['name']} {row['ancs']:08x}: {list(ancs)}")
            character = ancs.character_set.characters[row["character"]]
            row["catalog_model"] = row["model"]
            row["model"] = character.model_id
            row["skin"] = character.skin_id
            row["skeleton"] = character.skeleton_id
        if not prime.does_asset_exists(row["model"]):
            raise ValueError(f"Missing gallery model: {row['game']} {row['name']}")
    return prime, rows


def audit(manager, rows):
    result = []
    for row in rows:
        record = copy.deepcopy(row)
        model = manager.get_parsed_asset(row["model"])._raw
        record.update(
            surfaces=len(model.surfaces),
            vertices=len(model.attrib_arrays.positions),
            material_texture_counts=[len(material.texture_indices) for material in model.material_sets[0].materials],
        )
        if row.get("skin", 0xFFFFFFFF) != 0xFFFFFFFF:
            skin = manager.get_parsed_asset(row["skin"])._raw
            record["skin_groups"] = len(skin.vertex_groups)
            record["max_weights"] = max(len(group.weights_array) for group in skin.vertex_groups)
        result.append(record)
    return result
