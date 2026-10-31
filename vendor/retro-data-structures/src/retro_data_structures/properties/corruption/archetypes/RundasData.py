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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability

if typing.TYPE_CHECKING:
    class RundasDataJson(typing_extensions.TypedDict):
        unknown_0x1aeb498d: float
        unknown_0x9c7f3b23: float
        unknown_0x706186d2: float
        unknown_0x3f5d6545: float
        unknown_0x59a93220: float
        unknown_0x6cc73ec1: float
        grapple_struggle_time: float
        hypermode_vulnerability: json_util.JsonObject
        armor_vulnerability: json_util.JsonObject
        damage_info_0x8d4a2668: json_util.JsonObject
        ice_grenade_hp: float
        ice_grenade_damage: json_util.JsonObject
        ice_sword_damage: json_util.JsonObject
        ice_sword_range_min: float
        ice_sword_range_max: float
        unknown_0x050cb86e: float
        unknown_0xe36c178f: float
        damage_info_0x3063bbf1: json_util.JsonObject
        morning_star_damage: json_util.JsonObject
        rush_range_min: float
        rush_range_max: float
        unknown_0x3be0a66b: float
        unknown_0xf586836f: float
        unknown_0x7312f1c1: float
        unknown_0x775362cf: float
        unknown_0xf1c71061: float
        missile_freeze_distance: float
        surfing_projectile_damage: json_util.JsonObject
        min_surf_attack_burst: int
        max_surf_attack_burst: int
        min_surf_attack_burst_time: float
        max_surf_attack_burst_time: float
        min_surf_attack_time: float
        max_surf_attack_time: float
        surf_height_min: float
        surf_height_max: float
        elevation_timer: float
        shard_storm_timer: float
        ice_summon_timer: float
        rush_timer: float
        unknown_0xc758f52e: float
        surf_timer: float
        unknown_0xf80fcae2: float
        is_gandrayda: bool
        unknown_0x691746f2: float
        unknown_0xcf197148: float
        unknown_0x9ee0ca15: float
        unknown_0xfc629f72: float
        unknown_0xef2779d9: float
    

