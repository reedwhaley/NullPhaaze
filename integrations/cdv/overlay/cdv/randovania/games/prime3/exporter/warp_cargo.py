# Guarded native cargo reset for save-station Warp to Space. Boundary names here: apply.
"""Guarded native cargo reset for save-station Warp to Space.

Native game-state variables gate each planet's original cargo restoration.
Use isolated copies of only those operations, without its confirmation menus,
DoShipCommand event, or mission and hint updates.
"""
from __future__ import annotations

import copy
import hashlib
from retro_data_structures.enums.corruption import Message, State
from retro_data_structures.formats.script_object import ScriptInstanceRaw, _try_quick_get_name
from retro_data_structures.game_check import Game
from retro_data_structures.properties.corruption.objects.SpecialFunction import Function
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea, next_instance_id

CARGO_SOURCE = {
    0x55E832ED0345809E: 0x1219413B9F218A0A,
    0x821212E8F533C7E2: 0x5428E9D06F515F0B,
    0xF06FBFA781D9E57C: 0x96B87B34E7A25F36,
    0x9D38B4EBC66AFAED: 0x50110543F9A81DAE,
    0x0E44911F45063FFF: 0x50110543F9A81DAE,
}
# Audited native IDs and ordered connections for USA revision 0.
SPECS = {
    0x1219413B9F218A0A: {
        'variables': {
            0x00010002: ('TurretGenerator', 0x0001000B),
            0x0001000E: ('ColossusHead', 0x00010004),
        },
        'resets': {
            0x00010004: [
                ('Decrement', 0x0001000E),
                ('Deactivate', 0x0001000B),
                ('Deactivate', 0x00010004),
                ('Decrement', 0x0001000C),
                ('Increment', 0x0001000A),
                ('Increment', 0x00010007),
                ('Increment', 0x00010009),
                ('Decrement', 0x00010006),
            ],
            0x0001000B: [
                ('Decrement', 0x00010002),
                ('Deactivate', 0x00010004),
                ('Deactivate', 0x0001000B),
                ('Increment', 0x00010005),
                ('Decrement', 0x00010015),
                ('Increment', 0x00010008),
                ('Increment', 0x00010013),
                ('Decrement', 0x00010014),
            ],
        },
    },
    0x5428E9D06F515F0B: {
        'variables': {
            0x00010006: ('TurretGenerator', 0x0001000C),
            0x0001000E: ('ColossusHead', 0x00010013),
        },
        'resets': {
            0x00010013: [
                ('Decrement', 0x0001000E),
                ('Deactivate', 0x0001000C),
                ('Deactivate', 0x00010013),
                ('Decrement', 0x00010012),
                ('Increment', 0x00010004),
                ('Increment', 0x00010014),
                ('Decrement', 0x00010003),
                ('Increment', 0x0001001F),
            ],
            0x0001000C: [
                ('Decrement', 0x00010006),
                ('Deactivate', 0x00010013),
                ('Deactivate', 0x0001000C),
                ('Increment', 0x00010005),
                ('Increment', 0x00010015),
                ('Decrement', 0x0001000B),
                ('Decrement', 0x0001001E),
                ('Increment', 0x0001000D),
            ],
        },
    },
    0x96B87B34E7A25F36: {
        'variables': {
            0x0001000E: ('Donut08', 0x0001001E),
            0x00010026: ('Spike', 0x0001001E),
            0x00010060: ('Donut02', 0x0001001E),
        },
        'resets': {
            0x0001001E: [
                ('Increment', 0x00010025),
                ('Increment', 0x00010021),
                ('Decrement', 0x0001001C),
                ('Increment', 0x0001001D),
                ('Decrement', 0x0001001F),
                ('Decrement', 0x00010023),
                ('Decrement', 0x00010028),
                ('Increment', 0x00010024),
                ('Decrement', 0x0001001B),
                ('Decrement', 0x00010027),
                ('Decrement', 0x0001002B),
                ('Decrement', 0x00010022),
                ('Deactivate', 0x0001001E),
                ('Decrement', 0x0001006A),
                ('Decrement', 0x00010060),
                ('Decrement', 0x00010026),
                ('Decrement', 0x0001000E),
                ('Decrement', 0x00010061),
                ('Decrement', 0x00010095),
            ],
        },
    },
    0x50110543F9A81DAE: {
        'variables': {
            0x00010006: ('Donut02', 0x00010015),
            0x00010008: ('Spike', 0x00010015),
            0x0001000D: ('Donut08', 0x00010015),
        },
        'resets': {
            0x00010015: [
                ('Increment', 0x0001000E),
                ('Increment', 0x0001000C),
                ('Decrement', 0x00010024),
                ('Increment', 0x00010012),
                ('Decrement', 0x0001000F),
                ('Decrement', 0x00010011),
                ('Decrement', 0x00010016),
                ('Increment', 0x00010007),
                ('Decrement', 0x00010013),
                ('Decrement', 0x00010009),
                ('Decrement', 0x00010025),
                ('Decrement', 0x0001000B),
                ('Deactivate', 0x00010015),
                ('Decrement', 0x0001002C),
                ('Decrement', 0x00010006),
                ('Decrement', 0x0001000D),
                ('Decrement', 0x0001002D),
                ('Decrement', 0x00010008),
                ('Decrement', 0x0001002B),
            ],
        },
    },
}

