# Asset-only pickup effect approximations using the GC particle interpreters. Boundary names
# here: suppress_hypermode_default_billboard, color_channels, lower_native_color,
# translate_native_colors, translate_native_blends.
"""Asset-only pickup effect approximations using the GC particle interpreters.

Unsupported Wii operations are recorded per resource. No renderer/game code is patched.
"""

from __future__ import annotations

import contextlib
import copy
import hashlib
import io

from construct import Container, ListContainer
from retro_data_structures.conversion import part
from retro_data_structures.formats import effect_script as effects
from retro_data_structures.formats.txtr import Txtr
from retro_data_structures.game_check import Game

from randovania.patching.prime.corruption_particle_curves import lower_counter_curves
from randovania.patching.prime.corruption_static_mesh import allocate, convert_mesh, native_templates
from randovania.patching.prime.corruption_texture import atlas_frame

# Retail Prime's CreateWPSM dispatcher. The shared RDS schema also accepts
# fields from newer games, which can make the native loader stop mid-resource.
NATIVE_SWOOSH_FIELDS = frozenset(
    "PSLT TIME LRAD RRAD LLRD LENG COLR SIDE CROS SROT IROT ROTM POFS IVEL NPOS "
    "VELM VLM2 VLS1 VLS2 SPLN WIRE TEXR TSPN AALP ZBUF ORNT TEXW CRND _END".split()
)
# RDS accepting an element only proves schema coverage. The target game's
# interpreter still determines which operations execute. Keep omissions and
# approximations in the conversion report rather than claiming shader parity.
HYPERMODE_MODEL_QUADS = 0xBBC2AACA19834306
HYPER_CAPSULE_MODEL = 0x575AFCBCDEF5AC35


def suppress_hypermode_default_billboard(result, identity):
    """Retain the source PMUS quads without an additional native default sprite."""
    if identity != HYPERMODE_MODEL_QUADS:
        return []
    fields = {element.type: element.body for element in result.elements}
    model_quads = fields.get("PMUS")
    if (
        "SIZE" in fields
        or "COLR" in fields
        or "PMSC" not in fields
        or "PMCL" not in fields
        or model_quads is None
        or model_quads.magic != "CNST"
        or not model_quads.value
    ):
        raise ValueError("Hypermode model-quad source layout differs from the audited resource")
    # Retail Prime RenderParticles returns early for a constant SIZE of zero,
    # while RenderModels still renders PMUS using PMSC/PMCL and native PMAB.
    result.elements.insert(-1, Container(type="SIZE", body=Container(type="CNST", body=0.0)))
    return ["PMUS: suppress duplicate default billboard; retain textured model quads and their color/scale"]


def color_channels(expression):
    """Lower color arithmetic to four native scalar graphs without discarding factors."""
    kind, body = expression.type, expression.body
    if kind == "CNST":
        return [copy.deepcopy(body[axis]) for axis in "abcd"]
    if kind in ("KEYE", "KEYP"):
        result = []
        for channel in range(4):
            scalar = copy.deepcopy(expression)
            scalar.body["keys"] = ListContainer(key[channel] for key in body["keys"])
            result.append(scalar)
        return result
    if kind == "VRTC" and body.a.type == "CNST":
        return [copy.deepcopy(body.a.body[axis]) for axis in "abc"] + [copy.deepcopy(body.b)]
    if kind == "MULT":
        return [
            Container(type="MULT", body=Container(a=a, b=b))
            for a, b in zip(color_channels(body.a), color_channels(body.b))
        ]
    raise ValueError("Color expression cannot be lowered exactly: " + kind)


def lower_native_color(element):
    # RDS's generic downgrade can discard the second MULT operand. Preserve
    # RGB parameters AND the independent alpha/lifetime curve in native CNST.
    if element.type != "COLR" or element.body.type not in ("MULT", "VRTC"):
        return False
    try:
        channels = color_channels(element.body)
    except ValueError:
        return False
    element.body = Container(type="CNST", body=Container(dict(zip("abcd", channels))))
    return True


def translate_native_colors(result, game):
    if game != Game.PRIME:
        return []
    _, count = lower_counter_curves(result)
    notes = ["KEYF: exact native cumulative-count lookup with source loop-seam behavior"] if count else []
    return notes + [
        "COLR: preserve vector RGB and color multiplication as scalar RGBA graphs"
        for element in result.elements
        if lower_native_color(element)
    ]


