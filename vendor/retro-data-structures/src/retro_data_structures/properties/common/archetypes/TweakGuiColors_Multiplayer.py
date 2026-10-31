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
from retro_data_structures.properties.color import Color

if typing.TYPE_CHECKING:
    class TweakGuiColors_MultiplayerJson(typing_extensions.TypedDict):
        score_text_color: json_util.JsonValue
        winning_score_text_color: json_util.JsonValue
        timer_text_color: json_util.JsonValue
        timer_text_blink_color: json_util.JsonValue
        scoreboard_deco_color: json_util.JsonValue
        scoreboard_background_color: json_util.JsonValue
        kill_won_highlight_color: json_util.JsonValue
        kill_lost_hightlight_color: json_util.JsonValue
        lockon_indicator_on_color: json_util.JsonValue
        lockon_indicator_off_color: json_util.JsonValue
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x23cac744, 0xa09caefe, 0x6bf04ff9, 0x4280d00a, 0xec4197e3, 0x823e2fb3, 0x95cc4ed8, 0xdb2ca6ff, 0x3d27ffd, 0x4c215775)


@dataclasses.dataclass()
class TweakGuiColors_Multiplayer(BaseProperty):
    score_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x23cac744, original_name='ScoreTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    winning_score_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa09caefe, original_name='WinningScoreTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    timer_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6bf04ff9, original_name='TimerTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    timer_text_blink_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4280d00a, original_name='TimerTextBlinkColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scoreboard_deco_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xec4197e3, original_name='ScoreboardDecoColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scoreboard_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.5, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x823e2fb3, original_name='ScoreboardBackgroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    kill_won_highlight_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.5, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x95cc4ed8, original_name='KillWonHighlightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    kill_lost_hightlight_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.5, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdb2ca6ff, original_name='KillLostHightlightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    lockon_indicator_on_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x03d27ffd, original_name='LockonIndicatorOnColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    lockon_indicator_off_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4c215775, original_name='LockonIndicatorOffColor', from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 10:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffff')
    
        dec = _FAST_FORMAT.unpack(data.read(220))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[30], dec[36], dec[42], dec[48], dec[54]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            Color(*dec[26:30]),
            Color(*dec[32:36]),
            Color(*dec[38:42]),
            Color(*dec[44:48]),
            Color(*dec[50:54]),
            Color(*dec[56:60]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'#\xca\xc7D')  # 0x23cac744
        data.write(b'\x00\x10')  # size
        self.score_text_color.to_stream(data, game)

        data.write(b'\xa0\x9c\xae\xfe')  # 0xa09caefe
        data.write(b'\x00\x10')  # size
        self.winning_score_text_color.to_stream(data, game)

        data.write(b'k\xf0O\xf9')  # 0x6bf04ff9
        data.write(b'\x00\x10')  # size
        self.timer_text_color.to_stream(data, game)

        data.write(b'B\x80\xd0\n')  # 0x4280d00a
        data.write(b'\x00\x10')  # size
        self.timer_text_blink_color.to_stream(data, game)

        data.write(b'\xecA\x97\xe3')  # 0xec4197e3
        data.write(b'\x00\x10')  # size
        self.scoreboard_deco_color.to_stream(data, game)

        data.write(b'\x82>/\xb3')  # 0x823e2fb3
        data.write(b'\x00\x10')  # size
        self.scoreboard_background_color.to_stream(data, game)

        data.write(b'\x95\xccN\xd8')  # 0x95cc4ed8
        data.write(b'\x00\x10')  # size
        self.kill_won_highlight_color.to_stream(data, game)

        data.write(b'\xdb,\xa6\xff')  # 0xdb2ca6ff
        data.write(b'\x00\x10')  # size
        self.kill_lost_hightlight_color.to_stream(data, game)

        data.write(b'\x03\xd2\x7f\xfd')  # 0x3d27ffd
        data.write(b'\x00\x10')  # size
        self.lockon_indicator_on_color.to_stream(data, game)

        data.write(b'L!Wu')  # 0x4c215775
        data.write(b'\x00\x10')  # size
        self.lockon_indicator_off_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGuiColors_MultiplayerJson", data)
        return cls(
            score_text_color=Color.from_json(json_data['score_text_color']),
            winning_score_text_color=Color.from_json(json_data['winning_score_text_color']),
            timer_text_color=Color.from_json(json_data['timer_text_color']),
            timer_text_blink_color=Color.from_json(json_data['timer_text_blink_color']),
            scoreboard_deco_color=Color.from_json(json_data['scoreboard_deco_color']),
            scoreboard_background_color=Color.from_json(json_data['scoreboard_background_color']),
            kill_won_highlight_color=Color.from_json(json_data['kill_won_highlight_color']),
            kill_lost_hightlight_color=Color.from_json(json_data['kill_lost_hightlight_color']),
            lockon_indicator_on_color=Color.from_json(json_data['lockon_indicator_on_color']),
            lockon_indicator_off_color=Color.from_json(json_data['lockon_indicator_off_color']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'score_text_color': self.score_text_color.to_json(),
            'winning_score_text_color': self.winning_score_text_color.to_json(),
            'timer_text_color': self.timer_text_color.to_json(),
            'timer_text_blink_color': self.timer_text_blink_color.to_json(),
            'scoreboard_deco_color': self.scoreboard_deco_color.to_json(),
            'scoreboard_background_color': self.scoreboard_background_color.to_json(),
            'kill_won_highlight_color': self.kill_won_highlight_color.to_json(),
            'kill_lost_hightlight_color': self.kill_lost_hightlight_color.to_json(),
            'lockon_indicator_on_color': self.lockon_indicator_on_color.to_json(),
            'lockon_indicator_off_color': self.lockon_indicator_off_color.to_json(),
        }


def _decode_score_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_winning_score_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_timer_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_timer_text_blink_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scoreboard_deco_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scoreboard_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_kill_won_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_kill_lost_hightlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_lockon_indicator_on_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_lockon_indicator_off_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x23cac744: ('score_text_color', _decode_score_text_color),
    0xa09caefe: ('winning_score_text_color', _decode_winning_score_text_color),
    0x6bf04ff9: ('timer_text_color', _decode_timer_text_color),
    0x4280d00a: ('timer_text_blink_color', _decode_timer_text_blink_color),
    0xec4197e3: ('scoreboard_deco_color', _decode_scoreboard_deco_color),
    0x823e2fb3: ('scoreboard_background_color', _decode_scoreboard_background_color),
    0x95cc4ed8: ('kill_won_highlight_color', _decode_kill_won_highlight_color),
    0xdb2ca6ff: ('kill_lost_hightlight_color', _decode_kill_lost_hightlight_color),
    0x03d27ffd: ('lockon_indicator_on_color', _decode_lockon_indicator_on_color),
    0x4c215775: ('lockon_indicator_off_color', _decode_lockon_indicator_off_color),
}
