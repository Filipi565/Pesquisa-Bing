from typing import Union
import atexit
import sys
import os

HERE = os.path.abspath(os.path.join(sys.argv[0], ".."))

_process_path: Union[str, None] = None

@atexit.register
def _():
    global _process_path

    if (_process_path) and os.path.exists(_process_path):
        with open(os.path.join(HERE, "process_path.txt"), "w") as f:
            f.write(_process_path)

def get_process_path() -> str:
    global _process_path

    if (_process_path):
        return _process_path

    with open(os.path.join(HERE, "process_path.txt"), "r") as f:
        return f.read()
    
def set_process_path(process_path: str) -> None:
    global _process_path

    if not (isinstance(process_path, str)):
        raise TypeError("process_path must be string")
    
    if not (os.path.exists(process_path)):
        raise FileNotFoundError(f"The file '{process_path}' does not exists")
    
    _process_path = process_path