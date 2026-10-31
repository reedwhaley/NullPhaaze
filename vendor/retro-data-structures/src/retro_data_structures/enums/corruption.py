"""
Generated file.
"""
import enum
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs


class State(enum.Enum):
    NonZero = '!ZER'
    Acquired = 'ACQU'
    Active = 'ACTV'
    AILogicState1 = 'AIS1'
    AILogicState2 = 'AIS2'
    AILogicState3 = 'AIS3'
    AnimOver = 'ANMO'
    AnimStart = 'ANMS'
    Approach = 'APRC'
    Arrived = 'ARRV'
    AttachedCollisionObject = 'ATCL'
    AttachedAnimatedObject = 'ATOB'
    AttachedPath = 'ATPA'
    Attack = 'ATTK'
    BezierSpline = 'BEZR'
    BallIceXDamage = 'BIDG'
    BeginScan = 'BSCN'
    BSpline = 'BSPL'
    BallXDamage = 'BXDG'
    CustomInterpolation = 'CINT'
    Closed = 'CLOS'
    Connect = 'CONN'
    CameraPath = 'CPTH'
    CatmullRomSpline = 'CROM'
    CameraTarget = 'CTGT'
    CameraTime = 'CTIM'
    Damage = 'DAMG'
    DamageBomb = 'DBMB'
    Dead = 'DEAD'
    DeGenerate = 'DGNR'
    Down = 'DOWN'
    DarkXDamage = 'DRKX'
    Entered = 'ENTR'
    EndScan = 'ESCN'
    Exited = 'EXIT'
    Footstep = 'FOOT'
    FOVPath = 'FOVP'
    Freeze = 'FREZ'
    Generate0 = 'GRN0'
    Generate1 = 'GRN1'
    Generate = 'GRNT'
    InheritBounds = 'IBND'
    Inactive = 'ICTV'
    IceXDamage = 'IDMG'
    Inside = 'INSD'
    InternalState00 = 'IS00'
    InternalState01 = 'IS01'
    InternalState02 = 'IS02'
    InternalState03 = 'IS03'
    InternalState04 = 'IS04'
    InternalState05 = 'IS05'
    InternalState06 = 'IS06'
    InternalState07 = 'IS07'
    InternalState08 = 'IS08'
    InternalState09 = 'IS09'
    InternalState10 = 'IS10'
    InternalState11 = 'IS11'
    InternalState12 = 'IS12'
    InternalState13 = 'IS13'
    InternalState14 = 'IS14'
    InternalState15 = 'IS15'
    InternalState16 = 'IS16'
    InternalState17 = 'IS17'
    InternalState18 = 'IS18'
    InternalState19 = 'IS19'
    InternalState20 = 'IS20'
    InternalState21 = 'IS21'
    InternalState22 = 'IS22'
    InternalState23 = 'IS23'
    InternalState24 = 'IS24'
    InternalState25 = 'IS25'
    InternalState26 = 'IS26'
    InternalState27 = 'IS27'
    InternalState28 = 'IS28'
    InternalState29 = 'IS29'
    InternalState30 = 'IS30'
    InternalState31 = 'IS31'
    InternalState32 = 'IS32'
    InternalState33 = 'IS33'
    InternalState34 = 'IS34'
    InternalState35 = 'IS35'
    InternalState36 = 'IS36'
    InternalState37 = 'IS37'
    InternalState38 = 'IS38'
    InternalState39 = 'IS39'
    InternalState40 = 'IS40'
    InternalState41 = 'IS41'
    InternalState44 = 'IS44'
    InternalState45 = 'IS45'
    InternalState46 = 'IS46'
    InternalState47 = 'IS47'
    InternalState48 = 'IS48'
    DrawAfter = 'LDWA'
    DrawBefore = 'LDWB'
    Left = 'LEFT'
    LinearSpline = 'LINR'
    Locked = 'LOCK'
    ThinkAfter = 'LTKA'
    ThinkBefore = 'LTKB'
    MaxReached = 'MAXR'
    Modify = 'MDFY'
    MotionPath = 'MOTP'
    MotionSpline = 'MOTS'
    Next = 'NEXT'
    Open = 'OPEN'
    OrbitObject = 'ORBO'
    Play = 'PLAY'
    PlayerPath = 'PLRP'
    PressA = 'PRSA'
    PressB = 'PRSB'
    PressStart = 'PRST'
    PressX = 'PRSX'
    PressY = 'PRSY'
    PressZ = 'PRSZ'
    Patrol = 'PTRL'
    DeathRattle = 'RATL'
    RCRM = 'RCRM'
    SpawnResidue = 'RDUE'
    ReflectedDamage = 'REFD'
    ResistedDamage = 'RESD'
    Right = 'RGHT'
    Relay = 'RLAY'
    RotationOver = 'ROTO'
    RotationStart = 'ROTS'
    Retreat = 'RTRT'
    ScanDone = 'SCND'
    ScanSource = 'SCNS'
    ScriptEvent01 = 'SE01'
    ScriptEvent02 = 'SE02'
    ScriptEvent03 = 'SE03'
    Slave = 'SLAV'
    SpawnLargeCreatures = 'SLCR'
    SpawnMediumCreatures = 'SMCR'
    Sequence = 'SQNC'
    SpawnSmallCreatures = 'SSCR'
    TargetObject = 'TGTO'
    TargetPath = 'TGTP'
    TargetSpline = 'TGTS'
    UnFreeze = 'UFRZ'
    Unlocked = 'ULCK'
    Up = 'UP  '
    WLTE = 'WLTE'
    BackToFront = 'XB2F'
    XDamage = 'XDMG'
    FrontToBack = 'XF2B'
    InBack = 'XINB'
    InFront = 'XINF'
    Outside = 'XOUT'
    Zero = 'ZERO'

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (str))
        return cls(data)

    def to_json(self) -> str:
        return self.value


