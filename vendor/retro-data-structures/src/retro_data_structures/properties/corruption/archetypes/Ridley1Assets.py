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
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class Ridley1AssetsJson(typing_extensions.TypedDict):
        wall_scrape_effect: int
        wall_scrape_sparks: int
        part_0xafa0d295: int
        wpsc_0xb93e46e5: int
        below_beam: json_util.JsonObject
        txtr: int
        unknown_0xab46a8c3: float
        part_0xc89c34fd: int
        in_hand_fire_breath_visor_effect: int
        above_missile: int
        wpsc_0x67dd641e: int
        above_fireball: int
        above_fireball_took_damage_effect: int
        tunnel_steam_effect: int
        tunnel_steam_texture: int
        sound_steam: int
        sound_fireball_took_damage: int
        caud_0x79169d11: int
        sound_mouth_beam: int
        caud_0xbd8e8710: int
        small_pain_sound_threshold: float
        sound_small_pain_sound: int
        large_pain_sound_threshold: float
        sound_large_pain_sound: int
        sound_beam_telegraph: int
        sound_initial_warning: int
        unknown_0xf1bf1c16: int
        unknown_0x0436327d: float
        unknown_0x772b6eb8: int
        unknown_0x154b5804: float
        unknown_0xbc77bd1d: int
        unknown_0xacb083ec: float
        unknown_0x0cd1f3cf: int
        unknown_0x5804032e: int
        unknown_0xa48bdf63: int
        unknown_0x1a058c4f: int
    

