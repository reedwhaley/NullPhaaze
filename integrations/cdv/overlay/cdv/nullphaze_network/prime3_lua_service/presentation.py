# Existing HUD events and exact retail missile presentation; no inventory writes. Boundary
# names here: validate_lua50_length_syntax, instrument_lua, patch_pickup.
"""Existing HUD events and exact retail missile presentation; no inventory writes."""

from __future__ import annotations

import copy
import re
import struct
from pathlib import Path

from construct import Container
from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.base_resource import RawResource
from retro_data_structures.enums.corruption import Message, State
from retro_data_structures.file_provider import PathFileProvider
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.script_object import InstanceId
from retro_data_structures.formats.strg import Strg
from retro_data_structures.game_check import Game

from nullphaze_network.prime3_lua_service import probe

NETWORK_MESSAGES = (
    ("NetworkIPReady", State.InternalState10, "IP ADDRESS ACQUIRED"),
    ("NetworkSocketReady", State.InternalState11, "UDP SOCKET READY"),
    ("NetworkHello", State.InternalState12, "HELLO RECEIVED - SESSION ACCEPTED"),
    ("NetworkDisconnected", State.InternalState13, "NETWORK SESSION ENDED"),
    ("NetworkFailed", State.InternalState14, "NETWORK ERROR OR TIMEOUT\nSEE DIAGNOSTIC PANEL"),
    ("NetworkRejected", State.InternalState15, "NETWORK PACKET REJECTED\nSEE FR AND ST ON PANEL"),
    ("NetworkReady", State.InternalState16, "NETWORK SESSION CHECKS PASSED"),
    ("PickupMissileReceived", State.InternalState17, "MISSILE EXPANSION RECEIVED"),
)
MEMO = 0x4B4F9DC4253862CA
AUDIO = 0xA832FC0C74651F24
TEMPLATE_AREA = 9908630587780032110


def validate_lua50_length_syntax(source: str) -> None:
    """Guard this known Lua 5.0 incompatibility, not a complete Lua parser."""
    tokens = re.sub(r"""--\[\[.*?\]\]|--[^\n]*|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*' """, "", source, flags=re.S | re.X)
    if "#" in tokens:
        raise ValueError("Lua 5.0 does not support the table length operator")


def instrument_lua(source: str) -> str:
    result = (
        source
        + "\n-- Presentation resources SHA256 "
        + probe.file_hash(Path(__file__))
        + "\n"
        + Path(__file__).with_suffix(".lua").read_text(encoding="utf-8")
    )
    validate_lua50_length_syntax(result)
    return result


def patch_pickup(data: bytes, report: dict, source: Path) -> tuple[bytes, dict]:
    """Use the proven timed HUD route with retail text/jingle, not a modal pickup."""
    manager = AssetManager(PathFileProvider(source), Game.CORRUPTION)
    retail = manager.get_parsed_asset(TEMPLATE_AREA, type_hint=Mrea)
    templates = {item.id.instance: item for layer in retail.script_layers for item in layer.instances}
    memo, audio = templates[0x13E], templates[0x13D]
    if memo.type_name != "MEMO" or audio.type_name != "STAU":
        raise ValueError("Retail pickup presentation template mismatch")
    if dict(probe.properties(audio._raw.base_property))[0x9D1A67A8] != struct.pack(">Q", AUDIO):
        raise ValueError("Retail expansion jingle differs")
    assets = {MEMO: manager.get_raw_asset(MEMO), AUDIO: manager.get_raw_asset(AUDIO)}
    if assets[MEMO].type != "STRG" or assets[AUDIO].type != "STRM":
        raise ValueError("Retail pickup resource type mismatch")
    if list(Strg.parse(assets[MEMO].data, Game.CORRUPTION).get_strings("ENGL"))[0] != "Missile Expansion acquired.":
        raise ValueError("Retail missile text mismatch")
    pak = Pak.parse(data, Game.CORRUPTION)
    area = Mrea.parse(pak.get_asset(probe.UNIVERSE_AREA).data, Game.CORRUPTION)
    layer = list(area.script_layers)[0]
    event = next(item for item in report["added_memos"] if item["event"] == "PickupMissileReceived")
    target = next(item for item in layer.instances if int(item.id) == event["id"])
    # Keep the already-tested non-modal HUD configuration, changing only text.
    target._raw.base_property = probe.replace_properties(
        target._raw.base_property,
        {0x9182250C: struct.pack(">Q", MEMO), 0x64124219: struct.pack(">I", 0)},
    )
    script = next(item for item in layer.instances if int(item.id) == report["lua_instance_id"])
    # Action shows the timed HUD memo; the independent Play link keeps the jingle.
    script._raw.connections = tuple(c for c in script.connections if c.target != target.id)
    script.add_connection(State.InternalState17, Message.Action, target.id)
    highest = max(item.id.instance for item_layer in area.script_layers for item in item_layer.instances)
    if highest >= 65535:
        raise ValueError("No free presentation instance ID")
    audio_id = InstanceId.new(0, target.id.area, highest + 1)
    copied = copy.deepcopy(audio._raw)
    copied.id, copied.connections = audio_id, ()
    layer._raw.script_instances.append(copied)
    script.add_connection(State.InternalState17, Message.Play, audio_id)
    for aid, resource in assets.items():
        if pak.get_asset(aid) is None:
            pak.add_asset(aid, resource)
        elif pak.get_asset(aid) != resource:
            raise ValueError("Conflicting pickup resource already in UniverseArea")
        pak.get_pak_file_with_id(aid).should_compress = False
    deps = area.get_section("dependencies_section")[0]
    insertion = deps.offsets[1]
    # STRM is loaded by the streaming path, not the area resource factory.
    # Retail MEMO/STAU areas and the patcher's DependencyHandler exclude STRM.
    extras = [
        Container(asset_id=aid, type=resource.type) for aid, resource in assets.items() if resource.type != "STRM"
    ]
    deps.dependencies[insertion:insertion] = extras
    for index in range(1, len(deps.offsets)):
        deps.offsets[index] += len(extras)
    layer.mark_modified()
    pak.replace_asset(probe.UNIVERSE_AREA, RawResource("MREA", area.build()))
    result = pak.build()
    checked = Pak.parse(result, Game.CORRUPTION)
    for aid, resource in assets.items():
        actual = checked.get_asset(aid).data
        # Uncompressed Corruption PAK entries include up to 63 bytes of FF alignment.
        if (
            actual[: len(resource.data)] != resource.data
            or len(actual) - len(resource.data) not in range(64)
            or any(value != 255 for value in actual[len(resource.data) :])
        ):
            raise ValueError("Pickup resource roundtrip differs")
    original = Pak.parse(data, Game.CORRUPTION)
    for aid, resource in original.get_all_assets():
        if aid != probe.UNIVERSE_AREA and checked.get_asset(aid).data != resource.data:
            raise ValueError("Unrelated resource changed during presentation patch")
    return result, {
        "kind": "retail_missile_memo_and_stream",
        "notification": "non_modal_timed_hud",
        "memo": f"{MEMO:016x}",
        "audio": f"{AUDIO:016x}",
        "trigger": "successful_native_application_only",
        "inventory_connections": 0,
        "native_atomicity": False,
    }
