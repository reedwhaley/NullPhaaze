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
    class PowerBombGuardianStagePropertiesJson(typing_extensions.TypedDict):
        min_time_between_attacks: float
        max_time_between_attacks: float
        min_time_between_shots: float
        max_time_between_shots: float
        min_shots_in_a_burst: int
        max_shots_in_a_burst: int
        power_bomb_projectile_gravity_multiplier: float
        target_point_random_variance: float
        double_shot_chance: float
        min_attacks_per_double_shot: int
        max_attacks_per_double_shot: int
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x95e7a2c2, 0x76ba1c18, 0x3eb2de35, 0xe50d8dd2, 0x64d482d5, 0xc3e002ac, 0xbb4b6680, 0xd356c997, 0xca6ac43a, 0x87cc8ba4, 0x6491357e)


@dataclasses.dataclass()
class PowerBombGuardianStageProperties(BaseProperty):
    min_time_between_attacks: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    min_time_between_shots: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3eb2de35, original_name='MinTimeBetweenShots'
        ),
    })
    max_time_between_shots: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe50d8dd2, original_name='MaxTimeBetweenShots'
        ),
    })
    min_shots_in_a_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x64d482d5, original_name='MinShotsInABurst'
        ),
    })
    max_shots_in_a_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc3e002ac, original_name='MaxShotsInABurst'
        ),
    })
    power_bomb_projectile_gravity_multiplier: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbb4b6680, original_name='PowerBombProjectileGravityMultiplier'
        ),
    })
    target_point_random_variance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd356c997, original_name='TargetPointRandomVariance'
        ),
    })
    double_shot_chance: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xca6ac43a, original_name='DoubleShotChance'
        ),
    })
    min_attacks_per_double_shot: int = dataclasses.field(default=10, metadata={
        'reflection': FieldReflection[int](
            int, id=0x87cc8ba4, original_name='MinAttacksPerDoubleShot'
        ),
    })
    max_attacks_per_double_shot: int = dataclasses.field(default=10, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6491357e, original_name='MaxAttacksPerDoubleShot'
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
        if property_count != 11:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHlLHlLHfLHfLHfLHlLHl')
    
        dec = _FAST_FORMAT.unpack(data.read(110))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30]) == _FAST_IDS
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0b')  # 11 properties

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'>\xb2\xde5')  # 0x3eb2de35
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_shots))

        data.write(b'\xe5\r\x8d\xd2')  # 0xe50d8dd2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_shots))

        data.write(b'd\xd4\x82\xd5')  # 0x64d482d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_shots_in_a_burst))

        data.write(b'\xc3\xe0\x02\xac')  # 0xc3e002ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_shots_in_a_burst))

        data.write(b'\xbbKf\x80')  # 0xbb4b6680
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.power_bomb_projectile_gravity_multiplier))

        data.write(b'\xd3V\xc9\x97')  # 0xd356c997
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.target_point_random_variance))

        data.write(b'\xcaj\xc4:')  # 0xca6ac43a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.double_shot_chance))

        data.write(b'\x87\xcc\x8b\xa4')  # 0x87cc8ba4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_attacks_per_double_shot))

        data.write(b'd\x915~')  # 0x6491357e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_attacks_per_double_shot))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PowerBombGuardianStagePropertiesJson", data)
        return cls(
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            min_time_between_shots=json_data['min_time_between_shots'],
            max_time_between_shots=json_data['max_time_between_shots'],
            min_shots_in_a_burst=json_data['min_shots_in_a_burst'],
            max_shots_in_a_burst=json_data['max_shots_in_a_burst'],
            power_bomb_projectile_gravity_multiplier=json_data['power_bomb_projectile_gravity_multiplier'],
            target_point_random_variance=json_data['target_point_random_variance'],
            double_shot_chance=json_data['double_shot_chance'],
            min_attacks_per_double_shot=json_data['min_attacks_per_double_shot'],
            max_attacks_per_double_shot=json_data['max_attacks_per_double_shot'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'min_time_between_shots': self.min_time_between_shots,
            'max_time_between_shots': self.max_time_between_shots,
            'min_shots_in_a_burst': self.min_shots_in_a_burst,
            'max_shots_in_a_burst': self.max_shots_in_a_burst,
            'power_bomb_projectile_gravity_multiplier': self.power_bomb_projectile_gravity_multiplier,
            'target_point_random_variance': self.target_point_random_variance,
            'double_shot_chance': self.double_shot_chance,
            'min_attacks_per_double_shot': self.min_attacks_per_double_shot,
            'max_attacks_per_double_shot': self.max_attacks_per_double_shot,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0x3eb2de35: ('min_time_between_shots', structs.decode_BIG_f),
    0xe50d8dd2: ('max_time_between_shots', structs.decode_BIG_f),
    0x64d482d5: ('min_shots_in_a_burst', structs.decode_BIG_l),
    0xc3e002ac: ('max_shots_in_a_burst', structs.decode_BIG_l),
    0xbb4b6680: ('power_bomb_projectile_gravity_multiplier', structs.decode_BIG_f),
    0xd356c997: ('target_point_random_variance', structs.decode_BIG_f),
    0xca6ac43a: ('double_shot_chance', structs.decode_BIG_f),
    0x87cc8ba4: ('min_attacks_per_double_shot', structs.decode_BIG_l),
    0x6491357e: ('max_attacks_per_double_shot', structs.decode_BIG_l),
}
