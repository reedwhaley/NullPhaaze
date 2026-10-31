# Choose foreign visuals from the serialized model identity and validated cache. Replace
# only audited actor slots, add the correct loading dependencies and read the rebuilt seed
# resources back. Boundary names here: normalized_name, digest, install_cache, ModelCache,
# visual_bindings.
"""Apply locally cached, validated foreign visuals without changing game grants."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import struct
from pathlib import Path

from construct import Container
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.rules import catalog, recipe
from retro_data_structures.game_check import Game

from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
from nullphaze_network.prime3_lua_service.probe import properties, replace_properties

RENDERER = "corruption-opaque-emission-model-matched-v1"
VISUAL_FIELDS = {0xC27FFA8F: "CMDL", 0xA244C9D8: "CHAR", 0xA3D63F44: "CHAR"}
# These are the audited visual slots in core recipes, not a search for every
# CMDL/CHAR-looking value in a room. Fake pickups can share a location's visual
# through another actor or area, so the binding must include all recipe targets.


def normalized_name(name):
    return "".join(c for c in name.removesuffix(" INCOMPLETE").casefold() if c.isalnum())


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def install_cache(gallery: Path, output: Path, converted_assets: Path) -> dict:
    """Import a user's accepted assets; never distribute retail payloads in code."""
    acceptance = json.loads((gallery / "human-full-gallery-acceptance.json").read_text())
    build = json.loads((gallery / "build.json").read_text())
    manifest = json.loads((gallery / "converted-assets.json").read_text())
    if (
        acceptance.get("full_catalog_visual_acceptance") is not True
        or acceptance["image_sha256"] != build["image_sha256"]
        or manifest.get("effect_scale_policy") != "model_matched"
        or manifest["entry_count"] != 93
        or not manifest["zero_omissions"]
    ):
        raise ValueError("A complete accepted model-matched gallery is required")
    if digest(gallery / "image/RM3E01.wbfs") != acceptance["image_sha256"]:
        raise ValueError("Accepted gallery image changed")
    # The accepted PAK, not a mutable intermediate directory, is authoritative.
    archive = Archive(gallery / "image/DATA/files/Metroid1.pak")
    by_id = {r.identity: r for r in archive.resources}
    expected = {int(p.stem, 16): p.suffix[1:] for p in converted_assets.iterdir()}
    if len(expected) != 770:
        raise ValueError("Accepted asset inventory is incomplete")
    output.mkdir(parents=True, exist_ok=False)
    assets = output / "assets"
    assets.mkdir()
    hashes = {}
    for identity, kind in expected.items():
        resource = by_id[identity]
        if resource.kind.decode() != kind:
            raise ValueError("Accepted resource kind mismatch")
        if resource.read() != (converted_assets / f"{identity:016x}.{kind}").read_bytes():
            raise ValueError("Converted input differs from accepted gallery resource")
        path = assets / f"{identity:016x}.{kind}"
        path.write_bytes(resource.read())
        hashes[path.name] = digest(path)
    result = {
        "renderer": RENDERER,
        "entries": manifest["entries"],
        "files": hashes,
        "accepted_image_sha256": acceptance["image_sha256"],
        "local_user_assets_only": True,
    }
    (output / "models.json").write_text(json.dumps(result, indent=2))
    return result


