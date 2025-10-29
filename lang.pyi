from tkinter import StringVar
import util

class Lang(util.StrEnum):
    Title: str
    ErrorTitle: str
    ErrorMessage: str
    LevelName: str
    Start: str
    InvalidLevelError: str
    SelectBrowser: str
    Executables: str
    UpdateMessage: str

    @staticmethod
    def get_level_by_var(level_var: StringVar) -> int: ...