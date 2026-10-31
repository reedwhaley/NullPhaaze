# This inspects wrist-strap resource records and CMPR/alpha data. Decoded previews describe
# the supplied resource; they do not replace the production frontend or prove native
# rendering. Boundary names here: decode_cmpr, analyze, main.
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import struct
import sys
from pathlib import Path

from PIL import Image

if __package__ in {None, ""}:
    _repository_root = Path(__file__).resolve().parents[2]
    _repository_root_str = os.fspath(_repository_root)
    if _repository_root_str not in sys.path:
        sys.path.insert(0, _repository_root_str)

from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.pak_wii import PAKNoData
from retro_data_structures.formats.txtr import TXTR
from retro_data_structures.game_check import Game

RESOURCE_NAMES = (
    "TXTR_StrapScreenA43",
    "TXTR_StrapScreenB43",
    "TXTR_StrapScreenA169",
    "TXTR_StrapScreenB169",
)


def _rgb565(value: int) -> tuple[int, int, int]:
    return (
        ((value >> 11) & 0x1F) * 255 // 31,
        ((value >> 5) & 0x3F) * 255 // 63,
        (value & 0x1F) * 255 // 31,
    )


def _cmpr_colors(first: int, second: int) -> tuple[tuple[int, int, int, int], ...]:
    first_rgb = _rgb565(first)
    second_rgb = _rgb565(second)
    colors = ((first_rgb[0], first_rgb[1], first_rgb[2], 255), (second_rgb[0], second_rgb[1], second_rgb[2], 255))
    if first > second:
        return colors + (
            tuple((2 * first_rgb[index] + second_rgb[index]) // 3 for index in range(3)) + (255,),
            tuple((first_rgb[index] + 2 * second_rgb[index]) // 3 for index in range(3)) + (255,),
        )
    return colors + (
        tuple((first_rgb[index] + second_rgb[index]) // 2 for index in range(3)) + (255,),
        (0, 0, 0, 0),
    )


def decode_cmpr(image_data: bytes, width: int, height: int) -> Image.Image:
    expected_size = ((width + 7) // 8) * ((height + 7) // 8) * 32
    if len(image_data) != expected_size:
        raise ValueError(f"CMPR data has {len(image_data)} bytes; expected {expected_size}")

    pixels = bytearray(width * height * 4)
    offset = 0
    for block_y in range(0, height, 8):
        for block_x in range(0, width, 8):
            for subblock_y in range(2):
                for subblock_x in range(2):
                    first, second, indexes = struct.unpack_from(">HHI", image_data, offset)
                    offset += 8
                    colors = _cmpr_colors(first, second)
                    for pixel_y in range(4):
                        for pixel_x in range(4):
                            target_x = block_x + subblock_x * 4 + pixel_x
                            target_y = block_y + subblock_y * 4 + pixel_y
                            if target_x >= width or target_y >= height:
                                continue
                            index = (indexes >> (30 - 2 * (pixel_y * 4 + pixel_x))) & 3
                            pixel_offset = (target_y * width + target_x) * 4
                            pixels[pixel_offset : pixel_offset + 4] = bytes(colors[index])
    return Image.frombytes("RGBA", (width, height), bytes(pixels))


def _pak_records(pak_path: Path) -> tuple[Pak, dict[int, dict[str, int | str]]]:
    with pak_path.open("rb") as stream:
        header = PAKNoData.parse_stream(stream)
        data_start = (stream.tell() + 63) & ~63
    records: dict[int, dict[str, int | str]] = {}
    for resource in header.resources:
        records[int(resource.asset_id)] = {
            "packed_offset": data_start + int(resource.offset),
            "packed_size": int(resource.size),
            "compressed": int(resource.compressed),
            "asset_type": str(resource.asset_type),
        }
    with pak_path.open("rb") as stream:
        return Pak.parse_stream(stream, Game.CORRUPTION), records


def _alpha_summary(image: Image.Image) -> dict[str, int | list[int] | None]:
    alpha = image.getchannel("A")
    extrema = alpha.getextrema()
    alpha_bytes = alpha.tobytes()
    opaque = sum(value == 255 for value in alpha_bytes)
    transparent = sum(value == 0 for value in alpha_bytes)
    nonopaque = len(alpha_bytes) - opaque
    bounding_box = alpha.getbbox()
    return {
        "alpha_min": extrema[0],
        "alpha_max": extrema[1],
        "opaque_pixels": opaque,
        "transparent_pixels": transparent,
        "nonopaque_pixels": nonopaque,
        "nonzero_alpha_bbox": list(bounding_box) if bounding_box is not None else None,
    }


def analyze(pak_path: Path, output_directory: Path) -> list[dict[str, object]]:
    pak, records = _pak_records(pak_path)
    named_resources = dict(pak._raw.named_resources)
    output_directory.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    with pak_path.open("rb") as stream:
        for name in RESOURCE_NAMES:
            dependency = named_resources[name]
            asset_id = int(dependency.id)
            resource = pak.get_asset(dependency.id)
            if resource is None or resource.type != "TXTR":
                raise ValueError(f"{name} is not a TXTR resource")
            record = records[asset_id]
            stream.seek(int(record["packed_offset"]))
            packed_data = stream.read(int(record["packed_size"]))
            txtr = TXTR.parse(resource.data)
            if txtr.header.format != 10:
                raise ValueError(f"{name} uses unsupported GX format {txtr.header.format}")
            image = decode_cmpr(txtr.image_data, txtr.header.width, txtr.header.height)
            blob_path = output_directory / f"{name}.txtr"
            packed_path = output_directory / f"{name}.pak-compressed"
            png_path = output_directory / f"{name}.png"
            display_png_path = output_directory / f"{name}.display.png"
            blob_path.write_bytes(resource.data)
            packed_path.write_bytes(packed_data)
            image.save(png_path)
            image.transpose(Image.Transpose.FLIP_TOP_BOTTOM).save(display_png_path)
            row: dict[str, object] = {
                "name": name,
                "pak_path": str(pak_path),
                "asset_id": f"0x{asset_id:016X}",
                "asset_type": str(resource.type),
                "pak_compressed": bool(record["compressed"]),
                "pak_data_offset": f"0x{int(record['packed_offset']):X}",
                "pak_data_size": int(record["packed_size"]),
                "packed_sha256": hashlib.sha256(packed_data).hexdigest(),
                "txtr_size": len(resource.data),
                "txtr_sha256": hashlib.sha256(resource.data).hexdigest(),
                "gx_format": "CMPR",
                "width": txtr.header.width,
                "height": txtr.header.height,
                "mipmap_count": txtr.header.mipmap_count,
                "image_data_size": len(txtr.image_data),
                "png_path": str(png_path),
                "png_sha256": hashlib.sha256(png_path.read_bytes()).hexdigest(),
                "display_png_path": str(display_png_path),
                "display_png_sha256": hashlib.sha256(display_png_path.read_bytes()).hexdigest(),
                **_alpha_summary(image),
            }
            rows.append(row)
    with (output_directory / "resource-table-records.json").open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(rows, stream, indent=2)
        stream.write("\n")
    with (output_directory / "resource-table-records.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract and decode Prime 3 retail wrist-strap TXTR resources.")
    parser.add_argument("--pak", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = analyze(args.pak, args.output)
    print(json.dumps(rows, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