class Message(enum.Enum):
    Action = 'ACTN'
    Activate = 'ACTV'
    Alert = 'ALRT'
    Arrived = 'ARRV'
    Attach = 'ATCH'
    AttachInstance = 'ATCI'
    Close = 'CLOS'
    ClearOriginator = 'CORG'
    Deactivate = 'DCTV'
    Decrement = 'DECR'
    Down = 'DOWN'
    Escape = 'ESCP'
    FadeIn = 'FADI'
    FadeOut = 'FADO'
    Follow = 'FOLW'
    InternalMessage00 = 'IM00'
    InternalMessage01 = 'IM01'
    InternalMessage02 = 'IM02'
    InternalMessage03 = 'IM03'
    InternalMessage04 = 'IM04'
    InternalMessage05 = 'IM05'
    InternalMessage06 = 'IM06'
    InternalMessage07 = 'IM07'
    InternalMessage08 = 'IM08'
    InternalMessage09 = 'IM09'
    InternalMessage10 = 'IM10'
    InternalMessage11 = 'IM11'
    InternalMessage12 = 'IM12'
    InternalMessage13 = 'IM13'
    InternalMessage14 = 'IM14'
    InternalMessage15 = 'IM15'
    InternalMessage16 = 'IM16'
    InternalMessage17 = 'IM17'
    InternalMessage18 = 'IM18'
    InternalMessage19 = 'IM19'
    InternalMessage20 = 'IM20'
    InternalMessage21 = 'IM21'
    InternalMessage22 = 'IM22'
    InternalMessage23 = 'IM23'
    InternalMessage24 = 'IM24'
    InternalMessage25 = 'IM25'
    InternalMessage26 = 'IM26'
    InternalMessage27 = 'IM27'
    InternalMessage28 = 'IM28'
    InternalMessage42 = 'IM42'
    InternalMessage43 = 'IM43'
    Increment = 'INCR'
    Kill = 'KILL'
    Left = 'LEFT'
    Load = 'LOAD'
    Lock = 'LOCK'
    Next = 'NEXT'
    _None = 'NONE'
    Off = 'OFF '
    On = 'ON  '
    Open = 'OPEN'
    Play = 'PLAY'
    Right = 'RGHT'
    ResetMovement = 'RMOV'
    ResetAngle = 'RSAN'
    Reset = 'RSET'
    ResetPath = 'RSTP'
    ResetAndStart = 'RSTS'
    StopAllSounds = 'SALL'
    StopAllLoopedSounds = 'SALP'
    SetToMax = 'SMAX'
    SetOriginator = 'SORG'
    Stop = 'STOP'
    StopAndReset = 'STPR'
    Start = 'STRT'
    ToggleActive = 'TCTV'
    ToggleOpen = 'TOPN'
    Unlock = 'ULCK'
    Unload = 'ULOD'
    Up = 'UP  '
    AreaLoaded = 'XALD'
    AcidOnVisor = 'XAOV'
    AIUpdateDisabled = 'XAUD'
    AreaUnloading = 'XAUL'
    Clear = 'XCLR'
    Create = 'XCRT'
    Delete = 'XDEL'
    XDamage = 'XDMG'
    EnteredFluid = 'XENF'
    XENT = 'XENT'
    EnteredPhazonPool = 'XEPZ'
    ExitedFluid = 'XEXF'
    Falling = 'XFAL'
    HitObject = 'XHIT'
    InsideFluid = 'XINF'
    InShrubbery = 'XINS'
    InsidePhazonPool = 'XIPZ'
    Launching = 'XLAU'
    Landed = 'XLND'
    LandedOnStaticGround = 'XLSG'
    OffGround = 'XOFF'
    OnDirt = 'XOND'
    OnIce = 'XONI'
    OnOrganic = 'XONO'
    OnPlatform = 'XONP'
    XRDG = 'XRDG'
    WorldLoaded = 'XWLD'
    XXDG = 'XXDG'
    ExitedPhazonPool = 'XXPZ'
    SetToZero = 'ZERO'

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (str))
        return cls(data)

    def to_json(self) -> str:
        return self.value