@dataclasses.dataclass()
class RundasData(BaseProperty):
    unknown_0x1aeb498d: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1aeb498d, original_name='Unknown'
        ),
    })
    unknown_0x9c7f3b23: float = dataclasses.field(default=225.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9c7f3b23, original_name='Unknown'
        ),
    })
    unknown_0x706186d2: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x706186d2, original_name='Unknown'
        ),
    })
    unknown_0x3f5d6545: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3f5d6545, original_name='Unknown'
        ),
    })
    unknown_0x59a93220: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x59a93220, original_name='Unknown'
        ),
    })
    unknown_0x6cc73ec1: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6cc73ec1, original_name='Unknown'
        ),
    })
    grapple_struggle_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x57f0a2a7, original_name='GrappleStruggleTime'
        ),
    })
    hypermode_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xd1522831, original_name='HypermodeVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    armor_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x896d5bd9, original_name='ArmorVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    damage_info_0x8d4a2668: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x8d4a2668, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    ice_grenade_hp: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf41394f6, original_name='IceGrenadeHP'
        ),
    })
    ice_grenade_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xb1b44917, original_name='IceGrenadeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    ice_sword_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x7fbc7e81, original_name='IceSwordDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    ice_sword_range_min: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff944885, original_name='IceSwordRangeMin'
        ),
    })
    ice_sword_range_max: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x19f4e764, original_name='IceSwordRangeMax'
        ),
    })
    unknown_0x050cb86e: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x050cb86e, original_name='Unknown'
        ),
    })
    unknown_0xe36c178f: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe36c178f, original_name='Unknown'
        ),
    })
    damage_info_0x3063bbf1: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x3063bbf1, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    morning_star_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x5997ebe1, original_name='MorningStarDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    rush_range_min: float = dataclasses.field(default=35.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc922f0e0, original_name='RushRangeMin'
        ),
    })
    rush_range_max: float = dataclasses.field(default=200.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2f425f01, original_name='RushRangeMax'
        ),
    })
    unknown_0x3be0a66b: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3be0a66b, original_name='Unknown'
        ),
    })
    unknown_0xf586836f: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf586836f, original_name='Unknown'
        ),
    })
    unknown_0x7312f1c1: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7312f1c1, original_name='Unknown'
        ),
    })
    unknown_0x775362cf: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x775362cf, original_name='Unknown'
        ),
    })
    unknown_0xf1c71061: float = dataclasses.field(default=0.949999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf1c71061, original_name='Unknown'
        ),
    })
    missile_freeze_distance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3f196c78, original_name='MissileFreezeDistance'
        ),
    })
    surfing_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x78df0b7d, original_name='SurfingProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    min_surf_attack_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xca04d756, original_name='MinSurfAttackBurst'
        ),
    })
    max_surf_attack_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd94131fd, original_name='MaxSurfAttackBurst'
        ),
    })
    min_surf_attack_burst_time: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x821b0c82, original_name='MinSurfAttackBurstTime'
        ),
    })
    max_surf_attack_burst_time: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe4fe6af6, original_name='MaxSurfAttackBurstTime'
        ),
    })
    min_surf_attack_time: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7ef4effe, original_name='MinSurfAttackTime'
        ),
    })
    max_surf_attack_time: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3fe3d078, original_name='MaxSurfAttackTime'
        ),
    })
    surf_height_min: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1dcc7e61, original_name='SurfHeightMin'
        ),
    })
    surf_height_max: float = dataclasses.field(default=11.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfbacd180, original_name='SurfHeightMax'
        ),
    })
    elevation_timer: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe4cd7924, original_name='ElevationTimer'
        ),
    })
    shard_storm_timer: float = dataclasses.field(default=7.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3056ffba, original_name='ShardStormTimer'
        ),
    })
    ice_summon_timer: float = dataclasses.field(default=18.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x595e38d6, original_name='IceSummonTimer'
        ),
    })
    rush_timer: float = dataclasses.field(default=14.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6d0ba041, original_name='RushTimer'
        ),
    })
    unknown_0xc758f52e: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc758f52e, original_name='Unknown'
        ),
    })
    surf_timer: float = dataclasses.field(default=17.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x39d7265e, original_name='SurfTimer'
        ),
    })
    unknown_0xf80fcae2: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf80fcae2, original_name='Unknown'
        ),
    })
    is_gandrayda: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x531a8c85, original_name='IsGandrayda'
        ),
    })
    unknown_0x691746f2: float = dataclasses.field(default=125.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x691746f2, original_name='Unknown'
        ),
    })
    unknown_0xcf197148: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf197148, original_name='Unknown'
        ),
    })
    unknown_0x9ee0ca15: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9ee0ca15, original_name='Unknown'
        ),
    })
    unknown_0xfc629f72: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfc629f72, original_name='Unknown'
        ),
    })
    unknown_0xef2779d9: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xef2779d9, original_name='Unknown'
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
        assert property_id == 0x1aeb498d
        unknown_0x1aeb498d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c7f3b23
        unknown_0x9c7f3b23 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x706186d2
        unknown_0x706186d2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3f5d6545
        unknown_0x3f5d6545 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59a93220
        unknown_0x59a93220 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6cc73ec1
        unknown_0x6cc73ec1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57f0a2a7
        grapple_struggle_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd1522831
        hypermode_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x896d5bd9
        armor_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d4a2668
        damage_info_0x8d4a2668 = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf41394f6
        ice_grenade_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb1b44917
        ice_grenade_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fbc7e81
        ice_sword_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff944885
        ice_sword_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19f4e764
        ice_sword_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x050cb86e
        unknown_0x050cb86e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe36c178f
        unknown_0xe36c178f = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3063bbf1
        damage_info_0x3063bbf1 = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5997ebe1
        morning_star_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc922f0e0
        rush_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f425f01
        rush_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3be0a66b
        unknown_0x3be0a66b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf586836f
        unknown_0xf586836f = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7312f1c1
        unknown_0x7312f1c1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x775362cf
        unknown_0x775362cf = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1c71061
        unknown_0xf1c71061 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3f196c78
        missile_freeze_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78df0b7d
        surfing_projectile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca04d756
        min_surf_attack_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd94131fd
        max_surf_attack_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x821b0c82
        min_surf_attack_burst_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe4fe6af6
        max_surf_attack_burst_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ef4effe
        min_surf_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3fe3d078
        max_surf_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1dcc7e61
        surf_height_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbacd180
        surf_height_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe4cd7924
        elevation_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3056ffba
        shard_storm_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x595e38d6
        ice_summon_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d0ba041
        rush_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc758f52e
        unknown_0xc758f52e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39d7265e
        surf_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf80fcae2
        unknown_0xf80fcae2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531a8c85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x691746f2
        unknown_0x691746f2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf197148
        unknown_0xcf197148 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ee0ca15
        unknown_0x9ee0ca15 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc629f72
        unknown_0xfc629f72 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef2779d9
        unknown_0xef2779d9 = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(unknown_0x1aeb498d, unknown_0x9c7f3b23, unknown_0x706186d2, unknown_0x3f5d6545, unknown_0x59a93220, unknown_0x6cc73ec1, grapple_struggle_time, hypermode_vulnerability, armor_vulnerability, damage_info_0x8d4a2668, ice_grenade_hp, ice_grenade_damage, ice_sword_damage, ice_sword_range_min, ice_sword_range_max, unknown_0x050cb86e, unknown_0xe36c178f, damage_info_0x3063bbf1, morning_star_damage, rush_range_min, rush_range_max, unknown_0x3be0a66b, unknown_0xf586836f, unknown_0x7312f1c1, unknown_0x775362cf, unknown_0xf1c71061, missile_freeze_distance, surfing_projectile_damage, min_surf_attack_burst, max_surf_attack_burst, min_surf_attack_burst_time, max_surf_attack_burst_time, min_surf_attack_time, max_surf_attack_time, surf_height_min, surf_height_max, elevation_timer, shard_storm_timer, ice_summon_timer, rush_timer, unknown_0xc758f52e, surf_timer, unknown_0xf80fcae2, is_gandrayda, unknown_0x691746f2, unknown_0xcf197148, unknown_0x9ee0ca15, unknown_0xfc629f72, unknown_0xef2779d9)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x001')  # 49 properties

        data.write(b'\x1a\xebI\x8d')  # 0x1aeb498d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1aeb498d))

        data.write(b'\x9c\x7f;#')  # 0x9c7f3b23
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9c7f3b23))

        data.write(b'pa\x86\xd2')  # 0x706186d2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x706186d2))

        data.write(b'?]eE')  # 0x3f5d6545
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3f5d6545))

        data.write(b'Y\xa92 ')  # 0x59a93220
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x59a93220))

        data.write(b'l\xc7>\xc1')  # 0x6cc73ec1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6cc73ec1))

        data.write(b'W\xf0\xa2\xa7')  # 0x57f0a2a7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_struggle_time))

        data.write(b'\xd1R(1')  # 0xd1522831
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x89m[\xd9')  # 0x896d5bd9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.armor_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8dJ&h')  # 0x8d4a2668
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info_0x8d4a2668.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf4\x13\x94\xf6')  # 0xf41394f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ice_grenade_hp))

        data.write(b'\xb1\xb4I\x17')  # 0xb1b44917
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ice_grenade_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x7f\xbc~\x81')  # 0x7fbc7e81
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ice_sword_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xff\x94H\x85')  # 0xff944885
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ice_sword_range_min))

        data.write(b'\x19\xf4\xe7d')  # 0x19f4e764
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ice_sword_range_max))

        data.write(b'\x05\x0c\xb8n')  # 0x50cb86e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x050cb86e))

        data.write(b'\xe3l\x17\x8f')  # 0xe36c178f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe36c178f))

        data.write(b'0c\xbb\xf1')  # 0x3063bbf1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info_0x3063bbf1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Y\x97\xeb\xe1')  # 0x5997ebe1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.morning_star_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc9"\xf0\xe0')  # 0xc922f0e0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rush_range_min))

        data.write(b'/B_\x01')  # 0x2f425f01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rush_range_max))

        data.write(b';\xe0\xa6k')  # 0x3be0a66b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3be0a66b))

        data.write(b'\xf5\x86\x83o')  # 0xf586836f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf586836f))

        data.write(b's\x12\xf1\xc1')  # 0x7312f1c1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7312f1c1))

        data.write(b'wSb\xcf')  # 0x775362cf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x775362cf))

        data.write(b'\xf1\xc7\x10a')  # 0xf1c71061
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf1c71061))

        data.write(b'?\x19lx')  # 0x3f196c78
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_freeze_distance))

        data.write(b'x\xdf\x0b}')  # 0x78df0b7d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.surfing_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xca\x04\xd7V')  # 0xca04d756
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_surf_attack_burst))

        data.write(b'\xd9A1\xfd')  # 0xd94131fd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_surf_attack_burst))

        data.write(b'\x82\x1b\x0c\x82')  # 0x821b0c82
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_surf_attack_burst_time))

        data.write(b'\xe4\xfej\xf6')  # 0xe4fe6af6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_surf_attack_burst_time))

        data.write(b'~\xf4\xef\xfe')  # 0x7ef4effe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_surf_attack_time))

        data.write(b'?\xe3\xd0x')  # 0x3fe3d078
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_surf_attack_time))

        data.write(b'\x1d\xcc~a')  # 0x1dcc7e61
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.surf_height_min))

        data.write(b'\xfb\xac\xd1\x80')  # 0xfbacd180
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.surf_height_max))

        data.write(b'\xe4\xcdy$')  # 0xe4cd7924
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.elevation_timer))

        data.write(b'0V\xff\xba')  # 0x3056ffba
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shard_storm_timer))

        data.write(b'Y^8\xd6')  # 0x595e38d6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ice_summon_timer))

        data.write(b'm\x0b\xa0A')  # 0x6d0ba041
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rush_timer))

        data.write(b'\xc7X\xf5.')  # 0xc758f52e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc758f52e))

        data.write(b'9\xd7&^')  # 0x39d7265e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.surf_timer))

        data.write(b'\xf8\x0f\xca\xe2')  # 0xf80fcae2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf80fcae2))

        data.write(b'S\x1a\x8c\x85')  # 0x531a8c85
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b'i\x17F\xf2')  # 0x691746f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x691746f2))

        data.write(b'\xcf\x19qH')  # 0xcf197148
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcf197148))

        data.write(b'\x9e\xe0\xca\x15')  # 0x9ee0ca15
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9ee0ca15))

        data.write(b'\xfcb\x9fr')  # 0xfc629f72
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfc629f72))

        data.write(b"\xef'y\xd9")  # 0xef2779d9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xef2779d9))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RundasDataJson", data)
        return cls(
            unknown_0x1aeb498d=json_data['unknown_0x1aeb498d'],
            unknown_0x9c7f3b23=json_data['unknown_0x9c7f3b23'],
            unknown_0x706186d2=json_data['unknown_0x706186d2'],
            unknown_0x3f5d6545=json_data['unknown_0x3f5d6545'],
            unknown_0x59a93220=json_data['unknown_0x59a93220'],
            unknown_0x6cc73ec1=json_data['unknown_0x6cc73ec1'],
            grapple_struggle_time=json_data['grapple_struggle_time'],
            hypermode_vulnerability=DamageVulnerability.from_json(json_data['hypermode_vulnerability']),
            armor_vulnerability=DamageVulnerability.from_json(json_data['armor_vulnerability']),
            damage_info_0x8d4a2668=DamageInfo.from_json(json_data['damage_info_0x8d4a2668']),
            ice_grenade_hp=json_data['ice_grenade_hp'],
            ice_grenade_damage=DamageInfo.from_json(json_data['ice_grenade_damage']),
            ice_sword_damage=DamageInfo.from_json(json_data['ice_sword_damage']),
            ice_sword_range_min=json_data['ice_sword_range_min'],
            ice_sword_range_max=json_data['ice_sword_range_max'],
            unknown_0x050cb86e=json_data['unknown_0x050cb86e'],
            unknown_0xe36c178f=json_data['unknown_0xe36c178f'],
            damage_info_0x3063bbf1=DamageInfo.from_json(json_data['damage_info_0x3063bbf1']),
            morning_star_damage=DamageInfo.from_json(json_data['morning_star_damage']),
            rush_range_min=json_data['rush_range_min'],
            rush_range_max=json_data['rush_range_max'],
            unknown_0x3be0a66b=json_data['unknown_0x3be0a66b'],
            unknown_0xf586836f=json_data['unknown_0xf586836f'],
            unknown_0x7312f1c1=json_data['unknown_0x7312f1c1'],
            unknown_0x775362cf=json_data['unknown_0x775362cf'],
            unknown_0xf1c71061=json_data['unknown_0xf1c71061'],
            missile_freeze_distance=json_data['missile_freeze_distance'],
            surfing_projectile_damage=DamageInfo.from_json(json_data['surfing_projectile_damage']),
            min_surf_attack_burst=json_data['min_surf_attack_burst'],
            max_surf_attack_burst=json_data['max_surf_attack_burst'],
            min_surf_attack_burst_time=json_data['min_surf_attack_burst_time'],
            max_surf_attack_burst_time=json_data['max_surf_attack_burst_time'],
            min_surf_attack_time=json_data['min_surf_attack_time'],
            max_surf_attack_time=json_data['max_surf_attack_time'],
            surf_height_min=json_data['surf_height_min'],
            surf_height_max=json_data['surf_height_max'],
            elevation_timer=json_data['elevation_timer'],
            shard_storm_timer=json_data['shard_storm_timer'],
            ice_summon_timer=json_data['ice_summon_timer'],
            rush_timer=json_data['rush_timer'],
            unknown_0xc758f52e=json_data['unknown_0xc758f52e'],
            surf_timer=json_data['surf_timer'],
            unknown_0xf80fcae2=json_data['unknown_0xf80fcae2'],
            is_gandrayda=json_data['is_gandrayda'],
            unknown_0x691746f2=json_data['unknown_0x691746f2'],
            unknown_0xcf197148=json_data['unknown_0xcf197148'],
            unknown_0x9ee0ca15=json_data['unknown_0x9ee0ca15'],
            unknown_0xfc629f72=json_data['unknown_0xfc629f72'],
            unknown_0xef2779d9=json_data['unknown_0xef2779d9'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0x1aeb498d': self.unknown_0x1aeb498d,
            'unknown_0x9c7f3b23': self.unknown_0x9c7f3b23,
            'unknown_0x706186d2': self.unknown_0x706186d2,
            'unknown_0x3f5d6545': self.unknown_0x3f5d6545,
            'unknown_0x59a93220': self.unknown_0x59a93220,
            'unknown_0x6cc73ec1': self.unknown_0x6cc73ec1,
            'grapple_struggle_time': self.grapple_struggle_time,
            'hypermode_vulnerability': self.hypermode_vulnerability.to_json(),
            'armor_vulnerability': self.armor_vulnerability.to_json(),
            'damage_info_0x8d4a2668': self.damage_info_0x8d4a2668.to_json(),
            'ice_grenade_hp': self.ice_grenade_hp,
            'ice_grenade_damage': self.ice_grenade_damage.to_json(),
            'ice_sword_damage': self.ice_sword_damage.to_json(),
            'ice_sword_range_min': self.ice_sword_range_min,
            'ice_sword_range_max': self.ice_sword_range_max,
            'unknown_0x050cb86e': self.unknown_0x050cb86e,
            'unknown_0xe36c178f': self.unknown_0xe36c178f,
            'damage_info_0x3063bbf1': self.damage_info_0x3063bbf1.to_json(),
            'morning_star_damage': self.morning_star_damage.to_json(),
            'rush_range_min': self.rush_range_min,
            'rush_range_max': self.rush_range_max,
            'unknown_0x3be0a66b': self.unknown_0x3be0a66b,
            'unknown_0xf586836f': self.unknown_0xf586836f,
            'unknown_0x7312f1c1': self.unknown_0x7312f1c1,
            'unknown_0x775362cf': self.unknown_0x775362cf,
            'unknown_0xf1c71061': self.unknown_0xf1c71061,
            'missile_freeze_distance': self.missile_freeze_distance,
            'surfing_projectile_damage': self.surfing_projectile_damage.to_json(),
            'min_surf_attack_burst': self.min_surf_attack_burst,
            'max_surf_attack_burst': self.max_surf_attack_burst,
            'min_surf_attack_burst_time': self.min_surf_attack_burst_time,
            'max_surf_attack_burst_time': self.max_surf_attack_burst_time,
            'min_surf_attack_time': self.min_surf_attack_time,
            'max_surf_attack_time': self.max_surf_attack_time,
            'surf_height_min': self.surf_height_min,
            'surf_height_max': self.surf_height_max,
            'elevation_timer': self.elevation_timer,
            'shard_storm_timer': self.shard_storm_timer,
            'ice_summon_timer': self.ice_summon_timer,
            'rush_timer': self.rush_timer,
            'unknown_0xc758f52e': self.unknown_0xc758f52e,
            'surf_timer': self.surf_timer,
            'unknown_0xf80fcae2': self.unknown_0xf80fcae2,
            'is_gandrayda': self.is_gandrayda,
            'unknown_0x691746f2': self.unknown_0x691746f2,
            'unknown_0xcf197148': self.unknown_0xcf197148,
            'unknown_0x9ee0ca15': self.unknown_0x9ee0ca15,
            'unknown_0xfc629f72': self.unknown_0xfc629f72,
            'unknown_0xef2779d9': self.unknown_0xef2779d9,
        }


def _decode_hypermode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_armor_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_damage_info_0x8d4a2668(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ice_grenade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ice_sword_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x3063bbf1(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_morning_star_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_surfing_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1aeb498d: ('unknown_0x1aeb498d', structs.decode_BIG_f),
    0x9c7f3b23: ('unknown_0x9c7f3b23', structs.decode_BIG_f),
    0x706186d2: ('unknown_0x706186d2', structs.decode_BIG_f),
    0x3f5d6545: ('unknown_0x3f5d6545', structs.decode_BIG_f),
    0x59a93220: ('unknown_0x59a93220', structs.decode_BIG_f),
    0x6cc73ec1: ('unknown_0x6cc73ec1', structs.decode_BIG_f),
    0x57f0a2a7: ('grapple_struggle_time', structs.decode_BIG_f),
    0xd1522831: ('hypermode_vulnerability', _decode_hypermode_vulnerability),
    0x896d5bd9: ('armor_vulnerability', _decode_armor_vulnerability),
    0x8d4a2668: ('damage_info_0x8d4a2668', _decode_damage_info_0x8d4a2668),
    0xf41394f6: ('ice_grenade_hp', structs.decode_BIG_f),
    0xb1b44917: ('ice_grenade_damage', _decode_ice_grenade_damage),
    0x7fbc7e81: ('ice_sword_damage', _decode_ice_sword_damage),
    0xff944885: ('ice_sword_range_min', structs.decode_BIG_f),
    0x19f4e764: ('ice_sword_range_max', structs.decode_BIG_f),
    0x050cb86e: ('unknown_0x050cb86e', structs.decode_BIG_f),
    0xe36c178f: ('unknown_0xe36c178f', structs.decode_BIG_f),
    0x3063bbf1: ('damage_info_0x3063bbf1', _decode_damage_info_0x3063bbf1),
    0x5997ebe1: ('morning_star_damage', _decode_morning_star_damage),
    0xc922f0e0: ('rush_range_min', structs.decode_BIG_f),
    0x2f425f01: ('rush_range_max', structs.decode_BIG_f),
    0x3be0a66b: ('unknown_0x3be0a66b', structs.decode_BIG_f),
    0xf586836f: ('unknown_0xf586836f', structs.decode_BIG_f),
    0x7312f1c1: ('unknown_0x7312f1c1', structs.decode_BIG_f),
    0x775362cf: ('unknown_0x775362cf', structs.decode_BIG_f),
    0xf1c71061: ('unknown_0xf1c71061', structs.decode_BIG_f),
    0x3f196c78: ('missile_freeze_distance', structs.decode_BIG_f),
    0x78df0b7d: ('surfing_projectile_damage', _decode_surfing_projectile_damage),
    0xca04d756: ('min_surf_attack_burst', structs.decode_BIG_l),
    0xd94131fd: ('max_surf_attack_burst', structs.decode_BIG_l),
    0x821b0c82: ('min_surf_attack_burst_time', structs.decode_BIG_f),
    0xe4fe6af6: ('max_surf_attack_burst_time', structs.decode_BIG_f),
    0x7ef4effe: ('min_surf_attack_time', structs.decode_BIG_f),
    0x3fe3d078: ('max_surf_attack_time', structs.decode_BIG_f),
    0x1dcc7e61: ('surf_height_min', structs.decode_BIG_f),
    0xfbacd180: ('surf_height_max', structs.decode_BIG_f),
    0xe4cd7924: ('elevation_timer', structs.decode_BIG_f),
    0x3056ffba: ('shard_storm_timer', structs.decode_BIG_f),
    0x595e38d6: ('ice_summon_timer', structs.decode_BIG_f),
    0x6d0ba041: ('rush_timer', structs.decode_BIG_f),
    0xc758f52e: ('unknown_0xc758f52e', structs.decode_BIG_f),
    0x39d7265e: ('surf_timer', structs.decode_BIG_f),
    0xf80fcae2: ('unknown_0xf80fcae2', structs.decode_BIG_f),
    0x531a8c85: ('is_gandrayda', structs.decode_BIG_bool_),
    0x691746f2: ('unknown_0x691746f2', structs.decode_BIG_f),
    0xcf197148: ('unknown_0xcf197148', structs.decode_BIG_f),
    0x9ee0ca15: ('unknown_0x9ee0ca15', structs.decode_BIG_f),
    0xfc629f72: ('unknown_0xfc629f72', structs.decode_BIG_f),
    0xef2779d9: ('unknown_0xef2779d9', structs.decode_BIG_f),
}
