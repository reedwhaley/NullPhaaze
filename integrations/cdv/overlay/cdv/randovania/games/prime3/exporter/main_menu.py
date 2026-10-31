# GPL export addon: seed identity on the retail Corruption frontend. Boundary names here:
# metadata, validate_metadata, footer_text, session_patch_data, patch_frame.
"""GPL export addon: seed identity on the retail Corruption frontend.

The core's eleven-file interface stays unchanged. Two non-interactive GUI text
panes reuse the frontend's font, localization table and existing page parents.
No gameplay actors, save data or executable instructions are changed.
"""
from __future__ import annotations

import hashlib
import re
import struct
from pathlib import Path

from nullphaze_core.archives import Archive
from nullphaze_core.binary import pad
from retro_data_structures.formats.cmpd import CompressedWiiPakResource
from construct import Container
from retro_data_structures.formats.strg import Strg, STRG_V3
from retro_data_structures.game_check import Game

FRAME = 0xA0F86C4BC5274449
STRINGS = 0x4B58B2CD773428CD
FRAME_SHA256 = "b5d402c9550224694e2c0ef4fc7f1dc5a030c256c5db636d2c7bbdfcde2a692c"
WIDGET_COUNT_OFFSET = 0xCAA8
WIDGET_END = 125619
TITLE_START, TITLE_END = 52232, 52545
FOOTERS = (("NullphazeBuildInfo", "basewidget_MainMenu"),
           ("NullphazeSlotBuildInfo", "basewidget_SlotSelect"))


def metadata(version: str, word_hash: str, seed_hash: str) -> dict[str, str]:
    result = {"version": version, "word_hash": word_hash, "seed_hash": seed_hash}
    validate_metadata(result)
    return result


def validate_metadata(value: dict) -> None:
    if not isinstance(value, dict) or set(value) != {"version", "word_hash", "seed_hash"}:
        raise ValueError("Invalid Corruption menu identity metadata")
    for key, limit in (("version", 64), ("word_hash", 120)):
        text = value[key]
        if (not isinstance(text, str) or not 1 <= len(text) <= limit
                or not text.isprintable() or "&" in text):
            raise ValueError(f"Invalid Corruption menu {key}")
    if not isinstance(value["seed_hash"], str) or not re.fullmatch(r"[A-Z2-7]{8}", value["seed_hash"]):
        raise ValueError("Invalid Corruption menu seed hash")


def footer_text(value: dict) -> str:
    validate_metadata(value)
    return (f"&just=left;&main-color=#000000;CDV {value['version']}\n"
            f"Seed Hash: {value['word_hash']} ({value['seed_hash']})")


def session_patch_data(patch_data: dict, version: str, word_hash: str, seed_hash: str) -> dict:
    """Attach the open session's identity even when an older server exports it.

    Server patch data predates the optional menu field. The session already
    publishes its display hashes; never derive them from a checkpoint or name.
    """
    identity = metadata(version, word_hash, seed_hash)
    previous = patch_data.get("menu_identity")
    if previous is not None:
        validate_metadata(previous)
        if any(previous[key] != identity[key] for key in ("word_hash", "seed_hash")):
            raise ValueError("Corruption menu identity does not match the open session")
    return {**patch_data, "menu_identity": identity}


def patch_frame(raw: bytes) -> bytes:
    # RDS's FRME writer does not support Corruption's version-14 animation
    # envelope. Keep that envelope and all existing widgets byte-for-byte.
    if hashlib.sha256(raw).hexdigest() != FRAME_SHA256:
        raise ValueError("Unsupported Corruption frontend frame; refusing an unguarded menu patch")
    if struct.unpack_from(">I", raw, WIDGET_COUNT_OFFSET)[0] != 305:
        raise ValueError("Unexpected Corruption frontend widget count")
    template = raw[TITLE_START:TITLE_END]
    prefix = b"TXPNtextpane_MainMenu_Title\0basewidget_MainMenu\0"
    if not template.startswith(prefix) or raw[WIDGET_END:] != b"\xff" * (len(raw) - WIDGET_END):
        raise ValueError("Unexpected Corruption frontend widget layout")
    body = template[len(prefix):]
    if len(body) != 265 or struct.unpack_from(">5f", body, 24) != (
            5.875, 1.7623229026794434, 2.9375, 0.0, 0.8811614513397217):
        raise ValueError("Unexpected frontend text-pane dimensions")
    additions = bytearray()
    for name, parent in FOOTERS:
        if parent.encode() + b"\0" not in raw or name.encode() in raw:
            raise ValueError("Missing frontend page or duplicate seed footer")
        pane = bytearray(body)
        # Font raster dimensions set text size independently of the basis.
        # Use the menu row width and the empty band above the bottom controls.
        struct.pack_into(">5f", pane, 24, 23.5, 2.2, 11.75, 0.0, 1.1)
        for font_info in (53, 101):
            struct.pack_into(">II", pane, font_info, 625, 56)
        x, y, _ = struct.unpack_from(">3f", pane, len(pane) - 48)
        struct.pack_into(">3f", pane, len(pane) - 48, x, y, -4.2)
        additions.extend(b"TXPNtextpane_" + name.encode() + b"\0" + parent.encode() + b"\0" + pane)
    result = bytearray(raw[:WIDGET_END])
    struct.pack_into(">I", result, WIDGET_COUNT_OFFSET, 305 + len(FOOTERS))
    result.extend(additions)
    return pad(result, 32, 255)


