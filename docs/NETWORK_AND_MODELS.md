# Network delivery and cross-world models

I keep the pickup's grant, receipt, notification and model paths separate because
each has different state and acceptance requirements. The comments explain the
decisions where they happen; this note connects the calls across files.

The `randovania/` and `nullphaze_network/` paths below are supplied in the guarded
`integrations/cdv/overlay/cdv/` tree. They run with the separately supplied CDV
checkout after the overlay is applied. The backend in `src/nullphaze_core/` builds
and patches extracted files independently of that frontend.

## Incoming items and the loaded save

`randovania/game_connection/connector/prime3_multiworld_connector.py` receives
the server's ordered pickup history. `manifest.remote_pickup_key()` checks each
canonical pickup against the exported incoming recipes. With `sender-v1`, the
sender name participates in the key too. Two players sending the same item can
need different acquisition text. A post-export world-name change therefore
requires a matching re-export rather than a guessed sender substitution.

`DeliveryLedger.accept_incoming()` persists the ordered queue before anything
can be granted. The file is bound to world UUID, seed fingerprint and save slot.
The replacement is flushed and fsynced before `os.replace`; a failed write
restores the previous in-memory ledger. I need the same sequence-to-recipe
mapping after a client restart that the game's receipt already refers to.

`Prime3MultiworldClient` uses the existing CP3W UDP endpoint, normally port
43674. Telemetry and delivery share one negotiated session and one endpoint
owner. The request lock keeps requests from interleaving; the snapshot token
keeps both inventory pages tied to one frozen sample. HELLO negotiation alone
does not identify the save. STATUS checks the exported world/seed/slot again.

The client constructs a packet once per exchange. Timeout retries keep its
request ID and payload. Replies are checked for framing, length and CRC before
stale IDs are discarded. A lost reply leaves the grant result uncertain; the
next connector update reads STATUS and reconciles the receipt before choosing
another item. Malformed packets, rejected identities and conflicting histories
remain errors. The CRC detects corruption; it is not a secret authentication key.

`seed_compiler.seed_tables()` converts the exported canonical pickups into the
bounded native recipe allowlist. DELIVER carries a recipe key, sequence,
previous history, generation and exported identity. It does not carry arbitrary
memory addresses or a model to load. `multiworld_service.c` validates that
request and queues one recipe for the current game owner.

`receipt_delivery_tick()` runs the queued grant through the owning Lua/game
callback. It reads a stable receipt, reconstructs logical inventory, plans the
authorized gains and calls the retail capacity/amount helpers. It checks the
result before replacing the owner's receipt. If a check fails after a retail
mutator ran, the delivery path faults; it does not promise to undo the inventory
change. Continuing after that fault could make the receipt disagree with RAM.

The receipt history is
`SHA256(previous_history || sequence_BE32 || recipe_key)` in both Python and C.
An equal sequence number with a different history is a conflict. A duplicate
of the last applied delivery must reproduce the committed history and cannot
reach `apply()` again. The current implementation bounds incoming sequences
at 256; documenting that limit does not extend it.

## Applied, saved and uploaded mean different things

`cursor` describes items applied to the live owner. `saved_cursor` comes from
the validated disk receipt in `receipt_coupling.c`. A queued response, successful
DELIVER exchange, HUD notice or save submission does not establish persistence.

The coupling hooks bind receipt views to hashes of the actual native checkpoint
vectors and serialized slots. Before writing the private save container,
`coupling_prepare_save()` requires each present slot's bytes to match its stored
receipt view. A validated container read refreshes the disk anchors. The Python
checkpoint validator checks the envelope, native save integrity and slot records;
it does not perform native inventory/checkpoint pairing itself.

For example, the game can have live cursor 12 while disk still has cursor 10.
If death/load restores the checkpoint at 10, the ledger resumes with item 11.
It retains the server queue and verifies the restored history. Using the host's
previous high-water mark of 12 would skip items missing from restored inventory.

Outgoing location checks have their own acknowledgement. The game records the
collected-location bit; the host persists it and marks it uploaded after server
acknowledgement. That acknowledgement does not mean an incoming item was granted
or a console save completed. A foreign-recipient location records its check
without granting the foreign item's displayed model to the local player.

The presentation path starts only after a live grant commits. Its event is
`recipe_index * 4 + applied_progression_stage`, grouped into banks of 16. Each
bank has one current-area claimant. Splitting a bank across Lua dispatchers
could consume a notice before the script owning its text sees it. Retail LUAX
binds InternalState0 through 19, even though RDS exposes higher state codes.
These are native dispatch constraints, not spare schema fields to use freely.

The accepted receive path submits an asynchronous IOS receive with blocking
socket flags when the experimental NONBLOCK define is absent. The wait belongs
to that asynchronous request; do not turn it into a synchronous game-thread
receive loop. RDS migration changes resource handling, not this transport mode.

## Selecting a cross-world visual

