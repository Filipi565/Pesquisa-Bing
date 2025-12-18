from .window_base import WindowBase
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
try:
    from lang import Lang # type: ignore
except ImportError:
    from PT_br import Lang

def _entry_validator(P: str) -> bool:
    "Validate value P. Makes sure P is always a number"
    return P.isdigit() or P == ""

def _place_top(widget: tk.Widget) -> None:
    widget.place(relx=.5, rely=.2, anchor=tk.CENTER)

class Window(tk.Tk, WindowBase):
    def __init__(self):
        tk.Tk.__init__(self, className="com.github.Filipi565.BingSearch")
        WindowBase.__init__(self)

        self.title(Lang.Title)
        self.geometry("600x400")

        self.load_widgets()

    def load_widgets(self):
        self.top_label = ttk.Label(self, text=f"{Lang.TypeSearchesNumber}:")

        self.menu = ttk.OptionMenu(self, self._level_var, Lang.LevelName.format(1), Lang.LevelName.format(1), Lang.LevelName.format(2))
        _place_top(self.menu)

        self.extra_searches_btn = ttk.Checkbutton(self, variable=self._extra_searches_var, text=Lang.ExtraSearches)

        advanced_button = ttk.Checkbutton(self, variable=self._advanced_mode_var, text=Lang.AdvancedMode, command=self.update_gui)
        advanced_button.place(relx=.5, rely=.4, anchor=tk.CENTER)

        validator_command = (self.register(_entry_validator), '%P')
        self.search_count_entry = ttk.Entry(self, textvariable=self._search_count_var, validatecommand=validator_command, validate="key")

        self.button = ttk.Button(self, command=self.start_search, text=Lang.Start)
        self.button.place(relx=.5, rely=.6, anchor=tk.CENTER)

        select_browser = ttk.Button(self, text=Lang.SelectBrowser, command=self.select_browser)
        select_browser.place(relx=.5, rely=.8, anchor=tk.CENTER)

    def update_gui(self):
        if (self.advanced_mode):
            self.menu.place_forget()
            _place_top(self.search_count_entry)
            self.top_label.place(relx=.5, rely=.1, anchor=tk.CENTER)
            self.extra_searches_btn.place(relx=.5, rely=.3, anchor=tk.CENTER)
        else:
            self.search_count_entry.place_forget()
            self.extra_searches_btn.place_forget()
            self.top_label.place_forget()
            _place_top(self.menu)

    def start_search(self) -> None:
        if (self.advanced_mode and not self._search_count_var.get()):
            messagebox.showwarning(Lang.ErrorTitle, Lang.TypeANumberError)
            return

        self.button.configure(command=self.stop_search, text=Lang.Stop)
        self._start_search(self.__on_finish)

    def stop_search(self) -> None:
        self.button.configure(state="disabled", text=f"{Lang.Stoping}...")
        self.should_stop = True

    def __on_finish(self):
        self.button.configure(command=self.start_search, state="active", text=Lang.Start)