import os
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\Users\\paseb\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\paseb\\Anaconda3\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

exe = Executable(script="ShutdownManager.py", base=base, icon="icon.ico")

setup(name="Shutdown",
        options={"build_exe": {"packages": ["os", "threading", "appJar"], "include_files": ["icon.ico"]}},
        version="0.1",
        description="Shutdown Manager",
        executables=[exe])
