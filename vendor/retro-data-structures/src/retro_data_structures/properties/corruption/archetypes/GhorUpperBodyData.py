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
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.GhorAttackData import GhorAttackData
from retro_data_structures.properties.corruption.archetypes.GhorMaskData import GhorMaskData
from retro_data_structures.properties.corruption.archetypes.GhorShieldData import GhorShieldData
from retro_data_structures.properties.corruption.archetypes.GhorShieldGeneratorData import GhorShieldGeneratorData
from retro_data_structures.properties.corruption.archetypes.GhorUpperArmorData import GhorUpperArmorData
from retro_data_structures.properties.corruption.archetypes.GhorWeakSpotData import GhorWeakSpotData
from retro_data_structures.properties.corruption.archetypes.GhorWeaponData import GhorWeaponData
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GhorUpperBodyDataJson(typing_extensions.TypedDict):
        is_gandrayda: bool
        shield_data: json_util.JsonObject
        shield_generator_data: json_util.JsonObject
        armor_data: json_util.JsonObject
        face_target: json_util.JsonObject
        face_effect: str
        torso_target: json_util.JsonObject
        torso_shield: json_util.JsonObject
        torso_hypermode_vulnerability: json_util.JsonObject
        mask: json_util.JsonObject
        ball_target: json_util.JsonObject
        attack_data: json_util.JsonObject
        weapon_data: json_util.JsonObject
        hypermode_weapon_data: json_util.JsonObject
        rotate_body_sound: int
        lock_on_locator: str
        energy_bar_string: str
        stage1_health: json_util.JsonObject
        stage2_health: json_util.JsonObject
        stage3_health: json_util.JsonObject
        unknown_0xd16b54f9: float
        unknown_0xb40c6fbf: float
        armor_mod_inca_color_normal: json_util.JsonValue
        armor_mod_inca_color_hypermode: json_util.JsonValue
    

