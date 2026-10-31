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

if typing.TYPE_CHECKING:
    class Ridley1DataJson(typing_extensions.TypedDict):
        unknown_0xa0460b5e: float
        unknown_0xf33b0dd4: float
        unknown_0xa59260dd: float
        unknown_0x5bbdbc45: float
        unknown_0xbc1564b9: float
        damage_info_0xe82166db: json_util.JsonObject
        below_beam_damage: json_util.JsonObject
        below_bite_damage_threshold: float
        below_bite_damage: json_util.JsonObject
        damage_info_0x54031e21: json_util.JsonObject
        in_hand_bite_damage_threshold: float
        in_hand_bite_damage: json_util.JsonObject
        in_hand_fire_breath_damage_threshold: float
        in_hand_fire_breath_damage: json_util.JsonObject
        in_hand_slap_damage_threshold: float
        in_hand_slap_damage: json_util.JsonObject
        unknown_0xa4cb7b3c: float
        damage_info_0x742287f5: json_util.JsonObject
        unknown_0xbe3b8e93: float
        damage_info_0x78f4a916: json_util.JsonObject
        damage_info_0x76f0f23b: json_util.JsonObject
        above_dive_thrust_damage: json_util.JsonObject
        above_missile_damage: json_util.JsonObject
        above_fireball_damage: json_util.JsonObject
        above_fireball_health: float
    