# Bind copied layer controllers and native properties to audited retail actors.
PROPERTY_HASHES = {
    0x1219413B9F218A0A: {
        0x00010002: 'f16ea1290f1c084df50601a0c47cf29d916249f9e5727dc48b93686784afb9f5',
        0x00010004: '5c2e671289a337ce31b34882fc11636b7ac9239653b9f3ac9f900b547b7c44ca',
        0x00010005: '8f204e745f9aef9a268956b6d2338a0ebb4dd7d93eca1bd9c0447082f1297cd1',
        0x00010006: 'f6ffb7c7da5c305337deeb7411a1a9dc1ec773c0462b786509fea02b8c14dae4',
        0x00010007: '9f1cd8377d49bc82443e16117d1097c46a28d6a6b5d97d1588ebb0ddb98009c0',
        0x00010008: '1bf08d5eea929ab404492fe464285c8e24e4d0ef581ae477db8bb0b8dfa4ee45',
        0x00010009: '2758a59eb049e49c701e01f5776939640ec1da75768fd67009ff1ad5bf8dae20',
        0x0001000A: 'a565ec897e9b1d45b8f798ed2f338911a5499a3216dfb9fb747657427a839fb4',
        0x0001000B: '3f4f0edf9d8530576e7239c052c9e05c9e55514a5a5fa7c8fb0469d4c909b21d',
        0x0001000C: '42fba7d733b7dfa92ab6eefa8dd0f2587aa1b411414953169f05dcd3a59d54ec',
        0x0001000E: '42d68710df11841f9a921f8fb7e4802ae294a50c9cc02345f4e4f144efe36328',
        0x00010013: '68d434b26cc58c84011ae1611f6ac97c1338b28ff2a76bbbf9b94b908e478886',
        0x00010014: '55b088706b7cab80262db17a3b862b3e1698367f28242894bdb33e204e885ea6',
        0x00010015: '3c283ebe7fac8e00a3bdd274a58aea290dc1aed8b623b5ac061ccc347ce9c938',
    },
    0x5428E9D06F515F0B: {
        0x00010003: 'f6ffb7c7da5c305337deeb7411a1a9dc1ec773c0462b786509fea02b8c14dae4',
        0x00010004: '00c105f0d4d785f7660abd4009545525ec08469b02d199bbf2202b958ee1088c',
        0x00010005: '68d434b26cc58c84011ae1611f6ac97c1338b28ff2a76bbbf9b94b908e478886',
        0x00010006: 'f16ea1290f1c084df50601a0c47cf29d916249f9e5727dc48b93686784afb9f5',
        0x0001000B: '14836aa442063b8acf48d3f1ca6fc1cf1bb00bdc5ef3962ed9c617f42891be5c',
        0x0001000C: '3f4f0edf9d8530576e7239c052c9e05c9e55514a5a5fa7c8fb0469d4c909b21d',
        0x0001000D: '1bf08d5eea929ab404492fe464285c8e24e4d0ef581ae477db8bb0b8dfa4ee45',
        0x0001000E: '42d68710df11841f9a921f8fb7e4802ae294a50c9cc02345f4e4f144efe36328',
        0x00010012: '588c270c09b10391fd2750ed97fd8d30faf780c955a002d4d2fe92346a2325e6',
        0x00010013: '5c2e671289a337ce31b34882fc11636b7ac9239653b9f3ac9f900b547b7c44ca',
        0x00010014: '9f1cd8377d49bc82443e16117d1097c46a28d6a6b5d97d1588ebb0ddb98009c0',
        0x00010015: 'c4d60b2e77403d9954b3d707097769eb3d3114d995033c6cb146a58f9141ab99',
        0x0001001E: 'd7b8a7420504fe7095760a58e29913cd53ef286d3ec3002d2e0ed24a72aa25f8',
        0x0001001F: '2758a59eb049e49c701e01f5776939640ec1da75768fd67009ff1ad5bf8dae20',
    },
    0x96B87B34E7A25F36: {
        0x0001000E: '9f0adda1da3dddc6cef2adac4bb9d1a0ddea5af9d20263be4f6e771d6d1c8121',
        0x0001001B: '2af02d5a149682db7e015097fec3a89f85af71cea86f7d00cfebefe964c2fe56',
        0x0001001C: '0c431d25b31f780a77b83a880b65faebe9b136faf42ec4315432436a5adaf2b5',
        0x0001001D: '16bb7483e95beae7bf4e8b4f7f328221acb62244ccaffff0e3f5b12d63219b3d',
        0x0001001E: '24f836f57bd3ad181423eefcfeb128a8a90d27e402fd10cb3034e6576a71e145',
        0x0001001F: 'fc2519ae06e1cc25fe06bce0c3779435fd64a62df1cb57d266f4fd79a260496b',
        0x00010021: 'f65abecc8a87c0376a1ddadc4f11ffcb014dbfb78a65156b3af919780b5c80d8',
        0x00010022: '3f1f556146541ecc160ef4a114b20fd3d91a4449c0d17ed34ab4715a4be44084',
        0x00010023: 'c6e6a5425678f459bb9f78d923e7b1942065e02ea4a156de263a700d52380a20',
        0x00010024: '543a9318be2645205749fe64591a25fc0f80a910f96c4d7a86f7651d054b2a8b',
        0x00010025: '8410a05415abc6466d87a55ae632ba43a61d9e0b6fbe536227fd68cb6310d028',
        0x00010026: '4fe808ded58c4f3c5bee6c078807cf8179d891e26219b656e398252cb70ea02c',
        0x00010027: '4ee75d4b0802e2f5d2408eb99c3276607d8a2107ba64f28073cff845f87f9258',
        0x00010028: '02d3e9f87aa7e27f5860cd1cf3518ff42c2cca97bfee756831d7c893de9b0840',
        0x0001002B: '20b7e504ccb588eba6bc186127ab77e2fdbd16d997e6c66b668df5ca85fb154f',
        0x00010060: '6e136a50615423cef61a43c67db237e1c971815fd49e02d1884b517593278bc7',
        0x00010061: '53598c04b178887caf9fd98466e377d3e2195955d383d0fd583be131275a4105',
        0x0001006A: 'aeccf63ce0c7cb020994d04f3d3172cd5c18c6e28ded4b35f41cab187cc3563e',
        0x00010095: 'eac7e485aed06f1dbb140fb88ebb998d4c874b5a7713783d5abf29921f684617',
    },
    0x50110543F9A81DAE: {
        0x00010006: '1718940a7745b99982f5f29ad7c7e7695df4236b80ff0b147225822e34bbb4f8',
        0x00010007: 'ccb66d6217c7c68b1c35caa3ce3c72b60f3b239aa114011bfc6892f1503d4afe',
        0x00010008: '0c06bec3713d73d55f3cc7638399314e43d2a7e02aa79e39b5b55879669342e8',
        0x00010009: 'f6cb4bfb053bfc60da0beba26b77e3e4650d67a4df9a7dcf95ab68c431b00558',
        0x0001000B: '6dfba96f2717904d0e4a9e1e01e406b093f6e0d77d04b34e198fa07787fd1e88',
        0x0001000C: '79caad21938d41357d3e931f16f567efdd7bf9b65d1b1aad2b0be9b7c77afba3',
        0x0001000D: 'a5333c2d4072a4b0fc3573e655615624f49136ef25f34df49eebfe0476d5f09f',
        0x0001000E: '95bbd8779640dad19357ff3eec6b3421e892448e8d5d389536df3d18cb464be0',
        0x0001000F: '96668a7f842bc244e90381662f3b407fc1e0ad4999732d39e5b8468bd95b2b45',
        0x00010011: 'b8e0145de78fe841596295e0b2ac1b05c8c89d35b5fddfe99754a8fde8bce4a7',
        0x00010012: 'bad2ba44973669fe9ccc0bb4755157355c55ef1ea71f031be1e9f1be0eb115af',
        0x00010013: '5df7683a2fcf4534389540b798efc83c065337fb1662762f538028922d3c234e',
        0x00010015: 'd6a6e9893cb49ec609686eee2bb8179514f62327ab53d43c2b3cde3f3465c170',
        0x00010016: '9b16f9223653a1e835acb20e259495ff451acc7ec6aa330cb040e7575e0022ee',
        0x00010024: 'e77d7d7f2fea8a901021d2b8217f2a71aaa7ba37c5b570ba16b409d481416989',
        0x00010025: '25b9384dc93947b62244d917531d626f0a630487e0594bcc7f35aa3bc59b49f6',
        0x0001002B: '400693facb6904ce28106ed0beb067633d6d38ad5c6da32e6b30aad98e9f5fb7',
        0x0001002C: '7ec65df0f37f672562102c5a52ac8bd95696727a6e3a021ea9206e700a798af7',
        0x0001002D: '3f03c17970f62d23af2d04b3f87470d7e2224cff49d180e14a233af8b3ca573e',
    },
}


