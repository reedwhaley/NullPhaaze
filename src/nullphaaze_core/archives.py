"""
Streaming Wii PAK tables with explicit resource aliases and bounded reads.
See https://wiki.axiodl.com/w/PAK_(Metroid_Prime_3)
"""
from dataclasses import dataclass, replace
from pathlib import Path
import struct
from .binary import Reader, FormatError, pad, pack


@dataclass(frozen=True)
class Resource:
    """
    Represents an individual, unparsed resource in a PAK file.
    Resource data is not immediately loaded into memory, so it must be read before use
    """
    identity: int
    """The resource's ResourceId"""
    kind: bytes
    """The FourCC representing the resource's type (MREA, MLVL, etc...)"""
    compressed: int
    """Whether the resource is compressed via LZO"""
    size: int
    """The size of the resource in the PAK. Accounts for padding, so always a multiple of 64"""
    source: Path | None = None
    """The path to the PAK file from whence the resource comes from"""
    offset: int = 0
    """The offset of the resource's start relative to the start of the file (as opposed to the start of the DATA section)"""
    data: bytes | None = None
    """Memoized data after the first read"""

    def read(self):
        """
        Reads the raw bytes from the resource

        Raises :
        - FormatError if expected size and read result size are mismatched
        """
        # If we already have memoized data, directly return it
        if self.data is not None:
            return self.data
        # Otherwise, read from the source file and memoize the result if ok
        with self.source.open('rb') as stream:
            stream.seek(self.offset)
            result = stream.read(self.size)
        if len(result) != self.size:
            raise FormatError('Resource source changed or is truncated')
        # TODO : self.data = result
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

    def copy_to(self, destination, streams):
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
        # TODO : replace whatever this is with `destination.write(self.read())`
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
    Represents a Metroid Prime 3 : Corruption PAK file
    """
    # TODO : declare the fields set by the constructor here
    def __init__(self, path):
        # Initialize file data from filesystem
        self.path = Path(path)
        size = self.path.stat().st_size

        # TODO : declare `names` and `tables` here
        with self.path.open('rb') as stream:
            # Read header data
            header = stream.read(128)
            if len(header) != 128:
                raise FormatError('Truncated PAK header')

            # Check table of contents format
            if header[68:72] != b'STRG' or header[76:80] != b'RSHD' or header[84:88] != b'DATA':
                raise FormatError('Invalid PAK section table')

            # Read table of contents data
            name_size = struct.unpack_from('>I', header, 72)[0]
            table_size = struct.unpack_from('>I', header, 80)[0]
            data_size = struct.unpack_from('>I', header, 88)[0]

            # Check whether section sizes are consistent with table of contents data and general size
            if name_size % 64 or table_size % 64 or 128+name_size+table_size+data_size > size:
                raise FormatError('PAK sections exceed bounded archive')

            # Read named resources and resource table sections
            ## Note : I don't like that these variables are declared here, to be used right after this span ends.
            ## When you declare a variable, it is good practice not to bring it above the span in which you declared it
            ## This helps avoid unintended side effects when rewriting code. 
            ## Some programming languages, like Rust or OCaml, even enforce this practice.
            names = stream.read(name_size)
            table = Reader(stream.read(table_size))

        self.header = header[:64]

        # Parse named resources
        ## Note : This does litterally nothing. We have already read and stored the named resources section in `names`
        ## What this does is consume each named resource entry (without storing their values might I add), so that 
        ## once we're done, we reach the end of the section minus the padding, only to add it back one line later.
        ## We've essentially parsed bytes back into bytes by splitting it into parts and then adding them back together
        # TODO : Delete this
        named = Reader(names)
        for _ in range(named.count(13)):
            named.cstring()
            named.read(12)
        self.names = pad(names[:named.pos], 64)

        # Parse resource table
        self.resources = []
        for _ in range(table.count(24)):
            flag, kind, identity, length, offset = struct.unpack('>I4sQII', table.read(24))
            if flag not in (0, 1) or length % 64 or offset+length > data_size:
                raise FormatError('Invalid PAK resource extent or flag')
            self.resources.append(Resource(identity, kind, flag, length, self.path, 128+name_size+table_size+offset))

    def write(self, destination, resources, clear=False):
        """
        Write a given list of resources into a PAK file

        Arguments :
        - destination : the path towards the file in which to write the PAK
        - resources : the list of resources to write

        Keyword arguments :
        - clear : Whether names for named resources should be cleared. False by default

        Raises :
        - FormatError if a resource is fomratted incorrectly
        """
        names = pad(pack('I', 0), 64) if clear else self.names
        table = bytearray(pack('I', len(resources)))
        offset = 0

        # Pack all resource metadata into the resource table
        for resource in resources:
            if len(resource.kind) != 4 or resource.size % 64:
                raise FormatError('Invalid output resource metadata')
            table.extend(pack('I4sQII', resource.compressed, resource.kind, resource.identity, resource.size, offset))
            offset += resource.size
        table = pad(table, 64)
        toc = pad(pack('I4sI4sI4sI', 3, b'STRG', len(names), b'RSHD', len(table), b'DATA', offset), 64)

        # Write completed header info and resources themselves
        # TODO : Get rid of the streams dict once resource.copy_to has been fixed
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
