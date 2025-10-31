from zipfile import ZipFile
from version import Version
import os

lib_folder: str
zip_file:   ZipFile
version:    Version

ZipFile.extractall(zip_file, lib_folder) # type: ignore
os.remove(os.path.join(lib_folder, "instructions.py")) # type: ignore