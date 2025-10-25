from version import version as current_version, Version
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from typing import Union
import zipfile
import sys
import io
import os

def get_content(url: str) -> Union[bytes, None]:
    try:
        with urlopen(url) as f:
            return f.read()
    except HTTPError:
        return None

def download_zip_file(url: str) -> Union[zipfile.ZipFile, None]:
    content = get_content(url)
    
    if (content):
        return zipfile.ZipFile(io.BytesIO(content), "r")
    
def get_dl_url(url: str) -> str:
    content = get_content(url)
    if not (content):
        return ""
    
    soup = BeautifulSoup(content, "html.parser")
    button = soup.find("a", id="downloadButton")
    if not (button):
        return ""
    
    return str(button.get("href", ""))

def main():
    lib_folder = os.path.abspath(os.path.join(sys.argv[0], "..", "lib"))

    content_b = get_content("https://pastebin.com/raw/nQZRsXvJ")
    if not (content_b):
        return
    
    content = content_b.decode()
    
    version_text, mediafire_url = content.splitlines()

    last_version = Version(*map(int, version_text.split(".")))
    if not (current_version < last_version):
        return

    url = get_dl_url(mediafire_url)
    if not (url):
        return

    file = download_zip_file(url)
    if not file:
        return
    
    file.extractall(lib_folder)