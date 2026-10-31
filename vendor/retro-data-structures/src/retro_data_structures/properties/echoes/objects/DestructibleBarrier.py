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
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DestructibleBarrierJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        num_chunks_width: int
        num_chunks_height: int
        num_chunks_depth: int
        chunk_size: json_util.JsonValue
        left_model: int
        center_model: int
        right_model: int
        row_model_one_deep: int
        row_model_full_depth: int
        base_model: int
        destroyed_chunk_effect_1: int
        destroyed_chunk_effect_1_num_particles_to_generate: int
        destroyed_chunk_effect_2: int
        destroyed_chunk_effect_2_num_particles_to_generate: int
        destroyed_chunk_effect_3: int
        destroyed_chunk_effect_3_num_particles_to_generate: int
        destroyed_chunk_effect_4: int
        destroyed_chunk_effect_4_num_particles_to_generate: int
        sound_effect_on_chunk_generated: int
        sound_effect_on_chunk_destroyed: int
        sound_effect_on_move_down: int
        sound_effect_on_move_up: int
        sound_effect_on_stop: int
        percentage_damage_required_for_reset: float
        time_after_damaged_for_reset: float
        unknown: float
        barrier_starts_down: bool
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        actor_information: json_util.JsonObject
    

@dataclasses.dataclass()
class DestructibleBarrier(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    num_chunks_width: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xcd4f7e71, original_name='NumChunksWidth'
        ),
    })
    num_chunks_height: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa7f551f7, original_name='NumChunksHeight'
        ),
    })
    num_chunks_depth: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x609c6240, original_name='NumChunksDepth'
        ),
    })
    chunk_size: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.5, y=0.20000000298023224, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xb29e159e, original_name='ChunkSize', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    left_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x014a0c36, original_name='LeftModel'
        ),
    })
    center_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x90f55c5d, original_name='CenterModel'
        ),
    })
    right_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe1975355, original_name='RightModel'
        ),
    })
    row_model_one_deep: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x396660b4, original_name='RowModelOneDeep'
        ),
    })
    row_model_full_depth: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x48e25884, original_name='RowModelFullDepth'
        ),
    })
    base_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf1abb2c7, original_name='BaseModel'
        ),
    })
    destroyed_chunk_effect_1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1eb90d06, original_name='DestroyedChunkEffect_1'
        ),
    })
    destroyed_chunk_effect_1_num_particles_to_generate: int = dataclasses.field(default=4, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9d852dfe, original_name='DestroyedChunkEffect_1_NumParticlesToGenerate'
        ),
    })
    destroyed_chunk_effect_2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x982d7fa8, original_name='DestroyedChunkEffect_2'
        ),
    })
    destroyed_chunk_effect_2_num_particles_to_generate: int = dataclasses.field(default=4, metadata={
        'reflection': FieldReflection[int](
            int, id=0x2e11003d, original_name='DestroyedChunkEffect_2_NumParticlesToGenerate'
        ),
    })
    destroyed_chunk_effect_3: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5371ac0d, original_name='DestroyedChunkEffect_3'
        ),
    })
    destroyed_chunk_effect_3_num_particles_to_generate: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x409d1b7c, original_name='DestroyedChunkEffect_3_NumParticlesToGenerate'
        ),
    })
    destroyed_chunk_effect_4: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4e749cb5, original_name='DestroyedChunkEffect_4'
        ),
    })
    destroyed_chunk_effect_4_num_particles_to_generate: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x92485dfa, original_name='DestroyedChunkEffect_4_NumParticlesToGenerate'
        ),
    })
    sound_effect_on_chunk_generated: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x6e4a9d27, original_name='SoundEffectOnChunkGenerated'
        ),
    })
    sound_effect_on_chunk_destroyed: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xbc2381a6, original_name='SoundEffectOnChunkDestroyed'
        ),
    })
    sound_effect_on_move_down: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x6575a3d5, original_name='SoundEffectOnMoveDown'
        ),
    })
    sound_effect_on_move_up: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xc91b0946, original_name='SoundEffectOnMoveUp'
        ),
    })
    sound_effect_on_stop: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x4b2d5a37, original_name='SoundEffectOnStop'
        ),
    })
    percentage_damage_required_for_reset: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x605847b9, original_name='PercentageDamageRequiredForReset'
        ),
    })
    time_after_damaged_for_reset: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd9c67fe, original_name='TimeAfterDamagedForReset'
        ),
    })
    unknown: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0af428b4, original_name='Unknown'
        ),
    })
    barrier_starts_down: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4d3109e3, original_name='BarrierStartsDown'
        ),
    })
    health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0xcf90d15e, original_name='Health', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x7b71ae90, original_name='Vulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'DBAR'

    @classmethod
    def modules(cls) -> list[str]:
        return ['DestructibleBarrier.rel']

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
        if property_count != 31:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd4f7e71
        num_chunks_width = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7f551f7
        num_chunks_height = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x609c6240
        num_chunks_depth = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb29e159e
        chunk_size = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x014a0c36
        left_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90f55c5d
        center_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe1975355
        right_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x396660b4
        row_model_one_deep = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48e25884
        row_model_full_depth = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1abb2c7
        base_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1eb90d06
        destroyed_chunk_effect_1 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9d852dfe
        destroyed_chunk_effect_1_num_particles_to_generate = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x982d7fa8
        destroyed_chunk_effect_2 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e11003d
        destroyed_chunk_effect_2_num_particles_to_generate = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5371ac0d
        destroyed_chunk_effect_3 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x409d1b7c
        destroyed_chunk_effect_3_num_particles_to_generate = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4e749cb5
        destroyed_chunk_effect_4 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92485dfa
        destroyed_chunk_effect_4_num_particles_to_generate = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e4a9d27
        sound_effect_on_chunk_generated = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc2381a6
        sound_effect_on_chunk_destroyed = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6575a3d5
        sound_effect_on_move_down = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc91b0946
        sound_effect_on_move_up = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4b2d5a37
        sound_effect_on_stop = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x605847b9
        percentage_damage_required_for_reset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd9c67fe
        time_after_damaged_for_reset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0af428b4
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d3109e3
        barrier_starts_down = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf90d15e
        health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b71ae90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        return cls(editor_properties, num_chunks_width, num_chunks_height, num_chunks_depth, chunk_size, left_model, center_model, right_model, row_model_one_deep, row_model_full_depth, base_model, destroyed_chunk_effect_1, destroyed_chunk_effect_1_num_particles_to_generate, destroyed_chunk_effect_2, destroyed_chunk_effect_2_num_particles_to_generate, destroyed_chunk_effect_3, destroyed_chunk_effect_3_num_particles_to_generate, destroyed_chunk_effect_4, destroyed_chunk_effect_4_num_particles_to_generate, sound_effect_on_chunk_generated, sound_effect_on_chunk_destroyed, sound_effect_on_move_down, sound_effect_on_move_up, sound_effect_on_stop, percentage_damage_required_for_reset, time_after_damaged_for_reset, unknown, barrier_starts_down, health, vulnerability, actor_information)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x1f')  # 31 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcdO~q')  # 0xcd4f7e71
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_chunks_width))

        data.write(b'\xa7\xf5Q\xf7')  # 0xa7f551f7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_chunks_height))

        data.write(b'`\x9cb@')  # 0x609c6240
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_chunks_depth))

        data.write(b'\xb2\x9e\x15\x9e')  # 0xb29e159e
        data.write(b'\x00\x0c')  # size
        self.chunk_size.to_stream(data, game)

        data.write(b'\x01J\x0c6')  # 0x14a0c36
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.left_model))

        data.write(b'\x90\xf5\\]')  # 0x90f55c5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.center_model))

        data.write(b'\xe1\x97SU')  # 0xe1975355
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.right_model))

        data.write(b'9f`\xb4')  # 0x396660b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.row_model_one_deep))

        data.write(b'H\xe2X\x84')  # 0x48e25884
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.row_model_full_depth))

        data.write(b'\xf1\xab\xb2\xc7')  # 0xf1abb2c7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.base_model))

        data.write(b'\x1e\xb9\r\x06')  # 0x1eb90d06
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.destroyed_chunk_effect_1))

        data.write(b'\x9d\x85-\xfe')  # 0x9d852dfe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.destroyed_chunk_effect_1_num_particles_to_generate))

        data.write(b'\x98-\x7f\xa8')  # 0x982d7fa8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.destroyed_chunk_effect_2))

        data.write(b'.\x11\x00=')  # 0x2e11003d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.destroyed_chunk_effect_2_num_particles_to_generate))

        data.write(b'Sq\xac\r')  # 0x5371ac0d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.destroyed_chunk_effect_3))

        data.write(b'@\x9d\x1b|')  # 0x409d1b7c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.destroyed_chunk_effect_3_num_particles_to_generate))

        data.write(b'Nt\x9c\xb5')  # 0x4e749cb5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.destroyed_chunk_effect_4))

        data.write(b'\x92H]\xfa')  # 0x92485dfa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.destroyed_chunk_effect_4_num_particles_to_generate))

        data.write(b"nJ\x9d'")  # 0x6e4a9d27
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_effect_on_chunk_generated))

        data.write(b'\xbc#\x81\xa6')  # 0xbc2381a6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_effect_on_chunk_destroyed))

        data.write(b'eu\xa3\xd5')  # 0x6575a3d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_effect_on_move_down))

        data.write(b'\xc9\x1b\tF')  # 0xc91b0946
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_effect_on_move_up))

        data.write(b'K-Z7')  # 0x4b2d5a37
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_effect_on_stop))

        data.write(b'`XG\xb9')  # 0x605847b9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.percentage_damage_required_for_reset))

        data.write(b'\xcd\x9cg\xfe')  # 0xcd9c67fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_after_damaged_for_reset))

        data.write(b'\n\xf4(\xb4')  # 0xaf428b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'M1\t\xe3')  # 0x4d3109e3
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.barrier_starts_down))

        data.write(b'\xcf\x90\xd1^')  # 0xcf90d15e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{q\xae\x90')  # 0x7b71ae90
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vulnerability.to_stream(data, game)
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

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DestructibleBarrierJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            num_chunks_width=json_data['num_chunks_width'],
            num_chunks_height=json_data['num_chunks_height'],
            num_chunks_depth=json_data['num_chunks_depth'],
            chunk_size=Vector.from_json(json_data['chunk_size']),
            left_model=json_data['left_model'],
            center_model=json_data['center_model'],
            right_model=json_data['right_model'],
            row_model_one_deep=json_data['row_model_one_deep'],
            row_model_full_depth=json_data['row_model_full_depth'],
            base_model=json_data['base_model'],
            destroyed_chunk_effect_1=json_data['destroyed_chunk_effect_1'],
            destroyed_chunk_effect_1_num_particles_to_generate=json_data['destroyed_chunk_effect_1_num_particles_to_generate'],
            destroyed_chunk_effect_2=json_data['destroyed_chunk_effect_2'],
            destroyed_chunk_effect_2_num_particles_to_generate=json_data['destroyed_chunk_effect_2_num_particles_to_generate'],
            destroyed_chunk_effect_3=json_data['destroyed_chunk_effect_3'],
            destroyed_chunk_effect_3_num_particles_to_generate=json_data['destroyed_chunk_effect_3_num_particles_to_generate'],
            destroyed_chunk_effect_4=json_data['destroyed_chunk_effect_4'],
            destroyed_chunk_effect_4_num_particles_to_generate=json_data['destroyed_chunk_effect_4_num_particles_to_generate'],
            sound_effect_on_chunk_generated=json_data['sound_effect_on_chunk_generated'],
            sound_effect_on_chunk_destroyed=json_data['sound_effect_on_chunk_destroyed'],
            sound_effect_on_move_down=json_data['sound_effect_on_move_down'],
            sound_effect_on_move_up=json_data['sound_effect_on_move_up'],
            sound_effect_on_stop=json_data['sound_effect_on_stop'],
            percentage_damage_required_for_reset=json_data['percentage_damage_required_for_reset'],
            time_after_damaged_for_reset=json_data['time_after_damaged_for_reset'],
            unknown=json_data['unknown'],
            barrier_starts_down=json_data['barrier_starts_down'],
            health=HealthInfo.from_json(json_data['health']),
            vulnerability=DamageVulnerability.from_json(json_data['vulnerability']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'num_chunks_width': self.num_chunks_width,
            'num_chunks_height': self.num_chunks_height,
            'num_chunks_depth': self.num_chunks_depth,
            'chunk_size': self.chunk_size.to_json(),
            'left_model': self.left_model,
            'center_model': self.center_model,
            'right_model': self.right_model,
            'row_model_one_deep': self.row_model_one_deep,
            'row_model_full_depth': self.row_model_full_depth,
            'base_model': self.base_model,
            'destroyed_chunk_effect_1': self.destroyed_chunk_effect_1,
            'destroyed_chunk_effect_1_num_particles_to_generate': self.destroyed_chunk_effect_1_num_particles_to_generate,
            'destroyed_chunk_effect_2': self.destroyed_chunk_effect_2,
            'destroyed_chunk_effect_2_num_particles_to_generate': self.destroyed_chunk_effect_2_num_particles_to_generate,
            'destroyed_chunk_effect_3': self.destroyed_chunk_effect_3,
            'destroyed_chunk_effect_3_num_particles_to_generate': self.destroyed_chunk_effect_3_num_particles_to_generate,
            'destroyed_chunk_effect_4': self.destroyed_chunk_effect_4,
            'destroyed_chunk_effect_4_num_particles_to_generate': self.destroyed_chunk_effect_4_num_particles_to_generate,
            'sound_effect_on_chunk_generated': self.sound_effect_on_chunk_generated,
            'sound_effect_on_chunk_destroyed': self.sound_effect_on_chunk_destroyed,
            'sound_effect_on_move_down': self.sound_effect_on_move_down,
            'sound_effect_on_move_up': self.sound_effect_on_move_up,
            'sound_effect_on_stop': self.sound_effect_on_stop,
            'percentage_damage_required_for_reset': self.percentage_damage_required_for_reset,
            'time_after_damaged_for_reset': self.time_after_damaged_for_reset,
            'unknown': self.unknown,
            'barrier_starts_down': self.barrier_starts_down,
            'health': self.health.to_json(),
            'vulnerability': self.vulnerability.to_json(),
            'actor_information': self.actor_information.to_json(),
        }

    def _dependencies_for_left_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_model)

    def _dependencies_for_center_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.center_model)

    def _dependencies_for_right_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_model)

    def _dependencies_for_row_model_one_deep(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.row_model_one_deep)

    def _dependencies_for_row_model_full_depth(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.row_model_full_depth)

    def _dependencies_for_base_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.base_model)

    def _dependencies_for_destroyed_chunk_effect_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.destroyed_chunk_effect_1)

    def _dependencies_for_destroyed_chunk_effect_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.destroyed_chunk_effect_2)

    def _dependencies_for_destroyed_chunk_effect_3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.destroyed_chunk_effect_3)

    def _dependencies_for_destroyed_chunk_effect_4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.destroyed_chunk_effect_4)

    def _dependencies_for_sound_effect_on_chunk_generated(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_effect_on_chunk_generated)

    def _dependencies_for_sound_effect_on_chunk_destroyed(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_effect_on_chunk_destroyed)

    def _dependencies_for_sound_effect_on_move_down(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_effect_on_move_down)

    def _dependencies_for_sound_effect_on_move_up(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_effect_on_move_up)

    def _dependencies_for_sound_effect_on_stop(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_effect_on_stop)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_left_model, "left_model", "AssetId"),
            (self._dependencies_for_center_model, "center_model", "AssetId"),
            (self._dependencies_for_right_model, "right_model", "AssetId"),
            (self._dependencies_for_row_model_one_deep, "row_model_one_deep", "AssetId"),
            (self._dependencies_for_row_model_full_depth, "row_model_full_depth", "AssetId"),
            (self._dependencies_for_base_model, "base_model", "AssetId"),
            (self._dependencies_for_destroyed_chunk_effect_1, "destroyed_chunk_effect_1", "AssetId"),
            (self._dependencies_for_destroyed_chunk_effect_2, "destroyed_chunk_effect_2", "AssetId"),
            (self._dependencies_for_destroyed_chunk_effect_3, "destroyed_chunk_effect_3", "AssetId"),
            (self._dependencies_for_destroyed_chunk_effect_4, "destroyed_chunk_effect_4", "AssetId"),
            (self._dependencies_for_sound_effect_on_chunk_generated, "sound_effect_on_chunk_generated", "int"),
            (self._dependencies_for_sound_effect_on_chunk_destroyed, "sound_effect_on_chunk_destroyed", "int"),
            (self._dependencies_for_sound_effect_on_move_down, "sound_effect_on_move_down", "int"),
            (self._dependencies_for_sound_effect_on_move_up, "sound_effect_on_move_up", "int"),
            (self._dependencies_for_sound_effect_on_stop, "sound_effect_on_stop", "int"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DestructibleBarrier.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_chunk_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xcd4f7e71: ('num_chunks_width', structs.decode_BIG_l),
    0xa7f551f7: ('num_chunks_height', structs.decode_BIG_l),
    0x609c6240: ('num_chunks_depth', structs.decode_BIG_l),
    0xb29e159e: ('chunk_size', _decode_chunk_size),
    0x014a0c36: ('left_model', structs.decode_BIG_L),
    0x90f55c5d: ('center_model', structs.decode_BIG_L),
    0xe1975355: ('right_model', structs.decode_BIG_L),
    0x396660b4: ('row_model_one_deep', structs.decode_BIG_L),
    0x48e25884: ('row_model_full_depth', structs.decode_BIG_L),
    0xf1abb2c7: ('base_model', structs.decode_BIG_L),
    0x1eb90d06: ('destroyed_chunk_effect_1', structs.decode_BIG_L),
    0x9d852dfe: ('destroyed_chunk_effect_1_num_particles_to_generate', structs.decode_BIG_l),
    0x982d7fa8: ('destroyed_chunk_effect_2', structs.decode_BIG_L),
    0x2e11003d: ('destroyed_chunk_effect_2_num_particles_to_generate', structs.decode_BIG_l),
    0x5371ac0d: ('destroyed_chunk_effect_3', structs.decode_BIG_L),
    0x409d1b7c: ('destroyed_chunk_effect_3_num_particles_to_generate', structs.decode_BIG_l),
    0x4e749cb5: ('destroyed_chunk_effect_4', structs.decode_BIG_L),
    0x92485dfa: ('destroyed_chunk_effect_4_num_particles_to_generate', structs.decode_BIG_l),
    0x6e4a9d27: ('sound_effect_on_chunk_generated', structs.decode_BIG_l),
    0xbc2381a6: ('sound_effect_on_chunk_destroyed', structs.decode_BIG_l),
    0x6575a3d5: ('sound_effect_on_move_down', structs.decode_BIG_l),
    0xc91b0946: ('sound_effect_on_move_up', structs.decode_BIG_l),
    0x4b2d5a37: ('sound_effect_on_stop', structs.decode_BIG_l),
    0x605847b9: ('percentage_damage_required_for_reset', structs.decode_BIG_f),
    0xcd9c67fe: ('time_after_damaged_for_reset', structs.decode_BIG_f),
    0x0af428b4: ('unknown', structs.decode_BIG_f),
    0x4d3109e3: ('barrier_starts_down', structs.decode_BIG_bool_),
    0xcf90d15e: ('health', _decode_health),
    0x7b71ae90: ('vulnerability', _decode_vulnerability),
    0x7e397fed: ('actor_information', _decode_actor_information),
}
