from .process_path import get_process_path, set_process_path, HERE
from .quote import get_random_quote
from tkinter import filedialog
from threading import Thread
from typing import Union
import subprocess as sp
import tkinter as tk
import random
import time
import os
try:
    from lang import Lang # type: ignore
except ImportError:
    from PT_br import Lang

class WindowBase:
    def __init__(self, root: Union[tk.Misc, None] = None):
        self.level_var = tk.StringVar(root)
        self.should_stop = False

    def _start_search(self, on_finish):
        t = Thread(target=start_search, args=[self, on_finish])
        t.start()

    def select_browser(self):
        path = filedialog.askopenfilename(
            defaultextension=".exe",
            filetypes=[(Lang.Executables, "*.exe")]
        )

        if (path):
            set_process_path(path)

def start_search(window: WindowBase, on_finish) -> None:
    level = Lang.get_level_by_str(window.level_var.get())
    if (level == 1):
        search_count = 10
    elif (level == 2):
        search_count = 30
    else:
        raise RuntimeError(Lang.InvalidLevelError)
    
    search_count = int(1.5 * search_count)

    quotes_searched: set[str] = {"wikipedia"}

    process_path = get_process_path()
    with open(os.path.join(HERE, "dictionary.txt"), "rb") as f:
        items = f.read().splitlines()

    for _ in range(search_count):
        if (window.should_stop):
            break
        while True:
            quote = get_random_quote(random.choice(items)).replace(" ", "%20")
            if (quote not in quotes_searched):
                quotes_searched.add(quote)
                break
            
        sp.Popen([process_path, "--single-argument", f"https://www.bing.com/search?q={quote}&qs=n&form=QBRE&sp=-1&lq=0&pq=mercado+liv&sc=0-11&sk=&cvid=A0BDCD943A0A4E94A1D7A8B319714C88"])
        time.sleep(random.randint(50, 100) / 10)

    on_finish()
    window.should_stop = False