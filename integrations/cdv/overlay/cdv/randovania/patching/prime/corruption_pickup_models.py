# User-supplied Corruption disc -> versioned native pickup presentation for GC engines.
# Boundary names here: file_hash, disc_provider, transport_ancs, resource_dependencies,
# validate_cache.
"""User-supplied Corruption disc -> versioned native pickup presentation for GC engines."""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import shutil
import tempfile
from pathlib import Path

import nod
from construct import Container, ListContainer
from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.base_resource import RawResource
from retro_data_structures.formats.ancs import Ancs
from retro_data_structures.formats.meta_transition import MetaTransitionType
from retro_data_structures.formats.txtr import Txtr
from retro_data_structures.game_check import Game

from randovania.patching.prime.corruption_file_provider import NodFileProvider
from randovania.patching.prime.corruption_static_mesh import allocate, convert_mesh, native_templates

CACHE_VERSION = 32
# This cache is the opposite direction from multiworld_models.py: Corruption
# assets become Prime/Echoes-native resources. The key includes the exact source
# image, destination game/ID population, RDS version and this conversion revision.
# A schema or catalog fix must not quietly reuse an older converted payload.
# Model and character IDs from the standalone Corruption pickup catalog.
CATALOG = {
    "Missile": (0x9C5C5246993998A1, 0x308B5A3B94899037),
    "Energy Tank": (0x8F865363AED3AFE6, 0x778E1ABA10D9B9E0),
    "Space Jump Boots": (0x3A2C129709B59A7A, 0xBDDB0771D8E6FF10),
    "Ice Missile": (0x9E6C70ED8E3167BB, 0x552AB78689A0F988),
    "Seeker Missile": (0x954A2A9E6CA491A1, 0x59C5F4A30786C292),
    "Charge Beam": (0xDA171317DB2F1018, 0x59CC7F339B6BBF68),
    "Plasma Beam": (0x0BFD71F11557F941, 0x20A4CDC466D7D399),
    "Nova Beam": (0xBC80CB0D6E368D6C, 0xBD9ED79C3A559383),
    "Grapple Lasso": (0x5B97D697389EB7F6, 0x4384E99AEAAD74F5),
    "Grapple Swing": (0xED59EFA8AE51D07E, 0x6EBECA67A7746FFE),
    "Grapple Voltage": (0xDA7ADFD3B79BA92F, 0x1FB38813C5EBA3FE),
    "Morph Ball Bombs": (0xB76A031C210BA5E9, 0xF0C94C57DF6C679E),
    "Scan Visor": (0xAE573A664052CFFC, 0x78EEE0754E049C65),
    "Combat Visor": (0x76AE9336220563E4, 0xFE1F5CFA256F72C6),
    "Command Visor": (0x1E0EE5BDB118A947, 0x5D4F86DD0EC52CF7),
    "X-Ray Visor": (0x3DCCC3FBD1A3A4E8, 0xF30A209AAA390C01),
    "Screw Attack": (0x4FA417C2C753EA45, 0xCEAF06E20A977B0C),
    "Hazard Shield": (0x3AF42807F0FE5958, 0x267753B8F16FE297),
    "Morph Ball": (0xFCAE1BBDD5539E9B, 0xD7D9FF457E33A937),
    "Boost Ball": (0xBCEB006DA56C6F99, 0x017ADBB0E5F48915),
    "Spider Ball": (0x07DED1554A4348C6, 0xB344A3984594FD3E),
    "Hypermode": (0xA2BD157898333352, 0x1E75BF6DE7531D5E),
    "Hyper Ball": (0x0A229C0BF2B93E3E, 0x6DEE19A2C7BA110B),
    "Hyper Missile": (0x6FF70067566550DA, 0xA5534CB39EE8D90F),
    "Hyper Grapple": (0x12973E2FCB95C7F5, 0xF69C66580F14E646),
    "Ship Grapple": (0x9B7E40D1EDF119E4, 0x4847577B171DC087),
    # Main launcher and expansion have different retail CMDL/CHAR pairs. Keep
    # these identities separate even when required-launcher logic changes the
    # grant; swapping labels here reverses local and cross-world presentation.
    "Ship Missile Expansion": (0x4F21FCF9B0693C90, 0x778810531A3E822A),
    "Ship Missile": (0x79DF78A539413751, 0xA50DCBEF4C7A8E41),
    "Energy Cell": (0x31EF1551AF0D30D8, None),
    "Missile Launcher": (0x892D9A6706521D92, 0x1C51A269A168BA07),
}
# The starting Power Beam has no collectible model in Corruption; retain RDV's fallback.
NO_NATIVE_MODEL = frozenset({"Power Beam"})