def _decoded(resource):
    raw = resource.read()
    return CompressedWiiPakResource.parse(raw, target_game=Game.CORRUPTION) if resource.compressed else raw


def build_sequential_strings(table: Strg) -> bytes:
    """The native loader streams forward; deduplicated/backward offsets crash it.

    RDS can parse its deduplicated output, but the retail STRG loader cannot.
    Give every occurrence its own length-prefixed UTF-8 record.
    """
    strings, languages = [], []
    offset = 0
    count = None
    for language in table.get_language_list():
        values = table.get_strings(language)
        if count is None:
            count = len(values)
        if len(values) != count:
            raise ValueError("Inconsistent frontend string counts")
        offsets, size = [], 0
        for text in values:
            length = len(text.encode("utf-8")) + 1
            offsets.append(offset)
            strings.append(text)
            offset += 4 + length
            size += length
        languages.append(Container(strings_size=size, string_offsets=offsets))
    return STRG_V3.build(Container(
        header=Container(magic=0x87654321, version="prime3",
                         language_count=len(languages), string_count=count),
        name_table=dict(table._raw.name_table),
        language_ids=list(table.get_language_list()),
        language_table=languages, strings=strings))


def patch_archive(source: Path, output: Path, value: dict) -> dict:
    text = footer_text(value)
    if output.exists() or source.resolve() == output.resolve():
        raise ValueError("Use a new menu staging archive")
    archive = Archive(source)
    if any(sum(r.identity == identity for r in archive.resources) != 1 for identity in (FRAME, STRINGS)):
        raise ValueError("Missing or ambiguous Corruption menu resources")
    changed = []
    original_names = None
    original_languages = None
    for resource in archive.resources:
        if resource.identity == FRAME:
            changed.append(resource.updated(patch_frame(_decoded(resource)), compressed=0))
        elif resource.identity == STRINGS:
            table = Strg.parse(_decoded(resource), Game.CORRUPTION)
            if table._raw.name_table.get("MainMenu_Title") != 15:
                raise ValueError("Unsupported frontend localization table")
            original_names = dict(table._raw.name_table)
            original_languages = {lang: table.get_strings(lang) for lang in table.get_language_list()}
            for name, _ in FOOTERS:
                if name in table._raw.name_table:
                    raise ValueError("Frontend already contains a seed footer")
                table.append_string(text, name=name)
            changed.append(resource.updated(build_sequential_strings(table), compressed=0))
        else:
            changed.append(resource)
    archive.write(output, changed)
    check = Archive(output)
    if [(r.identity, r.kind) for r in archive.resources] != [(r.identity, r.kind) for r in check.resources]:
        raise ValueError("Menu patch changed archive resource identity/order")
    verified = 0
    for before, after in zip(archive.resources, check.resources, strict=True):
        if before.identity not in (FRAME, STRINGS):
            if before.compressed != after.compressed or before.read() != after.read():
                raise ValueError("Unrelated GUI resource changed")
            verified += 1
    table = Strg.parse(_decoded(next(r for r in check.resources if r.identity == STRINGS)), Game.CORRUPTION)
    if any(table._raw.name_table.get(k) != v for k, v in original_names.items()):
        raise ValueError("Existing frontend localization names changed")
    if set(table.get_language_list()) != set(original_languages):
        raise ValueError("Frontend language list changed")
    for lang, strings in original_languages.items():
        if table.get_strings(lang) != (*strings, text, text):
            raise ValueError("Existing frontend localization text changed")
    return {"applied": True, **value, "text": text, "gui_text_panes_added": len(FOOTERS),
            "gameplay_actors_added": 0, "unrelated_resources_verified": verified,
            "native_forward_string_order": True,
            "existing_localization_preserved": True,
            "archive_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}
