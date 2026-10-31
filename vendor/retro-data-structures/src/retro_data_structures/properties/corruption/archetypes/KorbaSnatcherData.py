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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class KorbaSnatcherDataJson(typing_extensions.TypedDict):
        player_attach_distance: float
        unknown_0xa2efcada: int
        unknown_0x37e9d29b: int
        morphball_lift_upward_velocity: float
        morphball_lift_upward_velocity_max: float
        snatcher_pull_force: float
        morphball_roll_speed_multiplier: float
        morphball_boosted_roll_speed_multiplier: float
        morphball_boosted_roll_snatcher_kill_time: float
        morphball_lift_time_limit: float
        korba_death_particle_effect: int
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xa350f15a, 0xa2efcada, 0x37e9d29b, 0xb827744f, 0x10f2e81, 0xf7e350db, 0xc7ec3d7b, 0x5a571a0, 0x8abb2662, 0x4d6c440, 0x973bf0ca)


@dataclasses.dataclass()
class KorbaSnatcherData(BaseProperty):
    player_attach_distance: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa350f15a, original_name='PlayerAttachDistance'
        ),
    })
    unknown_0xa2efcada: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa2efcada, original_name='Unknown'
        ),
    })
    unknown_0x37e9d29b: int = dataclasses.field(default=8, metadata={
        'reflection': FieldReflection[int](
            int, id=0x37e9d29b, original_name='Unknown'
        ),
    })
    morphball_lift_upward_velocity: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb827744f, original_name='MorphballLiftUpwardVelocity'
        ),
    })
    morphball_lift_upward_velocity_max: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x010f2e81, original_name='MorphballLiftUpwardVelocityMax'
        ),
    })
    snatcher_pull_force: float = dataclasses.field(default=2000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf7e350db, original_name='SnatcherPullForce'
        ),
    })
    morphball_roll_speed_multiplier: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc7ec3d7b, original_name='MorphballRollSpeedMultiplier'
        ),
    })
    morphball_boosted_roll_speed_multiplier: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x05a571a0, original_name='MorphballBoostedRollSpeedMultiplier'
        ),
    })
    morphball_boosted_roll_snatcher_kill_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8abb2662, original_name='MorphballBoostedRollSnatcherKillTime'
        ),
    })
    morphball_lift_time_limit: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x04d6c440, original_name='MorphballLiftTimeLimit'
        ),
    })
    korba_death_particle_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x973bf0ca, original_name='KorbaDeathParticleEffect'
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
            _FAST_FORMAT = struct.Struct('>LHfLHlLHlLHfLHfLHfLHfLHfLHfLHfLHQ')
    
        dec = _FAST_FORMAT.unpack(data.read(114))
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

        data.write(b'\xa3P\xf1Z')  # 0xa350f15a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.player_attach_distance))

        data.write(b'\xa2\xef\xca\xda')  # 0xa2efcada
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa2efcada))

        data.write(b'7\xe9\xd2\x9b')  # 0x37e9d29b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x37e9d29b))

        data.write(b"\xb8'tO")  # 0xb827744f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_lift_upward_velocity))

        data.write(b'\x01\x0f.\x81')  # 0x10f2e81
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_lift_upward_velocity_max))

        data.write(b'\xf7\xe3P\xdb')  # 0xf7e350db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.snatcher_pull_force))

        data.write(b'\xc7\xec={')  # 0xc7ec3d7b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_roll_speed_multiplier))

        data.write(b'\x05\xa5q\xa0')  # 0x5a571a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_boosted_roll_speed_multiplier))

        data.write(b'\x8a\xbb&b')  # 0x8abb2662
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_boosted_roll_snatcher_kill_time))

        data.write(b'\x04\xd6\xc4@')  # 0x4d6c440
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_lift_time_limit))

        data.write(b'\x97;\xf0\xca')  # 0x973bf0ca
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.korba_death_particle_effect))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KorbaSnatcherDataJson", data)
        return cls(
            player_attach_distance=json_data['player_attach_distance'],
            unknown_0xa2efcada=json_data['unknown_0xa2efcada'],
            unknown_0x37e9d29b=json_data['unknown_0x37e9d29b'],
            morphball_lift_upward_velocity=json_data['morphball_lift_upward_velocity'],
            morphball_lift_upward_velocity_max=json_data['morphball_lift_upward_velocity_max'],
            snatcher_pull_force=json_data['snatcher_pull_force'],
            morphball_roll_speed_multiplier=json_data['morphball_roll_speed_multiplier'],
            morphball_boosted_roll_speed_multiplier=json_data['morphball_boosted_roll_speed_multiplier'],
            morphball_boosted_roll_snatcher_kill_time=json_data['morphball_boosted_roll_snatcher_kill_time'],
            morphball_lift_time_limit=json_data['morphball_lift_time_limit'],
            korba_death_particle_effect=json_data['korba_death_particle_effect'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'player_attach_distance': self.player_attach_distance,
            'unknown_0xa2efcada': self.unknown_0xa2efcada,
            'unknown_0x37e9d29b': self.unknown_0x37e9d29b,
            'morphball_lift_upward_velocity': self.morphball_lift_upward_velocity,
            'morphball_lift_upward_velocity_max': self.morphball_lift_upward_velocity_max,
            'snatcher_pull_force': self.snatcher_pull_force,
            'morphball_roll_speed_multiplier': self.morphball_roll_speed_multiplier,
            'morphball_boosted_roll_speed_multiplier': self.morphball_boosted_roll_speed_multiplier,
            'morphball_boosted_roll_snatcher_kill_time': self.morphball_boosted_roll_snatcher_kill_time,
            'morphball_lift_time_limit': self.morphball_lift_time_limit,
            'korba_death_particle_effect': self.korba_death_particle_effect,
        }

    def _dependencies_for_korba_death_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.korba_death_particle_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_korba_death_particle_effect(asset_manager)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa350f15a: ('player_attach_distance', structs.decode_BIG_f),
    0xa2efcada: ('unknown_0xa2efcada', structs.decode_BIG_l),
    0x37e9d29b: ('unknown_0x37e9d29b', structs.decode_BIG_l),
    0xb827744f: ('morphball_lift_upward_velocity', structs.decode_BIG_f),
    0x010f2e81: ('morphball_lift_upward_velocity_max', structs.decode_BIG_f),
    0xf7e350db: ('snatcher_pull_force', structs.decode_BIG_f),
    0xc7ec3d7b: ('morphball_roll_speed_multiplier', structs.decode_BIG_f),
    0x05a571a0: ('morphball_boosted_roll_speed_multiplier', structs.decode_BIG_f),
    0x8abb2662: ('morphball_boosted_roll_snatcher_kill_time', structs.decode_BIG_f),
    0x04d6c440: ('morphball_lift_time_limit', structs.decode_BIG_f),
    0x973bf0ca: ('korba_death_particle_effect', structs.decode_BIG_Q),
}
