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
    class TweakBall_MiscJson(typing_extensions.TypedDict):
        ball_max_left_analogue_range: float
        ball_max_right_analogue_range: float
        unknown: float
        ball_touch_radius: float
        dark_world_light_radius: float
        dark_world_light_radius_dark_suit: float
        dark_world_light_radius_light_suit: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x13cfde23, 0xf3499713, 0x895a47fb, 0xbb751ca2, 0x9f73ace1, 0xad662ae9, 0xb0575d4e)


@dataclasses.dataclass()
class TweakBall_Misc(BaseProperty):
    ball_max_left_analogue_range: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13cfde23, original_name='BallMaxLeftAnalogueRange'
        ),
    })
    ball_max_right_analogue_range: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf3499713, original_name='BallMaxRightAnalogueRange'
        ),
    })
    unknown: float = dataclasses.field(default=200.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x895a47fb, original_name='Unknown'
        ),
    })
    ball_touch_radius: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbb751ca2, original_name='BallTouchRadius'
        ),
    })
    dark_world_light_radius: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9f73ace1, original_name='DarkWorldLightRadius'
        ),
    })
    dark_world_light_radius_dark_suit: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad662ae9, original_name='DarkWorldLightRadiusDarkSuit'
        ),
    })
    dark_world_light_radius_light_suit: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb0575d4e, original_name='DarkWorldLightRadiusLightSuit'
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
        if property_count != 7:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(70))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'\x13\xcf\xde#')  # 0x13cfde23
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_max_left_analogue_range))

        data.write(b'\xf3I\x97\x13')  # 0xf3499713
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_max_right_analogue_range))

        data.write(b'\x89ZG\xfb')  # 0x895a47fb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\xbbu\x1c\xa2')  # 0xbb751ca2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_touch_radius))

        data.write(b'\x9fs\xac\xe1')  # 0x9f73ace1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_world_light_radius))

        data.write(b'\xadf*\xe9')  # 0xad662ae9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_world_light_radius_dark_suit))

        data.write(b'\xb0W]N')  # 0xb0575d4e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_world_light_radius_light_suit))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakBall_MiscJson", data)
        return cls(
            ball_max_left_analogue_range=json_data['ball_max_left_analogue_range'],
            ball_max_right_analogue_range=json_data['ball_max_right_analogue_range'],
            unknown=json_data['unknown'],
            ball_touch_radius=json_data['ball_touch_radius'],
            dark_world_light_radius=json_data['dark_world_light_radius'],
            dark_world_light_radius_dark_suit=json_data['dark_world_light_radius_dark_suit'],
            dark_world_light_radius_light_suit=json_data['dark_world_light_radius_light_suit'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'ball_max_left_analogue_range': self.ball_max_left_analogue_range,
            'ball_max_right_analogue_range': self.ball_max_right_analogue_range,
            'unknown': self.unknown,
            'ball_touch_radius': self.ball_touch_radius,
            'dark_world_light_radius': self.dark_world_light_radius,
            'dark_world_light_radius_dark_suit': self.dark_world_light_radius_dark_suit,
            'dark_world_light_radius_light_suit': self.dark_world_light_radius_light_suit,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x13cfde23: ('ball_max_left_analogue_range', structs.decode_BIG_f),
    0xf3499713: ('ball_max_right_analogue_range', structs.decode_BIG_f),
    0x895a47fb: ('unknown', structs.decode_BIG_f),
    0xbb751ca2: ('ball_touch_radius', structs.decode_BIG_f),
    0x9f73ace1: ('dark_world_light_radius', structs.decode_BIG_f),
    0xad662ae9: ('dark_world_light_radius_dark_suit', structs.decode_BIG_f),
    0xb0575d4e: ('dark_world_light_radius_light_suit', structs.decode_BIG_f),
}
