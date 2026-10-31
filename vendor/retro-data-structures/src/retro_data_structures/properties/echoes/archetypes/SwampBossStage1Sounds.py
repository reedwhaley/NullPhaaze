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
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SwampBossStage1SoundsJson(typing_extensions.TypedDict):
        tongue_out_one_shot: json_util.JsonObject
        tongue_retract_loop: json_util.JsonObject
        tongue_hit_player_one_shot: json_util.JsonObject
        tongue_pull_player_loop: json_util.JsonObject
        weak_spot_hit_small_one_shot: json_util.JsonObject
        weak_spot_hit_large_one_shot: json_util.JsonObject
        pain_sound_one_shot: json_util.JsonObject
        pain_sound_damage_threshold: float
        telegraph_loop: json_util.JsonObject
        shock_wave_volumetric_loop: json_util.JsonObject
    

@dataclasses.dataclass()
class SwampBossStage1Sounds(BaseProperty):
    tongue_out_one_shot: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x4f904909, original_name='TongueOut_OneShot', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    tongue_retract_loop: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x82e108de, original_name='TongueRetract_Loop', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    tongue_hit_player_one_shot: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xdf090545, original_name='TongueHitPlayer_OneShot', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    tongue_pull_player_loop: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x3dd5b3cf, original_name='TonguePullPlayer_Loop', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    weak_spot_hit_small_one_shot: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xf82231bb, original_name='WeakSpotHitSmall_OneShot', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    weak_spot_hit_large_one_shot: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x009e3658, original_name='WeakSpotHitLarge_OneShot', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    pain_sound_one_shot: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x62bd75b1, original_name='PainSound_OneShot', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    pain_sound_damage_threshold: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7714baec, original_name='PainSoundDamageThreshold'
        ),
    })
    telegraph_loop: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x32969cba, original_name='Telegraph_Loop', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    shock_wave_volumetric_loop: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x597d2ac9, original_name='ShockWaveVolumetric_Loop', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
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
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f904909
        tongue_out_one_shot = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82e108de
        tongue_retract_loop = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf090545
        tongue_hit_player_one_shot = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3dd5b3cf
        tongue_pull_player_loop = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf82231bb
        weak_spot_hit_small_one_shot = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x009e3658
        weak_spot_hit_large_one_shot = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62bd75b1
        pain_sound_one_shot = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7714baec
        pain_sound_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32969cba
        telegraph_loop = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x597d2ac9
        shock_wave_volumetric_loop = AudioPlaybackParms.from_stream(data, game, property_size)
    
        return cls(tongue_out_one_shot, tongue_retract_loop, tongue_hit_player_one_shot, tongue_pull_player_loop, weak_spot_hit_small_one_shot, weak_spot_hit_large_one_shot, pain_sound_one_shot, pain_sound_damage_threshold, telegraph_loop, shock_wave_volumetric_loop)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'O\x90I\t')  # 0x4f904909
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tongue_out_one_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x82\xe1\x08\xde')  # 0x82e108de
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tongue_retract_loop.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdf\t\x05E')  # 0xdf090545
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tongue_hit_player_one_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'=\xd5\xb3\xcf')  # 0x3dd5b3cf
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tongue_pull_player_loop.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf8"1\xbb')  # 0xf82231bb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weak_spot_hit_small_one_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x00\x9e6X')  # 0x9e3658
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weak_spot_hit_large_one_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'b\xbdu\xb1')  # 0x62bd75b1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pain_sound_one_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'w\x14\xba\xec')  # 0x7714baec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pain_sound_damage_threshold))

        data.write(b'2\x96\x9c\xba')  # 0x32969cba
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.telegraph_loop.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Y}*\xc9')  # 0x597d2ac9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shock_wave_volumetric_loop.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwampBossStage1SoundsJson", data)
        return cls(
            tongue_out_one_shot=AudioPlaybackParms.from_json(json_data['tongue_out_one_shot']),
            tongue_retract_loop=AudioPlaybackParms.from_json(json_data['tongue_retract_loop']),
            tongue_hit_player_one_shot=AudioPlaybackParms.from_json(json_data['tongue_hit_player_one_shot']),
            tongue_pull_player_loop=AudioPlaybackParms.from_json(json_data['tongue_pull_player_loop']),
            weak_spot_hit_small_one_shot=AudioPlaybackParms.from_json(json_data['weak_spot_hit_small_one_shot']),
            weak_spot_hit_large_one_shot=AudioPlaybackParms.from_json(json_data['weak_spot_hit_large_one_shot']),
            pain_sound_one_shot=AudioPlaybackParms.from_json(json_data['pain_sound_one_shot']),
            pain_sound_damage_threshold=json_data['pain_sound_damage_threshold'],
            telegraph_loop=AudioPlaybackParms.from_json(json_data['telegraph_loop']),
            shock_wave_volumetric_loop=AudioPlaybackParms.from_json(json_data['shock_wave_volumetric_loop']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'tongue_out_one_shot': self.tongue_out_one_shot.to_json(),
            'tongue_retract_loop': self.tongue_retract_loop.to_json(),
            'tongue_hit_player_one_shot': self.tongue_hit_player_one_shot.to_json(),
            'tongue_pull_player_loop': self.tongue_pull_player_loop.to_json(),
            'weak_spot_hit_small_one_shot': self.weak_spot_hit_small_one_shot.to_json(),
            'weak_spot_hit_large_one_shot': self.weak_spot_hit_large_one_shot.to_json(),
            'pain_sound_one_shot': self.pain_sound_one_shot.to_json(),
            'pain_sound_damage_threshold': self.pain_sound_damage_threshold,
            'telegraph_loop': self.telegraph_loop.to_json(),
            'shock_wave_volumetric_loop': self.shock_wave_volumetric_loop.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.tongue_out_one_shot.dependencies_for, "tongue_out_one_shot", "AudioPlaybackParms"),
            (self.tongue_retract_loop.dependencies_for, "tongue_retract_loop", "AudioPlaybackParms"),
            (self.tongue_hit_player_one_shot.dependencies_for, "tongue_hit_player_one_shot", "AudioPlaybackParms"),
            (self.tongue_pull_player_loop.dependencies_for, "tongue_pull_player_loop", "AudioPlaybackParms"),
            (self.weak_spot_hit_small_one_shot.dependencies_for, "weak_spot_hit_small_one_shot", "AudioPlaybackParms"),
            (self.weak_spot_hit_large_one_shot.dependencies_for, "weak_spot_hit_large_one_shot", "AudioPlaybackParms"),
            (self.pain_sound_one_shot.dependencies_for, "pain_sound_one_shot", "AudioPlaybackParms"),
            (self.telegraph_loop.dependencies_for, "telegraph_loop", "AudioPlaybackParms"),
            (self.shock_wave_volumetric_loop.dependencies_for, "shock_wave_volumetric_loop", "AudioPlaybackParms"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SwampBossStage1Sounds.{field_name} ({field_type}): {e}"
                )


def _decode_tongue_out_one_shot(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_tongue_retract_loop(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_tongue_hit_player_one_shot(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_tongue_pull_player_loop(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_weak_spot_hit_small_one_shot(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_weak_spot_hit_large_one_shot(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_pain_sound_one_shot(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_telegraph_loop(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_shock_wave_volumetric_loop(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4f904909: ('tongue_out_one_shot', _decode_tongue_out_one_shot),
    0x82e108de: ('tongue_retract_loop', _decode_tongue_retract_loop),
    0xdf090545: ('tongue_hit_player_one_shot', _decode_tongue_hit_player_one_shot),
    0x3dd5b3cf: ('tongue_pull_player_loop', _decode_tongue_pull_player_loop),
    0xf82231bb: ('weak_spot_hit_small_one_shot', _decode_weak_spot_hit_small_one_shot),
    0x009e3658: ('weak_spot_hit_large_one_shot', _decode_weak_spot_hit_large_one_shot),
    0x62bd75b1: ('pain_sound_one_shot', _decode_pain_sound_one_shot),
    0x7714baec: ('pain_sound_damage_threshold', structs.decode_BIG_f),
    0x32969cba: ('telegraph_loop', _decode_telegraph_loop),
    0x597d2ac9: ('shock_wave_volumetric_loop', _decode_shock_wave_volumetric_loop),
}
