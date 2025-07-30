# This is a generated file, created by generate_headers.py
# Changes made here will be lost when re-running that script
# Input Everything3.h SHA256: 5ccadde782b3a4ddd6429a0439d6b3da1ba722fa148d7d04ecc07831cd4706dd

import ctypes
from ctypes import wintypes
import os
import sys

from .c_structs import *


def __dllimport(name):
    try:
        return ctypes.WinDLL(name)
    except FileNotFoundError:
        return ctypes.WinDLL(os.path.join(os.path.dirname(__file__), name))

# dll's should be placed next to this file if not in a common dll path
if sys.maxsize > 2**32:
    __dll = __dllimport("Everything3_x64.dll")
else:
    __dll = __dllimport("Everything3_x86.dll")

Everything3_GetLastError = __dll.Everything3_GetLastError
Everything3_GetLastError.argtypes = []
Everything3_GetLastError.restype = wintypes.DWORD

Everything3_ConnectUTF8 = __dll.Everything3_ConnectUTF8
Everything3_ConnectUTF8.argtypes = [wintypes.LPCSTR,]
Everything3_ConnectUTF8.restype = wintypes.LPVOID

Everything3_ConnectW = __dll.Everything3_ConnectW
Everything3_ConnectW.argtypes = [wintypes.LPCWSTR,]
Everything3_ConnectW.restype = wintypes.LPVOID

Everything3_ConnectA = __dll.Everything3_ConnectA
Everything3_ConnectA.argtypes = [wintypes.LPCSTR,]
Everything3_ConnectA.restype = wintypes.LPVOID

Everything3_ShutdownClient = __dll.Everything3_ShutdownClient
Everything3_ShutdownClient.argtypes = [wintypes.LPVOID,]
Everything3_ShutdownClient.restype = wintypes.BOOL

Everything3_DestroyClient = __dll.Everything3_DestroyClient
Everything3_DestroyClient.argtypes = [wintypes.LPVOID,]
Everything3_DestroyClient.restype = wintypes.BOOL

Everything3_GetIPCPipeVersion = __dll.Everything3_GetIPCPipeVersion
Everything3_GetIPCPipeVersion.argtypes = [wintypes.LPVOID,]
Everything3_GetIPCPipeVersion.restype = wintypes.DWORD

Everything3_GetMajorVersion = __dll.Everything3_GetMajorVersion
Everything3_GetMajorVersion.argtypes = [wintypes.LPVOID,]
Everything3_GetMajorVersion.restype = wintypes.DWORD

Everything3_GetMinorVersion = __dll.Everything3_GetMinorVersion
Everything3_GetMinorVersion.argtypes = [wintypes.LPVOID,]
Everything3_GetMinorVersion.restype = wintypes.DWORD

Everything3_GetRevision = __dll.Everything3_GetRevision
Everything3_GetRevision.argtypes = [wintypes.LPVOID,]
Everything3_GetRevision.restype = wintypes.DWORD

Everything3_GetBuildNumber = __dll.Everything3_GetBuildNumber
Everything3_GetBuildNumber.argtypes = [wintypes.LPVOID,]
Everything3_GetBuildNumber.restype = wintypes.DWORD

Everything_GetTargetMachine = __dll.Everything_GetTargetMachine
Everything_GetTargetMachine.argtypes = [wintypes.LPVOID,]
Everything_GetTargetMachine.restype = wintypes.DWORD

Everything3_IsDBLoaded = __dll.Everything3_IsDBLoaded
Everything3_IsDBLoaded.argtypes = [wintypes.LPVOID,]
Everything3_IsDBLoaded.restype = wintypes.BOOL

Everything3_GetRunCountFromFilenameUTF8 = __dll.Everything3_GetRunCountFromFilenameUTF8
Everything3_GetRunCountFromFilenameUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_GetRunCountFromFilenameUTF8.restype = wintypes.DWORD

Everything3_GetRunCountFromFilenameW = __dll.Everything3_GetRunCountFromFilenameW
Everything3_GetRunCountFromFilenameW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,]
Everything3_GetRunCountFromFilenameW.restype = wintypes.DWORD

Everything3_GetRunCountFromFilenameA = __dll.Everything3_GetRunCountFromFilenameA
Everything3_GetRunCountFromFilenameA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_GetRunCountFromFilenameA.restype = wintypes.DWORD

Everything3_SetRunCountFromFilenameUTF8 = __dll.Everything3_SetRunCountFromFilenameUTF8
Everything3_SetRunCountFromFilenameUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,wintypes.DWORD,]
Everything3_SetRunCountFromFilenameUTF8.restype = wintypes.BOOL

