# I keep every PAK directory entry, its order and its alias metadata while loading payloads
# lazily. Equal resource IDs do not authorize dropping a table occurrence. Boundary names
# here: Resource, Archive.
"""
Streaming Wii PAK tables with explicit resource aliases and bounded reads.
See https://wiki.axiodl.com/w/PAK_(Metroid_Prime_3)
"""
from dataclasses import dataclass, replace
from pathlib import Path
import struct
import construct as cs
from typing import Dict, List, Any
from io import BytesIO
from retro_data_structures.formats.pak_wii import PAKNoData
from .rds_formats import GAME
from .binary import Reader, FormatError, pad, pack


@dataclass(frozen=True)
class Resource:
    """
    Represents an individual, unparsed resource in a PAK file.
    Resource data is not immediately loaded into memory, so it must be read before use
    """
    identity: int
    """The resource's ResourceID"""
    kind: bytes
    """The FourCC representing the resource's type (MREA, MLVL, etc...)"""
    compressed: int
    """Whether the resource is compressed via LZO"""
    size: int
    """The size, in bytes, of the resource in the PAK. Accounts for padding, so always a multiple of 64"""
    source: Path | None = None
    """A path to the PAK file whence the resource comes from"""
    offset: int = 0
    """The offset of the resource's start relative to the start of the file (as opposed to the start of the DATA section)"""
    data: bytes | None = None
    """Optional, in-memory payload for when the resource has been manually created"""

    def read(self) -> bytes:
        """
        Reads the raw bytes from the resource

        Raises :
        - FormatError if expected size and read result size are mismatched
        """
        # If we already have memoized data, directly return it
        if self.data is not None:
            return self.data
        # Otherwise, read from the source file and memoize the result if ok
        # TODO : handle case where `self.source` is None
        with self.source.open('rb') as stream:
            stream.seek(self.offset)
            result = stream.read(self.size)
        if len(result) != self.size:
            raise FormatError('Resource source changed or is truncated')
        # TODO : memoize the read data once we've checked its validity
        return result

    def updated(self, data, kind=None, compressed=None):
        """
        Builds a new resource based on the current one. New resource is orphaned at creation
        Since data is directly provided, we can immediately memoize it for furure reads

        Arguments :
        - data : The raw bytes in the resource to be created        

        Keyword arguments :
        - kind : The FourCC type of resource. Defaults to this instance's type
        - compressed : Whether the new resource is compressed. Defaults to this instance's compression
        """
        data = pad(data, 64, 255)
        # TODO : make the None checks consistent accross both kwargs
        return replace(self, size=len(data), data=data, source=None, offset=0,
                       kind=kind or self.kind, compressed=self.compressed if compressed is None else compressed)

    def copy_to(self, destination : BytesIO, streams : Dict[Path, BytesIO]) -> None:
        """
        Copies this resource's memoized data to the specified destination
        If this resource's parent PAK file has no stream open, it will be opened added to `streams`

        Warning : the streams aren't closed after return, so the caller will have to close them 

        Arguments :
        - destination : the output stream on which to write the copy
        - streams : dictionnary linking resource source paths to open streams
        """
        ## Note : I REALLY don't like this implementation, even though it technically works for now.
        ## Keeping the stream open after the function returns when its purpose isn't opening the stream
        ## is a dangerous game to play, and is bad practice. Also, giving this function more side effects 
        ## than the copy by modifying `streams` is a recipe for mistakes.
        ## Also, the Resource.read method is right there, I don't know why we are reinventing the wheel here.

        # If the resource already has memoized data, directly copy it
        if self.data is not None:
            destination.write(self.data)
            return
        # Otherwise, read it, then write it to the destination 
        # TODO : Replace this with `destination.write(self.read())`
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
    """
    Represents a lazily parsed PAK file. Wrapper for RDS's `PakNoData` class
    """
    # TODO : Define all the fields initialized in __init__ here, along with their types
    def __init__(self, path : Any) -> None:
        self.path = Path(path)
        size = self.path.stat().st_size
        
        # Parse metadata
        try:
            with self.path.open('rb') as stream:
                # TODO : declare `metadata` outside of this block, as it is to be used outside of it
                metadata = PAKNoData.parse_stream(stream, target_game=GAME)
                stream.seek(0)
                self.header = stream.read(64)
        except (cs.ConstructError, ValueError, KeyError, IndexError, struct.error) as error:
            raise FormatError(f'Invalid RDS PAK header: {error}') from error
        self.metadata = metadata

        # Find Table of Contents and the start of the DATA section
        toc = metadata.table_of_contents
        if set(toc) != {'STRG', 'RSHD', 'DATA'} or any(toc[k] % 64 for k in toc):
            raise FormatError('Invalid PAK section table')
        ## NOTE : In Python, fields and methods starting with and _underscore are meant to have private visibility, like in C++ or Java.
        ## While Python allows reading the field, it is to be treated as such, and shouldn't be accessed this way
        ## Granted, when I wrote the RDS code for PAKs, PakNoData's position fields were only meant to support RDS's eager parsing,
        ## while here, we lazily parse. Other reviewers will want to know that when they see this, why we want to access a private field from outside.
        # Save DATA section offset to make lazy parsing possible 
        data_start = metadata._resources_end
        if (metadata._resources_start - metadata._named_resources_start != toc.STRG or
                metadata._resources_end - metadata._resources_start != toc.RSHD or
                data_start + toc.DATA > size):
            raise FormatError('PAK sections exceed bounded archive')
        
        # Fetch resource metadata for future reference
        self.resources = []
        for entry in metadata.resources:
            if (entry.compressed not in (0, 1) or entry.size % 64 or
                    entry.offset + entry.size > toc.DATA):
                raise FormatError('Invalid PAK resource extent or flag')
            self.resources.append(Resource(int(entry.asset_id), entry.asset_type.encode('ascii'),
                entry.compressed, entry.size, self.path, data_start + entry.offset))

    @property
    def names(self):
        ## NOTE : I don't understand this function. Why not simply return the list of names in named_resources ?
        schema = next(field.subcon for field in PAKNoData.subcons if field.name == 'named_resources')
        return schema.build(self.metadata.named_resources, target_game=GAME)

    @names.setter
    def names(self, value):
        ## NOTE : Same as the getter above. What is schema and why is it obtained through the `next` of an iterator with only one element ? 
        from .rds_formats import parse_exact
        schema = next(field.subcon for field in PAKNoData.subcons if field.name == 'named_resources')
        self.metadata.named_resources = parse_exact(schema, value)

    def write(self, destination : Any, resources : List[Resource], clear : bool = False) -> None:
        """
        Writes the modeled PAK file into the filesystem

        Arguments :
        - destination : Path to the exported PAK file
        - resources : A list of resources to include in the PAK file
        - clear : Whether to clear all the names of named resources. Defaults to False
        """
        from .rds_directory import write_records
        resources = list(resources)
        records, offset = [], 0
        for resource in resources:
            records.append((resource, offset))
            offset += resource.size
        ## NOTE : I will have things to say about this function later
        write_records(self, destination, records, resources, clear)
