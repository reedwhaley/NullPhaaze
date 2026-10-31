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
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.StaticGeometryTest import StaticGeometryTest
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ActorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        mass: float
        gravity: float
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        model: int
        collision_model: int
        character_animation_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        is_loop: bool
        immovable: bool
        is_solid: bool
        is_camera_through: bool
        render_texture_set: int
        draws_shadow: bool
        render_first_sorted: bool
        scale_animation: bool
        highlighted_in_x_ray: bool
        is_phaazite: bool
        phaazite_time_between_effects: float
        use_mod_inca: bool
        mod_inca_color: json_util.JsonValue
        mod_inca_amount: json_util.JsonObject
        random_animation_offset: float
        projectile: int
        projectile_damage: json_util.JsonObject
        projectile_static_geometry_test: json_util.JsonObject
        orbit_offset: json_util.JsonValue
        orbit_offset_local: bool
    

@dataclasses.dataclass()
class Actor(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    collision_box: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xf344c0b0, original_name='CollisionBox', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    collision_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x2e686c2a, original_name='CollisionOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    mass: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x75dbb375, original_name='Mass'
        ),
    })
    gravity: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2f2ae3e5, original_name='Gravity'
        ),
    })
    health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0xcf90d15e, original_name='Health', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x7b71ae90, original_name='Vulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc27ffa8f, original_name='Model'
        ),
    })
    collision_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['DCLN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0fc966dc, original_name='CollisionModel'
        ),
    })
    character_animation_information: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa244c9d8, original_name='CharacterAnimationInformation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    is_loop: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc08d1b93, original_name='IsLoop'
        ),
    })
    immovable: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1e32523e, original_name='Immovable'
        ),
    })
    is_solid: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1d8dd846, original_name='IsSolid'
        ),
    })
    is_camera_through: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7859b520, original_name='IsCameraThrough'
        ),
    })
    render_texture_set: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x32fab97e, original_name='RenderTextureSet'
        ),
    })
    draws_shadow: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x97687446, original_name='DrawsShadow'
        ),
    })
    render_first_sorted: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4743294f, original_name='RenderFirstSorted'
        ),
    })
    scale_animation: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x261e92a4, original_name='ScaleAnimation'
        ),
    })
    highlighted_in_x_ray: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa09d4a1f, original_name='HighlightedInXRay'
        ),
    })
    is_phaazite: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf3de9311, original_name='IsPhaazite'
        ),
    })
    phaazite_time_between_effects: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaa49b627, original_name='PhaaziteTimeBetweenEffects'
        ),
    })
    use_mod_inca: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb530d7de, original_name='UseModInca'
        ),
    })
    mod_inca_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf8df6cd2, original_name='ModIncaColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    mod_inca_amount: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xc23011d9, original_name='ModIncaAmount', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    random_animation_offset: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbf69c03e, original_name='RandomAnimationOffset'
        ),
    })
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x553b1339, original_name='ProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    projectile_static_geometry_test: StaticGeometryTest = dataclasses.field(default_factory=StaticGeometryTest, metadata={
        'reflection': FieldReflection[StaticGeometryTest](
            StaticGeometryTest, id=0x9a892818, original_name='ProjectileStaticGeometryTest', from_json=StaticGeometryTest.from_json, to_json=StaticGeometryTest.to_json
        ),
    })
    orbit_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x850115e4, original_name='OrbitOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    orbit_offset_local: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe73f123d, original_name='OrbitOffsetLocal'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'ACTR'

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
        if property_count != 31:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf344c0b0
        collision_box = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e686c2a
        collision_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75dbb375
        mass = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f2ae3e5
        gravity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf90d15e
        health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b71ae90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc27ffa8f
        model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fc966dc
        collision_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa244c9d8
        character_animation_information = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc08d1b93
        is_loop = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e32523e
        immovable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1d8dd846
        is_solid = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7859b520
        is_camera_through = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32fab97e
        render_texture_set = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97687446
        draws_shadow = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4743294f
        render_first_sorted = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x261e92a4
        scale_animation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa09d4a1f
        highlighted_in_x_ray = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3de9311
        is_phaazite = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa49b627
        phaazite_time_between_effects = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb530d7de
        use_mod_inca = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8df6cd2
        mod_inca_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc23011d9
        mod_inca_amount = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf69c03e
        random_animation_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553b1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a892818
        projectile_static_geometry_test = StaticGeometryTest.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x850115e4
        orbit_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe73f123d
        orbit_offset_local = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(editor_properties, collision_box, collision_offset, mass, gravity, health, vulnerability, model, collision_model, character_animation_information, actor_information, is_loop, immovable, is_solid, is_camera_through, render_texture_set, draws_shadow, render_first_sorted, scale_animation, highlighted_in_x_ray, is_phaazite, phaazite_time_between_effects, use_mod_inca, mod_inca_color, mod_inca_amount, random_animation_offset, projectile, projectile_damage, projectile_static_geometry_test, orbit_offset, orbit_offset_local)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x1f')  # 31 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf3D\xc0\xb0')  # 0xf344c0b0
        data.write(b'\x00\x0c')  # size
        self.collision_box.to_stream(data, game)

        data.write(b'.hl*')  # 0x2e686c2a
        data.write(b'\x00\x0c')  # size
        self.collision_offset.to_stream(data, game)

        data.write(b'u\xdb\xb3u')  # 0x75dbb375
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mass))

        data.write(b'/*\xe3\xe5')  # 0x2f2ae3e5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravity))

        data.write(b'\xcf\x90\xd1^')  # 0xcf90d15e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{q\xae\x90')  # 0x7b71ae90
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc2\x7f\xfa\x8f')  # 0xc27ffa8f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.model))

        data.write(b'\x0f\xc9f\xdc')  # 0xfc966dc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.collision_model))

        data.write(b'\xa2D\xc9\xd8')  # 0xa244c9d8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.character_animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~9\x7f\xed')  # 0x7e397fed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc0\x8d\x1b\x93')  # 0xc08d1b93
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_loop))

        data.write(b'\x1e2R>')  # 0x1e32523e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.immovable))

        data.write(b'\x1d\x8d\xd8F')  # 0x1d8dd846
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_solid))

        data.write(b'xY\xb5 ')  # 0x7859b520
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_camera_through))

        data.write(b'2\xfa\xb9~')  # 0x32fab97e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.render_texture_set))

        data.write(b'\x97htF')  # 0x97687446
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.draws_shadow))

        data.write(b'GC)O')  # 0x4743294f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.render_first_sorted))

        data.write(b'&\x1e\x92\xa4')  # 0x261e92a4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.scale_animation))

        data.write(b'\xa0\x9dJ\x1f')  # 0xa09d4a1f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.highlighted_in_x_ray))

        data.write(b'\xf3\xde\x93\x11')  # 0xf3de9311
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_phaazite))

        data.write(b"\xaaI\xb6'")  # 0xaa49b627
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phaazite_time_between_effects))

        data.write(b'\xb50\xd7\xde')  # 0xb530d7de
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_mod_inca))

        data.write(b'\xf8\xdfl\xd2')  # 0xf8df6cd2
        data.write(b'\x00\x10')  # size
        self.mod_inca_color.to_stream(data, game)

        data.write(b'\xc20\x11\xd9')  # 0xc23011d9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mod_inca_amount.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbfi\xc0>')  # 0xbf69c03e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.random_animation_offset))

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.projectile))

        data.write(b'U;\x139')  # 0x553b1339
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9a\x89(\x18')  # 0x9a892818
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_static_geometry_test.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x85\x01\x15\xe4')  # 0x850115e4
        data.write(b'\x00\x0c')  # size
        self.orbit_offset.to_stream(data, game)

        data.write(b'\xe7?\x12=')  # 0xe73f123d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.orbit_offset_local))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            collision_box=Vector.from_json(json_data['collision_box']),
            collision_offset=Vector.from_json(json_data['collision_offset']),
            mass=json_data['mass'],
            gravity=json_data['gravity'],
            health=HealthInfo.from_json(json_data['health']),
            vulnerability=DamageVulnerability.from_json(json_data['vulnerability']),
            model=json_data['model'],
            collision_model=json_data['collision_model'],
            character_animation_information=AnimationParameters.from_json(json_data['character_animation_information']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            is_loop=json_data['is_loop'],
            immovable=json_data['immovable'],
            is_solid=json_data['is_solid'],
            is_camera_through=json_data['is_camera_through'],
            render_texture_set=json_data['render_texture_set'],
            draws_shadow=json_data['draws_shadow'],
            render_first_sorted=json_data['render_first_sorted'],
            scale_animation=json_data['scale_animation'],
            highlighted_in_x_ray=json_data['highlighted_in_x_ray'],
            is_phaazite=json_data['is_phaazite'],
            phaazite_time_between_effects=json_data['phaazite_time_between_effects'],
            use_mod_inca=json_data['use_mod_inca'],
            mod_inca_color=Color.from_json(json_data['mod_inca_color']),
            mod_inca_amount=Spline.from_json(json_data['mod_inca_amount']),
            random_animation_offset=json_data['random_animation_offset'],
            projectile=json_data['projectile'],
            projectile_damage=DamageInfo.from_json(json_data['projectile_damage']),
            projectile_static_geometry_test=StaticGeometryTest.from_json(json_data['projectile_static_geometry_test']),
            orbit_offset=Vector.from_json(json_data['orbit_offset']),
            orbit_offset_local=json_data['orbit_offset_local'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'collision_box': self.collision_box.to_json(),
            'collision_offset': self.collision_offset.to_json(),
            'mass': self.mass,
            'gravity': self.gravity,
            'health': self.health.to_json(),
            'vulnerability': self.vulnerability.to_json(),
            'model': self.model,
            'collision_model': self.collision_model,
            'character_animation_information': self.character_animation_information.to_json(),
            'actor_information': self.actor_information.to_json(),
            'is_loop': self.is_loop,
            'immovable': self.immovable,
            'is_solid': self.is_solid,
            'is_camera_through': self.is_camera_through,
            'render_texture_set': self.render_texture_set,
            'draws_shadow': self.draws_shadow,
            'render_first_sorted': self.render_first_sorted,
            'scale_animation': self.scale_animation,
            'highlighted_in_x_ray': self.highlighted_in_x_ray,
            'is_phaazite': self.is_phaazite,
            'phaazite_time_between_effects': self.phaazite_time_between_effects,
            'use_mod_inca': self.use_mod_inca,
            'mod_inca_color': self.mod_inca_color.to_json(),
            'mod_inca_amount': self.mod_inca_amount.to_json(),
            'random_animation_offset': self.random_animation_offset,
            'projectile': self.projectile,
            'projectile_damage': self.projectile_damage.to_json(),
            'projectile_static_geometry_test': self.projectile_static_geometry_test.to_json(),
            'orbit_offset': self.orbit_offset.to_json(),
            'orbit_offset_local': self.orbit_offset_local,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_collision_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.collision_model)

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self._dependencies_for_collision_model, "collision_model", "AssetId"),
            (self.character_animation_information.dependencies_for, "character_animation_information", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Actor.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_character_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_mod_inca_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_mod_inca_amount(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_projectile_static_geometry_test(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


def _decode_orbit_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xf344c0b0: ('collision_box', _decode_collision_box),
    0x2e686c2a: ('collision_offset', _decode_collision_offset),
    0x75dbb375: ('mass', structs.decode_BIG_f),
    0x2f2ae3e5: ('gravity', structs.decode_BIG_f),
    0xcf90d15e: ('health', _decode_health),
    0x7b71ae90: ('vulnerability', _decode_vulnerability),
    0xc27ffa8f: ('model', structs.decode_BIG_Q),
    0x0fc966dc: ('collision_model', structs.decode_BIG_Q),
    0xa244c9d8: ('character_animation_information', _decode_character_animation_information),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xc08d1b93: ('is_loop', structs.decode_BIG_bool_),
    0x1e32523e: ('immovable', structs.decode_BIG_bool_),
    0x1d8dd846: ('is_solid', structs.decode_BIG_bool_),
    0x7859b520: ('is_camera_through', structs.decode_BIG_bool_),
    0x32fab97e: ('render_texture_set', structs.decode_BIG_l),
    0x97687446: ('draws_shadow', structs.decode_BIG_bool_),
    0x4743294f: ('render_first_sorted', structs.decode_BIG_bool_),
    0x261e92a4: ('scale_animation', structs.decode_BIG_bool_),
    0xa09d4a1f: ('highlighted_in_x_ray', structs.decode_BIG_bool_),
    0xf3de9311: ('is_phaazite', structs.decode_BIG_bool_),
    0xaa49b627: ('phaazite_time_between_effects', structs.decode_BIG_f),
    0xb530d7de: ('use_mod_inca', structs.decode_BIG_bool_),
    0xf8df6cd2: ('mod_inca_color', _decode_mod_inca_color),
    0xc23011d9: ('mod_inca_amount', _decode_mod_inca_amount),
    0xbf69c03e: ('random_animation_offset', structs.decode_BIG_f),
    0xef485db9: ('projectile', structs.decode_BIG_Q),
    0x553b1339: ('projectile_damage', _decode_projectile_damage),
    0x9a892818: ('projectile_static_geometry_test', _decode_projectile_static_geometry_test),
    0x850115e4: ('orbit_offset', _decode_orbit_offset),
    0xe73f123d: ('orbit_offset_local', structs.decode_BIG_bool_),
}
