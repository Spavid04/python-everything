# The main guts of the Everything wrapper

from lib3 import c_defines, c_functions

import ctypes
from ctypes import wintypes
import typing


UINT64_MAX = 2**64 - 1
INVALID_FILE_ATTRIBUTES = wintypes.DWORD(-1).value

def GetLastStatus() -> c_defines.Status:
    return c_defines.Status(c_functions.Everything3_GetLastError())

def GetLastExceptionType() -> typing.Type[c_defines.Everything3Exception]:
    return c_defines.StatusToExceptionType(GetLastStatus())

class Win32FindDataIterator():
    # TODO doc and make WIN32_FIND_DATAW nicer
    def __init__(self, client: "Everything", filename: str):
        self.client = client
        self.filename = filename

        self.findHandle: wintypes.LPVOID = None
        self.findData: wintypes.WIN32_FIND_DATAW = None

        self.began = False
        self.closed = False

    @property
    def RAW_PTR(self) -> wintypes.LPVOID:
        """
        Returns the EVERYTHING3_FIND_HANDLE* raw pointer.
        """
        return self.findHandle
    
    def __enter__(self):
        self.Begin()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Finish()
    
    def __del__(self):
        self.Finish()

    def Begin(self):
        if self.closed:
            raise ValueError("Already closed.")
        if self.began:
            return

        findData = wintypes.WIN32_FIND_DATAW()
        filenameWchar = ctypes.create_unicode_buffer(self.filename)
        findHandle = c_functions.Everything3_FindFirstFileW(self.client.RAW_PTR, filenameWchar, ctypes.byref(findData))
        if findHandle is None:
            status = GetLastStatus()
            if status != c_defines.Status.OK:
                raise GetLastExceptionType()

        self.findHandle = findHandle
        self.findData = findData
        self.began = True

    def Finish(self):
        if not self.began or self.closed:
            return
        c_functions.Everything3_FindClose(self.RAW_PTR)
        self.closed = True

    def Current(self) -> wintypes.WIN32_FIND_DATAW:
        if not self.began:
            raise ValueError("Hasn't began yet.")
        if self.closed:
            raise ValueError("Already closed.")
        return self.findData

    def Advance(self) -> bool:
        if not self.began:
            raise ValueError("Hasn't began yet.")
        if self.closed:
            raise ValueError("Already closed.")
        self.client.AssertConnected()
        result = c_functions.Everything3_FindNextFileW(self.RAW_PTR, ctypes.byref(self.findData)).value
        if not result:
            status = GetLastStatus()
            if status == c_defines.Status.OK:
                return False
            else:
                raise GetLastExceptionType()
        return True
    
    def __iter__(self) -> typing.Generator[wintypes.WIN32_FIND_DATAW, None, None]:
        yield self.Current()
        if not self.Advance():
            raise StopIteration

