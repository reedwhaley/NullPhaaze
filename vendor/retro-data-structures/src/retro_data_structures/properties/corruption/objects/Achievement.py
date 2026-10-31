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
from retro_data_structures.properties.corruption.archetypes.BonusCredit import BonusCredit
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AchievementJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        bonus_credit: json_util.JsonObject
        achievement: int
        normal_difficulty: bool
        hard_difficulty: bool
        elite_difficulty: bool
        bonus_credit_string: int
    

class AchievementEnum(enum.IntEnum):
    kBA_TinCan10 = 1290095210
    kBA_TinCan20 = 1741167017
    kBA_BossBerserker_GFShip = 1941731395
    kBA_BossBerserkerHard_GFShip = 1847676886
    SaveTrooper1 = 42311112
    SaveTrooper2 = 2302821108
    SaveTrooper3 = 3685060452
    SaveTrooper4 = 2575337497
    kBA_EscapeRidley = 977778753
    kBA_BossHatcher_GFPlanet = 1741569191
    kBA_BossHatcherHard_GFPlanet = 3796894174
    kBA_BossRidley_GFPlanet = 2288784460
    kBA_BossRidleyHard_GFPlanet = 2046095677
    kBA_BossRundas = 3347275427
    kBA_BossRundasHard = 1815168570
    kBA_BossKorakk = 1015929027
    kBA_BossKorakkHard = 105107473
    kBA_BossMogenar = 80518716
    kBA_BossMogenarHard = 1831985480
    kBA_RedPhazzoid_Bryyo1 = 1831093832
    kBA_RedPhazzoid_Bryyo2 = 4096595954
    kBA_RedPhazzoid_Bryyo3 = 2200577892
    kBA_BombGeneratorFire = 1437187765
    kBA_BombGeneratorPirate = 291959200
    kBA_DiscoverBryyoIce = 3841084878
    kBA_GauntletShortcut = 3936228971
    kBA_ReptilicusSuicide = 246361685
    kBA_BryyoSwitches = 761891303
    kBA_BossHatcher_Valhalla = 3831947482
    kBA_BossHatcherHard_Valhalla = 1643699619
    kBA_SecretAUDialogue = 1845492504
    kBA_BossGhor = 3065393673
    kBA_BossGhorHard = 2316897795
    kBA_BossSteamlord = 3682273482
    kBA_BossSteamlordHard = 2320145227
    kBA_BossMechanoid = 2373462654
    kBA_BossMechanoidHard = 2327213834
    kBA_BossBerserker_Skytown = 3078454223
    kBA_BossBerserkerHard_Skytown = 923107635
    kBA_BossHelios = 964468362
    kBA_BossHeliosHard = 3917812391
    kBA_RedPhazzoid_Skytown1 = 3278886900
    kBA_RedPhazzoid_Skytown2 = 1516668494
    kBA_RedPhazzoid_Skytown3 = 761378520
    kBA_SkytownBridge = 3986936146
    kBA_DiscoverPod = 311100150
    SeedShieldDestroyed = 1276826815
    kBA_LeviathanEye = 3582734640
    kBA_DefenseSystem = 159852610
    kBA_BossRidley_Pirate = 3670289904
    kBA_BossRidleyHard_Pirate = 3035079377
    kBA_RedPhazzoid_Pirate1 = 2621245633
    kBA_RedPhazzoid_Pirate2 = 87316859
    kBA_RedPhazzoid_Pirate3 = 1915972077
    kBA_RedPhazzoid_Pirate4 = 3965189198
    kBA_BossGandrayda = 675653541
    kBA_BossGandraydaHard = 1583013528
    kBA_BossHatcher_Pirate = 3845519601
    kBA_BossHatcherHard_Pirate = 1020841902
    kBA_BossHarvester = 2754677268
    kBA_BossHarvesterHard = 2238270125
    kBA_BossCommander = 2159809142
    kBA_BossCommanderHard = 3026027834
    kBA_PirateCommandos20 = 1534640759
    AllTroopersSurvived = 260599856
    kBA_BossDarkSamus = 118390863
    kBA_BossDarkSamusHard = 1657177142
    kBA_BossAU = 1896894749
    kBA_BossAUHard = 3803117518
    kBA_AllSeedSwarmsKilled = 1923499191
    kBA_ScanAU = 2458173973
    kBA_ScanMogenar = 335555508
    kBA_ScanMechaRidley = 3394623414
    kBA_ScanHelios = 800279568
    kBA_ScanGhor = 392796523
    kBA_ScanRundas = 3511454777
    kBA_ScanGandrayda = 1611981353
    kBA_ScanDarkSamus = 1331676611
    kBA_BeatenReptilicus = 4154542500
    kBA_FlyingPirateJetpackGrappled = 3931564681
    kBA_ScanDefenseMechanoid = 380595334
    kBA_BowlingForBots = 470973530
    kBA_Kill100 = 2698926786
    kBA_Invalid = 2439373502

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
class Achievement(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    bonus_credit: BonusCredit = dataclasses.field(default_factory=BonusCredit, metadata={
        'reflection': FieldReflection[BonusCredit](
            BonusCredit, id=0x7aac9e22, original_name='BonusCredit', from_json=BonusCredit.from_json, to_json=BonusCredit.to_json
        ),
    })
    achievement: AchievementEnum = dataclasses.field(default=AchievementEnum.kBA_Invalid, metadata={
        'reflection': FieldReflection[AchievementEnum](
            AchievementEnum, id=0x058d2ddb, original_name='Achievement', from_json=AchievementEnum.from_json, to_json=AchievementEnum.to_json
        ),
    })
    normal_difficulty: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x974f4aa1, original_name='NormalDifficulty'
        ),
    })
    hard_difficulty: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0f8cf6ff, original_name='HardDifficulty'
        ),
    })
    elite_difficulty: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x9b8903eb, original_name='EliteDifficulty'
        ),
    })
    bonus_credit_string: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['STRG'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd6a0cff1, original_name='BonusCreditString'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'ACHI'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_ScriptAchievement.rso']

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
        if property_count != 7:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7aac9e22
        bonus_credit = BonusCredit.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x058d2ddb
        achievement = AchievementEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x974f4aa1
        normal_difficulty = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f8cf6ff
        hard_difficulty = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b8903eb
        elite_difficulty = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6a0cff1
        bonus_credit_string = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(editor_properties, bonus_credit, achievement, normal_difficulty, hard_difficulty, elite_difficulty, bonus_credit_string)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'z\xac\x9e"')  # 0x7aac9e22
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bonus_credit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x05\x8d-\xdb')  # 0x58d2ddb
        data.write(b'\x00\x04')  # size
        self.achievement.to_stream(data, game)

        data.write(b'\x97OJ\xa1')  # 0x974f4aa1
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.normal_difficulty))

        data.write(b'\x0f\x8c\xf6\xff')  # 0xf8cf6ff
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.hard_difficulty))

        data.write(b'\x9b\x89\x03\xeb')  # 0x9b8903eb
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.elite_difficulty))

        data.write(b'\xd6\xa0\xcf\xf1')  # 0xd6a0cff1
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.bonus_credit_string))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AchievementJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            bonus_credit=BonusCredit.from_json(json_data['bonus_credit']),
            achievement=AchievementEnum.from_json(json_data['achievement']),
            normal_difficulty=json_data['normal_difficulty'],
            hard_difficulty=json_data['hard_difficulty'],
            elite_difficulty=json_data['elite_difficulty'],
            bonus_credit_string=json_data['bonus_credit_string'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'bonus_credit': self.bonus_credit.to_json(),
            'achievement': self.achievement.to_json(),
            'normal_difficulty': self.normal_difficulty,
            'hard_difficulty': self.hard_difficulty,
            'elite_difficulty': self.elite_difficulty,
            'bonus_credit_string': self.bonus_credit_string,
        }

    def _dependencies_for_bonus_credit_string(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bonus_credit_string)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_bonus_credit_string(asset_manager)


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_bonus_credit(data: typing.BinaryIO, game: Game, property_size: int) -> BonusCredit:
    return BonusCredit.from_stream(data, game, property_size)


def _decode_achievement(data: typing.BinaryIO, game: Game, property_size: int) -> AchievementEnum:
    return AchievementEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x7aac9e22: ('bonus_credit', _decode_bonus_credit),
    0x058d2ddb: ('achievement', _decode_achievement),
    0x974f4aa1: ('normal_difficulty', structs.decode_BIG_bool_),
    0x0f8cf6ff: ('hard_difficulty', structs.decode_BIG_bool_),
    0x9b8903eb: ('elite_difficulty', structs.decode_BIG_bool_),
    0xd6a0cff1: ('bonus_credit_string', structs.decode_BIG_Q),
}
