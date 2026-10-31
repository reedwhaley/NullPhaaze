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
from retro_data_structures.properties.corruption.archetypes.PuddleControlPhaseData import PuddleControlPhaseData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PuddleControlDataJson(typing_extensions.TypedDict):
        speed_mul: float
        bounding_box_scale: float
        start: json_util.JsonObject
        out: json_util.JsonObject
        reverse: json_util.JsonObject
        in_: json_util.JsonObject
        end: json_util.JsonObject
        start_sound: int
    

@dataclasses.dataclass()
class PuddleControlData(BaseProperty):
    speed_mul: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b3a08c9, original_name='SpeedMul'
        ),
    })
    bounding_box_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x14bfdea6, original_name='BoundingBoxScale'
        ),
    })
    start: PuddleControlPhaseData = dataclasses.field(default_factory=PuddleControlPhaseData, metadata={
        'reflection': FieldReflection[PuddleControlPhaseData](
            PuddleControlPhaseData, id=0xae0e60e2, original_name='Start', from_json=PuddleControlPhaseData.from_json, to_json=PuddleControlPhaseData.to_json
        ),
    })
    out: PuddleControlPhaseData = dataclasses.field(default_factory=PuddleControlPhaseData, metadata={
        'reflection': FieldReflection[PuddleControlPhaseData](
            PuddleControlPhaseData, id=0x1fd78dd3, original_name='Out', from_json=PuddleControlPhaseData.from_json, to_json=PuddleControlPhaseData.to_json
        ),
    })
    reverse: PuddleControlPhaseData = dataclasses.field(default_factory=PuddleControlPhaseData, metadata={
        'reflection': FieldReflection[PuddleControlPhaseData](
            PuddleControlPhaseData, id=0x5d4158a7, original_name='Reverse', from_json=PuddleControlPhaseData.from_json, to_json=PuddleControlPhaseData.to_json
        ),
    })
    in_: PuddleControlPhaseData = dataclasses.field(default_factory=PuddleControlPhaseData, metadata={
        'reflection': FieldReflection[PuddleControlPhaseData](
            PuddleControlPhaseData, id=0xda4488bf, original_name='In', from_json=PuddleControlPhaseData.from_json, to_json=PuddleControlPhaseData.to_json
        ),
    })
    end: PuddleControlPhaseData = dataclasses.field(default_factory=PuddleControlPhaseData, metadata={
        'reflection': FieldReflection[PuddleControlPhaseData](
            PuddleControlPhaseData, id=0x57b054de, original_name='End', from_json=PuddleControlPhaseData.from_json, to_json=PuddleControlPhaseData.to_json
        ),
    })
    start_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa8cc48b3, original_name='StartSound'
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
        if property_count != 8:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b3a08c9
        speed_mul = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14bfdea6
        bounding_box_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae0e60e2
        start = PuddleControlPhaseData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1fd78dd3
        out = PuddleControlPhaseData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d4158a7
        reverse = PuddleControlPhaseData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xda4488bf
        in_ = PuddleControlPhaseData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57b054de
        end = PuddleControlPhaseData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8cc48b3
        start_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(speed_mul, bounding_box_scale, start, out, reverse, in_, end, start_sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'\x0b:\x08\xc9')  # 0xb3a08c9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.speed_mul))

        data.write(b'\x14\xbf\xde\xa6')  # 0x14bfdea6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bounding_box_scale))

        data.write(b'\xae\x0e`\xe2')  # 0xae0e60e2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.start.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1f\xd7\x8d\xd3')  # 0x1fd78dd3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.out.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b']AX\xa7')  # 0x5d4158a7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.reverse.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdaD\x88\xbf')  # 0xda4488bf
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.in_.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'W\xb0T\xde')  # 0x57b054de
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.end.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa8\xccH\xb3')  # 0xa8cc48b3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.start_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PuddleControlDataJson", data)
        return cls(
            speed_mul=json_data['speed_mul'],
            bounding_box_scale=json_data['bounding_box_scale'],
            start=PuddleControlPhaseData.from_json(json_data['start']),
            out=PuddleControlPhaseData.from_json(json_data['out']),
            reverse=PuddleControlPhaseData.from_json(json_data['reverse']),
            in_=PuddleControlPhaseData.from_json(json_data['in_']),
            end=PuddleControlPhaseData.from_json(json_data['end']),
            start_sound=json_data['start_sound'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'speed_mul': self.speed_mul,
            'bounding_box_scale': self.bounding_box_scale,
            'start': self.start.to_json(),
            'out': self.out.to_json(),
            'reverse': self.reverse.to_json(),
            'in_': self.in_.to_json(),
            'end': self.end.to_json(),
            'start_sound': self.start_sound,
        }

    def _dependencies_for_start_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.start_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_start_sound(asset_manager)


def _decode_start(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_out(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_reverse(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_in_(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_end(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x0b3a08c9: ('speed_mul', structs.decode_BIG_f),
    0x14bfdea6: ('bounding_box_scale', structs.decode_BIG_f),
    0xae0e60e2: ('start', _decode_start),
    0x1fd78dd3: ('out', _decode_out),
    0x5d4158a7: ('reverse', _decode_reverse),
    0xda4488bf: ('in_', _decode_in_),
    0x57b054de: ('end', _decode_end),
    0xa8cc48b3: ('start_sound', structs.decode_BIG_Q),
}