@dataclasses.dataclass()
class Ridley1Assets(BaseProperty):
    wall_scrape_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xccf0cc68, original_name='WallScrapeEffect'
        ),
    })
    wall_scrape_sparks: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9cf6186b, original_name='WallScrapeSparks'
        ),
    })
    part_0xafa0d295: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xafa0d295, original_name='PART'
        ),
    })
    wpsc_0xb93e46e5: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb93e46e5, original_name='WPSC'
        ),
    })
    below_beam: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x1aae3db5, original_name='BelowBeam', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    txtr: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbf4f8d8c, original_name='TXTR'
        ),
    })
    unknown_0xab46a8c3: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xab46a8c3, original_name='Unknown'
        ),
    })
    part_0xc89c34fd: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc89c34fd, original_name='PART'
        ),
    })
    in_hand_fire_breath_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb10f94c5, original_name='InHandFireBreathVisorEffect'
        ),
    })
    above_missile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0bd56e50, original_name='AboveMissile'
        ),
    })
    wpsc_0x67dd641e: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x67dd641e, original_name='WPSC'
        ),
    })
    above_fireball: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x51fb4542, original_name='AboveFireball'
        ),
    })
    above_fireball_took_damage_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xca7f8a50, original_name='AboveFireballTookDamageEffect'
        ),
    })
    tunnel_steam_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc34287e4, original_name='TunnelSteamEffect'
        ),
    })
    tunnel_steam_texture: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6f888688, original_name='TunnelSteamTexture'
        ),
    })
    sound_steam: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x84e9ccc8, original_name='Sound_Steam'
        ),
    })
    sound_fireball_took_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe13ab25f, original_name='Sound_FireballTookDamage'
        ),
    })
    caud_0x79169d11: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x79169d11, original_name='CAUD'
        ),
    })
    sound_mouth_beam: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5037fafb, original_name='Sound_MouthBeam'
        ),
    })
    caud_0xbd8e8710: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbd8e8710, original_name='CAUD'
        ),
    })
    small_pain_sound_threshold: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7802cbf0, original_name='SmallPainSoundThreshold'
        ),
    })
    sound_small_pain_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x491096be, original_name='Sound_SmallPainSound'
        ),
    })
    large_pain_sound_threshold: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdbf376a9, original_name='LargePainSoundThreshold'
        ),
    })
    sound_large_pain_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6d56bc5b, original_name='Sound_LargePainSound'
        ),
    })
    sound_beam_telegraph: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4d0bfc69, original_name='Sound_BeamTelegraph'
        ),
    })
    sound_initial_warning: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8813c561, original_name='Sound_InitialWarning'
        ),
    })
    unknown_0xf1bf1c16: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf1bf1c16, original_name='Unknown'
        ),
    })
    unknown_0x0436327d: float = dataclasses.field(default=500.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0436327d, original_name='Unknown'
        ),
    })
    unknown_0x772b6eb8: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x772b6eb8, original_name='Unknown'
        ),
    })
    unknown_0x154b5804: float = dataclasses.field(default=250.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x154b5804, original_name='Unknown'
        ),
    })
    unknown_0xbc77bd1d: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbc77bd1d, original_name='Unknown'
        ),
    })
    unknown_0xacb083ec: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xacb083ec, original_name='Unknown'
        ),
    })
    unknown_0x0cd1f3cf: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0cd1f3cf, original_name='Unknown'
        ),
    })
    unknown_0x5804032e: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5804032e, original_name='Unknown'
        ),
    })
    unknown_0xa48bdf63: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa48bdf63, original_name='Unknown'
        ),
    })
    unknown_0x1a058c4f: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1a058c4f, original_name='Unknown'
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
        if property_count != 36:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccf0cc68
        wall_scrape_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9cf6186b
        wall_scrape_sparks = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xafa0d295
        part_0xafa0d295 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb93e46e5
        wpsc_0xb93e46e5 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1aae3db5
        below_beam = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf4f8d8c
        txtr = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab46a8c3
        unknown_0xab46a8c3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc89c34fd
        part_0xc89c34fd = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb10f94c5
        in_hand_fire_breath_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0bd56e50
        above_missile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67dd641e
        wpsc_0x67dd641e = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51fb4542
        above_fireball = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca7f8a50
        above_fireball_took_damage_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc34287e4
        tunnel_steam_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6f888688
        tunnel_steam_texture = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84e9ccc8
        sound_steam = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe13ab25f
        sound_fireball_took_damage = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79169d11
        caud_0x79169d11 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5037fafb
        sound_mouth_beam = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd8e8710
        caud_0xbd8e8710 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7802cbf0
        small_pain_sound_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x491096be
        sound_small_pain_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdbf376a9
        large_pain_sound_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d56bc5b
        sound_large_pain_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d0bfc69
        sound_beam_telegraph = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8813c561
        sound_initial_warning = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1bf1c16
        unknown_0xf1bf1c16 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0436327d
        unknown_0x0436327d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x772b6eb8
        unknown_0x772b6eb8 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x154b5804
        unknown_0x154b5804 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc77bd1d
        unknown_0xbc77bd1d = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xacb083ec
        unknown_0xacb083ec = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0cd1f3cf
        unknown_0x0cd1f3cf = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5804032e
        unknown_0x5804032e = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa48bdf63
        unknown_0xa48bdf63 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a058c4f
        unknown_0x1a058c4f = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(wall_scrape_effect, wall_scrape_sparks, part_0xafa0d295, wpsc_0xb93e46e5, below_beam, txtr, unknown_0xab46a8c3, part_0xc89c34fd, in_hand_fire_breath_visor_effect, above_missile, wpsc_0x67dd641e, above_fireball, above_fireball_took_damage_effect, tunnel_steam_effect, tunnel_steam_texture, sound_steam, sound_fireball_took_damage, caud_0x79169d11, sound_mouth_beam, caud_0xbd8e8710, small_pain_sound_threshold, sound_small_pain_sound, large_pain_sound_threshold, sound_large_pain_sound, sound_beam_telegraph, sound_initial_warning, unknown_0xf1bf1c16, unknown_0x0436327d, unknown_0x772b6eb8, unknown_0x154b5804, unknown_0xbc77bd1d, unknown_0xacb083ec, unknown_0x0cd1f3cf, unknown_0x5804032e, unknown_0xa48bdf63, unknown_0x1a058c4f)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00$')  # 36 properties

        data.write(b'\xcc\xf0\xcch')  # 0xccf0cc68
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wall_scrape_effect))

        data.write(b'\x9c\xf6\x18k')  # 0x9cf6186b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wall_scrape_sparks))

        data.write(b'\xaf\xa0\xd2\x95')  # 0xafa0d295
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0xafa0d295))

        data.write(b'\xb9>F\xe5')  # 0xb93e46e5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wpsc_0xb93e46e5))

        data.write(b'\x1a\xae=\xb5')  # 0x1aae3db5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.below_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbfO\x8d\x8c')  # 0xbf4f8d8c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.txtr))

        data.write(b'\xabF\xa8\xc3')  # 0xab46a8c3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xab46a8c3))

        data.write(b'\xc8\x9c4\xfd')  # 0xc89c34fd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0xc89c34fd))

        data.write(b'\xb1\x0f\x94\xc5')  # 0xb10f94c5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.in_hand_fire_breath_visor_effect))

        data.write(b'\x0b\xd5nP')  # 0xbd56e50
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.above_missile))

        data.write(b'g\xddd\x1e')  # 0x67dd641e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wpsc_0x67dd641e))

        data.write(b'Q\xfbEB')  # 0x51fb4542
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.above_fireball))

        data.write(b'\xca\x7f\x8aP')  # 0xca7f8a50
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.above_fireball_took_damage_effect))

        data.write(b'\xc3B\x87\xe4')  # 0xc34287e4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.tunnel_steam_effect))

        data.write(b'o\x88\x86\x88')  # 0x6f888688
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.tunnel_steam_texture))

        data.write(b'\x84\xe9\xcc\xc8')  # 0x84e9ccc8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_steam))

        data.write(b'\xe1:\xb2_')  # 0xe13ab25f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_fireball_took_damage))

        data.write(b'y\x16\x9d\x11')  # 0x79169d11
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.caud_0x79169d11))

        data.write(b'P7\xfa\xfb')  # 0x5037fafb
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_mouth_beam))

        data.write(b'\xbd\x8e\x87\x10')  # 0xbd8e8710
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.caud_0xbd8e8710))

        data.write(b'x\x02\xcb\xf0')  # 0x7802cbf0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.small_pain_sound_threshold))

        data.write(b'I\x10\x96\xbe')  # 0x491096be
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_small_pain_sound))

        data.write(b'\xdb\xf3v\xa9')  # 0xdbf376a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.large_pain_sound_threshold))

        data.write(b'mV\xbc[')  # 0x6d56bc5b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_large_pain_sound))

        data.write(b'M\x0b\xfci')  # 0x4d0bfc69
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_beam_telegraph))

        data.write(b'\x88\x13\xc5a')  # 0x8813c561
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_initial_warning))

        data.write(b'\xf1\xbf\x1c\x16')  # 0xf1bf1c16
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xf1bf1c16))

        data.write(b'\x0462}')  # 0x436327d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0436327d))

        data.write(b'w+n\xb8')  # 0x772b6eb8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x772b6eb8))

        data.write(b'\x15KX\x04')  # 0x154b5804
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x154b5804))

        data.write(b'\xbcw\xbd\x1d')  # 0xbc77bd1d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xbc77bd1d))

        data.write(b'\xac\xb0\x83\xec')  # 0xacb083ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xacb083ec))

        data.write(b'\x0c\xd1\xf3\xcf')  # 0xcd1f3cf
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x0cd1f3cf))

        data.write(b'X\x04\x03.')  # 0x5804032e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x5804032e))

        data.write(b'\xa4\x8b\xdfc')  # 0xa48bdf63
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xa48bdf63))

        data.write(b'\x1a\x05\x8cO')  # 0x1a058c4f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x1a058c4f))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("Ridley1AssetsJson", data)
        return cls(
            wall_scrape_effect=json_data['wall_scrape_effect'],
            wall_scrape_sparks=json_data['wall_scrape_sparks'],
            part_0xafa0d295=json_data['part_0xafa0d295'],
            wpsc_0xb93e46e5=json_data['wpsc_0xb93e46e5'],
            below_beam=PlasmaBeamInfo.from_json(json_data['below_beam']),
            txtr=json_data['txtr'],
            unknown_0xab46a8c3=json_data['unknown_0xab46a8c3'],
            part_0xc89c34fd=json_data['part_0xc89c34fd'],
            in_hand_fire_breath_visor_effect=json_data['in_hand_fire_breath_visor_effect'],
            above_missile=json_data['above_missile'],
            wpsc_0x67dd641e=json_data['wpsc_0x67dd641e'],
            above_fireball=json_data['above_fireball'],
            above_fireball_took_damage_effect=json_data['above_fireball_took_damage_effect'],
            tunnel_steam_effect=json_data['tunnel_steam_effect'],
            tunnel_steam_texture=json_data['tunnel_steam_texture'],
            sound_steam=json_data['sound_steam'],
            sound_fireball_took_damage=json_data['sound_fireball_took_damage'],
            caud_0x79169d11=json_data['caud_0x79169d11'],
            sound_mouth_beam=json_data['sound_mouth_beam'],
            caud_0xbd8e8710=json_data['caud_0xbd8e8710'],
            small_pain_sound_threshold=json_data['small_pain_sound_threshold'],
            sound_small_pain_sound=json_data['sound_small_pain_sound'],
            large_pain_sound_threshold=json_data['large_pain_sound_threshold'],
            sound_large_pain_sound=json_data['sound_large_pain_sound'],
            sound_beam_telegraph=json_data['sound_beam_telegraph'],
            sound_initial_warning=json_data['sound_initial_warning'],
            unknown_0xf1bf1c16=json_data['unknown_0xf1bf1c16'],
            unknown_0x0436327d=json_data['unknown_0x0436327d'],
            unknown_0x772b6eb8=json_data['unknown_0x772b6eb8'],
            unknown_0x154b5804=json_data['unknown_0x154b5804'],
            unknown_0xbc77bd1d=json_data['unknown_0xbc77bd1d'],
            unknown_0xacb083ec=json_data['unknown_0xacb083ec'],
            unknown_0x0cd1f3cf=json_data['unknown_0x0cd1f3cf'],
            unknown_0x5804032e=json_data['unknown_0x5804032e'],
            unknown_0xa48bdf63=json_data['unknown_0xa48bdf63'],
            unknown_0x1a058c4f=json_data['unknown_0x1a058c4f'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'wall_scrape_effect': self.wall_scrape_effect,
            'wall_scrape_sparks': self.wall_scrape_sparks,
            'part_0xafa0d295': self.part_0xafa0d295,
            'wpsc_0xb93e46e5': self.wpsc_0xb93e46e5,
            'below_beam': self.below_beam.to_json(),
            'txtr': self.txtr,
            'unknown_0xab46a8c3': self.unknown_0xab46a8c3,
            'part_0xc89c34fd': self.part_0xc89c34fd,
            'in_hand_fire_breath_visor_effect': self.in_hand_fire_breath_visor_effect,
            'above_missile': self.above_missile,
            'wpsc_0x67dd641e': self.wpsc_0x67dd641e,
            'above_fireball': self.above_fireball,
            'above_fireball_took_damage_effect': self.above_fireball_took_damage_effect,
            'tunnel_steam_effect': self.tunnel_steam_effect,
            'tunnel_steam_texture': self.tunnel_steam_texture,
            'sound_steam': self.sound_steam,
            'sound_fireball_took_damage': self.sound_fireball_took_damage,
            'caud_0x79169d11': self.caud_0x79169d11,
            'sound_mouth_beam': self.sound_mouth_beam,
            'caud_0xbd8e8710': self.caud_0xbd8e8710,
            'small_pain_sound_threshold': self.small_pain_sound_threshold,
            'sound_small_pain_sound': self.sound_small_pain_sound,
            'large_pain_sound_threshold': self.large_pain_sound_threshold,
            'sound_large_pain_sound': self.sound_large_pain_sound,
            'sound_beam_telegraph': self.sound_beam_telegraph,
            'sound_initial_warning': self.sound_initial_warning,
            'unknown_0xf1bf1c16': self.unknown_0xf1bf1c16,
            'unknown_0x0436327d': self.unknown_0x0436327d,
            'unknown_0x772b6eb8': self.unknown_0x772b6eb8,
            'unknown_0x154b5804': self.unknown_0x154b5804,
            'unknown_0xbc77bd1d': self.unknown_0xbc77bd1d,
            'unknown_0xacb083ec': self.unknown_0xacb083ec,
            'unknown_0x0cd1f3cf': self.unknown_0x0cd1f3cf,
            'unknown_0x5804032e': self.unknown_0x5804032e,
            'unknown_0xa48bdf63': self.unknown_0xa48bdf63,
            'unknown_0x1a058c4f': self.unknown_0x1a058c4f,
        }

    def _dependencies_for_wall_scrape_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wall_scrape_effect)

    def _dependencies_for_wall_scrape_sparks(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wall_scrape_sparks)

    def _dependencies_for_part_0xafa0d295(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xafa0d295)

    def _dependencies_for_wpsc_0xb93e46e5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_0xb93e46e5)

    def _dependencies_for_txtr(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.txtr)

    def _dependencies_for_part_0xc89c34fd(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xc89c34fd)

    def _dependencies_for_in_hand_fire_breath_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.in_hand_fire_breath_visor_effect)

    def _dependencies_for_above_missile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.above_missile)

    def _dependencies_for_wpsc_0x67dd641e(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_0x67dd641e)

    def _dependencies_for_above_fireball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.above_fireball)

    def _dependencies_for_above_fireball_took_damage_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.above_fireball_took_damage_effect)

    def _dependencies_for_tunnel_steam_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tunnel_steam_effect)

    def _dependencies_for_tunnel_steam_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tunnel_steam_texture)

    def _dependencies_for_sound_steam(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_steam)

    def _dependencies_for_sound_fireball_took_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_fireball_took_damage)

    def _dependencies_for_caud_0x79169d11(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.caud_0x79169d11)

    def _dependencies_for_sound_mouth_beam(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_mouth_beam)

    def _dependencies_for_caud_0xbd8e8710(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.caud_0xbd8e8710)

    def _dependencies_for_sound_small_pain_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_small_pain_sound)

    def _dependencies_for_sound_large_pain_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_large_pain_sound)

    def _dependencies_for_sound_beam_telegraph(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_beam_telegraph)

    def _dependencies_for_sound_initial_warning(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_initial_warning)

    def _dependencies_for_unknown_0xf1bf1c16(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0xf1bf1c16)

    def _dependencies_for_unknown_0x772b6eb8(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x772b6eb8)

    def _dependencies_for_unknown_0xbc77bd1d(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0xbc77bd1d)

    def _dependencies_for_unknown_0x0cd1f3cf(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x0cd1f3cf)

    def _dependencies_for_unknown_0x5804032e(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x5804032e)

    def _dependencies_for_unknown_0xa48bdf63(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0xa48bdf63)

    def _dependencies_for_unknown_0x1a058c4f(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x1a058c4f)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_wall_scrape_effect, "wall_scrape_effect", "AssetId"),
            (self._dependencies_for_wall_scrape_sparks, "wall_scrape_sparks", "AssetId"),
            (self._dependencies_for_part_0xafa0d295, "part_0xafa0d295", "AssetId"),
            (self._dependencies_for_wpsc_0xb93e46e5, "wpsc_0xb93e46e5", "AssetId"),
            (self.below_beam.dependencies_for, "below_beam", "PlasmaBeamInfo"),
            (self._dependencies_for_txtr, "txtr", "AssetId"),
            (self._dependencies_for_part_0xc89c34fd, "part_0xc89c34fd", "AssetId"),
            (self._dependencies_for_in_hand_fire_breath_visor_effect, "in_hand_fire_breath_visor_effect", "AssetId"),
            (self._dependencies_for_above_missile, "above_missile", "AssetId"),
            (self._dependencies_for_wpsc_0x67dd641e, "wpsc_0x67dd641e", "AssetId"),
            (self._dependencies_for_above_fireball, "above_fireball", "AssetId"),
            (self._dependencies_for_above_fireball_took_damage_effect, "above_fireball_took_damage_effect", "AssetId"),
            (self._dependencies_for_tunnel_steam_effect, "tunnel_steam_effect", "AssetId"),
            (self._dependencies_for_tunnel_steam_texture, "tunnel_steam_texture", "AssetId"),
            (self._dependencies_for_sound_steam, "sound_steam", "AssetId"),
            (self._dependencies_for_sound_fireball_took_damage, "sound_fireball_took_damage", "AssetId"),
            (self._dependencies_for_caud_0x79169d11, "caud_0x79169d11", "AssetId"),
            (self._dependencies_for_sound_mouth_beam, "sound_mouth_beam", "AssetId"),
            (self._dependencies_for_caud_0xbd8e8710, "caud_0xbd8e8710", "AssetId"),
            (self._dependencies_for_sound_small_pain_sound, "sound_small_pain_sound", "AssetId"),
            (self._dependencies_for_sound_large_pain_sound, "sound_large_pain_sound", "AssetId"),
            (self._dependencies_for_sound_beam_telegraph, "sound_beam_telegraph", "AssetId"),
            (self._dependencies_for_sound_initial_warning, "sound_initial_warning", "AssetId"),
            (self._dependencies_for_unknown_0xf1bf1c16, "unknown_0xf1bf1c16", "AssetId"),
            (self._dependencies_for_unknown_0x772b6eb8, "unknown_0x772b6eb8", "AssetId"),
            (self._dependencies_for_unknown_0xbc77bd1d, "unknown_0xbc77bd1d", "AssetId"),
            (self._dependencies_for_unknown_0x0cd1f3cf, "unknown_0x0cd1f3cf", "AssetId"),
            (self._dependencies_for_unknown_0x5804032e, "unknown_0x5804032e", "AssetId"),
            (self._dependencies_for_unknown_0xa48bdf63, "unknown_0xa48bdf63", "AssetId"),
            (self._dependencies_for_unknown_0x1a058c4f, "unknown_0x1a058c4f", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Ridley1Assets.{field_name} ({field_type}): {e}"
                )


