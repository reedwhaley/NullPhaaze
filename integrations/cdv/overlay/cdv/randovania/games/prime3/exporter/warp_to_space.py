# Native save-refusal warp addon, independent of the CDV networking runtime. Boundary names
# here: prompt_resource, transition_attachments, patch_station, patch_space, install.
"""Native save-refusal warp addon, independent of the CDV networking runtime.

The departure TEL1 is taken from the Elysian Seed's aftermath area, with only
its destination restored after the core's space-removal redirect. Its native
presentation attachments are retained; reward scripts and story controllers
are never copied.
"""
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import struct
from pathlib import Path

from construct import Container
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.binary import Reader
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea, next_instance_id
from nullphaze_network.prime3_lua_service.probe import properties, replace_properties
from retro_data_structures.enums.corruption import State, Message
from retro_data_structures.formats.script_object import ScriptInstanceRaw
from retro_data_structures.formats.script_object import _try_quick_get_name
from retro_data_structures.formats.strg import Strg
from retro_data_structures.game_check import Game
from retro_data_structures.properties.corruption.objects.SpecialFunction import Function
from retro_data_structures.properties.corruption.objects.GuiMenu import GuiMenu
from retro_data_structures.properties.corruption.objects.ScriptLayerController import ScriptLayerController
from retro_data_structures.properties.corruption.objects.Timer import Timer
from randovania.games.prime3.warp_to_space import SAVE_AREAS
from randovania.games.prime3.exporter.main_menu import _decoded, build_sequential_strings

