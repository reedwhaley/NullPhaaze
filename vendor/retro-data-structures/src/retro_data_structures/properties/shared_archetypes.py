# Generated File
import typing

from retro_data_structures.properties.prime.archetypes import ActorParameters as _ActorParameters_Prime
from retro_data_structures.properties.echoes.archetypes import ActorParameters as _ActorParameters_Echoes
from retro_data_structures.properties.corruption.archetypes import ActorParameters as _ActorParameters_Corruption
from retro_data_structures.properties.echoes.archetypes import CameraShakerData as _CameraShakerData_Echoes
from retro_data_structures.properties.corruption.archetypes import CameraShakerData as _CameraShakerData_Corruption
from retro_data_structures.properties.echoes.archetypes import CommandData as _CommandData_Echoes
from retro_data_structures.properties.corruption.archetypes import CommandData as _CommandData_Corruption
from retro_data_structures.properties.echoes.archetypes import ConditionalTest as _ConditionalTest_Echoes
from retro_data_structures.properties.corruption.archetypes import ConditionalTest as _ConditionalTest_Corruption
from retro_data_structures.properties.echoes.archetypes import Connection as _Connection_Echoes
from retro_data_structures.properties.corruption.archetypes import Connection as _Connection_Corruption
from retro_data_structures.properties.prime.archetypes import DamageInfo as _DamageInfo_Prime
from retro_data_structures.properties.echoes.archetypes import DamageInfo as _DamageInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import DamageInfo as _DamageInfo_Corruption
from retro_data_structures.properties.prime.archetypes import DamageVulnerability as _DamageVulnerability_Prime
from retro_data_structures.properties.echoes.archetypes import DamageVulnerability as _DamageVulnerability_Echoes
from retro_data_structures.properties.corruption.archetypes import DamageVulnerability as _DamageVulnerability_Corruption
from retro_data_structures.properties.prime.archetypes import FlareDef as _FlareDef_Prime
from retro_data_structures.properties.echoes.archetypes import FlareDef as _FlareDef_Echoes
from retro_data_structures.properties.corruption.archetypes import FlareDef as _FlareDef_Corruption
from retro_data_structures.properties.prime.archetypes import GrappleParameters as _GrappleParameters_Prime
from retro_data_structures.properties.echoes.archetypes import GrappleParameters as _GrappleParameters_Echoes
from retro_data_structures.properties.corruption.archetypes import GrappleParameters as _GrappleParameters_Corruption
from retro_data_structures.properties.prime.archetypes import HealthInfo as _HealthInfo_Prime
from retro_data_structures.properties.echoes.archetypes import HealthInfo as _HealthInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import HealthInfo as _HealthInfo_Corruption
from retro_data_structures.properties.echoes.archetypes import LayerInfo as _LayerInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import LayerInfo as _LayerInfo_Corruption
from retro_data_structures.properties.prime.archetypes import LightParameters as _LightParameters_Prime
from retro_data_structures.properties.echoes.archetypes import LightParameters as _LightParameters_Echoes
from retro_data_structures.properties.corruption.archetypes import LightParameters as _LightParameters_Corruption
from retro_data_structures.properties.echoes.archetypes import MasterLayer as _MasterLayer_Echoes
from retro_data_structures.properties.corruption.archetypes import MasterLayer as _MasterLayer_Corruption
from retro_data_structures.properties.echoes.archetypes import MysteryFlyerData as _MysteryFlyerData_Echoes
from retro_data_structures.properties.corruption.archetypes import MysteryFlyerData as _MysteryFlyerData_Corruption
from retro_data_structures.properties.prime.archetypes import PatternedAITypedef as _PatternedAITypedef_Prime
from retro_data_structures.properties.echoes.archetypes import PatternedAITypedef as _PatternedAITypedef_Echoes
from retro_data_structures.properties.corruption.archetypes import PatternedAITypedef as _PatternedAITypedef_Corruption
from retro_data_structures.properties.echoes.archetypes import PlasmaBeamInfo as _PlasmaBeamInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import PlasmaBeamInfo as _PlasmaBeamInfo_Corruption
from retro_data_structures.properties.echoes.archetypes import PlatformMotionProperties as _PlatformMotionProperties_Echoes
from retro_data_structures.properties.corruption.archetypes import PlatformMotionProperties as _PlatformMotionProperties_Corruption
from retro_data_structures.properties.echoes.archetypes import PlayerInventory as _PlayerInventory_Echoes
from retro_data_structures.properties.corruption.archetypes import PlayerInventory as _PlayerInventory_Corruption
from retro_data_structures.properties.prime.archetypes import ScannableParameters as _ScannableParameters_Prime
from retro_data_structures.properties.echoes.archetypes import ScannableParameters as _ScannableParameters_Echoes
from retro_data_structures.properties.corruption.archetypes import ScannableParameters as _ScannableParameters_Corruption
from retro_data_structures.properties.echoes.archetypes import ShockWaveInfo as _ShockWaveInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import ShockWaveInfo as _ShockWaveInfo_Corruption
from retro_data_structures.properties.echoes.archetypes import SpacePirateWeaponData as _SpacePirateWeaponData_Echoes
from retro_data_structures.properties.corruption.archetypes import SpacePirateWeaponData as _SpacePirateWeaponData_Corruption
from retro_data_structures.properties.echoes.archetypes import SurroundPan as _SurroundPan_Echoes
from retro_data_structures.properties.corruption.archetypes import SurroundPan as _SurroundPan_Corruption
from retro_data_structures.properties.echoes.archetypes import TBeamInfo as _TBeamInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import TBeamInfo as _TBeamInfo_Corruption
from retro_data_structures.properties.echoes.archetypes import TDamageInfo as _TDamageInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import TDamageInfo as _TDamageInfo_Corruption
from retro_data_structures.properties.echoes.archetypes import TWeaponDamage as _TWeaponDamage_Echoes
from retro_data_structures.properties.corruption.archetypes import TWeaponDamage as _TWeaponDamage_Corruption
from retro_data_structures.properties.echoes.archetypes import TextProperties as _TextProperties_Echoes
from retro_data_structures.properties.corruption.archetypes import TextProperties as _TextProperties_Corruption
from retro_data_structures.properties.echoes.archetypes import TriggerInfo as _TriggerInfo_Echoes
from retro_data_structures.properties.corruption.archetypes import TriggerInfo as _TriggerInfo_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakAutoMapper_Base as _TweakAutoMapper_Base_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakAutoMapper_Base as _TweakAutoMapper_Base_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakAutoMapper_DoorColors as _TweakAutoMapper_DoorColors_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakAutoMapper_DoorColors as _TweakAutoMapper_DoorColors_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakBall_BoostBall as _TweakBall_BoostBall_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakBall_BoostBall as _TweakBall_BoostBall_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakBall_CannonBall as _TweakBall_CannonBall_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakBall_CannonBall as _TweakBall_CannonBall_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakBall_DeathBall as _TweakBall_DeathBall_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakBall_DeathBall as _TweakBall_DeathBall_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakBall_Misc as _TweakBall_Misc_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakBall_Misc as _TweakBall_Misc_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakBall_ScrewAttack as _TweakBall_ScrewAttack_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakBall_ScrewAttack as _TweakBall_ScrewAttack_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakGuiColors_HUDColorsTypedef as _TweakGuiColors_HUDColorsTypedef_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakGuiColors_HUDColorsTypedef as _TweakGuiColors_HUDColorsTypedef_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakGuiColors_Misc as _TweakGuiColors_Misc_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakGuiColors_Misc as _TweakGuiColors_Misc_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakGui_Completion as _TweakGui_Completion_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakGui_Completion as _TweakGui_Completion_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakGui_Credits as _TweakGui_Credits_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakGui_Credits as _TweakGui_Credits_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakGui_HudColorTypedef as _TweakGui_HudColorTypedef_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakGui_HudColorTypedef as _TweakGui_HudColorTypedef_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakGui_Misc as _TweakGui_Misc_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakGui_Misc as _TweakGui_Misc_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakGui_ScanVisor as _TweakGui_ScanVisor_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakGui_ScanVisor as _TweakGui_ScanVisor_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayerGun_Beam_Misc as _TweakPlayerGun_Beam_Misc_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayerGun_Beam_Misc as _TweakPlayerGun_Beam_Misc_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayerGun_Misc as _TweakPlayerGun_Misc_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayerGun_Misc as _TweakPlayerGun_Misc_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayerGun_RicochetDamage_Factor as _TweakPlayerGun_RicochetDamage_Factor_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayerGun_RicochetDamage_Factor as _TweakPlayerGun_RicochetDamage_Factor_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayerGun_Weapons as _TweakPlayerGun_Weapons_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayerGun_Weapons as _TweakPlayerGun_Weapons_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayerRes_AutoMapperIcons as _TweakPlayerRes_AutoMapperIcons_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayerRes_AutoMapperIcons as _TweakPlayerRes_AutoMapperIcons_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayerRes_MapScreenIcons as _TweakPlayerRes_MapScreenIcons_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayerRes_MapScreenIcons as _TweakPlayerRes_MapScreenIcons_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayer_AimStuff as _TweakPlayer_AimStuff_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayer_AimStuff as _TweakPlayer_AimStuff_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayer_Grapple as _TweakPlayer_Grapple_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayer_Grapple as _TweakPlayer_Grapple_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayer_Misc as _TweakPlayer_Misc_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayer_Misc as _TweakPlayer_Misc_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayer_Motion as _TweakPlayer_Motion_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayer_Motion as _TweakPlayer_Motion_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayer_ScanVisor as _TweakPlayer_ScanVisor_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayer_ScanVisor as _TweakPlayer_ScanVisor_Corruption
from retro_data_structures.properties.echoes.archetypes import TweakPlayer_SuitDamageReduction as _TweakPlayer_SuitDamageReduction_Echoes
from retro_data_structures.properties.corruption.archetypes import TweakPlayer_SuitDamageReduction as _TweakPlayer_SuitDamageReduction_Corruption
from retro_data_structures.properties.prime.archetypes import Vector2f as _Vector2f_Prime
from retro_data_structures.properties.echoes.archetypes import Vector2f as _Vector2f_Echoes
from retro_data_structures.properties.corruption.archetypes import Vector2f as _Vector2f_Corruption
from retro_data_structures.properties.prime.archetypes import VisorParameters as _VisorParameters_Prime
from retro_data_structures.properties.echoes.archetypes import VisorParameters as _VisorParameters_Echoes
from retro_data_structures.properties.corruption.archetypes import VisorParameters as _VisorParameters_Corruption
from retro_data_structures.properties.echoes.archetypes import WeaponVulnerability as _WeaponVulnerability_Echoes
from retro_data_structures.properties.corruption.archetypes import WeaponVulnerability as _WeaponVulnerability_Corruption