class CableEnumEnum(enum.IntEnum):
    kLocation_Start = 2161975732
    kLocation_Burn = 617560305
    kLocation_End = 590757843

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


class DamageableTriggerEnumEnum(enum.IntEnum):
    kDO_None = 498294111
    kDO_Translation = 1637064024
    kDO_Transformation = 945710146
    kDO_ActorTransformation = 210876390

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


class DifficultyEnumEnum(enum.IntEnum):
    kDifficulty_Normal = 2457151020
    kDifficulty_Veteran = 2362448510
    kDifficulty_Hypermode = 2161792701
    kDifficulty_All = 4046075334

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


class HyperModeTypeEnum(enum.IntEnum):
    kHMT_Timer = 2781966248
    kHMT_PhazonLevel = 440171881
    kHMT_PhazonLevelTimer = 4246244689

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


class OrientationEnum(enum.IntEnum):
    kOT_None = 1990589437
    kOT_MovementDirection = 2503861812
    kOT_Physics = 2707747667

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


class PhysicalControlEnum(enum.IntEnum):
    kControl_REV_Home = 538784560
    kControl_REV_Select = 3795023653
    kControl_REV_A = 2527082480
    kControl_REV_B = 262760010
    kControl_REV_Small_a = 1706296828
    kControl_REV_Small_b = 4240266310
    kControl_REV_Start = 3978335045
    kControl_REV_PadUp = 371522223
    kControl_REV_PadDown = 1096604377
    kControl_REV_PadRight = 680639111
    kControl_REV_PadLeft = 667200906
    kControl_REV_PadAny = 2697488232
    kControl_REV_AnalogUp = 1761263604
    kControl_REV_AnalogUpLeft = 2435665866
    kControl_REV_AnalogUpRight = 1593512693
    kControl_REV_AnalogDown = 514168199
    kControl_REV_AnalogDownLeft = 1496847900
    kControl_REV_AnalogDownRight = 830697549
    kControl_REV_AnalogRight = 2753380155
    kControl_REV_AnalogLeft = 2017321684
    kControl_REV_Z1 = 1170446731
    kControl_REV_Z2 = 3704277041
    kControl_REV_NUNCHAKU_RollLeft = 3114222144
    kControl_REV_NUNCHAKU_RollRight = 1405012678
    kControl_REV_NUNCHAKU_PitchUp = 2759137981
    kControl_REV_NUNCHAKU_PitchDown = 2577594915
    kControl_REV_DPD_Up = 1462419467
    kControl_REV_DPD_Down = 1295727496
    kControl_REV_DPD_Right = 888257540
    kControl_REV_DPD_Left = 732122331
    kControl_REV_DPD_RollLeft = 1712867438
    kControl_REV_DPD_RollRight = 2411151363
    kControl_REV_DPD_PitchUp = 1133573905
    kControl_REV_DPD_PitchDown = 1168863462
    kControl_GC_A = 3776455486
    kControl_GC_B = 2014409348
    kControl_GC_X = 2238942206
    kControl_GC_Y = 4067736424
    kControl_GC_Start = 2195767795
    kControl_GC_Z = 1803414226
    kControl_GC_L = 2678677379
    kControl_GC_R = 1705403104
    kControl_GC_DUp = 1923125713
    kControl_GC_DRight = 438438636
    kControl_GC_DDown = 713052917
    kControl_GC_DLeft = 1276650918
    kControl_GC_TrigLeft = 4150513473
    kControl_GC_TrigRight = 620168925
    kControl_GC_AnalogUp = 3133194335
    kControl_GC_AnalogDown = 2481737266
    kControl_GC_AnalogRight = 530264547
    kControl_GC_AnalogLeft = 4118034785
    kControl_GC_CStickUp = 3915798836
    kControl_GC_CStickDown = 2620818456
    kControl_GC_CStickRight = 3291423487
    kControl_GC_CStickLeft = 4205769547
    kControl_PC_MouseUp = 4018211503
    kControl_PC_MouseDown = 4242657632
    kControl_PC_MouseRight = 2593197220
    kControl_PC_MouseLeft = 2591663667
    kControl_PC_MouseLeftButton = 391300525
    kControl_PC_MouseMiddleButton = 1938441096
    kControl_PC_MouseRightButton = 1047334326

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


