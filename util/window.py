from .window_base import WindowBase
from tkinter import ttk
import tkinter as tk
try:
    from lang import Lang # type: ignore
except ImportError:
    from PT_br import Lang

class Window(tk.Tk, WindowBase):
    def __init__(self):
        tk.Tk.__init__(self, className="com.github.Filipi565.BingSearch")
        WindowBase.__init__(self)
        self.title(Lang.Title)
        self.geometry("300x200")
        self.load_widgets()

    def load_widgets(self):
        menu = ttk.OptionMenu(self, self.level_var, Lang.LevelName.format(1), Lang.LevelName.format(1), Lang.LevelName.format(2))
        menu.place(relx=.5, rely=.1, anchor=tk.CENTER)

        self.button = ttk.Button(self, command=self.start_search, text=Lang.Start)
        self.button.place(relx=.5, rely=.5, anchor=tk.CENTER)

        select_browser = ttk.Button(self, text=Lang.SelectBrowser, command=self.select_browser)
        select_browser.place(relx=.5, rely=.8, anchor=tk.CENTER)

    def start_search(self) -> None:
        self.button.configure(command=self.stop_search, text=Lang.Stop)
        self._start_search(self.__on_finish)

    def stop_search(self) -> None:
        self.button.configure(state="disabled", text=f"{Lang.Stoping}...")
        self.should_stop = True

    def __on_finish(self):
        self.button.configure(command=self.start_search, state="active", text=Lang.Start)