def _decode_below_beam(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xccf0cc68: ('wall_scrape_effect', structs.decode_BIG_Q),
    0x9cf6186b: ('wall_scrape_sparks', structs.decode_BIG_Q),
    0xafa0d295: ('part_0xafa0d295', structs.decode_BIG_Q),
    0xb93e46e5: ('wpsc_0xb93e46e5', structs.decode_BIG_Q),
    0x1aae3db5: ('below_beam', _decode_below_beam),
    0xbf4f8d8c: ('txtr', structs.decode_BIG_Q),
    0xab46a8c3: ('unknown_0xab46a8c3', structs.decode_BIG_f),
    0xc89c34fd: ('part_0xc89c34fd', structs.decode_BIG_Q),
    0xb10f94c5: ('in_hand_fire_breath_visor_effect', structs.decode_BIG_Q),
    0x0bd56e50: ('above_missile', structs.decode_BIG_Q),
    0x67dd641e: ('wpsc_0x67dd641e', structs.decode_BIG_Q),
    0x51fb4542: ('above_fireball', structs.decode_BIG_Q),
    0xca7f8a50: ('above_fireball_took_damage_effect', structs.decode_BIG_Q),
    0xc34287e4: ('tunnel_steam_effect', structs.decode_BIG_Q),
    0x6f888688: ('tunnel_steam_texture', structs.decode_BIG_Q),
    0x84e9ccc8: ('sound_steam', structs.decode_BIG_Q),
    0xe13ab25f: ('sound_fireball_took_damage', structs.decode_BIG_Q),
    0x79169d11: ('caud_0x79169d11', structs.decode_BIG_Q),
    0x5037fafb: ('sound_mouth_beam', structs.decode_BIG_Q),
    0xbd8e8710: ('caud_0xbd8e8710', structs.decode_BIG_Q),
    0x7802cbf0: ('small_pain_sound_threshold', structs.decode_BIG_f),
    0x491096be: ('sound_small_pain_sound', structs.decode_BIG_Q),
    0xdbf376a9: ('large_pain_sound_threshold', structs.decode_BIG_f),
    0x6d56bc5b: ('sound_large_pain_sound', structs.decode_BIG_Q),
    0x4d0bfc69: ('sound_beam_telegraph', structs.decode_BIG_Q),
    0x8813c561: ('sound_initial_warning', structs.decode_BIG_Q),
    0xf1bf1c16: ('unknown_0xf1bf1c16', structs.decode_BIG_Q),
    0x0436327d: ('unknown_0x0436327d', structs.decode_BIG_f),
    0x772b6eb8: ('unknown_0x772b6eb8', structs.decode_BIG_Q),
    0x154b5804: ('unknown_0x154b5804', structs.decode_BIG_f),
    0xbc77bd1d: ('unknown_0xbc77bd1d', structs.decode_BIG_Q),
    0xacb083ec: ('unknown_0xacb083ec', structs.decode_BIG_f),
    0x0cd1f3cf: ('unknown_0x0cd1f3cf', structs.decode_BIG_Q),
    0x5804032e: ('unknown_0x5804032e', structs.decode_BIG_Q),
    0xa48bdf63: ('unknown_0xa48bdf63', structs.decode_BIG_Q),
    0x1a058c4f: ('unknown_0x1a058c4f', structs.decode_BIG_Q),
}
