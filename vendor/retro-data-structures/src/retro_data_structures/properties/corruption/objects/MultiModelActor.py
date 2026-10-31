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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.MultiModelInformation import MultiModelInformation
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MultiModelActorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        collision_model: int
        model: int
        multi_model_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        highlighted_in_x_ray: bool
        use_mod_inca: bool
        mod_inca_color: json_util.JsonValue
        mod_inca_amount: json_util.JsonObject
        orbit_offset: json_util.JsonValue
        orbit_offset_local: bool
        is_solid: bool
        immovable: bool
    

@dataclasses.dataclass()
class MultiModelActor(BaseObjectType):
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
    collision_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['DCLN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0fc966dc, original_name='CollisionModel'
        ),
    })
    model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc27ffa8f, original_name='Model'
        ),
    })
    multi_model_information: MultiModelInformation = dataclasses.field(default_factory=MultiModelInformation, metadata={
        'reflection': FieldReflection[MultiModelInformation](
            MultiModelInformation, id=0x1960932d, original_name='MultiModelInformation', from_json=MultiModelInformation.from_json, to_json=MultiModelInformation.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    highlighted_in_x_ray: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa09d4a1f, original_name='HighlightedInXRay'
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
    is_solid: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1d8dd846, original_name='IsSolid'
        ),
    })
    immovable: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1e32523e, original_name='Immovable'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'MMDL'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_ScriptMultiModelActor.rso']

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
        if property_count != 15:
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
        assert property_id == 0x0fc966dc
        collision_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc27ffa8f
        model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1960932d
        multi_model_information = MultiModelInformation.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa09d4a1f
        highlighted_in_x_ray = structs.BIG_bool_.unpack(data.read(1))[0]
    
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
        assert property_id == 0x850115e4
        orbit_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe73f123d
        orbit_offset_local = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1d8dd846
        is_solid = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e32523e
        immovable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(editor_properties, collision_box, collision_offset, collision_model, model, multi_model_information, actor_information, highlighted_in_x_ray, use_mod_inca, mod_inca_color, mod_inca_amount, orbit_offset, orbit_offset_local, is_solid, immovable)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x0f')  # 15 properties

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

        data.write(b'\x0f\xc9f\xdc')  # 0xfc966dc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.collision_model))

        data.write(b'\xc2\x7f\xfa\x8f')  # 0xc27ffa8f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.model))

        data.write(b'\x19`\x93-')  # 0x1960932d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.multi_model_information.to_stream(data, game)
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

        data.write(b'\xa0\x9dJ\x1f')  # 0xa09d4a1f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.highlighted_in_x_ray))

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

        data.write(b'\x85\x01\x15\xe4')  # 0x850115e4
        data.write(b'\x00\x0c')  # size
        self.orbit_offset.to_stream(data, game)

        data.write(b'\xe7?\x12=')  # 0xe73f123d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.orbit_offset_local))

        data.write(b'\x1d\x8d\xd8F')  # 0x1d8dd846
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_solid))

        data.write(b'\x1e2R>')  # 0x1e32523e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.immovable))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MultiModelActorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            collision_box=Vector.from_json(json_data['collision_box']),
            collision_offset=Vector.from_json(json_data['collision_offset']),
            collision_model=json_data['collision_model'],
            model=json_data['model'],
            multi_model_information=MultiModelInformation.from_json(json_data['multi_model_information']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            highlighted_in_x_ray=json_data['highlighted_in_x_ray'],
            use_mod_inca=json_data['use_mod_inca'],
            mod_inca_color=Color.from_json(json_data['mod_inca_color']),
            mod_inca_amount=Spline.from_json(json_data['mod_inca_amount']),
            orbit_offset=Vector.from_json(json_data['orbit_offset']),
            orbit_offset_local=json_data['orbit_offset_local'],
            is_solid=json_data['is_solid'],
            immovable=json_data['immovable'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'collision_box': self.collision_box.to_json(),
            'collision_offset': self.collision_offset.to_json(),
            'collision_model': self.collision_model,
            'model': self.model,
            'multi_model_information': self.multi_model_information.to_json(),
            'actor_information': self.actor_information.to_json(),
            'highlighted_in_x_ray': self.highlighted_in_x_ray,
            'use_mod_inca': self.use_mod_inca,
            'mod_inca_color': self.mod_inca_color.to_json(),
            'mod_inca_amount': self.mod_inca_amount.to_json(),
            'orbit_offset': self.orbit_offset.to_json(),
            'orbit_offset_local': self.orbit_offset_local,
            'is_solid': self.is_solid,
            'immovable': self.immovable,
        }

    def _dependencies_for_collision_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.collision_model)

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_collision_model, "collision_model", "AssetId"),
            (self._dependencies_for_model, "model", "AssetId"),
            (self.multi_model_information.dependencies_for, "multi_model_information", "MultiModelInformation"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MultiModelActor.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_multi_model_information(data: typing.BinaryIO, game: Game, property_size: int) -> MultiModelInformation:
    return MultiModelInformation.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_mod_inca_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_mod_inca_amount(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_orbit_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xf344c0b0: ('collision_box', _decode_collision_box),
    0x2e686c2a: ('collision_offset', _decode_collision_offset),
    0x0fc966dc: ('collision_model', structs.decode_BIG_Q),
    0xc27ffa8f: ('model', structs.decode_BIG_Q),
    0x1960932d: ('multi_model_information', _decode_multi_model_information),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xa09d4a1f: ('highlighted_in_x_ray', structs.decode_BIG_bool_),
    0xb530d7de: ('use_mod_inca', structs.decode_BIG_bool_),
    0xf8df6cd2: ('mod_inca_color', _decode_mod_inca_color),
    0xc23011d9: ('mod_inca_amount', _decode_mod_inca_amount),
    0x850115e4: ('orbit_offset', _decode_orbit_offset),
    0xe73f123d: ('orbit_offset_local', structs.decode_BIG_bool_),
    0x1d8dd846: ('is_solid', structs.decode_BIG_bool_),
    0x1e32523e: ('immovable', structs.decode_BIG_bool_),
}
