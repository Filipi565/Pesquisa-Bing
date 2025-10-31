from version import version as current_version, Version
from urllib.request import urlopen
from urllib.error import HTTPError
from tkinter import messagebox
from bs4 import BeautifulSoup
from zipfile import ZipFile
from typing import Union
import sys
import io
import os

try:
    from lang import Lang # type: ignore
except ImportError:
    from PT_br import Lang

def get_content(url: str) -> Union[bytes, None]:
    try:
        with urlopen(url) as f:
            return f.read()
    except HTTPError:
        return None

def download_zip_file(url: str) -> Union[io.BytesIO, None]:
    content = get_content(url)
    
    if (content):
        return io.BytesIO(content)
    
def get_dl_url(url: str) -> str:
    content = get_content(url)
    if not (content):
        return ""
    
    soup = BeautifulSoup(content, "html.parser")
    button = soup.find("a", id="downloadButton")
    if not (button):
        return ""
    
    return str(button.get("href", ""))

def user_want_update() -> bool:
    return messagebox.askyesno(Lang.Title, Lang.UpdateMessage)

def update(mediafire_url: str) -> None:
    lib_folder = os.path.abspath(os.path.join(sys.argv[0], "..", "lib"))

    url = get_dl_url(mediafire_url)
    if not (url):
        return

    file = download_zip_file(url)
    if not file:
        return
    
    with file:
        with ZipFile(file, "r") as zip_file:
            code = zip_file.read("instructions.py")
            exec(code, {"lib_folder": lib_folder, "zip_file": zip_file, "version": current_version})

def main():
    content_b = get_content("https://pastebin.com/raw/nQZRsXvJ")
    if not (content_b):
        return
    
    content = content_b.decode()
    
    version_text, mediafire_url = content.splitlines()

    last_version = Version(*map(int, version_text.split(".")))

    if not (current_version < last_version):
        return
    
    if (user_want_update()):
        update(mediafire_url)