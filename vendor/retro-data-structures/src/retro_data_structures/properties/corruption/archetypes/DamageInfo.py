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
    class DamageInfoJson(typing_extensions.TypedDict):
        di_weapon_type: int
        di_damage: float
        di_radius: float
        di_knock_back_power: float
        unknown: int
        adjust_for_difficulty: bool
    

class DI_WeaponType(enum.IntEnum):
    kWeaponType_Power = 2410944582
    kWeaponType_Plasma = 1118216892
    kWeaponType_Nova = 2134273114
    kWeaponType_Phazon = 444481760
    kWeaponType_Missile = 17740316
    kWeaponType_ScrewAttack = 2604127627
    kWeaponType_Ai = 3161493559
    kWeaponType_FriendlyAi = 3441875184
    kWeaponType_Unstoppable = 1243625939
    kWeaponType_Electrical = 4160790275
    kWeaponType_PoisonWater = 3877195498

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
_FAST_IDS = (0x445e00c8, 0xf2d02613, 0xee1be914, 0x555ff80a, 0x7a3fe00d, 0xefe9e465)


@dataclasses.dataclass()
class DamageInfo(BaseProperty):
    di_weapon_type: DI_WeaponType = dataclasses.field(default=DI_WeaponType.kWeaponType_Ai, metadata={
        'reflection': FieldReflection[DI_WeaponType](
            DI_WeaponType, id=0x445e00c8, original_name='DI_WeaponType', from_json=DI_WeaponType.from_json, to_json=DI_WeaponType.to_json
        ),
    })
    di_damage: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf2d02613, original_name='DI_Damage'
        ),
    })
    di_radius: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xee1be914, original_name='DI_Radius'
        ),
    })
    di_knock_back_power: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x555ff80a, original_name='DI_KnockBackPower'
        ),
    })
    unknown: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7a3fe00d, original_name='Unknown'
        ),
    })
    adjust_for_difficulty: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xefe9e465, original_name='AdjustForDifficulty'
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
        if property_count != 6:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHLLHfLHfLHfLHlLH?')
    
        dec = _FAST_FORMAT.unpack(data.read(57))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15]) == _FAST_IDS
        return cls(
            DI_WeaponType(dec[2]),
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'D^\x00\xc8')  # 0x445e00c8
        data.write(b'\x00\x04')  # size
        self.di_weapon_type.to_stream(data, game)

        data.write(b'\xf2\xd0&\x13')  # 0xf2d02613
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.di_damage))

        data.write(b'\xee\x1b\xe9\x14')  # 0xee1be914
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.di_radius))

        data.write(b'U_\xf8\n')  # 0x555ff80a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.di_knock_back_power))

        data.write(b'z?\xe0\r')  # 0x7a3fe00d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown))

        data.write(b'\xef\xe9\xe4e')  # 0xefe9e465
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.adjust_for_difficulty))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DamageInfoJson", data)
        return cls(
            di_weapon_type=DI_WeaponType.from_json(json_data['di_weapon_type']),
            di_damage=json_data['di_damage'],
            di_radius=json_data['di_radius'],
            di_knock_back_power=json_data['di_knock_back_power'],
            unknown=json_data['unknown'],
            adjust_for_difficulty=json_data['adjust_for_difficulty'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'di_weapon_type': self.di_weapon_type.to_json(),
            'di_damage': self.di_damage,
            'di_radius': self.di_radius,
            'di_knock_back_power': self.di_knock_back_power,
            'unknown': self.unknown,
            'adjust_for_difficulty': self.adjust_for_difficulty,
        }


def _decode_di_weapon_type(data: typing.BinaryIO, game: Game, property_size: int) -> DI_WeaponType:
    return DI_WeaponType.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x445e00c8: ('di_weapon_type', _decode_di_weapon_type),
    0xf2d02613: ('di_damage', structs.decode_BIG_f),
    0xee1be914: ('di_radius', structs.decode_BIG_f),
    0x555ff80a: ('di_knock_back_power', structs.decode_BIG_f),
    0x7a3fe00d: ('unknown', structs.decode_BIG_l),
    0xefe9e465: ('adjust_for_difficulty', structs.decode_BIG_bool_),
}
