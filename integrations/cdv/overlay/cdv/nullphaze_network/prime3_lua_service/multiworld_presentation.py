# Only a committed receipt creates a pickup notice. One current-area dispatcher owns each
# complete native event bank; claiming presentation must never advance the inventory
# receipt. Boundary names here: connection_notices, connection_source, plan, read_templates,
# bank_source.
"""GPL addon: receipt-driven timed text and native jingles from one owner."""
from __future__ import annotations

import copy
import hashlib
import struct
from dataclasses import replace

from construct import Container
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.resources import make_string_table
from retro_data_structures.enums.corruption import Message, State
from retro_data_structures.formats.script_object import InstanceId, ScriptInstance, ScriptInstanceRaw
from retro_data_structures.game_check import Game
from retro_data_structures.properties.corruption.objects.LUAScript import LUAScript

from nullphaze_network.prime3_lua_service import connection_audio, presentation, probe, sequence_presentation
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea, next_instance_id
from randovania.game.game_enum import RandovaniaGame
from randovania.game_description import default_database
from randovania.games.prime3.multiworld.seed_compiler import seed_tables

# Retail LUAX's event-name table exposes InternalState0 through 19. RDS also
# knows higher ISxx codes, but those names cannot be bound by retail Lua.
DISPATCH_STATES = tuple(State[f"InternalState{index:02d}"] for index in range(20))


def connection_notices():
    return [{"name": name, "text": text, "audio": connection_audio.stream_id(name), "string_id": int.from_bytes(hashlib.sha256(
        f"Nullphaze connection notice/{name}/{text}".encode()).digest()[:8], "big")}
        for name, text in (("lost", "Multiworld connection lost."),
                           ("restored", "Multiworld connection restored."))]


def connection_source(world, area):
    return f'''-- Once-per-transition connection notices; no inventory or network calls.
local elapsed=0
function OnThink(dt)
    if type(dt)~="number" or dt~=dt or dt<=0 or dt>1 then return end
    elapsed=elapsed+dt
    if elapsed<0.5 then return end
    elapsed=0
    local location=CP3WReadLocation()
    if type(location)~="string" or string.sub(location,1,33)~="{world}:{area}" then return end
    local notice=CP3WClaimConnectionNotice()
    if notice=="lost" then SendEvent("MWConnectionLost") end
    if notice=="restored" then SendEvent("MWConnectionRestored") end
end
'''


def plan(manifest, mapping):
    recipes, incoming, _ = seed_tables(manifest, mapping)
    database = default_database.resource_database_for(RandovaniaGame.METROID_PRIME_CORRUPTION)
    rows = []
    for index, (key, recipe) in enumerate(recipes.items()):
        if key not in incoming:
            continue
        for stage in range(max(1, len(recipe.progression))):
            name = manifest["incoming_recipes"][key]["name"]
            if len(recipe.progression) > 1:
                name = database.item[recipe.progression[stage][0]].long_name
            name = "".join(c if c.isprintable() and c != "&" else " " for c in name)[:120]
            event = index * 4 + stage
            resources = {resource for resource, _ in (*recipe.progression, *recipe.extra)}
            expansion = bool(resources & ({4, 20, 22, 44, 61, 62} | set(range(23, 32))))
            sender = manifest["incoming_recipes"][key].get("sender_name")
            if manifest.get("incoming_presentation") == "sender-v1":
                sender = "".join(c if c.isprintable() and c != "&" else " " for c in sender)[:64]
                text = f"Received {name} from {sender}!"
            else:
                text = name + " received!"  # Existing exports keep their original recipe/history identity.
            identity = int.from_bytes(hashlib.sha256(
                f"Nullphaze incoming/{manifest['world_uuid']}/{event}/{text}".encode()).digest()[:8], "big")
            rows.append({"event": event, "text": text, "string_id": identity,
                         "audio": sequence_presentation.EXPANSION if expansion else sequence_presentation.UPGRADE})
    if len({row["event"] for row in rows}) != len(rows) or any(row["event"] >= 1024 for row in rows):
        raise ValueError("Incoming presentation exceeds the native event banks")
    return rows


