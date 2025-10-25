from tkinter import StringVar
from util import StrEnum

class Lang(StrEnum):
    Title = ""
    ErrorTitle = ""
    ErrorMessage = ""
    LevelName = ""
    Start = ""
    InvalidLevelError = ""

    @staticmethod
    def get_level_by_var(level_var: StringVar) -> int: ...