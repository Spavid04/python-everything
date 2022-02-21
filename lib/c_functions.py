import ctypes
from ctypes import wintypes
import os
import sys


def __dllimport(name):
    try:
        return ctypes.WinDLL(name)
    except FileNotFoundError:
        return ctypes.WinDLL(os.path.join(os.path.dirname(__file__), name))
if sys.maxsize > 2**32:
    __dll = __dllimport("Everything64.dll")
else:
    __dll = __dllimport("Everything32.dll")


Everything_SetSearchW = __dll.Everything_SetSearchW
Everything_SetSearchW.argtypes = [wintypes.LPCWSTR]
Everything_SetSearchW.restype = None

Everything_SetSearchA = __dll.Everything_SetSearchA
Everything_SetSearchA.argtypes = [wintypes.LPCSTR]
Everything_SetSearchA.restype = None

Everything_SetMatchPath = __dll.Everything_SetMatchPath
Everything_SetMatchPath.argtypes = [wintypes.BOOL]
Everything_SetMatchPath.restype = None

Everything_SetMatchCase = __dll.Everything_SetMatchCase
Everything_SetMatchCase.argtypes = [wintypes.BOOL]
Everything_SetMatchCase.restype = None

Everything_SetMatchWholeWord = __dll.Everything_SetMatchWholeWord
Everything_SetMatchWholeWord.argtypes = [wintypes.BOOL]
Everything_SetMatchWholeWord.restype = None

Everything_SetRegex = __dll.Everything_SetRegex
Everything_SetRegex.argtypes = [wintypes.BOOL]
Everything_SetRegex.restype = None

Everything_SetMax = __dll.Everything_SetMax
Everything_SetMax.argtypes = [wintypes.DWORD]
Everything_SetMax.restype = None

Everything_SetOffset = __dll.Everything_SetOffset
Everything_SetOffset.argtypes = [wintypes.DWORD]
Everything_SetOffset.restype = None

Everything_SetReplyWindow = __dll.Everything_SetReplyWindow
Everything_SetReplyWindow.argtypes = [wintypes.HWND]
Everything_SetReplyWindow.restype = None

Everything_SetReplyID = __dll.Everything_SetReplyID
Everything_SetReplyID.argtypes = [wintypes.DWORD]
Everything_SetReplyID.restype = None

Everything_SetSort = __dll.Everything_SetSort
Everything_SetSort.argtypes = [wintypes.DWORD]
Everything_SetSort.restype = None

Everything_SetRequestFlags = __dll.Everything_SetRequestFlags
Everything_SetRequestFlags.argtypes = [wintypes.DWORD]
Everything_SetRequestFlags.restype = None


Everything_GetMatchPath = __dll.Everything_GetMatchPath
Everything_GetMatchPath.argtypes = []
Everything_GetMatchPath.restype = wintypes.BOOL

Everything_GetMatchCase = __dll.Everything_GetMatchCase
Everything_GetMatchCase.argtypes = []
Everything_GetMatchCase.restype = wintypes.BOOL

Everything_GetMatchWholeWord = __dll.Everything_GetMatchWholeWord
Everything_GetMatchWholeWord.argtypes = []
Everything_GetMatchWholeWord.restype = wintypes.BOOL

Everything_GetRegex = __dll.Everything_GetRegex
Everything_GetRegex.argtypes = []
Everything_GetRegex.restype = wintypes.BOOL

Everything_GetMax = __dll.Everything_GetMax
Everything_GetMax.argtypes = []
Everything_GetMax.restype = wintypes.DWORD

Everything_GetOffset = __dll.Everything_GetOffset
Everything_GetOffset.argtypes = []
Everything_GetOffset.restype = wintypes.DWORD

Everything_GetSearchA = __dll.Everything_GetSearchA
Everything_GetSearchA.argtypes = []
Everything_GetSearchA.restype = wintypes.LPCSTR

Everything_GetSearchW = __dll.Everything_GetSearchW
Everything_GetSearchW.argtypes = []
Everything_GetSearchW.restype = wintypes.LPCWSTR

Everything_GetLastError = __dll.Everything_GetLastError
Everything_GetLastError.argtypes = []
Everything_GetLastError.restype = wintypes.DWORD

Everything_GetReplyWindow = __dll.Everything_GetReplyWindow
Everything_GetReplyWindow.argtypes = []
Everything_GetReplyWindow.restype = wintypes.HWND

Everything_GetReplyID = __dll.Everything_GetReplyID
Everything_GetReplyID.argtypes = []
Everything_GetReplyID.restype = wintypes.DWORD