def translate_native_blends(result):
    """Map the source RGB blend factors to the native particle/model blend flags.

    Corruption's retail blend dispatcher at 0x803A5A3C distinguishes alpha,
    additive, premultiplied and destination-alpha variants. Destination-alpha
    overrides affect Wii postprocessing; the GC approximation preserves RGB.
    """
    translated, approximated = [], []
    replacements = {}
    for element in result.elements:
        if element.type == "MBDM" and element.body.type == "CNST" and element.body.body in (0, 1):
            mode = element.body.body
            replacements["PMAB"] = mode == 1
            translated.append(f"MBDM {mode}: native {'additive' if mode else 'alpha/opaque'} model RGB blending")
        if element.type == "PBDM" and element.body.type == "CNST":
            mode = element.body.body
            if mode in (0, 1, 3, 4, 6, 9):
                replacements["AAPH"] = mode in (1, 3, 4, 6)
                translated.append(f"PBDM {mode}: native {'additive' if replacements['AAPH'] else 'alpha'} RGB blending")
                if mode == 3:
                    approximated.append("PBDM 3: native source-alpha additive approximates source one/one blending")
                if mode in (4, 6, 9):
                    approximated.append(f"PBDM {mode}: Wii destination-alpha override omitted")
    if replacements:
        consumed = {"PBDM" if key == "AAPH" else "MBDM" for key in replacements}
        result.elements = ListContainer(e for e in result.elements if e.type not in (*consumed, *replacements))
        result.elements[-1:-1] = [
            Container(type=name, body=Container(magic="CNST", value=value)) for name, value in replacements.items()
        ]
    return translated, approximated


def native_elements(kind, elements, omitted):
    for element in elements:
        if kind == "SWHC" and element.type not in NATIVE_SWOOSH_FIELDS:
            omitted.append(element.type)
        else:
            yield element


def approximate_particle_capacity(element, kind, game, approximated):
    if (
        game == Game.PRIME
        and kind == "PART"
        and element.type == "MAXP"
        and element.body.type == "CNST"
        and element.body.body > 256
    ):
        element.body.body = 256
        approximated.append("MAXP: capped at Prime's 256-particle initial allocation")


