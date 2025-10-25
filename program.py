from threading import Thread
from tkinter import ttk
import subprocess as sp
import tkinter as tk
import random
import time
import sys
import os

try:
    from lang import Lang
except ImportError:
    from PT_br import Lang

def get_process_path() -> str:
    here = os.path.abspath(os.path.join(sys.argv[0], ".."))

    with open(os.path.join(here, "process_path.txt"), "r") as f:
        return f.read()
    
def get_random_quote(word: bytes) -> str:
    items = (b"what is {}", b"{}", b"{} what means", b"{} dictionary means", b"tradu\xe7\xe3o", b"{} wiki", b"wikipedia")

    while True:
        try:
            return random.choice(items).replace(b"{}", word).decode()
        except UnicodeError:
            pass

def start_search(level_var: tk.StringVar, should_quit: list[bool]) -> None:
    here = os.path.abspath(os.path.join(sys.argv[0], ".."))
    level = Lang.get_level_by_var(level_var)
    if (level == 1):
        search_count = 10
    elif (level == 2):
        search_count = 30
    else:
        raise RuntimeError(Lang.InvalidLevelError)

    quotes_searched: set[str] = {"wikipedia"}

    process_path = get_process_path()
    with open(os.path.join(here, "dictionary.txt"), "rb") as f:
        items = f.read().splitlines()

    for _ in range(search_count):
        if (should_quit[0]):
            return
        while True:
            quote = get_random_quote(random.choice(items)).replace(" ", "%20")
            if (quote not in quotes_searched):
                quotes_searched.add(quote)
                break
            
        sp.Popen([process_path, "--single-argument", f"https://www.bing.com/search?q={quote}&qs=n&form=QBRE&sp=-1&lq=0&pq=mercado+liv&sc=0-11&sk=&cvid=A0BDCD943A0A4E94A1D7A8B319714C88"])
        time.sleep(random.randint(50, 100) / 10)

class Window(tk.Tk):
    def __init__(self):
        super().__init__(className="com.github.Filipi565.BingSearch")
        self.title(Lang.Title)
        self.geometry("300x200")
        self.level_var = tk.StringVar(self)
        self.__should_quit = [False]
        self.load_widgets()

    def load_widgets(self):
        menu = ttk.OptionMenu(self, self.level_var, Lang.LevelName.format(1), Lang.LevelName.format(1), Lang.LevelName.format(2))
        menu.place(relx=.5, rely=.1, anchor=tk.CENTER)

        start_button = ttk.Button(self, command=self.start_search, text=Lang.Start)
        start_button.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def start_search(self):
        t = Thread(target=start_search, args=[self.level_var, self.__should_quit])
        t.start()

    @property
    def should_quit(self) -> bool:
        return self.__should_quit[0]
    
    @should_quit.setter
    def should_quit(self, other) -> None:
        assert isinstance(other, bool)

        self.__should_quit[0] = other

def main():
    window = Window()
    try:
        window.mainloop()
    except BaseException:
        window.should_quit = True

    window.should_quit = True

if __name__ == "__main__":
    main()