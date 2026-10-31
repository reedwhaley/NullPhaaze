# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.GhostBehave import GhostBehave
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ChozoGhostJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        hearing_radius: float
        fade_out_delay: float
        attack_delay: float
        freeze_time: float
        handblast: int
        handblast_damage: json_util.JsonObject
        powerball: int
        powerball_damage: json_util.JsonObject
        far: json_util.JsonObject
        mid: json_util.JsonObject
        near: json_util.JsonObject
        sound_impact: int
        disable_player_gun_time: float
        sound_phaze_in: int
        sound_phaze_out: int
        unknown: int
        projectile_stop_homing_range: float
        start_style: int
        hurl_recover_time: float
        projectile_visor_effect: int
        sound_projectile_visor: int
        near_to_mid_distance: float
        mid_to_far_distance: float
        near_chance: int
        mid_chance: int
    

@dataclasses.dataclass()
class ChozoGhost(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0xb3774750, original_name='Patterned', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    hearing_radius: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed69488f, original_name='HearingRadius'
        ),
    })
    fade_out_delay: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfb12f672, original_name='FadeOutDelay'
        ),
    })
    attack_delay: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b67981a, original_name='AttackDelay'
        ),
    })
    freeze_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1e8722c7, original_name='FreezeTime'
        ),
    })
    handblast: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x54151870, original_name='Handblast'
        ),
    })
    handblast_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xffcda1f8, original_name='HandblastDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    powerball: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3a58089c, original_name='Powerball'
        ),
    })
    powerball_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x1ff047a9, original_name='PowerballDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    far: GhostBehave = dataclasses.field(default_factory=GhostBehave, metadata={
        'reflection': FieldReflection[GhostBehave](
            GhostBehave, id=0xe832241f, original_name='Far', from_json=GhostBehave.from_json, to_json=GhostBehave.to_json
        ),
    })
    mid: GhostBehave = dataclasses.field(default_factory=GhostBehave, metadata={
        'reflection': FieldReflection[GhostBehave](
            GhostBehave, id=0x1e2c8483, original_name='Mid', from_json=GhostBehave.from_json, to_json=GhostBehave.to_json
        ),
    })
    near: GhostBehave = dataclasses.field(default_factory=GhostBehave, metadata={
        'reflection': FieldReflection[GhostBehave](
            GhostBehave, id=0x78d76034, original_name='Near', from_json=GhostBehave.from_json, to_json=GhostBehave.to_json
        ),
    })
    sound_impact: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x1bb16ea5, original_name='Sound_Impact'
        ),
    })
    disable_player_gun_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc87d7ec7, original_name='DisablePlayerGunTime'
        ),
    })
    sound_phaze_in: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x2adcbb2e, original_name='Sound_PhazeIn'
        ),
    })
    sound_phaze_out: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x58b8ec5d, original_name='Sound_PhazeOut'
        ),
    })
    unknown: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xec76940c, original_name='Unknown'
        ),
    })
    projectile_stop_homing_range: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x723542bb, original_name='ProjectileStopHomingRange'
        ),
    })
    start_style: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xfe9eac26, original_name='StartStyle'
        ),
    })  # Choice
    hurl_recover_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x96feb75d, original_name='HurlRecoverTime'
        ),
    })
    projectile_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8f8c64a0, original_name='ProjectileVisorEffect'
        ),
    })
    sound_projectile_visor: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe15b4f4a, original_name='Sound_ProjectileVisor'
        ),
    })
    near_to_mid_distance: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x61e511b3, original_name='NearToMidDistance'
        ),
    })
    mid_to_far_distance: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2369607a, original_name='MidToFarDistance'
        ),
    })
    near_chance: int = dataclasses.field(default=40, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa6a3879b, original_name='NearChance'
        ),
    })
    mid_chance: int = dataclasses.field(default=40, metadata={
        'reflection': FieldReflection[int](
            int, id=0x1b272781, original_name='MidChance'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'CHOG'

    @classmethod
    def modules(cls) -> list[str]:
        return ['ChozoGhost.rel']

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 28:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 720.0, 'detection_range': 25.0, 'min_attack_range': 8.0, 'max_attack_range': 70.0, 'leash_radius': 70.0, 'collision_height': 4.5, 'creature_size': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed69488f
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb12f672
        fade_out_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b67981a
        attack_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e8722c7
        freeze_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54151870
        handblast = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xffcda1f8
        handblast_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3a58089c
        powerball = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1ff047a9
        powerball_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe832241f
        far = GhostBehave.from_stream(data, game, property_size, default_override={'lurk': 20.0, 'heckle': 0.0, 'attack': 60.0, 'move': 20.0, 'charge_attack': 0.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e2c8483
        mid = GhostBehave.from_stream(data, game, property_size, default_override={'lurk': 20.0, 'heckle': 10.0, 'attack': 60.0, 'move': 10.0, 'charge_attack': 20.0, 'num_bolts': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78d76034
        near = GhostBehave.from_stream(data, game, property_size, default_override={'lurk': 0.0, 'heckle': 0.0, 'attack': 100.0, 'move': 0.0, 'num_bolts': 2})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1bb16ea5
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc87d7ec7
        disable_player_gun_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2adcbb2e
        sound_phaze_in = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58b8ec5d
        sound_phaze_out = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xec76940c
        unknown = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723542bb
        projectile_stop_homing_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe9eac26
        start_style = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96feb75d
        hurl_recover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f8c64a0
        projectile_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe15b4f4a
        sound_projectile_visor = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61e511b3
        near_to_mid_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2369607a
        mid_to_far_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6a3879b
        near_chance = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b272781
        mid_chance = structs.BIG_l.unpack(data.read(4))[0]
    
        return cls(editor_properties, patterned, actor_information, hearing_radius, fade_out_delay, attack_delay, freeze_time, handblast, handblast_damage, powerball, powerball_damage, far, mid, near, sound_impact, disable_player_gun_time, sound_phaze_in, sound_phaze_out, unknown, projectile_stop_homing_range, start_style, hurl_recover_time, projectile_visor_effect, sound_projectile_visor, near_to_mid_distance, mid_to_far_distance, near_chance, mid_chance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x1c')  # 28 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'turn_speed': 720.0, 'detection_range': 25.0, 'min_attack_range': 8.0, 'max_attack_range': 70.0, 'leash_radius': 70.0, 'collision_height': 4.5, 'creature_size': 1})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~9\x7f\xed')  # 0x7e397fed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xediH\x8f')  # 0xed69488f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b'\xfb\x12\xf6r')  # 0xfb12f672
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fade_out_delay))

        data.write(b'\x1bg\x98\x1a')  # 0x1b67981a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_delay))

        data.write(b'\x1e\x87"\xc7')  # 0x1e8722c7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.freeze_time))

        data.write(b'T\x15\x18p')  # 0x54151870
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.handblast))

        data.write(b'\xff\xcd\xa1\xf8')  # 0xffcda1f8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.handblast_damage.to_stream(data, game, default_override={'di_damage': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b':X\x08\x9c')  # 0x3a58089c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.powerball))

        data.write(b'\x1f\xf0G\xa9')  # 0x1ff047a9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.powerball_damage.to_stream(data, game, default_override={'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe82$\x1f')  # 0xe832241f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.far.to_stream(data, game, default_override={'lurk': 20.0, 'heckle': 0.0, 'attack': 60.0, 'move': 20.0, 'charge_attack': 0.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1e,\x84\x83')  # 0x1e2c8483
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mid.to_stream(data, game, default_override={'lurk': 20.0, 'heckle': 10.0, 'attack': 60.0, 'move': 10.0, 'charge_attack': 20.0, 'num_bolts': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'x\xd7`4')  # 0x78d76034
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.near.to_stream(data, game, default_override={'lurk': 0.0, 'heckle': 0.0, 'attack': 100.0, 'move': 0.0, 'num_bolts': 2})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1b\xb1n\xa5')  # 0x1bb16ea5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_impact))

        data.write(b'\xc8}~\xc7')  # 0xc87d7ec7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.disable_player_gun_time))

        data.write(b'*\xdc\xbb.')  # 0x2adcbb2e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_phaze_in))

        data.write(b'X\xb8\xec]')  # 0x58b8ec5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_phaze_out))

        data.write(b'\xecv\x94\x0c')  # 0xec76940c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown))

        data.write(b'r5B\xbb')  # 0x723542bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_stop_homing_range))

        data.write(b'\xfe\x9e\xac&')  # 0xfe9eac26
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.start_style))

        data.write(b'\x96\xfe\xb7]')  # 0x96feb75d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hurl_recover_time))

        data.write(b'\x8f\x8cd\xa0')  # 0x8f8c64a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.projectile_visor_effect))

        data.write(b'\xe1[OJ')  # 0xe15b4f4a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_projectile_visor))

        data.write(b'a\xe5\x11\xb3')  # 0x61e511b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.near_to_mid_distance))

        data.write(b'#i`z')  # 0x2369607a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mid_to_far_distance))

        data.write(b'\xa6\xa3\x87\x9b')  # 0xa6a3879b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.near_chance))

        data.write(b"\x1b''\x81")  # 0x1b272781
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.mid_chance))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ChozoGhostJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            hearing_radius=json_data['hearing_radius'],
            fade_out_delay=json_data['fade_out_delay'],
            attack_delay=json_data['attack_delay'],
            freeze_time=json_data['freeze_time'],
            handblast=json_data['handblast'],
            handblast_damage=DamageInfo.from_json(json_data['handblast_damage']),
            powerball=json_data['powerball'],
            powerball_damage=DamageInfo.from_json(json_data['powerball_damage']),
            far=GhostBehave.from_json(json_data['far']),
            mid=GhostBehave.from_json(json_data['mid']),
            near=GhostBehave.from_json(json_data['near']),
            sound_impact=json_data['sound_impact'],
            disable_player_gun_time=json_data['disable_player_gun_time'],
            sound_phaze_in=json_data['sound_phaze_in'],
            sound_phaze_out=json_data['sound_phaze_out'],
            unknown=json_data['unknown'],
            projectile_stop_homing_range=json_data['projectile_stop_homing_range'],
            start_style=json_data['start_style'],
            hurl_recover_time=json_data['hurl_recover_time'],
            projectile_visor_effect=json_data['projectile_visor_effect'],
            sound_projectile_visor=json_data['sound_projectile_visor'],
            near_to_mid_distance=json_data['near_to_mid_distance'],
            mid_to_far_distance=json_data['mid_to_far_distance'],
            near_chance=json_data['near_chance'],
            mid_chance=json_data['mid_chance'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'hearing_radius': self.hearing_radius,
            'fade_out_delay': self.fade_out_delay,
            'attack_delay': self.attack_delay,
            'freeze_time': self.freeze_time,
            'handblast': self.handblast,
            'handblast_damage': self.handblast_damage.to_json(),
            'powerball': self.powerball,
            'powerball_damage': self.powerball_damage.to_json(),
            'far': self.far.to_json(),
            'mid': self.mid.to_json(),
            'near': self.near.to_json(),
            'sound_impact': self.sound_impact,
            'disable_player_gun_time': self.disable_player_gun_time,
            'sound_phaze_in': self.sound_phaze_in,
            'sound_phaze_out': self.sound_phaze_out,
            'unknown': self.unknown,
            'projectile_stop_homing_range': self.projectile_stop_homing_range,
            'start_style': self.start_style,
            'hurl_recover_time': self.hurl_recover_time,
            'projectile_visor_effect': self.projectile_visor_effect,
            'sound_projectile_visor': self.sound_projectile_visor,
            'near_to_mid_distance': self.near_to_mid_distance,
            'mid_to_far_distance': self.mid_to_far_distance,
            'near_chance': self.near_chance,
            'mid_chance': self.mid_chance,
        }

    def _dependencies_for_handblast(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.handblast)

    def _dependencies_for_powerball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.powerball)

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_sound_phaze_in(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_phaze_in)

    def _dependencies_for_sound_phaze_out(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_phaze_out)

    def _dependencies_for_projectile_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_visor_effect)

    def _dependencies_for_sound_projectile_visor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_projectile_visor)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_handblast, "handblast", "AssetId"),
            (self._dependencies_for_powerball, "powerball", "AssetId"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_sound_phaze_in, "sound_phaze_in", "int"),
            (self._dependencies_for_sound_phaze_out, "sound_phaze_out", "int"),
            (self._dependencies_for_projectile_visor_effect, "projectile_visor_effect", "AssetId"),
            (self._dependencies_for_sound_projectile_visor, "sound_projectile_visor", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ChozoGhost.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 720.0, 'detection_range': 25.0, 'min_attack_range': 8.0, 'max_attack_range': 70.0, 'leash_radius': 70.0, 'collision_height': 4.5, 'creature_size': 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_handblast_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 10.0})


