# Build a retail-resource Lua probe without installing a network runtime. Boundary names
# here: sha256, file_hash, image_manifest, verify_image, properties.
"""Build a retail-resource Lua probe without installing a network runtime."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from retro_data_structures.base_resource import RawResource
from retro_data_structures.enums.corruption import Message, State
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.script_object import InstanceId, ScriptInstance, ScriptInstanceRaw
from retro_data_structures.formats.strg import NameTable, Strg
from retro_data_structures.game_check import Game
from retro_data_structures.properties.corruption.objects.LUAScript import LUAScript

from nullphaze_network.prime3_lua_service.inventory_profile import RETAIL_HASH, RETAIL_NAMES, extract_profile

RETAIL_UNIVERSE_HASH = "d745ec2b8c9767a803e97dfa9f582d794af6614712d85853973ef040ce6a881a"
DISC_IMAGE_NAME = "RM3E01.wbfs"
UNIVERSE_AREA = 0xE07F822F5594CBB4
MEMO_TEMPLATE = 0x51
STRING_TABLE = 0xBC7798AC32459585
SOURCE_PATH = Path(__file__).with_name("probe.lua")
MESSAGES = (
    ("ProbeReady", State.InternalState00, "LUA CALLBACK ACTIVE"),
    ("ProbeReadsPassed", State.InternalState01, "INVENTORY READS PASS"),
    ("ProbeChanged", State.InternalState02, "INVENTORY CHANGE OBSERVED"),
    ("ProbeUnavailable", State.InternalState03, "INVENTORY UNAVAILABLE"),
    ("ProbeRecovered", State.InternalState04, "INVENTORY RECOVERED"),
    ("ProbeHeartbeat", State.InternalState05, "INVENTORY HEARTBEAT (30 SECONDS)"),
    ("ProbeHeartbeatChanged", State.InternalState06, "INVENTORY CHANGE OBSERVED\nHEARTBEAT (30 SECONDS)"),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def image_manifest(image: Path) -> dict:
    parts = [image]
    for index in range(1, 10):
        part = image.with_suffix(f".wbf{index}")
        if part.exists():
            parts.append(part)
    if [part.suffix for part in parts] != [".wbfs", *(f".wbf{i}" for i in range(1, len(parts)))]:
        raise ValueError("Disc image parts are not contiguous")
    records = [{"name": part.name, "sha256": file_hash(part)} for part in parts]
    return {**records[0], "parts": records}


def verify_image(build: Path, manifest: dict) -> Path:
    image = build / manifest["image"]["name"]
    if image.parent != build or image.suffix != ".wbfs":
        raise ValueError("Invalid image manifest path")
    actual = image_manifest(image)
    expected = manifest["image"]
    if actual["sha256"] != expected["sha256"]:
        raise ValueError("Image does not match the build manifest")
    if actual["parts"] != expected.get("parts", [{"name": image.name, "sha256": expected["sha256"]}]):
        raise ValueError("Image parts do not match the build manifest")
    return image


def properties(data: bytes) -> list[tuple[int, bytes]]:
    """Read root TLVs without normalizing unrelated retail properties."""
    if len(data) < 8 or data[:4] != b"\xff" * 4:
        raise ValueError("Invalid property root")
    size, count = struct.unpack_from(">HH", data, 4)
    if size != len(data) - 6:
        raise ValueError("Invalid property root size")
    result = []
    offset = 8
    for _ in range(count):
        if offset + 6 > len(data):
            raise ValueError("Truncated property header")
        identifier, length = struct.unpack_from(">IH", data, offset)
        offset += 6
        if offset + length > len(data):
            raise ValueError("Truncated property value")
        result.append((identifier, data[offset : offset + length]))
        offset += length
    if offset != len(data) or len({key for key, _ in result}) != len(result):
        raise ValueError("Trailing bytes or duplicate properties")
    return result


def replace_properties(data: bytes, changes: dict[int, bytes]) -> bytes:
    fields = properties(data)
    if changes.keys() - {key for key, _ in fields}:
        raise ValueError("Requested property does not exist in retail template")
    payload = b"".join(
        struct.pack(">IH", key, len(changes.get(key, value))) + changes.get(key, value) for key, value in fields
    )
    return b"\xff" * 4 + struct.pack(">HH", len(payload) + 2, len(fields)) + payload


def build_retail_strg(table: Strg) -> bytes:
    """Keep every slot physical: the retail reader cannot rewind duplicates."""
    languages = table.get_language_list()
    strings = {language: list(table.get_strings(language)) for language in languages}
    counts = {len(values) for values in strings.values()}
    if len(counts) != 1:
        raise ValueError("String table languages have different lengths")
    count = counts.pop()
    data = bytearray()
    tables = bytearray()
    for language in languages:
        offsets = []
        total = 0
        for value in strings[language]:
            encoded = value.encode("utf-8") + b"\0"
            offsets.append(len(data))
            data.extend(struct.pack(">I", len(encoded)) + encoded)
            total += len(encoded)
        tables.extend(struct.pack(">I", total))
        tables.extend(struct.pack(f">{count}I", *offsets))
    result = (
        struct.pack(">4I", 0x87654321, 3, len(languages), count)
        + NameTable.build(table._raw.name_table)
        + b"".join(language.encode("ascii") for language in languages)
        + tables
        + data
    )
    result += bytes(-len(result) % 32)
    decoded = Strg.parse(result, Game.CORRUPTION)
    if any(list(decoded.get_strings(lang)) != values for lang, values in strings.items()):
        raise ValueError("Retail string serialization changed text")
    return result


def patch_pak(
    data: bytes, source: str, *, messages: tuple = MESSAGES, diagnostic_labels: bool = True
) -> tuple[bytes, dict]:
    pak = Pak.parse(data, Game.CORRUPTION)
    raw_area = pak.get_asset(UNIVERSE_AREA)
    raw_strings = pak.get_asset(STRING_TABLE)
    if raw_area is None or raw_area.type != "MREA" or raw_strings is None or raw_strings.type != "STRG":
        raise ValueError("Retail UniverseArea resources are missing")
    area = Mrea.parse(raw_area.data, Game.CORRUPTION)
    layers = list(area.script_layers)
    layer = layers[0]
    originals = [copy.deepcopy(item._raw) for item in layer.instances]
    all_instances = [item for item_layer in layers for item in item_layer.instances]
    template = next(item for item in layer.instances if item.id == MEMO_TEMPLATE)
    table = Strg.parse(raw_strings.data, Game.CORRUPTION)
    languages = table.get_language_list()
    lengths = {len(list(table.get_strings(language))) for language in languages}
    if len(lengths) != 1:
        raise ValueError("String table languages have different lengths")
    first_string = lengths.pop()
    marker = sha256(source.encode("utf-8"))[:8]
    highest_id = max(item.id.instance for item in all_instances)
    next_id = highest_id + 1
    if next_id + len(messages) >= 65536:
        raise ValueError("No unused instance IDs")
    area_index = template.id.area
    script_id = InstanceId.new(0, area_index, next_id)
    script_props = LUAScript(unknown_0xa1ecc54b=source)
    script_props.editor_properties.name = "CP3W Lua read-only service probe " + marker
    script_props.unknown_0xed4a2787 = "".join(
        f'"{event}" "InternalState{int(state.name.removeprefix("InternalState"))}"' for event, state, _ in messages
    )
    script = ScriptInstance(
        ScriptInstanceRaw("LUAX", script_id, (), script_props.to_bytes(Game.CORRUPTION)),
        Game.CORRUPTION,
        on_modify=layer.mark_modified,
    )
    added = []
    for index, (event, state, message) in enumerate(messages):
        instance_id = InstanceId.new(0, area_index, next_id + 1 + index)
        raw = copy.deepcopy(template._raw)
        raw.id = instance_id
        raw.connections = ()
        raw.base_property = replace_properties(
            raw.base_property,
            {
                0x64124219: struct.pack(">I", first_string + index),
                0x1A26C1CC: struct.pack(">f", 5.0),
                0xAFD0158E: b"\0",
                0xFB0E87DA: b"\0",
            },
        )
        layer._raw.script_instances.append(raw)
        script.add_connection(state, Message.Action, instance_id)
        table.append_string(f"&just=center;CP3W LUA {marker}\n{message}" if diagnostic_labels else message)
        added.append({"event": event, "id": int(instance_id), "string_index": first_string + index})
    layer._raw.script_instances.append(script._raw)
    layer.mark_modified()
    area_bytes = area.build()
    string_bytes = build_retail_strg(table)
    pak.replace_asset(UNIVERSE_AREA, RawResource("MREA", area_bytes))
    pak.replace_asset(STRING_TABLE, RawResource("STRG", string_bytes))
    # CMPD's library raw-block fallback is not accepted by this retail loader:
    # it still treats the payload as LZO segments. Store this small STRG raw.
    pak.get_pak_file_with_id(STRING_TABLE).should_compress = False
    patched = pak.build()
    checked = Pak.parse(patched, Game.CORRUPTION)
    stored_strings = checked.get_pak_file_with_id(STRING_TABLE)
    if stored_strings.should_compress or not stored_strings.get_decompressed(Game.CORRUPTION).startswith(
        bytes.fromhex("87654321")
    ):
        raise ValueError("Probe STRG must be stored as a raw retail resource, not CMPD")
    expected_ids = [(aid, raw.type) for aid, raw in pak.get_all_assets()]
    if [(aid, raw.type) for aid, raw in checked.get_all_assets()] != expected_ids:
        raise ValueError("PAK resource identity/order changed")
    original_pak = Pak.parse(data, Game.CORRUPTION)
    unchanged_count = 0
    for aid, original in original_pak.get_all_assets():
        if aid not in {UNIVERSE_AREA, STRING_TABLE}:
            if original.data != checked.get_asset(aid).data:
                raise ValueError(f"Unrelated resource changed: {aid:016x}")
            unchanged_count += 1
    decoded_area = Mrea.parse(checked.get_asset(UNIVERSE_AREA).data, Game.CORRUPTION)
    decoded_layers = list(decoded_area.script_layers)
    if [item._raw for item in decoded_layers[0].instances][: len(originals)] != originals:
        raise ValueError("Original default-layer objects changed")
    for index in range(1, len(layers)):
        if decoded_layers[index]._raw != layers[index]._raw:
            raise ValueError("Unrelated script layer changed")
    return patched, {
        "schema": 1,
        "probe_id": marker,
        "lua_source_sha256": sha256(source.encode("utf-8")),
        "input_pak_sha256": sha256(data),
        "output_pak_sha256": sha256(patched),
        "string_table_storage": "raw_not_cmpd",
        "area_id": UNIVERSE_AREA,
        "lua_instance_id": int(script_id),
        "added_memos": added,
        "unrelated_resources_verified": unchanged_count,
        "services": {"inventory": "read_only_probe", "location": "not_implemented", "grant": "disabled"},
        "network_operations": 0,
        "live_validation": {"dolphin": "not_run", "wii": "not_run", "vwii": "not_run"},
    }


def probe_source(inventory_scope: str = "basic") -> str:
    source = SOURCE_PATH.read_text(encoding="utf-8")
    if inventory_scope == "basic":
        return source
    if inventory_scope != "full":
        raise ValueError("Unknown inventory scope")
    old = 'items = {"PowerBeam", "Missile", "Energy", "ShipMissile", "SeekerMissile"}'
    if source.count(old) != 1 or source.count("schema = 1,") != 1 or source.count('"CP3W_LUA1"') != 1:
        raise ValueError("Probe template no longer matches the full-inventory transform")
    return (
        source.replace(old, "items = {" + ", ".join(json.dumps(name) for name in RETAIL_NAMES) + "}")
        .replace("schema = 1,", "schema = 2,")
        .replace('"CP3W_LUA1"', '"CP3W_LUA2"')
    )


def build(source: Path, output: Path, wit: Path | None, *, inventory_scope: str = "basic") -> dict:
    source, output = source.resolve(), output.resolve()
    if output == source or source in output.parents or output in source.parents:
        raise ValueError("Source and output trees must be disjoint")
    if output.exists():
        raise ValueError("Output must be a new directory")
    dol = source / "sys" / "main.dol"
    if file_hash(dol) != RETAIL_HASH:
        raise ValueError("Probe requires the supported clean retail NTSC-U DOL")
    pak_path = source / "files" / "UniverseArea.pak"
    original_pak = pak_path.read_bytes()
    if sha256(original_pak) != RETAIL_UNIVERSE_HASH:
        raise ValueError("Probe requires the supported clean retail UniverseArea.pak")
    lua = probe_source(inventory_scope)
    profile = extract_profile(dol.read_bytes()) if inventory_scope == "full" else None
    patched, report = patch_pak(original_pak, lua)
    # Repack twice before copying gigabytes or producing a playable artifact.
    repeated, _ = patch_pak(original_pak, lua)
    if repeated != patched:
        raise ValueError("PAK build is nondeterministic")
    report["deterministic_pak"] = True
    report["dol_sha256"] = RETAIL_HASH
    if profile is not None:
        report["inventory_profile"] = profile
    report["files"] = {}
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError("Source extraction contains symbolic links")
        if path.is_file():
            report["files"][path.relative_to(source).as_posix()] = file_hash(path)
    output.mkdir(parents=True)
    copied = output / "DATA"
    shutil.copytree(source, copied)
    (copied / "files" / "UniverseArea.pak").write_bytes(patched)
    for relative, expected in report["files"].items():
        wanted = report["output_pak_sha256"] if relative == "files/UniverseArea.pak" else expected
        if file_hash(copied / relative) != wanted or file_hash(source / relative) != expected:
            raise ValueError(f"Source/copy verification failed: {relative}")
    report["extraction_verified"] = True
    if wit is not None:
        image = output / DISC_IMAGE_NAME
        subprocess.run([os.fspath(wit), "COPY", "-B", "-z", "--trunc", os.fspath(copied), os.fspath(image)], check=True)
        subprocess.run([os.fspath(wit), "VERIFY", os.fspath(image)], check=True)
        report["image"] = {**image_manifest(image), "wit_verified": True}
    (output / "build.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--wit", type=Path)
    parser.add_argument("--inventory-scope", choices=("basic", "full"), default="basic")
    args = parser.parse_args()
    print(
        json.dumps(
            build(args.source_data, args.output, args.wit, inventory_scope=args.inventory_scope),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