Everything_GetSort = __dll.Everything_GetSort
Everything_GetSort.argtypes = []
Everything_GetSort.restype = wintypes.DWORD

Everything_GetRequestFlags = __dll.Everything_GetRequestFlags
Everything_GetRequestFlags.argtypes = []
Everything_GetRequestFlags.restype = wintypes.DWORD


Everything_QueryA = __dll.Everything_QueryA
Everything_QueryA.argtypes = [wintypes.BOOL]
Everything_QueryA.restype = wintypes.BOOL

Everything_QueryW = __dll.Everything_QueryW
Everything_QueryW.argtypes = [wintypes.BOOL]
Everything_QueryW.restype = wintypes.BOOL


Everything_IsQueryReply = __dll.Everything_IsQueryReply
Everything_IsQueryReply.argtypes = [wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM, wintypes.DWORD]
Everything_IsQueryReply.restype = wintypes.BOOL


Everything_SortResultsByPath = __dll.Everything_SortResultsByPath
Everything_SortResultsByPath.argtypes = []
Everything_SortResultsByPath.restype = None


Everything_GetNumFileResults = __dll.Everything_GetNumFileResults
Everything_GetNumFileResults.argtypes = []
Everything_GetNumFileResults.restype = wintypes.DWORD

Everything_GetNumFolderResults = __dll.Everything_GetNumFolderResults
Everything_GetNumFolderResults.argtypes = []
Everything_GetNumFolderResults.restype = wintypes.DWORD

Everything_GetNumResults = __dll.Everything_GetNumResults
Everything_GetNumResults.argtypes = []
Everything_GetNumResults.restype = wintypes.DWORD

Everything_GetTotFileResults = __dll.Everything_GetTotFileResults
Everything_GetTotFileResults.argtypes = []
Everything_GetTotFileResults.restype = wintypes.DWORD

Everything_GetTotFolderResults = __dll.Everything_GetTotFolderResults
Everything_GetTotFolderResults.argtypes = []
Everything_GetTotFolderResults.restype = wintypes.DWORD

Everything_GetTotResults = __dll.Everything_GetTotResults
Everything_GetTotResults.argtypes = []
Everything_GetTotResults.restype = wintypes.DWORD

Everything_IsVolumeResult = __dll.Everything_IsVolumeResult
Everything_IsVolumeResult.argtypes = [wintypes.DWORD]
Everything_IsVolumeResult.restype = wintypes.BOOL

Everything_IsFolderResult = __dll.Everything_IsFolderResult
Everything_IsFolderResult.argtypes = [wintypes.DWORD]
Everything_IsFolderResult.restype = wintypes.BOOL

Everything_IsFileResult = __dll.Everything_IsFileResult
Everything_IsFileResult.argtypes = [wintypes.DWORD]
Everything_IsFileResult.restype = wintypes.BOOL

Everything_GetResultFileNameW = __dll.Everything_GetResultFileNameW
Everything_GetResultFileNameW.argtypes = [wintypes.DWORD]
Everything_GetResultFileNameW.restype = wintypes.LPCWSTR

Everything_GetResultFileNameA = __dll.Everything_GetResultFileNameA
Everything_GetResultFileNameA.argtypes = [wintypes.DWORD]
Everything_GetResultFileNameA.restype = wintypes.LPCSTR

Everything_GetResultPathW = __dll.Everything_GetResultPathW
Everything_GetResultPathW.argtypes = [wintypes.DWORD]
Everything_GetResultPathW.restype = wintypes.LPCWSTR

Everything_GetResultPathA = __dll.Everything_GetResultPathA
Everything_GetResultPathA.argtypes = [wintypes.DWORD]
Everything_GetResultPathA.restype = wintypes.LPCSTR

Everything_GetResultFullPathNameA = __dll.Everything_GetResultFullPathNameA
Everything_GetResultFullPathNameA.argtypes = [wintypes.DWORD, wintypes.LPSTR, wintypes.DWORD]
Everything_GetResultFullPathNameA.restype = wintypes.DWORD

Everything_GetResultFullPathNameW = __dll.Everything_GetResultFullPathNameW
Everything_GetResultFullPathNameW.argtypes = [wintypes.DWORD, wintypes.LPWSTR, wintypes.DWORD]
Everything_GetResultFullPathNameW.restype = wintypes.DWORD

Everything_GetResultListSort = __dll.Everything_GetResultListSort
Everything_GetResultListSort.argtypes = []
Everything_GetResultListSort.restype = wintypes.DWORD

Everything_GetResultListRequestFlags = __dll.Everything_GetResultListRequestFlags
Everything_GetResultListRequestFlags.argtypes = []
Everything_GetResultListRequestFlags.restype = wintypes.DWORD