Everything3_SetRunCountFromFilenameW = __dll.Everything3_SetRunCountFromFilenameW
Everything3_SetRunCountFromFilenameW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,wintypes.DWORD,]
Everything3_SetRunCountFromFilenameW.restype = wintypes.BOOL

Everything3_SetRunCountFromFilenameA = __dll.Everything3_SetRunCountFromFilenameA
Everything3_SetRunCountFromFilenameA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,wintypes.DWORD,]
Everything3_SetRunCountFromFilenameA.restype = wintypes.BOOL

Everything3_IncRunCountFromFilenameUTF8 = __dll.Everything3_IncRunCountFromFilenameUTF8
Everything3_IncRunCountFromFilenameUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_IncRunCountFromFilenameUTF8.restype = wintypes.DWORD

Everything3_IncRunCountFromFilenameW = __dll.Everything3_IncRunCountFromFilenameW
Everything3_IncRunCountFromFilenameW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,]
Everything3_IncRunCountFromFilenameW.restype = wintypes.DWORD

Everything3_IncRunCountFromFilenameA = __dll.Everything3_IncRunCountFromFilenameA
Everything3_IncRunCountFromFilenameA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_IncRunCountFromFilenameA.restype = wintypes.DWORD

Everything3_GetFolderSizeFromFilenameUTF8 = __dll.Everything3_GetFolderSizeFromFilenameUTF8
Everything3_GetFolderSizeFromFilenameUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_GetFolderSizeFromFilenameUTF8.restype = ctypes.c_uint64

Everything3_GetFolderSizeFromFilenameW = __dll.Everything3_GetFolderSizeFromFilenameW
Everything3_GetFolderSizeFromFilenameW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,]
Everything3_GetFolderSizeFromFilenameW.restype = ctypes.c_uint64

Everything3_GetFolderSizeFromFilenameA = __dll.Everything3_GetFolderSizeFromFilenameA
Everything3_GetFolderSizeFromFilenameA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_GetFolderSizeFromFilenameA.restype = ctypes.c_uint64

Everything3_GetFileAttributesExW = __dll.Everything3_GetFileAttributesExW
Everything3_GetFileAttributesExW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,wintypes.LPWIN32_FIND_DATAW,]
Everything3_GetFileAttributesExW.restype = wintypes.BOOL

Everything3_GetFileAttributesExA = __dll.Everything3_GetFileAttributesExA
Everything3_GetFileAttributesExA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,wintypes.LPWIN32_FIND_DATAA,]
Everything3_GetFileAttributesExA.restype = wintypes.BOOL

Everything3_GetFileAttributesUTF8 = __dll.Everything3_GetFileAttributesUTF8
Everything3_GetFileAttributesUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_GetFileAttributesUTF8.restype = wintypes.DWORD

Everything3_GetFileAttributesW = __dll.Everything3_GetFileAttributesW
Everything3_GetFileAttributesW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,]
Everything3_GetFileAttributesW.restype = wintypes.DWORD

Everything3_GetFileAttributesA = __dll.Everything3_GetFileAttributesA
Everything3_GetFileAttributesA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_GetFileAttributesA.restype = wintypes.DWORD

Everything3_FindFirstFileW = __dll.Everything3_FindFirstFileW
Everything3_FindFirstFileW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,wintypes.LPWIN32_FIND_DATAW,]
Everything3_FindFirstFileW.restype = wintypes.LPVOID

Everything3_FindFirstFileA = __dll.Everything3_FindFirstFileA
Everything3_FindFirstFileA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,wintypes.LPWIN32_FIND_DATAA,]
Everything3_FindFirstFileA.restype = wintypes.LPVOID

Everything3_FindNextFileW = __dll.Everything3_FindNextFileW
Everything3_FindNextFileW.argtypes = [wintypes.LPVOID,wintypes.LPWIN32_FIND_DATAW,]
Everything3_FindNextFileW.restype = wintypes.BOOL

Everything3_FindNextFileA = __dll.Everything3_FindNextFileA
Everything3_FindNextFileA.argtypes = [wintypes.LPVOID,wintypes.LPWIN32_FIND_DATAA,]
Everything3_FindNextFileA.restype = wintypes.BOOL

Everything3_FindClose = __dll.Everything3_FindClose
Everything3_FindClose.argtypes = [wintypes.LPVOID,]
Everything3_FindClose.restype = wintypes.BOOL

Everything3_FindPropertyUTF8 = __dll.Everything3_FindPropertyUTF8
Everything3_FindPropertyUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_FindPropertyUTF8.restype = wintypes.DWORD

