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
from retro_data_structures.properties.corruption.archetypes.GrappleBlock import GrappleBlock
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SeedBoss1OrbDataJson(typing_extensions.TypedDict):
        normal_vulnerability: json_util.JsonObject
        not_slotted_vulnerability: json_util.JsonObject
        grapple_block: json_util.JsonObject
        initial_color: json_util.JsonValue
        should_generate: bool
        orb_damage_effect: int
        orb_destroyed_sound: int
        travel_time: float
        orb_damage_percentage: float
        regen_rate: float
        regen_delay: float
    

@dataclasses.dataclass()
class SeedBoss1OrbData(BaseProperty):
    normal_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x29df61e1, original_name='NormalVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    not_slotted_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xed8f36cf, original_name='NotSlottedVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    grapple_block: GrappleBlock = dataclasses.field(default_factory=GrappleBlock, metadata={
        'reflection': FieldReflection[GrappleBlock](
            GrappleBlock, id=0x922ef2cd, original_name='GrappleBlock', from_json=GrappleBlock.from_json, to_json=GrappleBlock.to_json
        ),
    })
    initial_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9f4149af, original_name='InitialColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    should_generate: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x5319e29b, original_name='ShouldGenerate'
        ),
    })
    orb_damage_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa0285357, original_name='OrbDamageEffect'
        ),
    })
    orb_destroyed_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x53cf49f6, original_name='OrbDestroyedSound'
        ),
    })
    travel_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x88474244, original_name='TravelTime'
        ),
    })
    orb_damage_percentage: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb3187a53, original_name='OrbDamagePercentage'
        ),
    })
    regen_rate: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x46e661f7, original_name='RegenRate'
        ),
    })
    regen_delay: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf1456ca, original_name='RegenDelay'
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
        if property_count != 11:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29df61e1
        normal_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed8f36cf
        not_slotted_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x922ef2cd
        grapple_block = GrappleBlock.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f4149af
        initial_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5319e29b
        should_generate = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0285357
        orb_damage_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53cf49f6
        orb_destroyed_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88474244
        travel_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3187a53
        orb_damage_percentage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46e661f7
        regen_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf1456ca
        regen_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(normal_vulnerability, not_slotted_vulnerability, grapple_block, initial_color, should_generate, orb_damage_effect, orb_destroyed_sound, travel_time, orb_damage_percentage, regen_rate, regen_delay)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0b')  # 11 properties

        data.write(b')\xdfa\xe1')  # 0x29df61e1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.normal_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\x8f6\xcf')  # 0xed8f36cf
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.not_slotted_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x92.\xf2\xcd')  # 0x922ef2cd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_block.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9fAI\xaf')  # 0x9f4149af
        data.write(b'\x00\x10')  # size
        self.initial_color.to_stream(data, game)

        data.write(b'S\x19\xe2\x9b')  # 0x5319e29b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.should_generate))

        data.write(b'\xa0(SW')  # 0xa0285357
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.orb_damage_effect))

        data.write(b'S\xcfI\xf6')  # 0x53cf49f6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.orb_destroyed_sound))

        data.write(b'\x88GBD')  # 0x88474244
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.travel_time))

        data.write(b'\xb3\x18zS')  # 0xb3187a53
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orb_damage_percentage))

        data.write(b'F\xe6a\xf7')  # 0x46e661f7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.regen_rate))

        data.write(b'\xcf\x14V\xca')  # 0xcf1456ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.regen_delay))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss1OrbDataJson", data)
        return cls(
            normal_vulnerability=DamageVulnerability.from_json(json_data['normal_vulnerability']),
            not_slotted_vulnerability=DamageVulnerability.from_json(json_data['not_slotted_vulnerability']),
            grapple_block=GrappleBlock.from_json(json_data['grapple_block']),
            initial_color=Color.from_json(json_data['initial_color']),
            should_generate=json_data['should_generate'],
            orb_damage_effect=json_data['orb_damage_effect'],
            orb_destroyed_sound=json_data['orb_destroyed_sound'],
            travel_time=json_data['travel_time'],
            orb_damage_percentage=json_data['orb_damage_percentage'],
            regen_rate=json_data['regen_rate'],
            regen_delay=json_data['regen_delay'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'normal_vulnerability': self.normal_vulnerability.to_json(),
            'not_slotted_vulnerability': self.not_slotted_vulnerability.to_json(),
            'grapple_block': self.grapple_block.to_json(),
            'initial_color': self.initial_color.to_json(),
            'should_generate': self.should_generate,
            'orb_damage_effect': self.orb_damage_effect,
            'orb_destroyed_sound': self.orb_destroyed_sound,
            'travel_time': self.travel_time,
            'orb_damage_percentage': self.orb_damage_percentage,
            'regen_rate': self.regen_rate,
            'regen_delay': self.regen_delay,
        }

    def _dependencies_for_orb_damage_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.orb_damage_effect)

    def _dependencies_for_orb_destroyed_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.orb_destroyed_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_orb_damage_effect, "orb_damage_effect", "AssetId"),
            (self._dependencies_for_orb_destroyed_sound, "orb_destroyed_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SeedBoss1OrbData.{field_name} ({field_type}): {e}"
                )


def _decode_normal_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_not_slotted_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_grapple_block(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


def _decode_initial_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x29df61e1: ('normal_vulnerability', _decode_normal_vulnerability),
    0xed8f36cf: ('not_slotted_vulnerability', _decode_not_slotted_vulnerability),
    0x922ef2cd: ('grapple_block', _decode_grapple_block),
    0x9f4149af: ('initial_color', _decode_initial_color),
    0x5319e29b: ('should_generate', structs.decode_BIG_bool_),
    0xa0285357: ('orb_damage_effect', structs.decode_BIG_Q),
    0x53cf49f6: ('orb_destroyed_sound', structs.decode_BIG_Q),
    0x88474244: ('travel_time', structs.decode_BIG_f),
    0xb3187a53: ('orb_damage_percentage', structs.decode_BIG_f),
    0x46e661f7: ('regen_rate', structs.decode_BIG_f),
    0xcf1456ca: ('regen_delay', structs.decode_BIG_f),
}