def file_hash(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def disc_provider(path):
    disc, is_wii = nod.open_disc_from_image(path)
    part = disc.get_data_partition()
    if not is_wii or part is None or not part.get_header().game_id.startswith(b"RM3"):
        raise ValueError("Select a standalone Metroid Prime 3: Corruption Wii disc (RM3).")
    return NodFileProvider(disc)


def transport_ancs():
    """Unused, dependency-free loader transport. Final actors MUST use static CMDL."""
    raw = Container(
        version=1,
        character_set=Container(version=1, characters=ListContainer()),
        animation_set=Container(
            table_count=1,
            animations=ListContainer(),
            transitions=ListContainer(),
            default_transition=Container(type=MetaTransitionType.Snap, body=Container()),
            additive=None,
            half_transitions=None,
            animation_resources=ListContainer(),
            event_sets=None,
        ),
    )
    return Ancs(raw, Game.PRIME).build()


def resource_dependencies(raw, game):
    """Explicit dependency closure for the supported converted resource families."""
    from retro_data_structures.formats import ancs, format_for
    from retro_data_structures.formats import effect_script as effects

    pairs = []
    # Walk only resource families the conversion actually emits. Parsing one
    # root CMDL/ANCS successfully does not make its referenced animation, event
    # or particle available in the destination PAK.
    if raw.type in ("TXTR", "CINF", "CSKR"):
        return []
    parsed = format_for(raw.type).parse(raw.data, target_game=game)
    if raw.type == "CMDL":
        pairs = [("TXTR", t) for m in parsed.material_sets for t in m.texture_file_ids]
    elif raw.type == "ANCS":
        if game == Game.ECHOES and (
            parsed.animation_set.table_count < 4
            or len(parsed.animation_set.event_sets) != len(parsed.animation_set.animations)
        ):
            raise ValueError("Echoes ANCS must expose an event table for every animation")
        pairs = list(ancs.legacy_dependencies(parsed, game))
    elif raw.type == "ANIM":
        if game == Game.PRIME:
            pairs = [("EVNT", parsed.anim.event_id)]
    elif raw.type == "EVNT":
        pairs = [(e.particle.type, e.particle.id) for e in parsed.particle_poi_nodes]
    elif raw.type in ("PART", "ELSC", "SWHC"):
        cls = {"PART": effects.Part, "ELSC": effects.Elsc, "SWHC": effects.Swhc}[raw.type]
        reference_types = {
            "SSWH": "SWHC",
            "PMDL": "CMDL",
            "SELC": "ELSC",
            "IDTS": "PART",
            "ICTS": "PART",
            "IITS": "PART",
            "GPSM": "PART",
            "EPSM": "PART",
        }
        for element in parsed.elements:
            if element.type in cls.texture_keys() and element.body.body is not None:
                pairs.append(("TXTR", element.body.body.id))
            elif element.type in cls.asset_id_keys() and element.body.body is not None:
                pairs.append((reference_types[element.type], element.body.body))
            elif element.type in cls.spawn_system_keys() and element.body.magic != "NONE":
                for spawn in element.body.value.spawns:
                    pairs.extend(("PART" if game == Game.PRIME else t.type, t.id) for t in spawn.v2)
    else:
        raise ValueError("Unsupported converted resource family")
    return [
        {"id": identity, "type": kind}
        for kind, identity in sorted(set(pairs))
        if identity is not None and identity not in (0, 0xFFFFFFFF)
    ]


def validate_cache(directory, identity):
    # Metadata is only the index. Verify type/ID relationships, dependency
    # closure and every payload hash before accepting it as reusable output.
    try:
        meta = json.loads((directory / "meta.json").read_text())
        if meta["identity"] != identity or set(meta["items"]) != {"prime3_" + n for n in CATALOG}:
            return None
        game = Game[identity["target_game"]]
        assets = {a["new_id"]: a for a in meta["new_assets"]}
        if len(assets) != len(meta["new_assets"]):
            return None
        wrapper = allocate("ANCS", 0x434F5252555054, game, set()) if game == Game.PRIME else 0xFFFFFFFF
        if game == Game.PRIME and assets.get(wrapper, {}).get("type") != "ANCS":
            return None
        native = identity.get("presentation") == "native-animated-v2"
        for name, (model, character) in CATALOG.items():
            item = meta["items"]["prime3_" + name]
            model_id = allocate("CMDL", model, game, set())
            animated = native and character is not None
            expected_ancs = allocate("ANCS", character, game, set()) if animated else wrapper
            expected = {"cmdl": model_id, "ancs": expected_ancs, "character": 0, "scale": 1.5}
            if native:
                expected["animated"] = animated
            if item != expected:
                return None
            if animated and assets.get(expected_ancs, {}).get("type") != "ANCS":
                return None
            if assets[model_id]["type"] != "CMDL" or assets[model_id]["old_id"] != model:
                return None
        for row in assets.values():
            if row["type"] not in ("CMDL", "TXTR", "ANCS", "CINF", "CSKR", "ANIM", "EVNT", "PART", "ELSC", "SWHC"):
                return None
            for dep in row["dependencies"]:
                if dep["id"] not in assets or assets[dep["id"]]["type"] != dep["type"]:
                    return None
        for name, digest in meta["files"].items():
            if Path(name).name != name or file_hash(directory / name) != digest:
                return None
        required = {f"{a['new_id']}.{a['type']}" for a in meta["new_assets"]}
        if required != set(meta["files"]):
            return None
        return meta
    except (OSError, ValueError, KeyError, TypeError):
        return None


def convert_pickups(source_iso, target_provider, game, cache_dir, progress):
    if game not in (Game.PRIME, Game.ECHOES):
        raise ValueError("Expected GameCube Prime or Echoes")
    cache = cache_dir.resolve()
    if cache == source_iso.resolve():
        raise ValueError("Asset cache must be separate from the source ISO")
    target_root = getattr(target_provider, "root", None)
    if target_root is not None:
        target_root = target_root.resolve()
        if cache.is_relative_to(target_root) or target_root.is_relative_to(cache):
            raise ValueError("Asset cache must be disjoint from the target extraction")
    provider = disc_provider(source_iso)
    source = AssetManager(provider, Game.CORRUPTION)
    target = AssetManager(target_provider, game)
    occupied = set(target.all_asset_ids())
    identity = {
        "version": CACHE_VERSION,
        "presentation": "native-animated-v2",
        "rds": importlib.metadata.version("retro-data-structures"),
        "source_sha256": file_hash(source_iso),
        "target_game": game.name,
        "target_asset_ids_sha256": hashlib.sha256(json.dumps(sorted(occupied)).encode()).hexdigest(),
    }
    # Destination occupancy affects allocated IDs. A cache from another target
    # extraction can collide even with the same Corruption disc and settings.
    existing = validate_cache(cache_dir, identity)
    if existing is not None:
        progress("Using verified Corruption pickup model cache", 1.0)
        return existing
    cache_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="corruption-models-", dir=cache_dir.parent) as temporary:
        output = Path(temporary)
        resources = {}
        metadata = {}
        model_ids = {}
        texture_ids = {}
        new_assets = []
        source_resources = {}
        wrapper = allocate("ANCS", 0x434F5252555054, game, occupied) if game == Game.PRIME else 0xFFFFFFFF
        if game == Game.PRIME:
            resources[wrapper] = RawResource("ANCS", transport_ancs())
            new_assets.append({"old_id": None, "new_id": wrapper, "type": "ANCS", "dependencies": []})
        for i, (name, (model, char)) in enumerate(CATALOG.items()):
            progress("Converting Corruption " + name, i / (2 * len(CATALOG)))
            if char is not None and source.get_parsed_asset(char)._raw.model_id != model:
                raise ValueError("Corruption catalog character/model association changed: " + name)
            mesh = source.get_parsed_asset(model)._raw
            textures = list(
                dict.fromkeys(
                    e.body.id for m in mesh.material_sets[0].materials for e in m.elements if e.type == "PASS"
                )
            )
            for old in textures:
                if old in texture_ids:
                    continue
                raw = source.get_raw_asset(old)
                if raw.type != "TXTR":
                    raise ValueError("Expected TXTR")
                Txtr.parse(raw.data, Game.CORRUPTION)
                Txtr.parse(raw.data, game)
                new = allocate("TXTR", old, game, occupied)
                texture_ids[old] = new
                resources[new] = raw
                new_assets.append({"old_id": old, "new_id": new, "type": "TXTR", "dependencies": []})
                source_resources[f"{old:016X}"] = hashlib.sha256(raw.data).hexdigest()
            new = allocate("CMDL", model, game, occupied)
            model_ids[model] = new
            profile = {0x8F865363AED3AFE6: "energy-tank", 0x6FF70067566550DA: "hyper-missile"}.get(model, "catalog")
            data = convert_mesh(mesh, native_templates(), game, {old: texture_ids[old] for old in textures}, profile)
            resources[new] = RawResource("CMDL", data)
            deps = [{"id": texture_ids[old], "type": "TXTR"} for old in textures]
            new_assets.append({"old_id": model, "new_id": new, "type": "CMDL", "dependencies": deps})
            source_resources[f"{model:016X}"] = hashlib.sha256(source.get_raw_asset(model).data).hexdigest()
            metadata["prime3_" + name] = {"cmdl": new, "ancs": wrapper, "character": 0, "scale": 1.5}
        from randovania.patching.prime.corruption_character import convert as convert_character
        from randovania.patching.prime.corruption_particles import ParticleConverter

        particles = ParticleConverter(source, game, occupied.copy(), {**texture_ids, **model_ids})
        occupied_by_static = occupied.copy()
        character_source_ids = {}
        for i, (name, (model, character)) in enumerate(CATALOG.items()):
            # Start from converted meshes/textures, then replace character-backed
            # entries with native animated rigs. Energy Cell has no CHAR and
            # retains its static path; do not invent a source animation for it.
            item = metadata["prime3_" + name]
            item["animated"] = character is not None
            if character is None:
                continue
            progress("Converting Corruption animation and effects: " + name, 0.5 + i / (2 * len(CATALOG)))
            mesh = source.get_parsed_asset(model).raw
            used = {e.body.id for m in mesh.material_sets[0].materials for e in m.elements if e.type == "PASS"}
            ids, converted = convert_character(
                source,
                None,
                model,
                character,
                {t: texture_ids[t] for t in used},
                game,
                occupied_by_static.copy(),
                particles=particles,
            )
            item["ancs"] = ids["ANCS"]
            source_character = source.get_parsed_asset(character).raw
            animation_source = next(
                a.anim_id
                for a in source_character.animation_aabb_array
                if allocate("ANIM", a.anim_id, game, set()) == ids["ANIM"]
            )
            character_source_ids.update(
                {
                    ids["ANCS"]: character,
                    ids["CINF"]: source_character.skeleton_id,
                    ids["CSKR"]: source_character.skin_id,
                    ids["ANIM"]: animation_source,
                }
            )
            for new_id, (kind, payload) in converted.items():
                resource = RawResource(kind, payload)
                if new_id in resources and kind != "CMDL" and resources[new_id] != resource:
                    raise ValueError("Converted character resource collision")
                resources[new_id] = resource
        for new_id, (kind, payload) in particles.resources.items():
            resource = RawResource(kind, payload)
            if new_id in resources and resources[new_id] != resource:
                raise ValueError("Converted particle resource collision")
            resources[new_id] = resource
        old_ids = {row["new_id"]: row["old_id"] for row in new_assets}
        old_ids.update(character_source_ids)
        old_ids.update({new_id: old for old, new_id in particles.mapping.items()})
        new_assets = [
            {
                "old_id": old_ids.get(asset_id),
                "new_id": asset_id,
                "type": raw.type,
                "dependencies": resource_dependencies(raw, game),
            }
            for asset_id, raw in resources.items()
        ]
        for old_id in set(old_ids.values()) - {None}:
            source_resources[f"{old_id:016X}"] = hashlib.sha256(source.get_raw_asset(old_id).data).hexdigest()
        for asset_id, raw in resources.items():
            (output / f"{asset_id}.{raw.type}").write_bytes(raw.data)
        meta = {
            "version": CACHE_VERSION,
            "identity": identity,
            "items": metadata,
            "new_assets": new_assets,
            "source_resources": source_resources,
            "static_models": False,
            "animated_models": [name for name, item in metadata.items() if item["animated"]],
            "effect_approximations": particles.approximations,
            "requires_static_actor_pass": game == Game.PRIME,
            "no_native_model": sorted(NO_NATIVE_MODEL),
            "limitations": [
                # These are conversion approximations to report, not evidence
                # of exact Wii rendering in the GC engine. RDS round trips and
                # complete dependencies still need visual/gameplay acceptance.
                "Rigid source animation resampled at 60 Hz into native retail animation format",
                "Unsupported Wii particle operations omitted; constant atlas phases retained, random sprite phases sampled",
                "Native GX reflection/reflectivity approximation; Wii bloom and X-ray shader passes omitted",
                "Unit-scale translation-only Wii SRT lowered to native scroll; other SRT transforms remain unsupported",
            ],
            "files": {p.name: file_hash(p) for p in output.iterdir()},
        }
        (output / "meta.json").write_text(json.dumps(meta, indent=2))
        if file_hash(source_iso) != identity["source_sha256"]:
            raise ValueError("Source ISO changed")
        if validate_cache(output, identity) is None:
            raise ValueError("Generated asset cache failed verification")
        # Only this feature's dedicated cache is replaced, after conversion succeeds.
        if cache_dir.exists():
            shutil.rmtree(cache_dir)
        shutil.copytree(output, cache_dir)
    progress("Finished converting Corruption pickup models", 1.0)
    return meta