Everything_GetResultExtensionW = __dll.Everything_GetResultExtensionW
Everything_GetResultExtensionW.argtypes = [wintypes.DWORD]
Everything_GetResultExtensionW.restype = wintypes.LPCWSTR

Everything_GetResultExtensionA = __dll.Everything_GetResultExtensionA
Everything_GetResultExtensionA.argtypes = [wintypes.DWORD]
Everything_GetResultExtensionA.restype = wintypes.LPCSTR

Everything_GetResultSize = __dll.Everything_GetResultSize
Everything_GetResultSize.argtypes = [wintypes.DWORD, wintypes.PLARGE_INTEGER]
Everything_GetResultSize.restype = wintypes.BOOL

Everything_GetResultDateCreated = __dll.Everything_GetResultDateCreated
Everything_GetResultDateCreated.argtypes = [wintypes.DWORD, wintypes.LPFILETIME]
Everything_GetResultDateCreated.restype = wintypes.BOOL

Everything_GetResultDateModified = __dll.Everything_GetResultDateModified
Everything_GetResultDateModified.argtypes = [wintypes.DWORD, wintypes.LPFILETIME]
Everything_GetResultDateModified.restype = wintypes.BOOL

Everything_GetResultDateAccessed = __dll.Everything_GetResultDateAccessed
Everything_GetResultDateAccessed.argtypes = [wintypes.DWORD, wintypes.LPFILETIME]
Everything_GetResultDateAccessed.restype = wintypes.BOOL

Everything_GetResultAttributes = __dll.Everything_GetResultAttributes
Everything_GetResultAttributes.argtypes = [wintypes.DWORD]
Everything_GetResultAttributes.restype = wintypes.DWORD

Everything_GetResultFileListFileNameW = __dll.Everything_GetResultFileListFileNameW
Everything_GetResultFileListFileNameW.argtypes = [wintypes.DWORD]
Everything_GetResultFileListFileNameW.restype = wintypes.LPCWSTR

Everything_GetResultFileListFileNameA = __dll.Everything_GetResultFileListFileNameA
Everything_GetResultFileListFileNameA.argtypes = [wintypes.DWORD]
Everything_GetResultFileListFileNameA.restype = wintypes.LPCSTR

Everything_GetResultRunCount = __dll.Everything_GetResultRunCount
Everything_GetResultRunCount.argtypes = [wintypes.DWORD]
Everything_GetResultRunCount.restype = wintypes.DWORD

Everything_GetResultDateRun = __dll.Everything_GetResultDateRun
Everything_GetResultDateRun.argtypes = [wintypes.DWORD, wintypes.LPFILETIME]
Everything_GetResultDateRun.restype = wintypes.BOOL

Everything_GetResultDateRecentlyChanged = __dll.Everything_GetResultDateRecentlyChanged
Everything_GetResultDateRecentlyChanged.argtypes = [wintypes.DWORD, wintypes.LPFILETIME]
Everything_GetResultDateRecentlyChanged.restype = wintypes.BOOL

Everything_GetResultHighlightedFileNameW = __dll.Everything_GetResultHighlightedFileNameW
Everything_GetResultHighlightedFileNameW.argtypes = [wintypes.DWORD]
Everything_GetResultHighlightedFileNameW.restype = wintypes.LPCWSTR

Everything_GetResultHighlightedFileNameA = __dll.Everything_GetResultHighlightedFileNameA
Everything_GetResultHighlightedFileNameA.argtypes = [wintypes.DWORD]
Everything_GetResultHighlightedFileNameA.restype = wintypes.LPCSTR

Everything_GetResultHighlightedPathW = __dll.Everything_GetResultHighlightedPathW
Everything_GetResultHighlightedPathW.argtypes = [wintypes.DWORD]
Everything_GetResultHighlightedPathW.restype = wintypes.LPCWSTR

Everything_GetResultHighlightedPathA = __dll.Everything_GetResultHighlightedPathA
Everything_GetResultHighlightedPathA.argtypes = [wintypes.DWORD]
Everything_GetResultHighlightedPathA.restype = wintypes.LPCSTR

Everything_GetResultHighlightedFullPathAndFileNameW = __dll.Everything_GetResultHighlightedFullPathAndFileNameW
Everything_GetResultHighlightedFullPathAndFileNameW.argtypes = [wintypes.DWORD]
Everything_GetResultHighlightedFullPathAndFileNameW.restype = wintypes.LPCWSTR

