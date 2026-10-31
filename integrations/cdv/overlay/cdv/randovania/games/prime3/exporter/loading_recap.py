# Guarded USA rev0 loader presentation bypass; retain native world loading. Boundary names
# here: patch, install.
"""Guarded USA rev0 loader presentation bypass; retain native world loading."""
from __future__ import annotations

import hashlib
from pathlib import Path

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header

CONSTRUCTOR = 0x800E1BA8
CONSTRUCTOR_END = 0x800E1F38
PRESENTATION_GATE = 0x800E1D30
LOADING_CONTINUATION = 0x800E1EF0
CONSTRUCTOR_SHA256 = "ac0a5f5969ba60e31a98449450dd5b0feffad1678d11aca3f4d44447b2abbd0a"
ORIGINAL = bytes.fromhex("88061A44")  # lbz r0,0x1a44(r6)
BYPASS = bytes.fromhex("38000040")  # li r0,0x40: native suppress-presentation request


def patch(data: bytes) -> tuple[bytes, dict]:
    header = parse_dol_header(data)
    section = header.section_for_address(CONSTRUCTOR)
    if section is None or section.kind != "text" or CONSTRUCTOR_END > section.end_address:
        raise ValueError("Loading recap: unsupported executable section layout")
    start = header.offset_for_address(CONSTRUCTOR)
    offset = header.offset_for_address(PRESENTATION_GATE)
    assert start is not None and offset is not None
    current = data[offset:offset + 4]
    if current not in (ORIGINAL, BYPASS):
        raise ValueError("Loading recap: unsupported presentation gate")
    normalized = bytearray(data[start:start + CONSTRUCTOR_END - CONSTRUCTOR])
    gate = PRESENTATION_GATE - CONSTRUCTOR
    normalized[gate:gate + 4] = ORIGINAL
    if hashlib.sha256(normalized).hexdigest() != CONSTRUCTOR_SHA256:
        raise ValueError("Loading recap: unsupported loader constructor; refusing to patch")
    result = data[:offset] + BYPASS + data[offset + 4:]
    return result, {
        "patch": "usa-rev0-loading-suppression-flag-v1",
        "changed": current != BYPASS,
        "address": f"{PRESENTATION_GATE:08X}",
        "suppression_flag_mask": 64,
        "shared_assets_modified": False,
        "continuation": f"{LOADING_CONTINUATION:08X}",
        "input_sha256": hashlib.sha256(data).hexdigest(),
        "output_sha256": hashlib.sha256(result).hexdigest(),
        "constructor_sha256": CONSTRUCTOR_SHA256,
        "asset_bytes_removed": 0,
        "gameplay_verified": False,
    }


def install(data_root: Path) -> dict:
    """Install only in the export's owned extraction, before image rebuilding."""
    path = Path(data_root) / "sys/main.dol"
    before = path.read_bytes()
    after, report = patch(before)
    if report["changed"]:
        # Replace rather than truncate: a diagnostic extraction may use hardlinks.
        temporary = path.with_name("main.dol.loading-recap-new")
        with temporary.open("xb") as stream:
            stream.write(after)
        temporary.replace(path)
    if path.read_bytes() != after:
        raise ValueError("Loading recap: executable readback mismatch")
    return report