def _decode_powerball_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 5.0})


def _decode_far(data: typing.BinaryIO, game: Game, property_size: int) -> GhostBehave:
    return GhostBehave.from_stream(data, game, property_size, default_override={'lurk': 20.0, 'heckle': 0.0, 'attack': 60.0, 'move': 20.0, 'charge_attack': 0.0})


def _decode_mid(data: typing.BinaryIO, game: Game, property_size: int) -> GhostBehave:
    return GhostBehave.from_stream(data, game, property_size, default_override={'lurk': 20.0, 'heckle': 10.0, 'attack': 60.0, 'move': 10.0, 'charge_attack': 20.0, 'num_bolts': 3})


def _decode_near(data: typing.BinaryIO, game: Game, property_size: int) -> GhostBehave:
    return GhostBehave.from_stream(data, game, property_size, default_override={'lurk': 0.0, 'heckle': 0.0, 'attack': 100.0, 'move': 0.0, 'num_bolts': 2})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xed69488f: ('hearing_radius', structs.decode_BIG_f),
    0xfb12f672: ('fade_out_delay', structs.decode_BIG_f),
    0x1b67981a: ('attack_delay', structs.decode_BIG_f),
    0x1e8722c7: ('freeze_time', structs.decode_BIG_f),
    0x54151870: ('handblast', structs.decode_BIG_L),
    0xffcda1f8: ('handblast_damage', _decode_handblast_damage),
    0x3a58089c: ('powerball', structs.decode_BIG_L),
    0x1ff047a9: ('powerball_damage', _decode_powerball_damage),
    0xe832241f: ('far', _decode_far),
    0x1e2c8483: ('mid', _decode_mid),
    0x78d76034: ('near', _decode_near),
    0x1bb16ea5: ('sound_impact', structs.decode_BIG_l),
    0xc87d7ec7: ('disable_player_gun_time', structs.decode_BIG_f),
    0x2adcbb2e: ('sound_phaze_in', structs.decode_BIG_l),
    0x58b8ec5d: ('sound_phaze_out', structs.decode_BIG_l),
    0xec76940c: ('unknown', structs.decode_BIG_l),
    0x723542bb: ('projectile_stop_homing_range', structs.decode_BIG_f),
    0xfe9eac26: ('start_style', structs.decode_BIG_L),
    0x96feb75d: ('hurl_recover_time', structs.decode_BIG_f),
    0x8f8c64a0: ('projectile_visor_effect', structs.decode_BIG_L),
    0xe15b4f4a: ('sound_projectile_visor', structs.decode_BIG_l),
    0x61e511b3: ('near_to_mid_distance', structs.decode_BIG_f),
    0x2369607a: ('mid_to_far_distance', structs.decode_BIG_f),
    0xa6a3879b: ('near_chance', structs.decode_BIG_l),
    0x1b272781: ('mid_chance', structs.decode_BIG_l),
}
