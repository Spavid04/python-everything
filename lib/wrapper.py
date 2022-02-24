from . import utils
from .c_defines import *
from .c_functions import *

import ctypes
from ctypes import wintypes
import datetime
import typing


#region commons
def __GetOptionalInt_common(func: typing.Callable) -> typing.Optional[int]:
    result = func()
    if result == 0:
        return None
    return result

def __GetResultDate_common(func: typing.Callable, index: int) -> typing.Optional[datetime.datetime]:
    filetime = wintypes.FILETIME()
    result = func(index, ctypes.byref(filetime))
    if result == 0:
        return None
    return utils.FiletimeToDatetime(filetime)
#endregion

def CleanUp():
    Everything_CleanUp()

def DeleteRunHistory() -> bool:
    return bool(Everything_DeleteRunHistory())

def Exit() -> bool:
    return bool(Everything_Exit())

def GetBuildNumber() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetBuildNumber)

def GetLastError() -> Status:
    return Status(Everything_GetLastError())

def GetMajorVersion() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetMajorVersion)

def GetMatchCase() -> bool:
    return bool(Everything_GetMatchCase())

def GetMatchPath() -> bool:
    return bool(Everything_GetMatchPath())

def GetMatchWholeWord() -> bool:
    return bool(Everything_GetMatchWholeWord())

def GetMax() -> int:
    return Everything_GetMax()

def GetMinorVersion() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetMinorVersion)

def GetNumFileResults() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetNumFileResults)

def GetNumFolderResults() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetNumFolderResults)

def GetNumResults() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetNumResults)

def GetOffset() -> int:
    return Everything_GetOffset()

def GetRegex() -> bool:
    return bool(Everything_GetRegex())

def GetReplyID() -> int:
    return Everything_GetReplyID()

def GetReplyWindow() -> wintypes.HWND:
    return Everything_GetReplyWindow()

def GetRequestFlags() -> typing.Optional[RequestFlags]:
    result = __GetOptionalInt_common(Everything_GetRequestFlags)
    if not result:
        return None
    return RequestFlags(result)

def GetResultAttributes(index: int) -> typing.Optional[FileAttributes]:
    result = Everything_GetResultAttributes(index)
    if result == INVALID_FILE_ATTRIBUTES:
        return None
    return FileAttributes(result)

def GetResultDateAccessed(index: int) -> typing.Optional[datetime.datetime]:
    return __GetResultDate_common(Everything_GetResultDateAccessed, index)

def GetResultDateCreated(index: int) -> typing.Optional[datetime.datetime]:
    return __GetResultDate_common(Everything_GetResultDateCreated, index)

def GetResultDateModified(index: int) -> typing.Optional[datetime.datetime]:
    return __GetResultDate_common(Everything_GetResultDateModified, index)

def GetResultDateRecentlyChanged(index: int) -> typing.Optional[datetime.datetime]:
    return __GetResultDate_common(Everything_GetResultDateRecentlyChanged, index)

def GetResultDateRun(index: int) -> typing.Optional[datetime.datetime]:
    return __GetResultDate_common(Everything_GetResultDateRun, index)

