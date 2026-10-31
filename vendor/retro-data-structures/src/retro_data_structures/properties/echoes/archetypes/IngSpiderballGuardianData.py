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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.IngSpiderballGuardianPuzzleData import IngSpiderballGuardianPuzzleData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class IngSpiderballGuardianDataJson(typing_extensions.TypedDict):
        puzzle1_properties: json_util.JsonObject
        puzzle2_properties: json_util.JsonObject
        puzzle3_properties: json_util.JsonObject
        puzzle4_properties: json_util.JsonObject
        puzzle5_properties: json_util.JsonObject
        puzzle6_properties: json_util.JsonObject
        damage_radius: float
        proximity_damage: json_util.JsonObject
        unknown: float
        audio_playback_parms_0xaed23abc: json_util.JsonObject
        sound_spiderball_rolling: json_util.JsonObject
        sound_spiderball_slow_rolling: json_util.JsonObject
        sound_spiderball_fast_rolling: json_util.JsonObject
        sound_enter_stunned: json_util.JsonObject
        audio_playback_parms_0x44c1f241: json_util.JsonObject
    

@dataclasses.dataclass()
class IngSpiderballGuardianData(BaseProperty):
    puzzle1_properties: IngSpiderballGuardianPuzzleData = dataclasses.field(default_factory=IngSpiderballGuardianPuzzleData, metadata={
        'reflection': FieldReflection[IngSpiderballGuardianPuzzleData](
            IngSpiderballGuardianPuzzleData, id=0x152db484, original_name='Puzzle1Properties', from_json=IngSpiderballGuardianPuzzleData.from_json, to_json=IngSpiderballGuardianPuzzleData.to_json
        ),
    })
    puzzle2_properties: IngSpiderballGuardianPuzzleData = dataclasses.field(default_factory=IngSpiderballGuardianPuzzleData, metadata={
        'reflection': FieldReflection[IngSpiderballGuardianPuzzleData](
            IngSpiderballGuardianPuzzleData, id=0x2d163ff7, original_name='Puzzle2Properties', from_json=IngSpiderballGuardianPuzzleData.from_json, to_json=IngSpiderballGuardianPuzzleData.to_json
        ),
    })
    puzzle3_properties: IngSpiderballGuardianPuzzleData = dataclasses.field(default_factory=IngSpiderballGuardianPuzzleData, metadata={
        'reflection': FieldReflection[IngSpiderballGuardianPuzzleData](
            IngSpiderballGuardianPuzzleData, id=0x8c2fbb19, original_name='Puzzle3Properties', from_json=IngSpiderballGuardianPuzzleData.from_json, to_json=IngSpiderballGuardianPuzzleData.to_json
        ),
    })
    puzzle4_properties: IngSpiderballGuardianPuzzleData = dataclasses.field(default_factory=IngSpiderballGuardianPuzzleData, metadata={
        'reflection': FieldReflection[IngSpiderballGuardianPuzzleData](
            IngSpiderballGuardianPuzzleData, id=0x5d612911, original_name='Puzzle4Properties', from_json=IngSpiderballGuardianPuzzleData.from_json, to_json=IngSpiderballGuardianPuzzleData.to_json
        ),
    })
    puzzle5_properties: IngSpiderballGuardianPuzzleData = dataclasses.field(default_factory=IngSpiderballGuardianPuzzleData, metadata={
        'reflection': FieldReflection[IngSpiderballGuardianPuzzleData](
            IngSpiderballGuardianPuzzleData, id=0xfc58adff, original_name='Puzzle5Properties', from_json=IngSpiderballGuardianPuzzleData.from_json, to_json=IngSpiderballGuardianPuzzleData.to_json
        ),
    })
    puzzle6_properties: IngSpiderballGuardianPuzzleData = dataclasses.field(default_factory=IngSpiderballGuardianPuzzleData, metadata={
        'reflection': FieldReflection[IngSpiderballGuardianPuzzleData](
            IngSpiderballGuardianPuzzleData, id=0xc463268c, original_name='Puzzle6Properties', from_json=IngSpiderballGuardianPuzzleData.from_json, to_json=IngSpiderballGuardianPuzzleData.to_json
        ),
    })
    damage_radius: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0f598739, original_name='DamageRadius'
        ),
    })
    proximity_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xba78d281, original_name='ProximityDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x32133b39, original_name='Unknown'
        ),
    })
    audio_playback_parms_0xaed23abc: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xaed23abc, original_name='AudioPlaybackParms', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_spiderball_rolling: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x3a5e2f52, original_name='Sound_SpiderballRolling', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_spiderball_slow_rolling: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xcee38f10, original_name='Sound_SpiderballSlowRolling', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_spiderball_fast_rolling: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x796fa303, original_name='Sound_SpiderballFastRolling', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_enter_stunned: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xd5f3e9c4, original_name='Sound_EnterStunned', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    audio_playback_parms_0x44c1f241: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x44c1f241, original_name='AudioPlaybackParms', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
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
        if property_count != 15:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x152db484
        puzzle1_properties = IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2d163ff7
        puzzle2_properties = IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8c2fbb19
        puzzle3_properties = IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d612911
        puzzle4_properties = IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc58adff
        puzzle5_properties = IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc463268c
        puzzle6_properties = IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f598739
        damage_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba78d281
        proximity_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 40.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32133b39
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaed23abc
        audio_playback_parms_0xaed23abc = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3a5e2f52
        sound_spiderball_rolling = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcee38f10
        sound_spiderball_slow_rolling = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x796fa303
        sound_spiderball_fast_rolling = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5f3e9c4
        sound_enter_stunned = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44c1f241
        audio_playback_parms_0x44c1f241 = AudioPlaybackParms.from_stream(data, game, property_size)
    
        return cls(puzzle1_properties, puzzle2_properties, puzzle3_properties, puzzle4_properties, puzzle5_properties, puzzle6_properties, damage_radius, proximity_damage, unknown, audio_playback_parms_0xaed23abc, sound_spiderball_rolling, sound_spiderball_slow_rolling, sound_spiderball_fast_rolling, sound_enter_stunned, audio_playback_parms_0x44c1f241)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0f')  # 15 properties

        data.write(b'\x15-\xb4\x84')  # 0x152db484
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.puzzle1_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'-\x16?\xf7')  # 0x2d163ff7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.puzzle2_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8c/\xbb\x19')  # 0x8c2fbb19
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.puzzle3_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b']a)\x11')  # 0x5d612911
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.puzzle4_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfcX\xad\xff')  # 0xfc58adff
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.puzzle5_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc4c&\x8c')  # 0xc463268c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.puzzle6_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0fY\x879')  # 0xf598739
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_radius))

        data.write(b'\xbax\xd2\x81')  # 0xba78d281
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.proximity_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 40.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'2\x13;9')  # 0x32133b39
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\xae\xd2:\xbc')  # 0xaed23abc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.audio_playback_parms_0xaed23abc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b':^/R')  # 0x3a5e2f52
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_spiderball_rolling.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xce\xe3\x8f\x10')  # 0xcee38f10
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_spiderball_slow_rolling.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'yo\xa3\x03')  # 0x796fa303
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_spiderball_fast_rolling.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd5\xf3\xe9\xc4')  # 0xd5f3e9c4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_enter_stunned.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'D\xc1\xf2A')  # 0x44c1f241
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.audio_playback_parms_0x44c1f241.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("IngSpiderballGuardianDataJson", data)
        return cls(
            puzzle1_properties=IngSpiderballGuardianPuzzleData.from_json(json_data['puzzle1_properties']),
            puzzle2_properties=IngSpiderballGuardianPuzzleData.from_json(json_data['puzzle2_properties']),
            puzzle3_properties=IngSpiderballGuardianPuzzleData.from_json(json_data['puzzle3_properties']),
            puzzle4_properties=IngSpiderballGuardianPuzzleData.from_json(json_data['puzzle4_properties']),
            puzzle5_properties=IngSpiderballGuardianPuzzleData.from_json(json_data['puzzle5_properties']),
            puzzle6_properties=IngSpiderballGuardianPuzzleData.from_json(json_data['puzzle6_properties']),
            damage_radius=json_data['damage_radius'],
            proximity_damage=DamageInfo.from_json(json_data['proximity_damage']),
            unknown=json_data['unknown'],
            audio_playback_parms_0xaed23abc=AudioPlaybackParms.from_json(json_data['audio_playback_parms_0xaed23abc']),
            sound_spiderball_rolling=AudioPlaybackParms.from_json(json_data['sound_spiderball_rolling']),
            sound_spiderball_slow_rolling=AudioPlaybackParms.from_json(json_data['sound_spiderball_slow_rolling']),
            sound_spiderball_fast_rolling=AudioPlaybackParms.from_json(json_data['sound_spiderball_fast_rolling']),
            sound_enter_stunned=AudioPlaybackParms.from_json(json_data['sound_enter_stunned']),
            audio_playback_parms_0x44c1f241=AudioPlaybackParms.from_json(json_data['audio_playback_parms_0x44c1f241']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'puzzle1_properties': self.puzzle1_properties.to_json(),
            'puzzle2_properties': self.puzzle2_properties.to_json(),
            'puzzle3_properties': self.puzzle3_properties.to_json(),
            'puzzle4_properties': self.puzzle4_properties.to_json(),
            'puzzle5_properties': self.puzzle5_properties.to_json(),
            'puzzle6_properties': self.puzzle6_properties.to_json(),
            'damage_radius': self.damage_radius,
            'proximity_damage': self.proximity_damage.to_json(),
            'unknown': self.unknown,
            'audio_playback_parms_0xaed23abc': self.audio_playback_parms_0xaed23abc.to_json(),
            'sound_spiderball_rolling': self.sound_spiderball_rolling.to_json(),
            'sound_spiderball_slow_rolling': self.sound_spiderball_slow_rolling.to_json(),
            'sound_spiderball_fast_rolling': self.sound_spiderball_fast_rolling.to_json(),
            'sound_enter_stunned': self.sound_enter_stunned.to_json(),
            'audio_playback_parms_0x44c1f241': self.audio_playback_parms_0x44c1f241.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.audio_playback_parms_0xaed23abc.dependencies_for, "audio_playback_parms_0xaed23abc", "AudioPlaybackParms"),
            (self.sound_spiderball_rolling.dependencies_for, "sound_spiderball_rolling", "AudioPlaybackParms"),
            (self.sound_spiderball_slow_rolling.dependencies_for, "sound_spiderball_slow_rolling", "AudioPlaybackParms"),
            (self.sound_spiderball_fast_rolling.dependencies_for, "sound_spiderball_fast_rolling", "AudioPlaybackParms"),
            (self.sound_enter_stunned.dependencies_for, "sound_enter_stunned", "AudioPlaybackParms"),
            (self.audio_playback_parms_0x44c1f241.dependencies_for, "audio_playback_parms_0x44c1f241", "AudioPlaybackParms"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for IngSpiderballGuardianData.{field_name} ({field_type}): {e}"
                )


def _decode_puzzle1_properties(data: typing.BinaryIO, game: Game, property_size: int) -> IngSpiderballGuardianPuzzleData:
    return IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)