Everything3_FindPropertyW = __dll.Everything3_FindPropertyW
Everything3_FindPropertyW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,]
Everything3_FindPropertyW.restype = wintypes.DWORD

Everything3_FindPropertyA = __dll.Everything3_FindPropertyA
Everything3_FindPropertyA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_FindPropertyA.restype = wintypes.DWORD

Everything3_GetPropertyNameUTF8 = __dll.Everything3_GetPropertyNameUTF8
Everything3_GetPropertyNameUTF8.argtypes = [wintypes.LPVOID,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetPropertyNameUTF8.restype = ctypes.c_size_t

Everything3_GetPropertyNameW = __dll.Everything3_GetPropertyNameW
Everything3_GetPropertyNameW.argtypes = [wintypes.LPVOID,wintypes.DWORD,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetPropertyNameW.restype = ctypes.c_size_t

Everything3_GetPropertyNameA = __dll.Everything3_GetPropertyNameA
Everything3_GetPropertyNameA.argtypes = [wintypes.LPVOID,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetPropertyNameA.restype = ctypes.c_size_t

Everything3_GetPropertyCanonicalNameUTF8 = __dll.Everything3_GetPropertyCanonicalNameUTF8
Everything3_GetPropertyCanonicalNameUTF8.argtypes = [wintypes.LPVOID,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetPropertyCanonicalNameUTF8.restype = ctypes.c_size_t

Everything3_GetPropertyCanonicalNameW = __dll.Everything3_GetPropertyCanonicalNameW
Everything3_GetPropertyCanonicalNameW.argtypes = [wintypes.LPVOID,wintypes.DWORD,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetPropertyCanonicalNameW.restype = ctypes.c_size_t

Everything3_GetPropertyCanonicalNameA = __dll.Everything3_GetPropertyCanonicalNameA
Everything3_GetPropertyCanonicalNameA.argtypes = [wintypes.LPVOID,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetPropertyCanonicalNameA.restype = ctypes.c_size_t

Everything3_GetPropertyType = __dll.Everything3_GetPropertyType
Everything3_GetPropertyType.argtypes = [wintypes.LPVOID,wintypes.DWORD,]
Everything3_GetPropertyType.restype = wintypes.DWORD

Everything3_IsPropertyIndexed = __dll.Everything3_IsPropertyIndexed
Everything3_IsPropertyIndexed.argtypes = [wintypes.LPVOID,wintypes.DWORD,]
Everything3_IsPropertyIndexed.restype = wintypes.BOOL

Everything3_IsPropertyFastSort = __dll.Everything3_IsPropertyFastSort
Everything3_IsPropertyFastSort.argtypes = [wintypes.LPVOID,wintypes.DWORD,]
Everything3_IsPropertyFastSort.restype = wintypes.BOOL

Everything3_CreateSearchState = __dll.Everything3_CreateSearchState
Everything3_CreateSearchState.argtypes = []
Everything3_CreateSearchState.restype = wintypes.LPVOID

Everything3_DestroySearchState = __dll.Everything3_DestroySearchState
Everything3_DestroySearchState.argtypes = [wintypes.LPVOID,]
Everything3_DestroySearchState.restype = wintypes.BOOL

Everything3_SetSearchMatchCase = __dll.Everything3_SetSearchMatchCase
Everything3_SetSearchMatchCase.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchMatchCase.restype = wintypes.BOOL

Everything3_SetSearchMatchDiacritics = __dll.Everything3_SetSearchMatchDiacritics
Everything3_SetSearchMatchDiacritics.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchMatchDiacritics.restype = wintypes.BOOL

Everything3_SetSearchMatchWholeWords = __dll.Everything3_SetSearchMatchWholeWords
Everything3_SetSearchMatchWholeWords.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchMatchWholeWords.restype = wintypes.BOOL

Everything3_SetSearchMatchPath = __dll.Everything3_SetSearchMatchPath
Everything3_SetSearchMatchPath.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchMatchPath.restype = wintypes.BOOL

Everything3_SetSearchMatchPrefix = __dll.Everything3_SetSearchMatchPrefix
Everything3_SetSearchMatchPrefix.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchMatchPrefix.restype = wintypes.BOOL

Everything3_SetSearchMatchSuffix = __dll.Everything3_SetSearchMatchSuffix
Everything3_SetSearchMatchSuffix.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchMatchSuffix.restype = wintypes.BOOL

Everything3_SetSearchIgnorePunctuation = __dll.Everything3_SetSearchIgnorePunctuation
Everything3_SetSearchIgnorePunctuation.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchIgnorePunctuation.restype = wintypes.BOOL

Everything3_SetSearchWhitespace = __dll.Everything3_SetSearchWhitespace
Everything3_SetSearchWhitespace.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchWhitespace.restype = wintypes.BOOL

Everything3_SetSearchRegex = __dll.Everything3_SetSearchRegex
Everything3_SetSearchRegex.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchRegex.restype = wintypes.BOOL

Everything3_SetSearchFoldersFirst = __dll.Everything3_SetSearchFoldersFirst
Everything3_SetSearchFoldersFirst.argtypes = [wintypes.LPVOID,wintypes.DWORD,]
Everything3_SetSearchFoldersFirst.restype = wintypes.BOOL

Everything3_SetSearchRequestTotalSize = __dll.Everything3_SetSearchRequestTotalSize
Everything3_SetSearchRequestTotalSize.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchRequestTotalSize.restype = wintypes.BOOL

Everything3_SetSearchHideResultOmissions = __dll.Everything3_SetSearchHideResultOmissions
Everything3_SetSearchHideResultOmissions.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchHideResultOmissions.restype = wintypes.BOOL

Everything3_SetSearchSortMix = __dll.Everything3_SetSearchSortMix
Everything3_SetSearchSortMix.argtypes = [wintypes.LPVOID,wintypes.BOOL,]
Everything3_SetSearchSortMix.restype = wintypes.BOOL

Everything3_SetSearchTextUTF8 = __dll.Everything3_SetSearchTextUTF8
Everything3_SetSearchTextUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_SetSearchTextUTF8.restype = wintypes.BOOL

Everything3_SetSearchTextW = __dll.Everything3_SetSearchTextW
Everything3_SetSearchTextW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,]
Everything3_SetSearchTextW.restype = wintypes.BOOL

Everything3_SetSearchTextA = __dll.Everything3_SetSearchTextA
Everything3_SetSearchTextA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,]
Everything3_SetSearchTextA.restype = wintypes.BOOL

Everything3_AddSearchSort = __dll.Everything3_AddSearchSort
Everything3_AddSearchSort.argtypes = [wintypes.LPVOID,wintypes.DWORD,wintypes.BOOL,]
Everything3_AddSearchSort.restype = wintypes.BOOL

Everything3_ClearSearchSorts = __dll.Everything3_ClearSearchSorts
Everything3_ClearSearchSorts.argtypes = [wintypes.LPVOID,]
Everything3_ClearSearchSorts.restype = wintypes.BOOL

Everything3_AddSearchPropertyRequest = __dll.Everything3_AddSearchPropertyRequest
Everything3_AddSearchPropertyRequest.argtypes = [wintypes.LPVOID,wintypes.DWORD,]
Everything3_AddSearchPropertyRequest.restype = wintypes.BOOL

Everything3_AddSearchPropertyRequestFormatted = __dll.Everything3_AddSearchPropertyRequestFormatted
Everything3_AddSearchPropertyRequestFormatted.argtypes = [wintypes.LPVOID,wintypes.DWORD,]
Everything3_AddSearchPropertyRequestFormatted.restype = wintypes.BOOL

Everything3_AddSearchPropertyRequestHighlighted = __dll.Everything3_AddSearchPropertyRequestHighlighted
Everything3_AddSearchPropertyRequestHighlighted.argtypes = [wintypes.LPVOID,wintypes.DWORD,]
Everything3_AddSearchPropertyRequestHighlighted.restype = wintypes.BOOL

Everything3_ClearSearchPropertyRequests = __dll.Everything3_ClearSearchPropertyRequests
Everything3_ClearSearchPropertyRequests.argtypes = [wintypes.LPVOID,]
Everything3_ClearSearchPropertyRequests.restype = wintypes.BOOL

Everything3_SetSearchViewportOffset = __dll.Everything3_SetSearchViewportOffset
Everything3_SetSearchViewportOffset.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_SetSearchViewportOffset.restype = wintypes.BOOL

Everything3_SetSearchViewportCount = __dll.Everything3_SetSearchViewportCount
Everything3_SetSearchViewportCount.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_SetSearchViewportCount.restype = wintypes.BOOL

Everything3_GetSearchMatchCase = __dll.Everything3_GetSearchMatchCase
Everything3_GetSearchMatchCase.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchMatchCase.restype = wintypes.BOOL

Everything3_GetSearchMatchDiacritics = __dll.Everything3_GetSearchMatchDiacritics
Everything3_GetSearchMatchDiacritics.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchMatchDiacritics.restype = wintypes.BOOL

Everything3_GetSearchMatchWholeWords = __dll.Everything3_GetSearchMatchWholeWords
Everything3_GetSearchMatchWholeWords.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchMatchWholeWords.restype = wintypes.BOOL

Everything3_GetSearchMatchPath = __dll.Everything3_GetSearchMatchPath
Everything3_GetSearchMatchPath.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchMatchPath.restype = wintypes.BOOL

Everything3_GetSearchMatchPrefix = __dll.Everything3_GetSearchMatchPrefix
Everything3_GetSearchMatchPrefix.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchMatchPrefix.restype = wintypes.BOOL

Everything3_GetSearchMatchSuffix = __dll.Everything3_GetSearchMatchSuffix
Everything3_GetSearchMatchSuffix.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchMatchSuffix.restype = wintypes.BOOL

Everything3_GetSearchIgnorePunctuation = __dll.Everything3_GetSearchIgnorePunctuation
Everything3_GetSearchIgnorePunctuation.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchIgnorePunctuation.restype = wintypes.BOOL

Everything3_GetSearchWhitespace = __dll.Everything3_GetSearchWhitespace
Everything3_GetSearchWhitespace.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchWhitespace.restype = wintypes.BOOL

Everything3_GetSearchRegex = __dll.Everything3_GetSearchRegex
Everything3_GetSearchRegex.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchRegex.restype = wintypes.BOOL

Everything3_GetSearchFoldersFirst = __dll.Everything3_GetSearchFoldersFirst
Everything3_GetSearchFoldersFirst.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchFoldersFirst.restype = wintypes.DWORD

Everything3_GetSearchRequestTotalSize = __dll.Everything3_GetSearchRequestTotalSize
Everything3_GetSearchRequestTotalSize.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchRequestTotalSize.restype = wintypes.BOOL

Everything3_GetSearchHideResultOmissions = __dll.Everything3_GetSearchHideResultOmissions
Everything3_GetSearchHideResultOmissions.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchHideResultOmissions.restype = wintypes.BOOL

Everything3_GetSearchSortMix = __dll.Everything3_GetSearchSortMix
Everything3_GetSearchSortMix.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchSortMix.restype = wintypes.BOOL

Everything3_GetSearchTextUTF8 = __dll.Everything3_GetSearchTextUTF8
Everything3_GetSearchTextUTF8.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetSearchTextUTF8.restype = ctypes.c_size_t

Everything3_GetSearchTextW = __dll.Everything3_GetSearchTextW
Everything3_GetSearchTextW.argtypes = [wintypes.LPVOID,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetSearchTextW.restype = ctypes.c_size_t

Everything3_GetSearchTextA = __dll.Everything3_GetSearchTextA
Everything3_GetSearchTextA.argtypes = [wintypes.LPVOID,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetSearchTextA.restype = ctypes.c_size_t

Everything3_GetSearchSortCount = __dll.Everything3_GetSearchSortCount
Everything3_GetSearchSortCount.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchSortCount.restype = ctypes.c_size_t

Everything3_GetSearchSortPropertyId = __dll.Everything3_GetSearchSortPropertyId
Everything3_GetSearchSortPropertyId.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetSearchSortPropertyId.restype = wintypes.DWORD

Everything3_GetSearchSortAscending = __dll.Everything3_GetSearchSortAscending
Everything3_GetSearchSortAscending.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetSearchSortAscending.restype = wintypes.BOOL

Everything3_GetSearchPropertyRequestCount = __dll.Everything3_GetSearchPropertyRequestCount
Everything3_GetSearchPropertyRequestCount.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchPropertyRequestCount.restype = ctypes.c_size_t

Everything3_GetSearchPropertyRequestPropertyId = __dll.Everything3_GetSearchPropertyRequestPropertyId
Everything3_GetSearchPropertyRequestPropertyId.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetSearchPropertyRequestPropertyId.restype = wintypes.DWORD

Everything3_GetSearchPropertyRequestHighlight = __dll.Everything3_GetSearchPropertyRequestHighlight
Everything3_GetSearchPropertyRequestHighlight.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetSearchPropertyRequestHighlight.restype = wintypes.BOOL

Everything3_GetSearchPropertyRequestFormat = __dll.Everything3_GetSearchPropertyRequestFormat
Everything3_GetSearchPropertyRequestFormat.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetSearchPropertyRequestFormat.restype = wintypes.BOOL

Everything3_GetSearchViewportOffset = __dll.Everything3_GetSearchViewportOffset
Everything3_GetSearchViewportOffset.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchViewportOffset.restype = ctypes.c_size_t

Everything3_GetSearchViewportCount = __dll.Everything3_GetSearchViewportCount
Everything3_GetSearchViewportCount.argtypes = [wintypes.LPVOID,]
Everything3_GetSearchViewportCount.restype = ctypes.c_size_t

Everything3_Search = __dll.Everything3_Search
Everything3_Search.argtypes = [wintypes.LPVOID,wintypes.LPVOID,]
Everything3_Search.restype = wintypes.LPVOID

Everything3_GetResults = __dll.Everything3_GetResults
Everything3_GetResults.argtypes = [wintypes.LPVOID,wintypes.LPVOID,]
Everything3_GetResults.restype = wintypes.LPVOID

Everything3_Sort = __dll.Everything3_Sort
Everything3_Sort.argtypes = [wintypes.LPVOID,wintypes.LPVOID,]
Everything3_Sort.restype = wintypes.LPVOID

Everything3_IsResultListChange = __dll.Everything3_IsResultListChange
Everything3_IsResultListChange.argtypes = [wintypes.LPVOID,]
Everything3_IsResultListChange.restype = wintypes.BOOL

Everything3_WaitForResultListChange = __dll.Everything3_WaitForResultListChange
Everything3_WaitForResultListChange.argtypes = [wintypes.LPVOID,]
Everything3_WaitForResultListChange.restype = wintypes.BOOL

Everything3_DestroyResultList = __dll.Everything3_DestroyResultList
Everything3_DestroyResultList.argtypes = [wintypes.LPVOID,]
Everything3_DestroyResultList.restype = wintypes.BOOL

Everything3_GetResultListFolderCount = __dll.Everything3_GetResultListFolderCount
Everything3_GetResultListFolderCount.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListFolderCount.restype = ctypes.c_size_t

Everything3_GetResultListFileCount = __dll.Everything3_GetResultListFileCount
Everything3_GetResultListFileCount.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListFileCount.restype = ctypes.c_size_t

Everything3_GetResultListCount = __dll.Everything3_GetResultListCount
Everything3_GetResultListCount.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListCount.restype = ctypes.c_size_t

Everything3_GetResultListTotalSize = __dll.Everything3_GetResultListTotalSize
Everything3_GetResultListTotalSize.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListTotalSize.restype = ctypes.c_uint64

Everything3_GetResultListViewportOffset = __dll.Everything3_GetResultListViewportOffset
Everything3_GetResultListViewportOffset.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListViewportOffset.restype = ctypes.c_size_t

Everything3_GetResultListViewportCount = __dll.Everything3_GetResultListViewportCount
Everything3_GetResultListViewportCount.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListViewportCount.restype = ctypes.c_size_t

Everything3_GetResultListSortCount = __dll.Everything3_GetResultListSortCount
Everything3_GetResultListSortCount.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListSortCount.restype = ctypes.c_size_t

Everything3_GetResultListSortPropertyId = __dll.Everything3_GetResultListSortPropertyId
Everything3_GetResultListSortPropertyId.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultListSortPropertyId.restype = wintypes.DWORD

Everything3_GetResultListSortAscending = __dll.Everything3_GetResultListSortAscending
Everything3_GetResultListSortAscending.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultListSortAscending.restype = wintypes.BOOL

Everything3_GetResultListPropertyRequestCount = __dll.Everything3_GetResultListPropertyRequestCount
Everything3_GetResultListPropertyRequestCount.argtypes = [wintypes.LPVOID,]
Everything3_GetResultListPropertyRequestCount.restype = ctypes.c_size_t

Everything3_GetResultListPropertyRequestPropertyId = __dll.Everything3_GetResultListPropertyRequestPropertyId
Everything3_GetResultListPropertyRequestPropertyId.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultListPropertyRequestPropertyId.restype = wintypes.DWORD

Everything3_GetResultListPropertyRequestValueType = __dll.Everything3_GetResultListPropertyRequestValueType
Everything3_GetResultListPropertyRequestValueType.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultListPropertyRequestValueType.restype = wintypes.DWORD

Everything3_GetResultListPropertyRequestOffset = __dll.Everything3_GetResultListPropertyRequestOffset
Everything3_GetResultListPropertyRequestOffset.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultListPropertyRequestOffset.restype = ctypes.c_size_t

Everything3_IsFolderResult = __dll.Everything3_IsFolderResult
Everything3_IsFolderResult.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_IsFolderResult.restype = wintypes.BOOL

Everything3_IsRootResult = __dll.Everything3_IsRootResult
Everything3_IsRootResult.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_IsRootResult.restype = wintypes.BOOL

Everything3_GetResultPropertyTextUTF8 = __dll.Everything3_GetResultPropertyTextUTF8
Everything3_GetResultPropertyTextUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextUTF8.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextW = __dll.Everything3_GetResultPropertyTextW
Everything3_GetResultPropertyTextW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextW.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextA = __dll.Everything3_GetResultPropertyTextA
Everything3_GetResultPropertyTextA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextA.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextFormattedUTF8 = __dll.Everything3_GetResultPropertyTextFormattedUTF8
Everything3_GetResultPropertyTextFormattedUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextFormattedUTF8.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextFormattedW = __dll.Everything3_GetResultPropertyTextFormattedW
Everything3_GetResultPropertyTextFormattedW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextFormattedW.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextFormattedA = __dll.Everything3_GetResultPropertyTextFormattedA
Everything3_GetResultPropertyTextFormattedA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextFormattedA.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextHighlightedUTF8 = __dll.Everything3_GetResultPropertyTextHighlightedUTF8
Everything3_GetResultPropertyTextHighlightedUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextHighlightedUTF8.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextHighlightedW = __dll.Everything3_GetResultPropertyTextHighlightedW
Everything3_GetResultPropertyTextHighlightedW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextHighlightedW.restype = ctypes.c_size_t

Everything3_GetResultPropertyTextHighlightedA = __dll.Everything3_GetResultPropertyTextHighlightedA
Everything3_GetResultPropertyTextHighlightedA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPropertyTextHighlightedA.restype = ctypes.c_size_t

Everything3_GetResultPropertyBYTE = __dll.Everything3_GetResultPropertyBYTE
Everything3_GetResultPropertyBYTE.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,]
Everything3_GetResultPropertyBYTE.restype = wintypes.BYTE

Everything3_GetResultPropertyWORD = __dll.Everything3_GetResultPropertyWORD
Everything3_GetResultPropertyWORD.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,]
Everything3_GetResultPropertyWORD.restype = wintypes.WORD

Everything3_GetResultPropertyDWORD = __dll.Everything3_GetResultPropertyDWORD
Everything3_GetResultPropertyDWORD.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,]
Everything3_GetResultPropertyDWORD.restype = wintypes.DWORD

Everything3_GetResultPropertyUINT64 = __dll.Everything3_GetResultPropertyUINT64
Everything3_GetResultPropertyUINT64.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,]
Everything3_GetResultPropertyUINT64.restype = ctypes.c_uint64

Everything3_GetResultPropertyUINT128 = __dll.Everything3_GetResultPropertyUINT128
Everything3_GetResultPropertyUINT128.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,ctypes.POINTER(UInt128),]
Everything3_GetResultPropertyUINT128.restype = wintypes.BOOL

Everything3_GetResultPropertyDIMENSIONS = __dll.Everything3_GetResultPropertyDIMENSIONS
Everything3_GetResultPropertyDIMENSIONS.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,ctypes.POINTER(Dimensions),]
Everything3_GetResultPropertyDIMENSIONS.restype = wintypes.BOOL

