from lib.c_defines import *
from lib import wrapper

import enum
import threading


EverythingSearchLock = threading.Lock()

# region Exceptions

class EverythingOutOfMemoryException(Exception):
    pass
class EverythingIPCUnavailableException(Exception):
    pass
class EverythingRegisterClassException(Exception):
    pass
class EverythingCreateWindowException(Exception):
    pass
class EverythingCreateThreadException(Exception):
    pass
class EverythingInvalidIndexException(Exception):
    pass
class EverythingInvalidCallException(Exception):
    pass
class EverythingInvalidRequestException(Exception):
    pass
class EverythingInvalidParameterException(Exception):
    pass

def GetExceptionFromStatus(status: Status) -> Exception:
    if status == Status.EVERYTHING_ERROR_MEMORY:
        return EverythingOutOfMemoryException()
    elif status == Status.EVERYTHING_ERROR_IPC:
        return EverythingIPCUnavailableException()
    elif status == Status.EVERYTHING_ERROR_REGISTERCLASSEX:
        return EverythingRegisterClassException()
    elif status == Status.EVERYTHING_ERROR_CREATEWINDOW:
        return EverythingCreateWindowException()
    elif status == Status.EVERYTHING_ERROR_CREATETHREAD:
        return EverythingCreateThreadException()
    elif status == Status.EVERYTHING_ERROR_INVALIDINDEX:
        return EverythingInvalidIndexException()
    elif status == Status.EVERYTHING_ERROR_INVALIDCALL:
        return EverythingInvalidCallException()
    elif status == Status.EVERYTHING_ERROR_INVALIDREQUEST:
        return EverythingInvalidRequestException()
    elif status == Status.EVERYTHING_ERROR_INVALIDPARAMETER:
        return EverythingInvalidParameterException()

# endregion

class QueryStringOptions(enum.IntFlag):
    CaseSensitive = enum.auto()
    Regex = enum.auto()
    FullPath = enum.auto()
    WholeWord = enum.auto()

class SortOrder(enum.IntEnum):
    Filename = 1
    Path = 3
    Size = 5
    Extension = 7
    Type = 9
    CreationDate = 11
    ModificationDate = 13
    Attributes = 15
    _FilelistFilename = 17
    _RunCount = 19
    _RecentlyChangedDate = 21
    AccessDate = 23
    _RunDate = 25

class FieldRequest(enum.IntFlag):
    Filename = RequestFlags.EVERYTHING_REQUEST_FILE_NAME
    ParentDirectory = RequestFlags.EVERYTHING_REQUEST_PATH
    Path = RequestFlags.EVERYTHING_REQUEST_FULL_PATH_AND_FILE_NAME
    Extension = RequestFlags.EVERYTHING_REQUEST_EXTENSION
    Size = RequestFlags.EVERYTHING_REQUEST_SIZE
    CreationDate = RequestFlags.EVERYTHING_REQUEST_DATE_CREATED
    ModificationDate = RequestFlags.EVERYTHING_REQUEST_DATE_MODIFIED
    AccessDate = RequestFlags.EVERYTHING_REQUEST_DATE_ACCESSED
    Attributes = RequestFlags.EVERYTHING_REQUEST_ATTRIBUTES
    _FilelistFilename = RequestFlags.EVERYTHING_REQUEST_FILE_LIST_FILE_NAME
    _RunCount = RequestFlags.EVERYTHING_REQUEST_RUN_COUNT
    _RecentlyChangedDate = RequestFlags.EVERYTHING_REQUEST_DATE_RECENTLY_CHANGED
    _HighlightedFilename = RequestFlags.EVERYTHING_REQUEST_HIGHLIGHTED_FILE_NAME
    _HighlightedParentDirectory = RequestFlags.EVERYTHING_REQUEST_HIGHLIGHTED_PATH
    _HighlightedPath = RequestFlags.EVERYTHING_REQUEST_HIGHLIGHTED_FULL_PATH_AND_FILE_NAME

    All = RequestFlags.EVERYTHING_REQUEST_FILE_NAME | RequestFlags.EVERYTHING_REQUEST_PATH | RequestFlags.EVERYTHING_REQUEST_FULL_PATH_AND_FILE_NAME | RequestFlags.EVERYTHING_REQUEST_EXTENSION | RequestFlags.EVERYTHING_REQUEST_SIZE | RequestFlags.EVERYTHING_REQUEST_DATE_CREATED | RequestFlags.EVERYTHING_REQUEST_DATE_MODIFIED | RequestFlags.EVERYTHING_REQUEST_DATE_ACCESSED | RequestFlags.EVERYTHING_REQUEST_ATTRIBUTES

