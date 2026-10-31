# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PlayerTurretJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flags: int
        max_horiz_rotation_left: float
        max_horiz_rotation_right: float
        max_vert_elevation_up: float
        max_vert_elevation_down: float
        damage_angle: float
        horiz_speed: float
        vert_speed: float
        fire_rate: float
        weapon_damage: json_util.JsonObject
        weapon_effect: int
        weapon_effect_multi_player: int
        sfx_turret_rotation: int
        sfx_single_player_impact: int
        sfx_multi_player_impact: int
        sfx_single_player_projectile: int
        sfx_multi_player_projectile: int
    

@dataclasses.dataclass()
class PlayerTurret(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    flags: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xeeadefa6, original_name='Flags'
        ),
    })  # Flagset
    max_horiz_rotation_left: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x17cd8b2a, original_name='MaxHorizRotationLeft'
        ),
    })
    max_horiz_rotation_right: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1473dad2, original_name='MaxHorizRotationRight'
        ),
    })
    max_vert_elevation_up: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3650ce75, original_name='MaxVertElevationUp'
        ),
    })
    max_vert_elevation_down: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x78520e6e, original_name='MaxVertElevationDown'
        ),
    })
    damage_angle: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa39a5d72, original_name='DamageAngle'
        ),
    })
    horiz_speed: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfb2e32db, original_name='HorizSpeed'
        ),
    })
    vert_speed: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b3c8683, original_name='VertSpeed'
        ),
    })
    fire_rate: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc6e48f18, original_name='FireRate'
        ),
    })
    weapon_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x8e5f7e96, original_name='WeaponDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    weapon_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc43360a7, original_name='WeaponEffect'
        ),
    })
    weapon_effect_multi_player: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa99d3dbe, original_name='WeaponEffectMultiPlayer'
        ),
    })
    sfx_turret_rotation: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe7234f72, original_name='SFXTurretRotation'
        ),
    })
    sfx_single_player_impact: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x3e2f7afb, original_name='SFXSinglePlayerImpact'
        ),
    })
    sfx_multi_player_impact: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x7cabd1f1, original_name='SFXMultiPlayerImpact'
        ),
    })
    sfx_single_player_projectile: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x7ef976eb, original_name='SFXSinglePlayerProjectile'
        ),
    })
    sfx_multi_player_projectile: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x035459fd, original_name='SFXMultiPlayerProjectile'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'PLRT'

    @classmethod
    def modules(cls) -> list[str]:
        return ['ScriptPlayerTurret.rel']

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 18:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeeadefa6
        flags = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17cd8b2a
        max_horiz_rotation_left = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1473dad2
        max_horiz_rotation_right = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3650ce75
        max_vert_elevation_up = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78520e6e
        max_vert_elevation_down = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa39a5d72
        damage_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb2e32db
        horiz_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b3c8683
        vert_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6e48f18
        fire_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e5f7e96
        weapon_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc43360a7
        weapon_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa99d3dbe
        weapon_effect_multi_player = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7234f72
        sfx_turret_rotation = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e2f7afb
        sfx_single_player_impact = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7cabd1f1
        sfx_multi_player_impact = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ef976eb
        sfx_single_player_projectile = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x035459fd
        sfx_multi_player_projectile = structs.BIG_l.unpack(data.read(4))[0]
    
        return cls(editor_properties, flags, max_horiz_rotation_left, max_horiz_rotation_right, max_vert_elevation_up, max_vert_elevation_down, damage_angle, horiz_speed, vert_speed, fire_rate, weapon_damage, weapon_effect, weapon_effect_multi_player, sfx_turret_rotation, sfx_single_player_impact, sfx_multi_player_impact, sfx_single_player_projectile, sfx_multi_player_projectile)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x12')  # 18 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xee\xad\xef\xa6')  # 0xeeadefa6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.flags))

        data.write(b'\x17\xcd\x8b*')  # 0x17cd8b2a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_horiz_rotation_left))

        data.write(b'\x14s\xda\xd2')  # 0x1473dad2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_horiz_rotation_right))

        data.write(b'6P\xceu')  # 0x3650ce75
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_vert_elevation_up))

        data.write(b'xR\x0en')  # 0x78520e6e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_vert_elevation_down))

        data.write(b'\xa3\x9a]r')  # 0xa39a5d72
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_angle))

        data.write(b'\xfb.2\xdb')  # 0xfb2e32db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.horiz_speed))

        data.write(b'\x1b<\x86\x83')  # 0x1b3c8683
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vert_speed))

        data.write(b'\xc6\xe4\x8f\x18')  # 0xc6e48f18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fire_rate))

        data.write(b'\x8e_~\x96')  # 0x8e5f7e96
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weapon_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc43`\xa7')  # 0xc43360a7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.weapon_effect))

        data.write(b'\xa9\x9d=\xbe')  # 0xa99d3dbe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.weapon_effect_multi_player))

        data.write(b'\xe7#Or')  # 0xe7234f72
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sfx_turret_rotation))

        data.write(b'>/z\xfb')  # 0x3e2f7afb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sfx_single_player_impact))

        data.write(b'|\xab\xd1\xf1')  # 0x7cabd1f1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sfx_multi_player_impact))

        data.write(b'~\xf9v\xeb')  # 0x7ef976eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sfx_single_player_projectile))

        data.write(b'\x03TY\xfd')  # 0x35459fd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sfx_multi_player_projectile))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerTurretJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            flags=json_data['flags'],
            max_horiz_rotation_left=json_data['max_horiz_rotation_left'],
            max_horiz_rotation_right=json_data['max_horiz_rotation_right'],
            max_vert_elevation_up=json_data['max_vert_elevation_up'],
            max_vert_elevation_down=json_data['max_vert_elevation_down'],
            damage_angle=json_data['damage_angle'],
            horiz_speed=json_data['horiz_speed'],
            vert_speed=json_data['vert_speed'],
            fire_rate=json_data['fire_rate'],
            weapon_damage=DamageInfo.from_json(json_data['weapon_damage']),
            weapon_effect=json_data['weapon_effect'],
            weapon_effect_multi_player=json_data['weapon_effect_multi_player'],
            sfx_turret_rotation=json_data['sfx_turret_rotation'],
            sfx_single_player_impact=json_data['sfx_single_player_impact'],
            sfx_multi_player_impact=json_data['sfx_multi_player_impact'],
            sfx_single_player_projectile=json_data['sfx_single_player_projectile'],
            sfx_multi_player_projectile=json_data['sfx_multi_player_projectile'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'flags': self.flags,
            'max_horiz_rotation_left': self.max_horiz_rotation_left,
            'max_horiz_rotation_right': self.max_horiz_rotation_right,
            'max_vert_elevation_up': self.max_vert_elevation_up,
            'max_vert_elevation_down': self.max_vert_elevation_down,
            'damage_angle': self.damage_angle,
            'horiz_speed': self.horiz_speed,
            'vert_speed': self.vert_speed,
            'fire_rate': self.fire_rate,
            'weapon_damage': self.weapon_damage.to_json(),
            'weapon_effect': self.weapon_effect,
            'weapon_effect_multi_player': self.weapon_effect_multi_player,
            'sfx_turret_rotation': self.sfx_turret_rotation,
            'sfx_single_player_impact': self.sfx_single_player_impact,
            'sfx_multi_player_impact': self.sfx_multi_player_impact,
            'sfx_single_player_projectile': self.sfx_single_player_projectile,
            'sfx_multi_player_projectile': self.sfx_multi_player_projectile,
        }

    def _dependencies_for_weapon_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon_effect)

    def _dependencies_for_weapon_effect_multi_player(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon_effect_multi_player)

    def _dependencies_for_sfx_turret_rotation(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx_turret_rotation)

    def _dependencies_for_sfx_single_player_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx_single_player_impact)

    def _dependencies_for_sfx_multi_player_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx_multi_player_impact)

    def _dependencies_for_sfx_single_player_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx_single_player_projectile)

    def _dependencies_for_sfx_multi_player_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx_multi_player_projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_weapon_effect, "weapon_effect", "AssetId"),
            (self._dependencies_for_weapon_effect_multi_player, "weapon_effect_multi_player", "AssetId"),
            (self._dependencies_for_sfx_turret_rotation, "sfx_turret_rotation", "int"),
            (self._dependencies_for_sfx_single_player_impact, "sfx_single_player_impact", "int"),
            (self._dependencies_for_sfx_multi_player_impact, "sfx_multi_player_impact", "int"),
            (self._dependencies_for_sfx_single_player_projectile, "sfx_single_player_projectile", "int"),
            (self._dependencies_for_sfx_multi_player_projectile, "sfx_multi_player_projectile", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PlayerTurret.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_weapon_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xeeadefa6: ('flags', structs.decode_BIG_L),
    0x17cd8b2a: ('max_horiz_rotation_left', structs.decode_BIG_f),
    0x1473dad2: ('max_horiz_rotation_right', structs.decode_BIG_f),
    0x3650ce75: ('max_vert_elevation_up', structs.decode_BIG_f),
    0x78520e6e: ('max_vert_elevation_down', structs.decode_BIG_f),
    0xa39a5d72: ('damage_angle', structs.decode_BIG_f),
    0xfb2e32db: ('horiz_speed', structs.decode_BIG_f),
    0x1b3c8683: ('vert_speed', structs.decode_BIG_f),
    0xc6e48f18: ('fire_rate', structs.decode_BIG_f),
    0x8e5f7e96: ('weapon_damage', _decode_weapon_damage),
    0xc43360a7: ('weapon_effect', structs.decode_BIG_L),
    0xa99d3dbe: ('weapon_effect_multi_player', structs.decode_BIG_L),
    0xe7234f72: ('sfx_turret_rotation', structs.decode_BIG_l),
    0x3e2f7afb: ('sfx_single_player_impact', structs.decode_BIG_l),
    0x7cabd1f1: ('sfx_multi_player_impact', structs.decode_BIG_l),
    0x7ef976eb: ('sfx_single_player_projectile', structs.decode_BIG_l),
    0x035459fd: ('sfx_multi_player_projectile', structs.decode_BIG_l),
}
