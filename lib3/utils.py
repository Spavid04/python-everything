import ctypes
from ctypes import wintypes
import datetime
import typing


WINDOWS_TICKS = int(1/10**-7)  # 10,000,000 (100 nanoseconds or .1 microseconds)
WINDOWS_EPOCH = datetime.datetime.strptime('1601-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
def FiletimeToDatetime(filetime: wintypes.FILETIME) -> datetime.datetime:
    quadword = (filetime.dwHighDateTime << 32) + filetime.dwLowDateTime
    return WINDOWS_EPOCH + datetime.timedelta(microseconds=quadword // 10)

def PtrToString(ptr: typing.Union[ctypes.c_char_p, ctypes.c_wchar_p], unicode: bool, size: int = -1) \
        -> typing.Optional[str]:
    if not ptr:
        return None

    if unicode:
        return ctypes.wstring_at(ptr, size)
    else:
        return ctypes.string_at(ptr, size)