@dataclasses.dataclass()
class GhorUpperBodyData(BaseProperty):
    is_gandrayda: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x531a8c85, original_name='IsGandrayda'
        ),
    })
    shield_data: GhorShieldData = dataclasses.field(default_factory=GhorShieldData, metadata={
        'reflection': FieldReflection[GhorShieldData](
            GhorShieldData, id=0x832c442e, original_name='ShieldData', from_json=GhorShieldData.from_json, to_json=GhorShieldData.to_json
        ),
    })
    shield_generator_data: GhorShieldGeneratorData = dataclasses.field(default_factory=GhorShieldGeneratorData, metadata={
        'reflection': FieldReflection[GhorShieldGeneratorData](
            GhorShieldGeneratorData, id=0xa0d0963b, original_name='ShieldGeneratorData', from_json=GhorShieldGeneratorData.from_json, to_json=GhorShieldGeneratorData.to_json
        ),
    })
    armor_data: GhorUpperArmorData = dataclasses.field(default_factory=GhorUpperArmorData, metadata={
        'reflection': FieldReflection[GhorUpperArmorData](
            GhorUpperArmorData, id=0x81cc0d22, original_name='ArmorData', from_json=GhorUpperArmorData.from_json, to_json=GhorUpperArmorData.to_json
        ),
    })
    face_target: GhorWeakSpotData = dataclasses.field(default_factory=GhorWeakSpotData, metadata={
        'reflection': FieldReflection[GhorWeakSpotData](
            GhorWeakSpotData, id=0xd345f07f, original_name='FaceTarget', from_json=GhorWeakSpotData.from_json, to_json=GhorWeakSpotData.to_json
        ),
    })
    face_effect: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xc59d1a2d, original_name='FaceEffect'
        ),
    })
    torso_target: GhorWeakSpotData = dataclasses.field(default_factory=GhorWeakSpotData, metadata={
        'reflection': FieldReflection[GhorWeakSpotData](
            GhorWeakSpotData, id=0x391a32ae, original_name='TorsoTarget', from_json=GhorWeakSpotData.from_json, to_json=GhorWeakSpotData.to_json
        ),
    })
    torso_shield: GhorWeakSpotData = dataclasses.field(default_factory=GhorWeakSpotData, metadata={
        'reflection': FieldReflection[GhorWeakSpotData](
            GhorWeakSpotData, id=0xafb9313a, original_name='TorsoShield', from_json=GhorWeakSpotData.from_json, to_json=GhorWeakSpotData.to_json
        ),
    })
    torso_hypermode_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xba4ad147, original_name='TorsoHypermodeVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    mask: GhorMaskData = dataclasses.field(default_factory=GhorMaskData, metadata={
        'reflection': FieldReflection[GhorMaskData](
            GhorMaskData, id=0x305cdad2, original_name='Mask', from_json=GhorMaskData.from_json, to_json=GhorMaskData.to_json
        ),
    })
    ball_target: GhorWeakSpotData = dataclasses.field(default_factory=GhorWeakSpotData, metadata={
        'reflection': FieldReflection[GhorWeakSpotData](
            GhorWeakSpotData, id=0x810ec49a, original_name='BallTarget', from_json=GhorWeakSpotData.from_json, to_json=GhorWeakSpotData.to_json
        ),
    })
    attack_data: GhorAttackData = dataclasses.field(default_factory=GhorAttackData, metadata={
        'reflection': FieldReflection[GhorAttackData](
            GhorAttackData, id=0x5b772f6d, original_name='AttackData', from_json=GhorAttackData.from_json, to_json=GhorAttackData.to_json
        ),
    })
    weapon_data: GhorWeaponData = dataclasses.field(default_factory=GhorWeaponData, metadata={
        'reflection': FieldReflection[GhorWeaponData](
            GhorWeaponData, id=0x0e07b299, original_name='WeaponData', from_json=GhorWeaponData.from_json, to_json=GhorWeaponData.to_json
        ),
    })
    hypermode_weapon_data: GhorWeaponData = dataclasses.field(default_factory=GhorWeaponData, metadata={
        'reflection': FieldReflection[GhorWeaponData](
            GhorWeaponData, id=0x73e98b8f, original_name='HypermodeWeaponData', from_json=GhorWeaponData.from_json, to_json=GhorWeaponData.to_json
        ),
    })
    rotate_body_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x15e3f283, original_name='RotateBodySound'
        ),
    })
    lock_on_locator: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x79bfd886, original_name='LockOnLocator'
        ),
    })
    energy_bar_string: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x337c4056, original_name='EnergyBarString'
        ),
    })
    stage1_health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0x3d43820c, original_name='Stage1Health', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    stage2_health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0x6ed9d988, original_name='Stage2Health', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    stage3_health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0xe97f12cb, original_name='Stage3Health', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    unknown_0xd16b54f9: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd16b54f9, original_name='Unknown'
        ),
    })
    unknown_0xb40c6fbf: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb40c6fbf, original_name='Unknown'
        ),
    })
    armor_mod_inca_color_normal: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x2443e8ec, original_name='ArmorModIncaColorNormal', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    armor_mod_inca_color_hypermode: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x888049bd, original_name='ArmorModIncaColorHypermode', from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 24:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531a8c85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x832c442e
        shield_data = GhorShieldData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0d0963b
        shield_generator_data = GhorShieldGeneratorData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81cc0d22
        armor_data = GhorUpperArmorData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd345f07f
        face_target = GhorWeakSpotData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc59d1a2d
        face_effect = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x391a32ae
        torso_target = GhorWeakSpotData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xafb9313a
        torso_shield = GhorWeakSpotData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba4ad147
        torso_hypermode_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x305cdad2
        mask = GhorMaskData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x810ec49a
        ball_target = GhorWeakSpotData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b772f6d
        attack_data = GhorAttackData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0e07b299
        weapon_data = GhorWeaponData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73e98b8f
        hypermode_weapon_data = GhorWeaponData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15e3f283
        rotate_body_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79bfd886
        lock_on_locator = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337c4056
        energy_bar_string = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d43820c
        stage1_health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ed9d988
        stage2_health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe97f12cb
        stage3_health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd16b54f9
        unknown_0xd16b54f9 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb40c6fbf
        unknown_0xb40c6fbf = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2443e8ec
        armor_mod_inca_color_normal = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x888049bd
        armor_mod_inca_color_hypermode = Color.from_stream(data, game, property_size)
    
        return cls(is_gandrayda, shield_data, shield_generator_data, armor_data, face_target, face_effect, torso_target, torso_shield, torso_hypermode_vulnerability, mask, ball_target, attack_data, weapon_data, hypermode_weapon_data, rotate_body_sound, lock_on_locator, energy_bar_string, stage1_health, stage2_health, stage3_health, unknown_0xd16b54f9, unknown_0xb40c6fbf, armor_mod_inca_color_normal, armor_mod_inca_color_hypermode)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x18')  # 24 properties

        data.write(b'S\x1a\x8c\x85')  # 0x531a8c85
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b'\x83,D.')  # 0x832c442e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shield_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa0\xd0\x96;')  # 0xa0d0963b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shield_generator_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x81\xcc\r"')  # 0x81cc0d22
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.armor_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd3E\xf0\x7f')  # 0xd345f07f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.face_target.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc5\x9d\x1a-')  # 0xc59d1a2d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.face_effect.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'9\x1a2\xae')  # 0x391a32ae
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.torso_target.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xaf\xb91:')  # 0xafb9313a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.torso_shield.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbaJ\xd1G')  # 0xba4ad147
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.torso_hypermode_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'0\\\xda\xd2')  # 0x305cdad2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mask.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x81\x0e\xc4\x9a')  # 0x810ec49a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_target.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'[w/m')  # 0x5b772f6d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attack_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0e\x07\xb2\x99')  # 0xe07b299
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weapon_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b's\xe9\x8b\x8f')  # 0x73e98b8f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_weapon_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15\xe3\xf2\x83')  # 0x15e3f283
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.rotate_body_sound))

        data.write(b'y\xbf\xd8\x86')  # 0x79bfd886
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.lock_on_locator.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3|@V')  # 0x337c4056
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.energy_bar_string.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'=C\x82\x0c')  # 0x3d43820c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage1_health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'n\xd9\xd9\x88')  # 0x6ed9d988
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage2_health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe9\x7f\x12\xcb')  # 0xe97f12cb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage3_health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd1kT\xf9')  # 0xd16b54f9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd16b54f9))

        data.write(b'\xb4\x0co\xbf')  # 0xb40c6fbf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb40c6fbf))

        data.write(b'$C\xe8\xec')  # 0x2443e8ec
        data.write(b'\x00\x10')  # size
        self.armor_mod_inca_color_normal.to_stream(data, game)

        data.write(b'\x88\x80I\xbd')  # 0x888049bd
        data.write(b'\x00\x10')  # size
        self.armor_mod_inca_color_hypermode.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorUpperBodyDataJson", data)
        return cls(
            is_gandrayda=json_data['is_gandrayda'],
            shield_data=GhorShieldData.from_json(json_data['shield_data']),
            shield_generator_data=GhorShieldGeneratorData.from_json(json_data['shield_generator_data']),
            armor_data=GhorUpperArmorData.from_json(json_data['armor_data']),
            face_target=GhorWeakSpotData.from_json(json_data['face_target']),
            face_effect=json_data['face_effect'],
            torso_target=GhorWeakSpotData.from_json(json_data['torso_target']),
            torso_shield=GhorWeakSpotData.from_json(json_data['torso_shield']),
            torso_hypermode_vulnerability=DamageVulnerability.from_json(json_data['torso_hypermode_vulnerability']),
            mask=GhorMaskData.from_json(json_data['mask']),
            ball_target=GhorWeakSpotData.from_json(json_data['ball_target']),
            attack_data=GhorAttackData.from_json(json_data['attack_data']),
            weapon_data=GhorWeaponData.from_json(json_data['weapon_data']),
            hypermode_weapon_data=GhorWeaponData.from_json(json_data['hypermode_weapon_data']),
            rotate_body_sound=json_data['rotate_body_sound'],
            lock_on_locator=json_data['lock_on_locator'],
            energy_bar_string=json_data['energy_bar_string'],
            stage1_health=HealthInfo.from_json(json_data['stage1_health']),
            stage2_health=HealthInfo.from_json(json_data['stage2_health']),
            stage3_health=HealthInfo.from_json(json_data['stage3_health']),
            unknown_0xd16b54f9=json_data['unknown_0xd16b54f9'],
            unknown_0xb40c6fbf=json_data['unknown_0xb40c6fbf'],
            armor_mod_inca_color_normal=Color.from_json(json_data['armor_mod_inca_color_normal']),
            armor_mod_inca_color_hypermode=Color.from_json(json_data['armor_mod_inca_color_hypermode']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'is_gandrayda': self.is_gandrayda,
            'shield_data': self.shield_data.to_json(),
            'shield_generator_data': self.shield_generator_data.to_json(),
            'armor_data': self.armor_data.to_json(),
            'face_target': self.face_target.to_json(),
            'face_effect': self.face_effect,
            'torso_target': self.torso_target.to_json(),
            'torso_shield': self.torso_shield.to_json(),
            'torso_hypermode_vulnerability': self.torso_hypermode_vulnerability.to_json(),
            'mask': self.mask.to_json(),
            'ball_target': self.ball_target.to_json(),
            'attack_data': self.attack_data.to_json(),
            'weapon_data': self.weapon_data.to_json(),
            'hypermode_weapon_data': self.hypermode_weapon_data.to_json(),
            'rotate_body_sound': self.rotate_body_sound,
            'lock_on_locator': self.lock_on_locator,
            'energy_bar_string': self.energy_bar_string,
            'stage1_health': self.stage1_health.to_json(),
            'stage2_health': self.stage2_health.to_json(),
            'stage3_health': self.stage3_health.to_json(),
            'unknown_0xd16b54f9': self.unknown_0xd16b54f9,
            'unknown_0xb40c6fbf': self.unknown_0xb40c6fbf,
            'armor_mod_inca_color_normal': self.armor_mod_inca_color_normal.to_json(),
            'armor_mod_inca_color_hypermode': self.armor_mod_inca_color_hypermode.to_json(),
        }

    def _dependencies_for_rotate_body_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rotate_body_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.shield_data.dependencies_for, "shield_data", "GhorShieldData"),
            (self.shield_generator_data.dependencies_for, "shield_generator_data", "GhorShieldGeneratorData"),
            (self.armor_data.dependencies_for, "armor_data", "GhorUpperArmorData"),
            (self.face_target.dependencies_for, "face_target", "GhorWeakSpotData"),
            (self.torso_target.dependencies_for, "torso_target", "GhorWeakSpotData"),
            (self.torso_shield.dependencies_for, "torso_shield", "GhorWeakSpotData"),
            (self.mask.dependencies_for, "mask", "GhorMaskData"),
            (self.ball_target.dependencies_for, "ball_target", "GhorWeakSpotData"),
            (self.attack_data.dependencies_for, "attack_data", "GhorAttackData"),
            (self.weapon_data.dependencies_for, "weapon_data", "GhorWeaponData"),
            (self.hypermode_weapon_data.dependencies_for, "hypermode_weapon_data", "GhorWeaponData"),
            (self._dependencies_for_rotate_body_sound, "rotate_body_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GhorUpperBodyData.{field_name} ({field_type}): {e}"
                )


