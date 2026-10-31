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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.common.archetypes.RotationSplines import RotationSplines
from retro_data_structures.properties.common.archetypes.ScaleSplines import ScaleSplines
from retro_data_structures.properties.corruption.archetypes.TranslationSplines import TranslationSplines
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ActorTransformJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flags: int
        duration: float
        rotation_controls: json_util.JsonObject
        scale_controls: json_util.JsonObject
        translation_control: json_util.JsonObject
        path_position: json_util.JsonObject
    

@dataclasses.dataclass()
class ActorTransform(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    flags: int = dataclasses.field(default=20, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc6ce7689, original_name='Flags'
        ),
    })  # Flagset
    duration: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b51e23f, original_name='Duration'
        ),
    })
    rotation_controls: RotationSplines = dataclasses.field(default_factory=RotationSplines, metadata={
        'reflection': FieldReflection[RotationSplines](
            RotationSplines, id=0xefe4ea57, original_name='RotationControls', from_json=RotationSplines.from_json, to_json=RotationSplines.to_json
        ),
    })
    scale_controls: ScaleSplines = dataclasses.field(default_factory=ScaleSplines, metadata={
        'reflection': FieldReflection[ScaleSplines](
            ScaleSplines, id=0x2f7ec0a2, original_name='ScaleControls', from_json=ScaleSplines.from_json, to_json=ScaleSplines.to_json
        ),
    })
    translation_control: TranslationSplines = dataclasses.field(default_factory=TranslationSplines, metadata={
        'reflection': FieldReflection[TranslationSplines](
            TranslationSplines, id=0x692267ea, original_name='TranslationControl', from_json=TranslationSplines.from_json, to_json=TranslationSplines.to_json
        ),
    })
    path_position: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x51b8aaca, original_name='PathPosition', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'ATRN'

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
        if property_count != 7:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6ce7689
        flags = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b51e23f
        duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefe4ea57
        rotation_controls = RotationSplines.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f7ec0a2
        scale_controls = ScaleSplines.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x692267ea
        translation_control = TranslationSplines.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51b8aaca
        path_position = Spline.from_stream(data, game, property_size)
    
        return cls(editor_properties, flags, duration, rotation_controls, scale_controls, translation_control, path_position)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6\xcev\x89')  # 0xc6ce7689
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.flags))

        data.write(b'\x8bQ\xe2?')  # 0x8b51e23f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b'\xef\xe4\xeaW')  # 0xefe4ea57
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rotation_controls.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'/~\xc0\xa2')  # 0x2f7ec0a2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scale_controls.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'i"g\xea')  # 0x692267ea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.translation_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Q\xb8\xaa\xca')  # 0x51b8aaca
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.path_position.to_stream(data, game)
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
        json_data = typing.cast("ActorTransformJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            flags=json_data['flags'],
            duration=json_data['duration'],
            rotation_controls=RotationSplines.from_json(json_data['rotation_controls']),
            scale_controls=ScaleSplines.from_json(json_data['scale_controls']),
            translation_control=TranslationSplines.from_json(json_data['translation_control']),
            path_position=Spline.from_json(json_data['path_position']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'flags': self.flags,
            'duration': self.duration,
            'rotation_controls': self.rotation_controls.to_json(),
            'scale_controls': self.scale_controls.to_json(),
            'translation_control': self.translation_control.to_json(),
            'path_position': self.path_position.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_rotation_controls(data: typing.BinaryIO, game: Game, property_size: int) -> RotationSplines:
    return RotationSplines.from_stream(data, game, property_size)


def _decode_scale_controls(data: typing.BinaryIO, game: Game, property_size: int) -> ScaleSplines:
    return ScaleSplines.from_stream(data, game, property_size)


def _decode_translation_control(data: typing.BinaryIO, game: Game, property_size: int) -> TranslationSplines:
    return TranslationSplines.from_stream(data, game, property_size)


def _decode_path_position(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xc6ce7689: ('flags', structs.decode_BIG_L),
    0x8b51e23f: ('duration', structs.decode_BIG_f),
    0xefe4ea57: ('rotation_controls', _decode_rotation_controls),
    0x2f7ec0a2: ('scale_controls', _decode_scale_controls),
    0x692267ea: ('translation_control', _decode_translation_control),
    0x51b8aaca: ('path_position', _decode_path_position),
}
