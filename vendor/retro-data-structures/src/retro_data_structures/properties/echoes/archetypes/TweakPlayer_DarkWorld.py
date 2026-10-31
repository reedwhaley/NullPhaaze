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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo

if typing.TYPE_CHECKING:
    class TweakPlayer_DarkWorldJson(typing_extensions.TypedDict):
        damage_grace_period: float
        unknown: float
        damage_per_second: json_util.JsonObject
        dark_suit_damage_reduction: float
        dark_suit_effect_generation_scale: float
        dark_suit_effect_color_scale: float
    

@dataclasses.dataclass()
class TweakPlayer_DarkWorld(BaseProperty):
    damage_grace_period: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4985bc73, original_name='DamageGracePeriod'
        ),
    })
    unknown: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa4e33ef0, original_name='Unknown'
        ),
    })
    damage_per_second: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xf9bf59a2, original_name='DamagePerSecond', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    dark_suit_damage_reduction: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x333b7549, original_name='DarkSuitDamageReduction'
        ),
    })
    dark_suit_effect_generation_scale: float = dataclasses.field(default=0.3499999940395355, metadata={
        'reflection': FieldReflection[float](
            float, id=0xee452490, original_name='DarkSuitEffectGenerationScale'
        ),
    })
    dark_suit_effect_color_scale: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x19275a97, original_name='DarkSuitEffectColorScale'
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
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4985bc73
        damage_grace_period = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4e33ef0
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9bf59a2
        damage_per_second = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 17})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x333b7549
        dark_suit_damage_reduction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee452490
        dark_suit_effect_generation_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19275a97
        dark_suit_effect_color_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(damage_grace_period, unknown, damage_per_second, dark_suit_damage_reduction, dark_suit_effect_generation_scale, dark_suit_effect_color_scale)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'I\x85\xbcs')  # 0x4985bc73
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_grace_period))

        data.write(b'\xa4\xe3>\xf0')  # 0xa4e33ef0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\xf9\xbfY\xa2')  # 0xf9bf59a2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_per_second.to_stream(data, game, default_override={'di_weapon_type': 17})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3;uI')  # 0x333b7549
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_suit_damage_reduction))

        data.write(b'\xeeE$\x90')  # 0xee452490
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_suit_effect_generation_scale))

        data.write(b"\x19'Z\x97")  # 0x19275a97
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_suit_effect_color_scale))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_DarkWorldJson", data)
        return cls(
            damage_grace_period=json_data['damage_grace_period'],
            unknown=json_data['unknown'],
            damage_per_second=DamageInfo.from_json(json_data['damage_per_second']),
            dark_suit_damage_reduction=json_data['dark_suit_damage_reduction'],
            dark_suit_effect_generation_scale=json_data['dark_suit_effect_generation_scale'],
            dark_suit_effect_color_scale=json_data['dark_suit_effect_color_scale'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'damage_grace_period': self.damage_grace_period,
            'unknown': self.unknown,
            'damage_per_second': self.damage_per_second.to_json(),
            'dark_suit_damage_reduction': self.dark_suit_damage_reduction,
            'dark_suit_effect_generation_scale': self.dark_suit_effect_generation_scale,
            'dark_suit_effect_color_scale': self.dark_suit_effect_color_scale,
        }


def _decode_damage_per_second(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 17})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4985bc73: ('damage_grace_period', structs.decode_BIG_f),
    0xa4e33ef0: ('unknown', structs.decode_BIG_f),
    0xf9bf59a2: ('damage_per_second', _decode_damage_per_second),
    0x333b7549: ('dark_suit_damage_reduction', structs.decode_BIG_f),
    0xee452490: ('dark_suit_effect_generation_scale', structs.decode_BIG_f),
    0x19275a97: ('dark_suit_effect_color_scale', structs.decode_BIG_f),
}
