"""Streaming Wii PAK tables with explicit resource aliases and bounded reads."""
from dataclasses import dataclass, replace
from pathlib import Path
import struct
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
        with self.path.open('rb') as stream:
            header = stream.read(128)
            if len(header) != 128:
                raise FormatError('Truncated PAK header')
            if header[68:72] != b'STRG' or header[76:80] != b'RSHD' or header[84:88] != b'DATA':
                raise FormatError('Invalid PAK section table')
            name_size, table_size, data_size = struct.unpack_from('>I', header, 72)[0], struct.unpack_from('>I', header, 80)[0], struct.unpack_from('>I', header, 88)[0]
            if name_size % 64 or table_size % 64 or 128+name_size+table_size+data_size > size:
                raise FormatError('PAK sections exceed bounded archive')
            names = stream.read(name_size)
            table = Reader(stream.read(table_size))
        self.header = header[:64]
        named = Reader(names)
        for _ in range(named.count(13)):
            named.cstring()
            named.read(12)
        self.names = pad(names[:named.pos], 64)
        self.resources = []
        for _ in range(table.count(24)):
            flag, kind, identity, length, offset = struct.unpack('>I4sQII', table.read(24))
            if flag not in (0, 1) or length % 64 or offset+length > data_size:
                raise FormatError('Invalid PAK resource extent or flag')
            self.resources.append(Resource(identity, kind, flag, length, self.path, 128+name_size+table_size+offset))

    def write(self, destination, resources, clear=False):
        names = pad(pack('I', 0), 64) if clear else self.names
        table = bytearray(pack('I', len(resources)))
        offset = 0
        for resource in resources:
            if len(resource.kind) != 4 or resource.size % 64:
                raise FormatError('Invalid output resource metadata')
            table.extend(pack('I4sQII', resource.compressed, resource.kind, resource.identity, resource.size, offset))
            offset += resource.size
        table = pad(table, 64)
        toc = pad(pack('I4sI4sI4sI', 3, b'STRG', len(names), b'RSHD', len(table), b'DATA', offset), 64)
        streams = {}
        try:
            with Path(destination).open('xb') as output:
                output.write(self.header+toc+names+table)
                for resource in resources:
                    resource.copy_to(output, streams)
                output.write(bytes((-output.tell()) % 64))
        finally:
            for stream in streams.values():
                stream.close()