class ParticleConverter:
    def __init__(self, source, target_game, occupied, existing=None):
        self.source = source
        self.target_game = target_game
        self.occupied = occupied
        self.mapping = dict(existing or {})
        self.resources = {}
        self.approximations = {}
        self.texture_variants = {}

    def convert_id(self, identity, source_game=Game.CORRUPTION):
        snapshot = (
            dict(self.mapping),
            dict(self.resources),
            set(self.occupied),
            dict(self.approximations),
            dict(self.texture_variants),
        )
        try:
            return self._convert_id(identity, source_game)
        except Exception as error:
            mapping, resources, occupied, approximations, variants = snapshot
            self.mapping, self.resources, self.approximations = mapping, resources, approximations
            self.texture_variants = variants
            self.occupied.clear()
            self.occupied.update(occupied)
            raise ValueError(f"Particle dependency {identity:016X}: {error}") from error

    def convert_texture(self, element, approximated, translated):
        if element.body.body is None:
            return
        texture = element.body.body
        if element.body.type != "TEXP":
            texture.id = self.convert_id(texture.id)
            return
        if texture.a.type != "CNST" or texture.b.type != "CNST":
            raise ValueError("Dynamic texture atlas tile size is unsupported")
        if texture.c.type in ("CNST", "PAP1"):
            # A constant TEXP phase selects one atlas cell, not a timed loop.
            original = texture.id
            self.convert_id(original)  # Retain source provenance and hash validation.
            phase = texture.c.body if texture.c.type == "CNST" else 0.5
            payload, index = atlas_frame(
                self.source.get_raw_asset(original).data, texture.a.body, texture.b.body, phase
            )
            key = (original, texture.a.body, texture.b.body, index)
            if key not in self.texture_variants:
                identity = int.from_bytes(hashlib.sha256(repr(key).encode()).digest()[:8], "big")
                new_id = allocate("TXTR", identity, self.target_game, self.occupied)
                self.resources[new_id] = ("TXTR", payload)
                self.texture_variants[key] = new_id
            element.body = Container(type="CNST", body=Container(sub_id="CNST", id=self.texture_variants[key]))
            if texture.c.type == "CNST":
                translated.append(f"TEXP: preserve constant phase as atlas frame {index}, including source mip texels")
            else:
                approximated.append(
                    f"TEXP: per-particle random sprite selection sampled at frame {index}; no invented timed cycle"
                )
            return
        element.body.type = "ATEX"
        element.body.body = Container(
            sub_id=texture.sub_id,
            id=self.convert_id(texture.id),
            extra=Container(
                a=copy.deepcopy(texture.a),
                b=copy.deepcopy(texture.b),
                c=copy.deepcopy(texture.a),
                d=copy.deepcopy(texture.b),
                e=Container(type="CNST", body=60),
                f=Container(magic="CNST", value=True),
            ),
        )
        approximated.append("TEXP: unsupported dynamic phase approximated by native ATEX one-second loop")

    def _convert_id(self, identity, source_game):
        if identity is None or not source_game.is_valid_asset_id(identity):
            return self.target_game.invalid_asset_id
        if identity in self.mapping:
            return self.mapping[identity]
        raw = self.source.get_raw_asset(identity)
        new = allocate(raw.type, identity, self.target_game, self.occupied)
        self.mapping[identity] = new
        try:
            if raw.type == "TXTR":
                Txtr.parse(raw.data, Game.CORRUPTION)
                Txtr.parse(raw.data, self.target_game)
                self.resources[new] = (raw.type, raw.data)
                return new
            if raw.type == "CMDL":
                mesh = self.source.get_parsed_asset(identity).raw
                textures = {e.body.id for m in mesh.material_sets[0].materials for e in m.elements if e.type == "PASS"}
                texture_map = {t: self.convert_id(t) for t in textures}
                data = convert_mesh(
                    mesh,
                    native_templates(),
                    self.target_game,
                    texture_map,
                    "catalog",
                    animated_uv=identity == HYPER_CAPSULE_MODEL,
                )
                if identity == HYPER_CAPSULE_MODEL:
                    self.approximations[f"{identity:016X}"] = {
                        "type": "CMDL",
                        "omitted_operations": [],
                        "approximated_operations": [],
                        "translated_operations": ["PMDL: retain native-compatible capsule reflection and UV scrolling"],
                    }
                self.resources[new] = ("CMDL", data)
                return new
            definitions = {
                "PART": ("GPSM", effects.PARTICLE_TYPES, effects.Part),
                "ELSC": ("ELSM", effects.ELECTRIC_TYPES, effects.Elsc),
                "SWHC": ("SWSH", effects.SWOOSH_TYPES, effects.Swhc),
            }
            if raw.type not in definitions:
                raise ValueError("Unsupported pickup effect dependency: " + raw.type)
            magic, types, effect_class = definitions[raw.type]
            source_types = dict(types)
            if raw.type == "ELSC":
                source_types["BLDM"] = effects.GetIntElement
            if raw.type == "SWHC":
                for key in ("XROT", "YROT", "ZROT"):
                    source_types[key] = effects.GetRealElement
                source_types["SBDM"] = effects.GetIntElement
            source_codec = effects.effect_script(magic, source_types)
            stream = io.BytesIO(raw.data)
            diagnostics = io.StringIO()
            try:
                with contextlib.redirect_stdout(diagnostics):
                    parsed = source_codec.parse_stream(stream, target_game=Game.CORRUPTION)
            except Exception as error:
                raise ValueError("Unsupported particle expression: " + diagnostics.getvalue()[-300:]) from error
            if any(v not in (0, 255) for v in stream.read()):
                raise ValueError("Unparsed particle payload")
            result = copy.deepcopy(parsed)
            quad_notes = suppress_hypermode_default_billboard(result, identity) if raw.type == "PART" else []
            translated = translate_native_colors(result, self.target_game)
            translated.extend(quad_notes)
            blends, blend_approximations = translate_native_blends(result) if raw.type == "PART" else ([], [])
            translated.extend(blends)
            if raw.type == "PART":
                result = part.downgrade(result, self, Game.CORRUPTION)
            retained = ListContainer()
            omitted = []
            approximated = blend_approximations
            for element in native_elements(raw.type, result.elements, omitted):
                approximate_particle_capacity(element, raw.type, self.target_game, approximated)
                if element.type in effect_class.texture_keys():
                    self.convert_texture(element, approximated, translated)
                # Test each expression against the actual destination grammar;
                # no unknown byte streams or 64-bit IDs reach the GC interpreter.
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        effects.FourCCSwitch(types).build(element, target_game=self.target_game)
                except Exception:
                    # 64-bit references are remapped below before the final check.
                    if element.type not in (
                        *effect_class.texture_keys(),
                        *effect_class.asset_id_keys(),
                        *effect_class.spawn_system_keys(),
                    ):
                        omitted.append(element.type)
                        continue
                if element.type in effect_class.asset_id_keys() and element.body.body is not None:
                    element.body.body = self.convert_id(element.body.body)
                elif element.type in effect_class.spawn_system_keys() and element.body.magic != "NONE":
                    for spawn in element.body.value.spawns:
                        for child in spawn.v2:
                            child.id = self.convert_id(child.id)
                            if self.target_game == Game.PRIME:
                                child.type = 0
                retained.append(element)
            result.elements = retained
            codec = effects.effect_script(magic, types)
            data = codec.build(result, target_game=self.target_game)
            checked = codec.parse(data, target_game=self.target_game)
            if codec.build(checked, target_game=self.target_game) != data:
                raise ValueError("Particle serialization differs")
            self.resources[new] = (raw.type, data)
            self.approximations[f"{identity:016X}"] = {
                "type": raw.type,
                "omitted_operations": omitted,
                "approximated_operations": approximated,
                "translated_operations": translated,
                "note": ("Closest GC subset; translated blends and remaining render approximations recorded above"),
            }
            return new
        except Exception:
            self.mapping.pop(identity, None)
            raise