SPACE_WORLD = 0x32DA226774D68D87
SPACE_AREA = 0xBD0BC908940A1A0C
SPACE_INTERNAL = 0x717CE5E51F7F836E
DEPARTURE_AREA = 0xEAD7F86FB4ADFB01
PROMPT_ID = int.from_bytes(hashlib.sha256(b'NullPhaaze:warp-to-space:prompt:v1').digest()[:8], 'big')
PROMPT = ('Warp to space?', 'Yes', 'No')
PROMPT_TEMPLATE = 0x40618D611592ECB8
MARKER = 'NullPhaaze Warp to Space'
DEPARTURE_SHA256 = '03700663d46ba24f3a83c51ef243752e3f2d4eec6d3c89ab473eb09c6cabb31a'
# Audited closure of the departure and its four presentation attachments. The native
# audio loader synchronously resolves both CSMP choices; omitting a leaf can
# halt the game before the station finishes loading.
TRANSITION_DEPENDENCIES = (
    (0x0155C589C830D69D, 'TXTR'),
    (0x03DCCC88BFAAA653, 'SAND'),
    (0x04702B4D266C6D63, 'SWHC'),
    (0x0AC46B59B70CBD22, 'CAUD'),
    (0x0B6C9562AF18E77C, 'TXTR'),
    (0x0C23EFA18C5A6649, 'PART'),
    (0x0DFB24A2E9056091, 'PART'),
    (0x12BAF9ECDF773034, 'TXTR'),
    (0x154526A63879C227, 'SAND'),
    (0x15B5FDE48C526619, 'ANIM'),
    (0x1CA57C901A17DCB8, 'TXTR'),
    (0x1FFC7F3BB4AA2666, 'CHAR'),
    (0x2037943B8C4730E8, 'PART'),
    (0x2296DACA4189C6C9, 'CSMP'),
    (0x2692D9751600CC80, 'TXTR'),
    (0x29AD0F891B3C2D2C, 'TXTR'),
    (0x29DDC762D596C516, 'TXTR'),
    (0x2D4A411A8D760CA8, 'PART'),
    (0x2F9D3E340FD3AA50, 'ANIM'),
    (0x309D5D7907019865, 'ANIM'),
    (0x364E357E63AF7640, 'TXTR'),
    (0x37B89613E4C3F6C8, 'TXTR'),
    (0x3DEF26D323542D26, 'CMDL'),
    (0x402FC75ACB2C6215, 'TXTR'),
    (0x404EE4F624FB1D76, 'TXTR'),
    (0x40CC1C712E18F585, 'SWHC'),
    (0x413CAE1DDB12881D, 'TXTR'),
    (0x41EA3B1559D7A659, 'TXTR'),
    (0x434E8F026EB716A1, 'TXTR'),
    (0x44384A0CB184F09F, 'CHAR'),
    (0x4512F3D53C550B4F, 'SAND'),
    (0x48AECB7069CC8B2C, 'CMDL'),
    (0x4925ED60B950072D, 'SAND'),
    (0x4AE9F0B6205B5794, 'CINF'),
    (0x4B898C64FD37621C, 'PART'),
    (0x4F56380B6B1747FE, 'CSMP'),
    (0x4FCF41FDCA23842B, 'TXTR'),
    (0x60AB29D22D0BE7CA, 'TXTR'),
    (0x61B5941BEF5960CD, 'TXTR'),
    (0x647254F6B02FC17C, 'TXTR'),
    (0x65582EFFB8057F00, 'TXTR'),
    (0x6CE5D8CC6D8DD898, 'PART'),
    (0x86502BF5936BAB90, 'CMDL'),
    (0x9147E5B8653A8325, 'CMDL'),
    (0x91C2077D1EA3827E, 'TXTR'),
    (0x9276B8F0CDB7CD78, 'TXTR'),
    (0x94605BB7CBBFF202, 'PART'),
    (0x966E8F25DBD20B06, 'PART'),
    (0x9B37A4C4C945CD5D, 'TXTR'),
    (0x9BD4DF3D1D8F07D1, 'CSKR'),
    (0x9D24D559162EC227, 'CHAR'),
    (0xA0D0F1E2F81398A3, 'TXTR'),
    (0xA2A88006BA920003, 'CINF'),
    (0xA40F3050D00398A6, 'SWHC'),
    (0xA508F940B6705AB9, 'TXTR'),
    (0xB1ADFDEE288A7CE6, 'TXTR'),
    (0xB435145729C0D878, 'PART'),
    (0xB486B8238686516F, 'CSKR'),
    (0xBB47E6F8EC7F28BE, 'TXTR'),
    (0xBBC07FBC12FB9BB1, 'TXTR'),
    (0xBE98C1C8E7786FBF, 'ANIM'),
    (0xBFFF4D12C4DF0C1A, 'TXTR'),
    (0xC1D4240C372C8BB4, 'TXTR'),
    (0xC1FA386D98CA5C49, 'SWHC'),
    (0xC9395C581C431670, 'SWHC'),
    (0xC94BF2CD27C741B2, 'CMDL'),
    (0xD4CC37C50AD39C62, 'PART'),
    (0xD8CCF1DEF421008F, 'TXTR'),
    (0xD95DEAF28F500225, 'TXTR'),
    (0xDAFC87B47B3DBA90, 'TXTR'),
    (0xDC4AFCBF31C375BB, 'TXTR'),
    (0xEAFC3DFF4D6107CC, 'TXTR'),
    (0xEE09F652F58D7DF1, 'CHAR'),
    (0xEE1F446D3144CCDF, 'TXTR'),
    (0xEEA34BD701188329, 'TXTR'),
    (0xFB02E8830C235A7F, 'TXTR'),
)


def _name(actor):
    return _try_quick_get_name(actor._raw.base_property) or ''


def prompt_resource(source):
    table = Strg.parse(_decoded(source), Game.CORRUPTION)
    if table._raw.name_table != {'message': 0, 'choice0': 1, 'choice1': 2}:
        raise ValueError('Warp to Space: unsupported retail confirmation string names')
    for language in table.get_language_list():
        if len(table.get_strings(language)) != 3:
            raise ValueError('Warp to Space: unexpected confirmation string count')
        table.set_string_list(list(PROMPT), language)
    raw = build_sequential_strings(table)
    return Resource(PROMPT_ID, b'STRG', 0, 0).updated(raw)


def _actor(area, identity, kind):
    found = [a for layer in area.script_layers for a in layer.instances if int(a.id) == identity]
    if len(found) != 1 or found[0].type_name != kind:
        raise ValueError(f'Warp to Space: expected one {kind} actor {identity:08X}; unsupported image structure')
    return found[0]