def read_templates(files):
    memo = audio = None
    streams = {}
    # Read only the required script templates and streams from this seed's
    # staged resources. No retail PAK/MREA is restored over randomized output.
    for path in sorted(files.glob("*.pak")):
        for resource in Archive(path).resources:
            if resource.identity == probe.UNIVERSE_AREA and resource.kind == b"MREA":
                area = SeedMrea.parse(resource.read(), Game.CORRUPTION)
                memo = copy.deepcopy(next(actor._raw for layer in area.script_layers for actor in layer.instances
                                          if int(actor.id) == probe.MEMO_TEMPLATE))
            if resource.identity == presentation.TEMPLATE_AREA and resource.kind == b"MREA":
                area = SeedMrea.parse(resource.read(), Game.CORRUPTION)
                audio = copy.deepcopy(next(actor._raw for layer in area.script_layers for actor in layer.instances
                                           if actor.id.instance == 0x13d))
            if resource.identity in (sequence_presentation.EXPANSION, sequence_presentation.UPGRADE):
                if resource.kind != b"STRM" or resource.compressed:
                    raise ValueError("Pickup jingle must be a native uncompressed STRM")
                streams[resource.identity] = replace(resource, source=None, offset=0, data=resource.read())
    if memo is None or audio is None or memo.type != "MEMO" or audio.type != "STAU" or len(streams) != 2:
        raise ValueError("This randomized seed lacks the required pickup presentation templates")
    from retro_data_structures.formats.cmpd import CompressedWiiPakResource
    audio_archive = Archive(files / "InGameAudio.pak")
    for event, (_, identity) in connection_audio.CUES.items():
        matches = [r for r in audio_archive.resources if r.identity == identity and r.kind == b"CSMP"]
        if len(matches) != 1:
            raise ValueError(f"Missing or ambiguous connection cue: {event}")
        sample = matches[0].read()
        if matches[0].compressed:
            sample = CompressedWiiPakResource.parse(sample, target_game=Game.CORRUPTION)
        stream = connection_audio.make_stream(event, sample, streams[sequence_presentation.EXPANSION].read())
        streams[stream.identity] = stream
    return memo, audio, streams


def bank_source(world, area, bank):
    return f'''-- Claim one committed notice only from its owning current room.
local elapsed=0
function OnThink(dt)
    if type(dt)~="number" or dt~=dt or dt<=0 or dt>1 then return end
    elapsed=elapsed+dt
    if elapsed<0.5 then return end
    elapsed=0
    local location=CP3WReadLocation()
    if type(location)~="string" or string.sub(location,1,33)~="{world}:{area}" then return end
    local event=CP3WClaimMWBank{bank}()
    if type(event)=="string" then
        local number=tonumber(event,16)
        if number and number>={bank*16} and number<{bank*16+16} then SendEvent("MWReceived"..tostring(number)) end
    end
end
'''


