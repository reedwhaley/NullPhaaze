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
from retro_data_structures.properties.common.archetypes.TGunResources import TGunResources
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class TBallTransitionResourcesJson(typing_extensions.TypedDict):
        suit_ancs: str
        gun_resources: json_util.JsonObject
        multi_player_gun_resources: json_util.JsonObject
        fp_to_ball_alpha: json_util.JsonObject
        ball_to_fp_alpha: json_util.JsonObject
        fp_to_ball_alpha_multi_player: json_util.JsonObject
        ball_to_fp_alpha_multi_player: json_util.JsonObject
        movement_control: json_util.JsonObject
    

@dataclasses.dataclass()
class TBallTransitionResources(BaseProperty):
    suit_ancs: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xd48e4124, original_name='SuitANCS'
        ),
    })
    gun_resources: TGunResources = dataclasses.field(default_factory=TGunResources, metadata={
        'reflection': FieldReflection[TGunResources](
            TGunResources, id=0x01e12c84, original_name='GunResources', from_json=TGunResources.from_json, to_json=TGunResources.to_json
        ),
    })
    multi_player_gun_resources: TGunResources = dataclasses.field(default_factory=TGunResources, metadata={
        'reflection': FieldReflection[TGunResources](
            TGunResources, id=0xf24b055d, original_name='MultiPlayerGunResources', from_json=TGunResources.from_json, to_json=TGunResources.to_json
        ),
    })
    fp_to_ball_alpha: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xa342c3a6, original_name='FPToBallAlpha', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    ball_to_fp_alpha: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x15b6840d, original_name='BallToFPAlpha', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    fp_to_ball_alpha_multi_player: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x23fb0e93, original_name='FPToBallAlphaMultiPlayer', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    ball_to_fp_alpha_multi_player: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x564262f0, original_name='BallToFPAlphaMultiPlayer', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    movement_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x9183a262, original_name='MovementControl', from_json=Spline.from_json, to_json=Spline.to_json
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
        assert property_id == 0xd48e4124
        suit_ancs = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01e12c84
        gun_resources = TGunResources.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf24b055d
        multi_player_gun_resources = TGunResources.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa342c3a6
        fp_to_ball_alpha = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15b6840d
        ball_to_fp_alpha = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23fb0e93
        fp_to_ball_alpha_multi_player = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x564262f0
        ball_to_fp_alpha_multi_player = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9183a262
        movement_control = Spline.from_stream(data, game, property_size)
    
        return cls(suit_ancs, gun_resources, multi_player_gun_resources, fp_to_ball_alpha, ball_to_fp_alpha, fp_to_ball_alpha_multi_player, ball_to_fp_alpha_multi_player, movement_control)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'\xd4\x8eA$')  # 0xd48e4124
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.suit_ancs.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x01\xe1,\x84')  # 0x1e12c84
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.gun_resources.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf2K\x05]')  # 0xf24b055d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.multi_player_gun_resources.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa3B\xc3\xa6')  # 0xa342c3a6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fp_to_ball_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15\xb6\x84\r')  # 0x15b6840d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_to_fp_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#\xfb\x0e\x93')  # 0x23fb0e93
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fp_to_ball_alpha_multi_player.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'VBb\xf0')  # 0x564262f0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_to_fp_alpha_multi_player.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x91\x83\xa2b')  # 0x9183a262
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.movement_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TBallTransitionResourcesJson", data)
        return cls(
            suit_ancs=json_data['suit_ancs'],
            gun_resources=TGunResources.from_json(json_data['gun_resources']),
            multi_player_gun_resources=TGunResources.from_json(json_data['multi_player_gun_resources']),
            fp_to_ball_alpha=Spline.from_json(json_data['fp_to_ball_alpha']),
            ball_to_fp_alpha=Spline.from_json(json_data['ball_to_fp_alpha']),
            fp_to_ball_alpha_multi_player=Spline.from_json(json_data['fp_to_ball_alpha_multi_player']),
            ball_to_fp_alpha_multi_player=Spline.from_json(json_data['ball_to_fp_alpha_multi_player']),
            movement_control=Spline.from_json(json_data['movement_control']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'suit_ancs': self.suit_ancs,
            'gun_resources': self.gun_resources.to_json(),
            'multi_player_gun_resources': self.multi_player_gun_resources.to_json(),
            'fp_to_ball_alpha': self.fp_to_ball_alpha.to_json(),
            'ball_to_fp_alpha': self.ball_to_fp_alpha.to_json(),
            'fp_to_ball_alpha_multi_player': self.fp_to_ball_alpha_multi_player.to_json(),
            'ball_to_fp_alpha_multi_player': self.ball_to_fp_alpha_multi_player.to_json(),
            'movement_control': self.movement_control.to_json(),
        }


def _decode_suit_ancs(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_gun_resources(data: typing.BinaryIO, game: Game, property_size: int) -> TGunResources:
    return TGunResources.from_stream(data, game, property_size)


def _decode_multi_player_gun_resources(data: typing.BinaryIO, game: Game, property_size: int) -> TGunResources:
    return TGunResources.from_stream(data, game, property_size)


def _decode_fp_to_ball_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_ball_to_fp_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fp_to_ball_alpha_multi_player(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_ball_to_fp_alpha_multi_player(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_movement_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xd48e4124: ('suit_ancs', _decode_suit_ancs),
    0x01e12c84: ('gun_resources', _decode_gun_resources),
    0xf24b055d: ('multi_player_gun_resources', _decode_multi_player_gun_resources),
    0xa342c3a6: ('fp_to_ball_alpha', _decode_fp_to_ball_alpha),
    0x15b6840d: ('ball_to_fp_alpha', _decode_ball_to_fp_alpha),
    0x23fb0e93: ('fp_to_ball_alpha_multi_player', _decode_fp_to_ball_alpha_multi_player),
    0x564262f0: ('ball_to_fp_alpha_multi_player', _decode_ball_to_fp_alpha_multi_player),
    0x9183a262: ('movement_control', _decode_movement_control),
}