def _space_layers(world):
    """Read the retained MLVL tail without normalizing its unknown envelopes."""
    r = Reader(world)
    if r.read(8) != bytes.fromhex('DEAFBABE00000019'):
        raise ValueError('Warp to Space requires Corruption MLVL 25')
    r.read(28)
    count = r.count(105)
    for _ in range(count):
        r.read(96)
        r.read(r.count(2)*2)
        for _ in range(r.count(8)):
            r.read(r.count(8)*8)
            r.read(r.count(12)*12)
        r.cstring()
    r.read(13)
    flag_count = r.count(12)
    sizes = []
    for _ in range(flag_count):
        sizes.append(r.u32())
        r.read(8)
    names = [r.cstring() for _ in range(r.count(1))]
    guids = [r.read(16) for _ in range(r.count(16))]
    offsets = [r.u32() for _ in range(r.count(4))]
    if count != 3 or flag_count != count or len(names) != len(guids) or len(offsets) != count or sizes[2] != 9:
        raise ValueError(f'Warp to Space: unexpected space layer table: {count}, {flag_count}, {sizes}, '
                         f'{len(names)}, {len(guids)}, {offsets}')
    start = offsets[2]
    result = [(names[start+i], guids[start+i]) for i in range(9)]
    if result[2] != ('Skytown', bytes.fromhex('7a5e89dc47229e4e96b06d2268d70a6a')) or result[6] != (
            'Ship Cockpit (NEW)', bytes.fromhex('0827feff16ecec488c2d39122bb65586')):
        raise ValueError('Warp to Space: unsupported ship layer identities')
    return result


def _append(area, entry_index, props):
    layer = next(area.script_layers)
    identity = next_instance_id(area, entry_index)
    layer._raw.script_instances.append(ScriptInstanceRaw(props.object_type(), identity, (), props.to_bytes(Game.CORRUPTION)))
    layer.mark_modified()
    return _actor(area, int(identity), props.object_type())


def _dependency(area, identity, kind):
    deps = area.get_section('dependencies_section')[0]
    if not any(d.asset_id == identity for d in deps.dependencies[:deps.offsets[1]]):
        deps.dependencies.insert(deps.offsets[1], Container(asset_id=identity, type=kind))
        for i in range(1, len(deps.offsets)):
            deps.offsets[i] += 1


def _teleporter_modules(area):
    # Save rooms have no retail teleporters, so their RSOS layer tables do not
    # load these factories. Copying TEL1 alone leaves the area unable to finish
    # loading. Register the same pair used by the Elysian departure area.
    table = area.get_section('rso_module_list_section')[0]
    for name in ('RSO_ScriptWorldTeleporter.rso', 'RSO_ScriptWorldTeleporterAttributes.rso'):
        if name not in table.modules[:table.offsets[1]]:
            table.modules.insert(table.offsets[1], name)
            for i in range(1, len(table.offsets)):
                table.offsets[i] += 1


def transition_attachments(source):
    links = _actor(source, 0x5000B, 'TEL1').connections
    expected_links = {
        (State.InternalState06, Message.Attach, 0x5000C),
        (State.InternalState09, Message.Attach, 0x5000C),
        (State.InternalState07, Message.Attach, 0x5000D),
        (State.InternalState10, Message.Attach, 0x5000D),
        (State.InternalState05, Message.Attach, 0x5000E),
        (State.InternalState08, Message.Attach, 0x5000E),
        (State.InternalState11, Message.Attach, 0x50011),
    }
    if len(links) != 7 or {(c.state, c.message, int(c.target)) for c in links} != expected_links:
        raise ValueError('Warp to Space: unsupported departure presentation links')
    expected = (
        (0x0005000C, 'CINE', '70abc7c8feceeeb04ea5d105b971ed1c4a6fd0e8f340cab728e87c43ea84d379'),
        (0x0005000D, 'DLHT', 'e19147301a342a42251dd027808ca0131377afcfe86ae5b44e23ec307579add9'),
        (0x0005000E, 'ACTR', '7c943de05815ac2d407eef023383a73534968e5fc8af46bfcec74f83397e45e5'),
        (0x00050011, 'WTAT', '2fe694292967e1592c2977e6b8d131427f40d8c55b4c08441377b257e8cd99bc'),
    )
    result = []
    for identity, kind, digest in expected:
        actor = _actor(source, identity, kind)
        raw = actor._raw.base_property
        # The core makes retail cinematics skippable (0x854 -> 0xA54).
        # Restore only this copied travel camera to its native transition flags.
        if identity == 0x5000C and hashlib.sha256(raw).hexdigest() == (
                '3a7578a3b6fc21c5690dc96adcd332e589a9c6991cc77b5d97047570d1f63ed9'):
            raw = replace_properties(raw, {0x05C5FC6E: struct.pack('>I', 0x854)})
        if actor.connections or hashlib.sha256(raw).hexdigest() != digest:
            raise ValueError(f'Warp to Space: unsupported departure attachment {identity:08X}')
        result.append(ScriptInstanceRaw(actor.type_name, actor.id, (), raw))
    return result


