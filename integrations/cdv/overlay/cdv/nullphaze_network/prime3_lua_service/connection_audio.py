# GPL addon: one-shot connection cues built locally from the user's game. Boundary names
# here: stream_id, make_stream.
"""GPL addon: one-shot connection cues built locally from the user's game.

Preserve DSP frames and channel state; wrap them in the already supported FSB3
stream container. No audio decoder, encoder or retail payload is distributed.
"""
import hashlib
import struct

from nullphaze_core.archives import Resource


CUES = {
    "lost": ("WarnLowHealth", 0xE5B3C708DDCA80DC),
    "restored": ("PauseMapRevealLandingsite", 0xB3C3DFCD8EA41CAB),
}


def stream_id(event):
    name, _ = CUES[event]
    return int.from_bytes(hashlib.sha256(f"Nullphaze connection audio v1/{name}".encode()).digest()[:8], "big")


def make_stream(event, sample, template):
    """Bounded mono CSMP/DSP to non-looping FSB3, without changing samples."""
    if sample[:8] != b"CSMP\0\0\0\1":
        raise ValueError("Connection cue lacks a supported CSMP header")
    offset, dsp = 8, None
    while offset < len(sample) and not all(b in (0, 255) for b in sample[offset:]):
        if offset + 8 > len(sample):
            raise ValueError("Truncated connection cue chunk")
        kind, size = struct.unpack_from(">4sI", sample, offset)
        size -= 4 if kind == b"DATA" else 0
        offset += 8
        if kind not in (b"NAME", b"INFO", b"PAD ", b"DATA") or size < 0 or offset + size > len(sample):
            raise ValueError("Invalid connection cue chunk")
        if kind == b"DATA":
            if dsp is not None:
                raise ValueError("Ambiguous connection cue sample")
            dsp = sample[offset:offset + size]
        offset += size
    if dsp is None or len(dsp) < 96:
        raise ValueError("Connection cue lacks a DSP sample")
    samples, nibbles, rate = struct.unpack_from(">III", dsp)
    if (not 1 <= rate <= 48000 or not 1 <= samples <= rate * 5 or nibbles < 2
            or samples > (nibbles // 16 * 14 + max(0, nibbles % 16 - 2))
            or (nibbles + 1) // 2 > len(dsp) - 96 or dsp[14:16] != b"\0\0"):
        raise ValueError("Connection cue DSP bounds or encoding are unsupported")
    if (template[:4] != b"FSB3" or len(template) < 104
            or struct.unpack_from("<I", template, 4)[0] != 1
            or struct.unpack_from("<I", template, 16)[0] != 0x30001):
        raise ValueError("Connection cue needs the native FSB3 stream template")
    payload = dsp[96:96 + (nibbles + 1) // 2]
    payload += bytes(-len(payload) % 8)
    header = bytearray(template[24:104])
    struct.pack_into("<H", header, 0, 126)  # 80-byte sample header + mono DSP state.
    header[2:32] = CUES[event][0].encode()[:29].ljust(30, b"\0")
    struct.pack_into("<IIII", header, 32, samples, len(payload), 0, 0)
    mode = struct.unpack_from("<I", header, 48)[0]
    if not mode & 0x02000000:
        raise ValueError("Connection cue template is not DSP audio")
    struct.pack_into("<I", header, 48, (mode & ~7) | 1)  # LOOP_OFF, no loop range.
    struct.pack_into("<I", header, 52, rate)
    struct.pack_into("<H", header, 62, 1)
    # DSP coefficients/state remain big endian in the FSB3 channel extension.
    bank = b"FSB3" + struct.pack("<5I", 1, 126, len(payload), 0x30001, 0) + header + dsp[28:74] + payload
    bank += b"\xff" * (-len(bank) % 64)
    return Resource(stream_id(event), b"STRM", 0, len(bank), data=bank)
