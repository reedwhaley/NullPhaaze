# FileProvider moved out of asset_manager in RDS 0.44. Boundary names here: NodFileProvider.
"""FileProvider moved out of asset_manager in RDS 0.44."""

from __future__ import annotations

try:
    from retro_data_structures.file_provider import FileProvider, IsoFileProvider, PathFileProvider
except ModuleNotFoundError:
    from retro_data_structures.asset_manager import FileProvider, IsoFileProvider, PathFileProvider

__all__ = ["FileProvider", "IsoFileProvider", "PathFileProvider", "NodFileProvider"]


class _NodStream:
    def __init__(self, stream):
        self.stream = stream

    def read(self, size=-1):
        return self.stream.read(None if size < 0 else size)

    def seek(self, offset, whence=0):
        return self.stream.seek(offset, whence)

    def tell(self):
        return self.stream.tell()

    def close(self):
        self.stream.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


class NodFileProvider(FileProvider):
    """Read Wii files through NOD; older RDS Wii streams misread sector boundaries."""

    def __init__(self, disc):
        self.disc = disc
        self.partition = disc.get_data_partition()
        self.names = self.partition.files()

    def is_file(self, name):
        return name in self.names

    def rglob(self, pattern):
        import fnmatch

        return (name for name in self.names if fnmatch.fnmatch(name, pattern))

    def open_binary(self, name):
        return _NodStream(self.partition.read_file(name))

    def read_binary(self, name):
        with self.open_binary(name) as stream:
            return stream.read()

    def get_dol(self):
        return self.partition.get_dol()

    def get_file_list(self):
        return list(self.names)