def patch_station(raw, *, area_id, index, departure, layers, attachments):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    originals = [[copy.deepcopy(a._raw) for a in layer.instances] for layer in area.script_layers]
    actors = [a for layer in area.script_layers for a in layer.instances]
    if any(_name(a).startswith(MARKER) for a in actors):
        raise ValueError('Warp to Space already installed')
    saves = [a for a in actors if a.type_name == 'SPFN' and _name(a) == 'Save Station - Save Progress']
    if len(saves) != 1:
        raise ValueError(f'Warp to Space: missing save station in {area_id:016X}')
    save = saves[0]
    if save.get_properties().function.value != 3039339760:
        raise ValueError('Warp to Space: save function differs from retail')
    refusal = [c for c in save.connections if c.state == State.Zero and c.message == Message.Close]
    success = [c for c in save.connections if c.state == State.MaxReached and c.message == Message.Open]
    if len(refusal) != 1 or len(success) != 1 or refusal[0].target != success[0].target:
        raise ValueError('Warp to Space: unsupported save/refusal connections')
    switch = _actor(area, int(refusal[0].target), 'SWTC')
    if not any(c.state == State.Closed for c in switch.connections):
        raise ValueError('Warp to Space: save result switch has no refusal branch')

    menu_props = GuiMenu(text=PROMPT_ID, choice2_enabled=False, choice3_enabled=False)
    menu_props.editor_properties.name = MARKER + ' - Confirm (Yes / No)'
    menu = _append(area, index, menu_props)
    delay_props = Timer(time=0.25)
    delay_props.editor_properties.name = MARKER + ' - Wait for save prompt to close'
    delay = _append(area, index, delay_props)
    delay.add_connection(State.Zero, Message.Action, menu.id)
    save.add_connection(State.Zero, Message.ResetAndStart, delay.id)

    # No resource grants, checkpoint callbacks, or dependency on a client.
    teleport_id = next_instance_id(area, index)
    next(area.script_layers)._raw.script_instances.append(ScriptInstanceRaw('TEL1', teleport_id, (), departure))
    teleporter = _actor(area, int(teleport_id), 'TEL1')
    # The transition dereferences its attached camera during Think, before the
    # world changes. These are presentation-only native actors with no outputs.
    if [(int(a.id), a.type) for a in attachments] != [
            (0x5000C, 'CINE'), (0x5000D, 'DLHT'), (0x5000E, 'ACTR'), (0x50011, 'WTAT')]:
        raise ValueError('Warp to Space: incomplete departure presentation attachments')
    targets = {}
    for template in attachments:
        if template.connections:
            raise ValueError('Warp to Space: departure attachment has unexpected outputs')
        identity = next_instance_id(area, index)
        next(area.script_layers)._raw.script_instances.append(
            ScriptInstanceRaw(template.type, identity, (), template.base_property))
        targets[int(template.id)] = identity
    for states, target in (
            ((State.InternalState06, State.InternalState09), 0x5000C),
            ((State.InternalState07, State.InternalState10), 0x5000D),
            ((State.InternalState05, State.InternalState08), 0x5000E),
            ((State.InternalState11,), 0x50011)):
        for state in states:
            teleporter.add_connection(state, Message.Attach, targets[target])
    # Native GMNU outputs choice 0 as InternalState00, choice 1 as 01.
    # Yes is choice 0; No and cancel have no warp connection.
    for layer_index in (2, 3, 4, 5, 6, 7, 8):
        controller_props = ScriptLayerController()
        controller_props.editor_properties.name = MARKER + f' - Ship layer {layer_index}'
        controller_props.master_layer.area_id = SPACE_INTERNAL
        # The corrected schema exposes the native 16-byte layer GUID directly.
        # Preserve those bytes; the previous reader represented them as four ints.
        import uuid
        controller_props.master_layer.layer_id = uuid.UUID(bytes=layers[layer_index][1])
        controller = _append(area, index, controller_props)
        menu.add_connection(State.InternalState00,
                            Message.Increment if layer_index in (2, 6) else Message.Decrement, controller.id)
    menu.add_connection(State.InternalState00, Message.SetToZero, teleporter.id)
    _dependency(area, PROMPT_ID, 'STRG')
    for identity, kind in TRANSITION_DEPENDENCIES:
        _dependency(area, identity, kind)
    _teleporter_modules(area)
    output = area.build()
    check = SeedMrea.parse(output, Game.CORRUPTION)
    # Existing actor properties and every original link remain intact. Only the
    # save function gains a decline-only edge to the delayed confirmation.
    for before, layer in zip(originals, check.script_layers, strict=True):
        after = [a._raw for a in layer.instances][:len(before)]
        for old, new in zip(before, after, strict=True):
            if old.id == save.id:
                if old.base_property != new.base_property or new.connections[:len(old.connections)] != old.connections:
                    raise ValueError('Warp to Space changed native saving')
            elif old != new:
                raise ValueError('Warp to Space changed an unrelated station actor')
    return output, {'area': f'{area_id:016X}', 'save_actor': f'{int(save.id):08X}',
                    'actors_added': len(list(next(check.script_layers).instances))-len(originals[0]),
                    'save_preserved': True, 'warp_saves_progress': False}