def presentation_groups(rows):
    """Pack whole native banks into the script's available internal states.

    A bank must have exactly one claimant: splitting it between scripts can
    consume a notice before the script owning its text sees it.
    """
    capacity = len(DISPATCH_STATES) - 2
    # Native event = recipe * 4 + applied progression stage; banks contain 16
    # events. Keep a complete bank in one dispatcher even when another script
    # has spare outputs, because claiming consumes that pending notice.
    groups = [[]]
    for bank in sorted({row["event"] // 16 for row in rows}):
        members = [row for row in rows if row["event"] // 16 == bank]
        if len(members) > capacity:
            raise ValueError("Native presentation bank exceeds script output states")
        if len(groups[-1]) + len(members) > capacity:
            groups.append([])
        groups[-1].extend(members)
    return groups


def dispatcher_source(world, area, rows, *, service=False):
    if world is None:
        raise ValueError("Lua polling requires an owning gameplay room")
    banks = sorted({row["event"] // 16 for row in rows})
    allowed = ",".join(f'[{row["event"]}]=true' for row in rows)
    polls = "\n".join(f'''    local event=CP3WClaimMWBank{bank}()
    if type(event)=="string" then
        local number=tonumber(event,16)
        if number and allowed[number] then SendEvent("MWReceived"..tostring(number)) end
    end''' for bank in banks)
    service_calls = '''    CP3WReceiptProbeTick()
    local notice=CP3WClaimConnectionNotice()
    if notice=="lost" then SendEvent("MWConnectionLost") end
    if notice=="restored" then SendEvent("MWConnectionRestored") end
''' if service else ""
    return f'''-- One dispatcher owns each complete native bank.
local elapsed=0
local allowed={{{allowed}}}
function OnThink(dt)
    if type(dt)~="number" or dt~=dt or dt<=0 or dt>1 then return end
    elapsed=elapsed+dt
    if elapsed<0.5 then return end
    elapsed=0
    local location=CP3WReadLocation()
    if type(location)~="string" or string.sub(location,1,33)~="{world}:{area}" then return end
{service_calls}{polls}
end
'''


def append(area, world, entry, rows, templates, *, shared_targets=None, targets_only=False):
    memo_template, audio_template, _ = templates
    layer = next(iter(area.script_layers))
    highest = max((actor.id.instance for part in [*area.script_layers, area.generated_objects_layer]
                   for actor in part.instances), default=0)

    def add(raw):
        nonlocal highest
        raw.id = next_instance_id(area, entry["index"])
        highest = raw.id.instance
        raw.connections = ()
        layer._raw.script_instances.append(raw)
        return ScriptInstance(raw, Game.CORRUPTION, on_modify=layer.mark_modified)

    target_owner = shared_targets is None
    targets = {} if target_owner else shared_targets
    audio_ids = {}
    if target_owner:
        for stream in sorted({row["audio"] for row in rows}):
            raw = copy.deepcopy(audio_template)
            raw.base_property = probe.replace_properties(raw.base_property, {0x9D1A67A8: struct.pack(">Q", stream)})
            audio_ids[stream] = add(raw).id
    outputs = DISPATCH_STATES
    event_owners = {}
    observer = None
    for index, group in enumerate([] if targets_only else presentation_groups(rows)):
        props = LUAScript(unknown_0xa1ecc54b=dispatcher_source(
            world, entry["mrea_id"], group, service=index == 0))
        props.editor_properties.name = f"Nullphaze current-area presentation dispatcher {index}"
        mappings = [(f'MWReceived{row["event"]}', outputs[offset]) for offset, row in enumerate(group)]
        if index == 0:
            mappings.extend((("MWConnectionLost", outputs[-2]), ("MWConnectionRestored", outputs[-1])))
        props.unknown_0xed4a2787 = "".join(
            f'"{event}" "InternalState{int(state.name.removeprefix("InternalState"))}"'
            for event, state in mappings)
        script = add(ScriptInstanceRaw("LUAX", 0, (), props.to_bytes(Game.CORRUPTION)))
        if index == 0:
            observer = script
        for offset, row in enumerate(group):
            event_owners[row["event"]] = script, outputs[offset]
    dependencies = area.get_section("dependencies_section")[0]
    for index, row in enumerate(connection_notices()):
        key = row["name"]
        if not target_owner:
            memo_id, sound_id = targets[key]
            observer.add_connection(outputs[-2 + index], Message.Action, memo_id)
            observer.add_connection(outputs[-2 + index], Message.Play, sound_id)
            continue
        raw = copy.deepcopy(memo_template)
        raw.base_property = probe.replace_properties(raw.base_property, {
            0x9182250C: struct.pack(">Q", row["string_id"]), 0x64124219: bytes(4),
            0x1A26C1CC: struct.pack(">f", 5.0), 0xAFD0158E: b"\0", 0xFB0E87DA: b"\0",
        })
        memo = add(raw)
        if observer is not None:
            observer.add_connection(outputs[-2 + index], Message.Action, memo.id)
        sound = copy.deepcopy(audio_template)
        sound.base_property = probe.replace_properties(sound.base_property, {
            0x9D1A67A8: struct.pack(">Q", row["audio"]),
            0x90AA341F: bytes(4), 0x7C269EBC: bytes(4),  # No fade swallowing the short cue.
            0x34B152C4: b"\0", 0x6E0E81F8: b"\0", 0x85707354: b"\0",
        })
        sound_id = add(sound).id
        targets[key] = memo.id, sound_id
        if observer is not None:
            observer.add_connection(outputs[-2 + index], Message.Play, sound_id)
        if any(dep.asset_id == row["string_id"] for dep in dependencies.dependencies):
            raise ValueError("Connection notice dependency identity collision")
        dependencies.dependencies.insert(dependencies.offsets[1], Container(asset_id=row["string_id"], type="STRG"))
        for offset in range(1, len(dependencies.offsets)):
            dependencies.offsets[offset] += 1
    for row in rows:
        if not target_owner:
            memo_id, sound_id = targets[row["event"]]
            bank, state = event_owners[row["event"]]
            bank.add_connection(state, Message.Action, memo_id)
            bank.add_connection(state, Message.Play, sound_id)
            continue
        raw = copy.deepcopy(memo_template)
        raw.base_property = probe.replace_properties(raw.base_property, {
            0x9182250C: struct.pack(">Q", row["string_id"]), 0x64124219: bytes(4),
            0x1A26C1CC: struct.pack(">f", 5.0), 0xAFD0158E: b"\0", 0xFB0E87DA: b"\0",
        })
        memo = add(raw)
        targets[row["event"]] = memo.id, audio_ids[row["audio"]]
        if not targets_only:
            bank, state = event_owners[row["event"]]
            bank.add_connection(state, Message.Action, memo.id)
            bank.add_connection(state, Message.Play, audio_ids[row["audio"]])
        if any(dep.asset_id == row["string_id"] for dep in dependencies.dependencies):
            raise ValueError("Incoming text dependency identity collision")
        dependencies.dependencies.insert(dependencies.offsets[1], Container(asset_id=row["string_id"], type="STRG"))
        for index in range(1, len(dependencies.offsets)):
            dependencies.offsets[index] += 1
    layer.mark_modified()
    return targets


def resources(rows, templates):
    result = []
    for row in [*rows, *connection_notices()]:
        text = make_string_table([row["text"]])
        result.append(Resource(row["string_id"], b"STRG", 0, len(text), data=text))
    for identity in sorted({row["audio"] for row in [*rows, *connection_notices()]}):
        result.append(templates[2][identity])
    return result
