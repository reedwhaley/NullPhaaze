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

if typing.TYPE_CHECKING:
    class GrappleParametersJson(typing_extensions.TypedDict):
        grapple_attach_min_distance: float
        grapple_attach_max_distance: float
        grapple_attach_max_angle: float
        visible_through_geometry: bool
        constrain_to_axis: bool
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x2ba7fabc, 0x7a5e41e1, 0x76104d9e, 0xbaa8a527, 0x11b6a17a)


@dataclasses.dataclass()
class GrappleParameters(BaseProperty):
    grapple_attach_min_distance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ba7fabc, original_name='GrappleAttachMinDistance'
        ),
    })
    grapple_attach_max_distance: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7a5e41e1, original_name='GrappleAttachMaxDistance'
        ),
    })
    grapple_attach_max_angle: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76104d9e, original_name='GrappleAttachMaxAngle'
        ),
    })
    visible_through_geometry: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbaa8a527, original_name='VisibleThroughGeometry'
        ),
    })
    constrain_to_axis: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x11b6a17a, original_name='ConstrainToAxis'
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
        if property_count != 5:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLH?LH?')
    
        dec = _FAST_FORMAT.unpack(data.read(44))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'+\xa7\xfa\xbc')  # 0x2ba7fabc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_attach_min_distance))

        data.write(b'z^A\xe1')  # 0x7a5e41e1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_attach_max_distance))

        data.write(b'v\x10M\x9e')  # 0x76104d9e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_attach_max_angle))

        data.write(b"\xba\xa8\xa5'")  # 0xbaa8a527
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.visible_through_geometry))

        data.write(b'\x11\xb6\xa1z')  # 0x11b6a17a
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.constrain_to_axis))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GrappleParametersJson", data)
        return cls(
            grapple_attach_min_distance=json_data['grapple_attach_min_distance'],
            grapple_attach_max_distance=json_data['grapple_attach_max_distance'],
            grapple_attach_max_angle=json_data['grapple_attach_max_angle'],
            visible_through_geometry=json_data['visible_through_geometry'],
            constrain_to_axis=json_data['constrain_to_axis'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'grapple_attach_min_distance': self.grapple_attach_min_distance,
            'grapple_attach_max_distance': self.grapple_attach_max_distance,
            'grapple_attach_max_angle': self.grapple_attach_max_angle,
            'visible_through_geometry': self.visible_through_geometry,
            'constrain_to_axis': self.constrain_to_axis,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2ba7fabc: ('grapple_attach_min_distance', structs.decode_BIG_f),
    0x7a5e41e1: ('grapple_attach_max_distance', structs.decode_BIG_f),
    0x76104d9e: ('grapple_attach_max_angle', structs.decode_BIG_f),
    0xbaa8a527: ('visible_through_geometry', structs.decode_BIG_bool_),
    0x11b6a17a: ('constrain_to_axis', structs.decode_BIG_bool_),
}
