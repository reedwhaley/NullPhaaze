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
from retro_data_structures.properties.echoes.archetypes.DSMissiles import DSMissiles

if typing.TYPE_CHECKING:
    class DSStageInfoJson(typing_extensions.TypedDict):
        health_percent_to_exit_this_stage: float
        min_time_between_actions: float
        max_time_between_actions: float
        min_time_between_actions_when_invisible: float
        max_time_between_actions_when_invisible: float
        unknown_0xd061ff99: float
        pause_duration_min: float
        pause_duration_max: float
        chance_to_double_dash: float
        missiles: json_util.JsonObject
        unknown_0x3ff87a8c: bool
        invisible_during_this_stage: bool
        cannot_be_killed_in_this_stage: bool
        unknown_0x53fdcb5b: bool
        uses_alternate_scannable_info: bool
        unknown_0xaa85c885: bool
        pause: float
        taunt: float
        look_around: bool
        melee_attack: float
        melee_dash: float
        scatter_shot: float
        moving_scatter_shot: float
        dive_attack: float
        unknown_0xb2c1e4fa: bool
        unknown_0xf5cf3c0f: bool
        normal_missile: float
        missile_jump: float
        super_missile: float
        freeze_beam_when_invisible: float
        normal_missile_when_invisible: float
        sweep_beam: float
        boost_ball: float
        unknown_0x2d7551e6: bool
        phazon_attack: float
        phazon_enrage: float
        pissed_off_at_end_of_stage: bool
    

