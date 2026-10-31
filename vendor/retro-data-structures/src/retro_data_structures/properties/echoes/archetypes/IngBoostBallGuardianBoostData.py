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

if typing.TYPE_CHECKING:
    class IngBoostBallGuardianBoostDataJson(typing_extensions.TypedDict):
        boost_puddle_mode_time: float
        percentage_puddle_damage_to_boost: float
        break_boost_puddle_mode_damage: float
        break_boost_mode_damage: float
        next_boost_time_min: float
        next_boost_time_max: float
        sequential_boost_attacks_min: int
        sequential_boost_attacks_max: int
        small_boost_num_bounces_min: int
        small_boost_num_bounces_max: int
        large_boost_num_bounces_min: int
        large_boost_num_bounces_max: int
        locomotion_speed_scale: float
        ing_spot_speed_scale: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x25d02bc5, 0xabe99de0, 0xe2b23f03, 0x2f845006, 0x5d1626fb, 0xbb76891a, 0x285d67ad, 0x6d5f242f, 0xe3ff2ed6, 0xa6fd6d54, 0xecb314b6, 0xa9b15734, 0x1213a7d4, 0xc19ed897)


@dataclasses.dataclass()
class IngBoostBallGuardianBoostData(BaseProperty):
    boost_puddle_mode_time: float = dataclasses.field(default=1.7999999523162842, metadata={
        'reflection': FieldReflection[float](
            float, id=0x25d02bc5, original_name='BoostPuddleModeTime'
        ),
    })
    percentage_puddle_damage_to_boost: float = dataclasses.field(default=1.7999999523162842, metadata={
        'reflection': FieldReflection[float](
            float, id=0xabe99de0, original_name='PercentagePuddleDamageToBoost'
        ),
    })
    break_boost_puddle_mode_damage: float = dataclasses.field(default=1.7999999523162842, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe2b23f03, original_name='BreakBoostPuddleModeDamage'
        ),
    })
    break_boost_mode_damage: float = dataclasses.field(default=150.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2f845006, original_name='BreakBoostModeDamage'
        ),
    })
    next_boost_time_min: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5d1626fb, original_name='NextBoostTimeMin'
        ),
    })
    next_boost_time_max: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbb76891a, original_name='NextBoostTimeMax'
        ),
    })
    sequential_boost_attacks_min: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x285d67ad, original_name='SequentialBoostAttacksMin'
        ),
    })
    sequential_boost_attacks_max: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6d5f242f, original_name='SequentialBoostAttacksMax'
        ),
    })
    small_boost_num_bounces_min: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe3ff2ed6, original_name='SmallBoostNumBouncesMin'
        ),
    })
    small_boost_num_bounces_max: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa6fd6d54, original_name='SmallBoostNumBouncesMax'
        ),
    })
    large_boost_num_bounces_min: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xecb314b6, original_name='LargeBoostNumBouncesMin'
        ),
    })
    large_boost_num_bounces_max: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa9b15734, original_name='LargeBoostNumBouncesMax'
        ),
    })
    locomotion_speed_scale: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1213a7d4, original_name='LocomotionSpeedScale'
        ),
    })
    ing_spot_speed_scale: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc19ed897, original_name='IngSpotSpeedScale'
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
        if property_count != 14:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHlLHlLHlLHlLHlLHlLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(140))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0e')  # 14 properties

        data.write(b'%\xd0+\xc5')  # 0x25d02bc5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.boost_puddle_mode_time))

        data.write(b'\xab\xe9\x9d\xe0')  # 0xabe99de0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.percentage_puddle_damage_to_boost))

        data.write(b'\xe2\xb2?\x03')  # 0xe2b23f03
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.break_boost_puddle_mode_damage))

        data.write(b'/\x84P\x06')  # 0x2f845006
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.break_boost_mode_damage))

        data.write(b']\x16&\xfb')  # 0x5d1626fb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_boost_time_min))

        data.write(b'\xbbv\x89\x1a')  # 0xbb76891a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_boost_time_max))

        data.write(b'(]g\xad')  # 0x285d67ad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sequential_boost_attacks_min))

        data.write(b'm_$/')  # 0x6d5f242f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sequential_boost_attacks_max))

        data.write(b'\xe3\xff.\xd6')  # 0xe3ff2ed6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.small_boost_num_bounces_min))

        data.write(b'\xa6\xfdmT')  # 0xa6fd6d54
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.small_boost_num_bounces_max))

        data.write(b'\xec\xb3\x14\xb6')  # 0xecb314b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.large_boost_num_bounces_min))

        data.write(b'\xa9\xb1W4')  # 0xa9b15734
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.large_boost_num_bounces_max))

        data.write(b'\x12\x13\xa7\xd4')  # 0x1213a7d4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.locomotion_speed_scale))

        data.write(b'\xc1\x9e\xd8\x97')  # 0xc19ed897
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ing_spot_speed_scale))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("IngBoostBallGuardianBoostDataJson", data)
        return cls(
            boost_puddle_mode_time=json_data['boost_puddle_mode_time'],
            percentage_puddle_damage_to_boost=json_data['percentage_puddle_damage_to_boost'],
            break_boost_puddle_mode_damage=json_data['break_boost_puddle_mode_damage'],
            break_boost_mode_damage=json_data['break_boost_mode_damage'],
            next_boost_time_min=json_data['next_boost_time_min'],
            next_boost_time_max=json_data['next_boost_time_max'],
            sequential_boost_attacks_min=json_data['sequential_boost_attacks_min'],
            sequential_boost_attacks_max=json_data['sequential_boost_attacks_max'],
            small_boost_num_bounces_min=json_data['small_boost_num_bounces_min'],
            small_boost_num_bounces_max=json_data['small_boost_num_bounces_max'],
            large_boost_num_bounces_min=json_data['large_boost_num_bounces_min'],
            large_boost_num_bounces_max=json_data['large_boost_num_bounces_max'],
            locomotion_speed_scale=json_data['locomotion_speed_scale'],
            ing_spot_speed_scale=json_data['ing_spot_speed_scale'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'boost_puddle_mode_time': self.boost_puddle_mode_time,
            'percentage_puddle_damage_to_boost': self.percentage_puddle_damage_to_boost,
            'break_boost_puddle_mode_damage': self.break_boost_puddle_mode_damage,
            'break_boost_mode_damage': self.break_boost_mode_damage,
            'next_boost_time_min': self.next_boost_time_min,
            'next_boost_time_max': self.next_boost_time_max,
            'sequential_boost_attacks_min': self.sequential_boost_attacks_min,
            'sequential_boost_attacks_max': self.sequential_boost_attacks_max,
            'small_boost_num_bounces_min': self.small_boost_num_bounces_min,
            'small_boost_num_bounces_max': self.small_boost_num_bounces_max,
            'large_boost_num_bounces_min': self.large_boost_num_bounces_min,
            'large_boost_num_bounces_max': self.large_boost_num_bounces_max,
            'locomotion_speed_scale': self.locomotion_speed_scale,
            'ing_spot_speed_scale': self.ing_spot_speed_scale,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x25d02bc5: ('boost_puddle_mode_time', structs.decode_BIG_f),
    0xabe99de0: ('percentage_puddle_damage_to_boost', structs.decode_BIG_f),
    0xe2b23f03: ('break_boost_puddle_mode_damage', structs.decode_BIG_f),
    0x2f845006: ('break_boost_mode_damage', structs.decode_BIG_f),
    0x5d1626fb: ('next_boost_time_min', structs.decode_BIG_f),
    0xbb76891a: ('next_boost_time_max', structs.decode_BIG_f),
    0x285d67ad: ('sequential_boost_attacks_min', structs.decode_BIG_l),
    0x6d5f242f: ('sequential_boost_attacks_max', structs.decode_BIG_l),
    0xe3ff2ed6: ('small_boost_num_bounces_min', structs.decode_BIG_l),
    0xa6fd6d54: ('small_boost_num_bounces_max', structs.decode_BIG_l),
    0xecb314b6: ('large_boost_num_bounces_min', structs.decode_BIG_l),
    0xa9b15734: ('large_boost_num_bounces_max', structs.decode_BIG_l),
    0x1213a7d4: ('locomotion_speed_scale', structs.decode_BIG_f),
    0xc19ed897: ('ing_spot_speed_scale', structs.decode_BIG_f),
}
