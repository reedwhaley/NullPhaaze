# Apply seeded cosmetic recipes after progression and pickup recipes so their existing
# ordering stays deterministic. Cosmetic options must not select a different recipient or
# item grant. Boundary names here: apply_cosmetics.
"""Optional seeded cosmetics, applied after progression and pickup recipes."""

def apply_cosmetics(options, add_static):
    if options.random_door_colors:
        add_static('CosmeticPatches.add_random_door_color_patch')
    if options.random_welding_colors:
        add_static('CosmeticPatches.add_context_welding_color_patch')
