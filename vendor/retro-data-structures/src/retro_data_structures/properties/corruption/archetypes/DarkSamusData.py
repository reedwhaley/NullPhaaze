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
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DarkSamusDataJson(typing_extensions.TypedDict):
        unknown_0xfbc0f458: float
        unknown_0x7d5486f6: float
        unknown_0xb6085553: float
        unknown_0xab0d65eb: float
        unknown_0x6051b64e: float
        unknown_0xfd5398eb: float
        unknown_0x7bc7ea45: float
        unknown_0xb09b39e0: float
        unknown_0xad9e0958: float
        unknown_0x66c2dafd: float
        unknown_0xf3dba20b: float
        unknown_0x754fd0a5: float
        unknown_0xbe130300: float
        unknown_0xa31633b8: float
        unknown_0x684ae01d: float
        unknown_0xa3ad3caf: int
        unknown_0xb1189341: int
        unknown_0x09a4f424: int
        unknown_0x9473cc9d: int
        unknown_0x4bf5e22c: float
        unknown_0xcd619082: float
        unknown_0x063d4327: float
        unknown_0x1b38739f: float
        unknown_0xd064a03a: float
        unknown_0x63cd8fea: float
        unknown_0xe559fd44: float
        unknown_0x2e052ee1: float
        unknown_0x33001e59: float
        unknown_0xf85ccdfc: float
        unknown_0x35c8d201: float
        unknown_0xb35ca0af: float
        unknown_0x7800730a: float
        unknown_0x650543b2: float
        unknown_0xae599017: float
        replenish_interrupt_threshold: float
        unknown_0xc377b3c1: float
        unknown_0x0df4b149: float
        melee_damage: json_util.JsonObject
        mega_blaster_damage: json_util.JsonObject
        mega_boost_trail_damage: json_util.JsonObject
        mega_boost_thru_player_damage: json_util.JsonObject
        phazon_barrage_beam_damage: json_util.JsonObject
        phazon_barrage_shockwave: json_util.JsonObject
        homing_missile_damage: json_util.JsonObject
        echo_health: float
        energy_wave_damage: json_util.JsonObject
        echo_blast_damage: json_util.JsonObject
        super_loop_damage: json_util.JsonObject
        shell_game_contact_damage: json_util.JsonObject
    

