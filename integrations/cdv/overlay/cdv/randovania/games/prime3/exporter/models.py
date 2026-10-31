# Visual identities are decoded independently of item names and recipients. Boundary names
# here: model_plan.
"""Visual identities are decoded independently of item names and recipients."""

from __future__ import annotations

import base64
import hashlib

from randovania.bitpacking.bitpacking import BitPackDecoder
from randovania.game.game_enum import RandovaniaGame
from randovania.game_description import default_database
from randovania.games.prime3.multiworld.manifest import pickup_bytes
from randovania.network_common.pickup_serializer import BitPackPickupEntry


def model_plan(manifest: dict) -> list[dict]:
    # Decode with the recipient game's database because that owns the pickup's
    # serialized resource references. The visual identity still comes from
    # PickupModel.game/name; recipient game and item display text cannot choose
    # the mesh. A cross-world item can intentionally use another game's model.
    result = []
    for row in manifest["locations"]:
        game = RandovaniaGame(row["recipient_game"])
        raw = base64.b85decode(row["pickup"])
        if len(raw) > 4096 or hashlib.sha256(raw).hexdigest() != row["pickup_key"]:
            raise ValueError("Pickup model source digest mismatch")
        database = default_database.resource_database_for(game)
        pickup = BitPackPickupEntry.bit_pack_unpack(BitPackDecoder(raw), database)
        if pickup_bytes(pickup, database) != raw:
            raise ValueError("Non-canonical pickup model source")
        # Nothing uses Corruption's native Friend Credit even for legacy seeds
        # whose serialized model was Scan Visor or a foreign Nothing mesh.
        visual = {"game": "prime3", "name": "Nothing"} if pickup.name == "Nothing" else pickup.model.as_json
        # Return only location + visual identity. Grant recipes, sender text and
        # receipt sequencing stay in the multiworld manifest/runtime path.
        result.append({"index": row["index"], **visual})
    if [r["index"] for r in result] != list(range(100)):
        raise ValueError("Model plan requires all 100 ordered locations")
    return result
