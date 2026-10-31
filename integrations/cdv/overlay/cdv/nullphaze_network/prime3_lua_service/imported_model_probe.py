# Isolated Prime Ice Beam mesh/texture proof; no production model importer. Boundary names
# here: asset_id, convert_model, patch_area, build.
"""Isolated Prime Ice Beam mesh/texture proof; no production model importer."""

import argparse
import copy
import hashlib
import json
import os
import shutil
import struct
import subprocess
from pathlib import Path

from construct import Container, ListContainer
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.resources import make_string_table
from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.file_provider import IsoFileProvider, PathFileProvider
from retro_data_structures.formats.cmdl import Cmdl
from retro_data_structures.game_check import Game

from nullphaze_network.prime3_lua_service import bridge, probe
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea

SOURCE_MODEL = 0xDA25B1BE
TEMPLATE_MODEL = 0x9C5C5246993998A1
TARGET_AREA = 0xD8CF355D3E9E3741
TARGET_PICKUP = 131122
TARGET_MEMO = 131130
NAMESPACE = b"Nullphaze isolated Prime Ice Beam static proof v1\0"


def asset_id(kind, source):
    return int.from_bytes(hashlib.sha256(NAMESPACE + kind + source.to_bytes(8, "big")).digest()[:8], "big")


def convert_model(source, template, textures):
    """Retain source geometry; use a known retail shader with imported textures.

    This deliberately does not claim exact GX TEV-to-Corruption shader fidelity,
    skeletal animation conversion, or support for arbitrary source models.
    """
    raw = copy.deepcopy(source._raw)
    if raw.version != 2 or len(raw.material_sets) != 1 or len(raw.surfaces) != 1:
        raise ValueError("Proof supports only the audited Prime Ice Beam mesh")
    low, high = list(raw.aabox.min), list(raw.aabox.max)
    center = [(a + b) / 2 for a, b in zip(low, high, strict=True)]
    scale = 1.15 / (high[2] - low[2])
    for position in raw.attrib_arrays.positions:
        for axis in range(3):
            position[axis] = (position[axis] - center[axis]) * scale
    for axis in range(3):
        raw.aabox.min[axis] = (low[axis] - center[axis]) * scale
        raw.aabox.max[axis] = (high[axis] - center[axis]) * scale
    raw.version = 5
    raw.flags &= ~4
    raw.attrib_arrays.lightmap_uvs = None
    source_set = source._raw.material_sets[0]
    materials = []
    for index, material in enumerate(source_set.materials):
        if material.vertex_attribute_flags != 0xF0F or len(material.texture_indices) != 2:
            raise ValueError("Unexpected source Ice Beam material/vertex layout")
        result = copy.deepcopy(template._raw.material_sets[0].materials[0])
        result.group_index = index
        result.vertex_attribute_flags = material.vertex_attribute_flags | 0x81000000
        passes = [element for element in result.elements if element.type == "PASS"]
        if [element.body.subtype for element in passes] != ["CLR ", "INCA"]:
            raise ValueError("Retail material template changed")
        for element, tex_index in zip(passes, material.texture_indices, strict=True):
            element.body.id = textures[source_set.texture_file_ids[tex_index]]
            element.body.uv_source = 0
            element.body.uv_animation = ListContainer()
        materials.append(result)
    raw.material_sets = ListContainer([Container(texture_file_ids=None, materials=ListContainer(materials))])
    for surface in raw.surfaces:
        for axis in range(3):
            surface.header.center_point[axis] = (surface.header.center_point[axis] - center[axis]) * scale
        surface.header.unk_1 = 0
        surface.header.unk_2 = 65535
        surface.header.extra_data = b"\xff"
        for primitive in surface.primitives:
            for vertex in primitive.vertices:
                vertex.matrix.position = 0
                vertex.matrix.tex["6"] = 0
    encoded = Cmdl(raw, Game.CORRUPTION).build()
    checked = Cmdl.parse(encoded, Game.CORRUPTION)
    if (any(abs(a - b) > 0.000001
            for expected, actual in zip(raw.attrib_arrays.positions, checked._raw.attrib_arrays.positions, strict=True)
            for a, b in zip(expected, actual, strict=True))
            or checked._raw.surfaces[0].primitives != raw.surfaces[0].primitives):
        raise ValueError("Imported geometry/display lists changed on target roundtrip")
    return encoded, {"scale": scale, "center": center, "source_version": 2, "target_version": 5,
                     "vertices": len(raw.attrib_arrays.positions), "surfaces": len(raw.surfaces),
                     "materials": "retail_CLR_INCA_shader_with_imported_textures", "exact_source_shading": False,
                     "skeletal_animation": False, "native_static_pickup": True}