class PhysicalControlBooleanEnum(enum.IntEnum):
    kPCB_And = 3437305164
    kPCB_Or = 1743300625
    kPCB_Not = 3272702804

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


class PlayerItemEnum(enum.IntEnum):
    kItem_PowerBeam = 4218679992
    kItem_PlasmaBeam = 2477616633
    kItem_NovaBeam = 1352706725
    kItem_ChargeUpgrade = 893945120
    kItem_Missile = 2452465320
    kItem_IceMissile = 2431700692
    kItem_SeekerMissile = 3086280557
    kItem_GrappleBeamPull = 1906007133
    kItem_GrappleBeamSwing = 522801372
    kItem_GrappleBeamVoltage = 536233745
    kItem_Bomb = 3112660177
    kItem_CombatVisor = 2523287191
    kItem_ScanVisor = 3016416327
    kItem_CommandVisor = 1943434474
    kItem_XRayVisor = 1714103130
    kItem_DoubleJump = 2512389418
    kItem_ScrewAttack = 3654131422
    kItem_Suit = 3492481752
    kItem_Energy = 649447109
    kItem_HypermodeEnergy = 496397544
    kItem_EnergyTank = 3010129117
    kItem_ItemPercentage = 1347001155
    kItem_Fuses = 2881244206
    kItem_Fuse1 = 862874770
    kItem_Fuse2 = 2858892584
    kItem_Fuse3 = 3714059710
    kItem_Fuse4 = 1124374557
    kItem_Fuse5 = 872654987
    kItem_Fuse6 = 2903177521
    kItem_Fuse7 = 3658336679
    kItem_Fuse8 = 1253233718
    kItem_Fuse9 = 1035330720
    kItem_MorphBall = 1211073077
    kItem_BoostBall = 2988161223
    kItem_SpiderBall = 1296127826
    kItem_HyperModeTank = 1432926409
    kItem_HyperModeBeam = 1239982508
    kItem_HyperModeMissile = 1364547232
    kItem_HyperModeBall = 2353547179
    kItem_HyperModeGrapple = 2270562373
    kItem_HyperModePermanent = 2414588173
    kItem_HyperModePhaaze = 4110398365
    kItem_HyperModeOriginal = 3854177617
    kItem_ShipGrapple = 1470237978
    kItem_ShipMissile = 2174833663
    kItem_FaceCorruptionLevel = 2109957860
    kItem_PhazonBall = 1373743611
    kItem_CannonBall = 2070581050
    kItem_ActivateMorphballBoost = 3022734302
    kItem_HyperShot = 2307731988
    kItem_CommandVisorJammed = 1065514078
    kItem_StatEnemiesKilled = 3227265003
    kItem_StatShotsFired = 2966561623
    kItem_StatDamageReceived = 3809976091
    kItem_StatDataSaves = 4187912088
    kItem_StatHypermodeUses = 1141429883
    kItem_StatCommandoKills = 1206369514
    kItem_StatTinCanHighScore = 574164774
    kItem_StatTinCanCurrentScore = 951995458

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