Everything3_GetResultPropertySIZE_T = __dll.Everything3_GetResultPropertySIZE_T
Everything3_GetResultPropertySIZE_T.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,]
Everything3_GetResultPropertySIZE_T.restype = ctypes.c_size_t

Everything3_GetResultPropertyINT32 = __dll.Everything3_GetResultPropertyINT32
Everything3_GetResultPropertyINT32.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,]
Everything3_GetResultPropertyINT32.restype = ctypes.c_int32

Everything3_GetResultPropertyBlob = __dll.Everything3_GetResultPropertyBlob
Everything3_GetResultPropertyBlob.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.DWORD,ctypes.POINTER(wintypes.BYTE),ctypes.POINTER(ctypes.c_size_t),]
Everything3_GetResultPropertyBlob.restype = wintypes.BOOL

Everything3_GetResultNameUTF8 = __dll.Everything3_GetResultNameUTF8
Everything3_GetResultNameUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultNameUTF8.restype = ctypes.c_size_t

Everything3_GetResultNameW = __dll.Everything3_GetResultNameW
Everything3_GetResultNameW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultNameW.restype = ctypes.c_size_t

Everything3_GetResultNameA = __dll.Everything3_GetResultNameA
Everything3_GetResultNameA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultNameA.restype = ctypes.c_size_t

