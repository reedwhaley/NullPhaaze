# Lossless GC SCLY framing; preserve every original object and connection. Boundary names
# here: u32, split_objects, object_info, split_prime_scly, static_prime_properties.
"""Lossless GC SCLY framing; preserve every original object and connection."""

import struct

from retro_data_structures.game_check import Game


def u32(data, offset):
    return struct.unpack_from(">I", data, offset)[0]


def split_objects(data, count, offset, game):
    objects = []
    for _ in range(count):
        header = 5 if game == Game.PRIME else 6
        if offset + header > len(data):
            raise ValueError("Truncated object header")
        size = u32(data, offset + 1) if game == Game.PRIME else struct.unpack_from(">H", data, offset + 4)[0]
        end = offset + header + size
        if size < (8 if game == Game.PRIME else 6) or end > len(data):
            raise ValueError("Invalid object extent")
        objects.append(data[offset:end])
        offset = end
    return objects, offset


def object_info(data, game):
    if game == Game.PRIME:
        kind, identity, count = data[0], u32(data, 5), u32(data, 9)
        start = 13 + 12 * count
    else:
        kind, identity, count = data[:4].decode("ascii"), u32(data, 6), struct.unpack_from(">H", data, 10)[0]
        start = 12 + 12 * count
    if start > len(data):
        raise ValueError("Connections exceed object extent")
    return kind, identity, data[start:]


def split_prime_scly(data):
    if data[:4] != b"SCLY":
        raise ValueError("Expected SCLY")
    count = u32(data, 8)
    if count > 64 or 12 + 4 * count > len(data):
        raise ValueError("Invalid layer count")
    layers, cursor = [], 12 + 4 * count
    for i in range(count):
        size = u32(data, 12 + 4 * i)
        layer = data[cursor : cursor + size]
        objects, end = split_objects(layer, u32(layer, 1), 5, Game.PRIME)
        layers.append((layer[:1], objects, layer[end:]))
        cursor += size
    if cursor > len(data):
        raise ValueError("Layers exceed section")
    return data[:8], layers, data[cursor:]


def static_prime_properties(props, item):
    """Change only rendering fields; preserve item amount/type, collection and scan data."""
    name_end = props.index(0, 4) + 1
    if len(props) < name_end + 104:
        raise ValueError("Truncated Prime pickup properties")
    changed = bytearray(props)
    struct.pack_into(">3f", changed, name_end + 12, 0.0, 0.0, 0.0)
    struct.pack_into(">III", changed, name_end + 88, 0xFFFFFFFF, 0, 0)
    return bytes(changed)


def static_prime_scly(data, items):
    prefix, layers, tail = split_prime_scly(data)
    blobs, count = [], 0
    for unknown, objects, padding in layers:
        updated = []
        for obj in objects:
            kind, identity, props = object_info(obj, Game.PRIME)
            if kind == 0x11:
                name_end = props.index(0, 4) + 1
                model = u32(props, name_end + 84)
                if model in items:
                    item = items[model]
                    if u32(props, name_end + 88) != item["ancs"]:
                        raise ValueError("Corruption pickup transport ANCS does not match")
                    changed = static_prime_properties(props, item)
                    obj = obj[: len(obj) - len(props)] + changed
                    count += 1
            updated.append(obj)
        blobs.append(unknown + struct.pack(">I", len(updated)) + b"".join(updated) + padding)
    return (
        prefix
        + struct.pack(">I", len(blobs))
        + struct.pack(">" + "I" * len(blobs), *map(len, blobs))
        + b"".join(blobs)
        + tail
    ), count


def static_prime_mrea(data, items):
    from retro_data_structures.formats.mrea import Mrea

    parsed = Mrea.parse(data, Game.PRIME)
    original = parsed._raw.raw_sections.script_layers_section[0]
    changed, count = static_prime_scly(original, items)
    if not count:
        return data, 0
    # Rendering fields have fixed widths. Patch their unique uncompressed SCLY
    # section in place, preserving every header/section byte across RDS versions.
    offset = data.find(original)
    if len(changed) != len(original) or offset < 0 or data.find(original, offset + 1) >= 0:
        raise ValueError("Cannot uniquely locate fixed-width Prime script section")
    encoded = data[:offset] + changed + data[offset + len(original) :]
    checked = Mrea.parse(encoded, Game.PRIME)
    for category, values in parsed._raw.raw_sections.items():
        if category != "script_layers_section" and checked._raw.raw_sections[category] != values:
            raise ValueError("Static actor pass changed unrelated MREA data")
    return encoded, count


