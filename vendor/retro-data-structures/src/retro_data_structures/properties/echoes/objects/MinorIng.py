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
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.MinorIngIngSpot import MinorIngIngSpot
from retro_data_structures.properties.echoes.archetypes.MinorIngInglet import MinorIngInglet
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MinorIngJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        projectile_damage: json_util.JsonObject
        projectile: int
        unknown_0xa03e450c: float
        attack_angle_limit: float
        line_of_sight_height_offset: float
        unknown_0xd6c8eac2: float
        unknown_0x2a5449ba: float
        hearing_radius: float
        allow_projectile_during_attack_pattern: bool
        unknown_0xbce16644: bool
        unknown_0x142433d3: bool
        stay_on_point_path_finding: bool
        allow_projectile_during_stay_on_point_path_finding: bool
        unknown_0x09207f51: bool
        allow_puddle_lock_on: bool
        ing_spot: json_util.JsonObject
        inglet: json_util.JsonObject
    

@dataclasses.dataclass()
class MinorIng(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0xb3774750, original_name='Patterned', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x553b1339, original_name='ProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    unknown_0xa03e450c: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa03e450c, original_name='Unknown'
        ),
    })
    attack_angle_limit: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7b9a0bb4, original_name='AttackAngleLimit'
        ),
    })
    line_of_sight_height_offset: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x99bb2559, original_name='LineOfSightHeightOffset'
        ),
    })
    unknown_0xd6c8eac2: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd6c8eac2, original_name='Unknown'
        ),
    })
    unknown_0x2a5449ba: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a5449ba, original_name='Unknown'
        ),
    })
    hearing_radius: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed69488f, original_name='HearingRadius'
        ),
    })
    allow_projectile_during_attack_pattern: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x399d1eaa, original_name='AllowProjectileDuringAttackPattern'
        ),
    })
    unknown_0xbce16644: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbce16644, original_name='Unknown'
        ),
    })
    unknown_0x142433d3: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x142433d3, original_name='Unknown'
        ),
    })
    stay_on_point_path_finding: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb6cc0063, original_name='StayOnPointPathFinding'
        ),
    })
    allow_projectile_during_stay_on_point_path_finding: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe601f7bd, original_name='AllowProjectileDuringStayOnPointPathFinding'
        ),
    })
    unknown_0x09207f51: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x09207f51, original_name='Unknown'
        ),
    })
    allow_puddle_lock_on: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2107e4fb, original_name='AllowPuddleLockOn'
        ),
    })
    ing_spot: MinorIngIngSpot = dataclasses.field(default_factory=MinorIngIngSpot, metadata={
        'reflection': FieldReflection[MinorIngIngSpot](
            MinorIngIngSpot, id=0x07e9d446, original_name='IngSpot', from_json=MinorIngIngSpot.from_json, to_json=MinorIngIngSpot.to_json
        ),
    })
    inglet: MinorIngInglet = dataclasses.field(default_factory=MinorIngInglet, metadata={
        'reflection': FieldReflection[MinorIngInglet](
            MinorIngInglet, id=0x3da35851, original_name='Inglet', from_json=MinorIngInglet.from_json, to_json=MinorIngInglet.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'MNNG'

    @classmethod
    def modules(cls) -> list[str]:
        return ['GeomBlobV2.rel', 'MinorIng.rel']

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
        if property_count != 20:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'min_attack_range': 4.5, 'max_attack_range': 30.0, 'average_attack_time': 3.0, 'collision_height': 4.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553b1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0, 'di_knock_back_power': 3.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa03e450c
        unknown_0xa03e450c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b9a0bb4
        attack_angle_limit = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x99bb2559
        line_of_sight_height_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6c8eac2
        unknown_0xd6c8eac2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a5449ba
        unknown_0x2a5449ba = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed69488f
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x399d1eaa
        allow_projectile_during_attack_pattern = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbce16644
        unknown_0xbce16644 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x142433d3
        unknown_0x142433d3 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6cc0063
        stay_on_point_path_finding = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe601f7bd
        allow_projectile_during_stay_on_point_path_finding = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09207f51
        unknown_0x09207f51 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2107e4fb
        allow_puddle_lock_on = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07e9d446
        ing_spot = MinorIngIngSpot.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3da35851
        inglet = MinorIngInglet.from_stream(data, game, property_size)
    
        return cls(editor_properties, patterned, actor_information, projectile_damage, projectile, unknown_0xa03e450c, attack_angle_limit, line_of_sight_height_offset, unknown_0xd6c8eac2, unknown_0x2a5449ba, hearing_radius, allow_projectile_during_attack_pattern, unknown_0xbce16644, unknown_0x142433d3, stay_on_point_path_finding, allow_projectile_during_stay_on_point_path_finding, unknown_0x09207f51, allow_puddle_lock_on, ing_spot, inglet)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x14')  # 20 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'min_attack_range': 4.5, 'max_attack_range': 30.0, 'average_attack_time': 3.0, 'collision_height': 4.0})
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

        data.write(b'U;\x139')  # 0x553b1339
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0, 'di_knock_back_power': 3.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b'\xa0>E\x0c')  # 0xa03e450c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa03e450c))

        data.write(b'{\x9a\x0b\xb4')  # 0x7b9a0bb4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_angle_limit))

        data.write(b'\x99\xbb%Y')  # 0x99bb2559
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.line_of_sight_height_offset))

        data.write(b'\xd6\xc8\xea\xc2')  # 0xd6c8eac2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd6c8eac2))

        data.write(b'*TI\xba')  # 0x2a5449ba
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2a5449ba))

        data.write(b'\xediH\x8f')  # 0xed69488f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b'9\x9d\x1e\xaa')  # 0x399d1eaa
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.allow_projectile_during_attack_pattern))

        data.write(b'\xbc\xe1fD')  # 0xbce16644
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbce16644))

        data.write(b'\x14$3\xd3')  # 0x142433d3
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x142433d3))

        data.write(b'\xb6\xcc\x00c')  # 0xb6cc0063
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.stay_on_point_path_finding))

        data.write(b'\xe6\x01\xf7\xbd')  # 0xe601f7bd
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.allow_projectile_during_stay_on_point_path_finding))

        data.write(b'\t \x7fQ')  # 0x9207f51
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x09207f51))

        data.write(b'!\x07\xe4\xfb')  # 0x2107e4fb
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.allow_puddle_lock_on))

        data.write(b'\x07\xe9\xd4F')  # 0x7e9d446
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_spot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'=\xa3XQ')  # 0x3da35851
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.inglet.to_stream(data, game)
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
        json_data = typing.cast("MinorIngJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            projectile_damage=DamageInfo.from_json(json_data['projectile_damage']),
            projectile=json_data['projectile'],
            unknown_0xa03e450c=json_data['unknown_0xa03e450c'],
            attack_angle_limit=json_data['attack_angle_limit'],
            line_of_sight_height_offset=json_data['line_of_sight_height_offset'],
            unknown_0xd6c8eac2=json_data['unknown_0xd6c8eac2'],
            unknown_0x2a5449ba=json_data['unknown_0x2a5449ba'],
            hearing_radius=json_data['hearing_radius'],
            allow_projectile_during_attack_pattern=json_data['allow_projectile_during_attack_pattern'],
            unknown_0xbce16644=json_data['unknown_0xbce16644'],
            unknown_0x142433d3=json_data['unknown_0x142433d3'],
            stay_on_point_path_finding=json_data['stay_on_point_path_finding'],
            allow_projectile_during_stay_on_point_path_finding=json_data['allow_projectile_during_stay_on_point_path_finding'],
            unknown_0x09207f51=json_data['unknown_0x09207f51'],
            allow_puddle_lock_on=json_data['allow_puddle_lock_on'],
            ing_spot=MinorIngIngSpot.from_json(json_data['ing_spot']),
            inglet=MinorIngInglet.from_json(json_data['inglet']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'projectile_damage': self.projectile_damage.to_json(),
            'projectile': self.projectile,
            'unknown_0xa03e450c': self.unknown_0xa03e450c,
            'attack_angle_limit': self.attack_angle_limit,
            'line_of_sight_height_offset': self.line_of_sight_height_offset,
            'unknown_0xd6c8eac2': self.unknown_0xd6c8eac2,
            'unknown_0x2a5449ba': self.unknown_0x2a5449ba,
            'hearing_radius': self.hearing_radius,
            'allow_projectile_during_attack_pattern': self.allow_projectile_during_attack_pattern,
            'unknown_0xbce16644': self.unknown_0xbce16644,
            'unknown_0x142433d3': self.unknown_0x142433d3,
            'stay_on_point_path_finding': self.stay_on_point_path_finding,
            'allow_projectile_during_stay_on_point_path_finding': self.allow_projectile_during_stay_on_point_path_finding,
            'unknown_0x09207f51': self.unknown_0x09207f51,
            'allow_puddle_lock_on': self.allow_puddle_lock_on,
            'ing_spot': self.ing_spot.to_json(),
            'inglet': self.inglet.to_json(),
        }

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self.ing_spot.dependencies_for, "ing_spot", "MinorIngIngSpot"),
            (self.inglet.dependencies_for, "inglet", "MinorIngInglet"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MinorIng.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'min_attack_range': 4.5, 'max_attack_range': 30.0, 'average_attack_time': 3.0, 'collision_height': 4.0})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0, 'di_knock_back_power': 3.0})