@dataclasses.dataclass()
class Ridley1Data(BaseProperty):
    unknown_0xa0460b5e: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa0460b5e, original_name='Unknown'
        ),
    })
    unknown_0xf33b0dd4: float = dataclasses.field(default=65.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf33b0dd4, original_name='Unknown'
        ),
    })
    unknown_0xa59260dd: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa59260dd, original_name='Unknown'
        ),
    })
    unknown_0x5bbdbc45: float = dataclasses.field(default=35.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5bbdbc45, original_name='Unknown'
        ),
    })
    unknown_0xbc1564b9: float = dataclasses.field(default=1000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbc1564b9, original_name='Unknown'
        ),
    })
    damage_info_0xe82166db: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xe82166db, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    below_beam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x36307b98, original_name='BelowBeamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    below_bite_damage_threshold: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf616d87b, original_name='BelowBiteDamageThreshold'
        ),
    })
    below_bite_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xfab0199e, original_name='BelowBiteDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    damage_info_0x54031e21: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x54031e21, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    in_hand_bite_damage_threshold: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb5194095, original_name='InHandBiteDamageThreshold'
        ),
    })
    in_hand_bite_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xd55917a9, original_name='InHandBiteDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    in_hand_fire_breath_damage_threshold: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xddd0212a, original_name='InHandFireBreathDamageThreshold'
        ),
    })
    in_hand_fire_breath_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x6bb8e35c, original_name='InHandFireBreathDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    in_hand_slap_damage_threshold: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf4c13980, original_name='InHandSlapDamageThreshold'
        ),
    })
    in_hand_slap_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x47d4427e, original_name='InHandSlapDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown_0xa4cb7b3c: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa4cb7b3c, original_name='Unknown'
        ),
    })
    damage_info_0x742287f5: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x742287f5, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown_0xbe3b8e93: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbe3b8e93, original_name='Unknown'
        ),
    })
    damage_info_0x78f4a916: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x78f4a916, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    damage_info_0x76f0f23b: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x76f0f23b, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    above_dive_thrust_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x77edd892, original_name='AboveDiveThrustDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    above_missile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xb6c739d2, original_name='AboveMissileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    above_fireball_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x79350ac0, original_name='AboveFireballDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    above_fireball_health: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4fa2bce1, original_name='AboveFireballHealth'
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
        assert property_id == 0xa0460b5e
        unknown_0xa0460b5e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf33b0dd4
        unknown_0xf33b0dd4 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa59260dd
        unknown_0xa59260dd = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5bbdbc45
        unknown_0x5bbdbc45 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc1564b9
        unknown_0xbc1564b9 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe82166db
        damage_info_0xe82166db = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36307b98
        below_beam_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf616d87b
        below_bite_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfab0199e
        below_bite_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54031e21
        damage_info_0x54031e21 = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5194095
        in_hand_bite_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd55917a9
        in_hand_bite_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xddd0212a
        in_hand_fire_breath_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bb8e35c
        in_hand_fire_breath_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4c13980
        in_hand_slap_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47d4427e
        in_hand_slap_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4cb7b3c
        unknown_0xa4cb7b3c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x742287f5
        damage_info_0x742287f5 = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe3b8e93
        unknown_0xbe3b8e93 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78f4a916
        damage_info_0x78f4a916 = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76f0f23b
        damage_info_0x76f0f23b = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77edd892
        above_dive_thrust_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6c739d2
        above_missile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79350ac0
        above_fireball_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4fa2bce1
        above_fireball_health = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(unknown_0xa0460b5e, unknown_0xf33b0dd4, unknown_0xa59260dd, unknown_0x5bbdbc45, unknown_0xbc1564b9, damage_info_0xe82166db, below_beam_damage, below_bite_damage_threshold, below_bite_damage, damage_info_0x54031e21, in_hand_bite_damage_threshold, in_hand_bite_damage, in_hand_fire_breath_damage_threshold, in_hand_fire_breath_damage, in_hand_slap_damage_threshold, in_hand_slap_damage, unknown_0xa4cb7b3c, damage_info_0x742287f5, unknown_0xbe3b8e93, damage_info_0x78f4a916, damage_info_0x76f0f23b, above_dive_thrust_damage, above_missile_damage, above_fireball_damage, above_fireball_health)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x19')  # 25 properties

        data.write(b'\xa0F\x0b^')  # 0xa0460b5e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa0460b5e))

        data.write(b'\xf3;\r\xd4')  # 0xf33b0dd4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf33b0dd4))

        data.write(b'\xa5\x92`\xdd')  # 0xa59260dd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa59260dd))

        data.write(b'[\xbd\xbcE')  # 0x5bbdbc45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5bbdbc45))

        data.write(b'\xbc\x15d\xb9')  # 0xbc1564b9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbc1564b9))

        data.write(b'\xe8!f\xdb')  # 0xe82166db
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info_0xe82166db.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'60{\x98')  # 0x36307b98
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.below_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf6\x16\xd8{')  # 0xf616d87b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.below_bite_damage_threshold))

        data.write(b'\xfa\xb0\x19\x9e')  # 0xfab0199e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.below_bite_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'T\x03\x1e!')  # 0x54031e21
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info_0x54031e21.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb5\x19@\x95')  # 0xb5194095
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.in_hand_bite_damage_threshold))

        data.write(b'\xd5Y\x17\xa9')  # 0xd55917a9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.in_hand_bite_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdd\xd0!*')  # 0xddd0212a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.in_hand_fire_breath_damage_threshold))

        data.write(b'k\xb8\xe3\\')  # 0x6bb8e35c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.in_hand_fire_breath_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf4\xc19\x80')  # 0xf4c13980
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.in_hand_slap_damage_threshold))

        data.write(b'G\xd4B~')  # 0x47d4427e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.in_hand_slap_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa4\xcb{<')  # 0xa4cb7b3c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa4cb7b3c))

        data.write(b't"\x87\xf5')  # 0x742287f5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info_0x742287f5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbe;\x8e\x93')  # 0xbe3b8e93
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbe3b8e93))

        data.write(b'x\xf4\xa9\x16')  # 0x78f4a916
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info_0x78f4a916.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'v\xf0\xf2;')  # 0x76f0f23b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info_0x76f0f23b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'w\xed\xd8\x92')  # 0x77edd892
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.above_dive_thrust_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb6\xc79\xd2')  # 0xb6c739d2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.above_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'y5\n\xc0')  # 0x79350ac0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.above_fireball_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'O\xa2\xbc\xe1')  # 0x4fa2bce1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.above_fireball_health))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("Ridley1DataJson", data)
        return cls(
            unknown_0xa0460b5e=json_data['unknown_0xa0460b5e'],
            unknown_0xf33b0dd4=json_data['unknown_0xf33b0dd4'],
            unknown_0xa59260dd=json_data['unknown_0xa59260dd'],
            unknown_0x5bbdbc45=json_data['unknown_0x5bbdbc45'],
            unknown_0xbc1564b9=json_data['unknown_0xbc1564b9'],
            damage_info_0xe82166db=DamageInfo.from_json(json_data['damage_info_0xe82166db']),
            below_beam_damage=DamageInfo.from_json(json_data['below_beam_damage']),
            below_bite_damage_threshold=json_data['below_bite_damage_threshold'],
            below_bite_damage=DamageInfo.from_json(json_data['below_bite_damage']),
            damage_info_0x54031e21=DamageInfo.from_json(json_data['damage_info_0x54031e21']),
            in_hand_bite_damage_threshold=json_data['in_hand_bite_damage_threshold'],
            in_hand_bite_damage=DamageInfo.from_json(json_data['in_hand_bite_damage']),
            in_hand_fire_breath_damage_threshold=json_data['in_hand_fire_breath_damage_threshold'],
            in_hand_fire_breath_damage=DamageInfo.from_json(json_data['in_hand_fire_breath_damage']),
            in_hand_slap_damage_threshold=json_data['in_hand_slap_damage_threshold'],
            in_hand_slap_damage=DamageInfo.from_json(json_data['in_hand_slap_damage']),
            unknown_0xa4cb7b3c=json_data['unknown_0xa4cb7b3c'],
            damage_info_0x742287f5=DamageInfo.from_json(json_data['damage_info_0x742287f5']),
            unknown_0xbe3b8e93=json_data['unknown_0xbe3b8e93'],
            damage_info_0x78f4a916=DamageInfo.from_json(json_data['damage_info_0x78f4a916']),
            damage_info_0x76f0f23b=DamageInfo.from_json(json_data['damage_info_0x76f0f23b']),
            above_dive_thrust_damage=DamageInfo.from_json(json_data['above_dive_thrust_damage']),
            above_missile_damage=DamageInfo.from_json(json_data['above_missile_damage']),
            above_fireball_damage=DamageInfo.from_json(json_data['above_fireball_damage']),
            above_fireball_health=json_data['above_fireball_health'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0xa0460b5e': self.unknown_0xa0460b5e,
            'unknown_0xf33b0dd4': self.unknown_0xf33b0dd4,
            'unknown_0xa59260dd': self.unknown_0xa59260dd,
            'unknown_0x5bbdbc45': self.unknown_0x5bbdbc45,
            'unknown_0xbc1564b9': self.unknown_0xbc1564b9,
            'damage_info_0xe82166db': self.damage_info_0xe82166db.to_json(),
            'below_beam_damage': self.below_beam_damage.to_json(),
            'below_bite_damage_threshold': self.below_bite_damage_threshold,
            'below_bite_damage': self.below_bite_damage.to_json(),
            'damage_info_0x54031e21': self.damage_info_0x54031e21.to_json(),
            'in_hand_bite_damage_threshold': self.in_hand_bite_damage_threshold,
            'in_hand_bite_damage': self.in_hand_bite_damage.to_json(),
            'in_hand_fire_breath_damage_threshold': self.in_hand_fire_breath_damage_threshold,
            'in_hand_fire_breath_damage': self.in_hand_fire_breath_damage.to_json(),
            'in_hand_slap_damage_threshold': self.in_hand_slap_damage_threshold,
            'in_hand_slap_damage': self.in_hand_slap_damage.to_json(),
            'unknown_0xa4cb7b3c': self.unknown_0xa4cb7b3c,
            'damage_info_0x742287f5': self.damage_info_0x742287f5.to_json(),
            'unknown_0xbe3b8e93': self.unknown_0xbe3b8e93,
            'damage_info_0x78f4a916': self.damage_info_0x78f4a916.to_json(),
            'damage_info_0x76f0f23b': self.damage_info_0x76f0f23b.to_json(),
            'above_dive_thrust_damage': self.above_dive_thrust_damage.to_json(),
            'above_missile_damage': self.above_missile_damage.to_json(),
            'above_fireball_damage': self.above_fireball_damage.to_json(),
            'above_fireball_health': self.above_fireball_health,
        }


def _decode_damage_info_0xe82166db(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_below_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_below_bite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x54031e21(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_in_hand_bite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_in_hand_fire_breath_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_in_hand_slap_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x742287f5(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x78f4a916(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x76f0f23b(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_above_dive_thrust_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_above_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_above_fireball_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa0460b5e: ('unknown_0xa0460b5e', structs.decode_BIG_f),
    0xf33b0dd4: ('unknown_0xf33b0dd4', structs.decode_BIG_f),
    0xa59260dd: ('unknown_0xa59260dd', structs.decode_BIG_f),
    0x5bbdbc45: ('unknown_0x5bbdbc45', structs.decode_BIG_f),
    0xbc1564b9: ('unknown_0xbc1564b9', structs.decode_BIG_f),
    0xe82166db: ('damage_info_0xe82166db', _decode_damage_info_0xe82166db),
    0x36307b98: ('below_beam_damage', _decode_below_beam_damage),
    0xf616d87b: ('below_bite_damage_threshold', structs.decode_BIG_f),
    0xfab0199e: ('below_bite_damage', _decode_below_bite_damage),
    0x54031e21: ('damage_info_0x54031e21', _decode_damage_info_0x54031e21),
    0xb5194095: ('in_hand_bite_damage_threshold', structs.decode_BIG_f),
    0xd55917a9: ('in_hand_bite_damage', _decode_in_hand_bite_damage),
    0xddd0212a: ('in_hand_fire_breath_damage_threshold', structs.decode_BIG_f),
    0x6bb8e35c: ('in_hand_fire_breath_damage', _decode_in_hand_fire_breath_damage),
    0xf4c13980: ('in_hand_slap_damage_threshold', structs.decode_BIG_f),
    0x47d4427e: ('in_hand_slap_damage', _decode_in_hand_slap_damage),
    0xa4cb7b3c: ('unknown_0xa4cb7b3c', structs.decode_BIG_f),
    0x742287f5: ('damage_info_0x742287f5', _decode_damage_info_0x742287f5),
    0xbe3b8e93: ('unknown_0xbe3b8e93', structs.decode_BIG_f),
    0x78f4a916: ('damage_info_0x78f4a916', _decode_damage_info_0x78f4a916),
    0x76f0f23b: ('damage_info_0x76f0f23b', _decode_damage_info_0x76f0f23b),
    0x77edd892: ('above_dive_thrust_damage', _decode_above_dive_thrust_damage),
    0xb6c739d2: ('above_missile_damage', _decode_above_missile_damage),
    0x79350ac0: ('above_fireball_damage', _decode_above_fireball_damage),
    0x4fa2bce1: ('above_fireball_health', structs.decode_BIG_f),
}