def finalize_prime_models(contents, metadata, progress):
    """Remove loader transport from actors/dependencies before an image can be published."""
    from retro_data_structures.base_resource import RawResource
    from retro_data_structures.formats.mlvl import Mlvl
    from retro_data_structures.formats.pak import Pak

    items = {item["cmdl"]: item for item in metadata["items"].values() if not item.get("animated", False)}
    wrappers = {item["ancs"] for item in items.values()}
    total = 0
    paths = sorted((contents / "files").glob("*.pak"))
    for index, path in enumerate(paths):
        pak = Pak.parse(path.read_bytes(), Game.PRIME)
        original = dict(pak.get_all_assets())
        changed = set()
        for asset_id, raw in original.items():
            if raw.type == "MREA":
                data, count = static_prime_mrea(raw.data, items)
                total += count
                if count:
                    pak.replace_asset(asset_id, RawResource("MREA", data))
                    changed.add(asset_id)
            elif raw.type == "MLVL":
                world = Mlvl.parse(raw.data, Game.PRIME)
                dirty = False
                for area in world._raw.areas:
                    deps = area.dependencies
                    # RDS 0.44 exposes immutable dependency tuples.
                    from retro_data_structures.formats.mrea import AreaDependencies

                    non_layer = tuple(d for d in deps.non_layer if d.id not in wrappers)
                    layers = tuple(tuple(d for d in layer if d.id not in wrappers) for layer in deps.layers)
                    if non_layer != deps.non_layer or layers != deps.layers:
                        area.dependencies = AreaDependencies(layers, non_layer)
                        dirty = True
                if dirty:
                    world._raw[None] = ""
                    pak.replace_asset(asset_id, RawResource("MLVL", world.build()))
                    changed.add(asset_id)
        for wrapper in wrappers & set(original):
            pak.remove_asset(wrapper)
            changed.add(wrapper)
        if changed:
            encoded = pak.build()
            checked = Pak.parse(encoded, Game.PRIME)
            for asset_id, raw in original.items():
                if asset_id not in changed:
                    actual = checked.get_asset(asset_id)
                    if actual.type != raw.type or actual.data != raw.data:
                        raise ValueError("Static actor pass changed unrelated resource")
            path.write_bytes(encoded)
        progress("Finalizing static Corruption models in " + path.name, (index + 1) / len(paths))
    return total


def finish_prime_image(image, output, metadata, progress):
    """Produce a complete final ISO atomically; temporary randomprime output is never published."""
    import tempfile
    from pathlib import Path

    from randovania.patching.patchers.gamecube.iso_packager import unpack_iso

    output.parent.mkdir(parents=True, exist_ok=True)
    with (
        tempfile.TemporaryDirectory(prefix="corruption-actors-", dir=image.parent) as temporary,
        tempfile.TemporaryDirectory(prefix="corruption-publish-", dir=output.parent) as publication,
    ):
        root = Path(temporary)
        contents = root / "contents"
        unpack_iso(image, contents, lambda s, p: progress(s, p * 0.3))
        count = finalize_prime_models(contents, metadata, lambda s, p: progress(s, 0.3 + p * 0.4))
        final = Path(publication) / "complete.iso"
        import nod

        if nod.DiscBuilderGCN.calculate_total_size_required(contents) is None:
            raise ValueError("Corruption model output exceeds GameCube disc capacity")
        nod.DiscBuilderGCN(final, lambda p, name, _: progress(name, 0.7 + p * 0.3)).build_from_directory(contents)
        # Reopen through the disc reader: ensure this is a real GC image and DOL/payloads match.
        from randovania.patching.prime.corruption_file_provider import IsoFileProvider, PathFileProvider

        actual, expected = IsoFileProvider(final), PathFileProvider(contents)
        if actual.get_dol() != expected.get_dol():
            raise ValueError("Packed DOL differs")
        if set(actual.get_file_list()) != set(expected.get_file_list()):
            raise ValueError("Packed file inventory differs")
        for name in expected.get_file_list():
            a, b = actual.read_binary(name), expected.read_binary(name)
            if a[: len(b)] != b or a[len(b) :] != b"\xff" * ((-len(b)) % 32):
                raise ValueError("Packed payload differs: " + name)
        final.replace(output)
    return count
