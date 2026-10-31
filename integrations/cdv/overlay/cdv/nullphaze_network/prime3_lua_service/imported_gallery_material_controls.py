# Bounded visual controls; not replacement production/gallery materials. Boundary names
# here: control_mesh.
"""Bounded visual controls; not replacement production/gallery materials."""

import copy

from construct import Container, ListContainer

NAMES = (
    "V3 MATERIAL",
    "CURRENT",
    "BNIF 32",
    "NATIVE BLACK",
    "NATIVE GREY",
    "BLOOM FLAG",
    "OPAQUE INCA",
    "OPAQUE MIX",
    "ALPHA CLR",
    "MASKED CLR",
    "SOLID WHITE",
    "FULL V3",
)


def control_mesh(current, previous, variant):
    if not 0 <= variant < len(NAMES):
        raise ValueError("Unknown material control")
    mesh = copy.deepcopy(previous if variant == 11 else current)
    if variant == 0:
        mesh.material_sets = copy.deepcopy(previous.material_sets)
    if variant in (0, 1, 11):
        return mesh
    for mat in mesh.material_sets[0].materials:
        emission = copy.deepcopy(next(e for e in mat.elements if e.type == "PASS"))
        emission.body.flags = 4 if variant == 5 else 0
        constants = [e for e in mat.elements if e.type not in ("PASS", "END ")]
        for element in constants:
            if element.type == "INT " and element.body.subtype == "BNIF":
                element.body.value = 32
            if element.type == "CLR " and element.body.subtype == "CLR ":
                if variant != 2:
                    element.body.value = 0x666666FF if variant == 4 else 255
        passes = [emission]
        if variant == 6:
            mat.flags = 0x81
        if variant in (7, 8, 9):
            color = copy.deepcopy(emission)
            color.body.subtype, color.body.flags = "CLR ", 0
            passes = [color, emission] if variant == 7 else [color]
            mat.flags = {7: 0x81, 8: 0x89, 9: 0x91}[variant]
            if variant in (8, 9):
                opacity = copy.deepcopy(color)
                opacity.body.subtype, opacity.body.flags = "TRAN", 3
                passes.append(opacity)
        if variant == 10:
            mat.flags, passes = 0x281, []
            for element in constants:
                if element.type == "CLR ":
                    element.body.value = 0xFFFFFFFF
            constants.append(Container(type="INT ", body=Container(subtype="OPAC", value=255)))
        mat.elements = ListContainer(constants + passes + [Container(type="END ", body=None)])
    return mesh
