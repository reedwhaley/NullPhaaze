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
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MetroidAlphaJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        frozen_vulnerability: json_util.JsonObject
        energy_drain_vulnerability: json_util.JsonObject
        baby_metroid_growth_vulnerability: json_util.JsonObject
        energy_drain_per_sec: float
        max_energy_drain_allowed: float
        telegraph_attack_time: float
        baby_metroid_scale: float
        baby_metroid_maturation_time: float
        baby_metroid_energy_source_check_time_interval: float
        baby_metroid_chance_to_seek_energy_source: float
        baby_metroid_transformation_particle_effect: int
        stage2_growth_scale: float
        stage2_growth_energy: float
        explosion_growth_energy: float
        dodge_check_time_interval: float
        chance_to_dodge: float
        metroid_flags: int
        ing_possession_data: json_util.JsonObject
    

class MetroidFlags(enum.IntFlag):
    BabyMetroid = 1
    StartsInWall = 2

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
class MetroidAlpha(BaseObjectType):
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
    frozen_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x411938aa, original_name='FrozenVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    energy_drain_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xd86ee93f, original_name='EnergyDrainVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    baby_metroid_growth_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x39d63082, original_name='BabyMetroidGrowthVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    energy_drain_per_sec: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x72439b39, original_name='EnergyDrainPerSec'
        ),
    })
    max_energy_drain_allowed: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3af75fcc, original_name='MaxEnergyDrainAllowed'
        ),
    })
    telegraph_attack_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa97edc02, original_name='TelegraphAttackTime'
        ),
    })
    baby_metroid_scale: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d7e7e2c, original_name='BabyMetroidScale'
        ),
    })
    baby_metroid_maturation_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x03362858, original_name='BabyMetroidMaturationTime'
        ),
    })
    baby_metroid_energy_source_check_time_interval: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x852d3bb0, original_name='BabyMetroidEnergySourceCheckTimeInterval'
        ),
    })
    baby_metroid_chance_to_seek_energy_source: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1c783744, original_name='BabyMetroidChanceToSeekEnergySource'
        ),
    })
    baby_metroid_transformation_particle_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x71a21b50, original_name='BabyMetroidTransformationParticleEffect'
        ),
    })
    stage2_growth_scale: float = dataclasses.field(default=1.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2fe164c4, original_name='Stage2GrowthScale'
        ),
    })
    stage2_growth_energy: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4c1f78f3, original_name='Stage2GrowthEnergy'
        ),
    })
    explosion_growth_energy: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5f3f294c, original_name='ExplosionGrowthEnergy'
        ),
    })
    dodge_check_time_interval: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x06b460f4, original_name='DodgeCheckTimeInterval'
        ),
    })
    chance_to_dodge: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23ca0676, original_name='ChanceToDodge'
        ),
    })
    metroid_flags: MetroidFlags = dataclasses.field(default=MetroidFlags(0), metadata={
        'reflection': FieldReflection[MetroidFlags](
            MetroidFlags, id=0xfa51d735, original_name='MetroidFlags', from_json=MetroidFlags.from_json, to_json=MetroidFlags.to_json
        ),
    })
    ing_possession_data: IngPossessionData = dataclasses.field(default_factory=IngPossessionData, metadata={
        'reflection': FieldReflection[IngPossessionData](
            IngPossessionData, id=0xe61748ed, original_name='IngPossessionData', from_json=IngPossessionData.from_json, to_json=IngPossessionData.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'MTDA'

    @classmethod
    def modules(cls) -> list[str]:
        return ['Metroid.rel']

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
        if property_count != 21:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 180.0, 'detection_range': 60.0, 'max_attack_range': 10.0, 'average_attack_time': 6.0, 'attack_time_variation': 5.0, 'creature_size': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x411938aa
        frozen_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd86ee93f
        energy_drain_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39d63082
        baby_metroid_growth_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72439b39
        energy_drain_per_sec = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3af75fcc
        max_energy_drain_allowed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa97edc02
        telegraph_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d7e7e2c
        baby_metroid_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03362858
        baby_metroid_maturation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x852d3bb0
        baby_metroid_energy_source_check_time_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1c783744
        baby_metroid_chance_to_seek_energy_source = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71a21b50
        baby_metroid_transformation_particle_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2fe164c4
        stage2_growth_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c1f78f3
        stage2_growth_energy = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f3f294c
        explosion_growth_energy = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06b460f4
        dodge_check_time_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23ca0676
        chance_to_dodge = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfa51d735
        metroid_flags = MetroidFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe61748ed
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)
    
        return cls(editor_properties, patterned, actor_information, frozen_vulnerability, energy_drain_vulnerability, baby_metroid_growth_vulnerability, energy_drain_per_sec, max_energy_drain_allowed, telegraph_attack_time, baby_metroid_scale, baby_metroid_maturation_time, baby_metroid_energy_source_check_time_interval, baby_metroid_chance_to_seek_energy_source, baby_metroid_transformation_particle_effect, stage2_growth_scale, stage2_growth_energy, explosion_growth_energy, dodge_check_time_interval, chance_to_dodge, metroid_flags, ing_possession_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x15')  # 21 properties

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
        self.patterned.to_stream(data, game, default_override={'turn_speed': 180.0, 'detection_range': 60.0, 'max_attack_range': 10.0, 'average_attack_time': 6.0, 'attack_time_variation': 5.0, 'creature_size': 1})
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

        data.write(b'A\x198\xaa')  # 0x411938aa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.frozen_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd8n\xe9?')  # 0xd86ee93f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_drain_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'9\xd60\x82')  # 0x39d63082
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.baby_metroid_growth_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'rC\x9b9')  # 0x72439b39
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_drain_per_sec))

        data.write(b':\xf7_\xcc')  # 0x3af75fcc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_energy_drain_allowed))

        data.write(b'\xa9~\xdc\x02')  # 0xa97edc02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.telegraph_attack_time))

        data.write(b'\r~~,')  # 0xd7e7e2c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.baby_metroid_scale))

        data.write(b'\x036(X')  # 0x3362858
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.baby_metroid_maturation_time))

        data.write(b'\x85-;\xb0')  # 0x852d3bb0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.baby_metroid_energy_source_check_time_interval))

        data.write(b'\x1cx7D')  # 0x1c783744
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.baby_metroid_chance_to_seek_energy_source))

        data.write(b'q\xa2\x1bP')  # 0x71a21b50
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.baby_metroid_transformation_particle_effect))

        data.write(b'/\xe1d\xc4')  # 0x2fe164c4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage2_growth_scale))

        data.write(b'L\x1fx\xf3')  # 0x4c1f78f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage2_growth_energy))

        data.write(b'_?)L')  # 0x5f3f294c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.explosion_growth_energy))

        data.write(b'\x06\xb4`\xf4')  # 0x6b460f4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_check_time_interval))

        data.write(b'#\xca\x06v')  # 0x23ca0676
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chance_to_dodge))

        data.write(b'\xfaQ\xd75')  # 0xfa51d735
        data.write(b'\x00\x04')  # size
        self.metroid_flags.to_stream(data, game)

        data.write(b'\xe6\x17H\xed')  # 0xe61748ed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidAlphaJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            frozen_vulnerability=DamageVulnerability.from_json(json_data['frozen_vulnerability']),
            energy_drain_vulnerability=DamageVulnerability.from_json(json_data['energy_drain_vulnerability']),
            baby_metroid_growth_vulnerability=DamageVulnerability.from_json(json_data['baby_metroid_growth_vulnerability']),
            energy_drain_per_sec=json_data['energy_drain_per_sec'],
            max_energy_drain_allowed=json_data['max_energy_drain_allowed'],
            telegraph_attack_time=json_data['telegraph_attack_time'],
            baby_metroid_scale=json_data['baby_metroid_scale'],
            baby_metroid_maturation_time=json_data['baby_metroid_maturation_time'],
            baby_metroid_energy_source_check_time_interval=json_data['baby_metroid_energy_source_check_time_interval'],
            baby_metroid_chance_to_seek_energy_source=json_data['baby_metroid_chance_to_seek_energy_source'],
            baby_metroid_transformation_particle_effect=json_data['baby_metroid_transformation_particle_effect'],
            stage2_growth_scale=json_data['stage2_growth_scale'],
            stage2_growth_energy=json_data['stage2_growth_energy'],
            explosion_growth_energy=json_data['explosion_growth_energy'],
            dodge_check_time_interval=json_data['dodge_check_time_interval'],
            chance_to_dodge=json_data['chance_to_dodge'],
            metroid_flags=MetroidFlags.from_json(json_data['metroid_flags']),
            ing_possession_data=IngPossessionData.from_json(json_data['ing_possession_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'frozen_vulnerability': self.frozen_vulnerability.to_json(),
            'energy_drain_vulnerability': self.energy_drain_vulnerability.to_json(),
            'baby_metroid_growth_vulnerability': self.baby_metroid_growth_vulnerability.to_json(),
            'energy_drain_per_sec': self.energy_drain_per_sec,
            'max_energy_drain_allowed': self.max_energy_drain_allowed,
            'telegraph_attack_time': self.telegraph_attack_time,
            'baby_metroid_scale': self.baby_metroid_scale,
            'baby_metroid_maturation_time': self.baby_metroid_maturation_time,
            'baby_metroid_energy_source_check_time_interval': self.baby_metroid_energy_source_check_time_interval,
            'baby_metroid_chance_to_seek_energy_source': self.baby_metroid_chance_to_seek_energy_source,
            'baby_metroid_transformation_particle_effect': self.baby_metroid_transformation_particle_effect,
            'stage2_growth_scale': self.stage2_growth_scale,
            'stage2_growth_energy': self.stage2_growth_energy,
            'explosion_growth_energy': self.explosion_growth_energy,
            'dodge_check_time_interval': self.dodge_check_time_interval,
            'chance_to_dodge': self.chance_to_dodge,
            'metroid_flags': self.metroid_flags.to_json(),
            'ing_possession_data': self.ing_possession_data.to_json(),
        }

    def _dependencies_for_baby_metroid_transformation_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.baby_metroid_transformation_particle_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_baby_metroid_transformation_particle_effect, "baby_metroid_transformation_particle_effect", "AssetId"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MetroidAlpha.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 180.0, 'detection_range': 60.0, 'max_attack_range': 10.0, 'average_attack_time': 6.0, 'attack_time_variation': 5.0, 'creature_size': 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_frozen_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_energy_drain_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_baby_metroid_growth_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_metroid_flags(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidFlags:
    return MetroidFlags.from_stream(data, game)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x411938aa: ('frozen_vulnerability', _decode_frozen_vulnerability),
    0xd86ee93f: ('energy_drain_vulnerability', _decode_energy_drain_vulnerability),
    0x39d63082: ('baby_metroid_growth_vulnerability', _decode_baby_metroid_growth_vulnerability),
    0x72439b39: ('energy_drain_per_sec', structs.decode_BIG_f),
    0x3af75fcc: ('max_energy_drain_allowed', structs.decode_BIG_f),
    0xa97edc02: ('telegraph_attack_time', structs.decode_BIG_f),
    0x0d7e7e2c: ('baby_metroid_scale', structs.decode_BIG_f),
    0x03362858: ('baby_metroid_maturation_time', structs.decode_BIG_f),
    0x852d3bb0: ('baby_metroid_energy_source_check_time_interval', structs.decode_BIG_f),
    0x1c783744: ('baby_metroid_chance_to_seek_energy_source', structs.decode_BIG_f),
    0x71a21b50: ('baby_metroid_transformation_particle_effect', structs.decode_BIG_L),
    0x2fe164c4: ('stage2_growth_scale', structs.decode_BIG_f),
    0x4c1f78f3: ('stage2_growth_energy', structs.decode_BIG_f),
    0x5f3f294c: ('explosion_growth_energy', structs.decode_BIG_f),
    0x06b460f4: ('dodge_check_time_interval', structs.decode_BIG_f),
    0x23ca0676: ('chance_to_dodge', structs.decode_BIG_f),
    0xfa51d735: ('metroid_flags', _decode_metroid_flags),
    0xe61748ed: ('ing_possession_data', _decode_ing_possession_data),
}
