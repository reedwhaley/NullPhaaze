# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl

if typing.TYPE_CHECKING:
    class PlayerMiscControlsJson(typing_extensions.TypedDict):
        item_menu: json_util.JsonObject
        use_item: json_util.JsonObject
        combat_visor: json_util.JsonObject
        scan_visor: json_util.JsonObject
        x_ray_visor: json_util.JsonObject
        command_visor: json_util.JsonObject
        cycle_visor_up: json_util.JsonObject
        cycle_visor_down: json_util.JsonObject
        scan_to_combat_visor: json_util.JsonObject
        orbit_lock: json_util.JsonObject
        grapple_lock: json_util.JsonObject
        grapple_pull: json_util.JsonObject
        grapple_release: json_util.JsonObject
        grapple_give: json_util.JsonObject
        grapple_receive: json_util.JsonObject
        summon_ship: json_util.JsonObject
        ship_fire: json_util.JsonObject
        scan_item: json_util.JsonObject
        scan_item_exit: json_util.JsonObject
        start_contextual_action: json_util.JsonObject
        cancel_contextual_action: json_util.JsonObject
        ift_hint_map_screen: json_util.JsonObject
        ift_cancel: json_util.JsonObject
        simple_hint_select: json_util.JsonObject
        struggle: json_util.JsonObject
    

