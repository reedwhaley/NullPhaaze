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
from retro_data_structures.properties.echoes.archetypes.TweakPlayerControls_Booleans import TweakPlayerControls_Booleans
from retro_data_structures.properties.echoes.archetypes.TweakPlayerControls_Controls import TweakPlayerControls_Controls

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class TweakPlayerControlsJson(typing_extensions.TypedDict):
        instance_name: str
        controls: json_util.JsonObject
        booleans: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakPlayerControls(BaseObjectType):
    instance_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x7fda1466, original_name='InstanceName'
        ),
    })
    controls: TweakPlayerControls_Controls = dataclasses.field(default_factory=TweakPlayerControls_Controls, metadata={
        'reflection': FieldReflection[TweakPlayerControls_Controls](
            TweakPlayerControls_Controls, id=0x3c34dfed, original_name='Controls', from_json=TweakPlayerControls_Controls.from_json, to_json=TweakPlayerControls_Controls.to_json
        ),
    })
    booleans: TweakPlayerControls_Booleans = dataclasses.field(default_factory=TweakPlayerControls_Booleans, metadata={
        'reflection': FieldReflection[TweakPlayerControls_Booleans](
            TweakPlayerControls_Booleans, id=0x168a79f1, original_name='Booleans', from_json=TweakPlayerControls_Booleans.from_json, to_json=TweakPlayerControls_Booleans.to_json
        ),
    })

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return 'TWPC'

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
        if property_count != 3:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fda1466
        instance_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c34dfed
        controls = TweakPlayerControls_Controls.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x168a79f1
        booleans = TweakPlayerControls_Booleans.from_stream(data, game, property_size)
    
        return cls(instance_name, controls, booleans)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x03')  # 3 properties

        data.write(b'\x7f\xda\x14f')  # 0x7fda1466
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.instance_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'<4\xdf\xed')  # 0x3c34dfed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.controls.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x16\x8ay\xf1')  # 0x168a79f1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.booleans.to_stream(data, game)
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
        json_data = typing.cast("TweakPlayerControlsJson", data)
        return cls(
            instance_name=json_data['instance_name'],
            controls=TweakPlayerControls_Controls.from_json(json_data['controls']),
            booleans=TweakPlayerControls_Booleans.from_json(json_data['booleans']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'instance_name': self.instance_name,
            'controls': self.controls.to_json(),
            'booleans': self.booleans.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_controls(data: typing.BinaryIO, game: Game, property_size: int) -> TweakPlayerControls_Controls:
    return TweakPlayerControls_Controls.from_stream(data, game, property_size)


def _decode_booleans(data: typing.BinaryIO, game: Game, property_size: int) -> TweakPlayerControls_Booleans:
    return TweakPlayerControls_Booleans.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7fda1466: ('instance_name', _decode_instance_name),
    0x3c34dfed: ('controls', _decode_controls),
    0x168a79f1: ('booleans', _decode_booleans),
}