def _decode_puzzle2_properties(data: typing.BinaryIO, game: Game, property_size: int) -> IngSpiderballGuardianPuzzleData:
    return IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)


def _decode_puzzle3_properties(data: typing.BinaryIO, game: Game, property_size: int) -> IngSpiderballGuardianPuzzleData:
    return IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)


def _decode_puzzle4_properties(data: typing.BinaryIO, game: Game, property_size: int) -> IngSpiderballGuardianPuzzleData:
    return IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)


def _decode_puzzle5_properties(data: typing.BinaryIO, game: Game, property_size: int) -> IngSpiderballGuardianPuzzleData:
    return IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)


def _decode_puzzle6_properties(data: typing.BinaryIO, game: Game, property_size: int) -> IngSpiderballGuardianPuzzleData:
    return IngSpiderballGuardianPuzzleData.from_stream(data, game, property_size)


def _decode_proximity_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 40.0, 'di_knock_back_power': 10.0})


def _decode_audio_playback_parms_0xaed23abc(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_spiderball_rolling(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_spiderball_slow_rolling(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_spiderball_fast_rolling(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_enter_stunned(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x44c1f241(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x152db484: ('puzzle1_properties', _decode_puzzle1_properties),
    0x2d163ff7: ('puzzle2_properties', _decode_puzzle2_properties),
    0x8c2fbb19: ('puzzle3_properties', _decode_puzzle3_properties),
    0x5d612911: ('puzzle4_properties', _decode_puzzle4_properties),
    0xfc58adff: ('puzzle5_properties', _decode_puzzle5_properties),
    0xc463268c: ('puzzle6_properties', _decode_puzzle6_properties),
    0x0f598739: ('damage_radius', structs.decode_BIG_f),
    0xba78d281: ('proximity_damage', _decode_proximity_damage),
    0x32133b39: ('unknown', structs.decode_BIG_f),
    0xaed23abc: ('audio_playback_parms_0xaed23abc', _decode_audio_playback_parms_0xaed23abc),
    0x3a5e2f52: ('sound_spiderball_rolling', _decode_sound_spiderball_rolling),
    0xcee38f10: ('sound_spiderball_slow_rolling', _decode_sound_spiderball_slow_rolling),
    0x796fa303: ('sound_spiderball_fast_rolling', _decode_sound_spiderball_fast_rolling),
    0xd5f3e9c4: ('sound_enter_stunned', _decode_sound_enter_stunned),
    0x44c1f241: ('audio_playback_parms_0x44c1f241', _decode_audio_playback_parms_0x44c1f241),
}