def merge_prime_assets(directories, output):
    """Combine Echoes and Corruption resources without replacing either source cache."""
    if any(output.resolve().is_relative_to(directory.resolve()) for directory in directories):
        raise ValueError("Merged output must be disjoint from asset caches")
    output.mkdir(parents=True, exist_ok=False)
    combined = {"items": {}, "new_assets": []}
    seen = set()
    for directory in directories:
        # The merged directory serves randomprime, not either source cache.
        # Reject duplicate names/IDs instead of letting copy order choose which
        # game's payload wins under a shared resource name.
        meta = json.loads((directory / "meta.json").read_text())
        if set(combined["items"]) & set(meta["items"]):
            raise ValueError("Duplicate external model name")
        combined["items"].update(meta["items"])
        for row in meta["new_assets"]:
            asset_id = row["new_id"]
            if asset_id in seen:
                raise ValueError("External resource ID collision")
            seen.add(asset_id)
            combined["new_assets"].append(row)
            name = f"{asset_id}.{row['type']}"
            shutil.copyfile(directory / name, output / name)
    # randomprime 1.33 matches decimal IDs by substring; reject ambiguous directories.
    filenames = sorted(p.name for p in output.iterdir())
    for row in combined["new_assets"]:
        expected = f"{row['new_id']}.{row['type']}"
        if next((name for name in filenames if str(row["new_id"]) in name), None) != expected:
            raise ValueError("Ambiguous external resource filename for randomprime")
    (output / "meta.json").write_text(json.dumps(combined, indent=2))
    return combined


