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
from retro_data_structures.properties.corruption.archetypes.BlinkData import BlinkData

if typing.TYPE_CHECKING:
    class FederationDataJson(typing_extensions.TypedDict):
        can_blink: bool
        blink_data: json_util.JsonObject
        unknown: bool
    

@dataclasses.dataclass()
class FederationData(BaseProperty):
    can_blink: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x5c747710, original_name='CanBlink'
        ),
    })
    blink_data: BlinkData = dataclasses.field(default_factory=BlinkData, metadata={
        'reflection': FieldReflection[BlinkData](
            BlinkData, id=0x6e58d714, original_name='BlinkData', from_json=BlinkData.from_json, to_json=BlinkData.to_json
        ),
    })
    unknown: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0f31fdae, original_name='Unknown'
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
        if property_count != 3:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5c747710
        can_blink = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e58d714
        blink_data = BlinkData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f31fdae
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(can_blink, blink_data, unknown)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x03')  # 3 properties

        data.write(b'\\tw\x10')  # 0x5c747710
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_blink))

        data.write(b'nX\xd7\x14')  # 0x6e58d714
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.blink_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0f1\xfd\xae')  # 0xf31fdae
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FederationDataJson", data)
        return cls(
            can_blink=json_data['can_blink'],
            blink_data=BlinkData.from_json(json_data['blink_data']),
            unknown=json_data['unknown'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'can_blink': self.can_blink,
            'blink_data': self.blink_data.to_json(),
            'unknown': self.unknown,
        }


def _decode_blink_data(data: typing.BinaryIO, game: Game, property_size: int) -> BlinkData:
    return BlinkData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5c747710: ('can_blink', structs.decode_BIG_bool_),
    0x6e58d714: ('blink_data', _decode_blink_data),
    0x0f31fdae: ('unknown', structs.decode_BIG_bool_),
}
