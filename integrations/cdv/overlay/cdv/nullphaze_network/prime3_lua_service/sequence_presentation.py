# Non-modal catalog pickup text and retail streams for the private sequence. Boundary names
# here: notice, stream, observer_source, retail_output_states, event_actors.
"""Non-modal catalog pickup text and retail streams for the private sequence.

Names and stream choices follow NullPhaaze's reference-derived item catalog
(reference assembly cc6adead78316487fd24b4d4dad1b4477779f4b1e96b1a76eaf159689ed66a57).
This is presentation only; no pickup actor or inventory connection is copied.
"""

import copy
import hashlib
import struct
from pathlib import Path

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.enums.corruption import Message, State
from retro_data_structures.file_provider import PathFileProvider
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.script_object import InstanceId
from retro_data_structures.game_check import Game
from retro_data_structures.properties.corruption.objects.LUAScript import LUAScript

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header
from nullphaze_network.prime3_lua_service import presentation, probe

EXPANSION = presentation.AUDIO
UPGRADE = 0xE59596E4FC84A29B
GROUP_SIZE = 16
NAMES = (
    "Missile Expansion",
    "Missile Expansion",
    "Energy Tank",
    "Space Jump Boots",
    "Ice Missile",
    "Seeker Missile",
    "Progressive Missile",
    "Charge Beam",
    "Plasma Beam",
    "Nova Beam",
    "Progressive Beam",
    "Grapple Lasso",
    "Grapple Swing",
    "Grapple Voltage",
    "Morph Ball Bomb",
    "Scan Visor",
    "Combat Visor",
    "Command Visor",
    "X-Ray Visor",
    "Screw Attack",
    "Hazard Shield",
    "Morph Ball",
    "Boost Ball",
    "Spider Ball",
    "Hypermode",
    "Hyper Ball",
    "Hyper Missile",
    "Hyper Grapple",
    "Ship Missile Expansion",
    "Ship Missile Expansion",
    "Ship Grapple Beam",
    *("Energy Cell" for _ in range(9)),
    "Missile Launcher",
    "Missile Launcher",
    "Ship Missile",
    "Ship Missile",
)


def notice(step):
    item = step["catalog_id"]
    if item in (6, 10):
        native = step["operations"][0][0]
        return {5: "Ice Missile", 6: "Seeker Missile", 1: "Plasma Beam", 2: "Nova Beam"}[native] + " acquired!"
    return NAMES[item] + " acquired!"


def stream(step):
    return EXPANSION if step["catalog_id"] in (0, 1, 2, 28, 29, *range(31, 40), 42, 43) else UPGRADE


def observer_source(first, last):
    return """-- Read-only presentation observer; never advances networking or grants.
local elapsed = 0
local seen = 0
function OnThink(dt)
    if type(dt) ~= "number" or dt ~= dt or dt <= 0 or dt > 1 then return end
    elapsed = elapsed + dt
    if elapsed < 0.5 then return end
    elapsed = 0
    local status = CP3WNetworkStatus()
    if type(status) ~= "string" or string.len(status) ~= 125 then return end
    local count = tonumber(string.sub(status, 91, 98), 16)
    local attempts = tonumber(string.sub(status, 100, 107), 16)
    if count and count > seen and count == attempts and count >= FIRST and count <= LAST then
        SendEvent("SequenceReceived" .. tostring(count))
    end
    seen = count or seen
end
""".replace("FIRST", str(first)).replace("LAST", str(last))


def retail_output_states(dol):
    if hashlib.sha256(dol).hexdigest() != probe.RETAIL_HASH:
        raise ValueError("Unknown executable Lua event vocabulary")
    header = parse_dol_header(dol)
    result = {}
    for index in range(160):
        offset = header.offset_for_address(0x8057E548 + index * 8)
        address, state = struct.unpack_from(">I4s", dol, offset)
        if not address:
            break
        start = header.offset_for_address(address)
        name = dol[start : start + 128].split(b"\0", 1)[0].decode("ascii")
        if name.startswith("InternalState"):
            result[name] = state.decode("ascii")
    if result != {f"InternalState{i}": f"IS{i:02d}" for i in range(20)}:
        raise ValueError("Retail Lua event state table differs")
    return result


