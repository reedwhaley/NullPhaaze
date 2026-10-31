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
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PhaazoidDataJson(typing_extensions.TypedDict):
        stage: int
        contains_red_phaazoid: bool
        play_initial_anim: bool
        acceleration: float
        max_speed: float
        min_attack_dist: float
        max_attack_dist: float
        min_horizontal_shot_height: float
        max_horizontal_shot_height: float
        moving_map_opacity: float
        max_vertical_shot_height: float
        torus_ring: json_util.JsonObject
        phaazoid_projectile: int
        phaazoid_projectile_damage_info: json_util.JsonObject
    

@dataclasses.dataclass()
class PhaazoidData(BaseProperty):
    stage: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb25774e2, original_name='Stage'
        ),
    })  # Choice
    contains_red_phaazoid: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x02a3e092, original_name='ContainsRedPhaazoid'
        ),
    })
    play_initial_anim: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x88fde98c, original_name='PlayInitialAnim'
        ),
    })
    acceleration: float = dataclasses.field(default=65.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x39fb7978, original_name='Acceleration'
        ),
    })
    max_speed: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x82db0cbe, original_name='MaxSpeed'
        ),
    })
    min_attack_dist: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d7447b4, original_name='MinAttackDist'
        ),
    })
    max_attack_dist: float = dataclasses.field(default=35.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ed25f50, original_name='MaxAttackDist'
        ),
    })
    min_horizontal_shot_height: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb5d19503, original_name='MinHorizontalShotHeight'
        ),
    })
    max_horizontal_shot_height: float = dataclasses.field(default=3.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe2dfc540, original_name='MaxHorizontalShotHeight'
        ),
    })
    moving_map_opacity: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3317d0c6, original_name='MovingMapOpacity'
        ),
    })
    max_vertical_shot_height: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd04a6e1c, original_name='MaxVerticalShotHeight'
        ),
    })
    torus_ring: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x12b8e543, original_name='TorusRing', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    phaazoid_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe8cd9627, original_name='PhaazoidProjectile'
        ),
    })
    phaazoid_projectile_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x1dc69e38, original_name='PhaazoidProjectileDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
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
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb25774e2
        stage = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02a3e092
        contains_red_phaazoid = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88fde98c
        play_initial_anim = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39fb7978
        acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82db0cbe
        max_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d7447b4
        min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ed25f50
        max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5d19503
        min_horizontal_shot_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe2dfc540
        max_horizontal_shot_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3317d0c6
        moving_map_opacity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd04a6e1c
        max_vertical_shot_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12b8e543
        torus_ring = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8cd9627
        phaazoid_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1dc69e38
        phaazoid_projectile_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        return cls(stage, contains_red_phaazoid, play_initial_anim, acceleration, max_speed, min_attack_dist, max_attack_dist, min_horizontal_shot_height, max_horizontal_shot_height, moving_map_opacity, max_vertical_shot_height, torus_ring, phaazoid_projectile, phaazoid_projectile_damage_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0e')  # 14 properties

        data.write(b'\xb2Wt\xe2')  # 0xb25774e2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.stage))

        data.write(b'\x02\xa3\xe0\x92')  # 0x2a3e092
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.contains_red_phaazoid))

        data.write(b'\x88\xfd\xe9\x8c')  # 0x88fde98c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.play_initial_anim))

        data.write(b'9\xfbyx')  # 0x39fb7978
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.acceleration))

        data.write(b'\x82\xdb\x0c\xbe')  # 0x82db0cbe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_speed))

        data.write(b'}tG\xb4')  # 0x7d7447b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_attack_dist))

        data.write(b'.\xd2_P')  # 0x2ed25f50
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_dist))

        data.write(b'\xb5\xd1\x95\x03')  # 0xb5d19503
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_horizontal_shot_height))

        data.write(b'\xe2\xdf\xc5@')  # 0xe2dfc540
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_horizontal_shot_height))

        data.write(b'3\x17\xd0\xc6')  # 0x3317d0c6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.moving_map_opacity))

        data.write(b'\xd0Jn\x1c')  # 0xd04a6e1c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_vertical_shot_height))

        data.write(b'\x12\xb8\xe5C')  # 0x12b8e543
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.torus_ring.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe8\xcd\x96'")  # 0xe8cd9627
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.phaazoid_projectile))

        data.write(b'\x1d\xc6\x9e8')  # 0x1dc69e38
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phaazoid_projectile_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PhaazoidDataJson", data)
        return cls(
            stage=json_data['stage'],
            contains_red_phaazoid=json_data['contains_red_phaazoid'],
            play_initial_anim=json_data['play_initial_anim'],
            acceleration=json_data['acceleration'],
            max_speed=json_data['max_speed'],
            min_attack_dist=json_data['min_attack_dist'],
            max_attack_dist=json_data['max_attack_dist'],
            min_horizontal_shot_height=json_data['min_horizontal_shot_height'],
            max_horizontal_shot_height=json_data['max_horizontal_shot_height'],
            moving_map_opacity=json_data['moving_map_opacity'],
            max_vertical_shot_height=json_data['max_vertical_shot_height'],
            torus_ring=ShockWaveInfo.from_json(json_data['torus_ring']),
            phaazoid_projectile=json_data['phaazoid_projectile'],
            phaazoid_projectile_damage_info=DamageInfo.from_json(json_data['phaazoid_projectile_damage_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'stage': self.stage,
            'contains_red_phaazoid': self.contains_red_phaazoid,
            'play_initial_anim': self.play_initial_anim,
            'acceleration': self.acceleration,
            'max_speed': self.max_speed,
            'min_attack_dist': self.min_attack_dist,
            'max_attack_dist': self.max_attack_dist,
            'min_horizontal_shot_height': self.min_horizontal_shot_height,
            'max_horizontal_shot_height': self.max_horizontal_shot_height,
            'moving_map_opacity': self.moving_map_opacity,
            'max_vertical_shot_height': self.max_vertical_shot_height,
            'torus_ring': self.torus_ring.to_json(),
            'phaazoid_projectile': self.phaazoid_projectile,
            'phaazoid_projectile_damage_info': self.phaazoid_projectile_damage_info.to_json(),
        }

    def _dependencies_for_phaazoid_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phaazoid_projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.torus_ring.dependencies_for, "torus_ring", "ShockWaveInfo"),
            (self._dependencies_for_phaazoid_projectile, "phaazoid_projectile", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PhaazoidData.{field_name} ({field_type}): {e}"
                )


def _decode_torus_ring(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_phaazoid_projectile_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb25774e2: ('stage', structs.decode_BIG_L),
    0x02a3e092: ('contains_red_phaazoid', structs.decode_BIG_bool_),
    0x88fde98c: ('play_initial_anim', structs.decode_BIG_bool_),
    0x39fb7978: ('acceleration', structs.decode_BIG_f),
    0x82db0cbe: ('max_speed', structs.decode_BIG_f),
    0x7d7447b4: ('min_attack_dist', structs.decode_BIG_f),
    0x2ed25f50: ('max_attack_dist', structs.decode_BIG_f),
    0xb5d19503: ('min_horizontal_shot_height', structs.decode_BIG_f),
    0xe2dfc540: ('max_horizontal_shot_height', structs.decode_BIG_f),
    0x3317d0c6: ('moving_map_opacity', structs.decode_BIG_f),
    0xd04a6e1c: ('max_vertical_shot_height', structs.decode_BIG_f),
    0x12b8e543: ('torus_ring', _decode_torus_ring),
    0xe8cd9627: ('phaazoid_projectile', structs.decode_BIG_Q),
    0x1dc69e38: ('phaazoid_projectile_damage_info', _decode_phaazoid_projectile_damage_info),
}