Everything3_GetResultPathUTF8 = __dll.Everything3_GetResultPathUTF8
Everything3_GetResultPathUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPathUTF8.restype = ctypes.c_size_t

Everything3_GetResultPathW = __dll.Everything3_GetResultPathW
Everything3_GetResultPathW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultPathW.restype = ctypes.c_size_t

Everything3_GetResultPathA = __dll.Everything3_GetResultPathA
Everything3_GetResultPathA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultPathA.restype = ctypes.c_size_t

Everything3_GetResultFullPathNameUTF8 = __dll.Everything3_GetResultFullPathNameUTF8
Everything3_GetResultFullPathNameUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultFullPathNameUTF8.restype = ctypes.c_size_t

Everything3_GetResultFullPathNameW = __dll.Everything3_GetResultFullPathNameW
Everything3_GetResultFullPathNameW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultFullPathNameW.restype = ctypes.c_size_t

Everything3_GetResultFullPathNameA = __dll.Everything3_GetResultFullPathNameA
Everything3_GetResultFullPathNameA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultFullPathNameA.restype = ctypes.c_size_t

Everything3_GetResultSize = __dll.Everything3_GetResultSize
Everything3_GetResultSize.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultSize.restype = ctypes.c_uint64

Everything3_GetResultExtensionUTF8 = __dll.Everything3_GetResultExtensionUTF8
Everything3_GetResultExtensionUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultExtensionUTF8.restype = ctypes.c_size_t