class ModelCache:
    def __init__(self, root: Path):
        self.root = root.resolve()
        try:
            self.manifest = json.loads((self.root / "models.json").read_text())
        except FileNotFoundError as error:
            raise ValueError(
                f"Foreign Corruption models are required. Prepare the local model cache at {root}; "
                "Scan Visor substitution is not allowed."
            ) from error
        games = set(self.manifest.get('games', ['Prime', 'Echoes']))
        # I allow only the recorded Echoes-only fallback set below. A missing
        # cache entry elsewhere is an export error, not permission to show Scan
        # Visor and make an incomplete import look successful.
        fallbacks = self.manifest.get('native_fallbacks', [])
        allowed_fallbacks = {'PowerBeam INCOMPLETE', 'CombatVisor INCOMPLETE', 'MorphBall INCOMPLETE'}
        if fallbacks and (games != {'Echoes'} or set(fallbacks) != allowed_fallbacks):
            raise ValueError('Invalid native model fallback policy')
        expected_count = (47 if 'Prime' in games else 0) + (46 if 'Echoes' in games else 0) - len(fallbacks)
        if (not games or not games <= {'Prime', 'Echoes'} or self.manifest["renderer"] != RENDERER
                or len(self.manifest["entries"]) != expected_count):
            raise ValueError("Unsupported Corruption model cache renderer")
        self.resources = {}
        for name, expected in self.manifest["files"].items():
            if Path(name).name != name or len(name.split(".")) != 2:
                raise ValueError("Invalid model cache resource path")
            path = self.root / "assets" / name
            if not path.is_file() or path.is_symlink() or digest(path) != expected:
                raise ValueError(f"Model cache resource changed: {name}")
            identity, kind = name.split(".")
            identity = int(identity, 16)
            if identity in self.resources:
                raise ValueError("Repeated model cache identity")
            self.resources[identity] = Resource(identity, kind.encode(), False, 0).updated(path.read_bytes())
        self.entries = {
            # Key by source game and normalized catalog name together. A Prime
            # and Echoes item with the same text can require different assets.
            ({"Prime": "prime1", "Echoes": "prime2"}[r["game"]], normalized_name(r["name"])): r
            for r in self.manifest["entries"]
        }
        actual_games = {r['game'] for r in self.manifest['entries']}
        if (actual_games != games or len(self.entries) != expected_count
                or (expected_count == 93 and len(self.resources) != 770)
                or not self.resources):
            raise ValueError("Incomplete or repeated model cache inventory")
        self.native_fallbacks = {('prime2', normalized_name(name)) for name in fallbacks}
        for entry in self.entries.values():
            if set(entry["native"]) != {"CMDL", "CSKR", "CINF", "CHAR", "SAND", "ANIM"}:
                raise ValueError("Incomplete imported model rig")
            for kind, identity in entry["native"].items():
                resource = self.resources.get(int(identity, 16))
                if resource is None or resource.kind.decode() != kind:
                    raise ValueError("Imported model rig dependency missing")

    def entry(self, row):
        key = row["game"], normalized_name(row["name"])
        # Prime's catalog uses Missile for its expansion model.
        if key == ("prime1", "missileexpansion"):
            key = "prime1", "missile"
        try:
            return self.entries[key]
        except KeyError as error:
            raise ValueError(f"No validated Corruption model for {key}; no silent placeholder is permitted") from error

    def dependencies(self, entry):
        # Keep this entry's complete native rig plus the accepted shared PART/
        # TXTR pool. This is intentionally broader than its six direct IDs:
        # dropping a shared effect/texture can pass mesh lookup and fail loading.
        own = {int(value, 16) for value in entry["native"].values()}
        return [r for identity, r in self.resources.items() if identity in own or r.kind in (b"PART", b"TXTR")]


def visual_bindings(plan):
    """Use audited core recipe targets, including aliases in other rooms."""
    data = catalog()
    result = {}
    for row in plan:
        if row["game"] == "prime3":
            continue
        index = row["index"]
        recipes = [recipe(data["pickupRecipes"][index][0][0])]
        # Read model-bearing targets from the established recipe catalog. Do
        # not assume the pickup actor itself owns every displayed model, or
        # that there is only one representation of a location in the world.
        recipes += [
            recipe(data["fakeRecipes"][i][0])
            for i, alias in enumerate(data["fakePickups"])
            if alias["item_index"] == index
        ]
        for rules in recipes:
            for operation in rules["object_modification_patches"]:
                fields = {
                    int.from_bytes(p["property_id"], "big") for p in operation["property_modifications"]
                } & VISUAL_FIELDS.keys()
                if not fields:
                    continue
                for area in operation["mrea_ids"]:
                    for layer in operation["layer_indexes"]:
                        for instance in operation["object_ids"]:
                            key = area, layer, instance
                            if key in result and result[key][0] != row:
                                raise ValueError("Conflicting pickup visual bindings")
                            old = result.get(key, (row, set()))[1]
                            result[key] = row, old | fields
    return result