class Query():
    def __init__(self,
                 queryString: str,
                 matchingOptions: QueryStringOptions = QueryStringOptions(0),
                 startAtMatch: int = 0,
                 maxResults: int = -1,
                 sortOrder: SortOrder = SortOrder.Filename,
                 reverseOrder: bool = False,
                 requestedFields: FieldRequest = FieldRequest.All,
                 unicode: bool = True,
                 waitForEntireResult: bool = True
                 ):
        self.QueryString = queryString
        self.MatchingOptions = matchingOptions
        self.StartAtMatch = startAtMatch
        self.MaxResults = maxResults
        self.SortOrder = sortOrder
        self.ReverseOrder = reverseOrder
        self.RequestedFields = requestedFields
        self.Unicode = unicode
        self.WaitForEntireResult = waitForEntireResult

        self.__lockHeld = False
        self.__executingQuery = False
        self.__resultCount = 0
        self.__currentIndex = 0

    def __enter__(self):
        self.Acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Release()

    def __iter__(self):
        self.Execute()
        return self

    def __next__(self) -> "Result":
        if self.__currentIndex >= self.__resultCount:
            self.EndQuery()
            raise StopIteration

        index = self.__currentIndex
        self.__currentIndex += 1
        return self.GetResult(index)

    def __len__(self):
        if not self.__executingQuery:
            raise RuntimeError("Query is not started or has finished.")
        return self.__resultCount

    def __getitem__(self, index: int) -> "Result":
        if not self.__executingQuery:
            raise RuntimeError("Query is not started or has finished.")
        if not isinstance(index, int):
            raise ValueError("Index must be an int value.")
        if index < -self.__resultCount or index >= self.__resultCount:
            raise IndexError("Index out of range")
        if index < 0:
            index = self.__resultCount - index

        return self.GetResult(index)

    def Acquire(self):
        EverythingSearchLock.acquire()
        self.__lockHeld = True

        self.__SetupEverythingOptions()

    def Release(self):
        self.__lockHeld = False
        self.__executingQuery = False
        self.__resultCount = 0

        wrapper.Reset()

        EverythingSearchLock.release()

    def Execute(self):
        if not self.__lockHeld:
            raise RuntimeError("Cannot run without locking the IPC API first.")

        if not wrapper.Query(self.WaitForEntireResult, self.Unicode):
            raise GetExceptionFromStatus(wrapper.GetLastError())
        self.__resultCount = wrapper.GetNumResults() or 1
        self.__currentIndex = 0
        self.__executingQuery = True

    def EndQuery(self):
        self.__executingQuery = False

    def GetResult(self, index: int) -> "Result":
        return Result(index, self.RequestedFields, self.Unicode)

    def __SetupEverythingOptions(self):
        wrapper.SetMatchCase(QueryStringOptions.CaseSensitive in self.MatchingOptions)
        wrapper.SetRegex(QueryStringOptions.Regex in self.MatchingOptions)
        wrapper.SetMatchPath(QueryStringOptions.FullPath in self.MatchingOptions)
        wrapper.SetMatchWholeWord(QueryStringOptions.WholeWord in self.MatchingOptions)
        wrapper.SetOffset(self.StartAtMatch)
        wrapper.SetMax(self.MaxResults)
        wrapper.SetRequestFlags(RequestFlags(self.RequestedFields))

        sortInt = self.SortOrder.value
        if self.ReverseOrder:
            sortInt += 1
        wrapper.SetSort(SortType(sortInt))

        wrapper.SetSearch(self.QueryString, self.Unicode)

class Result():
    def __init__(self, index: int, fieldFlags: FieldRequest, unicode: bool = True):
        """
        This constructor shouldn't be called directly.
        """
        self.Index = index
        self.FieldFlags = fieldFlags
        self.Unicode = unicode

        # region fields

        self.Filename = wrapper.GetResultFileName(index, unicode) if FieldRequest.Filename in fieldFlags else None
        self.ParentDirectory = wrapper.GetResultPath(index, unicode) if FieldRequest.ParentDirectory in fieldFlags else None
        self.Path = wrapper.GetResultFullPathName(index, unicode) if FieldRequest.Path in fieldFlags else None # todo length?
        self.Extension = wrapper.GetResultExtension(index, unicode) if FieldRequest.Extension in fieldFlags else None
        self.Size = wrapper.GetResultSize(index) if FieldRequest.Size in fieldFlags else None
        self.CreationDate = wrapper.GetResultDateCreated(index) if FieldRequest.CreationDate in fieldFlags else None
        self.ModificationDate = wrapper.GetResultDateModified(index) if FieldRequest.ModificationDate in fieldFlags else None
        self.AccessDate = wrapper.GetResultDateAccessed(index) if FieldRequest.AccessDate in fieldFlags else None
        self.Attributes = wrapper.GetResultAttributes(index) if FieldRequest.Attributes in fieldFlags else None
        self._FilelistFilename = wrapper.GetResultFileListFileName(index, unicode) if FieldRequest._FilelistFilename in fieldFlags else None
        self._RunCount = wrapper.GetResultRunCount(index) if FieldRequest._RunCount in fieldFlags else None
        self._RecentlyChangedDate = wrapper.GetResultDateRecentlyChanged(index) if FieldRequest._RecentlyChangedDate in fieldFlags else None
        self._HighlightedFilename = wrapper.GetResultHighlightedFileName(index, unicode) if FieldRequest._HighlightedFilename in fieldFlags else None
        self._HighlightedParentDirectory = wrapper.GetResultHighlightedPath(index, unicode) if FieldRequest._HighlightedParentDirectory in fieldFlags else None
        self._HighlightedPath = wrapper.GetResultHighlightedFullPathAndFileName(index, unicode) if FieldRequest._HighlightedPath in fieldFlags else None # todo length?

        # endregion