def apply(station_raw, source_raw, station_id):
    """Install a cargo check on Yes before TEL1, preserving all original actors."""
    if station_id not in CARGO_SOURCE:
        raise ValueError('Warp cargo: unknown source world')
    source_id = CARGO_SOURCE[station_id]
    spec = SPECS[source_id]
    source = SeedMrea.parse(source_raw, Game.CORRUPTION)
    original = {int(a.id): a for layer in source.script_layers for a in layer.instances}
    # Verify the exact native reset edges so an unfamiliar image cannot silently
    # copy unrelated state or quest actions.
    for rid, expected in spec['resets'].items():
        if rid not in original:
            raise ValueError(f'Warp cargo: missing reset relay {rid:08X}')
        actor = original[rid]
        actual = [(c.message.name, int(c.target)) for c in actor.connections
                  if c.state == State.Relay]
        if actor.type_name != 'SRLY' or len(actual) != len(actor.connections) or actual != expected:
            raise ValueError(f'Warp cargo: unsupported reset relay {rid:08X}')
    for vid, (name, rid) in spec['variables'].items():
        if vid not in original:
            raise ValueError(f'Warp cargo: missing state variable {vid:08X}')
        actor = original[vid]
        props = actor.get_properties()
        if (actor.type_name != 'SPFN' or props.function != Function.kSF_GameStateEnvVarController
                or props.string_parm != name or rid not in spec['resets']
                or not any(c.state == State.Open and c.message == Message.Activate
                           and int(c.target) == rid for c in actor.connections)):
            raise ValueError(f'Warp cargo: unsupported state variable {vid:08X}')
    ids = set(spec['variables']) | set(spec['resets'])
    ids.update(target for edges in spec['resets'].values() for _, target in edges)
    for identity in ids:
        if identity not in original or original[identity].type_name not in {'SPFN', 'SRLY', 'SLCT'}:
            raise ValueError(f'Warp cargo: unsupported reset target {identity:08X}')
        if hashlib.sha256(original[identity]._raw.base_property).hexdigest() != PROPERTY_HASHES[source_id][identity]:
            raise ValueError(f'Warp cargo: unsupported reset target properties {identity:08X}')
        if original[identity].type_name == 'SPFN' and identity not in spec['variables']:
            raise ValueError(f'Warp cargo: unexpected state variable {identity:08X}')
    area = SeedMrea.parse(station_raw, Game.CORRUPTION)
    before = {int(a.id): copy.deepcopy(a._raw) for layer in area.script_layers for a in layer.instances}
    menus = [a for layer in area.script_layers for a in layer.instances
             if a.type_name == 'GMNU' and a.get_properties().editor_properties.name == 'NullPhaaze Warp to Space - Confirm (Yes / No)']
    if len(menus) != 1:
        raise ValueError('Warp cargo: expected one installed warp menu')
    menu = menus[0]
    if any((_try_quick_get_name(a._raw.base_property) or '').startswith('NullPhaaze Cargo Reset')
           for layer in area.script_layers for a in layer.instances):
        raise ValueError('Warp cargo: already installed')
    tel = [c for c in menu.connections if c.state == State.InternalState00 and c.message == Message.SetToZero]
    if len(tel) != 1:
        raise ValueError('Warp cargo: unsupported teleport menu')
    tel_link = tel[0]
    area_index = menu.id.area
    layer = next(area.script_layers)
    clones = {}
    for identity in sorted(ids):
        src = original[identity]
        props = src.get_properties()
        props.editor_properties.name = f'NullPhaaze Cargo Reset {identity:08X} - {props.editor_properties.name}'
        new_id = next_instance_id(area, area_index)
        layer._raw.script_instances.append(ScriptInstanceRaw(src.type_name, new_id, (), props.to_bytes(Game.CORRUPTION)))
        layer.mark_modified()
        clones[identity] = new_id
    by_id = {int(a.id): a for a in layer.instances}
    for rid, edges in spec['resets'].items():
        clone = by_id[int(clones[rid])]
        for message, target in edges:
            clone.add_connection(State.Relay, getattr(Message, message), clones[target])
    # The native chain probes with SetToZero. An open result identifies the
    # carried object; activate then execute its normally inactive reset relay.
    for vid, (_, rid) in spec['variables'].items():
        probe = by_id[int(clones[vid])]
        probe.add_connection(State.Open, Message.Activate, clones[rid])
        probe.add_connection(State.Open, Message.Action, clones[rid])
    menu.connections = tuple(c for c in menu.connections if c != tel_link)
    for vid in spec['variables']:
        menu.add_connection(State.InternalState00, Message.SetToZero, clones[vid])
    menu.add_connection(State.InternalState00, Message.SetToZero, tel_link.target)
    output = area.build()
    check = SeedMrea.parse(output, Game.CORRUPTION)
    after = {int(a.id): a._raw for l in check.script_layers for a in l.instances}
    if any(after[i] != old for i, old in before.items() if i != int(menu.id)):
        raise ValueError('Warp cargo changed an unrelated station actor')
    return output, {'source_area': f'{source_id:016X}', 'variables': [v[0] for v in spec['variables'].values()],
                    'actors_added': len(clones), 'native_reset_relays': [f'{i:08X}' for i in spec['resets']]}
