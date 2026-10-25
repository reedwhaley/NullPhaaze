"""Capacity for user-requested exports; macOS may reclaim purgeable storage."""
import ctypes
import logging
import os
import shutil
import sys


def _macos_available_capacity(directory):
    """Query the selected volume via Apple's important-usage capacity API."""
    cf = ctypes.CDLL('/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation')
    pointer = ctypes.c_void_p
    cf.CFURLCreateFromFileSystemRepresentation.argtypes = [pointer, ctypes.c_char_p, ctypes.c_long, ctypes.c_bool]
    cf.CFURLCreateFromFileSystemRepresentation.restype = pointer
    cf.CFURLCopyResourcePropertyForKey.argtypes = [pointer, pointer, ctypes.POINTER(pointer), ctypes.POINTER(pointer)]
    cf.CFURLCopyResourcePropertyForKey.restype = ctypes.c_bool
    cf.CFNumberGetTypeID.restype = ctypes.c_ulong
    cf.CFGetTypeID.argtypes = [pointer]
    cf.CFGetTypeID.restype = ctypes.c_ulong
    cf.CFNumberGetValue.argtypes = [pointer, ctypes.c_int, pointer]
    cf.CFNumberGetValue.restype = ctypes.c_bool
    cf.CFRelease.argtypes = [pointer]
    cf.CFRelease.restype = None
    key = pointer.in_dll(cf, 'kCFURLVolumeAvailableCapacityForImportantUsageKey')
    path = os.fsencode(os.path.realpath(directory))
    url = cf.CFURLCreateFromFileSystemRepresentation(None, path, len(path), True)
    if not url:
        raise OSError('Could not create output-volume URL')
    value, error = pointer(), pointer()
    try:
        if not cf.CFURLCopyResourcePropertyForKey(url, key, ctypes.byref(value), ctypes.byref(error)) or not value:
            raise OSError('macOS did not provide important-usage capacity')
        if cf.CFGetTypeID(value) != cf.CFNumberGetTypeID():
            raise ValueError('macOS returned a nonnumeric capacity')
        result = ctypes.c_int64()
        if not cf.CFNumberGetValue(value, 4, ctypes.byref(result)) or result.value < 0:  # kCFNumberSInt64Type
            raise ValueError('macOS returned an invalid capacity')
        return result.value
    finally:
        for reference in (value, error, url):
            if reference:
                cf.CFRelease(reference)


def available_bytes(directory):
    usage = shutil.disk_usage(directory)
    if sys.platform == 'darwin':
        try:
            capacity = _macos_available_capacity(directory)
            if not isinstance(capacity, int) or not 0 <= capacity <= usage.total:
                raise ValueError('macOS capacity is outside the volume size')
            logging.getLogger(__name__).info(
                'Export capacity: immediately free=%s, available for important usage=%s bytes', usage.free, capacity)
            return capacity
        except (OSError, ValueError, AttributeError):
            logging.getLogger(__name__).warning('macOS capacity query failed; using immediately free space', exc_info=True)
    return usage.free