class Everything():
    def __init__(self, instanceName: typing.Optional[str] = "1.5a"): # TODO remove instance name after 1.5 becomes the default
        """
        Creates a new Everything Client connection to the specified Everything instance name.

        Args:
            instanceName (optional): name of the instance
        """
        self.instanceName = instanceName

        self.client: wintypes.LPVOID = None

        self.connected = False
        self.closed = False

    @property
    def RAW_PTR(self) -> wintypes.LPVOID:
        """
        Returns the EVERYTHING3_CLIENT* raw pointer.
        """
        return self.client

    #region Open & Close
    def Connect(self):
        """
        Connect to the client.
        """
        if self.closed:
            raise ValueError("Connection is closed. Create a new one.")
        if self.connected:
            return

        instanceName = None
        if self.instanceName:
            instanceName = self.instanceName.encode("utf-8")
        client = c_functions.Everything3_ConnectUTF8(instanceName)

        if not client:
            raise GetLastExceptionType()
        self.client = client
        self.connected = True

    def __enter__(self):
        self.Connect()
        return self

    def Disconnect(self):
        """
        Disconnect from the client, allowing a new connection later.
        """
        if self.closed or not self.connected:
            return
        c_functions.Everything3_ShutdownClient(self.RAW_PTR)
        self.connected = False

    def Close(self):
        """
        Close the connection and dispose all resources.
        """
        return
        if self.closed or not self.connected:
            return
        self.Disconnect()
        c_functions.Everything3_DestroyClient(self.RAW_PTR)
        self.closed = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()
    #endregion

    #region Assertion Helpers
    def AssertConnected(self):
        """
        Raise an exception if the client is not connected.
        """
        if self.closed or not self.connected:
            raise ConnectionError("Not connected.")
    
    def AssertOk(self):
        status = GetLastStatus()
        if status != c_defines.Status.OK:
            raise GetLastExceptionType()
    #endregion

    #region Status & Version
    def GetVersion(self) -> typing.Tuple[int, int, int, int]:
        """
        Returns:
            a tuple of (major, minor, revision, buildNumber)
        """
        self.AssertConnected()
        version = []
        for func in (c_functions.Everything3_GetMajorVersion,
                     c_functions.Everything3_GetMinorVersion,
                     c_functions.Everything3_GetRevision,
                     c_functions.Everything3_GetBuildNumber):
            ver = func(self.RAW_PTR).value
            if ver == 0:
                raise GetLastExceptionType()
            version.append(ver)
        return tuple(version)

    def GetIPCPipeVersion(self) -> int:
        self.AssertConnected()
        version = c_functions.Everything3_GetIPCPipeVersion(self.RAW_PTR).value
        if version == 0:
            raise GetLastExceptionType()
        return version
    
    def GetTargetMachine(self) -> c_defines.TargetMachine:
        self.AssertConnected()
        machine = c_functions.Everything_GetTargetMachine(self.RAW_PTR).value
        if machine == 0:
            raise GetLastExceptionType()
        return c_defines.TargetMachine(machine)
    
    def IsDBLoaded(self) -> bool:
        """
        Checks whether the DB is loaded.
        Call GetLastStatus() if it returns False.
        """
        self.AssertConnected()
        loaded = c_functions.Everything3_IsDBLoaded(self.RAW_PTR).value
        return bool(loaded)
    #endregion

    #region Run Count Operations
    def GetRunCount(self, path: str) -> int:
        self.AssertConnected()
        runCount = c_functions.Everything3_GetRunCountFromFilenameUTF8(self.RAW_PTR, path.encode("utf-8")).value
        if GetLastStatus() == c_defines.Status.OK:
            return runCount
        else:
            raise GetLastExceptionType()

    def SetRunCount(self, path: str, runCount: int):
        self.AssertConnected()
        result = c_functions.Everything3_SetRunCountFromFilenameUTF8(self.RAW_PTR, path.encode("utf-8"), runCount).value
        if not result:
            raise GetLastExceptionType()

    def IncrementRunCount(self, path: str):
        self.AssertConnected()
        result = c_functions.Everything3_IncRunCountFromFilenameUTF8(self.RAW_PTR, path.encode("utf-8")).value
        if not result:
            raise GetLastExceptionType()
    #endregion

    #region Folder Size
    def GetFolderSize(self, path: str) -> int:
        self.AssertConnected()
        size = c_functions.Everything3_GetFolderSizeFromFilenameUTF8(self.RAW_PTR, path.encode("utf-8")).value
        if GetLastStatus() == c_defines.Status.OK:
            return size
        else:
            raise GetLastExceptionType()
    #endregion

    #region Win32 equivalents
    #region File Attributes
    def GetFileAttributes(self, path: str, extended: bool=False) -> typing.Union[int, wintypes.WIN32_FIND_DATAW]:
        """
        Fetches the file attributes as a simple DWORD (int) or a WIN32_FIND_DATAW.

        Args:
            extended: if True, returns a WIN32_FIND_DATAW structure, otherwise a DWORD (int)
        
        Note:
            If extended attributes are requested, only indexed attributes are populated.
        """
        # TODO convert DWORD(int) to nicer attributes (and probably the struct too)
        self.AssertConnected()
        pathBytes = path.encode("utf-8")
        if extended:
            findData = wintypes.WIN32_FIND_DATAW()
            result = c_functions.Everything3_GetFileAttributesExW(self.RAW_PTR, pathBytes, ctypes.byref(findData))
            if not result:
                raise GetLastExceptionType()
            return findData
        else:
            attributes = c_functions.Everything3_GetFileAttributesUTF8(self.RAW_PTR, pathBytes).value
            if attributes == INVALID_FILE_ATTRIBUTES:
                raise GetLastExceptionType()
            return attributes
    #endregion
    #region Find File
    def FindFile(self, filename: str) -> Win32FindDataIterator:
        self.AssertConnected()
        return Win32FindDataIterator(self.RAW_PTR, filename)
    #endregion
    #endregion

    #region Property Metadata
    def FindPropertyByName(self, name: str) -> c_defines.PropertyId:
        self.AssertConnected()
        id = c_functions.Everything3_FindPropertyUTF8(self.RAW_PTR, name.encode("utf-8"))
        status = GetLastStatus()
        if id == c_defines.PropertyId.INVALID_PROPERTY_ID:
            self.AssertOk()
        return c_defines.PropertyId(id)
    
    def FindPropertyById(self, id: c_defines.PropertyId, canonicalName: bool=True) -> str:
        self.AssertConnected()
        buffer = ctypes.create_string_buffer(4096)
        if canonicalName:
            func = c_functions.Everything3_GetPropertyCanonicalNameUTF8
        else:
            func = c_functions.Everything3_GetPropertyNameUTF8
        actualSize = func(self.RAW_PTR, int(id), buffer, ctypes.sizeof(buffer))
        if actualSize == 0:
            self.AssertOk()
        return buffer.value.decode("utf-8")
    
    def GetPropertyType(self, id: c_defines.PropertyId) -> c_defines.PropertyType:
        self.AssertConnected()
        pType = c_functions.Everything3_GetPropertyType(self.RAW_PTR, int(id))
        if pType == c_defines.PropertyType.NONE:
            self.AssertOk()
        return c_defines.PropertyType(pType)

    @staticmethod
    def GetPropertyValueType(id: c_defines.PropertyId) -> c_defines.PropertyValueType:
        """
        Note:
            Does not require the client to be connected.
        """
        pType = c_defines.PropertyIdToValueType(id)
        if pType is None:
            raise ValueError("Invalid property.")
        return c_defines.PropertyValueType(pType)
    
    def IsPropertyIndexed(self, id: c_defines.PropertyId) -> bool:
        self.AssertConnected()
        result = c_functions.Everything3_IsPropertyIndexed(self.RAW_PTR, int(id))
        if not result:
            self.AssertOk()
        return bool(result)

    def IsPropertyFastSort(self, id: c_defines.PropertyId) -> bool:
        self.AssertConnected()
        result = c_functions.Everything3_IsPropertyFastSort(self.RAW_PTR, int(id))
        if not result:
            self.AssertOk()
        return bool(result)
    #endregion
