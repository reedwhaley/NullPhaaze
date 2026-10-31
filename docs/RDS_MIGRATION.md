# RDS migration

The detailed network receipt/save flow and both cross-world model directions
are in [NETWORK_AND_MODELS.md](NETWORK_AND_MODELS.md), with comments at the
corresponding source decision points.

The behavior baseline is the accepted `.14r2` source from October 29. The older
RDS migration supplies the corrected readers and the schema field resolver. It
does not replace the later hint, respawn, map, model, tracker or runtime fixes.
All work here is isolated from the installed client and previous releases.

## Entry points

`nullphaze_core.engine.export` still accepts the eleven-file patcher interface.
The CLI and CDV exporter call the same backend. `planner.build_plan` composes the
seed settings and placements; `patches/` separates frontend, starting inventory,
world progression, pickups and cosmetics without changing recipe order.

RDS owns PAK directories, MREA section framing and compression, MLVL, SCLY,
STRG and NTWK. `rds_formats.py` keeps the compatibility exceptions together.
The archive interface remains lazy so an export does not load all game payloads
into memory. Duplicate directory entries and their original order stay intact.

## Property edits

`rds_scripts.decode_fields` observes the strict generated decoder to resolve a
property ID to a concrete field name, nested path and byte span. The evaluator
edits that span and decodes the result again. The export path no longer scans
arbitrary property bytes for matching four-byte IDs.

I keep the original object encoding. A complete typed rebuild can add absent
defaults or canonicalize nested data, which would expand the change beyond the
field we intended to edit. A matching header inside a string is not a field.
The decoy-header and absent-default tests cover that distinction.

The exact legacy CRLY and empty-PCKP sentinel values are allowed only while the
relevant decoder runs. Unexpected enum values still fail. Decoding is serialized
around that temporary override. Generated slow readers retain their framing
assertions; the field observer depends on the pinned generator implementation.

## Compatibility points

- The required dependency is the vendored
  `retro-data-structures==0.44.1+nullphaze.20261024`, including its generated RSOT
  readers. Stock `0.44.1` is rejected. The vendor notice records both source pins.
- The ordinary RDS script reader drops connections whose signal enum is unknown.
  Our adapter retains the raw FourCC through RDS's record constructs instead.
- MREA section padding is counted in both the data and section-size table.
  The historical addon alignment adapter remains in place.
- MLVL's unused flag bits remain source data. The adapter preserves them instead
  of filling them with a default. Only the verified FF alignment envelope is
  accepted after a world record.
- Generated STRGs keep every occurrence in forward order. The general RDS string
  writer deduplicates repeated strings; that previously crashed the native
  frontend loader. FF resource padding also stays compatible with the baseline.
- NTWK edits use its typed script properties. The legacy codec argument remains
  accepted by callers, but exports no longer load the separate codec DLL.
- Owned Corruption serializers pass `Game.CORRUPTION` explicitly. Layer
  controllers now use `master_layer` and the native UUID representation rather
  than the old four-integer layer-ID wrapper.
- Inherited OPR uses several old generated import and field names. Its adapters
  map names with the same property ID; they preserve the actual RDS classes.
  This compatibility does not assign new meanings to unknown fields.

## Existing bounded edits

Some established addons deliberately replace a guarded byte span instead of
rebuilding an entire resource. The Corruption FRME v14 envelope, DOL instruction
patches and the single MAPA visibility word are examples. Their existing source
guards and preservation checks remain. RDS migration does not turn those edits
into a claim that every Corruption format has a complete typed writer.

The Aurora fix still moves only `00070190` to the transform of `00070024`.
The remaining respawns, connections, inventory and flags stay intact. The full
map changes visibility without marking rooms visited. Native blocking receive,
CRC handling and the `.14r2` startup layout remain the runtime baseline.

## Acceptance and scope

The isolated phase root contains the option matrix, differential room audit,
complete export comparisons, regression XML and build/export receipts. The
`RDS Migration` tab in the existing feature tracker records these separately.

The spreadsheet's unfinished feature requests need their own requirements.
Migration preserves implemented behavior; it does not silently invent a Hidden
Court fix, choose a Hyper Ball statue, or redesign starting items.

A rebuild or resource comparison is structural evidence. Dolphin interaction,
save/reload, live multiworld delivery and physical Wii/vWii behavior remain
separate acceptance checks. No release or server deployment is implied.

## Build this source package

Use the standalone backend instructions in [README.md](../README.md). The private
RDS project is in `vendor/retro-data-structures`; install it before the backend.
The CDV-facing files live under `integrations/cdv/overlay/cdv`, with the same
module paths used above after the guarded overlay is applied to its recognized
`.14r2` checkout. Build native templates from that overlaid source before export.

The old standalone codec libraries are excluded. RDS supplies compression; WIT
remains the external image tool for the frontend's extract/patch/rebuild path.
Direct Wii ISO replacement is a separate project.

Original MIT notices remain with the core and generated source. The combined
RDS-backed package also carries its GPL requirements; see [NOTICE.md](../NOTICE.md)
and the preserved vendor licenses.
