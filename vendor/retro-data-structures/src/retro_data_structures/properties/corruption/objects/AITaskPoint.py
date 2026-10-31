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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AITaskPointJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        stay_forever: bool
        time_to_stay_min: float
        time_to_stay_max: float
        unknown: bool
        arrive_animation: int
        idle_animation: int
        exit_animation: int
        time_between_fidgets_min: float
        time_between_fidgets_max: float
        fidget_animation_one: int
        fidget_animation_two: int
        fidget_animation_three: int
        fidget_animation_four: int
        fidget_animation_five: int
        fidget_animation_six: int
        fidget_animation_seven: int
        fidget_animation_eight: int
        last_random_fidget: int
        is_combat_task: bool
        head_track_when_idling: bool
        head_track_when_fidgeting: bool
        play_fidgets_randomly: bool
        align_ai: bool
        return_to_locomotion: bool
    

@dataclasses.dataclass()
class AITaskPoint(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    stay_forever: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x56941eb7, original_name='StayForever'
        ),
    })
    time_to_stay_min: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb553cda1, original_name='TimeToStayMin'
        ),
    })
    time_to_stay_max: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x53336240, original_name='TimeToStayMax'
        ),
    })
    unknown: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x12341132, original_name='Unknown'
        ),
    })
    arrive_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xaaccd7cd, original_name='ArriveAnimation'
        ),
    })
    idle_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa2a5b38f, original_name='IdleAnimation'
        ),
    })
    exit_animation: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x799f6f58, original_name='ExitAnimation'
        ),
    })
    time_between_fidgets_min: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x121045f5, original_name='TimeBetweenFidgetsMin'
        ),
    })
    time_between_fidgets_max: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf470ea14, original_name='TimeBetweenFidgetsMax'
        ),
    })
    fidget_animation_one: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7aa31371, original_name='FidgetAnimationOne'
        ),
    })
    fidget_animation_two: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x0ac4d7ad, original_name='FidgetAnimationTwo'
        ),
    })
    fidget_animation_three: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x03d511b9, original_name='FidgetAnimationThree'
        ),
    })
    fidget_animation_four: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x2bd321da, original_name='FidgetAnimationFour'
        ),
    })
    fidget_animation_five: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x2b3bd997, original_name='FidgetAnimationFive'
        ),
    })
    fidget_animation_six: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc36101f6, original_name='FidgetAnimationSix'
        ),
    })
    fidget_animation_seven: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x3fa8c740, original_name='FidgetAnimationSeven'
        ),
    })
    fidget_animation_eight: int = dataclasses.field(default=-1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x3aca31d7, original_name='FidgetAnimationEight'
        ),
    })
    last_random_fidget: int = dataclasses.field(default=8, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe5d4d300, original_name='LastRandomFidget'
        ),
    })
    is_combat_task: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2528f442, original_name='IsCombatTask'
        ),
    })
    head_track_when_idling: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2cf6f605, original_name='HeadTrackWhenIdling'
        ),
    })
    head_track_when_fidgeting: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x81591346, original_name='HeadTrackWhenFidgeting'
        ),
    })
    play_fidgets_randomly: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf874aa52, original_name='PlayFidgetsRandomly'
        ),
    })
    align_ai: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x5c20cf58, original_name='AlignAI'
        ),
    })
    return_to_locomotion: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2340b043, original_name='ReturnToLocomotion'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'AITP'

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
        if property_count != 25:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56941eb7
        stay_forever = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb553cda1
        time_to_stay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53336240
        time_to_stay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12341132
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaaccd7cd
        arrive_animation = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa2a5b38f
        idle_animation = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x799f6f58
        exit_animation = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x121045f5
        time_between_fidgets_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf470ea14
        time_between_fidgets_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7aa31371
        fidget_animation_one = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ac4d7ad
        fidget_animation_two = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03d511b9
        fidget_animation_three = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2bd321da
        fidget_animation_four = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b3bd997
        fidget_animation_five = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc36101f6
        fidget_animation_six = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3fa8c740
        fidget_animation_seven = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3aca31d7
        fidget_animation_eight = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5d4d300
        last_random_fidget = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2528f442
        is_combat_task = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2cf6f605
        head_track_when_idling = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81591346
        head_track_when_fidgeting = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf874aa52
        play_fidgets_randomly = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5c20cf58
        align_ai = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2340b043
        return_to_locomotion = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(editor_properties, stay_forever, time_to_stay_min, time_to_stay_max, unknown, arrive_animation, idle_animation, exit_animation, time_between_fidgets_min, time_between_fidgets_max, fidget_animation_one, fidget_animation_two, fidget_animation_three, fidget_animation_four, fidget_animation_five, fidget_animation_six, fidget_animation_seven, fidget_animation_eight, last_random_fidget, is_combat_task, head_track_when_idling, head_track_when_fidgeting, play_fidgets_randomly, align_ai, return_to_locomotion)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x19')  # 25 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'V\x94\x1e\xb7')  # 0x56941eb7
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.stay_forever))

        data.write(b'\xb5S\xcd\xa1')  # 0xb553cda1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_to_stay_min))

        data.write(b'S3b@')  # 0x53336240
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_to_stay_max))

        data.write(b'\x124\x112')  # 0x12341132
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b'\xaa\xcc\xd7\xcd')  # 0xaaccd7cd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.arrive_animation))

        data.write(b'\xa2\xa5\xb3\x8f')  # 0xa2a5b38f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.idle_animation))

        data.write(b'y\x9foX')  # 0x799f6f58
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.exit_animation))

        data.write(b'\x12\x10E\xf5')  # 0x121045f5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_between_fidgets_min))

        data.write(b'\xf4p\xea\x14')  # 0xf470ea14
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_between_fidgets_max))

        data.write(b'z\xa3\x13q')  # 0x7aa31371
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_one))

        data.write(b'\n\xc4\xd7\xad')  # 0xac4d7ad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_two))

        data.write(b'\x03\xd5\x11\xb9')  # 0x3d511b9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_three))

        data.write(b'+\xd3!\xda')  # 0x2bd321da
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_four))

        data.write(b'+;\xd9\x97')  # 0x2b3bd997
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_five))

        data.write(b'\xc3a\x01\xf6')  # 0xc36101f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_six))

        data.write(b'?\xa8\xc7@')  # 0x3fa8c740
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_seven))

        data.write(b':\xca1\xd7')  # 0x3aca31d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.fidget_animation_eight))

        data.write(b'\xe5\xd4\xd3\x00')  # 0xe5d4d300
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.last_random_fidget))

        data.write(b'%(\xf4B')  # 0x2528f442
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_combat_task))

        data.write(b',\xf6\xf6\x05')  # 0x2cf6f605
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.head_track_when_idling))

        data.write(b'\x81Y\x13F')  # 0x81591346
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.head_track_when_fidgeting))

        data.write(b'\xf8t\xaaR')  # 0xf874aa52
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.play_fidgets_randomly))

        data.write(b'\\ \xcfX')  # 0x5c20cf58
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.align_ai))

        data.write(b'#@\xb0C')  # 0x2340b043
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.return_to_locomotion))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AITaskPointJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            stay_forever=json_data['stay_forever'],
            time_to_stay_min=json_data['time_to_stay_min'],
            time_to_stay_max=json_data['time_to_stay_max'],
            unknown=json_data['unknown'],
            arrive_animation=json_data['arrive_animation'],
            idle_animation=json_data['idle_animation'],
            exit_animation=json_data['exit_animation'],
            time_between_fidgets_min=json_data['time_between_fidgets_min'],
            time_between_fidgets_max=json_data['time_between_fidgets_max'],
            fidget_animation_one=json_data['fidget_animation_one'],
            fidget_animation_two=json_data['fidget_animation_two'],
            fidget_animation_three=json_data['fidget_animation_three'],
            fidget_animation_four=json_data['fidget_animation_four'],
            fidget_animation_five=json_data['fidget_animation_five'],
            fidget_animation_six=json_data['fidget_animation_six'],
            fidget_animation_seven=json_data['fidget_animation_seven'],
            fidget_animation_eight=json_data['fidget_animation_eight'],
            last_random_fidget=json_data['last_random_fidget'],
            is_combat_task=json_data['is_combat_task'],
            head_track_when_idling=json_data['head_track_when_idling'],
            head_track_when_fidgeting=json_data['head_track_when_fidgeting'],
            play_fidgets_randomly=json_data['play_fidgets_randomly'],
            align_ai=json_data['align_ai'],
            return_to_locomotion=json_data['return_to_locomotion'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'stay_forever': self.stay_forever,
            'time_to_stay_min': self.time_to_stay_min,
            'time_to_stay_max': self.time_to_stay_max,
            'unknown': self.unknown,
            'arrive_animation': self.arrive_animation,
            'idle_animation': self.idle_animation,
            'exit_animation': self.exit_animation,
            'time_between_fidgets_min': self.time_between_fidgets_min,
            'time_between_fidgets_max': self.time_between_fidgets_max,
            'fidget_animation_one': self.fidget_animation_one,
            'fidget_animation_two': self.fidget_animation_two,
            'fidget_animation_three': self.fidget_animation_three,
            'fidget_animation_four': self.fidget_animation_four,
            'fidget_animation_five': self.fidget_animation_five,
            'fidget_animation_six': self.fidget_animation_six,
            'fidget_animation_seven': self.fidget_animation_seven,
            'fidget_animation_eight': self.fidget_animation_eight,
            'last_random_fidget': self.last_random_fidget,
            'is_combat_task': self.is_combat_task,
            'head_track_when_idling': self.head_track_when_idling,
            'head_track_when_fidgeting': self.head_track_when_fidgeting,
            'play_fidgets_randomly': self.play_fidgets_randomly,
            'align_ai': self.align_ai,
            'return_to_locomotion': self.return_to_locomotion,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x56941eb7: ('stay_forever', structs.decode_BIG_bool_),
    0xb553cda1: ('time_to_stay_min', structs.decode_BIG_f),
    0x53336240: ('time_to_stay_max', structs.decode_BIG_f),
    0x12341132: ('unknown', structs.decode_BIG_bool_),
    0xaaccd7cd: ('arrive_animation', structs.decode_BIG_l),
    0xa2a5b38f: ('idle_animation', structs.decode_BIG_l),
    0x799f6f58: ('exit_animation', structs.decode_BIG_l),
    0x121045f5: ('time_between_fidgets_min', structs.decode_BIG_f),
    0xf470ea14: ('time_between_fidgets_max', structs.decode_BIG_f),
    0x7aa31371: ('fidget_animation_one', structs.decode_BIG_l),
    0x0ac4d7ad: ('fidget_animation_two', structs.decode_BIG_l),
    0x03d511b9: ('fidget_animation_three', structs.decode_BIG_l),
    0x2bd321da: ('fidget_animation_four', structs.decode_BIG_l),
    0x2b3bd997: ('fidget_animation_five', structs.decode_BIG_l),
    0xc36101f6: ('fidget_animation_six', structs.decode_BIG_l),
    0x3fa8c740: ('fidget_animation_seven', structs.decode_BIG_l),
    0x3aca31d7: ('fidget_animation_eight', structs.decode_BIG_l),
    0xe5d4d300: ('last_random_fidget', structs.decode_BIG_l),
    0x2528f442: ('is_combat_task', structs.decode_BIG_bool_),
    0x2cf6f605: ('head_track_when_idling', structs.decode_BIG_bool_),
    0x81591346: ('head_track_when_fidgeting', structs.decode_BIG_bool_),
    0xf874aa52: ('play_fidgets_randomly', structs.decode_BIG_bool_),
    0x5c20cf58: ('align_ai', structs.decode_BIG_bool_),
    0x2340b043: ('return_to_locomotion', structs.decode_BIG_bool_),
}
