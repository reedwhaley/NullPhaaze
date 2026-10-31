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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    class TweakPlayer_FirstPersonCameraJson(typing_extensions.TypedDict):
        first_person_camera_speed: float
        camera_elevation: float
        jump_camera_pitch_down_start: float
        jump_camera_pitch_down_full: float
        jump_camera_pitch_down_angle: float
        fall_camera_pitch_down_start: float
        fall_camera_pitch_down_full: float
        fall_camera_pitch_down_angle: float
        dark_light_pitch: float
        dark_light_scale: json_util.JsonValue
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xba5eb7f5, 0xd41e3ba, 0xb400ebd6, 0xfd26b7b9, 0x97b14dc6, 0xeb59925a, 0xa1d73380, 0xc8e8344a, 0xd40c480e, 0x7960c3a0)


@dataclasses.dataclass()
class TweakPlayer_FirstPersonCamera(BaseProperty):
    first_person_camera_speed: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xba5eb7f5, original_name='FirstPersonCameraSpeed'
        ),
    })
    camera_elevation: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d41e3ba, original_name='CameraElevation'
        ),
    })
    jump_camera_pitch_down_start: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb400ebd6, original_name='JumpCameraPitchDownStart'
        ),
    })
    jump_camera_pitch_down_full: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfd26b7b9, original_name='JumpCameraPitchDownFull'
        ),
    })
    jump_camera_pitch_down_angle: float = dataclasses.field(default=73.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x97b14dc6, original_name='JumpCameraPitchDownAngle'
        ),
    })
    fall_camera_pitch_down_start: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeb59925a, original_name='FallCameraPitchDownStart'
        ),
    })
    fall_camera_pitch_down_full: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa1d73380, original_name='FallCameraPitchDownFull'
        ),
    })
    fall_camera_pitch_down_angle: float = dataclasses.field(default=73.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc8e8344a, original_name='FallCameraPitchDownAngle'
        ),
    })
    dark_light_pitch: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd40c480e, original_name='DarkLightPitch'
        ),
    })
    dark_light_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=20.0, y=25.0, z=20.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x7960c3a0, original_name='DarkLightScale', from_json=Vector.from_json, to_json=Vector.to_json
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
        if property_count != 10:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfff')
    
        dec = _FAST_FORMAT.unpack(data.read(108))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            Vector(*dec[29:32]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\xba^\xb7\xf5')  # 0xba5eb7f5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.first_person_camera_speed))

        data.write(b'\rA\xe3\xba')  # 0xd41e3ba
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.camera_elevation))

        data.write(b'\xb4\x00\xeb\xd6')  # 0xb400ebd6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_camera_pitch_down_start))

        data.write(b'\xfd&\xb7\xb9')  # 0xfd26b7b9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_camera_pitch_down_full))

        data.write(b'\x97\xb1M\xc6')  # 0x97b14dc6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_camera_pitch_down_angle))

        data.write(b'\xebY\x92Z')  # 0xeb59925a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fall_camera_pitch_down_start))

        data.write(b'\xa1\xd73\x80')  # 0xa1d73380
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fall_camera_pitch_down_full))

        data.write(b'\xc8\xe84J')  # 0xc8e8344a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fall_camera_pitch_down_angle))

        data.write(b'\xd4\x0cH\x0e')  # 0xd40c480e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_light_pitch))

        data.write(b'y`\xc3\xa0')  # 0x7960c3a0
        data.write(b'\x00\x0c')  # size
        self.dark_light_scale.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_FirstPersonCameraJson", data)
        return cls(
            first_person_camera_speed=json_data['first_person_camera_speed'],
            camera_elevation=json_data['camera_elevation'],
            jump_camera_pitch_down_start=json_data['jump_camera_pitch_down_start'],
            jump_camera_pitch_down_full=json_data['jump_camera_pitch_down_full'],
            jump_camera_pitch_down_angle=json_data['jump_camera_pitch_down_angle'],
            fall_camera_pitch_down_start=json_data['fall_camera_pitch_down_start'],
            fall_camera_pitch_down_full=json_data['fall_camera_pitch_down_full'],
            fall_camera_pitch_down_angle=json_data['fall_camera_pitch_down_angle'],
            dark_light_pitch=json_data['dark_light_pitch'],
            dark_light_scale=Vector.from_json(json_data['dark_light_scale']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'first_person_camera_speed': self.first_person_camera_speed,
            'camera_elevation': self.camera_elevation,
            'jump_camera_pitch_down_start': self.jump_camera_pitch_down_start,
            'jump_camera_pitch_down_full': self.jump_camera_pitch_down_full,
            'jump_camera_pitch_down_angle': self.jump_camera_pitch_down_angle,
            'fall_camera_pitch_down_start': self.fall_camera_pitch_down_start,
            'fall_camera_pitch_down_full': self.fall_camera_pitch_down_full,
            'fall_camera_pitch_down_angle': self.fall_camera_pitch_down_angle,
            'dark_light_pitch': self.dark_light_pitch,
            'dark_light_scale': self.dark_light_scale.to_json(),
        }


def _decode_dark_light_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xba5eb7f5: ('first_person_camera_speed', structs.decode_BIG_f),
    0x0d41e3ba: ('camera_elevation', structs.decode_BIG_f),
    0xb400ebd6: ('jump_camera_pitch_down_start', structs.decode_BIG_f),
    0xfd26b7b9: ('jump_camera_pitch_down_full', structs.decode_BIG_f),
    0x97b14dc6: ('jump_camera_pitch_down_angle', structs.decode_BIG_f),
    0xeb59925a: ('fall_camera_pitch_down_start', structs.decode_BIG_f),
    0xa1d73380: ('fall_camera_pitch_down_full', structs.decode_BIG_f),
    0xc8e8344a: ('fall_camera_pitch_down_angle', structs.decode_BIG_f),
    0xd40c480e: ('dark_light_pitch', structs.decode_BIG_f),
    0x7960c3a0: ('dark_light_scale', _decode_dark_light_scale),
}