def _decode_ing_spot(data: typing.BinaryIO, game: Game, property_size: int) -> MinorIngIngSpot:
    return MinorIngIngSpot.from_stream(data, game, property_size)


def _decode_inglet(data: typing.BinaryIO, game: Game, property_size: int) -> MinorIngInglet:
    return MinorIngInglet.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x553b1339: ('projectile_damage', _decode_projectile_damage),
    0xef485db9: ('projectile', structs.decode_BIG_L),
    0xa03e450c: ('unknown_0xa03e450c', structs.decode_BIG_f),
    0x7b9a0bb4: ('attack_angle_limit', structs.decode_BIG_f),
    0x99bb2559: ('line_of_sight_height_offset', structs.decode_BIG_f),
    0xd6c8eac2: ('unknown_0xd6c8eac2', structs.decode_BIG_f),
    0x2a5449ba: ('unknown_0x2a5449ba', structs.decode_BIG_f),
    0xed69488f: ('hearing_radius', structs.decode_BIG_f),
    0x399d1eaa: ('allow_projectile_during_attack_pattern', structs.decode_BIG_bool_),
    0xbce16644: ('unknown_0xbce16644', structs.decode_BIG_bool_),
    0x142433d3: ('unknown_0x142433d3', structs.decode_BIG_bool_),
    0xb6cc0063: ('stay_on_point_path_finding', structs.decode_BIG_bool_),
    0xe601f7bd: ('allow_projectile_during_stay_on_point_path_finding', structs.decode_BIG_bool_),
    0x09207f51: ('unknown_0x09207f51', structs.decode_BIG_bool_),
    0x2107e4fb: ('allow_puddle_lock_on', structs.decode_BIG_bool_),
    0x07e9d446: ('ing_spot', _decode_ing_spot),
    0x3da35851: ('inglet', _decode_inglet),
}