def patch_area(raw, model, dependencies, string, *, character=None):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    originals = {int(actor.id): copy.deepcopy(actor._raw) for layer in layers for actor in layer.instances}
    objects = {int(actor.id): actor for layer in layers for actor in layer.instances}
    pickup = objects[TARGET_PICKUP]
    if pickup.type_name != "PCKP":
        raise ValueError("Audited pickup actor changed")
    pickup._raw.base_property = probe.replace_properties(pickup._raw.base_property, {
        0xC27FFA8F: struct.pack(">Q", model),
        0xA244C9D8: struct.pack(">QI", character if character is not None else 0xffffffffffffffff, 0),
    })
    objects[TARGET_MEMO]._raw.base_property = probe.replace_properties(objects[TARGET_MEMO]._raw.base_property, {
        0x9182250C: struct.pack(">Q", string), 0x64124219: bytes(4),
    })
    deps = area.get_section("dependencies_section")[0]
    additions = [Container(asset_id=resource.identity, type=resource.kind.decode("ascii")) for resource in dependencies]
    deps.dependencies[deps.offsets[1]:deps.offsets[1]] = additions
    for index in range(1, len(deps.offsets)):
        deps.offsets[index] += len(additions)
    layers[0].mark_modified()
    encoded = area.build()
    checked = SeedMrea.parse(encoded, Game.CORRUPTION)
    rebuilt = {int(actor.id): actor for layer in checked.script_layers for actor in layer.instances}
    if set(rebuilt) != set(originals):
        raise ValueError("Model proof changed script population")
    for identity, original in originals.items():
        if identity not in (TARGET_PICKUP, TARGET_MEMO) and rebuilt[identity]._raw != original:
            raise ValueError("Model proof changed an unrelated seed script")
    fields = dict(probe.properties(rebuilt[TARGET_PICKUP]._raw.base_property))
    if any(fields[key] != bytes(4) for key in (0x28C71B54, 0x94AF1445, 0x165AB069)):
        raise ValueError("Model proof restored a native pickup grant")
    return encoded


