# Quick code generator; read function print_help for more info

import hashlib
import os
import re
import sys


def print_help():
    print("This is a quick wrapper code parser and generator for C to PY.")
    print("It's used for generating c_defines.py and c_functions.py.")
    print("Usage: generate_headers.py [path to Everything3.h] [output directory]")

def _quick_get_sha(path) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def _writeln(f, s=""):
    f.write(s + "\n")

def _write_generated_header(f, everythingHeaderPath):
    _writeln(f, f"""# This is a generated file, created by generate_headers.py
# Changes made here will be lost when re-running that script
# Input Everything3.h SHA256: {_quick_get_sha(everythingHeaderPath)}""")
    _writeln(f)

_HexNumberRegex = "(?:0x)?[a-fA-F0-9]+"
_CSymbolRegex = "[a-zA-Z_][a-zA-Z0-9_]*"

def gen_defines(everythingHeaderPath, outDirectory):
    print("Parsing defines...")

    with open(everythingHeaderPath, "r", encoding="utf-8") as f:
        headerContents = f.read()

    with open(os.path.join(outDirectory, "c_defines.py"), "w", encoding="utf-8") as f:
        _write_generated_header(f, everythingHeaderPath)
        _writeln(f, "import enum")
        _writeln(f)
        _writeln(f)

        def gen_errors():
            print("Parsing error statuses...")
            errorNamesToMessages = []

            _writeln(f, "class Status(enum.IntEnum):")

            _writeln(f, f"    OK = 0")
            errorNamesToMessages.append(("OK", "no error"))

            ms = re.finditer(rf"^\s*#define\s+EVERYTHING3_ERROR_({_CSymbolRegex})\s+({_HexNumberRegex})\s*(?://\s*(.+))?", headerContents, re.M)
            for m in ms:
                print(f"  error status: {m.group(1)}")
                _writeln(f, f"    {m.group(1)} = {m.group(2)}")
                errorNamesToMessages.append((m.group(1), m.group(3) or ""))

            _writeln(f)

            _writeln(f, "def StatusToMessage(status: Status) -> str:")
            for (name, message) in errorNamesToMessages:
                _writeln(f, f"    if status == Status.{name}:")
                _writeln(f, f"        return \"{message or name}\"")
            _writeln(f, "    return \"<unknown error>\"")

            _writeln(f)
            print("Parsing error statuses OK!")
        gen_errors()

        def gen_target_machine():
            print("Parsing target machines...")
            _writeln(f, "class TargetMachine(enum.IntEnum):")
            ms = re.finditer(rf"^\s*#define\s+EVERYTHING3_TARGET_MACHINE_({_CSymbolRegex})\s+({_HexNumberRegex})", headerContents, re.M)
            for m in ms:
                print(f"  target machine: {m.group(1)}")
                _writeln(f, f"    {m.group(1)} = {m.group(2)}")

            _writeln(f)
            print("Parsing target machines OK!")
        gen_target_machine()

        def gen_search_folders():
            print("Parsing search folder options...")
            _writeln(f, "class FolderFirst(enum.IntEnum):")
            ms = re.finditer(rf"^\s*#define\s+EVERYTHING3_SEARCH_FOLDERS_FIRST_({_CSymbolRegex})\s+({_HexNumberRegex})", headerContents, re.M)
            for m in ms:
                print(f"  search folder option: {m.group(1)}")
                _writeln(f, f"    {m.group(1)} = {m.group(2)}")

            _writeln(f)
            print("Parsing search folder options OK!")
        gen_search_folders()

        def gen_property_type():
            print("Parsing property types...")
            _writeln(f, "class PropertyType(enum.IntEnum):")
            ms = re.finditer(rf"^\s*#define\s+EVERYTHING3_PROPERTY_TYPE_({_CSymbolRegex})\s+({_HexNumberRegex})", headerContents, re.M)
            for m in ms:
                print(f"  property type: {m.group(1)}")
                _writeln(f, f"    {m.group(1)} = {m.group(2)}")

            _writeln(f)
            print("Parsing property types OK!")
        gen_property_type()

        def gen_property_value():
            print("Parsing property value types...")
            _writeln(f, "class PropertyType(enum.IntEnum):")
            ms = re.finditer(rf"^\s*#define\s+EVERYTHING3_PROPERTY_VALUE_TYPE_({_CSymbolRegex})\s+({_HexNumberRegex})", headerContents, re.M)
            for m in ms:
                print(f"  property value type: {m.group(1)}")
                _writeln(f, f"    {m.group(1)} = {m.group(2)}")

            _writeln(f)
            print("Parsing property value types OK!")
        gen_property_value()

        def gen_property_id():
            print("Parsing property ids...")
            propertyTypes = []

            _writeln(f, "class PropertyId(enum.IntEnum):")
            _writeln(f, "    INVALID_PROPERTY_ID = -1")
            ms = re.finditer(rf"^\s*#define\s+EVERYTHING3_PROPERTY_ID_({_CSymbolRegex})\s+({_HexNumberRegex})\s*(?://\s*(.+))?", headerContents, re.M)
            for m in ms:
                print(f"  property id: {m.group(1)}")
                _writeln(f, f"    {m.group(1)} = {m.group(2)}")
                mv = re.search(f"EVERYTHING3_PROPERTY_VALUE_TYPE_({_CSymbolRegex})", m.group(3), re.I)

                # TODO fix this quickhack when/if it's fixed in the sdk
                value = mv.group(1)
                if value == "OWORD":
                    value = "UINT128"
                propertyTypes.append((m.group(1), value))
            
            _writeln(f)

            _writeln(f, "PropertyIdToValueTypeMap = {")
            for (id, type) in propertyTypes:
                _writeln(f, f"    PropertyId.{id}: PropertyType.{type},")
            _writeln(f, "}")

            _writeln(f)
            print("Parsing property ids OK!")
        gen_property_id()

    print("Parsing defines OK!")

