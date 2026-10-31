# Guard the supported retail frame-completion entry before installing the pump. Boundary
# names here: patch.
"""Guard the supported retail frame-completion entry before installing the pump."""
import hashlib

from randovania.games.prime3.exporter.dol_patcher import (
    encode_ppc_unconditional_branch,
    parse_dol_header,
    patch_guarded_instruction_word,
)

ADDRESS = 0x803E9F78
SIZE = 964
SHA256 = "eef27a5fdfe146f70dff58205ad62b92e9972d6fa03a2eed15191931ffaf8ffe"
SYMBOLS = {"network_frame_poll", "network_frame_poll_hook", "network_frame_poll_state"}
CONTRACT = {"schema": 2, "kind": "retail_graphics_end_scene", "address": ADDRESS,
            "function_size": SIZE, "function_sha256": SHA256,
            "cadence_ms": 500, "lua_driven": False, "applies_items": False}


def patch(original, updated, symbols):
    offset = parse_dol_header(original).offset_for_address(ADDRESS)
    if hashlib.sha256(original[offset:offset + SIZE]).hexdigest() != SHA256:
        raise ValueError("Unsupported retail CGraphics::EndScene function")
    return patch_guarded_instruction_word(
        updated, address=ADDRESS, expected_original_word=0x9421FED0,
        replacement_word=encode_ppc_unconditional_branch(ADDRESS, symbols["network_frame_poll_hook"]),
    )