class QuickSelectMethodEnum(enum.IntEnum):
    kQSM_None = 3138569503
    kQSM_Held = 3604958465
    kQSM_Release = 1504980732
    kQSM_Modal = 3891005505
    kQSM_ModalAndPress = 4199960577

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


class RevViewLockTypeEnum(enum.IntEnum):
    kVLT_HoldToLock = 3836570269
    kVLT_HoldToFreeLook = 3796405200
    kVLT_Toggle = 4233376783

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


class RevolutionControlTypeEnum(enum.IntEnum):
    kRCT_None = 1989807457
    kRCT_Physical = 3492954719
    kRCT_PhysicalCombo = 2606158878
    kRCT_Virtual = 1231291285
    kRCT_VirtualCombo = 3555293293
    kRCT_Pointer = 1272469130
    kRCT_Gesture = 3663496210

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


class RevolutionGestureEnum(enum.IntEnum):
    kRG_ThrustForward = 2597642428
    kRG_ThrustBackward = 1190654113
    kRG_LeftToRight = 2373762245
    kRG_RightToLeft = 2784335752
    kRG_DownToUp = 1553256326
    kRG_UpToDown = 3438239968
    kRG_NunchakuThrustForward = 2352913090
    kRG_NunchakuThrustBackward = 4049356512
    kRG_NunchakuLeftToRight = 3952457493
    kRG_NunchakuRightToLeft = 3273432152
    kRG_NunchakuDownToUp = 2212135243
    kRG_NunchakuUpToDown = 329330221

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


class RevolutionPointerShapeEnum(enum.IntEnum):
    kRPS_Circle = 1154737403
    kRPS_Rectangle = 967762110
    kRPS_PieSlice = 1744548478

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


class RevolutionVirtualControlEnum(enum.IntEnum):
    kRVC_Tap = 2997493716
    kRVC_FlickHoriz = 288465778
    kRVC_FlickVert = 4009748226
    kRVC_UpBeat = 3635765891
    kRVC_DownBeat = 891244416
    kRVC_LeftBeat = 2689619302
    kRVC_RightBeat = 837808268
    kRVC_Shake = 21086754
    kRVC_NunchakuTap = 396303202
    kRVC_NunchakuFlickHoriz = 3664856383
    kRVC_NunchakuFlickVert = 3484034738
    kRVC_NunchakuUpBeat = 733602211
    kRVC_NunchakuDownBeat = 3559541428
    kRVC_NunchakuLeftBeat = 1097158738
    kRVC_NunchakuRightBeat = 280637756
    kRVC_NunchakuShake = 3031673392

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


class ScanSpeedEnum(enum.IntEnum):
    Normal = 0
    Slow = 1

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


class TweakGui_UnknownEnum1Enum(enum.IntEnum):
    Unknown1 = 4043628561
    Unknown2 = 1745727915
    Unknown3 = 520782141
    Unknown4 = 2171475102
    Unknown5 = 4134085640
    Unknown6 = 1868592562
    Unknown9 = 4292831267
    Unknown10 = 1285035198

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


class TweakPlayer_AimStuff_UnknownEnum2Enum(enum.IntEnum):
    kIRT_None = 2531440486
    kIRT_Both = 313036472
    kIRT_Horiz = 576609856
    kIRT_Vert = 2183082095

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
