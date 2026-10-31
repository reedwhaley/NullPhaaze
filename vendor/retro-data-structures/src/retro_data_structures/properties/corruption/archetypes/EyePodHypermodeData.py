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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class EyePodHypermodeDataJson(typing_extensions.TypedDict):
        hyper_mode_check_chance: float
        initial_hyper_mode_check_time_min: float
        initial_hyper_mode_check_time_max: float
        hyper_mode_check_time_min: float
        hyper_mode_check_time_max: float
        hyper_mode_duration_min: float
        hyper_mode_duration_max: float
        hyper_mode_vulnerability: json_util.JsonObject
        min_time_between_attacks: float
        max_time_between_attacks: float
        min_shots_in_a_burst: int
        max_shots_in_a_burst: int
        unknown: float
        hyper_mode_shot_angle_variance: float
        launch_projectile_info: json_util.JsonObject
    

@dataclasses.dataclass()
class EyePodHypermodeData(BaseProperty):
    hyper_mode_check_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf04452f3, original_name='HyperModeCheckChance'
        ),
    })
    initial_hyper_mode_check_time_min: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc8e312dd, original_name='InitialHyperModeCheckTimeMin'
        ),
    })
    initial_hyper_mode_check_time_max: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2e83bd3c, original_name='InitialHyperModeCheckTimeMax'
        ),
    })
    hyper_mode_check_time_min: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf06a131d, original_name='HyperModeCheckTimeMin'
        ),
    })
    hyper_mode_check_time_max: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x160abcfc, original_name='HyperModeCheckTimeMax'
        ),
    })
    hyper_mode_duration_min: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4866df6c, original_name='HyperModeDurationMin'
        ),
    })
    hyper_mode_duration_max: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xae06708d, original_name='HyperModeDurationMax'
        ),
    })
    hyper_mode_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xc8a1eac8, original_name='HyperModeVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    min_time_between_attacks: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    min_shots_in_a_burst: int = dataclasses.field(default=4, metadata={
        'reflection': FieldReflection[int](
            int, id=0x64d482d5, original_name='MinShotsInABurst'
        ),
    })
    max_shots_in_a_burst: int = dataclasses.field(default=7, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc3e002ac, original_name='MaxShotsInABurst'
        ),
    })
    unknown: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x77b6541c, original_name='Unknown'
        ),
    })
    hyper_mode_shot_angle_variance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9c889645, original_name='HyperModeShotAngleVariance'
        ),
    })
    launch_projectile_info: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x11473c13, original_name='LaunchProjectileInfo', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
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
        if property_count != 15:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf04452f3
        hyper_mode_check_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8e312dd
        initial_hyper_mode_check_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e83bd3c
        initial_hyper_mode_check_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf06a131d
        hyper_mode_check_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x160abcfc
        hyper_mode_check_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4866df6c
        hyper_mode_duration_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae06708d
        hyper_mode_duration_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8a1eac8
        hyper_mode_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e7a2c2
        min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ba1c18
        max_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64d482d5
        min_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3e002ac
        max_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77b6541c
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c889645
        hyper_mode_shot_angle_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11473c13
        launch_projectile_info = LaunchProjectileData.from_stream(data, game, property_size)
    
        return cls(hyper_mode_check_chance, initial_hyper_mode_check_time_min, initial_hyper_mode_check_time_max, hyper_mode_check_time_min, hyper_mode_check_time_max, hyper_mode_duration_min, hyper_mode_duration_max, hyper_mode_vulnerability, min_time_between_attacks, max_time_between_attacks, min_shots_in_a_burst, max_shots_in_a_burst, unknown, hyper_mode_shot_angle_variance, launch_projectile_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0f')  # 15 properties

        data.write(b'\xf0DR\xf3')  # 0xf04452f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_check_chance))

        data.write(b'\xc8\xe3\x12\xdd')  # 0xc8e312dd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_hyper_mode_check_time_min))

        data.write(b'.\x83\xbd<')  # 0x2e83bd3c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_hyper_mode_check_time_max))

        data.write(b'\xf0j\x13\x1d')  # 0xf06a131d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_check_time_min))

        data.write(b'\x16\n\xbc\xfc')  # 0x160abcfc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_check_time_max))

        data.write(b'Hf\xdfl')  # 0x4866df6c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_duration_min))

        data.write(b'\xae\x06p\x8d')  # 0xae06708d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_duration_max))

        data.write(b'\xc8\xa1\xea\xc8')  # 0xc8a1eac8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'd\xd4\x82\xd5')  # 0x64d482d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_shots_in_a_burst))

        data.write(b'\xc3\xe0\x02\xac')  # 0xc3e002ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_shots_in_a_burst))

        data.write(b'w\xb6T\x1c')  # 0x77b6541c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\x9c\x88\x96E')  # 0x9c889645
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_shot_angle_variance))

        data.write(b'\x11G<\x13')  # 0x11473c13
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.launch_projectile_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EyePodHypermodeDataJson", data)
        return cls(
            hyper_mode_check_chance=json_data['hyper_mode_check_chance'],
            initial_hyper_mode_check_time_min=json_data['initial_hyper_mode_check_time_min'],
            initial_hyper_mode_check_time_max=json_data['initial_hyper_mode_check_time_max'],
            hyper_mode_check_time_min=json_data['hyper_mode_check_time_min'],
            hyper_mode_check_time_max=json_data['hyper_mode_check_time_max'],
            hyper_mode_duration_min=json_data['hyper_mode_duration_min'],
            hyper_mode_duration_max=json_data['hyper_mode_duration_max'],
            hyper_mode_vulnerability=DamageVulnerability.from_json(json_data['hyper_mode_vulnerability']),
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            min_shots_in_a_burst=json_data['min_shots_in_a_burst'],
            max_shots_in_a_burst=json_data['max_shots_in_a_burst'],
            unknown=json_data['unknown'],
            hyper_mode_shot_angle_variance=json_data['hyper_mode_shot_angle_variance'],
            launch_projectile_info=LaunchProjectileData.from_json(json_data['launch_projectile_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'hyper_mode_check_chance': self.hyper_mode_check_chance,
            'initial_hyper_mode_check_time_min': self.initial_hyper_mode_check_time_min,
            'initial_hyper_mode_check_time_max': self.initial_hyper_mode_check_time_max,
            'hyper_mode_check_time_min': self.hyper_mode_check_time_min,
            'hyper_mode_check_time_max': self.hyper_mode_check_time_max,
            'hyper_mode_duration_min': self.hyper_mode_duration_min,
            'hyper_mode_duration_max': self.hyper_mode_duration_max,
            'hyper_mode_vulnerability': self.hyper_mode_vulnerability.to_json(),
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'min_shots_in_a_burst': self.min_shots_in_a_burst,
            'max_shots_in_a_burst': self.max_shots_in_a_burst,
            'unknown': self.unknown,
            'hyper_mode_shot_angle_variance': self.hyper_mode_shot_angle_variance,
            'launch_projectile_info': self.launch_projectile_info.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self.launch_projectile_info.dependencies_for(asset_manager)


def _decode_hyper_mode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_launch_projectile_info(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xf04452f3: ('hyper_mode_check_chance', structs.decode_BIG_f),
    0xc8e312dd: ('initial_hyper_mode_check_time_min', structs.decode_BIG_f),
    0x2e83bd3c: ('initial_hyper_mode_check_time_max', structs.decode_BIG_f),
    0xf06a131d: ('hyper_mode_check_time_min', structs.decode_BIG_f),
    0x160abcfc: ('hyper_mode_check_time_max', structs.decode_BIG_f),
    0x4866df6c: ('hyper_mode_duration_min', structs.decode_BIG_f),
    0xae06708d: ('hyper_mode_duration_max', structs.decode_BIG_f),
    0xc8a1eac8: ('hyper_mode_vulnerability', _decode_hyper_mode_vulnerability),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0x64d482d5: ('min_shots_in_a_burst', structs.decode_BIG_l),
    0xc3e002ac: ('max_shots_in_a_burst', structs.decode_BIG_l),
    0x77b6541c: ('unknown', structs.decode_BIG_f),
    0x9c889645: ('hyper_mode_shot_angle_variance', structs.decode_BIG_f),
    0x11473c13: ('launch_projectile_info', _decode_launch_projectile_info),
}
