"""Source-only x64 codec roundtrips and bounded-failure checks."""
from pathlib import Path
import random
import sys
import hashlib
import json
import ctypes
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'src'))
from nullphaaze_core.codec import Codec
from nullphaaze_core.binary import FormatError


def main():
    codec = Codec()
    rng = random.Random(16001)
    count = 0
    for size in (1, 2, 3, 16, 255, 256, 1024, 16383, 16384, 20000):
        for data in (bytes(size), bytes(i % 251 for i in range(size)), rng.randbytes(size)):
            assert codec.decode_chunks(codec.encode_chunks(data), size) == data
            count += 1
    for encoded, expected in [(b'\0\0', 1), (b'\0\1\0', 1), (b'\xff\xff', 1), (b'\xff\xffX', 0)]:
        try:
            codec.decode_chunks(encoded, expected)
        except FormatError:
            pass
        else:
            raise AssertionError('Malformed codec record accepted')
    try:
        codec._call('compress_without_dict', bytes(32), 1)
    except FormatError:
        pass
    else:
        raise AssertionError('Undersized destination accepted')
    print(f'PASS {count} x64 codec roundtrips and five bounded-failure cases; no original binary used')
    evidence = Path(__file__).resolve().parent.parent/'evidence'
    evidence.mkdir(exist_ok=True)
    (evidence/'core-codec-validation.json').write_text(json.dumps(dict(passed=True, roundtrips=count,
        malformedCases=4, capacityCases=1, processBits=ctypes.sizeof(ctypes.c_void_p)*8,
        codecSha256=hashlib.sha256(codec.path.read_bytes()).hexdigest(), originalBinaryUsed=False), indent=2)+'\n')


if __name__ == '__main__':
    main()
