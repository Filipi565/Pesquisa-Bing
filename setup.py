from cx_Freeze import setup, Executable
from setuptools import Extension

setup(
    name="BingSearch",
    version="1.0.0",
    description="github.com/Filipi565",
    executables=[Executable(script="program.py", base="gui")]
)