`randovania/games/prime3/exporter/models.py:model_plan()` starts with the
serialized pickup and its verified digest. The recipient game's database decodes
the pickup, then `PickupModel.game` and `PickupModel.name` identify the visual.
The recipient's game, item display text and sender name cannot substitute for
those model fields. The approved Nothing override uses Corruption's native
Friend Credit even for an older seed serialized with a different Nothing model.

The model plan contains location index plus visual identity for all 100 locations.
The grant recipe stays in the multiworld path above. The post-core model stage
works on randomized PAKs; it cannot restore a retail room just to obtain a useful
actor template. That would also restore the room's old pickup and script state.

`multiworld_models.visual_bindings()` follows the existing core recipe targets,
including fake-pickup aliases in other areas. It identifies the exact MREA,
layer, instance and serialized model slot. It replaces the audited CMDL/CHAR
fields present on that actor and adds loading dependencies to the correct layer.
PAK presence alone does not make an asset available when its layer streams in.

The rebuilt room is parsed again. Restoring only the original visual fields for
comparison must reproduce the original seeded actors. Grants, callbacks,
connections and transforms stay intact. Archive readback then checks every
written resource. An occupied asset ID can reuse an equal payload; a different
payload under the same ID is rejected. Scripted rewards with no audited model
slot are reported instead of acquiring an invented collectible actor.

## Prime/Echoes assets in Corruption

`multiworld_models.ModelCache` selects entries by source game and normalized
catalog name together. Prime's Missile Expansion resolves to its catalog's
Missile entry. Native rigs require CMDL, CSKR, CINF, CHAR, SAND and ANIM entries;
the stage also installs the accepted shared particle/texture pool. Each file's
hash, resource type, identity and required inventory are checked before use.

The full accepted cache has 93 entries and 770 resources. The separately allowed
Echoes-only policy names exactly PowerBeam INCOMPLETE, CombatVisor INCOMPLETE
and MorphBall INCOMPLETE as native fallbacks. Disabling a game's foreign models
also keeps the existing native visual through a presentation-only projection.
Neither route changes recipient or grant. A missing model outside the recorded
policy remains an export error; it does not silently become Scan Visor.

The installed cache comes from the accepted gallery PAK, checked against its
image hash and converted asset inventory. The renderer retains the reviewed
opaque emission materials and model-matched effect scale. The isolated Ice Beam
rig/animation/effect tools document narrower experiments; their existence does
not make arbitrary character conversion part of this accepted cache path.

## Corruption assets in Prime/Echoes

`PickupExporter.export()` first applies the requested model style, including
disguised visuals, and carries the original visual alongside the ordinary
offworld fallback. `PickupExporter.get_model()` resolves the target-specific
offworld name. `original_pickup_model()` handles the legacy Ship Missile
Expansion alias without rewriting the pickup or its multiworld identity.

Prime's `adjust_model_names()` and Echoes' `adjust_model_name()` look up the
game-qualified original visual in the assets available to that export. If no
converted entry exists, they retain the ordinary offworld model. That native
fallback policy belongs to the GC exporters; it is separate from Corruption's
strict validated-cache rules above. Model style and available converted assets
therefore both matter before any destination model index is selected.

`randovania/patching/prime/corruption_pickup_models.py` handles this direction.
Its version-32 cache identity includes the source disc hash, target game, RDS
version and target asset-ID population. The target population matters because
allocated IDs must avoid existing resources. Reusing a cache from a different
target extraction can collide even with the same source Corruption disc.

Conversion builds native meshes/textures and character-backed ANCS rigs with
their skin, skeleton, animation, event and particle dependencies. A Wii CHAR is
not renamed into ANCS. `corruption_character.py` rewrites destination bone IDs,
parent markers and references, selects a supported pickup animation leaf and
serializes through the target layouts. Energy Cell has no source CHAR and keeps
its static route. The emitted family allowlist and dependency closure are checked
along with every cached payload hash.

The main Ship Missile uses CMDL `79DF78A539413751` and CHAR `A50DCBEF4C7A8E41`.
Ship Missile Expansion uses CMDL `4F21FCF9B0693C90` and CHAR `778810531A3E822A`.
Keep that distinction through required-launcher rules and old-seed alias handling.
The reviewed 0.925 presentation adjustment belongs to the expansion model.

`corruption_model_scale.py` matches the seed's native rendered footprint while
preserving proportions and per-axis modifiers. Reviewed visual multipliers are
applied afterward. Particle conversion records unsupported Wii operations and
approximations; schema acceptance alone cannot establish that a GC interpreter
implements the same operation or shader. Cache validation proves the declared
resources are consistent, not that the visual matches Wii rendering exactly.

## What remains unverified

The migration's structural, scripted connection, runtime-generation and package
checks are recorded in the phase reports. Live delivery, checkpoint rollback,
save/reload and physical Wii/vWii acceptance for the migrated build remain
separate. The existing model-gallery acceptance is evidence for that gallery's
assets, not a new seeded gameplay or hardware result. This notation pass adds
comments and explanation; it does not change the transport, grants, model
selection, cache revision or release/deployment state.