def install_echoes_models(contents, cache_dir, metadata, randomizer_data, progress):
    """Install static ModelData entries and assets in each gameplay PAK, like Prime imports."""
    from retro_data_structures.formats.pak import Pak

    by_id = {r["new_id"]: r for r in metadata["new_assets"]}

    def item_assets(item):
        # Echoes ModelData needs the transitive closure rooted at CMDL/ANCS.
        # Registering only the mesh can leave the skin, animation or particles
        # absent when this pickup is streamed in a different gameplay PAK.
        seen = set()
        stack = [item["cmdl"], item["ancs"]]
        while stack:
            identity = stack.pop()
            if identity == 0xFFFFFFFF or identity in seen:
                continue
            seen.add(identity)
            row = by_id[identity]
            stack.extend(d["id"] for d in row["dependencies"])
        return [{"AssetID": identity, "Type": by_id[identity]["type"]} for identity in sorted(seen)]

    for name, item in metadata["items"].items():
        randomizer_data["ModelData"].append(
            {
                "Index": len(randomizer_data["ModelData"]),
                "Name": name,
                "Model": item["cmdl"],
                "ScanModel": 0xFFFFFFFF,
                "AnimSet": item["ancs"],
                "Character": 0,
                "DefaultAnim": 0,
                "Rotation": [0.0, 0.0, 0.0],
                "Scale": [item["scale"]] * 3,
                "OrbitOffset": [0.0, 0.0, 0.0],
                "Lighting": {"CastShadow": True, "UnknownBool1": True, "UseWorldLighting": 1, "UnknownBool2": False},
                "Assets": item_assets(item),
            }
        )
    resources = {
        r["new_id"]: RawResource(r["type"], (cache_dir / f"{r['new_id']}.{r['type']}").read_bytes())
        for r in metadata["new_assets"]
    }
    for i in range(1, 6):
        path = contents / "files" / f"Metroid{i}.pak"
        pak = Pak.parse(path.read_bytes(), Game.ECHOES)
        old = dict(pak.get_all_assets())
        if set(old) & set(resources):
            raise ValueError("Corruption resource ID collision")
        for identity, raw in resources.items():
            pak.add_asset(identity, raw)
        encoded = pak.build()
        check = Pak.parse(encoded, Game.ECHOES)
        for identity, raw in old.items():
            actual = check.get_asset(identity)
            if actual.type != raw.type or actual.data != raw.data:
                raise ValueError("Unrelated Echoes resource changed")
        path.write_bytes(encoded)
        progress("Installed Corruption models in " + path.name, i / 5)


