# These measured native model bounds provide the reference footprint for imported visuals.
# Keep the model-name keys paired with their dimensions rather than substituting a cache-
# wide guessed scale.
"""Native Prime pickup sizes for preserving the seed replacement footprint.

Numeric extents only; no geometry or textures. Measured from native actors
exported by randomprime 1.33.2 on the supported US 1.00 disc.
Validation: tools/corruption_model_export/audit_pickup_sizes.py.
"""

PRIME_PICKUP_DIMENSIONS = {
    "Artifact of Chozo": (2.47496544, 0.24979955, 2.94472713),
    "Artifact of Elder": (2.59886464, 0.26230476, 3.09214306),
    "Artifact of Lifegiver": (2.47496544, 0.24979955, 2.94472713),
    "Artifact of Nature": (2.44474593, 0.24674948, 2.9087718),
    "Artifact of Newborn": (1.81316142, 0.18300333, 2.15730916),
    "Artifact of Spirit": (2.56864532, 0.25925471, 3.05618795),
    "Artifact of Strength": (1.44750724, 0.14609766, 1.72225186),
    "Artifact of Sun": (2.32386862, 0.23454927, 2.76495133),
    "Artifact of Truth": (2.4175485, 0.24400443, 2.87641215),
    "Artifact of Warrior": (3.02193558, 0.30500554, 3.59551513),
    "Artifact of Wild": (2.4175485, 0.24400443, 2.87641215),
    "Artifact of World": (2.11233315, 0.21319889, 2.51326529),
    "Boost Ball": (1.04019201, 1.01116699, 1.01116598),
    "Charge Beam": (0.77020198, 0.23141, 0.76541996),
    "Cog": (0.77503717, 1.95184354, 1.95184354),
    "Combat Visor": (1.25192706, 1.25192706, 1.68772508),
    "Energy Tank": (1.3372636, 0.70824307, 0.74469005),
    "Flamethrower": (0.82933408, 0.30814928, 1.69025755),
    "FlamethrowerOld": (0.82933408, 0.30814928, 1.69025755),
    "Gamecube": (1.00334907, 1.24878266, 1.12446023),
    "Grapple Beam": (0.6461556, 1.28583716, 1.42729075),
    "Gravity Suit": (1.25981575, 0.48696476, 1.33746034),
    "Ice Beam": (0.7686082, 0.73099004, 1.44224916),
    "Ice Spreader": (0.82933408, 0.30814928, 1.69025755),
    "Ice Trap": (1.33732252, 2.35077128, 1.04255877),
    "Missile": (0.7472637, 0.74726379, 1.27595103),
    "Morph Ball": (1.66430724, 1.61786721, 1.61786559),
    "Morph Ball Bomb": (0.67421818, 0.65798169, 0.67421818),
    "Nothing": (1.44424224, 1.40884501, 1.40562505),
    "Phazon Suit": (1.51093902, 0.58403307, 1.60406077),
    "Plasma Beam": (0.7686082, 0.73099004, 1.44224916),
    "Power Bomb": (1.74063403, 1.74063403, 1.74063403),
    "Power Bomb Expansion": (1.30849504, 1.04774994, 1.04775),
    "Shiny Missile": (0.7472637, 0.74726379, 1.27595103),
    "Space Jump Boots": (0.83461797, 0.83461797, 1.12514997),
    "Spider Ball": (0.9993853, 1.01858383, 1.01858366),
    "Super Missile": (0.82933408, 0.30814928, 1.69025755),
    "Thermal Visor": (1.25192706, 1.25192706, 1.68772508),
    "Varia Suit": (1.25981575, 0.48696476, 1.33746034),
    "Visor": (1.25192706, 1.25192706, 1.68772508),
    "Wave Beam": (0.76860878, 0.73099039, 1.44224938),
    "Wavebuster": (0.82933399, 0.30815001, 1.690256),
    "X-Ray Visor": (1.25192706, 1.25192706, 1.68772508),
    "Zoomer": (1.5550665, 1.69912513, 1.05416738),
}
