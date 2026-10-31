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
import retro_data_structures.enums.echoes as enums

if typing.TYPE_CHECKING:
    class TDamageInfoJson(typing_extensions.TypedDict):
        weapon_type: int
        damage_amount: float
        radius_damage_amount: float
        damage_radius: float
        knock_back_power: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x4d577910, 0xf3ec8748, 0x37b6df3d, 0xf598739, 0x56f98c49)


@dataclasses.dataclass()
class TDamageInfo(BaseProperty):
    weapon_type: enums.WeaponTypeEnum = dataclasses.field(default=enums.WeaponTypeEnum.Power, metadata={
        'reflection': FieldReflection[enums.WeaponTypeEnum](
            enums.WeaponTypeEnum, id=0x4d577910, original_name='WeaponType', from_json=enums.WeaponTypeEnum.from_json, to_json=enums.WeaponTypeEnum.to_json
        ),
    })
    damage_amount: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf3ec8748, original_name='DamageAmount'
        ),
    })
    radius_damage_amount: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x37b6df3d, original_name='RadiusDamageAmount'
        ),
    })
    damage_radius: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0f598739, original_name='DamageRadius'
        ),
    })
    knock_back_power: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x56f98c49, original_name='KnockBackPower'
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
        if property_count != 5:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHLLHfLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(50))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            enums.WeaponTypeEnum(dec[2]),
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'MWy\x10')  # 0x4d577910
        data.write(b'\x00\x04')  # size
        self.weapon_type.to_stream(data, game)

        data.write(b'\xf3\xec\x87H')  # 0xf3ec8748
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_amount))

        data.write(b'7\xb6\xdf=')  # 0x37b6df3d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.radius_damage_amount))

        data.write(b'\x0fY\x879')  # 0xf598739
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_radius))

        data.write(b'V\xf9\x8cI')  # 0x56f98c49
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.knock_back_power))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TDamageInfoJson", data)
        return cls(
            weapon_type=enums.WeaponTypeEnum.from_json(json_data['weapon_type']),
            damage_amount=json_data['damage_amount'],
            radius_damage_amount=json_data['radius_damage_amount'],
            damage_radius=json_data['damage_radius'],
            knock_back_power=json_data['knock_back_power'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'weapon_type': self.weapon_type.to_json(),
            'damage_amount': self.damage_amount,
            'radius_damage_amount': self.radius_damage_amount,
            'damage_radius': self.damage_radius,
            'knock_back_power': self.knock_back_power,
        }


def _decode_weapon_type(data: typing.BinaryIO, game: Game, property_size: int) -> enums.WeaponTypeEnum:
    return enums.WeaponTypeEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4d577910: ('weapon_type', _decode_weapon_type),
    0xf3ec8748: ('damage_amount', structs.decode_BIG_f),
    0x37b6df3d: ('radius_damage_amount', structs.decode_BIG_f),
    0x0f598739: ('damage_radius', structs.decode_BIG_f),
    0x56f98c49: ('knock_back_power', structs.decode_BIG_f),
}