Everything_GetResultHighlightedFullPathAndFileNameA = __dll.Everything_GetResultHighlightedFullPathAndFileNameA
Everything_GetResultHighlightedFullPathAndFileNameA.argtypes = [wintypes.DWORD]
Everything_GetResultHighlightedFullPathAndFileNameA.restype = wintypes.LPCSTR


Everything_Reset = __dll.Everything_Reset
Everything_Reset.argtypes = []
Everything_Reset.restype = None

Everything_CleanUp = __dll.Everything_CleanUp
Everything_CleanUp.argtypes = []
Everything_CleanUp.restype = None


Everything_GetMajorVersion = __dll.Everything_GetMajorVersion
Everything_GetMajorVersion.argtypes = []
Everything_GetMajorVersion.restype = wintypes.DWORD

Everything_GetMinorVersion = __dll.Everything_GetMinorVersion
Everything_GetMinorVersion.argtypes = []
Everything_GetMinorVersion.restype = wintypes.DWORD

Everything_GetRevision = __dll.Everything_GetRevision
Everything_GetRevision.argtypes = []
Everything_GetRevision.restype = wintypes.DWORD

Everything_GetBuildNumber = __dll.Everything_GetBuildNumber
Everything_GetBuildNumber.argtypes = []
Everything_GetBuildNumber.restype = wintypes.DWORD

Everything_Exit = __dll.Everything_Exit
Everything_Exit.argtypes = []
Everything_Exit.restype = wintypes.BOOL

Everything_IsDBLoaded = __dll.Everything_IsDBLoaded
Everything_IsDBLoaded.argtypes = []
Everything_IsDBLoaded.restype = wintypes.BOOL

Everything_IsAdmin = __dll.Everything_IsAdmin
Everything_IsAdmin.argtypes = []
Everything_IsAdmin.restype = wintypes.BOOL

Everything_IsAppData = __dll.Everything_IsAppData
Everything_IsAppData.argtypes = []
Everything_IsAppData.restype = wintypes.BOOL

Everything_RebuildDB = __dll.Everything_RebuildDB
Everything_RebuildDB.argtypes = []
Everything_RebuildDB.restype = wintypes.BOOL

Everything_UpdateAllFolderIndexes = __dll.Everything_UpdateAllFolderIndexes
Everything_UpdateAllFolderIndexes.argtypes = []
Everything_UpdateAllFolderIndexes.restype = wintypes.BOOL

Everything_SaveDB = __dll.Everything_SaveDB
Everything_SaveDB.argtypes = []
Everything_SaveDB.restype = wintypes.BOOL

Everything_SaveRunHistory = __dll.Everything_SaveRunHistory
Everything_SaveRunHistory.argtypes = []
Everything_SaveRunHistory.restype = wintypes.BOOL

Everything_DeleteRunHistory = __dll.Everything_DeleteRunHistory
Everything_DeleteRunHistory.argtypes = []
Everything_DeleteRunHistory.restype = wintypes.BOOL

Everything_GetTargetMachine = __dll.Everything_GetTargetMachine
Everything_GetTargetMachine.argtypes = []
Everything_GetTargetMachine.restype = wintypes.DWORD


Everything_GetRunCountFromFileNameW = __dll.Everything_GetRunCountFromFileNameW
Everything_GetRunCountFromFileNameW.argtypes = [wintypes.LPCWSTR]
Everything_GetRunCountFromFileNameW.restype = wintypes.DWORD

Everything_GetRunCountFromFileNameA = __dll.Everything_GetRunCountFromFileNameA
Everything_GetRunCountFromFileNameA.argtypes = [wintypes.LPCSTR]
Everything_GetRunCountFromFileNameA.restype = wintypes.DWORD

Everything_SetRunCountFromFileNameW = __dll.Everything_SetRunCountFromFileNameW
Everything_SetRunCountFromFileNameW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD]
Everything_SetRunCountFromFileNameW.restype = wintypes.BOOL

Everything_SetRunCountFromFileNameA = __dll.Everything_SetRunCountFromFileNameA
Everything_SetRunCountFromFileNameA.argtypes = [wintypes.LPCSTR, wintypes.DWORD]
Everything_SetRunCountFromFileNameA.restype = wintypes.BOOL

Everything_IncRunCountFromFileNameW = __dll.Everything_IncRunCountFromFileNameW
Everything_IncRunCountFromFileNameW.argtypes = [wintypes.LPCWSTR]
Everything_IncRunCountFromFileNameW.restype = wintypes.DWORD

Everything_IncRunCountFromFileNameA = __dll.Everything_IncRunCountFromFileNameA
Everything_IncRunCountFromFileNameA.argtypes = [wintypes.LPCSTR]
Everything_IncRunCountFromFileNameA.restype = wintypes.DWORD
