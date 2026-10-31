# Traversal/progression recipes retain their original catalog order and option gates. RDS
# changes the resource reader, not which later recipe wins on a shared target. Boundary
# names here: apply_worlds.
"""World progression and traversal edits in their original catalog order.

The order matters when multiple recipes touch the same object. RDS changes
how we read the resource; it does not change which recipe wins.
"""


def apply_worlds(options, statics, add_static):
    excluded = {'FrontEndPatches.patch_attract_videos', 'PickupPatches.add_special_pickup_patches'}
    conditional = {'NorionPatches.add_control_tower_norion_layer_change_patches': options.start != 'olympus',
                   'GeneralPatches.add_fast_flying_patches': options.fast_flying,
                   'GeneralPatches.add_phaaze_skip_patches': options.phaaze_skip,
                   'CosmeticPatches.add_random_door_color_patch': False,
                   'CosmeticPatches.add_context_welding_color_patch': False}
    for name in statics:
        if name not in excluded and conditional.get(name, True):
            add_static(name)