def publish_echoes_image(contents, output, progress):
    """Keep an existing export intact until packing and payload validation succeed."""
    from randovania.patching.patchers.gamecube.iso_packager import pack_iso
    from randovania.patching.prime.corruption_file_provider import IsoFileProvider, PathFileProvider

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="corruption-publish-", dir=output.parent) as temporary:
        # NOD closes and reopens this file while packing. A library scanner can
        # claim a new .iso between those opens and block the next Windows write.
        # Publish the game-image extension only after packing and readback pass.
        image = Path(temporary) / "complete.tmp"
        pack_iso(image, contents, lambda s, p: progress(s, p * 0.9))
        actual, expected = IsoFileProvider(image), PathFileProvider(contents)
        if actual.get_dol() != expected.get_dol():
            raise ValueError("Packed DOL differs from staging")
        if set(actual.get_file_list()) != set(expected.get_file_list()):
            raise ValueError("Packed file inventory differs from staging")
        for name in expected.get_file_list():
            a, b = actual.read_binary(name), expected.read_binary(name)
            if a[: len(b)] != b or a[len(b) :] != b"\xff" * ((-len(b)) % 32):
                raise ValueError("Packed payload differs from staging: " + name)
        image.replace(output)
    progress("Finished packing ISO", 1.0)
