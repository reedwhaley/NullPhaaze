# Corruption Multiworld Models

For the source-level lookup chain, receipt/grant separation, fallback rules and
Corruption-to-GC conversion path, see
[Network delivery and cross-world models](../../../docs/NETWORK_AND_MODELS.md).

The exporter derives its visual plan from each serialized pickup's
`PickupModel.game` and `PickupModel.name`, not item display names or recipients.
The post-core stage replaces audited PCKP/ACTR/PLAT model fields, including
fake-pickup aliases in other areas, and adds the native rig, particle and texture
dependencies to the archive and correct script layer. Full archive readback and
field-exact script comparisons are required. Grants, callbacks, transforms, scan
data, and acquisition text are not changed by this stage.

Scripted rewards with no core model slot retain their acquisition sequence and
are listed in `scripted_rewards_without_model_slots`. No new collectible actor
is fabricated for cutscenes or fixed interaction sequences.

## Local Assets

No game assets are distributed in the source package. The dialog uses
`internal_copies/prime3/imported_models` in the user's configured CDV data
directory. The cache contains the 93 accepted model forms, including source
catalog variants/placeholders. Unknown models, missing assets and changed hashes
fail export rather than silently substituting Scan Visor.

Install user-owned accepted assets into a new local cache:

```powershell
python -m nullphaze_network.prime3_lua_service.multiworld_models --accepted-gallery <gallery-directory> --converted-assets <converted-assets-directory> --output <data-directory>/internal_copies/prime3/imported_models
```

The installer checks the accepted image hash and matches every asset against
the accepted PAK. It refuses an existing destination and does not silently
regenerate assets from arbitrary ISO revisions. The cache's renderer recipe
retains the M06 opaque emission-only materials and model-matched effect scale.
The independent particle-size clamp must not be restored.

## Runtime Boundary

This stage does not enable general multiworld runtime publication: the separate
export guard remains intact. Private runtime builds can pass `--model-cache`
to run this same model stage before service-area patching. Native-only exports
do not require imported assets. Hardware and seeded gameplay acceptance remain
separate from the accepted 93-model Dolphin gallery.
