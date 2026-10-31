# Build the isolated, no-grant Docking Bay 5 model gallery. Boundary names here: height_at,
# gallery_positions, patch_gallery, build.
"""Build the isolated, no-grant Docking Bay 5 model gallery."""

import argparse
import copy
import json
import math
import shutil
import struct
import subprocess
from pathlib import Path

from construct import Container
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.resources import make_string_table
from retro_data_structures.enums.corruption import Message, State
from retro_data_structures.formats.script_object import Connection, InstanceId, ScriptInstanceRaw
from retro_data_structures.game_check import Game
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.vector import Vector

from nullphaze_network.prime3_lua_service import bridge, probe
from nullphaze_network.prime3_lua_service import imported_model_probe as model
from nullphaze_network.prime3_lua_service.imported_gallery_assets import asset_id
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea


def height_at(triangles, x, y):
    heights = []
    for a, b, c in triangles:
        denominator = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
        if abs(denominator) < 1e-7:
            continue
        u = ((b[1] - c[1]) * (x - c[0]) + (c[0] - b[0]) * (y - c[1])) / denominator
        v = ((c[1] - a[1]) * (x - c[0]) + (a[0] - c[0]) * (y - c[1])) / denominator
        if u >= -1e-6 and v >= -1e-6 and u + v <= 1 + 1e-6:
            heights.append(u * a[2] + v * b[2] + (1 - u - v) * c[2])
    return max(heights) if heights else None


def gallery_positions(area, count):
    collision = area.get_section("collision_section")[0].collision_indices
    triangles = []
    for triangle in collision.triangles:
        indices = set()
        for edge in triangle.values():
            indices.update((collision.edges[edge].vertexA, collision.edges[edge].vertexB))
        if len(indices) != 3:
            raise ValueError("Invalid source collision triangle")
        points = [list(collision.vertices[i]) for i in sorted(indices)]
        if min(p[2] for p in points) >= -22.3 and max(p[2] for p in points) <= -20.8:
            triangles.append(points)
    candidates = []
    for ix in range(22):
        for iy in range(25):
            x, y = 178 + ix * 2.4, -63 + iy * 2.4
            support = [
                height_at(triangles, x + dx, y + dy)
                for dx, dy in ((0, 0), (-0.55, 0), (0.55, 0), (0, -0.55), (0, 0.55))
            ]
            if all(z is not None for z in support) and max(support) - min(support) < 0.2:
                candidates.append([x, y, support[0] + 0.9])
    candidates.sort(key=lambda p: (math.hypot(p[0] - 219, p[1] + 34), p[0], p[1]))
    if len(candidates) < count:
        raise ValueError(f"Only {len(candidates)} supported gallery positions for {count} entries")
    return sorted(candidates[:count], key=lambda p: (-p[1], p[0]))


