### This is a legacy branch of the master branch. Do not use this
This branch will be kept for a while for historical reasons.

### This is a quick and dirty Python 3 wrapper over [Voidtools Everything](https://www.voidtools.com/)
You should have `Everything[32/64].dll` accessible through standard DLL load methods. If you don't know if that's the case, just drop the DLL file inside the `lib` directory, next to the `c_functions.py` file.

Most functions assume that Everything.exe is already running. Function references can be found [at the official SDK page](https://voidtools.com/support/everything/sdk/). While all the exposed functions are wrapped in Python, you generally need to import only `Everything.py`.

### Usage example
```python
import Everything  
  
def main():  
    with Everything.Query("searched.txt", matchingOptions=Everything.QueryStringOptions.WholeWord) as q:  
        for result in q:  
            print(result.Path)  
  
if __name__ == "__main__":  
    main()
```

### Requirements
No non-standard Python packages.