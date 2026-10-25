"""Bounded binary primitives. All offsets and counts are checked before use."""
import struct


class FormatError(ValueError):
    pass


def pad(data, alignment, fill=0):
    return bytes(data)+bytes([fill])*((-len(data)) % alignment)


def pack(fmt, *values):
    try:
        return struct.pack('>'+fmt, *values)
    except struct.error as error:
        raise FormatError(str(error)) from error


class Reader:
    def __init__(self, data):
        self.data = memoryview(data)
        self.pos = 0

    @property
    def remaining(self):
        return len(self.data)-self.pos

    def read(self, count):
        if count < 0 or count > self.remaining:
            raise FormatError(f'Truncated record at {self.pos}: need {count}, have {self.remaining}')
        result = self.data[self.pos:self.pos+count].tobytes()
        self.pos += count
        return result

    def number(self, fmt):
        return struct.unpack('>'+fmt, self.read(struct.calcsize('>'+fmt)))[0]

    def u8(self): return self.number('B')
    def u16(self): return self.number('H')
    def u32(self): return self.number('I')
    def u64(self): return self.number('Q')

    def count(self, stride, width=4):
        count = self.number({2: 'H', 4: 'I'}[width])
        if count > self.remaining//stride:
            raise FormatError(f'Count {count} exceeds bounded record')
        return count

    def align(self, alignment):
        return self.read((-self.pos) % alignment)

    def cstring(self):
        start = self.pos
        while self.remaining:
            if self.u8() == 0:
                return self.data[start:self.pos-1].tobytes().decode('utf-8')
        raise FormatError('Unterminated string')