Everything3_GetResultExtensionW = __dll.Everything3_GetResultExtensionW
Everything3_GetResultExtensionW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultExtensionW.restype = ctypes.c_size_t

Everything3_GetResultExtensionA = __dll.Everything3_GetResultExtensionA
Everything3_GetResultExtensionA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultExtensionA.restype = ctypes.c_size_t

Everything3_GetResultTypeUTF8 = __dll.Everything3_GetResultTypeUTF8
Everything3_GetResultTypeUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultTypeUTF8.restype = ctypes.c_size_t

Everything3_GetResultTypeW = __dll.Everything3_GetResultTypeW
Everything3_GetResultTypeW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultTypeW.restype = ctypes.c_size_t

Everything3_GetResultTypeA = __dll.Everything3_GetResultTypeA
Everything3_GetResultTypeA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultTypeA.restype = ctypes.c_size_t

Everything3_GetResultDateModified = __dll.Everything3_GetResultDateModified
Everything3_GetResultDateModified.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultDateModified.restype = ctypes.c_uint64

Everything3_GetResultDateCreated = __dll.Everything3_GetResultDateCreated
Everything3_GetResultDateCreated.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultDateCreated.restype = ctypes.c_uint64

Everything3_GetResultDateAccessed = __dll.Everything3_GetResultDateAccessed
Everything3_GetResultDateAccessed.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultDateAccessed.restype = ctypes.c_uint64