def patch_area(raw, area_id, bindings, cache):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    originals = {int(o.id): copy.deepcopy(o._raw) for layer in layers for o in layer.instances}
    added, changed = {}, []
    for (identity, layer_index, instance), (row, fields) in bindings.items():
        if identity != area_id:
            continue
        matches = [o for o in layers[layer_index].instances if o.id.instance == instance]
        if len(matches) != 1:
            raise ValueError("Missing or ambiguous randomized visual actor")
        actor = matches[0]
        old_fields = dict(properties(actor._raw.base_property))
        entry = cache.entry(row)
        values = {}
        # Core recipes list alternative character properties for PCKP/ACTR/PLAT.
        # Apply only the slots actually serialized by this audited actor type.
        fields = fields & old_fields.keys()
        if not fields:
            raise ValueError(
                f"No model slot on audited actor {actor.type_name}/{int(actor.id):08x} for location {row['index']}"
            )
        for field in fields:
            value = int(entry["native"][VISUAL_FIELDS[field]], 16)
            values[field] = struct.pack(">Q", value) if VISUAL_FIELDS[field] == "CMDL" else struct.pack(">QI", value, 0)
            if len(values[field]) != len(old_fields[field]):
                raise ValueError("Unreviewed visual field layout")
        actor._raw.base_property = replace_properties(actor._raw.base_property, values)
        # An asset existing in the PAK is not enough: the loading layer needs
        # its dependency entries as well. Insert at this layer's end and shift
        # every following boundary so unrelated layers retain their slices.
        for resource in cache.dependencies(entry):
            added[resource.identity] = resource
        deps = area.get_section("dependencies_section")[0]
        existing = {d.asset_id for d in deps.dependencies[deps.offsets[layer_index] : deps.offsets[layer_index + 1]]}
        additions = [
            Container(asset_id=r.identity, type=r.kind.decode())
            for r in cache.dependencies(entry)
            if r.identity not in existing
        ]
        offset = deps.offsets[layer_index + 1]
        deps.dependencies[offset:offset] = additions
        for i in range(layer_index + 1, len(deps.offsets)):
            deps.offsets[i] += len(additions)
        layers[layer_index].mark_modified()
        changed.append(
            {
                "location": row["index"],
                "actor": int(actor.id),
                "game": row["game"],
                "model": row["name"],
                "fields": sorted(fields),
            }
        )
    encoded = area.build()
    checked = SeedMrea.parse(encoded, Game.CORRUPTION)
    modified = {r["actor"]: r for r in changed}
    # Read the rebuilt room back and undo only our visual fields for comparison.
    # Everything else must match the seeded actor, including grant properties,
    # connections and transforms. A correct-looking mesh is not that proof.
    for layer in checked.script_layers:
        for actor in layer.instances:
            expected = copy.deepcopy(actor._raw)
            if int(actor.id) in modified:
                old = dict(properties(originals[int(actor.id)].base_property))
                expected.base_property = replace_properties(
                    expected.base_property, {f: old[f] for f in modified[int(actor.id)]["fields"]}
                )
            if expected != originals[int(actor.id)]:
                raise ValueError("Model patch changed grants, callbacks, transforms or unrelated fields")
    return encoded, list(added.values()), changed


def presentation_plan(plan, enabled_games, cache=None):
    """Select visuals only; never rewrite serialized pickups or recipient data."""
    enabled = {'prime1', 'prime2'} if enabled_games is None else set(enabled_games)
    if not enabled <= {'prime1', 'prime2'}:
        raise ValueError('Unknown imported model game')
    result = []
    for row in plan:
        # This projection affects only the model stage. Marking a row prime3
        # means retain the existing native visual; it does not retarget the item
        # to the local player or replace its serialized acquisition behavior.
        use_model = row['game'] in enabled
        if use_model and cache is not None and (row['game'], normalized_name(row['name'])) in cache.native_fallbacks:
            use_model = False
        result.append(dict(row) if use_model else dict(row, game='prime3'))
    return result


