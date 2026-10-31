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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GhorAttackDataJson(typing_extensions.TypedDict):
        charge_attack_min_range: float
        charge_attack_max_range: float
        charge_attack_hit_stunned_duration: float
        charge_attack_stop_stunned_duration: float
        charge_attack_slip_stunned_duration: float
        charge_attack_hit_sound: int
        charge_attack_shielded_hit_sound: int
        mini_gun_sweep: json_util.JsonObject
        mini_gun_sweep2: json_util.JsonObject
        mini_gun_track_speed: float
        beam_sweep: json_util.JsonObject
        beam_sweep2: json_util.JsonObject
        unknown_0xb2671c2a: int
        beam_track_speed: float
        beam_cancel_range: float
        beam_cancel_time: float
        jump_min_range: float
        jump_max_range: float
        jump_initial_turn_time: float
        missile_min_range: float
        unknown_0x041abba6: float
        melee_attack_min_range: float
        unknown_0x625f214b: float
        melee_attack_range: float
        melee_min_time_between_attacks: float
        melee_collide_sound: int
        collision_damage: json_util.JsonObject
        hypermode_effect: str
        hypermode_cycle_time: float
        hypermode_initial_on_time: float
        unknown_0xd8255983: float
    

@dataclasses.dataclass()
class GhorAttackData(BaseProperty):
    charge_attack_min_range: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xea4b88c8, original_name='ChargeAttackMinRange'
        ),
    })
    charge_attack_max_range: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaa04f0be, original_name='ChargeAttackMaxRange'
        ),
    })
    charge_attack_hit_stunned_duration: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x59f8b6d0, original_name='ChargeAttackHitStunnedDuration'
        ),
    })
    charge_attack_stop_stunned_duration: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x460020aa, original_name='ChargeAttackStopStunnedDuration'
        ),
    })
    charge_attack_slip_stunned_duration: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x353abf40, original_name='ChargeAttackSlipStunnedDuration'
        ),
    })
    charge_attack_hit_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2822a8fa, original_name='ChargeAttackHitSound'
        ),
    })
    charge_attack_shielded_hit_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x95d26130, original_name='ChargeAttackShieldedHitSound'
        ),
    })
    mini_gun_sweep: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xbfb8336b, original_name='MiniGunSweep', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    mini_gun_sweep2: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xf79adca8, original_name='MiniGunSweep2', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    mini_gun_track_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x68454cb4, original_name='MiniGunTrackSpeed'
        ),
    })
    beam_sweep: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x34ddd21c, original_name='BeamSweep', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    beam_sweep2: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x39705dd6, original_name='BeamSweep2', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    unknown_0xb2671c2a: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb2671c2a, original_name='Unknown'
        ),
    })
    beam_track_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x546dab4c, original_name='BeamTrackSpeed'
        ),
    })
    beam_cancel_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfbdcb40f, original_name='BeamCancelRange'
        ),
    })
    beam_cancel_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d225e0a, original_name='BeamCancelTime'
        ),
    })
    jump_min_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcfd57029, original_name='JumpMinRange'
        ),
    })
    jump_max_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8f9a085f, original_name='JumpMaxRange'
        ),
    })
    jump_initial_turn_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb619c33a, original_name='JumpInitialTurnTime'
        ),
    })
    missile_min_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5eccb98c, original_name='MissileMinRange'
        ),
    })
    unknown_0x041abba6: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x041abba6, original_name='Unknown'
        ),
    })
    melee_attack_min_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbeadf2e0, original_name='MeleeAttackMinRange'
        ),
    })
    unknown_0x625f214b: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x625f214b, original_name='Unknown'
        ),
    })
    melee_attack_range: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3e43d0e, original_name='MeleeAttackRange'
        ),
    })
    melee_min_time_between_attacks: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3e618127, original_name='MeleeMinTimeBetweenAttacks'
        ),
    })
    melee_collide_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x095080d9, original_name='MeleeCollideSound'
        ),
    })
    collision_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x0cfd3139, original_name='CollisionDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    hypermode_effect: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x8062d2f8, original_name='HypermodeEffect'
        ),
    })
    hypermode_cycle_time: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbf26fcfb, original_name='HypermodeCycleTime'
        ),
    })
    hypermode_initial_on_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe64bd01e, original_name='HypermodeInitialOnTime'
        ),
    })
    unknown_0xd8255983: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd8255983, original_name='Unknown'
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
        if property_count != 31:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea4b88c8
        charge_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa04f0be
        charge_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59f8b6d0
        charge_attack_hit_stunned_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x460020aa
        charge_attack_stop_stunned_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x353abf40
        charge_attack_slip_stunned_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2822a8fa
        charge_attack_hit_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95d26130
        charge_attack_shielded_hit_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbfb8336b
        mini_gun_sweep = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf79adca8
        mini_gun_sweep2 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68454cb4
        mini_gun_track_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34ddd21c
        beam_sweep = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39705dd6
        beam_sweep2 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb2671c2a
        unknown_0xb2671c2a = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x546dab4c
        beam_track_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbdcb40f
        beam_cancel_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d225e0a
        beam_cancel_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfd57029
        jump_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f9a085f
        jump_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb619c33a
        jump_initial_turn_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5eccb98c
        missile_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x041abba6
        unknown_0x041abba6 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbeadf2e0
        melee_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x625f214b
        unknown_0x625f214b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3e43d0e
        melee_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e618127
        melee_min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x095080d9
        melee_collide_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0cfd3139
        collision_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8062d2f8
        hypermode_effect = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf26fcfb
        hypermode_cycle_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe64bd01e
        hypermode_initial_on_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8255983
        unknown_0xd8255983 = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(charge_attack_min_range, charge_attack_max_range, charge_attack_hit_stunned_duration, charge_attack_stop_stunned_duration, charge_attack_slip_stunned_duration, charge_attack_hit_sound, charge_attack_shielded_hit_sound, mini_gun_sweep, mini_gun_sweep2, mini_gun_track_speed, beam_sweep, beam_sweep2, unknown_0xb2671c2a, beam_track_speed, beam_cancel_range, beam_cancel_time, jump_min_range, jump_max_range, jump_initial_turn_time, missile_min_range, unknown_0x041abba6, melee_attack_min_range, unknown_0x625f214b, melee_attack_range, melee_min_time_between_attacks, melee_collide_sound, collision_damage, hypermode_effect, hypermode_cycle_time, hypermode_initial_on_time, unknown_0xd8255983)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1f')  # 31 properties

        data.write(b'\xeaK\x88\xc8')  # 0xea4b88c8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_attack_min_range))

        data.write(b'\xaa\x04\xf0\xbe')  # 0xaa04f0be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_attack_max_range))

        data.write(b'Y\xf8\xb6\xd0')  # 0x59f8b6d0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_attack_hit_stunned_duration))

        data.write(b'F\x00 \xaa')  # 0x460020aa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_attack_stop_stunned_duration))

        data.write(b'5:\xbf@')  # 0x353abf40
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_attack_slip_stunned_duration))

        data.write(b'("\xa8\xfa')  # 0x2822a8fa
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.charge_attack_hit_sound))

        data.write(b'\x95\xd2a0')  # 0x95d26130
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.charge_attack_shielded_hit_sound))

        data.write(b'\xbf\xb83k')  # 0xbfb8336b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mini_gun_sweep.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf7\x9a\xdc\xa8')  # 0xf79adca8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mini_gun_sweep2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'hEL\xb4')  # 0x68454cb4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_gun_track_speed))

        data.write(b'4\xdd\xd2\x1c')  # 0x34ddd21c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_sweep.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'9p]\xd6')  # 0x39705dd6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_sweep2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb2g\x1c*')  # 0xb2671c2a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb2671c2a))

        data.write(b'Tm\xabL')  # 0x546dab4c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_track_speed))

        data.write(b'\xfb\xdc\xb4\x0f')  # 0xfbdcb40f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_cancel_range))

        data.write(b'\r"^\n')  # 0xd225e0a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_cancel_time))

        data.write(b'\xcf\xd5p)')  # 0xcfd57029
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_min_range))

        data.write(b'\x8f\x9a\x08_')  # 0x8f9a085f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_max_range))

        data.write(b'\xb6\x19\xc3:')  # 0xb619c33a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_initial_turn_time))

        data.write(b'^\xcc\xb9\x8c')  # 0x5eccb98c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_min_range))

        data.write(b'\x04\x1a\xbb\xa6')  # 0x41abba6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x041abba6))

        data.write(b'\xbe\xad\xf2\xe0')  # 0xbeadf2e0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_attack_min_range))

        data.write(b'b_!K')  # 0x625f214b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x625f214b))

        data.write(b'\xc3\xe4=\x0e')  # 0xc3e43d0e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_attack_range))

        data.write(b">a\x81'")  # 0x3e618127
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_min_time_between_attacks))

        data.write(b'\tP\x80\xd9')  # 0x95080d9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.melee_collide_sound))

        data.write(b'\x0c\xfd19')  # 0xcfd3139
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.collision_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x80b\xd2\xf8')  # 0x8062d2f8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.hypermode_effect.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbf&\xfc\xfb')  # 0xbf26fcfb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hypermode_cycle_time))

        data.write(b'\xe6K\xd0\x1e')  # 0xe64bd01e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hypermode_initial_on_time))

        data.write(b'\xd8%Y\x83')  # 0xd8255983
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd8255983))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorAttackDataJson", data)
        return cls(
            charge_attack_min_range=json_data['charge_attack_min_range'],
            charge_attack_max_range=json_data['charge_attack_max_range'],
            charge_attack_hit_stunned_duration=json_data['charge_attack_hit_stunned_duration'],
            charge_attack_stop_stunned_duration=json_data['charge_attack_stop_stunned_duration'],
            charge_attack_slip_stunned_duration=json_data['charge_attack_slip_stunned_duration'],
            charge_attack_hit_sound=json_data['charge_attack_hit_sound'],
            charge_attack_shielded_hit_sound=json_data['charge_attack_shielded_hit_sound'],
            mini_gun_sweep=Spline.from_json(json_data['mini_gun_sweep']),
            mini_gun_sweep2=Spline.from_json(json_data['mini_gun_sweep2']),
            mini_gun_track_speed=json_data['mini_gun_track_speed'],
            beam_sweep=Spline.from_json(json_data['beam_sweep']),
            beam_sweep2=Spline.from_json(json_data['beam_sweep2']),
            unknown_0xb2671c2a=json_data['unknown_0xb2671c2a'],
            beam_track_speed=json_data['beam_track_speed'],
            beam_cancel_range=json_data['beam_cancel_range'],
            beam_cancel_time=json_data['beam_cancel_time'],
            jump_min_range=json_data['jump_min_range'],
            jump_max_range=json_data['jump_max_range'],
            jump_initial_turn_time=json_data['jump_initial_turn_time'],
            missile_min_range=json_data['missile_min_range'],
            unknown_0x041abba6=json_data['unknown_0x041abba6'],
            melee_attack_min_range=json_data['melee_attack_min_range'],
            unknown_0x625f214b=json_data['unknown_0x625f214b'],
            melee_attack_range=json_data['melee_attack_range'],
            melee_min_time_between_attacks=json_data['melee_min_time_between_attacks'],
            melee_collide_sound=json_data['melee_collide_sound'],
            collision_damage=DamageInfo.from_json(json_data['collision_damage']),
            hypermode_effect=json_data['hypermode_effect'],
            hypermode_cycle_time=json_data['hypermode_cycle_time'],
            hypermode_initial_on_time=json_data['hypermode_initial_on_time'],
            unknown_0xd8255983=json_data['unknown_0xd8255983'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'charge_attack_min_range': self.charge_attack_min_range,
            'charge_attack_max_range': self.charge_attack_max_range,
            'charge_attack_hit_stunned_duration': self.charge_attack_hit_stunned_duration,
            'charge_attack_stop_stunned_duration': self.charge_attack_stop_stunned_duration,
            'charge_attack_slip_stunned_duration': self.charge_attack_slip_stunned_duration,
            'charge_attack_hit_sound': self.charge_attack_hit_sound,
            'charge_attack_shielded_hit_sound': self.charge_attack_shielded_hit_sound,
            'mini_gun_sweep': self.mini_gun_sweep.to_json(),
            'mini_gun_sweep2': self.mini_gun_sweep2.to_json(),
            'mini_gun_track_speed': self.mini_gun_track_speed,
            'beam_sweep': self.beam_sweep.to_json(),
            'beam_sweep2': self.beam_sweep2.to_json(),
            'unknown_0xb2671c2a': self.unknown_0xb2671c2a,
            'beam_track_speed': self.beam_track_speed,
            'beam_cancel_range': self.beam_cancel_range,
            'beam_cancel_time': self.beam_cancel_time,
            'jump_min_range': self.jump_min_range,
            'jump_max_range': self.jump_max_range,
            'jump_initial_turn_time': self.jump_initial_turn_time,
            'missile_min_range': self.missile_min_range,
            'unknown_0x041abba6': self.unknown_0x041abba6,
            'melee_attack_min_range': self.melee_attack_min_range,
            'unknown_0x625f214b': self.unknown_0x625f214b,
            'melee_attack_range': self.melee_attack_range,
            'melee_min_time_between_attacks': self.melee_min_time_between_attacks,
            'melee_collide_sound': self.melee_collide_sound,
            'collision_damage': self.collision_damage.to_json(),
            'hypermode_effect': self.hypermode_effect,
            'hypermode_cycle_time': self.hypermode_cycle_time,
            'hypermode_initial_on_time': self.hypermode_initial_on_time,
            'unknown_0xd8255983': self.unknown_0xd8255983,
        }

    def _dependencies_for_charge_attack_hit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.charge_attack_hit_sound)

    def _dependencies_for_charge_attack_shielded_hit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.charge_attack_shielded_hit_sound)

    def _dependencies_for_melee_collide_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.melee_collide_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_charge_attack_hit_sound, "charge_attack_hit_sound", "AssetId"),
            (self._dependencies_for_charge_attack_shielded_hit_sound, "charge_attack_shielded_hit_sound", "AssetId"),
            (self._dependencies_for_melee_collide_sound, "melee_collide_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GhorAttackData.{field_name} ({field_type}): {e}"
                )


