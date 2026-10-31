# Generated File
from __future__ import annotations

import dataclasses
import enum
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.CommandoEGrenade import CommandoEGrenade
from retro_data_structures.properties.echoes.archetypes.CommandoShield import CommandoShield
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class CommandoPirateJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        ing_possession_data: json_util.JsonObject
        commando_flags: int
        aggressiveness: float
        cover_check: float
        search_radius: float
        dodge_check: float
        sound_impact: int
        sound_hurled: int
        sound_death: int
        sound_drowing: int
        drowing_fx: int
        blade_damage: json_util.JsonObject
        projectile: int
        projectile_damage: json_util.JsonObject
        sound_projectile: int
        hearing_radius: float
        e_grenade: json_util.JsonObject
        shield_info: json_util.JsonObject
        intra_burst_shot_time: float
        intra_burst_shot_variation: float
    

class CommandoPirateFlags(enum.IntFlag):
    PendingAmbush = 1
    BreakAmbush = 2
    NoDodge = 4
    Melee = 8
    Stationary = 16
    NoKnockbackImpulseReset = 32
    NoMeleeAttack = 64
    FloatingCorpse = 128
    CanWarp = 256
    NoShieldCharge = 512
    NoArmShield = 1024
    NoGrenadeAttack = 2048

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class CommandoPirate(BaseObjectType):
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
    ing_possession_data: IngPossessionData = dataclasses.field(default_factory=IngPossessionData, metadata={
        'reflection': FieldReflection[IngPossessionData](
            IngPossessionData, id=0xe61748ed, original_name='IngPossessionData', from_json=IngPossessionData.from_json, to_json=IngPossessionData.to_json
        ),
    })
    commando_flags: CommandoPirateFlags = dataclasses.field(default=CommandoPirateFlags(0), metadata={
        'reflection': FieldReflection[CommandoPirateFlags](
            CommandoPirateFlags, id=0x7abed4ce, original_name='CommandoFlags', from_json=CommandoPirateFlags.from_json, to_json=CommandoPirateFlags.to_json
        ),
    })
    aggressiveness: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9579b1f2, original_name='Aggressiveness'
        ),
    })
    cover_check: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf89ab419, original_name='CoverCheck'
        ),
    })
    search_radius: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed9bf5a3, original_name='SearchRadius'
        ),
    })
    dodge_check: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdc36e745, original_name='DodgeCheck'
        ),
    })
    sound_impact: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x1bb16ea5, original_name='Sound_Impact'
        ),
    })
    sound_hurled: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x3bb37a8f, original_name='Sound_Hurled'
        ),
    })
    sound_death: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe160b593, original_name='Sound_Death'
        ),
    })
    sound_drowing: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xfca76593, original_name='Sound_Drowing'
        ),
    })
    drowing_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x467c3d94, original_name='DrowingFx'
        ),
    })
    blade_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xa5912430, original_name='BladeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x553b1339, original_name='ProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sound_projectile: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xeac27605, original_name='Sound_Projectile'
        ),
    })
    hearing_radius: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed69488f, original_name='HearingRadius'
        ),
    })
    e_grenade: CommandoEGrenade = dataclasses.field(default_factory=CommandoEGrenade, metadata={
        'reflection': FieldReflection[CommandoEGrenade](
            CommandoEGrenade, id=0xfb435257, original_name='EGrenade', from_json=CommandoEGrenade.from_json, to_json=CommandoEGrenade.to_json
        ),
    })
    shield_info: CommandoShield = dataclasses.field(default_factory=CommandoShield, metadata={
        'reflection': FieldReflection[CommandoShield](
            CommandoShield, id=0x388e16c9, original_name='ShieldInfo', from_json=CommandoShield.from_json, to_json=CommandoShield.to_json
        ),
    })
    intra_burst_shot_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71587b45, original_name='IntraBurstShotTime'
        ),
    })
    intra_burst_shot_variation: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7903312e, original_name='IntraBurstShotVariation'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'CMDO'

    @classmethod
    def modules(cls) -> list[str]:
        return ['PirateRagDoll.rel', 'CommandoPirate.rel']

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
        if property_count != 23:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0, 'detection_angle': 90.0, 'average_attack_time': 1.0, 'attack_time_variation': 0.5, 'damage_wait_time': 3.0, 'collision_radius': 0.800000011920929, 'collision_height': 3.0, 'step_up_height': 0.30000001192092896, 'transition_from_freeze_time': 0.20000000298023224, 'creature_size': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe61748ed
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7abed4ce
        commando_flags = CommandoPirateFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9579b1f2
        aggressiveness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf89ab419
        cover_check = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed9bf5a3
        search_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc36e745
        dodge_check = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1bb16ea5
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3bb37a8f
        sound_hurled = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe160b593
        sound_death = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfca76593
        sound_drowing = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x467c3d94
        drowing_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa5912430
        blade_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553b1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeac27605
        sound_projectile = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed69488f
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb435257
        e_grenade = CommandoEGrenade.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388e16c9
        shield_info = CommandoShield.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71587b45
        intra_burst_shot_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7903312e
        intra_burst_shot_variation = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, patterned, actor_information, ing_possession_data, commando_flags, aggressiveness, cover_check, search_radius, dodge_check, sound_impact, sound_hurled, sound_death, sound_drowing, drowing_fx, blade_damage, projectile, projectile_damage, sound_projectile, hearing_radius, e_grenade, shield_info, intra_burst_shot_time, intra_burst_shot_variation)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x17')  # 23 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'turn_speed': 360.0, 'detection_angle': 90.0, 'average_attack_time': 1.0, 'attack_time_variation': 0.5, 'damage_wait_time': 3.0, 'collision_radius': 0.800000011920929, 'collision_height': 3.0, 'step_up_height': 0.30000001192092896, 'transition_from_freeze_time': 0.20000000298023224, 'creature_size': 1})
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

        data.write(b'\xe6\x17H\xed')  # 0xe61748ed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'z\xbe\xd4\xce')  # 0x7abed4ce
        data.write(b'\x00\x04')  # size
        self.commando_flags.to_stream(data, game)

        data.write(b'\x95y\xb1\xf2')  # 0x9579b1f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aggressiveness))

        data.write(b'\xf8\x9a\xb4\x19')  # 0xf89ab419
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cover_check))

        data.write(b'\xed\x9b\xf5\xa3')  # 0xed9bf5a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.search_radius))

        data.write(b'\xdc6\xe7E')  # 0xdc36e745
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_check))

        data.write(b'\x1b\xb1n\xa5')  # 0x1bb16ea5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_impact))

        data.write(b';\xb3z\x8f')  # 0x3bb37a8f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_hurled))

        data.write(b'\xe1`\xb5\x93')  # 0xe160b593
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_death))

        data.write(b'\xfc\xa7e\x93')  # 0xfca76593
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_drowing))

        data.write(b'F|=\x94')  # 0x467c3d94
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.drowing_fx))

        data.write(b'\xa5\x91$0')  # 0xa5912430
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.blade_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b'U;\x139')  # 0x553b1339
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xea\xc2v\x05')  # 0xeac27605
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_projectile))

        data.write(b'\xediH\x8f')  # 0xed69488f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b'\xfbCRW')  # 0xfb435257
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.e_grenade.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'8\x8e\x16\xc9')  # 0x388e16c9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shield_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'qX{E')  # 0x71587b45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.intra_burst_shot_time))

        data.write(b'y\x031.')  # 0x7903312e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.intra_burst_shot_variation))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CommandoPirateJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            ing_possession_data=IngPossessionData.from_json(json_data['ing_possession_data']),
            commando_flags=CommandoPirateFlags.from_json(json_data['commando_flags']),
            aggressiveness=json_data['aggressiveness'],
            cover_check=json_data['cover_check'],
            search_radius=json_data['search_radius'],
            dodge_check=json_data['dodge_check'],
            sound_impact=json_data['sound_impact'],
            sound_hurled=json_data['sound_hurled'],
            sound_death=json_data['sound_death'],
            sound_drowing=json_data['sound_drowing'],
            drowing_fx=json_data['drowing_fx'],
            blade_damage=DamageInfo.from_json(json_data['blade_damage']),
            projectile=json_data['projectile'],
            projectile_damage=DamageInfo.from_json(json_data['projectile_damage']),
            sound_projectile=json_data['sound_projectile'],
            hearing_radius=json_data['hearing_radius'],
            e_grenade=CommandoEGrenade.from_json(json_data['e_grenade']),
            shield_info=CommandoShield.from_json(json_data['shield_info']),
            intra_burst_shot_time=json_data['intra_burst_shot_time'],
            intra_burst_shot_variation=json_data['intra_burst_shot_variation'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'ing_possession_data': self.ing_possession_data.to_json(),
            'commando_flags': self.commando_flags.to_json(),
            'aggressiveness': self.aggressiveness,
            'cover_check': self.cover_check,
            'search_radius': self.search_radius,
            'dodge_check': self.dodge_check,
            'sound_impact': self.sound_impact,
            'sound_hurled': self.sound_hurled,
            'sound_death': self.sound_death,
            'sound_drowing': self.sound_drowing,
            'drowing_fx': self.drowing_fx,
            'blade_damage': self.blade_damage.to_json(),
            'projectile': self.projectile,
            'projectile_damage': self.projectile_damage.to_json(),
            'sound_projectile': self.sound_projectile,
            'hearing_radius': self.hearing_radius,
            'e_grenade': self.e_grenade.to_json(),
            'shield_info': self.shield_info.to_json(),
            'intra_burst_shot_time': self.intra_burst_shot_time,
            'intra_burst_shot_variation': self.intra_burst_shot_variation,
        }

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_sound_hurled(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_hurled)

    def _dependencies_for_sound_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_death)

    def _dependencies_for_sound_drowing(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_drowing)

    def _dependencies_for_drowing_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.drowing_fx)

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_sound_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_sound_hurled, "sound_hurled", "int"),
            (self._dependencies_for_sound_death, "sound_death", "int"),
            (self._dependencies_for_sound_drowing, "sound_drowing", "int"),
            (self._dependencies_for_drowing_fx, "drowing_fx", "AssetId"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_sound_projectile, "sound_projectile", "int"),
            (self.e_grenade.dependencies_for, "e_grenade", "CommandoEGrenade"),
            (self.shield_info.dependencies_for, "shield_info", "CommandoShield"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for CommandoPirate.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0, 'detection_angle': 90.0, 'average_attack_time': 1.0, 'attack_time_variation': 0.5, 'damage_wait_time': 3.0, 'collision_radius': 0.800000011920929, 'collision_height': 3.0, 'step_up_height': 0.30000001192092896, 'transition_from_freeze_time': 0.20000000298023224, 'creature_size': 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


def _decode_commando_flags(data: typing.BinaryIO, game: Game, property_size: int) -> CommandoPirateFlags:
    return CommandoPirateFlags.from_stream(data, game)


def _decode_blade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_e_grenade(data: typing.BinaryIO, game: Game, property_size: int) -> CommandoEGrenade:
    return CommandoEGrenade.from_stream(data, game, property_size)


def _decode_shield_info(data: typing.BinaryIO, game: Game, property_size: int) -> CommandoShield:
    return CommandoShield.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xe61748ed: ('ing_possession_data', _decode_ing_possession_data),
    0x7abed4ce: ('commando_flags', _decode_commando_flags),
    0x9579b1f2: ('aggressiveness', structs.decode_BIG_f),
    0xf89ab419: ('cover_check', structs.decode_BIG_f),
    0xed9bf5a3: ('search_radius', structs.decode_BIG_f),
    0xdc36e745: ('dodge_check', structs.decode_BIG_f),
    0x1bb16ea5: ('sound_impact', structs.decode_BIG_l),
    0x3bb37a8f: ('sound_hurled', structs.decode_BIG_l),
    0xe160b593: ('sound_death', structs.decode_BIG_l),
    0xfca76593: ('sound_drowing', structs.decode_BIG_l),
    0x467c3d94: ('drowing_fx', structs.decode_BIG_L),
    0xa5912430: ('blade_damage', _decode_blade_damage),
    0xef485db9: ('projectile', structs.decode_BIG_L),
    0x553b1339: ('projectile_damage', _decode_projectile_damage),
    0xeac27605: ('sound_projectile', structs.decode_BIG_l),
    0xed69488f: ('hearing_radius', structs.decode_BIG_f),
    0xfb435257: ('e_grenade', _decode_e_grenade),
    0x388e16c9: ('shield_info', _decode_shield_info),
    0x71587b45: ('intra_burst_shot_time', structs.decode_BIG_f),
    0x7903312e: ('intra_burst_shot_variation', structs.decode_BIG_f),
}
