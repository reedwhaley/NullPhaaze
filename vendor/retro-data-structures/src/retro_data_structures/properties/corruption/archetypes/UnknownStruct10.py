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

    class UnknownStruct10Json(typing_extensions.TypedDict):
        attract: bool
        repulse: bool
        rotate: bool
        power: float
        radius: float
        alpha_target: float
        alpha_delta: float
        x_ray_alpha_target: float
        x_ray_alpha_delta: float
        cloud_alpha_target: float
        cloud_alpha_delta: float
        cloud_x_ray_alpha_target: float
        cloud_x_ray_alpha_delta: float
        flash: bool
        explode: bool
        die: bool
        flash_damage: json_util.JsonObject
        explode_damage: json_util.JsonObject
        sound: int
        auto_transition: bool
        duration: float
        duration_variance: float
    

@dataclasses.dataclass()
class UnknownStruct10(BaseProperty):
    attract: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe4103cce, original_name='Attract'
        ),
    })
    repulse: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x73c0f1ae, original_name='Repulse'
        ),
    })
    rotate: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x923109d6, original_name='Rotate'
        ),
    })
    power: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x10cda13d, original_name='Power'
        ),
    })
    radius: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x78c507eb, original_name='Radius'
        ),
    })
    alpha_target: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2d72a3d3, original_name='AlphaTarget'
        ),
    })
    alpha_delta: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a1d3a89, original_name='AlphaDelta'
        ),
    })
    x_ray_alpha_target: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa19c4b46, original_name='XRayAlphaTarget'
        ),
    })
    x_ray_alpha_delta: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x17895cd7, original_name='XRayAlphaDelta'
        ),
    })
    cloud_alpha_target: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf66ca675, original_name='CloudAlphaTarget'
        ),
    })
    cloud_alpha_delta: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8fd14aa3, original_name='CloudAlphaDelta'
        ),
    })
    cloud_x_ray_alpha_target: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0a17fbf7, original_name='CloudXRayAlphaTarget'
        ),
    })
    cloud_x_ray_alpha_delta: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4d04b4f8, original_name='CloudXRayAlphaDelta'
        ),
    })
    flash: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4ecac914, original_name='Flash'
        ),
    })
    explode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x6a922800, original_name='Explode'
        ),
    })
    die: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xd83b3eca, original_name='Die'
        ),
    })
    flash_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x6a5bd5e5, original_name='FlashDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    explode_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xf6206a12, original_name='ExplodeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa55dacf6, original_name='Sound'
        ),
    })
    auto_transition: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x6575bf29, original_name='AutoTransition'
        ),
    })
    duration: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b51e23f, original_name='Duration'
        ),
    })
    duration_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe8835d69, original_name='DurationVariance'
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
        if property_count != 22:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe4103cce
        attract = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73c0f1ae
        repulse = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x923109d6
        rotate = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10cda13d
        power = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78c507eb
        radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2d72a3d3
        alpha_target = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a1d3a89
        alpha_delta = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa19c4b46
        x_ray_alpha_target = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17895cd7
        x_ray_alpha_delta = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf66ca675
        cloud_alpha_target = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8fd14aa3
        cloud_alpha_delta = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a17fbf7
        cloud_x_ray_alpha_target = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d04b4f8
        cloud_x_ray_alpha_delta = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ecac914
        flash = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6a922800
        explode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd83b3eca
        die = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6a5bd5e5
        flash_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6206a12
        explode_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa55dacf6
        sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6575bf29
        auto_transition = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b51e23f
        duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8835d69
        duration_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(attract, repulse, rotate, power, radius, alpha_target, alpha_delta, x_ray_alpha_target, x_ray_alpha_delta, cloud_alpha_target, cloud_alpha_delta, cloud_x_ray_alpha_target, cloud_x_ray_alpha_delta, flash, explode, die, flash_damage, explode_damage, sound, auto_transition, duration, duration_variance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x16')  # 22 properties

        data.write(b'\xe4\x10<\xce')  # 0xe4103cce
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.attract))

        data.write(b's\xc0\xf1\xae')  # 0x73c0f1ae
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.repulse))

        data.write(b'\x921\t\xd6')  # 0x923109d6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rotate))

        data.write(b'\x10\xcd\xa1=')  # 0x10cda13d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.power))

        data.write(b'x\xc5\x07\xeb')  # 0x78c507eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.radius))

        data.write(b'-r\xa3\xd3')  # 0x2d72a3d3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.alpha_target))

        data.write(b'*\x1d:\x89')  # 0x2a1d3a89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.alpha_delta))

        data.write(b'\xa1\x9cKF')  # 0xa19c4b46
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_alpha_target))

        data.write(b'\x17\x89\\\xd7')  # 0x17895cd7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_alpha_delta))

        data.write(b'\xf6l\xa6u')  # 0xf66ca675
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloud_alpha_target))

        data.write(b'\x8f\xd1J\xa3')  # 0x8fd14aa3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloud_alpha_delta))

        data.write(b'\n\x17\xfb\xf7')  # 0xa17fbf7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloud_x_ray_alpha_target))

        data.write(b'M\x04\xb4\xf8')  # 0x4d04b4f8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloud_x_ray_alpha_delta))

        data.write(b'N\xca\xc9\x14')  # 0x4ecac914
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.flash))

        data.write(b'j\x92(\x00')  # 0x6a922800
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.explode))

        data.write(b'\xd8;>\xca')  # 0xd83b3eca
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.die))

        data.write(b'j[\xd5\xe5')  # 0x6a5bd5e5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flash_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf6 j\x12')  # 0xf6206a12
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.explode_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa5]\xac\xf6')  # 0xa55dacf6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound))

        data.write(b'eu\xbf)')  # 0x6575bf29
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.auto_transition))

        data.write(b'\x8bQ\xe2?')  # 0x8b51e23f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b'\xe8\x83]i')  # 0xe8835d69
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.duration_variance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct10Json", data)
        return cls(
            attract=json_data['attract'],
            repulse=json_data['repulse'],
            rotate=json_data['rotate'],
            power=json_data['power'],
            radius=json_data['radius'],
            alpha_target=json_data['alpha_target'],
            alpha_delta=json_data['alpha_delta'],
            x_ray_alpha_target=json_data['x_ray_alpha_target'],
            x_ray_alpha_delta=json_data['x_ray_alpha_delta'],
            cloud_alpha_target=json_data['cloud_alpha_target'],
            cloud_alpha_delta=json_data['cloud_alpha_delta'],
            cloud_x_ray_alpha_target=json_data['cloud_x_ray_alpha_target'],
            cloud_x_ray_alpha_delta=json_data['cloud_x_ray_alpha_delta'],
            flash=json_data['flash'],
            explode=json_data['explode'],
            die=json_data['die'],
            flash_damage=DamageInfo.from_json(json_data['flash_damage']),
            explode_damage=DamageInfo.from_json(json_data['explode_damage']),
            sound=json_data['sound'],
            auto_transition=json_data['auto_transition'],
            duration=json_data['duration'],
            duration_variance=json_data['duration_variance'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'attract': self.attract,
            'repulse': self.repulse,
            'rotate': self.rotate,
            'power': self.power,
            'radius': self.radius,
            'alpha_target': self.alpha_target,
            'alpha_delta': self.alpha_delta,
            'x_ray_alpha_target': self.x_ray_alpha_target,
            'x_ray_alpha_delta': self.x_ray_alpha_delta,
            'cloud_alpha_target': self.cloud_alpha_target,
            'cloud_alpha_delta': self.cloud_alpha_delta,
            'cloud_x_ray_alpha_target': self.cloud_x_ray_alpha_target,
            'cloud_x_ray_alpha_delta': self.cloud_x_ray_alpha_delta,
            'flash': self.flash,
            'explode': self.explode,
            'die': self.die,
            'flash_damage': self.flash_damage.to_json(),
            'explode_damage': self.explode_damage.to_json(),
            'sound': self.sound,
            'auto_transition': self.auto_transition,
            'duration': self.duration,
            'duration_variance': self.duration_variance,
        }

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_sound(asset_manager)


def _decode_flash_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_explode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xe4103cce: ('attract', structs.decode_BIG_bool_),
    0x73c0f1ae: ('repulse', structs.decode_BIG_bool_),
    0x923109d6: ('rotate', structs.decode_BIG_bool_),
    0x10cda13d: ('power', structs.decode_BIG_f),
    0x78c507eb: ('radius', structs.decode_BIG_f),
    0x2d72a3d3: ('alpha_target', structs.decode_BIG_f),
    0x2a1d3a89: ('alpha_delta', structs.decode_BIG_f),
    0xa19c4b46: ('x_ray_alpha_target', structs.decode_BIG_f),
    0x17895cd7: ('x_ray_alpha_delta', structs.decode_BIG_f),
    0xf66ca675: ('cloud_alpha_target', structs.decode_BIG_f),
    0x8fd14aa3: ('cloud_alpha_delta', structs.decode_BIG_f),
    0x0a17fbf7: ('cloud_x_ray_alpha_target', structs.decode_BIG_f),
    0x4d04b4f8: ('cloud_x_ray_alpha_delta', structs.decode_BIG_f),
    0x4ecac914: ('flash', structs.decode_BIG_bool_),
    0x6a922800: ('explode', structs.decode_BIG_bool_),
    0xd83b3eca: ('die', structs.decode_BIG_bool_),
    0x6a5bd5e5: ('flash_damage', _decode_flash_damage),
    0xf6206a12: ('explode_damage', _decode_explode_damage),
    0xa55dacf6: ('sound', structs.decode_BIG_Q),
    0x6575bf29: ('auto_transition', structs.decode_BIG_bool_),
    0x8b51e23f: ('duration', structs.decode_BIG_f),
    0xe8835d69: ('duration_variance', structs.decode_BIG_f),
}
