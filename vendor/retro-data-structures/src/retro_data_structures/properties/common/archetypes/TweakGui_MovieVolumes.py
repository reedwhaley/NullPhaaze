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
    class TweakGui_MovieVolumesJson(typing_extensions.TypedDict):
        movie_volume_lost_game: int
        unknown_0xc1a2e858: int
        unknown_0x138c3bb8: int
        movie_volume_before_credits: int
        movie_volume_completion_screen: int
        movie_volume_after_credits: int
        movie_volume_credits_music: int
        movie_volume_completion_screen_music: int
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xae149646, 0xc1a2e858, 0x138c3bb8, 0xe5587648, 0x9ed00248, 0x6f135424, 0xdb2260b7, 0xf38093f5)


@dataclasses.dataclass()
class TweakGui_MovieVolumes(BaseProperty):
    movie_volume_lost_game: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0xae149646, original_name='MovieVolumeLostGame'
        ),
    })
    unknown_0xc1a2e858: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc1a2e858, original_name='Unknown'
        ),
    })
    unknown_0x138c3bb8: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0x138c3bb8, original_name='Unknown'
        ),
    })
    movie_volume_before_credits: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe5587648, original_name='MovieVolumeBeforeCredits'
        ),
    })
    movie_volume_completion_screen: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9ed00248, original_name='MovieVolumeCompletionScreen'
        ),
    })
    movie_volume_after_credits: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6f135424, original_name='MovieVolumeAfterCredits'
        ),
    })
    movie_volume_credits_music: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0xdb2260b7, original_name='MovieVolumeCreditsMusic'
        ),
    })
    movie_volume_completion_screen_music: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0xf38093f5, original_name='MovieVolumeCompletionScreenMusic'
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
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHlLHlLHlLHlLHlLHlLHlLHl')
    
        dec = _FAST_FORMAT.unpack(data.read(80))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'\xae\x14\x96F')  # 0xae149646
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.movie_volume_lost_game))

        data.write(b'\xc1\xa2\xe8X')  # 0xc1a2e858
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc1a2e858))

        data.write(b'\x13\x8c;\xb8')  # 0x138c3bb8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x138c3bb8))

        data.write(b'\xe5XvH')  # 0xe5587648
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.movie_volume_before_credits))

        data.write(b'\x9e\xd0\x02H')  # 0x9ed00248
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.movie_volume_completion_screen))

        data.write(b'o\x13T$')  # 0x6f135424
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.movie_volume_after_credits))

        data.write(b'\xdb"`\xb7')  # 0xdb2260b7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.movie_volume_credits_music))

        data.write(b'\xf3\x80\x93\xf5')  # 0xf38093f5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.movie_volume_completion_screen_music))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_MovieVolumesJson", data)
        return cls(
            movie_volume_lost_game=json_data['movie_volume_lost_game'],
            unknown_0xc1a2e858=json_data['unknown_0xc1a2e858'],
            unknown_0x138c3bb8=json_data['unknown_0x138c3bb8'],
            movie_volume_before_credits=json_data['movie_volume_before_credits'],
            movie_volume_completion_screen=json_data['movie_volume_completion_screen'],
            movie_volume_after_credits=json_data['movie_volume_after_credits'],
            movie_volume_credits_music=json_data['movie_volume_credits_music'],
            movie_volume_completion_screen_music=json_data['movie_volume_completion_screen_music'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'movie_volume_lost_game': self.movie_volume_lost_game,
            'unknown_0xc1a2e858': self.unknown_0xc1a2e858,
            'unknown_0x138c3bb8': self.unknown_0x138c3bb8,
            'movie_volume_before_credits': self.movie_volume_before_credits,
            'movie_volume_completion_screen': self.movie_volume_completion_screen,
            'movie_volume_after_credits': self.movie_volume_after_credits,
            'movie_volume_credits_music': self.movie_volume_credits_music,
            'movie_volume_completion_screen_music': self.movie_volume_completion_screen_music,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xae149646: ('movie_volume_lost_game', structs.decode_BIG_l),
    0xc1a2e858: ('unknown_0xc1a2e858', structs.decode_BIG_l),
    0x138c3bb8: ('unknown_0x138c3bb8', structs.decode_BIG_l),
    0xe5587648: ('movie_volume_before_credits', structs.decode_BIG_l),
    0x9ed00248: ('movie_volume_completion_screen', structs.decode_BIG_l),
    0x6f135424: ('movie_volume_after_credits', structs.decode_BIG_l),
    0xdb2260b7: ('movie_volume_credits_music', structs.decode_BIG_l),
    0xf38093f5: ('movie_volume_completion_screen_music', structs.decode_BIG_l),
}
