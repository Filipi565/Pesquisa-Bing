from tkinter import StringVar
import util

class Lang(util.StrEnum):
    Title = ""
    ErrorTitle = ""
    ErrorMessage = ""
    LevelName = ""
    Start = ""
    InvalidLevelError = ""

    @staticmethod
    def get_level_by_var(level_var: StringVar) -> int: ...