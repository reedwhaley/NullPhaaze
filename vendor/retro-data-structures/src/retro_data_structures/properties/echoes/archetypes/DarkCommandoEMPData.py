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
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DarkCommandoEMPDataJson(typing_extensions.TypedDict):
        pre_fire_idle_time: float
        min_attack_range: float
        max_attack_range: float
        grenade_damage: json_util.JsonObject
        grenade_explosion: int
        grenade_effect: int
        grenade_trail: int
        grenade_mass: float
        grenade_bounciness: float
        grenade_min_launch_speed: float
        grenade_max_launch_speed: float
        grenade_num_bounces: int
        emp_duration: float
        sound_grenade_bounce: int
        sound_grenade_explode: int
    

@dataclasses.dataclass()
class DarkCommandoEMPData(BaseProperty):
    pre_fire_idle_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb33a0cbc, original_name='PreFireIdleTime'
        ),
    })
    min_attack_range: float = dataclasses.field(default=35.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x58434916, original_name='MinAttackRange'
        ),
    })
    max_attack_range: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff77c96f, original_name='MaxAttackRange'
        ),
    })
    grenade_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x14d1a3a8, original_name='GrenadeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grenade_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1319e077, original_name='GrenadeExplosion'
        ),
    })
    grenade_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd207ff0f, original_name='GrenadeEffect'
        ),
    })
    grenade_trail: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2b31c882, original_name='GrenadeTrail'
        ),
    })
    grenade_mass: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9a6bb47f, original_name='GrenadeMass'
        ),
    })
    grenade_bounciness: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed086ce0, original_name='GrenadeBounciness'
        ),
    })
    grenade_min_launch_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00fc6646, original_name='GrenadeMinLaunchSpeed'
        ),
    })
    grenade_max_launch_speed: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa7c8e63f, original_name='GrenadeMaxLaunchSpeed'
        ),
    })
    grenade_num_bounces: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x454f16b1, original_name='GrenadeNumBounces'
        ),
    })
    emp_duration: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2d4706e8, original_name='EMPDuration'
        ),
    })
    sound_grenade_bounce: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x258c3e1b, original_name='Sound_GrenadeBounce'
        ),
    })
    sound_grenade_explode: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xaf6aad88, original_name='Sound_GrenadeExplode'
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
        assert property_id == 0xb33a0cbc
        pre_fire_idle_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58434916
        min_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff77c96f
        max_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14d1a3a8
        grenade_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1319e077
        grenade_explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd207ff0f
        grenade_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b31c882
        grenade_trail = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a6bb47f
        grenade_mass = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed086ce0
        grenade_bounciness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00fc6646
        grenade_min_launch_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7c8e63f
        grenade_max_launch_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x454f16b1
        grenade_num_bounces = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2d4706e8
        emp_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x258c3e1b
        sound_grenade_bounce = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf6aad88
        sound_grenade_explode = structs.BIG_l.unpack(data.read(4))[0]
    
        return cls(pre_fire_idle_time, min_attack_range, max_attack_range, grenade_damage, grenade_explosion, grenade_effect, grenade_trail, grenade_mass, grenade_bounciness, grenade_min_launch_speed, grenade_max_launch_speed, grenade_num_bounces, emp_duration, sound_grenade_bounce, sound_grenade_explode)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0f')  # 15 properties

        data.write(b'\xb3:\x0c\xbc')  # 0xb33a0cbc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pre_fire_idle_time))

        data.write(b'XCI\x16')  # 0x58434916
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_attack_range))

        data.write(b'\xffw\xc9o')  # 0xff77c96f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_range))

        data.write(b'\x14\xd1\xa3\xa8')  # 0x14d1a3a8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grenade_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x13\x19\xe0w')  # 0x1319e077
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grenade_explosion))

        data.write(b'\xd2\x07\xff\x0f')  # 0xd207ff0f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grenade_effect))

        data.write(b'+1\xc8\x82')  # 0x2b31c882
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grenade_trail))

        data.write(b'\x9ak\xb4\x7f')  # 0x9a6bb47f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_mass))

        data.write(b'\xed\x08l\xe0')  # 0xed086ce0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_bounciness))

        data.write(b'\x00\xfcfF')  # 0xfc6646
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_min_launch_speed))

        data.write(b'\xa7\xc8\xe6?')  # 0xa7c8e63f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_max_launch_speed))

        data.write(b'EO\x16\xb1')  # 0x454f16b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grenade_num_bounces))

        data.write(b'-G\x06\xe8')  # 0x2d4706e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.emp_duration))

        data.write(b'%\x8c>\x1b')  # 0x258c3e1b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_grenade_bounce))

        data.write(b'\xafj\xad\x88')  # 0xaf6aad88
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_grenade_explode))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkCommandoEMPDataJson", data)
        return cls(
            pre_fire_idle_time=json_data['pre_fire_idle_time'],
            min_attack_range=json_data['min_attack_range'],
            max_attack_range=json_data['max_attack_range'],
            grenade_damage=DamageInfo.from_json(json_data['grenade_damage']),
            grenade_explosion=json_data['grenade_explosion'],
            grenade_effect=json_data['grenade_effect'],
            grenade_trail=json_data['grenade_trail'],
            grenade_mass=json_data['grenade_mass'],
            grenade_bounciness=json_data['grenade_bounciness'],
            grenade_min_launch_speed=json_data['grenade_min_launch_speed'],
            grenade_max_launch_speed=json_data['grenade_max_launch_speed'],
            grenade_num_bounces=json_data['grenade_num_bounces'],
            emp_duration=json_data['emp_duration'],
            sound_grenade_bounce=json_data['sound_grenade_bounce'],
            sound_grenade_explode=json_data['sound_grenade_explode'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'pre_fire_idle_time': self.pre_fire_idle_time,
            'min_attack_range': self.min_attack_range,
            'max_attack_range': self.max_attack_range,
            'grenade_damage': self.grenade_damage.to_json(),
            'grenade_explosion': self.grenade_explosion,
            'grenade_effect': self.grenade_effect,
            'grenade_trail': self.grenade_trail,
            'grenade_mass': self.grenade_mass,
            'grenade_bounciness': self.grenade_bounciness,
            'grenade_min_launch_speed': self.grenade_min_launch_speed,
            'grenade_max_launch_speed': self.grenade_max_launch_speed,
            'grenade_num_bounces': self.grenade_num_bounces,
            'emp_duration': self.emp_duration,
            'sound_grenade_bounce': self.sound_grenade_bounce,
            'sound_grenade_explode': self.sound_grenade_explode,
        }

    def _dependencies_for_grenade_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_explosion)

    def _dependencies_for_grenade_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_effect)

    def _dependencies_for_grenade_trail(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_trail)

    def _dependencies_for_sound_grenade_bounce(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_grenade_bounce)

    def _dependencies_for_sound_grenade_explode(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_grenade_explode)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_grenade_explosion, "grenade_explosion", "AssetId"),
            (self._dependencies_for_grenade_effect, "grenade_effect", "AssetId"),
            (self._dependencies_for_grenade_trail, "grenade_trail", "AssetId"),
            (self._dependencies_for_sound_grenade_bounce, "sound_grenade_bounce", "int"),
            (self._dependencies_for_sound_grenade_explode, "sound_grenade_explode", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DarkCommandoEMPData.{field_name} ({field_type}): {e}"
                )


def _decode_grenade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb33a0cbc: ('pre_fire_idle_time', structs.decode_BIG_f),
    0x58434916: ('min_attack_range', structs.decode_BIG_f),
    0xff77c96f: ('max_attack_range', structs.decode_BIG_f),
    0x14d1a3a8: ('grenade_damage', _decode_grenade_damage),
    0x1319e077: ('grenade_explosion', structs.decode_BIG_L),
    0xd207ff0f: ('grenade_effect', structs.decode_BIG_L),
    0x2b31c882: ('grenade_trail', structs.decode_BIG_L),
    0x9a6bb47f: ('grenade_mass', structs.decode_BIG_f),
    0xed086ce0: ('grenade_bounciness', structs.decode_BIG_f),
    0x00fc6646: ('grenade_min_launch_speed', structs.decode_BIG_f),
    0xa7c8e63f: ('grenade_max_launch_speed', structs.decode_BIG_f),
    0x454f16b1: ('grenade_num_bounces', structs.decode_BIG_l),
    0x2d4706e8: ('emp_duration', structs.decode_BIG_f),
    0x258c3e1b: ('sound_grenade_bounce', structs.decode_BIG_l),
    0xaf6aad88: ('sound_grenade_explode', structs.decode_BIG_l),
}