def build(root, baseline, source_iso, retail, *, source_effects=False, source_animation=False, stage=None):
    if root.exists() or root.resolve().is_relative_to(baseline.resolve()):
        raise ValueError("Use a new isolated model-proof directory")
    root.mkdir(parents=True)
    if shutil.disk_usage(root).free < 10 * 1024**3:
        raise ValueError("The isolated model proof needs 10 GiB free for its image and verification extraction")
    if stage is not None:
        stage.mkdir(parents=True, exist_ok=False)
        if stage.resolve().is_relative_to(baseline.resolve()) or baseline.resolve().is_relative_to(stage.resolve()):
            raise ValueError("Staging and baseline must be disjoint")
        if shutil.disk_usage(stage).free < 2 * 1024**3:
            raise ValueError("The isolated PAK staging drive needs 2 GiB free")
    else:
        stage = root
    source_hash = probe.file_hash(source_iso)
    prime = AssetManager(IsoFileProvider(source_iso), Game.PRIME)
    target = AssetManager(PathFileProvider(retail), Game.CORRUPTION)
    source = prime.get_parsed_asset(SOURCE_MODEL, type_hint=Cmdl)
    template = target.get_parsed_asset(TEMPLATE_MODEL, type_hint=Cmdl)
    texture_ids = {identity: asset_id(b"TXTR", identity) for identity in source._raw.material_sets[0].texture_file_ids}
    assets = []
    for identity, converted in texture_ids.items():
        resource = prime.get_raw_asset(identity)
        if resource.type != "TXTR":
            raise ValueError("Source texture dependency has unexpected type")
        assets.append(Resource(converted, b"TXTR", 0, 0).updated(resource.data))
    model, conversion = convert_model(source, template, texture_ids)
    model_id, string_id = asset_id(b"CMDL", SOURCE_MODEL), asset_id(b"STRG", TARGET_MEMO)
    assets.append(Resource(model_id, b"CMDL", 0, 0).updated(model))
    assets.append(Resource(string_id, b"STRG", 0, 0).updated(make_string_table(["Ice Beam sent to Prime!"])))
    effects = None
    if source_effects or source_animation:
        from nullphaze_network.prime3_lua_service import imported_model_effects  # noqa: PLC0415

        dependencies, effect_id, effects = imported_model_effects.convert(prime)
        assets.extend(dependencies)
    rig_ids = None
    if source_animation:
        from nullphaze_network.prime3_lua_service import imported_model_rig  # noqa: PLC0415

        rig_assets, rig_ids, conversion = imported_model_rig.convert(prime, target, texture_ids, effect_id)
        assets = [resource for resource in assets if resource.kind != b"CMDL"] + rig_assets
        conversion.update(skeletal_animation=True, native_static_pickup=False, vertices=987,
                          materials="source_CLR_INCA_combiner_and_UV0_UV1_native_shader",
                          exact_source_shading=False, animation_acceptance="pending_Dolphin",
                          source_motion_frames=130, source_motion_seconds=4.300000190734863)
    if len({resource.identity for resource in assets}) != len(assets):
        raise ValueError("Duplicate imported asset identity")
    data = baseline / "image/DATA"
    for pak in data.joinpath("files").glob("*.pak"):
        if {resource.identity for resource in Archive(pak).resources} & {resource.identity for resource in assets}:
            raise ValueError("Imported asset ID collision")
    original = Archive(data / "files/Metroid1.pak")
    resources = []
    for resource in original.resources:
        if resource.identity == TARGET_AREA:
            resources.extend(assets)
            area = patch_area(resource.read(), model_id, assets, string_id,
                              character=rig_ids["CHAR"] if rig_ids else None)
            if effects is not None and not source_animation:
                area, effects = imported_model_effects.attach(area, effect_id, conversion, effects)
            resources.append(resource.updated(area))
        else:
            resources.append(resource)
    patched = stage / "Metroid1.pak"
    original.write(patched, resources)
    rebuilt = {resource.identity: resource for resource in Archive(patched).resources}
    for resource in original.resources:
        if resource.identity != TARGET_AREA and rebuilt[resource.identity].read() != resource.read():
            raise ValueError("Imported model changed an unrelated archive resource")
    copied = stage / "image/DATA"
    hashes = {}
    for path in data.rglob("*"):
        if path.is_file():
            relative = path.relative_to(data)
            destination = copied / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            source_path = patched if relative.as_posix() == "files/Metroid1.pak" else path
            # Hard links are read-only build inputs; no linked file is edited.
            os.link(source_path, destination)
            hashes[relative.as_posix()] = probe.file_hash(source_path)
    image = root / "image/RM3E01.wbfs"
    image.parent.mkdir(parents=True, exist_ok=True)
    wit = Path(r"C:\Users\Reed Whaley\Documents\MP3 Networking\randovania\data\gollop_mp3_patcher\wit\bin\wit.exe")
    for command in ([str(wit), "COPY", "-B", "--no-split", "--trunc", str(copied), str(image)],
                    [str(wit), "VERIFY", str(image)]):
        result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=3600)
        (root / f"wit-{command[1].lower()}.log").write_text(result.stdout + result.stderr)
        if result.returncode or "!!" in result.stderr:
            raise ValueError("Model proof image integrity command failed")
    report = copy.deepcopy(json.loads((baseline / "build.json").read_text()))
    expected = {
        "files": hashes, "dol_sha256": hashes["sys/main.dol"],
        "output_pak_sha256": hashes["files/UniverseArea.pak"],
    }
    extracted = root / "roundtrip"
    result = subprocess.run([str(wit), "EXTRACT", "--psel", "DATA", str(image), str(extracted)],
                            capture_output=True, text=True, check=False, timeout=3600)
    (root / "wit-extract.txt").write_text(result.stdout + result.stderr)
    if result.returncode or "!!" in result.stderr:
        raise ValueError("Model proof extraction failed")
    report["disc_roundtrip"] = bridge.verify_extracted(extracted, copied, expected)
    for filename in ("profile.bin", "disposable-checkpoint.bin"):
        shutil.copyfile(baseline / filename, root / filename)
    if probe.file_hash(source_iso) != source_hash or any(probe.file_hash(copied / p) != h for p, h in hashes.items()):
        raise ValueError("An immutable model-proof input changed")
    report["image_sha256"] = probe.file_hash(image)
    report["image_verified"] = True
    report["native_execution"] = "pending_Dolphin_model_proof"
    report["imported_model_prototype"] = {
        "source_iso_sha256": source_hash, "source_model": f"{SOURCE_MODEL:08x}",
        "target_model": f"{model_id:016x}", "source_item": "Prime Ice Beam", "target_location": 11,
        "recipient_text": "Ice Beam sent to Prime!", "fixture_text_override_only": True,
        "remote_delivery_enabled": False, "production_seed_manifest_unchanged": True,
        "conversion": conversion, "texture_count": len(texture_ids),
        "baseline_image_sha256": json.loads((baseline / "build.json").read_text())["image_sha256"],
        "source_particle_effect": effects, "staging_data": str(copied),
        "source_rig_assets": {kind: f"{identity:016x}" for kind, identity in rig_ids.items()} if rig_ids else None,
        "particle_route": "native_character_bone_event" if rig_ids else "standalone_effect_actor",
        "runtime_binary_reused_from_verified_baseline": True,
    }
    (root / "build.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report["imported_model_prototype"]), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("root", "baseline", "source-iso", "retail"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--source-effects", action="store_true")
    parser.add_argument("--source-animation", action="store_true")
    parser.add_argument("--stage", type=Path)
    args = parser.parse_args()
    build(args.root.resolve(), args.baseline.resolve(), args.source_iso.resolve(), args.retail.resolve(),
          source_effects=args.source_effects, source_animation=args.source_animation,
          stage=args.stage.resolve() if args.stage else None)