def event_actors(layer, script, highest, steps):
    actors = []
    script._raw.connections = ()
    for group in range((len(steps) + GROUP_SIZE - 1) // GROUP_SIZE):
        subset = steps[group * GROUP_SIZE : (group + 1) * GROUP_SIZE]
        target = script
        if group:
            copied = copy.deepcopy(script._raw)
            copied.id = InstanceId.new(0, script.id.area, highest + group)
            copied.connections = ()
            layer._raw.script_instances.append(copied)
            target = next(item for item in layer.instances if item.id == copied.id)
        props = target.get_properties()
        if not isinstance(props, LUAScript):
            raise ValueError("Expected LUAX presentation event owner")
        props.unknown_0xed4a2787 = "".join(
            f'"SequenceReceived{step["sequence"]}" "InternalState{index}"' for index, step in enumerate(subset)
        )
        if group:
            props.unknown_0xa1ecc54b = observer_source(subset[0]["sequence"], subset[-1]["sequence"])
            props.editor_properties.name = f"CP3W read-only pickup event bank {group}"
        target.set_properties(props)
        actors.append(target)
    return actors


def patch_pickups(data: bytes, report: dict, source: Path, steps: list) -> tuple[bytes, dict]:
    supported_states = retail_output_states((source / "sys/main.dol").read_bytes())
    manager = AssetManager(PathFileProvider(source), Game.CORRUPTION)
    retail = manager.get_parsed_asset(presentation.TEMPLATE_AREA, type_hint=Mrea)
    template = next(item for layer in retail.script_layers for item in layer.instances if item.id.instance == 0x13D)
    if template.type_name != "STAU":
        raise ValueError("Retail pickup audio actor differs")
    pak = Pak.parse(data, Game.CORRUPTION)
    area = Mrea.parse(pak.get_asset(probe.UNIVERSE_AREA).data, Game.CORRUPTION)
    layers = list(area.script_layers)
    layer = layers[0]
    script = next(item for item in layer.instances if int(item.id) == report["lua_instance_id"])
    highest = max(item.id.instance for part in layers for item in part.instances)
    audio_ids = {}
    for index, aid in enumerate((EXPANSION, UPGRADE), 1):
        resource = manager.get_raw_asset(aid)
        if resource.type != "STRM":
            raise ValueError("Catalog pickup audio is not a retail stream")
        existing = pak.get_asset(aid)
        if existing is None:
            pak.add_asset(aid, resource)
        elif existing != resource:
            raise ValueError("Conflicting pickup stream")
        pak.get_pak_file_with_id(aid).should_compress = False
        copied = copy.deepcopy(template._raw)
        copied.id = InstanceId.new(0, script.id.area, highest + index)
        copied.connections = ()
        copied.base_property = probe.replace_properties(copied.base_property, {0x9D1A67A8: struct.pack(">Q", aid)})
        layer._raw.script_instances.append(copied)
        audio_ids[aid] = copied.id
    actors = event_actors(layer, script, highest + len(audio_ids), steps)
    states = [state for state in State if state.name.startswith("InternalState")]
    routes = []
    for step in steps:
        index = step["sequence"] - 1
        event = next(row for row in report["added_memos"] if row["event"] == f"SequenceReceived{index + 1}")
        memo = next(item for item in layer.instances if int(item.id) == event["id"])
        fields = dict(probe.properties(memo._raw.base_property))
        if fields[0x4AB3B95B] != bytes(4) or fields[0xFB0E87DA] != b"\0" or memo.connections:
            raise ValueError("Item notice must remain non-modal and inventory-free")
        target = actors[index // GROUP_SIZE]
        state = states[index % GROUP_SIZE]
        target.add_connection(state, Message.Action, memo.id)
        target.add_connection(state, Message.Play, audio_ids[stream(step)])
        routes.append({"sequence": index + 1, "text": notice(step), "stream": f"{stream(step):016x}"})
    # STRM must not enter the area factory dependency list; STAU streams it.
    dependencies = area.get_section("dependencies_section")[0].dependencies
    if any(dep.asset_id in audio_ids for dep in dependencies):
        raise ValueError("Stream incorrectly preloaded as an area resource")
    layer.mark_modified()
    pak.replace_asset(probe.UNIVERSE_AREA, probe.RawResource("MREA", area.build()))
    result = pak.build()
    checked = Pak.parse(result, Game.CORRUPTION)
    for aid, resource in Pak.parse(data, Game.CORRUPTION).get_all_assets():
        if aid != probe.UNIVERSE_AREA and checked.get_asset(aid).data != resource.data:
            raise ValueError("Unrelated resource changed during sequence presentation")
    return result, {
        "kind": "catalog_acquired_text_and_retail_pickup_streams",
        "routes": routes,
        "notification": "non_modal_timed_hud",
        "inventory_connections": 0,
        "trigger": "successful_native_application_only",
        "event_banks": len(actors),
        "events_per_bank_limit": GROUP_SIZE,
        "runtime_supported_internal_states": supported_states,
    }