def GetResultExtension(index: int, unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetResultExtensionW if unicode else Everything_GetResultExtensionA
    return utils.PtrToString(func(index), unicode)

def GetResultFileListFileName(index: int, unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetResultFileListFileNameW if unicode else Everything_GetResultFileListFileNameA
    return utils.PtrToString(func(index), unicode)

def GetResultFileName(index: int, unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetResultFileNameW if unicode else Everything_GetResultFileNameA
    return utils.PtrToString(func(index), unicode)

def GetResultFullPathName(index: int, unicode: bool = True, maxLength: int = 260) -> typing.Optional[typing.Union[str, int]]:
    if maxLength == 0:
        func = Everything_GetResultFullPathNameA
        buffer = ctypes.c_char_p()
    elif unicode:
        func = Everything_GetResultFullPathNameW
        buffer = ctypes.create_unicode_buffer(maxLength + 1)
    else:
        func = Everything_GetResultFullPathNameA
        buffer = ctypes.create_string_buffer(maxLength + 1)

    result = func(index, buffer, maxLength + 1)
    if result == 0:
        return None
    elif maxLength == 0:
        return result
    else:
        if result == maxLength:
            # todo: possible truncation
            pass
        return utils.PtrToString(buffer, unicode)

def GetResultHighlightedFileName(index: int, unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetResultHighlightedFileNameW if unicode else Everything_GetResultHighlightedFileNameA
    return utils.PtrToString(func(index), unicode)

def GetResultHighlightedFullPathAndFileName(index: int, unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetResultHighlightedFullPathAndFileNameW if unicode else Everything_GetResultHighlightedFullPathAndFileNameA
    return utils.PtrToString(func(index), unicode)

def GetResultHighlightedPath(index: int, unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetResultHighlightedPathW if unicode else Everything_GetResultHighlightedPathA
    return utils.PtrToString(func(index), unicode)

def GetResultListRequestFlags() -> typing.Optional[RequestFlags]:
    result = __GetOptionalInt_common(Everything_GetResultListRequestFlags)
    if not result:
        return None
    return RequestFlags(result)

def GetResultListSort() -> typing.Optional[SortType]:
    result = __GetOptionalInt_common(Everything_GetResultListSort)
    if not result:
        return None
    return SortType(result)

def GetResultPath(index: int, unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetResultPathW if unicode else Everything_GetResultPathA
    return utils.PtrToString(func(index), unicode)

def GetResultRunCount(index: int) -> typing.Optional[int]:
    result = Everything_GetResultRunCount(index)
    if result == 0:
        return None
    return result

def GetResultSize(index: int) -> typing.Optional[int]:
    li = wintypes.LARGE_INTEGER()
    result = Everything_GetResultSize(index, ctypes.byref(li))
    if result == 0:
        return None
    return li.value

def GetRevision() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetRevision)

def GetRunCountFromFileName(filename: str, unicode: bool = True) -> typing.Optional[int]:
    func = Everything_GetRunCountFromFileNameW if unicode else Everything_GetRunCountFromFileNameA
    result = func(filename)
    if result == 0:
        return None
    return result

def GetSearch(unicode: bool = True) -> typing.Optional[str]:
    func = Everything_GetSearchW if unicode else Everything_GetSearchA
    return utils.PtrToString(func(), unicode)

def GetSort() -> typing.Optional[SortType]:
    result = __GetOptionalInt_common(Everything_GetSort)
    if not result:
        return None
    return SortType(result)

def GetTargetMachine() -> TargetMachine:
    result = __GetOptionalInt_common(Everything_GetTargetMachine)
    return TargetMachine(result)

def GetTotFileResults() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetTotFileResults)

def GetTotFolderResults() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetTotFolderResults)

def GetTotResults() -> typing.Optional[int]:
    return __GetOptionalInt_common(Everything_GetTotResults)

def IncRunCountFromFileName(filename: str, unicode: bool = True) -> typing.Optional[int]:
    func = Everything_IncRunCountFromFileNameW if unicode else Everything_IncRunCountFromFileNameA
    result = func(filename)
    if result == 0:
        return None
    return result

def IsAdmin() -> bool:
    return bool(Everything_IsAdmin())

def IsAppData() -> bool:
    return bool(Everything_IsAppData())

def IsDBLoaded() -> bool:
    return bool(Everything_IsDBLoaded())

def IsFileResult(index: int) -> bool:
    return bool(Everything_IsFileResult(index))

def IsFolderResult(index: int) -> bool:
    return bool(Everything_IsFolderResult(index))

def IsQueryReply(message: int, w: wintypes.WPARAM, l: wintypes.LPARAM, replyId: int) -> bool:
    return bool(Everything_IsQueryReply(message, w, l, replyId))

def IsVolumeResult(index: int) -> bool:
    return bool(Everything_IsVolumeResult(index))

def Query(wait: bool = True, unicode: bool = True) -> bool:
    func = Everything_QueryW if unicode else Everything_QueryA
    return bool(func(wait))

def RebuildDB() -> bool:
    return bool(Everything_RebuildDB())

def Reset():
    Everything_Reset()

def SaveDB() -> bool:
    return bool(Everything_SaveDB())

def SaveRunHistory() -> bool:
    return bool(Everything_SaveRunHistory())

def SetMatchCase(caseSensitive: bool):
    Everything_SetMatchCase(int(caseSensitive))

def SetMatchPath(fullMatch: bool):
    Everything_SetMatchPath(int(fullMatch))

def SetMatchWholeWord(wholeWord: bool):
    Everything_SetMatchWholeWord(int(wholeWord))

def SetMax(maxResults: int = -1):
    Everything_SetMax(maxResults)

def SetOffset(offset: int = 0):
    Everything_SetOffset(offset)

def SetRegex(regexMatch: bool):
    Everything_SetRegex(int(regexMatch))

def SetReplyID(replyId: int):
    Everything_SetReplyID(replyId)

def SetReplyWindow(replyWindow: wintypes.HWND):
    Everything_SetReplyWindow(replyWindow)

def SetRequestFlags(requestFlags: RequestFlags):
    Everything_SetRequestFlags(int(requestFlags))

def SetRunCountFromFileName(filename: str, runCount: int, unicode: bool = True) -> bool:
    func = Everything_SetRunCountFromFileNameW if unicode else Everything_SetRunCountFromFileNameA
    return bool(func(filename, runCount))

def SetSearch(string: str, unicode: bool = True):
    func = Everything_SetSearchW if unicode else Everything_SetSearchA
    func(string)

def SetSort(sortType: SortType):
    Everything_SetSort(int(sortType))

def SortResultsByPath():
    Everything_SortResultsByPath()

def UpdateAllFolderIndexes() -> bool:
    return bool(Everything_UpdateAllFolderIndexes())
