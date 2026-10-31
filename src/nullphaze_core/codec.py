# This is the historical ctypes codec adapter retained as source compatibility. Active RDS
# exports use the dependency's compression path; this bundle ships no standalone codec DLL.
# Boundary names here: Codec.
"""Native MIT lzokay bridge with bounded LZO chunk envelopes."""
import ctypes
import os
import sys
from pathlib import Path
from .binary import Reader, FormatError, pack


class Codec:
    def __init__(self, path=None):
        filename = {'darwin': 'liblzokay.dylib', 'linux': 'liblzokay.so'}.get(sys.platform, 'lzokay.dll')
        default = Path(__file__).parent/'native'/filename
        if not default.is_file():
            default = Path(__file__).resolve().parents[2]/'artifacts/core-native/Release'/filename
        path = Path(path or os.environ.get('NULLPHAZE_CORE_CODEC', default)).resolve()
        self.path = path
        self.library = ctypes.CDLL(str(path))
        for name in ('compress_without_dict', 'decompress'):
            function = getattr(self.library, name)
            function.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int,
                                 ctypes.POINTER(ctypes.c_int)]
            function.restype = ctypes.c_int

    def _call(self, name, data, capacity):
        if not data or not 0 < capacity <= 256*1024**2:
            raise FormatError('Invalid codec buffer size')
        source = ctypes.create_string_buffer(data)
        destination = ctypes.create_string_buffer(capacity)
        written = ctypes.c_int()
        status = getattr(self.library, name)(source, len(data), destination, capacity, ctypes.byref(written))
        if status != 0 or not 0 <= written.value <= capacity:
            raise FormatError(f'LZO {name} failed: {status}')
        return destination.raw[:written.value]

    def compress(self, data):
        return self._call('compress_without_dict', data, len(data)+len(data)//16+128)

    def decode_chunks(self, encoded, expected):
        if not 0 <= expected <= 256*1024**2:
            raise FormatError('Decoded block exceeds limit')
        reader = Reader(encoded)
        result = bytearray()
        while reader.remaining:
            length = reader.number('h')
            if not length:
                raise FormatError('Zero-length LZO chunk')
            payload = reader.read(abs(length))
            block = self._call('decompress', payload, 16384) if length > 0 else payload
            if len(block) > 16384 or len(result)+len(block) > expected:
                raise FormatError('LZO chunk exceeds declared output')
            result.extend(block)
        if len(result) != expected:
            raise FormatError('Decoded block length mismatch')
        return bytes(result)

    def encode_chunks(self, data):
        result = bytearray()
        for offset in range(0, len(data), 16384):
            chunk = data[offset:offset+16384]
            encoded = self.compress(chunk)
            if len(encoded) < len(chunk):
                result.extend(pack('h', len(encoded))+encoded)
            else:
                result.extend(pack('h', -len(chunk))+chunk)
        return bytes(result)
