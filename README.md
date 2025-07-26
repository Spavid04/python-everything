# Currently WIP and only wraps C functions in Python, no helpers provided
# If you want the old working version (for Everything 1.4) use the `legacy_master` branch

### This is a Python 3 adapter/wrapper for Voidtools' [Everything](https://www.voidtools.com/) API
This repo currently targets version 3 of the SDK (for Everything 1.5 alpha).
You can find its source [here](https://github.com/voidtools/everything_sdk3).

You should have `Everything3_x[64/86].dll` accessible through standard DLL load methods. If you don't know whether that's the case, just drop the DLL file inside the `lib3` directory, next to the `c_functions.py` file.