Everything3_GetResultAttributes = __dll.Everything3_GetResultAttributes
Everything3_GetResultAttributes.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultAttributes.restype = wintypes.DWORD

Everything3_GetResultDateRecentlyChanged = __dll.Everything3_GetResultDateRecentlyChanged
Everything3_GetResultDateRecentlyChanged.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultDateRecentlyChanged.restype = ctypes.c_uint64

Everything3_GetResultRunCount = __dll.Everything3_GetResultRunCount
Everything3_GetResultRunCount.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultRunCount.restype = wintypes.DWORD

Everything3_GetResultDateRun = __dll.Everything3_GetResultDateRun
Everything3_GetResultDateRun.argtypes = [wintypes.LPVOID,ctypes.c_size_t,]
Everything3_GetResultDateRun.restype = ctypes.c_uint64

Everything3_GetResultFilelistFilenameUTF8 = __dll.Everything3_GetResultFilelistFilenameUTF8
Everything3_GetResultFilelistFilenameUTF8.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultFilelistFilenameUTF8.restype = ctypes.c_size_t

Everything3_GetResultFilelistFilenameW = __dll.Everything3_GetResultFilelistFilenameW
Everything3_GetResultFilelistFilenameW.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCWSTR,ctypes.c_size_t,]
Everything3_GetResultFilelistFilenameW.restype = ctypes.c_size_t

Everything3_GetResultFilelistFilenameA = __dll.Everything3_GetResultFilelistFilenameA
Everything3_GetResultFilelistFilenameA.argtypes = [wintypes.LPVOID,ctypes.c_size_t,wintypes.LPCSTR,ctypes.c_size_t,]
Everything3_GetResultFilelistFilenameA.restype = ctypes.c_size_t

