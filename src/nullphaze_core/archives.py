# I keep every PAK directory entry, its order and its alias metadata while loading payloads
# lazily. Equal resource IDs do not authorize dropping a table occurrence. Boundary names
# here: Resource, Archive.
"""Streaming Wii PAK tables with explicit resource aliases and bounded reads."""
from dataclasses import dataclass, replace
from pathlib import Path
import struct
import construct as cs
from retro_data_structures.formats.pak_wii import PAKNoData
from .rds_formats import GAME
from .binary import Reader, FormatError, pad, pack


@dataclass(frozen=True)
class Resource:
    identity: int
    kind: bytes
    compressed: int
    size: int
    source: Path | None = None
    offset: int = 0
    data: bytes | None = None

    def read(self):
        if self.data is not None:
            return self.data
        with self.source.open('rb') as stream:
            stream.seek(self.offset)
            result = stream.read(self.size)
        if len(result) != self.size:
            raise FormatError('Resource source changed or is truncated')
        return result

    def updated(self, data, kind=None, compressed=None):
        data = pad(data, 64, 255)
        return replace(self, size=len(data), data=data, source=None, offset=0,
                       kind=kind or self.kind, compressed=self.compressed if compressed is None else compressed)

    def copy_to(self, destination, streams):
        if self.data is not None:
            destination.write(self.data)
            return
        if self.source not in streams:
            streams[self.source] = self.source.open('rb')
        stream = streams[self.source]
        stream.seek(self.offset)
        remaining = self.size
        while remaining:
            block = stream.read(min(remaining, 1024*1024))
            if not block:
                raise FormatError('Truncated archive payload')
            destination.write(block)
            remaining -= len(block)


class Archive:
    def __init__(self, path):
        self.path = Path(path)
        size = self.path.stat().st_size
        try:
            with self.path.open('rb') as stream:
                metadata = PAKNoData.parse_stream(stream, target_game=GAME)
                stream.seek(0)
                self.header = stream.read(64)
        except (cs.ConstructError, ValueError, KeyError, IndexError, struct.error) as error:
            raise FormatError(f'Invalid RDS PAK header: {error}') from error
        self.metadata = metadata
        toc = metadata.table_of_contents
        if set(toc) != {'STRG', 'RSHD', 'DATA'} or any(toc[k] % 64 for k in toc):
            raise FormatError('Invalid PAK section table')
        data_start = metadata._resources_end
        if (metadata._resources_start - metadata._named_resources_start != toc.STRG or
                metadata._resources_end - metadata._resources_start != toc.RSHD or
                data_start + toc.DATA > size):
            raise FormatError('PAK sections exceed bounded archive')
        self.resources = []
        for entry in metadata.resources:
            if (entry.compressed not in (0, 1) or entry.size % 64 or
                    entry.offset + entry.size > toc.DATA):
                raise FormatError('Invalid PAK resource extent or flag')
            self.resources.append(Resource(int(entry.asset_id), entry.asset_type.encode('ascii'),
                entry.compressed, entry.size, self.path, data_start + entry.offset))

    @property
    def names(self):
        schema = next(field.subcon for field in PAKNoData.subcons if field.name == 'named_resources')
        return schema.build(self.metadata.named_resources, target_game=GAME)

    @names.setter
    def names(self, value):
        from .rds_formats import parse_exact
        schema = next(field.subcon for field in PAKNoData.subcons if field.name == 'named_resources')
        self.metadata.named_resources = parse_exact(schema, value)

    def write(self, destination, resources, clear=False):
        from .rds_directory import write_records
        resources = list(resources)
        records, offset = [], 0
        for resource in resources:
            records.append((resource, offset))
            offset += resource.size
        write_records(self, destination, records, resources, clear)
