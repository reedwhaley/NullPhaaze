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
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SamusFormBoostBallDataJson(typing_extensions.TypedDict):
        animation: json_util.JsonObject
        roll_speed_scale: float
        unknown_0x205db165: float
        unknown_0x45515b5e: float
        damage_info: json_util.JsonObject
        trail_effect: int
        glow_effect: int
        wall_collision_sound: int
        player_collision_sound: int
        player_morph_ball_collision_sound: int
    

@dataclasses.dataclass()
class SamusFormBoostBallData(BaseProperty):
    animation: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa3d63f44, original_name='Animation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    roll_speed_scale: float = dataclasses.field(default=1.2999999523162842, metadata={
        'reflection': FieldReflection[float](
            float, id=0x60ac7175, original_name='RollSpeedScale'
        ),
    })
    unknown_0x205db165: float = dataclasses.field(default=3.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x205db165, original_name='Unknown'
        ),
    })
    unknown_0x45515b5e: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x45515b5e, original_name='Unknown'
        ),
    })
    damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xc97013d0, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    trail_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x36eee791, original_name='TrailEffect'
        ),
    })
    glow_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x845bd2ee, original_name='GlowEffect'
        ),
    })
    wall_collision_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4faba78a, original_name='WallCollisionSound'
        ),
    })
    player_collision_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe90069bd, original_name='PlayerCollisionSound'
        ),
    })
    player_morph_ball_collision_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6ab7c2f5, original_name='PlayerMorphBallCollisionSound'
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
        if property_count != 10:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3d63f44
        animation = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60ac7175
        roll_speed_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x205db165
        unknown_0x205db165 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45515b5e
        unknown_0x45515b5e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc97013d0
        damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36eee791
        trail_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x845bd2ee
        glow_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4faba78a
        wall_collision_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe90069bd
        player_collision_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ab7c2f5
        player_morph_ball_collision_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(animation, roll_speed_scale, unknown_0x205db165, unknown_0x45515b5e, damage_info, trail_effect, glow_effect, wall_collision_sound, player_collision_sound, player_morph_ball_collision_sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\xa3\xd6?D')  # 0xa3d63f44
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'`\xacqu')  # 0x60ac7175
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.roll_speed_scale))

        data.write(b' ]\xb1e')  # 0x205db165
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x205db165))

        data.write(b'EQ[^')  # 0x45515b5e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x45515b5e))

        data.write(b'\xc9p\x13\xd0')  # 0xc97013d0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'6\xee\xe7\x91')  # 0x36eee791
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.trail_effect))

        data.write(b'\x84[\xd2\xee')  # 0x845bd2ee
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.glow_effect))

        data.write(b'O\xab\xa7\x8a')  # 0x4faba78a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wall_collision_sound))

        data.write(b'\xe9\x00i\xbd')  # 0xe90069bd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.player_collision_sound))

        data.write(b'j\xb7\xc2\xf5')  # 0x6ab7c2f5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.player_morph_ball_collision_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SamusFormBoostBallDataJson", data)
        return cls(
            animation=AnimationParameters.from_json(json_data['animation']),
            roll_speed_scale=json_data['roll_speed_scale'],
            unknown_0x205db165=json_data['unknown_0x205db165'],
            unknown_0x45515b5e=json_data['unknown_0x45515b5e'],
            damage_info=DamageInfo.from_json(json_data['damage_info']),
            trail_effect=json_data['trail_effect'],
            glow_effect=json_data['glow_effect'],
            wall_collision_sound=json_data['wall_collision_sound'],
            player_collision_sound=json_data['player_collision_sound'],
            player_morph_ball_collision_sound=json_data['player_morph_ball_collision_sound'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'animation': self.animation.to_json(),
            'roll_speed_scale': self.roll_speed_scale,
            'unknown_0x205db165': self.unknown_0x205db165,
            'unknown_0x45515b5e': self.unknown_0x45515b5e,
            'damage_info': self.damage_info.to_json(),
            'trail_effect': self.trail_effect,
            'glow_effect': self.glow_effect,
            'wall_collision_sound': self.wall_collision_sound,
            'player_collision_sound': self.player_collision_sound,
            'player_morph_ball_collision_sound': self.player_morph_ball_collision_sound,
        }

    def _dependencies_for_trail_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.trail_effect)

    def _dependencies_for_glow_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.glow_effect)

    def _dependencies_for_wall_collision_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wall_collision_sound)

    def _dependencies_for_player_collision_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.player_collision_sound)

    def _dependencies_for_player_morph_ball_collision_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.player_morph_ball_collision_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.animation.dependencies_for, "animation", "AnimationParameters"),
            (self._dependencies_for_trail_effect, "trail_effect", "AssetId"),
            (self._dependencies_for_glow_effect, "glow_effect", "AssetId"),
            (self._dependencies_for_wall_collision_sound, "wall_collision_sound", "AssetId"),
            (self._dependencies_for_player_collision_sound, "player_collision_sound", "AssetId"),
            (self._dependencies_for_player_morph_ball_collision_sound, "player_morph_ball_collision_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SamusFormBoostBallData.{field_name} ({field_type}): {e}"
                )


def _decode_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa3d63f44: ('animation', _decode_animation),
    0x60ac7175: ('roll_speed_scale', structs.decode_BIG_f),
    0x205db165: ('unknown_0x205db165', structs.decode_BIG_f),
    0x45515b5e: ('unknown_0x45515b5e', structs.decode_BIG_f),
    0xc97013d0: ('damage_info', _decode_damage_info),
    0x36eee791: ('trail_effect', structs.decode_BIG_Q),
    0x845bd2ee: ('glow_effect', structs.decode_BIG_Q),
    0x4faba78a: ('wall_collision_sound', structs.decode_BIG_Q),
    0xe90069bd: ('player_collision_sound', structs.decode_BIG_Q),
    0x6ab7c2f5: ('player_morph_ball_collision_sound', structs.decode_BIG_Q),
}
