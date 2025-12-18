import util

class Lang(util.StrEnum):
    Title: str
    ErrorTitle: str
    ErrorMessage: str
    LevelName: str
    Start: str
    Stop: str
    Stoping: str
    InvalidLevelError: str
    SelectBrowser: str
    Executables: str
    UpdateMessage: str
    AdvancedMode: str
    TypeSearchesNumber: str
    TypeANumberError: str
    ExtraSearches: str

    @staticmethod
    def get_level_by_str(text: str) -> int: ...