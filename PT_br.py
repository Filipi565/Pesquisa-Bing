import tkinter as tk
import util

class Lang(util.StrEnum):
    Title = "Pesquisa Bing"
    ErrorTitle = "Erro"
    ErrorMessage = "Error ao obter conjunto de palavras, verifique sua internet e tente novamente mais tarde. Código de Erro: {}"
    LevelName = "Nível {}"
    Start = "Iniciar"
    InvalidLevelError = "Nível inválido"
    SelectBrowser = "Selecionar Navegador"
    Executables = "Executáveis"

    @staticmethod
    def get_level_by_var(level_var: tk.StringVar) -> int:
        result = level_var.get()

        return int(result.replace("Nível ", ""))


del util