# Generated File
from __future__ import annotations

import dataclasses
import enum
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PlayerControllerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        player_proxy_flags: int
        model: int
        animation_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        proxy_type: int
        player_offset: json_util.JsonValue
        int_parameter1: int
        int_parameter2: int
        float_parameter1: float
        float_parameter2: float
        float_parameter3: float
        vector_parameter1: json_util.JsonValue
        string_parameter1: str
    

class PlayerProxyFlags(enum.IntFlag):
    ApplytoPlayer1 = 1
    ApplytoPlayer2 = 2
    ApplytoPlayer3 = 4
    ApplytoPlayer4 = 8
    ApplytoTeam1 = 16
    ApplytoTeam2 = 32

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class PlayerController(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    player_proxy_flags: PlayerProxyFlags = dataclasses.field(default=PlayerProxyFlags(0), metadata={
        'reflection': FieldReflection[PlayerProxyFlags](
            PlayerProxyFlags, id=0xe71de331, original_name='PlayerProxyFlags', from_json=PlayerProxyFlags.from_json, to_json=PlayerProxyFlags.to_json
        ),
    })
    model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc27ffa8f, original_name='Model'
        ),
    })
    animation_information: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xe25fb08c, original_name='AnimationInformation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    proxy_type: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xca56a18a, original_name='ProxyType'
        ),
    })  # Choice
    player_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=1.5), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x1d8b933f, original_name='PlayerOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    int_parameter1: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xcb753319, original_name='IntParameter1'
        ),
    })
    int_parameter2: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd9c09cf7, original_name='IntParameter2'
        ),
    })
    float_parameter1: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf09c2b4b, original_name='FloatParameter1'
        ),
    })
    float_parameter2: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x760859e5, original_name='FloatParameter2'
        ),
    })
    float_parameter3: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbd548a40, original_name='FloatParameter3'
        ),
    })
    vector_parameter1: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xc012f196, original_name='VectorParameter1', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    string_parameter1: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x70bc90a6, original_name='StringParameter1'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'PLCT'

    @classmethod
    def modules(cls) -> list[str]:
        return ['ScriptPlayerProxy.rel']

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
        if property_count != 14:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe71de331
        player_proxy_flags = PlayerProxyFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc27ffa8f
        model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe25fb08c
        animation_information = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca56a18a
        proxy_type = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1d8b933f
        player_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcb753319
        int_parameter1 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd9c09cf7
        int_parameter2 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf09c2b4b
        float_parameter1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x760859e5
        float_parameter2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd548a40
        float_parameter3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc012f196
        vector_parameter1 = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70bc90a6
        string_parameter1 = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        return cls(editor_properties, player_proxy_flags, model, animation_information, actor_information, proxy_type, player_offset, int_parameter1, int_parameter2, float_parameter1, float_parameter2, float_parameter3, vector_parameter1, string_parameter1)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x0e')  # 14 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe7\x1d\xe31')  # 0xe71de331
        data.write(b'\x00\x04')  # size
        self.player_proxy_flags.to_stream(data, game)

        data.write(b'\xc2\x7f\xfa\x8f')  # 0xc27ffa8f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.model))

        data.write(b'\xe2_\xb0\x8c')  # 0xe25fb08c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.animation_information.to_stream(data, game)
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

        data.write(b'\xcaV\xa1\x8a')  # 0xca56a18a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.proxy_type))

        data.write(b'\x1d\x8b\x93?')  # 0x1d8b933f
        data.write(b'\x00\x0c')  # size
        self.player_offset.to_stream(data, game)

        data.write(b'\xcbu3\x19')  # 0xcb753319
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.int_parameter1))

        data.write(b'\xd9\xc0\x9c\xf7')  # 0xd9c09cf7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.int_parameter2))

        data.write(b'\xf0\x9c+K')  # 0xf09c2b4b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.float_parameter1))

        data.write(b'v\x08Y\xe5')  # 0x760859e5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.float_parameter2))

        data.write(b'\xbdT\x8a@')  # 0xbd548a40
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.float_parameter3))

        data.write(b'\xc0\x12\xf1\x96')  # 0xc012f196
        data.write(b'\x00\x0c')  # size
        self.vector_parameter1.to_stream(data, game)

        data.write(b'p\xbc\x90\xa6')  # 0x70bc90a6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.string_parameter1.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
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
        json_data = typing.cast("PlayerControllerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            player_proxy_flags=PlayerProxyFlags.from_json(json_data['player_proxy_flags']),
            model=json_data['model'],
            animation_information=AnimationParameters.from_json(json_data['animation_information']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            proxy_type=json_data['proxy_type'],
            player_offset=Vector.from_json(json_data['player_offset']),
            int_parameter1=json_data['int_parameter1'],
            int_parameter2=json_data['int_parameter2'],
            float_parameter1=json_data['float_parameter1'],
            float_parameter2=json_data['float_parameter2'],
            float_parameter3=json_data['float_parameter3'],
            vector_parameter1=Vector.from_json(json_data['vector_parameter1']),
            string_parameter1=json_data['string_parameter1'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'player_proxy_flags': self.player_proxy_flags.to_json(),
            'model': self.model,
            'animation_information': self.animation_information.to_json(),
            'actor_information': self.actor_information.to_json(),
            'proxy_type': self.proxy_type,
            'player_offset': self.player_offset.to_json(),
            'int_parameter1': self.int_parameter1,
            'int_parameter2': self.int_parameter2,
            'float_parameter1': self.float_parameter1,
            'float_parameter2': self.float_parameter2,
            'float_parameter3': self.float_parameter3,
            'vector_parameter1': self.vector_parameter1.to_json(),
            'string_parameter1': self.string_parameter1,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PlayerController.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_player_proxy_flags(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerProxyFlags:
    return PlayerProxyFlags.from_stream(data, game)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_player_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_vector_parameter1(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_string_parameter1(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xe71de331: ('player_proxy_flags', _decode_player_proxy_flags),
    0xc27ffa8f: ('model', structs.decode_BIG_L),
    0xe25fb08c: ('animation_information', _decode_animation_information),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xca56a18a: ('proxy_type', structs.decode_BIG_L),
    0x1d8b933f: ('player_offset', _decode_player_offset),
    0xcb753319: ('int_parameter1', structs.decode_BIG_l),
    0xd9c09cf7: ('int_parameter2', structs.decode_BIG_l),
    0xf09c2b4b: ('float_parameter1', structs.decode_BIG_f),
    0x760859e5: ('float_parameter2', structs.decode_BIG_f),
    0xbd548a40: ('float_parameter3', structs.decode_BIG_f),
    0xc012f196: ('vector_parameter1', _decode_vector_parameter1),
    0x70bc90a6: ('string_parameter1', _decode_string_parameter1),
}