def _decode_shield_data(data: typing.BinaryIO, game: Game, property_size: int) -> GhorShieldData:
    return GhorShieldData.from_stream(data, game, property_size)


def _decode_shield_generator_data(data: typing.BinaryIO, game: Game, property_size: int) -> GhorShieldGeneratorData:
    return GhorShieldGeneratorData.from_stream(data, game, property_size)


def _decode_armor_data(data: typing.BinaryIO, game: Game, property_size: int) -> GhorUpperArmorData:
    return GhorUpperArmorData.from_stream(data, game, property_size)


def _decode_face_target(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeakSpotData:
    return GhorWeakSpotData.from_stream(data, game, property_size)


def _decode_face_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_torso_target(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeakSpotData:
    return GhorWeakSpotData.from_stream(data, game, property_size)


def _decode_torso_shield(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeakSpotData:
    return GhorWeakSpotData.from_stream(data, game, property_size)


def _decode_torso_hypermode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_mask(data: typing.BinaryIO, game: Game, property_size: int) -> GhorMaskData:
    return GhorMaskData.from_stream(data, game, property_size)


def _decode_ball_target(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeakSpotData:
    return GhorWeakSpotData.from_stream(data, game, property_size)


def _decode_attack_data(data: typing.BinaryIO, game: Game, property_size: int) -> GhorAttackData:
    return GhorAttackData.from_stream(data, game, property_size)


def _decode_weapon_data(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeaponData:
    return GhorWeaponData.from_stream(data, game, property_size)


def _decode_hypermode_weapon_data(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeaponData:
    return GhorWeaponData.from_stream(data, game, property_size)


def _decode_lock_on_locator(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_energy_bar_string(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_stage1_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_stage2_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_stage3_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_armor_mod_inca_color_normal(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_armor_mod_inca_color_hypermode(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x531a8c85: ('is_gandrayda', structs.decode_BIG_bool_),
    0x832c442e: ('shield_data', _decode_shield_data),
    0xa0d0963b: ('shield_generator_data', _decode_shield_generator_data),
    0x81cc0d22: ('armor_data', _decode_armor_data),
    0xd345f07f: ('face_target', _decode_face_target),
    0xc59d1a2d: ('face_effect', _decode_face_effect),
    0x391a32ae: ('torso_target', _decode_torso_target),
    0xafb9313a: ('torso_shield', _decode_torso_shield),
    0xba4ad147: ('torso_hypermode_vulnerability', _decode_torso_hypermode_vulnerability),
    0x305cdad2: ('mask', _decode_mask),
    0x810ec49a: ('ball_target', _decode_ball_target),
    0x5b772f6d: ('attack_data', _decode_attack_data),
    0x0e07b299: ('weapon_data', _decode_weapon_data),
    0x73e98b8f: ('hypermode_weapon_data', _decode_hypermode_weapon_data),
    0x15e3f283: ('rotate_body_sound', structs.decode_BIG_Q),
    0x79bfd886: ('lock_on_locator', _decode_lock_on_locator),
    0x337c4056: ('energy_bar_string', _decode_energy_bar_string),
    0x3d43820c: ('stage1_health', _decode_stage1_health),
    0x6ed9d988: ('stage2_health', _decode_stage2_health),
    0xe97f12cb: ('stage3_health', _decode_stage3_health),
    0xd16b54f9: ('unknown_0xd16b54f9', structs.decode_BIG_f),
    0xb40c6fbf: ('unknown_0xb40c6fbf', structs.decode_BIG_f),
    0x2443e8ec: ('armor_mod_inca_color_normal', _decode_armor_mod_inca_color_normal),
    0x888049bd: ('armor_mod_inca_color_hypermode', _decode_armor_mod_inca_color_hypermode),
}