def patch_gallery(raw, resources, entries):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    objects = {int(actor.id): actor for layer in layers for actor in layer.instances}
    original = {identity: copy.deepcopy(actor._raw) for identity, actor in objects.items()}
    pickup, memo = objects[model.TARGET_PICKUP], objects[model.TARGET_MEMO]
    positions = gallery_positions(area, len(entries))
    used = {actor.id.instance for actor in objects.values()}
    free = iter(i for i in range(30000, 60000) if i not in used)
    layout, additions = [], list(resources)
    for index, (entry, position) in enumerate(zip(entries, positions, strict=True), 1):
        pickup_id = InstanceId.new(0, pickup.id.area, next(free))
        memo_id = InstanceId.new(0, pickup.id.area, next(free))
        label = f"{index:02d} {entry['game']}: {entry['name'].replace(' INCOMPLETE', '')}"
        if "placeholder" in entry.get("provenance", ""):
            label += " [Gamecube placeholder]"
        string_id = asset_id("STRG", label)
        additions.append(Resource(string_id, b"STRG", False, 0).updated(make_string_table([label])))
        editor = EditorProperties.from_bytes(dict(probe.properties(pickup._raw.base_property))[0x255A4580], Game.CORRUPTION)
        editor.name = "Gallery " + label
        editor.active = True
        editor.transform.position = Vector(*position)
        editor.transform.rotation = Vector(0, 0, 0)
        editor.transform.scale = Vector(1, 1, 1)
        state_id = struct.pack(">QQ", asset_id("STATE", label), asset_id("STATE2", label))
        properties = probe.replace_properties(
            pickup._raw.base_property,
            {
                0x255A4580: editor.to_bytes(Game.CORRUPTION),
                0x16D9A75D: state_id,
                0xC27FFA8F: struct.pack(">Q", int(entry["native"]["CMDL"], 16)),
                0xA244C9D8: struct.pack(">QI", int(entry["native"]["CHAR"], 16), 0),
                0x28C71B54: bytes(4),
                0x94AF1445: bytes(4),
                0x165AB069: bytes(4),
                0xE10BCB96: bytes(1),
                0x3A3E03BA: struct.pack(">fff", 0.4, 0.4, 0.4),
                0x2E686C2A: bytes(12),
                0xA6EA280D: struct.pack(">f", 0),
            },
        )
        connection = Connection(State.Acquired, Message.SetToZero, memo_id)
        layers[0]._raw.script_instances.append(ScriptInstanceRaw("PCKP", pickup_id, (connection,), properties))
        memo_editor = copy.deepcopy(editor)
        memo_editor.name = "Gallery notice " + label
        memo_properties = probe.replace_properties(
            memo._raw.base_property,
            {
                0x255A4580: memo_editor.to_bytes(Game.CORRUPTION),
                0x9182250C: struct.pack(">Q", string_id),
                0x64124219: bytes(4),
            },
        )
        layers[0]._raw.script_instances.append(ScriptInstanceRaw("MEMO", memo_id, (), memo_properties))
        layout.append(
            {
                "index": index,
                "label": label,
                "position": position,
                "pickup_id": int(pickup_id),
                "memo_id": int(memo_id),
                "state_id": state_id.hex(),
                "native": entry["native"],
                "grant_amount": 0,
                "receipt_callback": False,
            }
        )
    deps = area.get_section("dependencies_section")[0]
    deps.dependencies[deps.offsets[1] : deps.offsets[1]] = [
        Container(asset_id=r.identity, type=r.kind.decode()) for r in additions
    ]
    for i in range(1, len(deps.offsets)):
        deps.offsets[i] += len(additions)
    layers[0].mark_modified()
    encoded = area.build()
    checked = SeedMrea.parse(encoded, Game.CORRUPTION)
    rebuilt = {int(actor.id): actor for layer in checked.script_layers for actor in layer.instances}
    if len(rebuilt) != len(original) + 2 * len(entries):
        raise ValueError("Gallery actor population mismatch")
    for identity, before in original.items():
        if rebuilt[identity]._raw != before:
            raise ValueError("Gallery changed an original room actor")
    for item in layout:
        actor = rebuilt[item["pickup_id"]]
        fields = dict(probe.properties(actor._raw.base_property))
        if any(fields[key] != bytes(4) for key in (0x28C71B54, 0x94AF1445, 0x165AB069)):
            raise ValueError("A gallery pickup grants local inventory")
        if len(actor._raw.connections) != 1 or int(actor._raw.connections[0].target) != item["memo_id"]:
            raise ValueError("A gallery pickup has a non-label callback")
    return encoded, additions, layout


