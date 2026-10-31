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
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.PlayerActorOverlay import PlayerActorOverlay
from retro_data_structures.properties.corruption.archetypes.ShadowProjection import ShadowProjection
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PlayerActorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        mass: float
        gravity: float
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        no_model: int
        animation: json_util.JsonObject
        actor_information: json_util.JsonObject
        is_loop: bool
        immovable: bool
        is_solid: bool
        empty_suit_model: int
        empty_suit_skin_rule: int
        varia_suit_model: int
        varia_suit_skin_rule: int
        varia_suit_grapple_model: int
        varia_suit_grapple_skin_rule: int
        stage01_suit_model: int
        stage01_skin_rule: int
        stage02_suit_model: int
        stage02_skin_rule: int
        stage03_suit_model: int
        stage03_skin_rule: int
        stage03_acid_model: int
        stage03_acid_rule: int
        stage04_suit_model: int
        stage04_skin_rule: int
        overlay_model_info: json_util.JsonObject
        hyper_mode_overlay: json_util.JsonObject
        flags: int
        render_gun_override: int
        shadow_projection: json_util.JsonObject
    

@dataclasses.dataclass()
class PlayerActor(BaseObjectType):
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
    no_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x405e5286, original_name='NoModel'
        ),
    })
    animation: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa3d63f44, original_name='Animation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
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
    empty_suit_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x846397a8, original_name='EmptySuitModel'
        ),
    })
    empty_suit_skin_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x685a4c01, original_name='EmptySuitSkinRule'
        ),
    })
    varia_suit_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9834ecc9, original_name='VariaSuitModel'
        ),
    })
    varia_suit_skin_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x188b8960, original_name='VariaSuitSkinRule'
        ),
    })
    varia_suit_grapple_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x134a81e3, original_name='VariaSuitGrappleModel'
        ),
    })
    varia_suit_grapple_skin_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4abf030c, original_name='VariaSuitGrappleSkinRule'
        ),
    })
    stage01_suit_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9bf030dc, original_name='Stage01SuitModel'
        ),
    })
    stage01_skin_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x981263d3, original_name='Stage01SkinRule'
        ),
    })
    stage02_suit_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8a8d5aa5, original_name='Stage02SuitModel'
        ),
    })
    stage02_skin_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe4734608, original_name='Stage02SkinRule'
        ),
    })
    stage03_suit_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3376814d, original_name='Stage03SuitModel'
        ),
    })
    stage03_skin_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x797ca77e, original_name='Stage03SkinRule'
        ),
    })
    stage03_acid_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0ebec440, original_name='Stage03AcidModel'
        ),
    })
    stage03_acid_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbc0952d8, original_name='Stage03AcidRule'
        ),
    })
    stage04_suit_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa8778e57, original_name='Stage04SuitModel'
        ),
    })
    stage04_skin_rule: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1cb10dbe, original_name='Stage04SkinRule'
        ),
    })
    overlay_model_info: PlayerActorOverlay = dataclasses.field(default_factory=PlayerActorOverlay, metadata={
        'reflection': FieldReflection[PlayerActorOverlay](
            PlayerActorOverlay, id=0x1098d091, original_name='OverlayModelInfo', from_json=PlayerActorOverlay.from_json, to_json=PlayerActorOverlay.to_json
        ),
    })
    hyper_mode_overlay: PlayerActorOverlay = dataclasses.field(default_factory=PlayerActorOverlay, metadata={
        'reflection': FieldReflection[PlayerActorOverlay](
            PlayerActorOverlay, id=0xc7385390, original_name='HyperModeOverlay', from_json=PlayerActorOverlay.from_json, to_json=PlayerActorOverlay.to_json
        ),
    })
    flags: int = dataclasses.field(default=16388, metadata={
        'reflection': FieldReflection[int](
            int, id=0x33507998, original_name='Flags'
        ),
    })  # Flagset
    render_gun_override: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb6832840, original_name='RenderGunOverride'
        ),
    })  # Choice
    shadow_projection: ShadowProjection = dataclasses.field(default_factory=ShadowProjection, metadata={
        'reflection': FieldReflection[ShadowProjection](
            ShadowProjection, id=0xa21b515a, original_name='ShadowProjection', from_json=ShadowProjection.from_json, to_json=ShadowProjection.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'PLAC'

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
        if property_count != 34:
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
        assert property_id == 0x405e5286
        no_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3d63f44
        animation = AnimationParameters.from_stream(data, game, property_size)
    
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
        assert property_id == 0x846397a8
        empty_suit_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x685a4c01
        empty_suit_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9834ecc9
        varia_suit_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x188b8960
        varia_suit_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x134a81e3
        varia_suit_grapple_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4abf030c
        varia_suit_grapple_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9bf030dc
        stage01_suit_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x981263d3
        stage01_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8a8d5aa5
        stage02_suit_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe4734608
        stage02_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3376814d
        stage03_suit_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x797ca77e
        stage03_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ebec440
        stage03_acid_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc0952d8
        stage03_acid_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8778e57
        stage04_suit_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1cb10dbe
        stage04_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1098d091
        overlay_model_info = PlayerActorOverlay.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7385390
        hyper_mode_overlay = PlayerActorOverlay.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33507998
        flags = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6832840
        render_gun_override = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa21b515a
        shadow_projection = ShadowProjection.from_stream(data, game, property_size)
    
        return cls(editor_properties, collision_box, collision_offset, mass, gravity, health, vulnerability, no_model, animation, actor_information, is_loop, immovable, is_solid, empty_suit_model, empty_suit_skin_rule, varia_suit_model, varia_suit_skin_rule, varia_suit_grapple_model, varia_suit_grapple_skin_rule, stage01_suit_model, stage01_skin_rule, stage02_suit_model, stage02_skin_rule, stage03_suit_model, stage03_skin_rule, stage03_acid_model, stage03_acid_rule, stage04_suit_model, stage04_skin_rule, overlay_model_info, hyper_mode_overlay, flags, render_gun_override, shadow_projection)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00"')  # 34 properties

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

        data.write(b'@^R\x86')  # 0x405e5286
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.no_model))

        data.write(b'\xa3\xd6?D')  # 0xa3d63f44
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.animation.to_stream(data, game)
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

        data.write(b'\x84c\x97\xa8')  # 0x846397a8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.empty_suit_model))

        data.write(b'hZL\x01')  # 0x685a4c01
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.empty_suit_skin_rule))

        data.write(b'\x984\xec\xc9')  # 0x9834ecc9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_model))

        data.write(b'\x18\x8b\x89`')  # 0x188b8960
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_skin_rule))

        data.write(b'\x13J\x81\xe3')  # 0x134a81e3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_grapple_model))

        data.write(b'J\xbf\x03\x0c')  # 0x4abf030c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_grapple_skin_rule))

        data.write(b'\x9b\xf00\xdc')  # 0x9bf030dc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage01_suit_model))

        data.write(b'\x98\x12c\xd3')  # 0x981263d3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage01_skin_rule))

        data.write(b'\x8a\x8dZ\xa5')  # 0x8a8d5aa5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage02_suit_model))

        data.write(b'\xe4sF\x08')  # 0xe4734608
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage02_skin_rule))

        data.write(b'3v\x81M')  # 0x3376814d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage03_suit_model))

        data.write(b'y|\xa7~')  # 0x797ca77e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage03_skin_rule))

        data.write(b'\x0e\xbe\xc4@')  # 0xebec440
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage03_acid_model))

        data.write(b'\xbc\tR\xd8')  # 0xbc0952d8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage03_acid_rule))

        data.write(b'\xa8w\x8eW')  # 0xa8778e57
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage04_suit_model))

        data.write(b'\x1c\xb1\r\xbe')  # 0x1cb10dbe
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stage04_skin_rule))

        data.write(b'\x10\x98\xd0\x91')  # 0x1098d091
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.overlay_model_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc78S\x90')  # 0xc7385390
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_overlay.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3Py\x98')  # 0x33507998
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.flags))

        data.write(b'\xb6\x83(@')  # 0xb6832840
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.render_gun_override))

        data.write(b'\xa2\x1bQZ')  # 0xa21b515a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shadow_projection.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerActorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            collision_box=Vector.from_json(json_data['collision_box']),
            collision_offset=Vector.from_json(json_data['collision_offset']),
            mass=json_data['mass'],
            gravity=json_data['gravity'],
            health=HealthInfo.from_json(json_data['health']),
            vulnerability=DamageVulnerability.from_json(json_data['vulnerability']),
            no_model=json_data['no_model'],
            animation=AnimationParameters.from_json(json_data['animation']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            is_loop=json_data['is_loop'],
            immovable=json_data['immovable'],
            is_solid=json_data['is_solid'],
            empty_suit_model=json_data['empty_suit_model'],
            empty_suit_skin_rule=json_data['empty_suit_skin_rule'],
            varia_suit_model=json_data['varia_suit_model'],
            varia_suit_skin_rule=json_data['varia_suit_skin_rule'],
            varia_suit_grapple_model=json_data['varia_suit_grapple_model'],
            varia_suit_grapple_skin_rule=json_data['varia_suit_grapple_skin_rule'],
            stage01_suit_model=json_data['stage01_suit_model'],
            stage01_skin_rule=json_data['stage01_skin_rule'],
            stage02_suit_model=json_data['stage02_suit_model'],
            stage02_skin_rule=json_data['stage02_skin_rule'],
            stage03_suit_model=json_data['stage03_suit_model'],
            stage03_skin_rule=json_data['stage03_skin_rule'],
            stage03_acid_model=json_data['stage03_acid_model'],
            stage03_acid_rule=json_data['stage03_acid_rule'],
            stage04_suit_model=json_data['stage04_suit_model'],
            stage04_skin_rule=json_data['stage04_skin_rule'],
            overlay_model_info=PlayerActorOverlay.from_json(json_data['overlay_model_info']),
            hyper_mode_overlay=PlayerActorOverlay.from_json(json_data['hyper_mode_overlay']),
            flags=json_data['flags'],
            render_gun_override=json_data['render_gun_override'],
            shadow_projection=ShadowProjection.from_json(json_data['shadow_projection']),
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
            'no_model': self.no_model,
            'animation': self.animation.to_json(),
            'actor_information': self.actor_information.to_json(),
            'is_loop': self.is_loop,
            'immovable': self.immovable,
            'is_solid': self.is_solid,
            'empty_suit_model': self.empty_suit_model,
            'empty_suit_skin_rule': self.empty_suit_skin_rule,
            'varia_suit_model': self.varia_suit_model,
            'varia_suit_skin_rule': self.varia_suit_skin_rule,
            'varia_suit_grapple_model': self.varia_suit_grapple_model,
            'varia_suit_grapple_skin_rule': self.varia_suit_grapple_skin_rule,
            'stage01_suit_model': self.stage01_suit_model,
            'stage01_skin_rule': self.stage01_skin_rule,
            'stage02_suit_model': self.stage02_suit_model,
            'stage02_skin_rule': self.stage02_skin_rule,
            'stage03_suit_model': self.stage03_suit_model,
            'stage03_skin_rule': self.stage03_skin_rule,
            'stage03_acid_model': self.stage03_acid_model,
            'stage03_acid_rule': self.stage03_acid_rule,
            'stage04_suit_model': self.stage04_suit_model,
            'stage04_skin_rule': self.stage04_skin_rule,
            'overlay_model_info': self.overlay_model_info.to_json(),
            'hyper_mode_overlay': self.hyper_mode_overlay.to_json(),
            'flags': self.flags,
            'render_gun_override': self.render_gun_override,
            'shadow_projection': self.shadow_projection.to_json(),
        }

    def _dependencies_for_no_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.no_model)

    def _dependencies_for_empty_suit_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.empty_suit_model)

    def _dependencies_for_empty_suit_skin_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.empty_suit_skin_rule)

    def _dependencies_for_varia_suit_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.varia_suit_model)

    def _dependencies_for_varia_suit_skin_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.varia_suit_skin_rule)

    def _dependencies_for_varia_suit_grapple_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.varia_suit_grapple_model)

    def _dependencies_for_varia_suit_grapple_skin_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.varia_suit_grapple_skin_rule)

    def _dependencies_for_stage01_suit_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage01_suit_model)

    def _dependencies_for_stage01_skin_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage01_skin_rule)

    def _dependencies_for_stage02_suit_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage02_suit_model)

    def _dependencies_for_stage02_skin_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage02_skin_rule)

    def _dependencies_for_stage03_suit_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage03_suit_model)

    def _dependencies_for_stage03_skin_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage03_skin_rule)

    def _dependencies_for_stage03_acid_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage03_acid_model)

    def _dependencies_for_stage03_acid_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage03_acid_rule)

    def _dependencies_for_stage04_suit_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage04_suit_model)

    def _dependencies_for_stage04_skin_rule(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stage04_skin_rule)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_no_model, "no_model", "AssetId"),
            (self.animation.dependencies_for, "animation", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_empty_suit_model, "empty_suit_model", "AssetId"),
            (self._dependencies_for_empty_suit_skin_rule, "empty_suit_skin_rule", "AssetId"),
            (self._dependencies_for_varia_suit_model, "varia_suit_model", "AssetId"),
            (self._dependencies_for_varia_suit_skin_rule, "varia_suit_skin_rule", "AssetId"),
            (self._dependencies_for_varia_suit_grapple_model, "varia_suit_grapple_model", "AssetId"),
            (self._dependencies_for_varia_suit_grapple_skin_rule, "varia_suit_grapple_skin_rule", "AssetId"),
            (self._dependencies_for_stage01_suit_model, "stage01_suit_model", "AssetId"),
            (self._dependencies_for_stage01_skin_rule, "stage01_skin_rule", "AssetId"),
            (self._dependencies_for_stage02_suit_model, "stage02_suit_model", "AssetId"),
            (self._dependencies_for_stage02_skin_rule, "stage02_skin_rule", "AssetId"),
            (self._dependencies_for_stage03_suit_model, "stage03_suit_model", "AssetId"),
            (self._dependencies_for_stage03_skin_rule, "stage03_skin_rule", "AssetId"),
            (self._dependencies_for_stage03_acid_model, "stage03_acid_model", "AssetId"),
            (self._dependencies_for_stage03_acid_rule, "stage03_acid_rule", "AssetId"),
            (self._dependencies_for_stage04_suit_model, "stage04_suit_model", "AssetId"),
            (self._dependencies_for_stage04_skin_rule, "stage04_skin_rule", "AssetId"),
            (self.overlay_model_info.dependencies_for, "overlay_model_info", "PlayerActorOverlay"),
            (self.hyper_mode_overlay.dependencies_for, "hyper_mode_overlay", "PlayerActorOverlay"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PlayerActor.{field_name} ({field_type}): {e}"
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


def _decode_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_overlay_model_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerActorOverlay:
    return PlayerActorOverlay.from_stream(data, game, property_size)


def _decode_hyper_mode_overlay(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerActorOverlay:
    return PlayerActorOverlay.from_stream(data, game, property_size)


def _decode_shadow_projection(data: typing.BinaryIO, game: Game, property_size: int) -> ShadowProjection:
    return ShadowProjection.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xf344c0b0: ('collision_box', _decode_collision_box),
    0x2e686c2a: ('collision_offset', _decode_collision_offset),
    0x75dbb375: ('mass', structs.decode_BIG_f),
    0x2f2ae3e5: ('gravity', structs.decode_BIG_f),
    0xcf90d15e: ('health', _decode_health),
    0x7b71ae90: ('vulnerability', _decode_vulnerability),
    0x405e5286: ('no_model', structs.decode_BIG_Q),
    0xa3d63f44: ('animation', _decode_animation),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xc08d1b93: ('is_loop', structs.decode_BIG_bool_),
    0x1e32523e: ('immovable', structs.decode_BIG_bool_),
    0x1d8dd846: ('is_solid', structs.decode_BIG_bool_),
    0x846397a8: ('empty_suit_model', structs.decode_BIG_Q),
    0x685a4c01: ('empty_suit_skin_rule', structs.decode_BIG_Q),
    0x9834ecc9: ('varia_suit_model', structs.decode_BIG_Q),
    0x188b8960: ('varia_suit_skin_rule', structs.decode_BIG_Q),
    0x134a81e3: ('varia_suit_grapple_model', structs.decode_BIG_Q),
    0x4abf030c: ('varia_suit_grapple_skin_rule', structs.decode_BIG_Q),
    0x9bf030dc: ('stage01_suit_model', structs.decode_BIG_Q),
    0x981263d3: ('stage01_skin_rule', structs.decode_BIG_Q),
    0x8a8d5aa5: ('stage02_suit_model', structs.decode_BIG_Q),
    0xe4734608: ('stage02_skin_rule', structs.decode_BIG_Q),
    0x3376814d: ('stage03_suit_model', structs.decode_BIG_Q),
    0x797ca77e: ('stage03_skin_rule', structs.decode_BIG_Q),
    0x0ebec440: ('stage03_acid_model', structs.decode_BIG_Q),
    0xbc0952d8: ('stage03_acid_rule', structs.decode_BIG_Q),
    0xa8778e57: ('stage04_suit_model', structs.decode_BIG_Q),
    0x1cb10dbe: ('stage04_skin_rule', structs.decode_BIG_Q),
    0x1098d091: ('overlay_model_info', _decode_overlay_model_info),
    0xc7385390: ('hyper_mode_overlay', _decode_hyper_mode_overlay),
    0x33507998: ('flags', structs.decode_BIG_L),
    0xb6832840: ('render_gun_override', structs.decode_BIG_L),
    0xa21b515a: ('shadow_projection', _decode_shadow_projection),
}
