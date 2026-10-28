"""Bounded binary primitives. All offsets and counts are checked before use."""
from typing import Any
import struct


class FormatError(ValueError):
    """
    An error to be raised when encountering a parsing error
    """
    pass


def pad(data : Any, alignment : int, fill : int = 0) -> bytes:
    """
    Pads binary data to align to a certain length

    Arguments:
    - data : The bytes to be aligned
    - alignment : Which number the final length should be a multiple of
    Keyword arguments:
    - fill : Which value should padding bytes be at. 0 by default
    """
    return bytes(data)+bytes([fill])*((-len(data)) % alignment)


def pack(fmt : str, *values) -> bytes:
    """
    A shorthand call to `struct.pack` for big-endian data

    Arguments:
    - fmt : The `struct` format string to use
    - *values : Any other values to call `struct.pack` with
    Raises :
    - FormatError if `struct.pack` raises an error
    """
    try:
        return struct.pack('>'+fmt, *values)
    except struct.error as error:
        raise FormatError(str(error)) from error


class Reader:
    """
    Provides a stream interface to read the given bytes
    """
    def __init__(self, data : Any) -> Reader:
        self.data = memoryview(data)
        self.pos = 0

    @property
    def remaining(self) -> int:
        """How many bytes until end of stream"""
        return len(self.data)-self.pos

    def read(self, count : int) -> bytes:
        """
        Read the given amount of bytes from the stream

        Arguments :
        - count : amount of bytes to read
        Raises :
        - FormatError when count < 0 or count > `self.remaining()`
        """
        if count < 0 or count > self.remaining:
            raise FormatError(f'Truncated record at {self.pos}: need {count}, have {self.remaining}')
        result = self.data[self.pos:self.pos+count].tobytes()
        self.pos += count
        return result

    def number(self, fmt : str) -> int:
        """
        Reads the next specified format as a big-endian number
        Consumes the stream in the same way as `self.read()`

        Arguments:
        - fmt : The `struct` format string to use
        """
        return struct.unpack('>'+fmt, self.read(struct.calcsize('>'+fmt)))[0]

    def u8(self) -> int: 
        """
        Reads the next unsigned byte
        Consumes the stream in the same way as `self.read()`
        """
        return self.number('B')

    def u16(self) -> int: 
        """
        Reads the next unsigned short
        Consumes the stream in the same way as `self.read()`
        """
        return self.number('H')

    def u32(self) -> int: 
        """
        Reads the next unsigned int
        Consumes the stream in the same way as `self.read()`
        """
        return self.number('I')

    def u64(self) -> int: 
        """
        Reads the next unsigned long
        Consumes the stream in the same way as `self.read()`
        """
        return self.number('Q')

    def count(self, stride : int, width : int = 4) -> int:
        """
        Reads the next integer of specified width and checks if it counts the amount of 
        patterns of length stride.
        Only reads and consumes the specified width

        Arguments:
        - stride : The width of the repeating pattern to check for
        Keyword arguments:
        - width : The width of the integer to read. Only accepts 2 or 4. 4 by default
        Raises:
        - FormatError if the repeated patter is longer than the remaining data
        """
        count = self.number({2: 'H', 4: 'I'}[width])
        if count > self.remaining//stride:
            raise FormatError(f'Count {count} exceeds bounded record')
        return count

    def align(self, alignment : int) -> bytes:
        """
        Reads the stream until in the specified alignment

        Arguments:
        - alignment : the alignment which needs to be met
        """
        return self.read((-self.pos) % alignment)

    def cstring(self) -> str:
        """
        Reads a null-terminated string

        Raises :
        - Format error if string is not terminated before end of stream
        """
        start = self.pos
        while self.remaining:
            if self.u8() == 0:
                return self.data[start:self.pos-1].tobytes().decode('utf-8')
        raise FormatError('Unterminated string')