type ActorParameters = typing.Union[
    _ActorParameters_Prime,
    _ActorParameters_Echoes,
    _ActorParameters_Corruption
]
type CameraShakerData = typing.Union[
    _CameraShakerData_Echoes,
    _CameraShakerData_Corruption
]
type CommandData = typing.Union[
    _CommandData_Echoes,
    _CommandData_Corruption
]
type ConditionalTest = typing.Union[
    _ConditionalTest_Echoes,
    _ConditionalTest_Corruption
]
type Connection = typing.Union[
    _Connection_Echoes,
    _Connection_Corruption
]
type DamageInfo = typing.Union[
    _DamageInfo_Prime,
    _DamageInfo_Echoes,
    _DamageInfo_Corruption
]
type DamageVulnerability = typing.Union[
    _DamageVulnerability_Prime,
    _DamageVulnerability_Echoes,
    _DamageVulnerability_Corruption
]
type FlareDef = typing.Union[
    _FlareDef_Prime,
    _FlareDef_Echoes,
    _FlareDef_Corruption
]
type GrappleParameters = typing.Union[
    _GrappleParameters_Prime,
    _GrappleParameters_Echoes,
    _GrappleParameters_Corruption
]
type HealthInfo = typing.Union[
    _HealthInfo_Prime,
    _HealthInfo_Echoes,
    _HealthInfo_Corruption
]
type LayerInfo = typing.Union[
    _LayerInfo_Echoes,
    _LayerInfo_Corruption
]
type LightParameters = typing.Union[
    _LightParameters_Prime,
    _LightParameters_Echoes,
    _LightParameters_Corruption
]
type MasterLayer = typing.Union[
    _MasterLayer_Echoes,
    _MasterLayer_Corruption
]
type MysteryFlyerData = typing.Union[
    _MysteryFlyerData_Echoes,
    _MysteryFlyerData_Corruption
]
type PatternedAITypedef = typing.Union[
    _PatternedAITypedef_Prime,
    _PatternedAITypedef_Echoes,
    _PatternedAITypedef_Corruption
]
type PlasmaBeamInfo = typing.Union[
    _PlasmaBeamInfo_Echoes,
    _PlasmaBeamInfo_Corruption
]
type PlatformMotionProperties = typing.Union[
    _PlatformMotionProperties_Echoes,
    _PlatformMotionProperties_Corruption
]
type PlayerInventory = typing.Union[
    _PlayerInventory_Echoes,
    _PlayerInventory_Corruption
]
type ScannableParameters = typing.Union[
    _ScannableParameters_Prime,
    _ScannableParameters_Echoes,
    _ScannableParameters_Corruption
]
type ShockWaveInfo = typing.Union[
    _ShockWaveInfo_Echoes,
    _ShockWaveInfo_Corruption
]
type SpacePirateWeaponData = typing.Union[
    _SpacePirateWeaponData_Echoes,
    _SpacePirateWeaponData_Corruption
]
type SurroundPan = typing.Union[
    _SurroundPan_Echoes,
    _SurroundPan_Corruption
]
type TBeamInfo = typing.Union[
    _TBeamInfo_Echoes,
    _TBeamInfo_Corruption
]
type TDamageInfo = typing.Union[
    _TDamageInfo_Echoes,
    _TDamageInfo_Corruption
]
type TWeaponDamage = typing.Union[
    _TWeaponDamage_Echoes,
    _TWeaponDamage_Corruption
]
type TextProperties = typing.Union[
    _TextProperties_Echoes,
    _TextProperties_Corruption
]
type TriggerInfo = typing.Union[
    _TriggerInfo_Echoes,
    _TriggerInfo_Corruption
]
type TweakAutoMapper_Base = typing.Union[
    _TweakAutoMapper_Base_Echoes,
    _TweakAutoMapper_Base_Corruption
]
type TweakAutoMapper_DoorColors = typing.Union[
    _TweakAutoMapper_DoorColors_Echoes,
    _TweakAutoMapper_DoorColors_Corruption
]
type TweakBall_BoostBall = typing.Union[
    _TweakBall_BoostBall_Echoes,
    _TweakBall_BoostBall_Corruption
]
type TweakBall_CannonBall = typing.Union[
    _TweakBall_CannonBall_Echoes,
    _TweakBall_CannonBall_Corruption
]
type TweakBall_DeathBall = typing.Union[
    _TweakBall_DeathBall_Echoes,
    _TweakBall_DeathBall_Corruption
]
type TweakBall_Misc = typing.Union[
    _TweakBall_Misc_Echoes,
    _TweakBall_Misc_Corruption
]
type TweakBall_ScrewAttack = typing.Union[
    _TweakBall_ScrewAttack_Echoes,
    _TweakBall_ScrewAttack_Corruption
]
type TweakGuiColors_HUDColorsTypedef = typing.Union[
    _TweakGuiColors_HUDColorsTypedef_Echoes,
    _TweakGuiColors_HUDColorsTypedef_Corruption
]
type TweakGuiColors_Misc = typing.Union[
    _TweakGuiColors_Misc_Echoes,
    _TweakGuiColors_Misc_Corruption
]
type TweakGui_Completion = typing.Union[
    _TweakGui_Completion_Echoes,
    _TweakGui_Completion_Corruption
]
type TweakGui_Credits = typing.Union[
    _TweakGui_Credits_Echoes,
    _TweakGui_Credits_Corruption
]
type TweakGui_HudColorTypedef = typing.Union[
    _TweakGui_HudColorTypedef_Echoes,
    _TweakGui_HudColorTypedef_Corruption
]
type TweakGui_Misc = typing.Union[
    _TweakGui_Misc_Echoes,
    _TweakGui_Misc_Corruption
]
type TweakGui_ScanVisor = typing.Union[
    _TweakGui_ScanVisor_Echoes,
    _TweakGui_ScanVisor_Corruption
]
type TweakPlayerGun_Beam_Misc = typing.Union[
    _TweakPlayerGun_Beam_Misc_Echoes,
    _TweakPlayerGun_Beam_Misc_Corruption
]
type TweakPlayerGun_Misc = typing.Union[
    _TweakPlayerGun_Misc_Echoes,
    _TweakPlayerGun_Misc_Corruption
]
type TweakPlayerGun_RicochetDamage_Factor = typing.Union[
    _TweakPlayerGun_RicochetDamage_Factor_Echoes,
    _TweakPlayerGun_RicochetDamage_Factor_Corruption
]
type TweakPlayerGun_Weapons = typing.Union[
    _TweakPlayerGun_Weapons_Echoes,
    _TweakPlayerGun_Weapons_Corruption
]
type TweakPlayerRes_AutoMapperIcons = typing.Union[
    _TweakPlayerRes_AutoMapperIcons_Echoes,
    _TweakPlayerRes_AutoMapperIcons_Corruption
]
type TweakPlayerRes_MapScreenIcons = typing.Union[
    _TweakPlayerRes_MapScreenIcons_Echoes,
    _TweakPlayerRes_MapScreenIcons_Corruption
]
type TweakPlayer_AimStuff = typing.Union[
    _TweakPlayer_AimStuff_Echoes,
    _TweakPlayer_AimStuff_Corruption
]
type TweakPlayer_Grapple = typing.Union[
    _TweakPlayer_Grapple_Echoes,
    _TweakPlayer_Grapple_Corruption
]
type TweakPlayer_Misc = typing.Union[
    _TweakPlayer_Misc_Echoes,
    _TweakPlayer_Misc_Corruption
]
type TweakPlayer_Motion = typing.Union[
    _TweakPlayer_Motion_Echoes,
    _TweakPlayer_Motion_Corruption
]
type TweakPlayer_ScanVisor = typing.Union[
    _TweakPlayer_ScanVisor_Echoes,
    _TweakPlayer_ScanVisor_Corruption
]
type TweakPlayer_SuitDamageReduction = typing.Union[
    _TweakPlayer_SuitDamageReduction_Echoes,
    _TweakPlayer_SuitDamageReduction_Corruption
]
type Vector2f = typing.Union[
    _Vector2f_Prime,
    _Vector2f_Echoes,
    _Vector2f_Corruption
]
type VisorParameters = typing.Union[
    _VisorParameters_Prime,
    _VisorParameters_Echoes,
    _VisorParameters_Corruption
]
type WeaponVulnerability = typing.Union[
    _WeaponVulnerability_Echoes,
    _WeaponVulnerability_Corruption
]
