from zipfile import ZipFile
from version import Version
import shutil
import os

lib_folder: str
zip_file:   ZipFile
version:    Version

if (version <= Version(1, 5, 1)): # type: ignore
    shutil.rmtree(os.path.join(lib_folder, "util")) # type: ignore

ZipFile.extractall(zip_file, lib_folder) # type: ignore
os.remove(os.path.join(lib_folder, "instructions.py")) # type: ignore