def build(root, inputs, baseline):
    if root.exists():
        raise ValueError("Use a new gallery image directory")
    root.mkdir(parents=True)
    if shutil.disk_usage(root).free < 16 * 1024**3:
        raise ValueError("Gallery image and readback need 16 GiB free")
    manifest = json.loads((inputs / "converted-assets.json").read_text())
    controls = manifest.get("diagnostic_material_controls")
    diagnostic = (
        manifest.get("diagnostic_only") is True
        and controls is not None
        and [row["gallery_index"] for row in controls] == list(range(27, 39))
    )
    effect_controls = manifest.get("diagnostic_effect_controls")
    effect_diagnostic = (
        manifest.get("diagnostic_only") is True
        and isinstance(effect_controls, list)
        and len(effect_controls) == manifest["entry_count"] == len(manifest["entries"]) == 18
        and [r["index"] for r in effect_controls] == list(range(1, 19))
        and [r["variant"] for r in effect_controls] == ["clamped", "model_matched"] * 9
    )
    if not effect_diagnostic and (manifest["entry_count"] != 93 or not (manifest["zero_omissions"] or diagnostic)):
        raise ValueError("Incomplete gallery source set")
    resources = [
        Resource(int(path.stem, 16), path.suffix[1:].encode(), False, 0).updated(path.read_bytes())
        for path in (inputs / "converted-assets").iterdir()
    ]
    original = Archive(baseline / "image/DATA/files/Metroid1.pak")
    target = next(r for r in original.resources if r.identity == model.TARGET_AREA)
    raw, resources, layout = patch_gallery(target.read(), resources, manifest["entries"])
    identities = {r.identity for r in resources}
    if len(identities) != len(resources):
        raise ValueError("Duplicate gallery resources")
    for pak in (baseline / "image/DATA/files").glob("*.pak"):
        if {r.identity for r in Archive(pak).resources} & identities:
            raise ValueError("Gallery resource collides with the baseline")
    additions = [target.updated(raw), *resources]
    patched = root / "Metroid1.pak"
    original.write(patched, [r for r in original.resources if r.identity != model.TARGET_AREA] + additions)
    data = root / "image/DATA"
    hashes = {}
    source_data = baseline / "image/DATA"
    for path in source_data.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(source_data)
        source = patched if relative.as_posix() == "files/Metroid1.pak" else path
        destination = data / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        hashes[relative.as_posix()] = probe.file_hash(source)
    (root / "gallery-layout.json").write_text(json.dumps(layout, indent=2))
    lines = [
        "# Docking Bay 5 Model Gallery",
        "",
        f"{len(manifest['entries'])} no-grant, no-receipt test pickups; do not save.",
        "",
        "Source shader roles, blending and UV transforms are mapped; visual fidelity remains a live gate.",
        (
            "Meshes fit a 0.8 m animated envelope. Effects follow model-matched scale; trajectories are not bounded."
            if manifest.get("effect_scale_policy") == "model_matched"
            else "Meshes fit a 0.8 m animated envelope. This diagnostic retains its manifest's particle scales."
        ),
        "",
        "| Number | Model | Position |",
        "| --- | --- | --- |",
    ]
    lines.extend(f"| {row['index']} | {row['label']} | {row['position']} |" for row in layout)
    (root / "gallery-guide.md").write_text("\n".join(lines) + "\n")
    image = root / "image/RM3E01.wbfs"
    wit = Path(r"C:\Users\Reed Whaley\Documents\MP3 Networking\randovania\data\gollop_mp3_patcher\wit\bin\wit.exe")
    for command in (
        [str(wit), "COPY", "-B", "--no-split", "--trunc", str(data), str(image)],
        [str(wit), "VERIFY", str(image)],
        [str(wit), "EXTRACT", "--psel", "DATA", str(image), str(root / "roundtrip")],
    ):
        result = subprocess.run(command, capture_output=True, text=True, timeout=3600, check=False)
        (root / f"wit-{command[1].lower()}.log").write_text(result.stdout + result.stderr)
        if result.returncode or "!!" in result.stderr:
            raise ValueError("Gallery image integrity operation failed")
    expected = {
        "files": hashes,
        "dol_sha256": hashes["sys/main.dol"],
        "output_pak_sha256": hashes["files/UniverseArea.pak"],
    }
    report = json.loads((baseline / "build.json").read_text())
    report["disc_roundtrip"] = bridge.verify_extracted(root / "roundtrip", data, expected)
    report.update(
        image_verified=True,
        image_sha256=probe.file_hash(image),
        native_execution="pending_Dolphin_gallery",
        gallery_entries=len(manifest["entries"]),
        gallery_catalog_complete=not (diagnostic or effect_diagnostic),
        gallery_material_controls=controls if diagnostic else [],
        gallery_effect_controls=effect_controls if effect_diagnostic else [],
        gallery_effect_scale_policy=manifest.get("effect_scale_policy", "input_manifest"),
        gallery_local_grants=False,
        gallery_receipt_callbacks=False,
        gallery_material_fidelity="source semantic roles/blending/UV transforms mapped; visual acceptance pending",
    )
    for name in ("profile.bin", "disposable-checkpoint.bin"):
        shutil.copyfile(baseline / name, root / name)
    if any(probe.file_hash(data / path) != value for path, value in hashes.items()):
        raise ValueError("Gallery staging changed during verification")
    (root / "build.json").write_text(json.dumps(report, indent=2))
    print(json.dumps({"entries": len(manifest["entries"]), "image_sha256": report["image_sha256"], "verified": True}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("root", "inputs", "baseline"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    build(args.root.resolve(), args.inputs.resolve(), args.baseline.resolve())