def _decode_mini_gun_sweep(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_mini_gun_sweep2(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_beam_sweep(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_beam_sweep2(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_collision_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_hypermode_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xea4b88c8: ('charge_attack_min_range', structs.decode_BIG_f),
    0xaa04f0be: ('charge_attack_max_range', structs.decode_BIG_f),
    0x59f8b6d0: ('charge_attack_hit_stunned_duration', structs.decode_BIG_f),
    0x460020aa: ('charge_attack_stop_stunned_duration', structs.decode_BIG_f),
    0x353abf40: ('charge_attack_slip_stunned_duration', structs.decode_BIG_f),
    0x2822a8fa: ('charge_attack_hit_sound', structs.decode_BIG_Q),
    0x95d26130: ('charge_attack_shielded_hit_sound', structs.decode_BIG_Q),
    0xbfb8336b: ('mini_gun_sweep', _decode_mini_gun_sweep),
    0xf79adca8: ('mini_gun_sweep2', _decode_mini_gun_sweep2),
    0x68454cb4: ('mini_gun_track_speed', structs.decode_BIG_f),
    0x34ddd21c: ('beam_sweep', _decode_beam_sweep),
    0x39705dd6: ('beam_sweep2', _decode_beam_sweep2),
    0xb2671c2a: ('unknown_0xb2671c2a', structs.decode_BIG_l),
    0x546dab4c: ('beam_track_speed', structs.decode_BIG_f),
    0xfbdcb40f: ('beam_cancel_range', structs.decode_BIG_f),
    0x0d225e0a: ('beam_cancel_time', structs.decode_BIG_f),
    0xcfd57029: ('jump_min_range', structs.decode_BIG_f),
    0x8f9a085f: ('jump_max_range', structs.decode_BIG_f),
    0xb619c33a: ('jump_initial_turn_time', structs.decode_BIG_f),
    0x5eccb98c: ('missile_min_range', structs.decode_BIG_f),
    0x041abba6: ('unknown_0x041abba6', structs.decode_BIG_f),
    0xbeadf2e0: ('melee_attack_min_range', structs.decode_BIG_f),
    0x625f214b: ('unknown_0x625f214b', structs.decode_BIG_f),
    0xc3e43d0e: ('melee_attack_range', structs.decode_BIG_f),
    0x3e618127: ('melee_min_time_between_attacks', structs.decode_BIG_f),
    0x095080d9: ('melee_collide_sound', structs.decode_BIG_Q),
    0x0cfd3139: ('collision_damage', _decode_collision_damage),
    0x8062d2f8: ('hypermode_effect', _decode_hypermode_effect),
    0xbf26fcfb: ('hypermode_cycle_time', structs.decode_BIG_f),
    0xe64bd01e: ('hypermode_initial_on_time', structs.decode_BIG_f),
    0xd8255983: ('unknown_0xd8255983', structs.decode_BIG_f),
}