def patch_space(raw):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    # Only this restored, previously unreachable area is changed. Suppress the
    # briefing entry point and its automatic world-map unlock helpers.
    timer = _actor(area, 0x00020368, 'TIMR')
    timer.connections = ()
    arrived = _actor(area, 0x180201CF, 'SRLY')
    hold = [c for c in arrived.connections if c.state == State.Relay
            and c.message == Message.Action and int(c.target) == 0x18020376]
    if len(hold) != 1:
        raise ValueError('Warp to Space: unsupported cockpit arrival/briefing connection')
    # The normal briefing's completion path initializes the cockpit and releases
    # its control hold. Skipping only the dialogue timer would leave the player
    # waiting for a briefing that will never finish.
    _actor(area, 0x00020197, 'SRLY')
    arrived.connections = tuple(c for c in arrived.connections if c not in hold)
    arrived.add_connection(State.Relay, Message.Action, 0x00020197)
    suppressed = []
    for layer in area.script_layers:
        for actor in layer.instances:
            if actor.type_name != 'SPFN':
                continue
            props = actor.get_properties()
            if props.function == Function.kSF_SunGeneratorTeleporter:
                props.string_parm = ''
                actor.set_properties(props)
                actor.connections = tuple(c for c in actor.connections if not (
                    c.message == Message.Attach and any(
                        int(a.id) == int(c.target) and a.type_name == 'SPFN'
                        and a.get_properties().function == Function.kSF_MapStation
                        for a in layer.instances)))
                suppressed.append(f'{int(actor.id):08X}')
    return area.build(), suppressed


