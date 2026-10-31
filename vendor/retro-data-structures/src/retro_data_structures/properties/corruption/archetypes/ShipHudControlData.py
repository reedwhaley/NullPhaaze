# Generated File
from __future__ import annotations

import dataclasses
import enum
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    class ShipHudControlDataJson(typing_extensions.TypedDict):
        hud_control_group: int
        unknown_0x868cfe92: bool
        unknown_0xf1943b5a: bool
        idle_mode_animation: int
        move_command_animation: int
        pickup_command_animation: int
        drop_command_animation: int
        missile_attack_command_animation: int
        bomb_attack_command_animation: int
        land_command_animation: int
    

class HudControlGroup(enum.IntEnum):
    kHudControlGroup_Local = 2868300453
    kHudControlGroup_CarryObjectOverride = 881720149
    kHudControlGroup_EvasiveActionOverride = 1464639200

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x4131a2a, 0x868cfe92, 0xf1943b5a, 0x44bf1dc9, 0x7c538ed3, 0xfcd2a1a0, 0x1aec3e02, 0xe0e4573d, 0x21103ec1, 0xc7c06435)


@dataclasses.dataclass()
class ShipHudControlData(BaseProperty):
    hud_control_group: HudControlGroup = dataclasses.field(default=HudControlGroup.kHudControlGroup_Local, metadata={
        'reflection': FieldReflection[HudControlGroup](
            HudControlGroup, id=0x04131a2a, original_name='HudControlGroup', from_json=HudControlGroup.from_json, to_json=HudControlGroup.to_json
        ),
    })
    unknown_0x868cfe92: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x868cfe92, original_name='Unknown'
        ),
    })
    unknown_0xf1943b5a: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf1943b5a, original_name='Unknown'
        ),
    })
    idle_mode_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x44bf1dc9, original_name='IdleModeAnimation'
        ),
    })
    move_command_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7c538ed3, original_name='MoveCommandAnimation'
        ),
    })
    pickup_command_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xfcd2a1a0, original_name='PickupCommandAnimation'
        ),
    })
    drop_command_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x1aec3e02, original_name='DropCommandAnimation'
        ),
    })
    missile_attack_command_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe0e4573d, original_name='MissileAttackCommandAnimation'
        ),
    })
    bomb_attack_command_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x21103ec1, original_name='BombAttackCommandAnimation'
        ),
    })
    land_command_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc7c06435, original_name='LandCommandAnimation'
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
        if property_count != 10:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHLLH?LH?LHlLHlLHlLHlLHlLHlLHl')
    
        dec = _FAST_FORMAT.unpack(data.read(94))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27]) == _FAST_IDS
        return cls(
            HudControlGroup(dec[2]),
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\x04\x13\x1a*')  # 0x4131a2a
        data.write(b'\x00\x04')  # size
        self.hud_control_group.to_stream(data, game)

        data.write(b'\x86\x8c\xfe\x92')  # 0x868cfe92
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x868cfe92))

        data.write(b'\xf1\x94;Z')  # 0xf1943b5a
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf1943b5a))

        data.write(b'D\xbf\x1d\xc9')  # 0x44bf1dc9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.idle_mode_animation))

        data.write(b'|S\x8e\xd3')  # 0x7c538ed3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.move_command_animation))

        data.write(b'\xfc\xd2\xa1\xa0')  # 0xfcd2a1a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.pickup_command_animation))

        data.write(b'\x1a\xec>\x02')  # 0x1aec3e02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.drop_command_animation))

        data.write(b'\xe0\xe4W=')  # 0xe0e4573d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.missile_attack_command_animation))

        data.write(b'!\x10>\xc1')  # 0x21103ec1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.bomb_attack_command_animation))

        data.write(b'\xc7\xc0d5')  # 0xc7c06435
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.land_command_animation))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShipHudControlDataJson", data)
        return cls(
            hud_control_group=HudControlGroup.from_json(json_data['hud_control_group']),
            unknown_0x868cfe92=json_data['unknown_0x868cfe92'],
            unknown_0xf1943b5a=json_data['unknown_0xf1943b5a'],
            idle_mode_animation=json_data['idle_mode_animation'],
            move_command_animation=json_data['move_command_animation'],
            pickup_command_animation=json_data['pickup_command_animation'],
            drop_command_animation=json_data['drop_command_animation'],
            missile_attack_command_animation=json_data['missile_attack_command_animation'],
            bomb_attack_command_animation=json_data['bomb_attack_command_animation'],
            land_command_animation=json_data['land_command_animation'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'hud_control_group': self.hud_control_group.to_json(),
            'unknown_0x868cfe92': self.unknown_0x868cfe92,
            'unknown_0xf1943b5a': self.unknown_0xf1943b5a,
            'idle_mode_animation': self.idle_mode_animation,
            'move_command_animation': self.move_command_animation,
            'pickup_command_animation': self.pickup_command_animation,
            'drop_command_animation': self.drop_command_animation,
            'missile_attack_command_animation': self.missile_attack_command_animation,
            'bomb_attack_command_animation': self.bomb_attack_command_animation,
            'land_command_animation': self.land_command_animation,
        }


def _decode_hud_control_group(data: typing.BinaryIO, game: Game, property_size: int) -> HudControlGroup:
    return HudControlGroup.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x04131a2a: ('hud_control_group', _decode_hud_control_group),
    0x868cfe92: ('unknown_0x868cfe92', structs.decode_BIG_bool_),
    0xf1943b5a: ('unknown_0xf1943b5a', structs.decode_BIG_bool_),
    0x44bf1dc9: ('idle_mode_animation', structs.decode_BIG_l),
    0x7c538ed3: ('move_command_animation', structs.decode_BIG_l),
    0xfcd2a1a0: ('pickup_command_animation', structs.decode_BIG_l),
    0x1aec3e02: ('drop_command_animation', structs.decode_BIG_l),
    0xe0e4573d: ('missile_attack_command_animation', structs.decode_BIG_l),
    0x21103ec1: ('bomb_attack_command_animation', structs.decode_BIG_l),
    0xc7c06435: ('land_command_animation', structs.decode_BIG_l),
}
