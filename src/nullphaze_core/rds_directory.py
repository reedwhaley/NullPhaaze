# Serialize the RDS PAK directory with the actual stored extents and alignment. Aliased
# records can reuse an extent; the payload sequence still defines the output bounds.
# Boundary names here: write_records.
"""RDS PAK directory serialization for sequential and aliased payload layouts."""
from pathlib import Path
import construct as cs
from retro_data_structures.formats.pak_wii import PAKNoData
from .binary import FormatError
from .rds_formats import GAME


def write_records(archive, destination, records, payloads, clear=False):
    records, payloads = list(records), list(payloads)
    extent = sum(resource.size for resource in payloads)
    metadata = cs.Container(_header=archive.metadata._header,
        table_of_contents=cs.Container(archive.metadata.table_of_contents),
        named_resources=[] if clear else list(archive.metadata.named_resources), resources=[])
    for resource, offset in records:
        if (len(resource.kind) != 4 or resource.size % 64 or offset % 64 or offset < 0
                or offset + resource.size > extent or resource.compressed not in (0, 1)):
            raise FormatError('Invalid output PAK resource extent or metadata')
        metadata.resources.append(cs.Container(compressed=resource.compressed,
            asset_type=resource.kind.decode('ascii'), asset_id=resource.identity,
            size=resource.size, offset=offset))
    preliminary = PAKNoData.build(metadata, target_game=GAME)
    measured = PAKNoData.parse(preliminary, target_game=GAME)
    metadata.table_of_contents.STRG = measured._resources_start - measured._named_resources_start
    metadata.table_of_contents.RSHD = measured._resources_end - measured._resources_start
    metadata.table_of_contents.DATA = extent
    header = PAKNoData.build(metadata, target_game=GAME)
    # The directory can point backward to an identical payload. Keep every
    # entry and its order; removing an alias changes the native area bundles.
    streams = {}
    try:
        with Path(destination).open('xb') as output:
            output.write(archive.header + header[64:])
            for resource in payloads:
                resource.copy_to(output, streams)
            output.write(bytes(-output.tell() % 64))
    finally:
        for stream in streams.values():
            stream.close()