def gen_functions(everythingHeaderPath, outDirectory):
    # a fairly bad but functional C parser, but at least the parsed code looks very well behaved

    sourceTypeToPyTypeMap = {
        "EVERYTHING3_CLIENT*":       "wintypes.LPCVOID",
        "EVERYTHING3_FIND_HANDLE*":  "wintypes.LPCVOID",
        "EVERYTHING3_SEARCH_STATE*": "wintypes.LPCVOID",
        "EVERYTHING3_RESULT_LIST*":  "wintypes.LPCVOID",

        "EVERYTHING3_UTF8*":         "wintypes.LPCSTR",
        "EVERYTHING3_WCHAR*":        "wintypes.LPCWSTR",
        "EVERYTHING3_CHAR*":         "wintypes.LPCSTR",

        "EVERYTHING3_BOOL":          "wintypes.BOOL",
        "EVERYTHING3_BYTE":          "wintypes.BYTE",
        "EVERYTHING3_WORD":          "wintypes.WORD",
        "EVERYTHING3_DWORD":         "wintypes.DWORD",
        "EVERYTHING3_INT32":         "ctypes.c_int32",
        "EVERYTHING3_UINT64":        "ctypes.c_uint64",
        "EVERYTHING3_SIZE_T":        "ctypes.c_size_t",

        "WIN32_FIND_DATAA*":         "wintypes.LPWIN32_FIND_DATAA",
        "WIN32_FIND_DATAW*":         "wintypes.LPWIN32_FIND_DATAW",
    }

    with open(everythingHeaderPath, "r", encoding="utf-8") as f:
        headerContents = f.read()

    with open(os.path.join(outDirectory, "c_functions.py"), "w", encoding="utf-8") as f:
        _write_generated_header(f, everythingHeaderPath)
        _writeln(f, """import ctypes
from ctypes import wintypes
import os
import sys


def __dllimport(name):
    try:
        return ctypes.WinDLL(name)
    except FileNotFoundError:
        return ctypes.WinDLL(os.path.join(os.path.dirname(__file__), name))

# dll's should be placed next to this file if not in a common dll path
if sys.maxsize > 2**32:
    __dll = __dllimport("Everything3_x64.dll")
else:
    __dll = __dllimport("Everything3_x86.dll")""")
        _writeln(f)
        
        functionDeclarationRegex = (
            "^\s*"
            "EVERYTHING3_USERAPI\s+"
            f"({_CSymbolRegex}[\s*]+)" # [1] return value
            "EVERYTHING3_API\s+"
            f"({_CSymbolRegex})\s*" # [2] function name
            "\\(\s*"
            f"(.+)\s*" # [3] parameter list as string
            "\\)\s*;"
        )

        parameterRegex = (
            "^\s*"
            "(?:const\s+)?" # optional const that we throw away
            f"({_CSymbolRegex})\s*" # [1] parameter type
            "([\s*]*)" # [2] pointer-ness
            f"({_CSymbolRegex})\s*" # [3] parameter name
            ",?"
        )

        functions = re.finditer(functionDeclarationRegex, headerContents, re.M)
        for func in functions:
            returnType = func.group(1).replace(" ", "")
            name = func.group(2)
            parametersText = func.group(3)

            print(f"  parsing function: {name}...")

            parameterTypes = []
            if parametersText.strip() != "void":
                parameters = re.finditer(parameterRegex, parametersText, re.M)
                for param in parameters:
                    parameterTypes.append(param.group(1) + param.group(2).replace(" ",""))

            if returnType == "void":
                pyReturnType = "None"
            else:
                pyReturnType = sourceTypeToPyTypeMap[returnType]

            pyParameters = "[]" # no parameters or just one parameter of type void
            if len(parameterTypes) >= 1 and parameterTypes[0] != "void":
                pyParameters = "["
                for paramType in parameterTypes:
                    pyParameters += sourceTypeToPyTypeMap[paramType] + ","
                pyParameters += "]"

            _writeln(f, f"{name} = __dll.{name}")
            _writeln(f, f"{name}.argtypes = {pyParameters}")
            _writeln(f, f"{name}.restype = {pyReturnType}")
            """
            Everything_SetSearchA = __dll.Everything_SetSearchA
            Everything_SetSearchA.argtypes = [wintypes.LPCSTR]
            Everything_SetSearchA.restype = None
            """
            _writeln(f)


def main():
    if len(sys.argv) != 3:
        print_help()
        return 0

    everythingHeaderPath = sys.argv[1]
    outDirectory = sys.argv[2]

    print("Starting to parse header...")

    gen_defines(everythingHeaderPath, outDirectory)
    gen_functions(everythingHeaderPath, outDirectory)

    print("Finished OK!")
    return 0

if __name__ == "__main__":
    exit(main())
