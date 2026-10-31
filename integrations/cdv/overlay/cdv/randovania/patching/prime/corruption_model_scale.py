# Preserve the seed's native pickup footprint when substituting Corruption models. Boundary
# names here: presentation_multiplier, dimensions, match_scale, prime_dimensions,
# echoes_dimensions.
"""Preserve the seed's native pickup footprint when substituting Corruption models."""

from __future__ import annotations

import copy
import math
import struct

from retro_data_structures.game_check import Game

from randovania.patching.prime.prime_pickup_dimensions import PRIME_PICKUP_DIMENSIONS


def presentation_multiplier(model_name, game=Game.PRIME):
    """Apply reviewed visual adjustments after matching the seed footprint."""
    if model_name in {"prime3_Hyper Ball", "prime3_Hyper Missile", "prime3_Hyper Grapple"}:
        return 1.075 * (1.05 if game == Game.ECHOES else 1.0)
    if model_name == "prime3_Ship Missile Expansion":
        # The reviewed 0.925 adjustment belongs to the expansion's visual, not
        # the main launcher or whichever grant a required-item rule selects.
        return 0.925
    return 1.0


def dimensions(payload, scale):
    """Read native CMDL bounds without decoding texture or display-list data."""
    if len(payload) < 36 or payload[:4] != bytes.fromhex("DEADBABE"):
        raise ValueError("Missing native CMDL bounds for pickup sizing")
    bounds = struct.unpack_from(">6f", payload, 12)
    if len(scale) != 3 or any(not math.isfinite(v) for v in (*bounds, *scale)):
        raise ValueError("Invalid pickup bounds or scale")
    result = tuple((bounds[i + 3] - bounds[i]) * abs(scale[i]) for i in range(3))
    if any(v < 0 for v in result) or max(result) <= 0:
        raise ValueError("Empty or inverted pickup bounds")
    return result


def match_scale(source, reference, modifier=(1.0, 1.0, 1.0)):
    """Match the largest rendered dimension while preserving proportions and seed modifiers."""
    for vector in (source, reference, modifier):
        if len(vector) != 3 or any(not math.isfinite(v) for v in vector):
            raise ValueError("Invalid pickup sizing vector")
    if any(v < 0 for v in (*source, *reference)) or min(max(source), max(reference)) <= 0:
        raise ValueError("Empty or inverted pickup sizing vector")
    current = max(abs(v * s) for v, s in zip(source, modifier))
    # Match the largest rendered dimension using the same seed modifier on
    # both bounds. Preserve proportions and signed per-axis scale; replacing
    # the transform with a single guessed constant loses the seed's sizing.
    target = max(abs(v * s) for v, s in zip(reference, modifier))
    if current == target == 0:
        return list(modifier)
    if min(current, target) <= 0:
        raise ValueError("Degenerate pickup sizing modifier")
    return [s * target / current for s in modifier]


def prime_dimensions(metadata, directory):
    result = dict(PRIME_PICKUP_DIMENSIONS)
    for name, item in metadata["items"].items():
        if name.startswith("prime3_"):
            payload = (directory / f"{item['cmdl']}.CMDL").read_bytes()
            result[name] = dimensions(payload, [item["scale"]] * 3)
    for alias, name in (("Scan Visor", "Visor"), ("Power Suit", "Gamecube"), ("Power Beam", "Gamecube")):
        result[alias] = result[name]
    return result


def echoes_dimensions(patch_data, randomizer_data, manager):
    """Measure only the models used by this seed, including native custom assets."""
    from open_prime_rando.echoes import custom_assets

    entries = {entry["Name"]: entry for entry in randomizer_data["ModelData"]}
    needed = set()
    for pickup in patch_data["pickups"]:
        original = pickup["original_model"]
        name = f"{original['game']}_{original['name']}"
        if name.startswith("prime3_") and name in entries:
            needed.update((name, pickup["model"]["name"]))
    # These Claris/OPR models change textures only, retaining their source bounds.
    # Resolve them before Claris installs the derived resources into the target.
    aliases = {
        translator.new_cmdl: custom_assets.SCAN_VISOR_CMDL
        for translator in (
            custom_assets.VIOLET_TRANSLATOR,
            custom_assets.AMBER_TRANSLATOR,
            custom_assets.EMERALD_TRANSLATOR,
            custom_assets.COBALT_TRANSLATOR,
        )
    }
    aliases.update(
        {
            ammo.new_cmdl: custom_assets.BEAM_AMMO_EXPANSION_CMDL
            for ammo in (custom_assets.DARK_AMMO, custom_assets.LIGHT_AMMO)
        }
    )
    result = {}
    for name in sorted(needed):
        entry = entries[name]
        identity = aliases.get(entry["Model"], entry["Model"])
        result[name] = dimensions(manager.get_raw_asset(identity).data, entry["Scale"])
    return result


def sized_echoes_index(randomizer_data, source, reference, model_dimensions):
    name = f"{source}__sized_{reference}"
    models = randomizer_data["ModelData"]
    existing = next((entry for entry in models if entry["Name"] == name), None)
    if existing is not None:
        return existing["Index"]
    original = next(entry for entry in models if entry["Name"] == source)
    variant = copy.deepcopy(original)
    variant["Name"] = name
    variant["Index"] = max(entry["Index"] for entry in models) + 1
    modifier = match_scale(model_dimensions[source], model_dimensions[reference])
    variant["Scale"] = [
        a * b * presentation_multiplier(source, Game.ECHOES) for a, b in zip(original["Scale"], modifier)
    ]
    models.append(variant)
    return variant["Index"]