def patch_archives(source: Path, output: Path, plan: list[dict], cache_path: Path, *, enabled_games=None):
    # Run against post-core, randomized PAKs. Restoring a retail room to obtain
    # a convenient model slot would also restore its old pickup/actor graph.
    if [r["index"] for r in plan] != list(range(100)):
        raise ValueError("Model placement requires all 100 locations")
    projected = presentation_plan(plan, enabled_games)
    if not any(r["game"] != "prime3" for r in projected):
        return {"foreign_locations": 0, "archives": {}, "actors": 0,
                'native_fallback_locations': sum(r['game'] != 'prime3' for r in plan)}
    cache = ModelCache(cache_path)
    projected = presentation_plan(plan, enabled_games, cache)
    for row in projected:
        if row["game"] != "prime3":
            cache.entry(row)
    bindings = visual_bindings(projected)
    output.mkdir(parents=True, exist_ok=False)
    remaining = {key[0] for key in bindings}
    target_areas = set(remaining)
    report = {
        "foreign_locations": sum(r["game"] != "prime3" for r in plan),
        "archives": {},
        "actors": 0,
        "renderer": RENDERER,
        'native_fallback_locations': sum(a['game'] != 'prime3' and b['game'] == 'prime3'
                                         for a, b in zip(plan, projected, strict=True)),
    }
    for path in sorted(source.glob("*.pak")):
        archive = Archive(path)
        areas = {r.identity for r in archive.resources if r.kind == b"MREA"} & target_areas
        if not areas:
            continue
        resources, additions, changes = [], {}, []
        originals = {r.identity: r for r in archive.resources}
        for resource in archive.resources:
            if resource.identity in areas:
                raw, added, changed = patch_area(resource.read(), resource.identity, bindings, cache)
                resources.append(resource.updated(raw))
                additions.update({r.identity: r for r in added})
                changes.extend(changed)
            else:
                resources.append(resource)
        for identity, resource in additions.items():
            # Equal IDs may reuse exactly equal payloads. A different payload
            # under an occupied seed ID is a collision, not an overwrite option.
            if identity in originals:
                if originals[identity].kind != resource.kind or originals[identity].read() != resource.read():
                    raise ValueError("Imported model resource collides with seed resource")
            else:
                resources.append(resource)
        destination = output / path.name
        archive.write(destination, resources)
        actual = {r.identity: r for r in Archive(destination).resources}
        if set(actual) != {r.identity for r in resources}:
            raise ValueError("Model archive resource population mismatch")
        for resource in resources:
            if actual[resource.identity].kind != resource.kind or actual[resource.identity].read() != resource.read():
                raise ValueError("Model archive readback mismatch")
        remaining -= areas
        report["archives"][path.name] = changes
        report["actors"] += len(changes)
    if remaining:
        raise ValueError(f"Missing randomized model areas: {sorted(remaining)}")
    replaced = {record["location"] for records in report["archives"].values() for record in records}
    report["scripted_rewards_without_model_slots"] = [
        # Record rewards whose acquisition sequence has no audited model target.
        # I do not add a collectible actor to force a visual into a cutscene.
        r["index"] for r in plan if r["game"] != "prime3" and r["index"] not in replaced
    ]
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Install user-owned, accepted Corruption model assets locally")
    parser.add_argument("--accepted-gallery", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--converted-assets", required=True, type=Path)
    args = parser.parse_args()
    result = install_cache(args.accepted_gallery.resolve(), args.output.resolve(), args.converted_assets.resolve())
    print(
        json.dumps(
            {"renderer": result["renderer"], "models": len(result["entries"]), "resources": len(result["files"])}
        )
    )