def install(files: Path, output: Path) -> dict:
    files, output = Path(files), Path(output)
    if output.exists() or files.resolve() == output.resolve():
        raise ValueError('Warp to Space requires a new staging directory')
    output.mkdir(parents=True)
    archives = {p.name: Archive(p) for p in files.glob('*.pak')}
    def resource(pak, identity):
        found = [r for r in archives[pak].resources if r.identity == identity]
        if not found or any((r.kind, r.compressed, r.read()) !=
                            (found[0].kind, found[0].compressed, found[0].read()) for r in found[1:]):
            raise ValueError(f'Warp to Space: missing or conflicting resource {identity:016X} in {pak}')
        return found[0]
    space = resource('Metroid8.pak', SPACE_AREA)
    world = resource('Worlds.pak', SPACE_WORLD)
    layers = _space_layers(world.read())
    source = SeedMrea.parse(resource('Metroid7.pak', DEPARTURE_AREA).read(), Game.CORRUPTION)
    departure = _actor(source, 0x0005000B, 'TEL1')._raw.base_property
    fields = dict(properties(departure))
    if fields.get(0x474BCCE3) != bytes.fromhex('C30E5A46'):
        raise ValueError('Warp to Space: unexpected Elysian Seed transition type')
    departure = replace_properties(departure, {
        0x31EC14BC: struct.pack('>Q', SPACE_WORLD), 0xE0C17804: struct.pack('>Q', SPACE_AREA)})
    if hashlib.sha256(departure).hexdigest() != DEPARTURE_SHA256:
        raise ValueError('Warp to Space: Elysian departure template differs from supported retail data')
    extra = [prompt_resource(resource('Metroid1.pak', PROMPT_TEMPLATE))]
    for identity, kind in TRANSITION_DEPENDENCIES:
        found = [r for r in archives['Metroid7.pak'].resources if r.identity == identity]
        if not found or any(r.kind.decode() != kind for r in found):
            raise ValueError(f'Warp to Space: missing transition dependency {kind} {identity:016X}')
        extra.append(found[0])
    from randovania.games.prime3.exporter.warp_cargo import CARGO_SOURCE, apply as apply_cargo
    stations, changed_archives, covered = [], {}, set()
    space_compaction = None
    for name, archive in archives.items():
        rows = []
        modified = False
        for res in archive.resources:
            if res.kind == b'MREA' and res.identity in SAVE_AREAS:
                # Area index is encoded in native instance IDs, independent of PAK order.
                parsed = SeedMrea.parse(res.read(), Game.CORRUPTION)
                existing = next(iter(next(parsed.script_layers).instances))
                index = existing.id.area
                raw, report = patch_station(res.read(), area_id=res.identity, index=index,
                                            departure=departure, layers=layers, attachments=transition_attachments(source))
                if res.identity in CARGO_SOURCE:
                    source_id = CARGO_SOURCE[res.identity]
                    source_pak = 'Metroid3.pak' if source_id in (0x1219413B9F218A0A, 0x5428E9D06F515F0B) else 'Metroid4.pak'
                    raw, report['cargo_reset'] = apply_cargo(raw, resource(source_pak, source_id).read(), res.identity)
                else:
                    report['cargo_reset'] = None
                # Corruption streams an area's dependency bundle before its
                # MREA. Keep aliases in each room's bundle, as the core and
                # pickup callback patcher do; a PAK-wide tail is too late.
                rows.extend(extra)
                rows.append(res.updated(raw))
                stations.append(report)
                covered.add(res.identity)
                modified = True
            elif res.kind == b'MREA' and res.identity == SPACE_AREA:
                raw, suppressed = patch_space(space.read())
                rows.append(res.updated(raw))
                modified = True
            else:
                rows.append(res)
        if modified:
            archive.write(output/name, rows)
            changed_archives[name] = hashlib.sha256((output/name).read_bytes()).hexdigest()
    if covered != SAVE_AREAS:
        raise ValueError('Warp to Space: save-station coverage differs from retail')
    report = {'schema': 1, 'stations': stations, 'archives': changed_archives,
              'space_area_restored': True, 'briefings_disabled': True,
              'space_compaction': space_compaction,
              'native_cockpit_initialization_without_briefing': True,
              'prompt_named_entries': {'message': 0, 'choice0': 1, 'choice1': 2},
              'prompt_order': ['Yes', 'No'], 'default_choice': 'Yes',
              'warp_choice_state': 'InternalState00',
              'space_unlock_helpers_suppressed': suppressed,
              'polling_added': False, 'requires_cdv': False, 'gameplay_verified': False}
    report['transition_dependencies'] = [{'id': f'{identity:016X}', 'type': kind}
                                         for identity, kind in TRANSITION_DEPENDENCIES]
    (output/'report.json').write_text(json.dumps(report, indent=2)+'\n')
    for name in changed_archives:
        shutil.copyfile(output/name, files/name)
    return report
