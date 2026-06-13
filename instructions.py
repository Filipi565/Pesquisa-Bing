from zipfile import ZipFile
from version import Version
from typing import cast
import shutil
import os

lib_folder = cast(str, globals()["lib_folder"])
zip_file   = cast(ZipFile, globals()["zip_file"])
version    = cast(Version, globals()["version"])

if (version <= Version(1, 5, 1)):
    shutil.rmtree(os.path.join(lib_folder, "util"))

ZipFile.extractall(zip_file, lib_folder)
os.remove(os.path.join(lib_folder, "instructions.py"))