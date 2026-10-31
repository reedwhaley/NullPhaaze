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
from retro_data_structures.properties.corruption.archetypes.ModalParameters import ModalParameters

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MultiModelInformationJson(typing_extensions.TypedDict):
        num_extra_models: int
        use_fade: bool
        fade_time: float
        x02: json_util.JsonObject
        x03: json_util.JsonObject
        x04: json_util.JsonObject
        x05: json_util.JsonObject
        x06: json_util.JsonObject
        x07: json_util.JsonObject
        x08: json_util.JsonObject
        x09: json_util.JsonObject
        x10: json_util.JsonObject
    

@dataclasses.dataclass()
class MultiModelInformation(BaseProperty):
    num_extra_models: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6439f487, original_name='NumExtraModels'
        ),
    })
    use_fade: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe25a15c1, original_name='UseFade'
        ),
    })
    fade_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4124c4c, original_name='FadeTime'
        ),
    })
    x02: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0x681c4457, original_name='x02', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x03: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0xc674d5c6, original_name='x03', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x04: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0x3b8d2db3, original_name='x04', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x05: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0x95e5bc22, original_name='x05', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x06: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0xbc2d08d0, original_name='x06', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x07: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0x12459941, original_name='x07', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x08: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0x9caffe7b, original_name='x08', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x09: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0x32c76fea, original_name='x09', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
        ),
    })
    x10: ModalParameters = dataclasses.field(default_factory=ModalParameters, metadata={
        'reflection': FieldReflection[ModalParameters](
            ModalParameters, id=0x681aaa77, original_name='x10', from_json=ModalParameters.from_json, to_json=ModalParameters.to_json
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
        if property_count != 12:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6439f487
        num_extra_models = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe25a15c1
        use_fade = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4124c4c
        fade_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x681c4457
        x02 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc674d5c6
        x03 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3b8d2db3
        x04 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e5bc22
        x05 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc2d08d0
        x06 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12459941
        x07 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9caffe7b
        x08 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32c76fea
        x09 = ModalParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x681aaa77
        x10 = ModalParameters.from_stream(data, game, property_size)
    
        return cls(num_extra_models, use_fade, fade_time, x02, x03, x04, x05, x06, x07, x08, x09, x10)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0c')  # 12 properties

        data.write(b'd9\xf4\x87')  # 0x6439f487
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_extra_models))

        data.write(b'\xe2Z\x15\xc1')  # 0xe25a15c1
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_fade))

        data.write(b'\xd4\x12LL')  # 0xd4124c4c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fade_time))

        data.write(b'h\x1cDW')  # 0x681c4457
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x02.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6t\xd5\xc6')  # 0xc674d5c6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x03.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b';\x8d-\xb3')  # 0x3b8d2db3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x04.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x95\xe5\xbc"')  # 0x95e5bc22
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x05.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbc-\x08\xd0')  # 0xbc2d08d0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x06.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x12E\x99A')  # 0x12459941
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x07.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9c\xaf\xfe{')  # 0x9caffe7b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x08.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'2\xc7o\xea')  # 0x32c76fea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x09.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'h\x1a\xaaw')  # 0x681aaa77
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x10.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MultiModelInformationJson", data)
        return cls(
            num_extra_models=json_data['num_extra_models'],
            use_fade=json_data['use_fade'],
            fade_time=json_data['fade_time'],
            x02=ModalParameters.from_json(json_data['x02']),
            x03=ModalParameters.from_json(json_data['x03']),
            x04=ModalParameters.from_json(json_data['x04']),
            x05=ModalParameters.from_json(json_data['x05']),
            x06=ModalParameters.from_json(json_data['x06']),
            x07=ModalParameters.from_json(json_data['x07']),
            x08=ModalParameters.from_json(json_data['x08']),
            x09=ModalParameters.from_json(json_data['x09']),
            x10=ModalParameters.from_json(json_data['x10']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'num_extra_models': self.num_extra_models,
            'use_fade': self.use_fade,
            'fade_time': self.fade_time,
            'x02': self.x02.to_json(),
            'x03': self.x03.to_json(),
            'x04': self.x04.to_json(),
            'x05': self.x05.to_json(),
            'x06': self.x06.to_json(),
            'x07': self.x07.to_json(),
            'x08': self.x08.to_json(),
            'x09': self.x09.to_json(),
            'x10': self.x10.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.x02.dependencies_for, "x02", "ModalParameters"),
            (self.x03.dependencies_for, "x03", "ModalParameters"),
            (self.x04.dependencies_for, "x04", "ModalParameters"),
            (self.x05.dependencies_for, "x05", "ModalParameters"),
            (self.x06.dependencies_for, "x06", "ModalParameters"),
            (self.x07.dependencies_for, "x07", "ModalParameters"),
            (self.x08.dependencies_for, "x08", "ModalParameters"),
            (self.x09.dependencies_for, "x09", "ModalParameters"),
            (self.x10.dependencies_for, "x10", "ModalParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MultiModelInformation.{field_name} ({field_type}): {e}"
                )


def _decode_x02(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x03(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x04(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x05(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x06(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x07(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x08(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x09(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


def _decode_x10(data: typing.BinaryIO, game: Game, property_size: int) -> ModalParameters:
    return ModalParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6439f487: ('num_extra_models', structs.decode_BIG_l),
    0xe25a15c1: ('use_fade', structs.decode_BIG_bool_),
    0xd4124c4c: ('fade_time', structs.decode_BIG_f),
    0x681c4457: ('x02', _decode_x02),
    0xc674d5c6: ('x03', _decode_x03),
    0x3b8d2db3: ('x04', _decode_x04),
    0x95e5bc22: ('x05', _decode_x05),
    0xbc2d08d0: ('x06', _decode_x06),
    0x12459941: ('x07', _decode_x07),
    0x9caffe7b: ('x08', _decode_x08),
    0x32c76fea: ('x09', _decode_x09),
    0x681aaa77: ('x10', _decode_x10),
}
