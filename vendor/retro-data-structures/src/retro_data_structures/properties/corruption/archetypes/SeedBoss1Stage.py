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
from retro_data_structures.properties.corruption.archetypes.SeedBoss1Action import SeedBoss1Action

if typing.TYPE_CHECKING:
    class SeedBoss1StageJson(typing_extensions.TypedDict):
        anim_playback_rate: float
        min_health_percentage: float
        min_time_between_attacks: float
        max_time_between_attacks: float
        unknown_0xcd4edca2: float
        unknown_0xf9b082b0: float
        time_before_orb_grab: float
        unknown_0x905063f4: bool
        can_stomp: bool
        can_energize: bool
        min_orb_cover_time: float
        max_orb_cover_time: float
        min_orb_cover_close_time: float
        max_orb_cover_close_time: float
        unknown_0xc31d15ee: float
        reverse_direction_chance: float
        hand_projectile: json_util.JsonObject
        breath_attack: json_util.JsonObject
        unknown_0xaf8c9223: float
        hyper_quake: json_util.JsonObject
        hyper_homing_shot: json_util.JsonObject
        charge_player: json_util.JsonObject
        unknown_0x4432c4fe: int
        unknown_0x2ac6aa4b: float
        unknown_0xdbf10d5e: float
    

@dataclasses.dataclass()
class SeedBoss1Stage(BaseProperty):
    anim_playback_rate: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b0e75b3, original_name='AnimPlaybackRate'
        ),
    })
    min_health_percentage: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdfea46b3, original_name='MinHealthPercentage'
        ),
    })
    min_time_between_attacks: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    unknown_0xcd4edca2: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd4edca2, original_name='Unknown'
        ),
    })
    unknown_0xf9b082b0: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf9b082b0, original_name='Unknown'
        ),
    })
    time_before_orb_grab: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2362c4e2, original_name='TimeBeforeOrbGrab'
        ),
    })
    unknown_0x905063f4: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x905063f4, original_name='Unknown'
        ),
    })
    can_stomp: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbae5eabb, original_name='CanStomp'
        ),
    })
    can_energize: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1e3a9394, original_name='CanEnergize'
        ),
    })
    min_orb_cover_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x40c60cfc, original_name='MinOrbCoverTime'
        ),
    })
    max_orb_cover_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x69b8f1e4, original_name='MaxOrbCoverTime'
        ),
    })
    min_orb_cover_close_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xae7dd037, original_name='MinOrbCoverCloseTime'
        ),
    })
    max_orb_cover_close_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x90c818bf, original_name='MaxOrbCoverCloseTime'
        ),
    })
    unknown_0xc31d15ee: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc31d15ee, original_name='Unknown'
        ),
    })
    reverse_direction_chance: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa059d75f, original_name='ReverseDirectionChance'
        ),
    })
    hand_projectile: SeedBoss1Action = dataclasses.field(default_factory=SeedBoss1Action, metadata={
        'reflection': FieldReflection[SeedBoss1Action](
            SeedBoss1Action, id=0x1e857439, original_name='HandProjectile', from_json=SeedBoss1Action.from_json, to_json=SeedBoss1Action.to_json
        ),
    })
    breath_attack: SeedBoss1Action = dataclasses.field(default_factory=SeedBoss1Action, metadata={
        'reflection': FieldReflection[SeedBoss1Action](
            SeedBoss1Action, id=0xbaf37baa, original_name='BreathAttack', from_json=SeedBoss1Action.from_json, to_json=SeedBoss1Action.to_json
        ),
    })
    unknown_0xaf8c9223: float = dataclasses.field(default=0.05999999865889549, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaf8c9223, original_name='Unknown'
        ),
    })
    hyper_quake: SeedBoss1Action = dataclasses.field(default_factory=SeedBoss1Action, metadata={
        'reflection': FieldReflection[SeedBoss1Action](
            SeedBoss1Action, id=0xd83d4564, original_name='HyperQuake', from_json=SeedBoss1Action.from_json, to_json=SeedBoss1Action.to_json
        ),
    })
    hyper_homing_shot: SeedBoss1Action = dataclasses.field(default_factory=SeedBoss1Action, metadata={
        'reflection': FieldReflection[SeedBoss1Action](
            SeedBoss1Action, id=0x95b6d3b7, original_name='HyperHomingShot', from_json=SeedBoss1Action.from_json, to_json=SeedBoss1Action.to_json
        ),
    })
    charge_player: SeedBoss1Action = dataclasses.field(default_factory=SeedBoss1Action, metadata={
        'reflection': FieldReflection[SeedBoss1Action](
            SeedBoss1Action, id=0x46aa8016, original_name='ChargePlayer', from_json=SeedBoss1Action.from_json, to_json=SeedBoss1Action.to_json
        ),
    })
    unknown_0x4432c4fe: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x4432c4fe, original_name='Unknown'
        ),
    })
    unknown_0x2ac6aa4b: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ac6aa4b, original_name='Unknown'
        ),
    })
    unknown_0xdbf10d5e: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdbf10d5e, original_name='Unknown'
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
        if property_count != 25:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b0e75b3
        anim_playback_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfea46b3
        min_health_percentage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e7a2c2
        min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ba1c18
        max_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd4edca2
        unknown_0xcd4edca2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9b082b0
        unknown_0xf9b082b0 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2362c4e2
        time_before_orb_grab = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x905063f4
        unknown_0x905063f4 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbae5eabb
        can_stomp = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e3a9394
        can_energize = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40c60cfc
        min_orb_cover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69b8f1e4
        max_orb_cover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae7dd037
        min_orb_cover_close_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90c818bf
        max_orb_cover_close_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc31d15ee
        unknown_0xc31d15ee = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa059d75f
        reverse_direction_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e857439
        hand_projectile = SeedBoss1Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbaf37baa
        breath_attack = SeedBoss1Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf8c9223
        unknown_0xaf8c9223 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd83d4564
        hyper_quake = SeedBoss1Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95b6d3b7
        hyper_homing_shot = SeedBoss1Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46aa8016
        charge_player = SeedBoss1Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4432c4fe
        unknown_0x4432c4fe = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ac6aa4b
        unknown_0x2ac6aa4b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdbf10d5e
        unknown_0xdbf10d5e = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(anim_playback_rate, min_health_percentage, min_time_between_attacks, max_time_between_attacks, unknown_0xcd4edca2, unknown_0xf9b082b0, time_before_orb_grab, unknown_0x905063f4, can_stomp, can_energize, min_orb_cover_time, max_orb_cover_time, min_orb_cover_close_time, max_orb_cover_close_time, unknown_0xc31d15ee, reverse_direction_chance, hand_projectile, breath_attack, unknown_0xaf8c9223, hyper_quake, hyper_homing_shot, charge_player, unknown_0x4432c4fe, unknown_0x2ac6aa4b, unknown_0xdbf10d5e)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x19')  # 25 properties

        data.write(b'\x1b\x0eu\xb3')  # 0x1b0e75b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.anim_playback_rate))

        data.write(b'\xdf\xeaF\xb3')  # 0xdfea46b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_health_percentage))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'\xcdN\xdc\xa2')  # 0xcd4edca2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd4edca2))

        data.write(b'\xf9\xb0\x82\xb0')  # 0xf9b082b0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf9b082b0))

        data.write(b'#b\xc4\xe2')  # 0x2362c4e2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_before_orb_grab))

        data.write(b'\x90Pc\xf4')  # 0x905063f4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x905063f4))

        data.write(b'\xba\xe5\xea\xbb')  # 0xbae5eabb
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_stomp))

        data.write(b'\x1e:\x93\x94')  # 0x1e3a9394
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_energize))

        data.write(b'@\xc6\x0c\xfc')  # 0x40c60cfc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_orb_cover_time))

        data.write(b'i\xb8\xf1\xe4')  # 0x69b8f1e4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_orb_cover_time))

        data.write(b'\xae}\xd07')  # 0xae7dd037
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_orb_cover_close_time))

        data.write(b'\x90\xc8\x18\xbf')  # 0x90c818bf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_orb_cover_close_time))

        data.write(b'\xc3\x1d\x15\xee')  # 0xc31d15ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc31d15ee))

        data.write(b'\xa0Y\xd7_')  # 0xa059d75f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverse_direction_chance))

        data.write(b'\x1e\x85t9')  # 0x1e857439
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hand_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xba\xf3{\xaa')  # 0xbaf37baa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.breath_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xaf\x8c\x92#')  # 0xaf8c9223
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xaf8c9223))

        data.write(b'\xd8=Ed')  # 0xd83d4564
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_quake.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x95\xb6\xd3\xb7')  # 0x95b6d3b7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_homing_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'F\xaa\x80\x16')  # 0x46aa8016
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_player.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'D2\xc4\xfe')  # 0x4432c4fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x4432c4fe))

        data.write(b'*\xc6\xaaK')  # 0x2ac6aa4b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2ac6aa4b))

        data.write(b'\xdb\xf1\r^')  # 0xdbf10d5e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdbf10d5e))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss1StageJson", data)
        return cls(
            anim_playback_rate=json_data['anim_playback_rate'],
            min_health_percentage=json_data['min_health_percentage'],
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            unknown_0xcd4edca2=json_data['unknown_0xcd4edca2'],
            unknown_0xf9b082b0=json_data['unknown_0xf9b082b0'],
            time_before_orb_grab=json_data['time_before_orb_grab'],
            unknown_0x905063f4=json_data['unknown_0x905063f4'],
            can_stomp=json_data['can_stomp'],
            can_energize=json_data['can_energize'],
            min_orb_cover_time=json_data['min_orb_cover_time'],
            max_orb_cover_time=json_data['max_orb_cover_time'],
            min_orb_cover_close_time=json_data['min_orb_cover_close_time'],
            max_orb_cover_close_time=json_data['max_orb_cover_close_time'],
            unknown_0xc31d15ee=json_data['unknown_0xc31d15ee'],
            reverse_direction_chance=json_data['reverse_direction_chance'],
            hand_projectile=SeedBoss1Action.from_json(json_data['hand_projectile']),
            breath_attack=SeedBoss1Action.from_json(json_data['breath_attack']),
            unknown_0xaf8c9223=json_data['unknown_0xaf8c9223'],
            hyper_quake=SeedBoss1Action.from_json(json_data['hyper_quake']),
            hyper_homing_shot=SeedBoss1Action.from_json(json_data['hyper_homing_shot']),
            charge_player=SeedBoss1Action.from_json(json_data['charge_player']),
            unknown_0x4432c4fe=json_data['unknown_0x4432c4fe'],
            unknown_0x2ac6aa4b=json_data['unknown_0x2ac6aa4b'],
            unknown_0xdbf10d5e=json_data['unknown_0xdbf10d5e'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'anim_playback_rate': self.anim_playback_rate,
            'min_health_percentage': self.min_health_percentage,
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'unknown_0xcd4edca2': self.unknown_0xcd4edca2,
            'unknown_0xf9b082b0': self.unknown_0xf9b082b0,
            'time_before_orb_grab': self.time_before_orb_grab,
            'unknown_0x905063f4': self.unknown_0x905063f4,
            'can_stomp': self.can_stomp,
            'can_energize': self.can_energize,
            'min_orb_cover_time': self.min_orb_cover_time,
            'max_orb_cover_time': self.max_orb_cover_time,
            'min_orb_cover_close_time': self.min_orb_cover_close_time,
            'max_orb_cover_close_time': self.max_orb_cover_close_time,
            'unknown_0xc31d15ee': self.unknown_0xc31d15ee,
            'reverse_direction_chance': self.reverse_direction_chance,
            'hand_projectile': self.hand_projectile.to_json(),
            'breath_attack': self.breath_attack.to_json(),
            'unknown_0xaf8c9223': self.unknown_0xaf8c9223,
            'hyper_quake': self.hyper_quake.to_json(),
            'hyper_homing_shot': self.hyper_homing_shot.to_json(),
            'charge_player': self.charge_player.to_json(),
            'unknown_0x4432c4fe': self.unknown_0x4432c4fe,
            'unknown_0x2ac6aa4b': self.unknown_0x2ac6aa4b,
            'unknown_0xdbf10d5e': self.unknown_0xdbf10d5e,
        }


def _decode_hand_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Action:
    return SeedBoss1Action.from_stream(data, game, property_size)


def _decode_breath_attack(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Action:
    return SeedBoss1Action.from_stream(data, game, property_size)


def _decode_hyper_quake(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Action:
    return SeedBoss1Action.from_stream(data, game, property_size)


def _decode_hyper_homing_shot(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Action:
    return SeedBoss1Action.from_stream(data, game, property_size)


def _decode_charge_player(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Action:
    return SeedBoss1Action.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1b0e75b3: ('anim_playback_rate', structs.decode_BIG_f),
    0xdfea46b3: ('min_health_percentage', structs.decode_BIG_f),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0xcd4edca2: ('unknown_0xcd4edca2', structs.decode_BIG_f),
    0xf9b082b0: ('unknown_0xf9b082b0', structs.decode_BIG_f),
    0x2362c4e2: ('time_before_orb_grab', structs.decode_BIG_f),
    0x905063f4: ('unknown_0x905063f4', structs.decode_BIG_bool_),
    0xbae5eabb: ('can_stomp', structs.decode_BIG_bool_),
    0x1e3a9394: ('can_energize', structs.decode_BIG_bool_),
    0x40c60cfc: ('min_orb_cover_time', structs.decode_BIG_f),
    0x69b8f1e4: ('max_orb_cover_time', structs.decode_BIG_f),
    0xae7dd037: ('min_orb_cover_close_time', structs.decode_BIG_f),
    0x90c818bf: ('max_orb_cover_close_time', structs.decode_BIG_f),
    0xc31d15ee: ('unknown_0xc31d15ee', structs.decode_BIG_f),
    0xa059d75f: ('reverse_direction_chance', structs.decode_BIG_f),
    0x1e857439: ('hand_projectile', _decode_hand_projectile),
    0xbaf37baa: ('breath_attack', _decode_breath_attack),
    0xaf8c9223: ('unknown_0xaf8c9223', structs.decode_BIG_f),
    0xd83d4564: ('hyper_quake', _decode_hyper_quake),
    0x95b6d3b7: ('hyper_homing_shot', _decode_hyper_homing_shot),
    0x46aa8016: ('charge_player', _decode_charge_player),
    0x4432c4fe: ('unknown_0x4432c4fe', structs.decode_BIG_l),
    0x2ac6aa4b: ('unknown_0x2ac6aa4b', structs.decode_BIG_f),
    0xdbf10d5e: ('unknown_0xdbf10d5e', structs.decode_BIG_f),
}
