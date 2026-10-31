# Native atlas frame extraction without changing the source texels or format. Boundary names
# here: crop_cmpr, atlas_frame.
"""Native atlas frame extraction without changing the source texels or format."""

import math
import struct


def crop_cmpr(source, source_width, origin_x, origin_y, width, height):
    """Retile DXT1 indices while retaining the source color endpoints exactly."""
    result = bytearray()
    macro_columns = (source_width + 7) // 8
    for macro_y in range((height + 7) // 8):
        for macro_x in range((width + 7) // 8):
            for quadrant_y in range(2):
                for quadrant_x in range(2):
                    palette = None
                    rows = []
                    for y in range(4):
                        bits = 0
                        for x in range(4):
                            sx = origin_x + min(width - 1, macro_x * 8 + quadrant_x * 4 + x)
                            sy = origin_y + min(height - 1, macro_y * 8 + quadrant_y * 4 + y)
                            offset = ((sy // 8) * macro_columns + sx // 8) * 32
                            offset += ((sy % 8) // 4 * 2 + (sx % 8) // 4) * 8
                            endpoints = source[offset : offset + 4]
                            if palette is not None and palette != endpoints:
                                raise ValueError("Atlas crop crosses incompatible compressed color blocks")
                            palette = endpoints
                            index = (source[offset + 4 + sy % 4] >> (6 - 2 * (sx % 4))) & 3
                            bits |= index << (6 - 2 * x)
                        rows.append(bits)
                    result.extend(palette)
                    result.extend(rows)
    return result


def atlas_frame(payload, tile_width, tile_height, phase):
    """Extract the clamped TEXP phase used by the retail Wii UV reader.

    The source reader at 0x803E0660 selects int(phase * frame_count),
    clamped to the last frame, from rows enumerated bottom to top.
    RGB565/RGB5A3 and CMPR mip levels preserve their source texels.
    """
    texture_format, width, height, levels = struct.unpack_from(">IHHI", payload)
    if texture_format not in (7, 8, 10):
        raise ValueError("Unsupported native atlas texture format")
    if not math.isfinite(phase) or min(tile_width, tile_height) <= 0:
        raise ValueError("Invalid atlas phase or tile extent")
    if width % tile_width or height % tile_height:
        raise ValueError("Atlas tiles must divide the texture")
    columns, rows = width // tile_width, height // tile_height
    index = max(0, min(columns * rows - 1, int(phase * columns * rows)))
    tile_x, tile_y = index % columns, rows - 1 - index // columns
    encoded = bytearray(struct.pack(">IHHI", texture_format, tile_width, tile_height, levels))
    offset = 12
    for level in range(levels):
        source_w, source_h = max(1, width >> level), max(1, height >> level)
        target_w, target_h = max(1, tile_width >> level), max(1, tile_height >> level)
        block = 8 if texture_format == 10 else 4
        source_columns = (source_w + block - 1) // block
        source_size = source_columns * ((source_h + block - 1) // block) * 32
        source = payload[offset : offset + source_size]
        if len(source) != source_size:
            raise ValueError("Truncated atlas mip level")
        if texture_format == 10:
            encoded.extend(crop_cmpr(source, source_w, tile_x * target_w, tile_y * target_h, target_w, target_h))
            offset += source_size
            continue
        for block_y in range((target_h + 3) // 4):
            for block_x in range((target_w + 3) // 4):
                for y in range(4):
                    for x in range(4):
                        sx = min(source_w - 1, tile_x * target_w + min(target_w - 1, block_x * 4 + x))
                        sy = min(source_h - 1, tile_y * target_h + min(target_h - 1, block_y * 4 + y))
                        position = ((sy // 4) * source_columns + sx // 4) * 32 + ((sy % 4) * 4 + sx % 4) * 2
                        encoded.extend(source[position : position + 2])
        offset += source_size
    if any(value not in (0, 255) for value in payload[offset:]):
        raise ValueError("Unrecognized atlas payload tail")
    return bytes(encoded), index