@dataclasses.dataclass()
class PlayerMiscControls(BaseProperty):
    item_menu: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xddf88c92, original_name='ItemMenu', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    use_item: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x8b0e64f6, original_name='UseItem', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    combat_visor: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xd49e5fcf, original_name='CombatVisor', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    scan_visor: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x9c182689, original_name='ScanVisor', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    x_ray_visor: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x011f0193, original_name='XRayVisor', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    command_visor: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xbb560ad3, original_name='CommandVisor', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    cycle_visor_up: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x12a3619e, original_name='CycleVisorUp', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    cycle_visor_down: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x33e1a595, original_name='CycleVisorDown', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    scan_to_combat_visor: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xabfaa1fa, original_name='ScanToCombatVisor', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    orbit_lock: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x23717b97, original_name='OrbitLock', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    grapple_lock: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x0e59d622, original_name='GrappleLock', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    grapple_pull: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x67d45eb2, original_name='GrapplePull', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    grapple_release: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xb4a66335, original_name='GrappleRelease', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    grapple_give: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xe073645b, original_name='GrappleGive', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    grapple_receive: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xcb6d207d, original_name='GrappleReceive', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    summon_ship: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x7ee3acdf, original_name='SummonShip', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    ship_fire: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xf6c87bf5, original_name='ShipFire', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    scan_item: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x4a88a76f, original_name='ScanItem', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    scan_item_exit: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xb43b2477, original_name='ScanItemExit', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    start_contextual_action: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xf3a2fbdd, original_name='StartContextualAction', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    cancel_contextual_action: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x30d313eb, original_name='CancelContextualAction', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    ift_hint_map_screen: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x79dc49ca, original_name='IFTHintMapScreen', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    ift_cancel: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xefd76f97, original_name='IFTCancel', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    simple_hint_select: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xe6366106, original_name='SimpleHintSelect', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    struggle: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x98da6d03, original_name='Struggle', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 25:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xddf88c92
        item_menu = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b0e64f6
        use_item = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd49e5fcf
        combat_visor = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c182689
        scan_visor = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x011f0193
        x_ray_visor = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb560ad3
        command_visor = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12a3619e
        cycle_visor_up = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33e1a595
        cycle_visor_down = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xabfaa1fa
        scan_to_combat_visor = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23717b97
        orbit_lock = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0e59d622
        grapple_lock = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67d45eb2
        grapple_pull = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb4a66335
        grapple_release = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe073645b
        grapple_give = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcb6d207d
        grapple_receive = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ee3acdf
        summon_ship = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6c87bf5
        ship_fire = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a88a76f
        scan_item = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb43b2477
        scan_item_exit = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3a2fbdd
        start_contextual_action = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30d313eb
        cancel_contextual_action = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79dc49ca
        ift_hint_map_screen = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefd76f97
        ift_cancel = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe6366106
        simple_hint_select = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98da6d03
        struggle = RevolutionControl.from_stream(data, game, property_size)
    
        return cls(item_menu, use_item, combat_visor, scan_visor, x_ray_visor, command_visor, cycle_visor_up, cycle_visor_down, scan_to_combat_visor, orbit_lock, grapple_lock, grapple_pull, grapple_release, grapple_give, grapple_receive, summon_ship, ship_fire, scan_item, scan_item_exit, start_contextual_action, cancel_contextual_action, ift_hint_map_screen, ift_cancel, simple_hint_select, struggle)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x19')  # 25 properties

        data.write(b'\xdd\xf8\x8c\x92')  # 0xddf88c92
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.item_menu.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8b\x0ed\xf6')  # 0x8b0e64f6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.use_item.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd4\x9e_\xcf')  # 0xd49e5fcf
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.combat_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9c\x18&\x89')  # 0x9c182689
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x01\x1f\x01\x93')  # 0x11f0193
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x_ray_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbbV\n\xd3')  # 0xbb560ad3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.command_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x12\xa3a\x9e')  # 0x12a3619e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cycle_visor_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3\xe1\xa5\x95')  # 0x33e1a595
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cycle_visor_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xab\xfa\xa1\xfa')  # 0xabfaa1fa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_to_combat_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#q{\x97')  # 0x23717b97
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.orbit_lock.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0eY\xd6"')  # 0xe59d622
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_lock.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'g\xd4^\xb2')  # 0x67d45eb2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_pull.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb4\xa6c5')  # 0xb4a66335
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_release.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe0sd[')  # 0xe073645b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_give.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcbm }')  # 0xcb6d207d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_receive.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~\xe3\xac\xdf')  # 0x7ee3acdf
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.summon_ship.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf6\xc8{\xf5')  # 0xf6c87bf5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ship_fire.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'J\x88\xa7o')  # 0x4a88a76f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_item.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb4;$w')  # 0xb43b2477
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_item_exit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf3\xa2\xfb\xdd')  # 0xf3a2fbdd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.start_contextual_action.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'0\xd3\x13\xeb')  # 0x30d313eb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cancel_contextual_action.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'y\xdcI\xca')  # 0x79dc49ca
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ift_hint_map_screen.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xef\xd7o\x97')  # 0xefd76f97
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ift_cancel.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe66a\x06')  # 0xe6366106
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.simple_hint_select.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x98\xdam\x03')  # 0x98da6d03
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.struggle.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerMiscControlsJson", data)
        return cls(
            item_menu=RevolutionControl.from_json(json_data['item_menu']),
            use_item=RevolutionControl.from_json(json_data['use_item']),
            combat_visor=RevolutionControl.from_json(json_data['combat_visor']),
            scan_visor=RevolutionControl.from_json(json_data['scan_visor']),
            x_ray_visor=RevolutionControl.from_json(json_data['x_ray_visor']),
            command_visor=RevolutionControl.from_json(json_data['command_visor']),
            cycle_visor_up=RevolutionControl.from_json(json_data['cycle_visor_up']),
            cycle_visor_down=RevolutionControl.from_json(json_data['cycle_visor_down']),
            scan_to_combat_visor=RevolutionControl.from_json(json_data['scan_to_combat_visor']),
            orbit_lock=RevolutionControl.from_json(json_data['orbit_lock']),
            grapple_lock=RevolutionControl.from_json(json_data['grapple_lock']),
            grapple_pull=RevolutionControl.from_json(json_data['grapple_pull']),
            grapple_release=RevolutionControl.from_json(json_data['grapple_release']),
            grapple_give=RevolutionControl.from_json(json_data['grapple_give']),
            grapple_receive=RevolutionControl.from_json(json_data['grapple_receive']),
            summon_ship=RevolutionControl.from_json(json_data['summon_ship']),
            ship_fire=RevolutionControl.from_json(json_data['ship_fire']),
            scan_item=RevolutionControl.from_json(json_data['scan_item']),
            scan_item_exit=RevolutionControl.from_json(json_data['scan_item_exit']),
            start_contextual_action=RevolutionControl.from_json(json_data['start_contextual_action']),
            cancel_contextual_action=RevolutionControl.from_json(json_data['cancel_contextual_action']),
            ift_hint_map_screen=RevolutionControl.from_json(json_data['ift_hint_map_screen']),
            ift_cancel=RevolutionControl.from_json(json_data['ift_cancel']),
            simple_hint_select=RevolutionControl.from_json(json_data['simple_hint_select']),
            struggle=RevolutionControl.from_json(json_data['struggle']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'item_menu': self.item_menu.to_json(),
            'use_item': self.use_item.to_json(),
            'combat_visor': self.combat_visor.to_json(),
            'scan_visor': self.scan_visor.to_json(),
            'x_ray_visor': self.x_ray_visor.to_json(),
            'command_visor': self.command_visor.to_json(),
            'cycle_visor_up': self.cycle_visor_up.to_json(),
            'cycle_visor_down': self.cycle_visor_down.to_json(),
            'scan_to_combat_visor': self.scan_to_combat_visor.to_json(),
            'orbit_lock': self.orbit_lock.to_json(),
            'grapple_lock': self.grapple_lock.to_json(),
            'grapple_pull': self.grapple_pull.to_json(),
            'grapple_release': self.grapple_release.to_json(),
            'grapple_give': self.grapple_give.to_json(),
            'grapple_receive': self.grapple_receive.to_json(),
            'summon_ship': self.summon_ship.to_json(),
            'ship_fire': self.ship_fire.to_json(),
            'scan_item': self.scan_item.to_json(),
            'scan_item_exit': self.scan_item_exit.to_json(),
            'start_contextual_action': self.start_contextual_action.to_json(),
            'cancel_contextual_action': self.cancel_contextual_action.to_json(),
            'ift_hint_map_screen': self.ift_hint_map_screen.to_json(),
            'ift_cancel': self.ift_cancel.to_json(),
            'simple_hint_select': self.simple_hint_select.to_json(),
            'struggle': self.struggle.to_json(),
        }


def _decode_item_menu(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_use_item(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_combat_visor(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_scan_visor(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_x_ray_visor(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_command_visor(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_cycle_visor_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_cycle_visor_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_scan_to_combat_visor(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_orbit_lock(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_grapple_lock(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_grapple_pull(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_grapple_release(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_grapple_give(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_grapple_receive(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_summon_ship(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_ship_fire(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_scan_item(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_scan_item_exit(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_start_contextual_action(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_cancel_contextual_action(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_ift_hint_map_screen(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_ift_cancel(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_simple_hint_select(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_struggle(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xddf88c92: ('item_menu', _decode_item_menu),
    0x8b0e64f6: ('use_item', _decode_use_item),
    0xd49e5fcf: ('combat_visor', _decode_combat_visor),
    0x9c182689: ('scan_visor', _decode_scan_visor),
    0x011f0193: ('x_ray_visor', _decode_x_ray_visor),
    0xbb560ad3: ('command_visor', _decode_command_visor),
    0x12a3619e: ('cycle_visor_up', _decode_cycle_visor_up),
    0x33e1a595: ('cycle_visor_down', _decode_cycle_visor_down),
    0xabfaa1fa: ('scan_to_combat_visor', _decode_scan_to_combat_visor),
    0x23717b97: ('orbit_lock', _decode_orbit_lock),
    0x0e59d622: ('grapple_lock', _decode_grapple_lock),
    0x67d45eb2: ('grapple_pull', _decode_grapple_pull),
    0xb4a66335: ('grapple_release', _decode_grapple_release),
    0xe073645b: ('grapple_give', _decode_grapple_give),
    0xcb6d207d: ('grapple_receive', _decode_grapple_receive),
    0x7ee3acdf: ('summon_ship', _decode_summon_ship),
    0xf6c87bf5: ('ship_fire', _decode_ship_fire),
    0x4a88a76f: ('scan_item', _decode_scan_item),
    0xb43b2477: ('scan_item_exit', _decode_scan_item_exit),
    0xf3a2fbdd: ('start_contextual_action', _decode_start_contextual_action),
    0x30d313eb: ('cancel_contextual_action', _decode_cancel_contextual_action),
    0x79dc49ca: ('ift_hint_map_screen', _decode_ift_hint_map_screen),
    0xefd76f97: ('ift_cancel', _decode_ift_cancel),
    0xe6366106: ('simple_hint_select', _decode_simple_hint_select),
    0x98da6d03: ('struggle', _decode_struggle),
}
