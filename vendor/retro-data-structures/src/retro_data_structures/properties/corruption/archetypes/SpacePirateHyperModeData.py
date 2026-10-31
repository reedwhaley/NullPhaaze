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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SpacePirateHyperModeDataJson(typing_extensions.TypedDict):
        enable_hyper_mode: bool
        initial_hyper_mode_time: float
        hyper_mode_check_time: float
        hyper_mode_check_chance: float
        hyper_mode_duration: float
        skip_taunt: bool
        unknown: bool
        shot_projectile: int
        sound_projectile: int
        shot_damage: json_util.JsonObject
        intra_burst_shot_time: float
        intra_burst_shot_variation: float
        hyper_mode_attack_time: float
        hyper_mode_attack_time_variance: float
        hyper_mode_vulnerability: json_util.JsonObject
    

@dataclasses.dataclass()
class SpacePirateHyperModeData(BaseProperty):
    enable_hyper_mode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xdd448cc9, original_name='EnableHyperMode'
        ),
    })
    initial_hyper_mode_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8a834618, original_name='InitialHyperModeTime'
        ),
    })
    hyper_mode_check_time: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe9fd5a01, original_name='HyperModeCheckTime'
        ),
    })
    hyper_mode_check_chance: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf04452f3, original_name='HyperModeCheckChance'
        ),
    })
    hyper_mode_duration: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa3f3be5d, original_name='HyperModeDuration'
        ),
    })
    skip_taunt: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x071d8999, original_name='SkipTaunt'
        ),
    })
    unknown: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xdb922374, original_name='Unknown'
        ),
    })
    shot_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x51253ba3, original_name='ShotProjectile'
        ),
    })
    sound_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x10e3efdd, original_name='Sound_Projectile'
        ),
    })
    shot_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xcea30138, original_name='ShotDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    intra_burst_shot_time: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71587b45, original_name='IntraBurstShotTime'
        ),
    })
    intra_burst_shot_variation: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7903312e, original_name='IntraBurstShotVariation'
        ),
    })
    hyper_mode_attack_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe9b7d4ee, original_name='HyperModeAttackTime'
        ),
    })
    hyper_mode_attack_time_variance: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xca686731, original_name='HyperModeAttackTimeVariance'
        ),
    })
    hyper_mode_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xc8a1eac8, original_name='HyperModeVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        assert property_id == 0xdd448cc9
        enable_hyper_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8a834618
        initial_hyper_mode_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9fd5a01
        hyper_mode_check_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf04452f3
        hyper_mode_check_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3f3be5d
        hyper_mode_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x071d8999
        skip_taunt = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdb922374
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51253ba3
        shot_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10e3efdd
        sound_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcea30138
        shot_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71587b45
        intra_burst_shot_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7903312e
        intra_burst_shot_variation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9b7d4ee
        hyper_mode_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca686731
        hyper_mode_attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8a1eac8
        hyper_mode_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(enable_hyper_mode, initial_hyper_mode_time, hyper_mode_check_time, hyper_mode_check_chance, hyper_mode_duration, skip_taunt, unknown, shot_projectile, sound_projectile, shot_damage, intra_burst_shot_time, intra_burst_shot_variation, hyper_mode_attack_time, hyper_mode_attack_time_variance, hyper_mode_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0f')  # 15 properties

        data.write(b'\xddD\x8c\xc9')  # 0xdd448cc9
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.enable_hyper_mode))

        data.write(b'\x8a\x83F\x18')  # 0x8a834618
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_hyper_mode_time))

        data.write(b'\xe9\xfdZ\x01')  # 0xe9fd5a01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_check_time))

        data.write(b'\xf0DR\xf3')  # 0xf04452f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_check_chance))

        data.write(b'\xa3\xf3\xbe]')  # 0xa3f3be5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_duration))

        data.write(b'\x07\x1d\x89\x99')  # 0x71d8999
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.skip_taunt))

        data.write(b'\xdb\x92#t')  # 0xdb922374
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b'Q%;\xa3')  # 0x51253ba3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shot_projectile))

        data.write(b'\x10\xe3\xef\xdd')  # 0x10e3efdd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_projectile))

        data.write(b'\xce\xa3\x018')  # 0xcea30138
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shot_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'qX{E')  # 0x71587b45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.intra_burst_shot_time))

        data.write(b'y\x031.')  # 0x7903312e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.intra_burst_shot_variation))

        data.write(b'\xe9\xb7\xd4\xee')  # 0xe9b7d4ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_attack_time))

        data.write(b'\xcahg1')  # 0xca686731
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_attack_time_variance))

        data.write(b'\xc8\xa1\xea\xc8')  # 0xc8a1eac8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpacePirateHyperModeDataJson", data)
        return cls(
            enable_hyper_mode=json_data['enable_hyper_mode'],
            initial_hyper_mode_time=json_data['initial_hyper_mode_time'],
            hyper_mode_check_time=json_data['hyper_mode_check_time'],
            hyper_mode_check_chance=json_data['hyper_mode_check_chance'],
            hyper_mode_duration=json_data['hyper_mode_duration'],
            skip_taunt=json_data['skip_taunt'],
            unknown=json_data['unknown'],
            shot_projectile=json_data['shot_projectile'],
            sound_projectile=json_data['sound_projectile'],
            shot_damage=DamageInfo.from_json(json_data['shot_damage']),
            intra_burst_shot_time=json_data['intra_burst_shot_time'],
            intra_burst_shot_variation=json_data['intra_burst_shot_variation'],
            hyper_mode_attack_time=json_data['hyper_mode_attack_time'],
            hyper_mode_attack_time_variance=json_data['hyper_mode_attack_time_variance'],
            hyper_mode_vulnerability=DamageVulnerability.from_json(json_data['hyper_mode_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'enable_hyper_mode': self.enable_hyper_mode,
            'initial_hyper_mode_time': self.initial_hyper_mode_time,
            'hyper_mode_check_time': self.hyper_mode_check_time,
            'hyper_mode_check_chance': self.hyper_mode_check_chance,
            'hyper_mode_duration': self.hyper_mode_duration,
            'skip_taunt': self.skip_taunt,
            'unknown': self.unknown,
            'shot_projectile': self.shot_projectile,
            'sound_projectile': self.sound_projectile,
            'shot_damage': self.shot_damage.to_json(),
            'intra_burst_shot_time': self.intra_burst_shot_time,
            'intra_burst_shot_variation': self.intra_burst_shot_variation,
            'hyper_mode_attack_time': self.hyper_mode_attack_time,
            'hyper_mode_attack_time_variance': self.hyper_mode_attack_time_variance,
            'hyper_mode_vulnerability': self.hyper_mode_vulnerability.to_json(),
        }

    def _dependencies_for_shot_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shot_projectile)

    def _dependencies_for_sound_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_shot_projectile, "shot_projectile", "AssetId"),
            (self._dependencies_for_sound_projectile, "sound_projectile", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SpacePirateHyperModeData.{field_name} ({field_type}): {e}"
                )