@dataclasses.dataclass()
class DSStageInfo(BaseProperty):
    health_percent_to_exit_this_stage: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb5af7831, original_name='HealthPercentToExitThisStage'
        ),
    })
    min_time_between_actions: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xac65eb7a, original_name='MinTimeBetweenActions'
        ),
    })
    max_time_between_actions: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f3855a0, original_name='MaxTimeBetweenActions'
        ),
    })
    min_time_between_actions_when_invisible: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x08c0b02c, original_name='MinTimeBetweenActionsWhenInvisible'
        ),
    })
    max_time_between_actions_when_invisible: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x695f68c7, original_name='MaxTimeBetweenActionsWhenInvisible'
        ),
    })
    unknown_0xd061ff99: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd061ff99, original_name='Unknown'
        ),
    })
    pause_duration_min: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x97dbd42a, original_name='PauseDurationMin'
        ),
    })
    pause_duration_max: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71bb7bcb, original_name='PauseDurationMax'
        ),
    })
    chance_to_double_dash: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb751778b, original_name='ChanceToDoubleDash'
        ),
    })
    missiles: DSMissiles = dataclasses.field(default_factory=DSMissiles, metadata={
        'reflection': FieldReflection[DSMissiles](
            DSMissiles, id=0xd6740348, original_name='Missiles', from_json=DSMissiles.from_json, to_json=DSMissiles.to_json
        ),
    })
    unknown_0x3ff87a8c: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3ff87a8c, original_name='Unknown'
        ),
    })
    invisible_during_this_stage: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x49b9936d, original_name='InvisibleDuringThisStage'
        ),
    })
    cannot_be_killed_in_this_stage: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc96b8223, original_name='CannotBeKilledInThisStage'
        ),
    })
    unknown_0x53fdcb5b: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x53fdcb5b, original_name='Unknown'
        ),
    })
    uses_alternate_scannable_info: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0d7ef013, original_name='UsesAlternateScannableInfo'
        ),
    })
    unknown_0xaa85c885: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xaa85c885, original_name='Unknown'
        ),
    })
    pause: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x80f7e605, original_name='Pause'
        ),
    })
    taunt: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x479f6a4f, original_name='Taunt'
        ),
    })
    look_around: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x778791f5, original_name='LookAround'
        ),
    })
    melee_attack: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xce4c4668, original_name='MeleeAttack'
        ),
    })
    melee_dash: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5951a03f, original_name='MeleeDash'
        ),
    })
    scatter_shot: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x94615651, original_name='ScatterShot'
        ),
    })
    moving_scatter_shot: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x94f48974, original_name='MovingScatterShot'
        ),
    })
    dive_attack: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6e40fb76, original_name='DiveAttack'
        ),
    })
    unknown_0xb2c1e4fa: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb2c1e4fa, original_name='Unknown'
        ),
    })
    unknown_0xf5cf3c0f: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf5cf3c0f, original_name='Unknown'
        ),
    })
    normal_missile: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6847efa7, original_name='NormalMissile'
        ),
    })
    missile_jump: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x083fd602, original_name='MissileJump'
        ),
    })
    super_missile: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdb21402f, original_name='SuperMissile'
        ),
    })
    freeze_beam_when_invisible: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe63286eb, original_name='FreezeBeamWhenInvisible'
        ),
    })
    normal_missile_when_invisible: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4aae6186, original_name='NormalMissileWhenInvisible'
        ),
    })
    sweep_beam: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2bd1c15b, original_name='SweepBeam'
        ),
    })
    boost_ball: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb53693fa, original_name='BoostBall'
        ),
    })
    unknown_0x2d7551e6: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2d7551e6, original_name='Unknown'
        ),
    })
    phazon_attack: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x93a876f3, original_name='PhazonAttack'
        ),
    })
    phazon_enrage: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaea228b9, original_name='PhazonEnrage'
        ),
    })
    pissed_off_at_end_of_stage: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x911a2476, original_name='PissedOffAtEndOfStage'
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
        if property_count != 37:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5af7831
        health_percent_to_exit_this_stage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac65eb7a
        min_time_between_actions = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f3855a0
        max_time_between_actions = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08c0b02c
        min_time_between_actions_when_invisible = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x695f68c7
        max_time_between_actions_when_invisible = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd061ff99
        unknown_0xd061ff99 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97dbd42a
        pause_duration_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71bb7bcb
        pause_duration_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb751778b
        chance_to_double_dash = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6740348
        missiles = DSMissiles.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ff87a8c
        unknown_0x3ff87a8c = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49b9936d
        invisible_during_this_stage = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc96b8223
        cannot_be_killed_in_this_stage = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53fdcb5b
        unknown_0x53fdcb5b = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d7ef013
        uses_alternate_scannable_info = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa85c885
        unknown_0xaa85c885 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80f7e605
        pause = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x479f6a4f
        taunt = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x778791f5
        look_around = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce4c4668
        melee_attack = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5951a03f
        melee_dash = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94615651
        scatter_shot = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94f48974
        moving_scatter_shot = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e40fb76
        dive_attack = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb2c1e4fa
        unknown_0xb2c1e4fa = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5cf3c0f
        unknown_0xf5cf3c0f = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6847efa7
        normal_missile = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x083fd602
        missile_jump = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdb21402f
        super_missile = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe63286eb
        freeze_beam_when_invisible = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4aae6186
        normal_missile_when_invisible = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2bd1c15b
        sweep_beam = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb53693fa
        boost_ball = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2d7551e6
        unknown_0x2d7551e6 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93a876f3
        phazon_attack = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaea228b9
        phazon_enrage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x911a2476
        pissed_off_at_end_of_stage = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(health_percent_to_exit_this_stage, min_time_between_actions, max_time_between_actions, min_time_between_actions_when_invisible, max_time_between_actions_when_invisible, unknown_0xd061ff99, pause_duration_min, pause_duration_max, chance_to_double_dash, missiles, unknown_0x3ff87a8c, invisible_during_this_stage, cannot_be_killed_in_this_stage, unknown_0x53fdcb5b, uses_alternate_scannable_info, unknown_0xaa85c885, pause, taunt, look_around, melee_attack, melee_dash, scatter_shot, moving_scatter_shot, dive_attack, unknown_0xb2c1e4fa, unknown_0xf5cf3c0f, normal_missile, missile_jump, super_missile, freeze_beam_when_invisible, normal_missile_when_invisible, sweep_beam, boost_ball, unknown_0x2d7551e6, phazon_attack, phazon_enrage, pissed_off_at_end_of_stage)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00%')  # 37 properties

        data.write(b'\xb5\xafx1')  # 0xb5af7831
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.health_percent_to_exit_this_stage))

        data.write(b'\xace\xebz')  # 0xac65eb7a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_actions))

        data.write(b'O8U\xa0')  # 0x4f3855a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_actions))

        data.write(b'\x08\xc0\xb0,')  # 0x8c0b02c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_actions_when_invisible))

        data.write(b'i_h\xc7')  # 0x695f68c7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_actions_when_invisible))

        data.write(b'\xd0a\xff\x99')  # 0xd061ff99
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd061ff99))

        data.write(b'\x97\xdb\xd4*')  # 0x97dbd42a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pause_duration_min))

        data.write(b'q\xbb{\xcb')  # 0x71bb7bcb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pause_duration_max))

        data.write(b'\xb7Qw\x8b')  # 0xb751778b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chance_to_double_dash))

        data.write(b'\xd6t\x03H')  # 0xd6740348
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.missiles.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'?\xf8z\x8c')  # 0x3ff87a8c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x3ff87a8c))

        data.write(b'I\xb9\x93m')  # 0x49b9936d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.invisible_during_this_stage))

        data.write(b'\xc9k\x82#')  # 0xc96b8223
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.cannot_be_killed_in_this_stage))

        data.write(b'S\xfd\xcb[')  # 0x53fdcb5b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x53fdcb5b))

        data.write(b'\r~\xf0\x13')  # 0xd7ef013
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.uses_alternate_scannable_info))

        data.write(b'\xaa\x85\xc8\x85')  # 0xaa85c885
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xaa85c885))

        data.write(b'\x80\xf7\xe6\x05')  # 0x80f7e605
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pause))

        data.write(b'G\x9fjO')  # 0x479f6a4f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.taunt))

        data.write(b'w\x87\x91\xf5')  # 0x778791f5
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.look_around))

        data.write(b'\xceLFh')  # 0xce4c4668
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_attack))

        data.write(b'YQ\xa0?')  # 0x5951a03f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_dash))

        data.write(b'\x94aVQ')  # 0x94615651
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scatter_shot))

        data.write(b'\x94\xf4\x89t')  # 0x94f48974
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.moving_scatter_shot))

        data.write(b'n@\xfbv')  # 0x6e40fb76
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dive_attack))

        data.write(b'\xb2\xc1\xe4\xfa')  # 0xb2c1e4fa
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xb2c1e4fa))

        data.write(b'\xf5\xcf<\x0f')  # 0xf5cf3c0f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf5cf3c0f))

        data.write(b'hG\xef\xa7')  # 0x6847efa7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_missile))

        data.write(b'\x08?\xd6\x02')  # 0x83fd602
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_jump))

        data.write(b'\xdb!@/')  # 0xdb21402f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.super_missile))

        data.write(b'\xe62\x86\xeb')  # 0xe63286eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.freeze_beam_when_invisible))

        data.write(b'J\xaea\x86')  # 0x4aae6186
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_missile_when_invisible))

        data.write(b'+\xd1\xc1[')  # 0x2bd1c15b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.sweep_beam))

        data.write(b'\xb56\x93\xfa')  # 0xb53693fa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.boost_ball))

        data.write(b'-uQ\xe6')  # 0x2d7551e6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2d7551e6))

        data.write(b'\x93\xa8v\xf3')  # 0x93a876f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_attack))

        data.write(b'\xae\xa2(\xb9')  # 0xaea228b9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_enrage))

        data.write(b'\x91\x1a$v')  # 0x911a2476
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.pissed_off_at_end_of_stage))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DSStageInfoJson", data)
        return cls(
            health_percent_to_exit_this_stage=json_data['health_percent_to_exit_this_stage'],
            min_time_between_actions=json_data['min_time_between_actions'],
            max_time_between_actions=json_data['max_time_between_actions'],
            min_time_between_actions_when_invisible=json_data['min_time_between_actions_when_invisible'],
            max_time_between_actions_when_invisible=json_data['max_time_between_actions_when_invisible'],
            unknown_0xd061ff99=json_data['unknown_0xd061ff99'],
            pause_duration_min=json_data['pause_duration_min'],
            pause_duration_max=json_data['pause_duration_max'],
            chance_to_double_dash=json_data['chance_to_double_dash'],
            missiles=DSMissiles.from_json(json_data['missiles']),
            unknown_0x3ff87a8c=json_data['unknown_0x3ff87a8c'],
            invisible_during_this_stage=json_data['invisible_during_this_stage'],
            cannot_be_killed_in_this_stage=json_data['cannot_be_killed_in_this_stage'],
            unknown_0x53fdcb5b=json_data['unknown_0x53fdcb5b'],
            uses_alternate_scannable_info=json_data['uses_alternate_scannable_info'],
            unknown_0xaa85c885=json_data['unknown_0xaa85c885'],
            pause=json_data['pause'],
            taunt=json_data['taunt'],
            look_around=json_data['look_around'],
            melee_attack=json_data['melee_attack'],
            melee_dash=json_data['melee_dash'],
            scatter_shot=json_data['scatter_shot'],
            moving_scatter_shot=json_data['moving_scatter_shot'],
            dive_attack=json_data['dive_attack'],
            unknown_0xb2c1e4fa=json_data['unknown_0xb2c1e4fa'],
            unknown_0xf5cf3c0f=json_data['unknown_0xf5cf3c0f'],
            normal_missile=json_data['normal_missile'],
            missile_jump=json_data['missile_jump'],
            super_missile=json_data['super_missile'],
            freeze_beam_when_invisible=json_data['freeze_beam_when_invisible'],
            normal_missile_when_invisible=json_data['normal_missile_when_invisible'],
            sweep_beam=json_data['sweep_beam'],
            boost_ball=json_data['boost_ball'],
            unknown_0x2d7551e6=json_data['unknown_0x2d7551e6'],
            phazon_attack=json_data['phazon_attack'],
            phazon_enrage=json_data['phazon_enrage'],
            pissed_off_at_end_of_stage=json_data['pissed_off_at_end_of_stage'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'health_percent_to_exit_this_stage': self.health_percent_to_exit_this_stage,
            'min_time_between_actions': self.min_time_between_actions,
            'max_time_between_actions': self.max_time_between_actions,
            'min_time_between_actions_when_invisible': self.min_time_between_actions_when_invisible,
            'max_time_between_actions_when_invisible': self.max_time_between_actions_when_invisible,
            'unknown_0xd061ff99': self.unknown_0xd061ff99,
            'pause_duration_min': self.pause_duration_min,
            'pause_duration_max': self.pause_duration_max,
            'chance_to_double_dash': self.chance_to_double_dash,
            'missiles': self.missiles.to_json(),
            'unknown_0x3ff87a8c': self.unknown_0x3ff87a8c,
            'invisible_during_this_stage': self.invisible_during_this_stage,
            'cannot_be_killed_in_this_stage': self.cannot_be_killed_in_this_stage,
            'unknown_0x53fdcb5b': self.unknown_0x53fdcb5b,
            'uses_alternate_scannable_info': self.uses_alternate_scannable_info,
            'unknown_0xaa85c885': self.unknown_0xaa85c885,
            'pause': self.pause,
            'taunt': self.taunt,
            'look_around': self.look_around,
            'melee_attack': self.melee_attack,
            'melee_dash': self.melee_dash,
            'scatter_shot': self.scatter_shot,
            'moving_scatter_shot': self.moving_scatter_shot,
            'dive_attack': self.dive_attack,
            'unknown_0xb2c1e4fa': self.unknown_0xb2c1e4fa,
            'unknown_0xf5cf3c0f': self.unknown_0xf5cf3c0f,
            'normal_missile': self.normal_missile,
            'missile_jump': self.missile_jump,
            'super_missile': self.super_missile,
            'freeze_beam_when_invisible': self.freeze_beam_when_invisible,
            'normal_missile_when_invisible': self.normal_missile_when_invisible,
            'sweep_beam': self.sweep_beam,
            'boost_ball': self.boost_ball,
            'unknown_0x2d7551e6': self.unknown_0x2d7551e6,
            'phazon_attack': self.phazon_attack,
            'phazon_enrage': self.phazon_enrage,
            'pissed_off_at_end_of_stage': self.pissed_off_at_end_of_stage,
        }


def _decode_missiles(data: typing.BinaryIO, game: Game, property_size: int) -> DSMissiles:
    return DSMissiles.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb5af7831: ('health_percent_to_exit_this_stage', structs.decode_BIG_f),
    0xac65eb7a: ('min_time_between_actions', structs.decode_BIG_f),
    0x4f3855a0: ('max_time_between_actions', structs.decode_BIG_f),
    0x08c0b02c: ('min_time_between_actions_when_invisible', structs.decode_BIG_f),
    0x695f68c7: ('max_time_between_actions_when_invisible', structs.decode_BIG_f),
    0xd061ff99: ('unknown_0xd061ff99', structs.decode_BIG_f),
    0x97dbd42a: ('pause_duration_min', structs.decode_BIG_f),
    0x71bb7bcb: ('pause_duration_max', structs.decode_BIG_f),
    0xb751778b: ('chance_to_double_dash', structs.decode_BIG_f),
    0xd6740348: ('missiles', _decode_missiles),
    0x3ff87a8c: ('unknown_0x3ff87a8c', structs.decode_BIG_bool_),
    0x49b9936d: ('invisible_during_this_stage', structs.decode_BIG_bool_),
    0xc96b8223: ('cannot_be_killed_in_this_stage', structs.decode_BIG_bool_),
    0x53fdcb5b: ('unknown_0x53fdcb5b', structs.decode_BIG_bool_),
    0x0d7ef013: ('uses_alternate_scannable_info', structs.decode_BIG_bool_),
    0xaa85c885: ('unknown_0xaa85c885', structs.decode_BIG_bool_),
    0x80f7e605: ('pause', structs.decode_BIG_f),
    0x479f6a4f: ('taunt', structs.decode_BIG_f),
    0x778791f5: ('look_around', structs.decode_BIG_bool_),
    0xce4c4668: ('melee_attack', structs.decode_BIG_f),
    0x5951a03f: ('melee_dash', structs.decode_BIG_f),
    0x94615651: ('scatter_shot', structs.decode_BIG_f),
    0x94f48974: ('moving_scatter_shot', structs.decode_BIG_f),
    0x6e40fb76: ('dive_attack', structs.decode_BIG_f),
    0xb2c1e4fa: ('unknown_0xb2c1e4fa', structs.decode_BIG_bool_),
    0xf5cf3c0f: ('unknown_0xf5cf3c0f', structs.decode_BIG_bool_),
    0x6847efa7: ('normal_missile', structs.decode_BIG_f),
    0x083fd602: ('missile_jump', structs.decode_BIG_f),
    0xdb21402f: ('super_missile', structs.decode_BIG_f),
    0xe63286eb: ('freeze_beam_when_invisible', structs.decode_BIG_f),
    0x4aae6186: ('normal_missile_when_invisible', structs.decode_BIG_f),
    0x2bd1c15b: ('sweep_beam', structs.decode_BIG_f),
    0xb53693fa: ('boost_ball', structs.decode_BIG_f),
    0x2d7551e6: ('unknown_0x2d7551e6', structs.decode_BIG_bool_),
    0x93a876f3: ('phazon_attack', structs.decode_BIG_f),
    0xaea228b9: ('phazon_enrage', structs.decode_BIG_f),
    0x911a2476: ('pissed_off_at_end_of_stage', structs.decode_BIG_bool_),
}
