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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PTCNoseTurretDataJson(typing_extensions.TypedDict):
        aiming_prediction: float
        scanning_range_min: float
        scanning_range_max: float
        scanning_speed: float
        max_detection_angle: float
        default_scan_pitch: float
        max_attack_angle: float
        max_rotation_speed: float
        max_rotation: float
        min_rotation: float
        max_pitch_speed: float
        max_pitch: float
        min_pitch: float
        projectile: int
        damage: json_util.JsonObject
        burst_delay: float
        shots_in_burst: int
        burst_shot_delay: float
        unknown: int
        sound_shot: int
        debugging_mode: bool
    

@dataclasses.dataclass()
class PTCNoseTurretData(BaseProperty):
    aiming_prediction: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x395b81ef, original_name='AimingPrediction'
        ),
    })
    scanning_range_min: float = dataclasses.field(default=-90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x44e01377, original_name='ScanningRangeMin'
        ),
    })
    scanning_range_max: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa280bc96, original_name='ScanningRangeMax'
        ),
    })
    scanning_speed: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf71c6dd7, original_name='ScanningSpeed'
        ),
    })
    max_detection_angle: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x679028ba, original_name='MaxDetectionAngle'
        ),
    })
    default_scan_pitch: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x494be648, original_name='DefaultScanPitch'
        ),
    })
    max_attack_angle: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf11f7384, original_name='MaxAttackAngle'
        ),
    })
    max_rotation_speed: float = dataclasses.field(default=360.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50eeb9e3, original_name='MaxRotationSpeed'
        ),
    })
    max_rotation: float = dataclasses.field(default=135.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7721deea, original_name='MaxRotation'
        ),
    })
    min_rotation: float = dataclasses.field(default=-135.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x26d865b7, original_name='MinRotation'
        ),
    })
    max_pitch_speed: float = dataclasses.field(default=360.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9597a329, original_name='MaxPitchSpeed'
        ),
    })
    max_pitch: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd8c8763, original_name='MaxPitch'
        ),
    })
    min_pitch: float = dataclasses.field(default=-45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8dc3ff15, original_name='MinPitch'
        ),
    })
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    burst_delay: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeb903473, original_name='BurstDelay'
        ),
    })
    shots_in_burst: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb5702ca3, original_name='ShotsInBurst'
        ),
    })
    burst_shot_delay: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe8f29e1e, original_name='BurstShotDelay'
        ),
    })
    unknown: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xaf28dc00, original_name='Unknown'
        ),
    })
    sound_shot: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc23a1955, original_name='Sound_Shot'
        ),
    })
    debugging_mode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x55d9abef, original_name='DebuggingMode'
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
        if property_count != 21:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x395b81ef
        aiming_prediction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44e01377
        scanning_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa280bc96
        scanning_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf71c6dd7
        scanning_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x679028ba
        max_detection_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x494be648
        default_scan_pitch = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf11f7384
        max_attack_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50eeb9e3
        max_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7721deea
        max_rotation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26d865b7
        min_rotation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9597a329
        max_pitch_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd8c8763
        max_pitch = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8dc3ff15
        min_pitch = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeb903473
        burst_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5702ca3
        shots_in_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8f29e1e
        burst_shot_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf28dc00
        unknown = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc23a1955
        sound_shot = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55d9abef
        debugging_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(aiming_prediction, scanning_range_min, scanning_range_max, scanning_speed, max_detection_angle, default_scan_pitch, max_attack_angle, max_rotation_speed, max_rotation, min_rotation, max_pitch_speed, max_pitch, min_pitch, projectile, damage, burst_delay, shots_in_burst, burst_shot_delay, unknown, sound_shot, debugging_mode)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x15')  # 21 properties

        data.write(b'9[\x81\xef')  # 0x395b81ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aiming_prediction))

        data.write(b'D\xe0\x13w')  # 0x44e01377
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scanning_range_min))

        data.write(b'\xa2\x80\xbc\x96')  # 0xa280bc96
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scanning_range_max))

        data.write(b'\xf7\x1cm\xd7')  # 0xf71c6dd7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scanning_speed))

        data.write(b'g\x90(\xba')  # 0x679028ba
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_detection_angle))

        data.write(b'IK\xe6H')  # 0x494be648
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.default_scan_pitch))

        data.write(b'\xf1\x1fs\x84')  # 0xf11f7384
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_angle))

        data.write(b'P\xee\xb9\xe3')  # 0x50eeb9e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_rotation_speed))

        data.write(b'w!\xde\xea')  # 0x7721deea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_rotation))

        data.write(b'&\xd8e\xb7')  # 0x26d865b7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_rotation))

        data.write(b'\x95\x97\xa3)')  # 0x9597a329
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_pitch_speed))

        data.write(b'\xcd\x8c\x87c')  # 0xcd8c8763
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_pitch))

        data.write(b'\x8d\xc3\xff\x15')  # 0x8dc3ff15
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_pitch))

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.projectile))

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xeb\x904s')  # 0xeb903473
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burst_delay))

        data.write(b'\xb5p,\xa3')  # 0xb5702ca3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.shots_in_burst))

        data.write(b'\xe8\xf2\x9e\x1e')  # 0xe8f29e1e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burst_shot_delay))

        data.write(b'\xaf(\xdc\x00')  # 0xaf28dc00
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown))

        data.write(b'\xc2:\x19U')  # 0xc23a1955
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_shot))

        data.write(b'U\xd9\xab\xef')  # 0x55d9abef
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.debugging_mode))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PTCNoseTurretDataJson", data)
        return cls(
            aiming_prediction=json_data['aiming_prediction'],
            scanning_range_min=json_data['scanning_range_min'],
            scanning_range_max=json_data['scanning_range_max'],
            scanning_speed=json_data['scanning_speed'],
            max_detection_angle=json_data['max_detection_angle'],
            default_scan_pitch=json_data['default_scan_pitch'],
            max_attack_angle=json_data['max_attack_angle'],
            max_rotation_speed=json_data['max_rotation_speed'],
            max_rotation=json_data['max_rotation'],
            min_rotation=json_data['min_rotation'],
            max_pitch_speed=json_data['max_pitch_speed'],
            max_pitch=json_data['max_pitch'],
            min_pitch=json_data['min_pitch'],
            projectile=json_data['projectile'],
            damage=DamageInfo.from_json(json_data['damage']),
            burst_delay=json_data['burst_delay'],
            shots_in_burst=json_data['shots_in_burst'],
            burst_shot_delay=json_data['burst_shot_delay'],
            unknown=json_data['unknown'],
            sound_shot=json_data['sound_shot'],
            debugging_mode=json_data['debugging_mode'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'aiming_prediction': self.aiming_prediction,
            'scanning_range_min': self.scanning_range_min,
            'scanning_range_max': self.scanning_range_max,
            'scanning_speed': self.scanning_speed,
            'max_detection_angle': self.max_detection_angle,
            'default_scan_pitch': self.default_scan_pitch,
            'max_attack_angle': self.max_attack_angle,
            'max_rotation_speed': self.max_rotation_speed,
            'max_rotation': self.max_rotation,
            'min_rotation': self.min_rotation,
            'max_pitch_speed': self.max_pitch_speed,
            'max_pitch': self.max_pitch,
            'min_pitch': self.min_pitch,
            'projectile': self.projectile,
            'damage': self.damage.to_json(),
            'burst_delay': self.burst_delay,
            'shots_in_burst': self.shots_in_burst,
            'burst_shot_delay': self.burst_shot_delay,
            'unknown': self.unknown,
            'sound_shot': self.sound_shot,
            'debugging_mode': self.debugging_mode,
        }

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_sound_shot(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_shot)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_sound_shot, "sound_shot", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PTCNoseTurretData.{field_name} ({field_type}): {e}"
                )


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x395b81ef: ('aiming_prediction', structs.decode_BIG_f),
    0x44e01377: ('scanning_range_min', structs.decode_BIG_f),
    0xa280bc96: ('scanning_range_max', structs.decode_BIG_f),
    0xf71c6dd7: ('scanning_speed', structs.decode_BIG_f),
    0x679028ba: ('max_detection_angle', structs.decode_BIG_f),
    0x494be648: ('default_scan_pitch', structs.decode_BIG_f),
    0xf11f7384: ('max_attack_angle', structs.decode_BIG_f),
    0x50eeb9e3: ('max_rotation_speed', structs.decode_BIG_f),
    0x7721deea: ('max_rotation', structs.decode_BIG_f),
    0x26d865b7: ('min_rotation', structs.decode_BIG_f),
    0x9597a329: ('max_pitch_speed', structs.decode_BIG_f),
    0xcd8c8763: ('max_pitch', structs.decode_BIG_f),
    0x8dc3ff15: ('min_pitch', structs.decode_BIG_f),
    0xef485db9: ('projectile', structs.decode_BIG_Q),
    0x337f9524: ('damage', _decode_damage),
    0xeb903473: ('burst_delay', structs.decode_BIG_f),
    0xb5702ca3: ('shots_in_burst', structs.decode_BIG_l),
    0xe8f29e1e: ('burst_shot_delay', structs.decode_BIG_f),
    0xaf28dc00: ('unknown', structs.decode_BIG_l),
    0xc23a1955: ('sound_shot', structs.decode_BIG_Q),
    0x55d9abef: ('debugging_mode', structs.decode_BIG_bool_),
}