@dataclasses.dataclass()
class DarkSamusData(BaseProperty):
    unknown_0xfbc0f458: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfbc0f458, original_name='Unknown'
        ),
    })
    unknown_0x7d5486f6: float = dataclasses.field(default=625.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d5486f6, original_name='Unknown'
        ),
    })
    unknown_0xb6085553: float = dataclasses.field(default=625.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb6085553, original_name='Unknown'
        ),
    })
    unknown_0xab0d65eb: float = dataclasses.field(default=510.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xab0d65eb, original_name='Unknown'
        ),
    })
    unknown_0x6051b64e: float = dataclasses.field(default=400.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6051b64e, original_name='Unknown'
        ),
    })
    unknown_0xfd5398eb: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfd5398eb, original_name='Unknown'
        ),
    })
    unknown_0x7bc7ea45: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7bc7ea45, original_name='Unknown'
        ),
    })
    unknown_0xb09b39e0: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb09b39e0, original_name='Unknown'
        ),
    })
    unknown_0xad9e0958: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad9e0958, original_name='Unknown'
        ),
    })
    unknown_0x66c2dafd: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x66c2dafd, original_name='Unknown'
        ),
    })
    unknown_0xf3dba20b: float = dataclasses.field(default=11.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf3dba20b, original_name='Unknown'
        ),
    })
    unknown_0x754fd0a5: float = dataclasses.field(default=11.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x754fd0a5, original_name='Unknown'
        ),
    })
    unknown_0xbe130300: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbe130300, original_name='Unknown'
        ),
    })
    unknown_0xa31633b8: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa31633b8, original_name='Unknown'
        ),
    })
    unknown_0x684ae01d: float = dataclasses.field(default=9.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x684ae01d, original_name='Unknown'
        ),
    })
    unknown_0xa3ad3caf: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa3ad3caf, original_name='Unknown'
        ),
    })
    unknown_0xb1189341: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb1189341, original_name='Unknown'
        ),
    })
    unknown_0x09a4f424: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0x09a4f424, original_name='Unknown'
        ),
    })
    unknown_0x9473cc9d: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9473cc9d, original_name='Unknown'
        ),
    })
    unknown_0x4bf5e22c: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4bf5e22c, original_name='Unknown'
        ),
    })
    unknown_0xcd619082: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd619082, original_name='Unknown'
        ),
    })
    unknown_0x063d4327: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x063d4327, original_name='Unknown'
        ),
    })
    unknown_0x1b38739f: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b38739f, original_name='Unknown'
        ),
    })
    unknown_0xd064a03a: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd064a03a, original_name='Unknown'
        ),
    })
    unknown_0x63cd8fea: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x63cd8fea, original_name='Unknown'
        ),
    })
    unknown_0xe559fd44: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe559fd44, original_name='Unknown'
        ),
    })
    unknown_0x2e052ee1: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2e052ee1, original_name='Unknown'
        ),
    })
    unknown_0x33001e59: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x33001e59, original_name='Unknown'
        ),
    })
    unknown_0xf85ccdfc: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf85ccdfc, original_name='Unknown'
        ),
    })
    unknown_0x35c8d201: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x35c8d201, original_name='Unknown'
        ),
    })
    unknown_0xb35ca0af: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb35ca0af, original_name='Unknown'
        ),
    })
    unknown_0x7800730a: float = dataclasses.field(default=1.2999999523162842, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7800730a, original_name='Unknown'
        ),
    })
    unknown_0x650543b2: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x650543b2, original_name='Unknown'
        ),
    })
    unknown_0xae599017: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xae599017, original_name='Unknown'
        ),
    })
    replenish_interrupt_threshold: float = dataclasses.field(default=750.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x781cc1e9, original_name='ReplenishInterruptThreshold'
        ),
    })
    unknown_0xc377b3c1: float = dataclasses.field(default=375.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc377b3c1, original_name='Unknown'
        ),
    })
    unknown_0x0df4b149: float = dataclasses.field(default=21.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0df4b149, original_name='Unknown'
        ),
    })
    melee_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xc9416034, original_name='MeleeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    mega_blaster_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x414046a8, original_name='MegaBlasterDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    mega_boost_trail_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xa0e0d7f8, original_name='MegaBoostTrailDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    mega_boost_thru_player_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x429c17bd, original_name='MegaBoostThruPlayerDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_barrage_beam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x995aa633, original_name='PhazonBarrageBeamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_barrage_shockwave: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x55571199, original_name='PhazonBarrageShockwave', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    homing_missile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x598c0005, original_name='HomingMissileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    echo_health: float = dataclasses.field(default=360.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4bc4ae5c, original_name='EchoHealth'
        ),
    })
    energy_wave_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x93ecf945, original_name='EnergyWaveDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    echo_blast_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xaef2f857, original_name='EchoBlastDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    super_loop_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xd74fc76c, original_name='SuperLoopDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    shell_game_contact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xcaa6ecee, original_name='ShellGameContactDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
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
        if property_count != 49:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbc0f458
        unknown_0xfbc0f458 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d5486f6
        unknown_0x7d5486f6 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6085553
        unknown_0xb6085553 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab0d65eb
        unknown_0xab0d65eb = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6051b64e
        unknown_0x6051b64e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd5398eb
        unknown_0xfd5398eb = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7bc7ea45
        unknown_0x7bc7ea45 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb09b39e0
        unknown_0xb09b39e0 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad9e0958
        unknown_0xad9e0958 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66c2dafd
        unknown_0x66c2dafd = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3dba20b
        unknown_0xf3dba20b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x754fd0a5
        unknown_0x754fd0a5 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe130300
        unknown_0xbe130300 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa31633b8
        unknown_0xa31633b8 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x684ae01d
        unknown_0x684ae01d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3ad3caf
        unknown_0xa3ad3caf = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb1189341
        unknown_0xb1189341 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09a4f424
        unknown_0x09a4f424 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9473cc9d
        unknown_0x9473cc9d = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4bf5e22c
        unknown_0x4bf5e22c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd619082
        unknown_0xcd619082 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x063d4327
        unknown_0x063d4327 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b38739f
        unknown_0x1b38739f = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd064a03a
        unknown_0xd064a03a = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x63cd8fea
        unknown_0x63cd8fea = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe559fd44
        unknown_0xe559fd44 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e052ee1
        unknown_0x2e052ee1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33001e59
        unknown_0x33001e59 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf85ccdfc
        unknown_0xf85ccdfc = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35c8d201
        unknown_0x35c8d201 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb35ca0af
        unknown_0xb35ca0af = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7800730a
        unknown_0x7800730a = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x650543b2
        unknown_0x650543b2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae599017
        unknown_0xae599017 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x781cc1e9
        replenish_interrupt_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc377b3c1
        unknown_0xc377b3c1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0df4b149
        unknown_0x0df4b149 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc9416034
        melee_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x414046a8
        mega_blaster_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0e0d7f8
        mega_boost_trail_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x429c17bd
        mega_boost_thru_player_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x995aa633
        phazon_barrage_beam_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55571199
        phazon_barrage_shockwave = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x598c0005
        homing_missile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4bc4ae5c
        echo_health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93ecf945
        energy_wave_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaef2f857
        echo_blast_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd74fc76c
        super_loop_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcaa6ecee
        shell_game_contact_damage = DamageInfo.from_stream(data, game, property_size)
    
        return cls(unknown_0xfbc0f458, unknown_0x7d5486f6, unknown_0xb6085553, unknown_0xab0d65eb, unknown_0x6051b64e, unknown_0xfd5398eb, unknown_0x7bc7ea45, unknown_0xb09b39e0, unknown_0xad9e0958, unknown_0x66c2dafd, unknown_0xf3dba20b, unknown_0x754fd0a5, unknown_0xbe130300, unknown_0xa31633b8, unknown_0x684ae01d, unknown_0xa3ad3caf, unknown_0xb1189341, unknown_0x09a4f424, unknown_0x9473cc9d, unknown_0x4bf5e22c, unknown_0xcd619082, unknown_0x063d4327, unknown_0x1b38739f, unknown_0xd064a03a, unknown_0x63cd8fea, unknown_0xe559fd44, unknown_0x2e052ee1, unknown_0x33001e59, unknown_0xf85ccdfc, unknown_0x35c8d201, unknown_0xb35ca0af, unknown_0x7800730a, unknown_0x650543b2, unknown_0xae599017, replenish_interrupt_threshold, unknown_0xc377b3c1, unknown_0x0df4b149, melee_damage, mega_blaster_damage, mega_boost_trail_damage, mega_boost_thru_player_damage, phazon_barrage_beam_damage, phazon_barrage_shockwave, homing_missile_damage, echo_health, energy_wave_damage, echo_blast_damage, super_loop_damage, shell_game_contact_damage)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x001')  # 49 properties

        data.write(b'\xfb\xc0\xf4X')  # 0xfbc0f458
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfbc0f458))

        data.write(b'}T\x86\xf6')  # 0x7d5486f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7d5486f6))

        data.write(b'\xb6\x08US')  # 0xb6085553
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb6085553))

        data.write(b'\xab\re\xeb')  # 0xab0d65eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xab0d65eb))

        data.write(b'`Q\xb6N')  # 0x6051b64e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6051b64e))

        data.write(b'\xfdS\x98\xeb')  # 0xfd5398eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfd5398eb))

        data.write(b'{\xc7\xeaE')  # 0x7bc7ea45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7bc7ea45))

        data.write(b'\xb0\x9b9\xe0')  # 0xb09b39e0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb09b39e0))

        data.write(b'\xad\x9e\tX')  # 0xad9e0958
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xad9e0958))

        data.write(b'f\xc2\xda\xfd')  # 0x66c2dafd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x66c2dafd))

        data.write(b'\xf3\xdb\xa2\x0b')  # 0xf3dba20b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf3dba20b))

        data.write(b'uO\xd0\xa5')  # 0x754fd0a5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x754fd0a5))

        data.write(b'\xbe\x13\x03\x00')  # 0xbe130300
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbe130300))

        data.write(b'\xa3\x163\xb8')  # 0xa31633b8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa31633b8))

        data.write(b'hJ\xe0\x1d')  # 0x684ae01d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x684ae01d))

        data.write(b'\xa3\xad<\xaf')  # 0xa3ad3caf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa3ad3caf))

        data.write(b'\xb1\x18\x93A')  # 0xb1189341
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb1189341))

        data.write(b'\t\xa4\xf4$')  # 0x9a4f424
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x09a4f424))

        data.write(b'\x94s\xcc\x9d')  # 0x9473cc9d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9473cc9d))

        data.write(b'K\xf5\xe2,')  # 0x4bf5e22c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4bf5e22c))

        data.write(b'\xcda\x90\x82')  # 0xcd619082
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd619082))

        data.write(b"\x06=C'")  # 0x63d4327
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x063d4327))

        data.write(b'\x1b8s\x9f')  # 0x1b38739f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1b38739f))

        data.write(b'\xd0d\xa0:')  # 0xd064a03a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd064a03a))

        data.write(b'c\xcd\x8f\xea')  # 0x63cd8fea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x63cd8fea))

        data.write(b'\xe5Y\xfdD')  # 0xe559fd44
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe559fd44))

        data.write(b'.\x05.\xe1')  # 0x2e052ee1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2e052ee1))

        data.write(b'3\x00\x1eY')  # 0x33001e59
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x33001e59))

        data.write(b'\xf8\\\xcd\xfc')  # 0xf85ccdfc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf85ccdfc))

        data.write(b'5\xc8\xd2\x01')  # 0x35c8d201
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x35c8d201))

        data.write(b'\xb3\\\xa0\xaf')  # 0xb35ca0af
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb35ca0af))

        data.write(b'x\x00s\n')  # 0x7800730a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7800730a))

        data.write(b'e\x05C\xb2')  # 0x650543b2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x650543b2))

        data.write(b'\xaeY\x90\x17')  # 0xae599017
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xae599017))

        data.write(b'x\x1c\xc1\xe9')  # 0x781cc1e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.replenish_interrupt_threshold))

        data.write(b'\xc3w\xb3\xc1')  # 0xc377b3c1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc377b3c1))

        data.write(b'\r\xf4\xb1I')  # 0xdf4b149
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0df4b149))

        data.write(b'\xc9A`4')  # 0xc9416034
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'A@F\xa8')  # 0x414046a8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mega_blaster_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa0\xe0\xd7\xf8')  # 0xa0e0d7f8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mega_boost_trail_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'B\x9c\x17\xbd')  # 0x429c17bd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mega_boost_thru_player_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x99Z\xa63')  # 0x995aa633
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_barrage_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'UW\x11\x99')  # 0x55571199
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_barrage_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Y\x8c\x00\x05')  # 0x598c0005
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.homing_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'K\xc4\xae\\')  # 0x4bc4ae5c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_health))

        data.write(b'\x93\xec\xf9E')  # 0x93ecf945
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_wave_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xae\xf2\xf8W')  # 0xaef2f857
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.echo_blast_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd7O\xc7l')  # 0xd74fc76c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.super_loop_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xca\xa6\xec\xee')  # 0xcaa6ecee
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shell_game_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkSamusDataJson", data)
        return cls(
            unknown_0xfbc0f458=json_data['unknown_0xfbc0f458'],
            unknown_0x7d5486f6=json_data['unknown_0x7d5486f6'],
            unknown_0xb6085553=json_data['unknown_0xb6085553'],
            unknown_0xab0d65eb=json_data['unknown_0xab0d65eb'],
            unknown_0x6051b64e=json_data['unknown_0x6051b64e'],
            unknown_0xfd5398eb=json_data['unknown_0xfd5398eb'],
            unknown_0x7bc7ea45=json_data['unknown_0x7bc7ea45'],
            unknown_0xb09b39e0=json_data['unknown_0xb09b39e0'],
            unknown_0xad9e0958=json_data['unknown_0xad9e0958'],
            unknown_0x66c2dafd=json_data['unknown_0x66c2dafd'],
            unknown_0xf3dba20b=json_data['unknown_0xf3dba20b'],
            unknown_0x754fd0a5=json_data['unknown_0x754fd0a5'],
            unknown_0xbe130300=json_data['unknown_0xbe130300'],
            unknown_0xa31633b8=json_data['unknown_0xa31633b8'],
            unknown_0x684ae01d=json_data['unknown_0x684ae01d'],
            unknown_0xa3ad3caf=json_data['unknown_0xa3ad3caf'],
            unknown_0xb1189341=json_data['unknown_0xb1189341'],
            unknown_0x09a4f424=json_data['unknown_0x09a4f424'],
            unknown_0x9473cc9d=json_data['unknown_0x9473cc9d'],
            unknown_0x4bf5e22c=json_data['unknown_0x4bf5e22c'],
            unknown_0xcd619082=json_data['unknown_0xcd619082'],
            unknown_0x063d4327=json_data['unknown_0x063d4327'],
            unknown_0x1b38739f=json_data['unknown_0x1b38739f'],
            unknown_0xd064a03a=json_data['unknown_0xd064a03a'],
            unknown_0x63cd8fea=json_data['unknown_0x63cd8fea'],
            unknown_0xe559fd44=json_data['unknown_0xe559fd44'],
            unknown_0x2e052ee1=json_data['unknown_0x2e052ee1'],
            unknown_0x33001e59=json_data['unknown_0x33001e59'],
            unknown_0xf85ccdfc=json_data['unknown_0xf85ccdfc'],
            unknown_0x35c8d201=json_data['unknown_0x35c8d201'],
            unknown_0xb35ca0af=json_data['unknown_0xb35ca0af'],
            unknown_0x7800730a=json_data['unknown_0x7800730a'],
            unknown_0x650543b2=json_data['unknown_0x650543b2'],
            unknown_0xae599017=json_data['unknown_0xae599017'],
            replenish_interrupt_threshold=json_data['replenish_interrupt_threshold'],
            unknown_0xc377b3c1=json_data['unknown_0xc377b3c1'],
            unknown_0x0df4b149=json_data['unknown_0x0df4b149'],
            melee_damage=DamageInfo.from_json(json_data['melee_damage']),
            mega_blaster_damage=DamageInfo.from_json(json_data['mega_blaster_damage']),
            mega_boost_trail_damage=DamageInfo.from_json(json_data['mega_boost_trail_damage']),
            mega_boost_thru_player_damage=DamageInfo.from_json(json_data['mega_boost_thru_player_damage']),
            phazon_barrage_beam_damage=DamageInfo.from_json(json_data['phazon_barrage_beam_damage']),
            phazon_barrage_shockwave=ShockWaveInfo.from_json(json_data['phazon_barrage_shockwave']),
            homing_missile_damage=DamageInfo.from_json(json_data['homing_missile_damage']),
            echo_health=json_data['echo_health'],
            energy_wave_damage=DamageInfo.from_json(json_data['energy_wave_damage']),
            echo_blast_damage=DamageInfo.from_json(json_data['echo_blast_damage']),
            super_loop_damage=DamageInfo.from_json(json_data['super_loop_damage']),
            shell_game_contact_damage=DamageInfo.from_json(json_data['shell_game_contact_damage']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0xfbc0f458': self.unknown_0xfbc0f458,
            'unknown_0x7d5486f6': self.unknown_0x7d5486f6,
            'unknown_0xb6085553': self.unknown_0xb6085553,
            'unknown_0xab0d65eb': self.unknown_0xab0d65eb,
            'unknown_0x6051b64e': self.unknown_0x6051b64e,
            'unknown_0xfd5398eb': self.unknown_0xfd5398eb,
            'unknown_0x7bc7ea45': self.unknown_0x7bc7ea45,
            'unknown_0xb09b39e0': self.unknown_0xb09b39e0,
            'unknown_0xad9e0958': self.unknown_0xad9e0958,
            'unknown_0x66c2dafd': self.unknown_0x66c2dafd,
            'unknown_0xf3dba20b': self.unknown_0xf3dba20b,
            'unknown_0x754fd0a5': self.unknown_0x754fd0a5,
            'unknown_0xbe130300': self.unknown_0xbe130300,
            'unknown_0xa31633b8': self.unknown_0xa31633b8,
            'unknown_0x684ae01d': self.unknown_0x684ae01d,
            'unknown_0xa3ad3caf': self.unknown_0xa3ad3caf,
            'unknown_0xb1189341': self.unknown_0xb1189341,
            'unknown_0x09a4f424': self.unknown_0x09a4f424,
            'unknown_0x9473cc9d': self.unknown_0x9473cc9d,
            'unknown_0x4bf5e22c': self.unknown_0x4bf5e22c,
            'unknown_0xcd619082': self.unknown_0xcd619082,
            'unknown_0x063d4327': self.unknown_0x063d4327,
            'unknown_0x1b38739f': self.unknown_0x1b38739f,
            'unknown_0xd064a03a': self.unknown_0xd064a03a,
            'unknown_0x63cd8fea': self.unknown_0x63cd8fea,
            'unknown_0xe559fd44': self.unknown_0xe559fd44,
            'unknown_0x2e052ee1': self.unknown_0x2e052ee1,
            'unknown_0x33001e59': self.unknown_0x33001e59,
            'unknown_0xf85ccdfc': self.unknown_0xf85ccdfc,
            'unknown_0x35c8d201': self.unknown_0x35c8d201,
            'unknown_0xb35ca0af': self.unknown_0xb35ca0af,
            'unknown_0x7800730a': self.unknown_0x7800730a,
            'unknown_0x650543b2': self.unknown_0x650543b2,
            'unknown_0xae599017': self.unknown_0xae599017,
            'replenish_interrupt_threshold': self.replenish_interrupt_threshold,
            'unknown_0xc377b3c1': self.unknown_0xc377b3c1,
            'unknown_0x0df4b149': self.unknown_0x0df4b149,
            'melee_damage': self.melee_damage.to_json(),
            'mega_blaster_damage': self.mega_blaster_damage.to_json(),
            'mega_boost_trail_damage': self.mega_boost_trail_damage.to_json(),
            'mega_boost_thru_player_damage': self.mega_boost_thru_player_damage.to_json(),
            'phazon_barrage_beam_damage': self.phazon_barrage_beam_damage.to_json(),
            'phazon_barrage_shockwave': self.phazon_barrage_shockwave.to_json(),
            'homing_missile_damage': self.homing_missile_damage.to_json(),
            'echo_health': self.echo_health,
            'energy_wave_damage': self.energy_wave_damage.to_json(),
            'echo_blast_damage': self.echo_blast_damage.to_json(),
            'super_loop_damage': self.super_loop_damage.to_json(),
            'shell_game_contact_damage': self.shell_game_contact_damage.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self.phazon_barrage_shockwave.dependencies_for(asset_manager)


def _decode_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_mega_blaster_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_mega_boost_trail_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_mega_boost_thru_player_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_barrage_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_barrage_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_homing_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_energy_wave_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_echo_blast_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_super_loop_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_shell_game_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xfbc0f458: ('unknown_0xfbc0f458', structs.decode_BIG_f),
    0x7d5486f6: ('unknown_0x7d5486f6', structs.decode_BIG_f),
    0xb6085553: ('unknown_0xb6085553', structs.decode_BIG_f),
    0xab0d65eb: ('unknown_0xab0d65eb', structs.decode_BIG_f),
    0x6051b64e: ('unknown_0x6051b64e', structs.decode_BIG_f),
    0xfd5398eb: ('unknown_0xfd5398eb', structs.decode_BIG_f),
    0x7bc7ea45: ('unknown_0x7bc7ea45', structs.decode_BIG_f),
    0xb09b39e0: ('unknown_0xb09b39e0', structs.decode_BIG_f),
    0xad9e0958: ('unknown_0xad9e0958', structs.decode_BIG_f),
    0x66c2dafd: ('unknown_0x66c2dafd', structs.decode_BIG_f),
    0xf3dba20b: ('unknown_0xf3dba20b', structs.decode_BIG_f),
    0x754fd0a5: ('unknown_0x754fd0a5', structs.decode_BIG_f),
    0xbe130300: ('unknown_0xbe130300', structs.decode_BIG_f),
    0xa31633b8: ('unknown_0xa31633b8', structs.decode_BIG_f),
    0x684ae01d: ('unknown_0x684ae01d', structs.decode_BIG_f),
    0xa3ad3caf: ('unknown_0xa3ad3caf', structs.decode_BIG_l),
    0xb1189341: ('unknown_0xb1189341', structs.decode_BIG_l),
    0x09a4f424: ('unknown_0x09a4f424', structs.decode_BIG_l),
    0x9473cc9d: ('unknown_0x9473cc9d', structs.decode_BIG_l),
    0x4bf5e22c: ('unknown_0x4bf5e22c', structs.decode_BIG_f),
    0xcd619082: ('unknown_0xcd619082', structs.decode_BIG_f),
    0x063d4327: ('unknown_0x063d4327', structs.decode_BIG_f),
    0x1b38739f: ('unknown_0x1b38739f', structs.decode_BIG_f),
    0xd064a03a: ('unknown_0xd064a03a', structs.decode_BIG_f),
    0x63cd8fea: ('unknown_0x63cd8fea', structs.decode_BIG_f),
    0xe559fd44: ('unknown_0xe559fd44', structs.decode_BIG_f),
    0x2e052ee1: ('unknown_0x2e052ee1', structs.decode_BIG_f),
    0x33001e59: ('unknown_0x33001e59', structs.decode_BIG_f),
    0xf85ccdfc: ('unknown_0xf85ccdfc', structs.decode_BIG_f),
    0x35c8d201: ('unknown_0x35c8d201', structs.decode_BIG_f),
    0xb35ca0af: ('unknown_0xb35ca0af', structs.decode_BIG_f),
    0x7800730a: ('unknown_0x7800730a', structs.decode_BIG_f),
    0x650543b2: ('unknown_0x650543b2', structs.decode_BIG_f),
    0xae599017: ('unknown_0xae599017', structs.decode_BIG_f),
    0x781cc1e9: ('replenish_interrupt_threshold', structs.decode_BIG_f),
    0xc377b3c1: ('unknown_0xc377b3c1', structs.decode_BIG_f),
    0x0df4b149: ('unknown_0x0df4b149', structs.decode_BIG_f),
    0xc9416034: ('melee_damage', _decode_melee_damage),
    0x414046a8: ('mega_blaster_damage', _decode_mega_blaster_damage),
    0xa0e0d7f8: ('mega_boost_trail_damage', _decode_mega_boost_trail_damage),
    0x429c17bd: ('mega_boost_thru_player_damage', _decode_mega_boost_thru_player_damage),
    0x995aa633: ('phazon_barrage_beam_damage', _decode_phazon_barrage_beam_damage),
    0x55571199: ('phazon_barrage_shockwave', _decode_phazon_barrage_shockwave),
    0x598c0005: ('homing_missile_damage', _decode_homing_missile_damage),
    0x4bc4ae5c: ('echo_health', structs.decode_BIG_f),
    0x93ecf945: ('energy_wave_damage', _decode_energy_wave_damage),
    0xaef2f857: ('echo_blast_damage', _decode_echo_blast_damage),
    0xd74fc76c: ('super_loop_damage', _decode_super_loop_damage),
    0xcaa6ecee: ('shell_game_contact_damage', _decode_shell_game_contact_damage),
}
