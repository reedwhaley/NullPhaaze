"""Own staged outputs only; immutable inputs and exclusive publication on Windows, macOS and Linux."""
import ctypes
import sys
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
from .binary import FormatError


def checksum(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def reject_links(path):
    for item in (path, *path.parents):
        if item.is_symlink() or getattr(item, 'is_junction', lambda: False)():
            raise FormatError('Input/output paths must not traverse links or junctions')


def rename_exclusive(source, destination):
    if sys.platform == 'win32':
        # Windows rename refuses existing files and directories atomically.
        os.rename(source, destination)
    elif sys.platform == 'darwin':
        # Darwin RENAME_EXCL prevents replacement even for an empty directory.
        # Never fall back to POSIX rename: it could overwrite a competing export.
        library = ctypes.CDLL(None, use_errno=True)
        function = library.renamex_np
        function.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
        function.restype = ctypes.c_int
        if function(os.fsencode(source), os.fsencode(destination), 0x00000004):
            error = ctypes.get_errno()
            raise OSError(error, os.strerror(error), str(destination))
    elif sys.platform == 'linux':
        # glibc renameat2 + RENAME_NOREPLACE preserves competing destinations.
        # Unsupported libc/filesystems fail closed; never fall back to rename.
        library = ctypes.CDLL(None, use_errno=True)
        function = library.renameat2
        function.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int,
                             ctypes.c_char_p, ctypes.c_uint]
        function.restype = ctypes.c_int
        if function(-100, os.fsencode(source), -100, os.fsencode(destination), 1):
            error = ctypes.get_errno()
            raise OSError(error, os.strerror(error), str(destination))
    else:
        raise FormatError('Exclusive directory publication supports Windows, macOS and Linux only')


class Session:
    def __init__(self, source, output):
        source, output = Path(source).absolute(), Path(output).absolute()
        reject_links(source)
        reject_links(output)
        self.source, self.output = source.resolve(), output.resolve()
        if self.source == self.output or self.source in self.output.parents or self.output in self.source.parents:
            raise FormatError('Input and output directories must be separate')
        if not self.source.is_dir() or not self.output.parent.is_dir():
            raise FormatError('Input directory and output parent must exist')
        if self.output.exists():
            raise FileExistsError('Choose a new output directory')
        self.staging = None
        self.committed = False

    def __enter__(self):
        self.staging = Path(tempfile.mkdtemp(prefix='.nullphaaze-core-', suffix='.staging', dir=self.output.parent))
        return self

    def commit(self):
        rename_exclusive(self.staging, self.output)
        self.committed = True

    def __exit__(self, exception_type, exception, traceback):
        if self.committed or self.staging is None:
            return
        if self.staging.parent != self.output.parent or not self.staging.name.startswith('.nullphaaze-core-'):
            raise RuntimeError('Refusing cleanup outside the owned staging directory')
        reject_links(self.staging)
        shutil.rmtree(self.staging)


def verified_inputs(source):
    manifest = json.loads((Path(__file__).parent/'data/inputs.json').read_text())
    results = {}
    for name, expected in manifest.items():
        path = source/name
        reject_links(path)
        if path.stat().st_size != expected['bytes'] or checksum(path) != expected['sha256']:
            raise FormatError('Input does not match verified USA revision 0: '+name)
        results[name] = {'size': path.stat().st_size, 'mtime': path.stat().st_mtime_ns, 'sha256': expected['sha256']}
    return results
