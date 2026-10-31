# Isolated gallery rendering experiment selected by the M06 live control. Boundary names
# here: opaque_emission_mesh.
"""Isolated gallery rendering experiment selected by the M06 live control."""

import copy


def opaque_emission_mesh(source):
    """Change only additive, emission-only materials; retain their own assets."""
    mesh = copy.deepcopy(source)
    changed = []
    for set_index, material_set in enumerate(mesh.material_sets):
        for index, material in enumerate(material_set.materials):
            passes = [e for e in material.elements if e.type == "PASS"]
            if not (material.flags & 0x20) or not passes:
                continue
            if any(e.body.subtype != "INCA" for e in passes):
                continue
            material.flags &= ~0x38
            for element in material.elements:
                if element.type == "INT " and element.body.subtype == "BNIF":
                    element.body.value = 32
                elif element.type == "CLR " and element.body.subtype == "CLR ":
                    element.body.value = 255
            changed.append([set_index, index])
    return mesh, changed