def _decode_shot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_hyper_mode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xdd448cc9: ('enable_hyper_mode', structs.decode_BIG_bool_),
    0x8a834618: ('initial_hyper_mode_time', structs.decode_BIG_f),
    0xe9fd5a01: ('hyper_mode_check_time', structs.decode_BIG_f),
    0xf04452f3: ('hyper_mode_check_chance', structs.decode_BIG_f),
    0xa3f3be5d: ('hyper_mode_duration', structs.decode_BIG_f),
    0x071d8999: ('skip_taunt', structs.decode_BIG_bool_),
    0xdb922374: ('unknown', structs.decode_BIG_bool_),
    0x51253ba3: ('shot_projectile', structs.decode_BIG_Q),
    0x10e3efdd: ('sound_projectile', structs.decode_BIG_Q),
    0xcea30138: ('shot_damage', _decode_shot_damage),
    0x71587b45: ('intra_burst_shot_time', structs.decode_BIG_f),
    0x7903312e: ('intra_burst_shot_variation', structs.decode_BIG_f),
    0xe9b7d4ee: ('hyper_mode_attack_time', structs.decode_BIG_f),
    0xca686731: ('hyper_mode_attack_time_variance', structs.decode_BIG_f),
    0xc8a1eac8: ('hyper_mode_vulnerability', _decode_hyper_mode_vulnerability),
}
