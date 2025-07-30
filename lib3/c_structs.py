# This file contains definitions for some Everything structs
# It is *not* automatically generated

import ctypes
from ctypes import wintypes


class UInt128(ctypes.Structure):
    _fields_ = [
        ("bytes", ctypes.c_byte * 16)
    ]

class Dimensions(ctypes.Structure):
    _fields_ = [
        ("width", wintypes.DWORD),
        ("height", wintypes.DWORD)
    ]
