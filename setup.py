from cx_Freeze import setup, Executable
from version import version

setup(
    name="BingSearch",
    version=str(version),
    description="github.com/Filipi565",
    executables=[Executable(script="BingSearch.py", base="gui")]
)