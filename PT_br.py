import util

class Lang(util.StrEnum):
    Title = "Pesquisa Bing"
    ErrorTitle = "Erro"
    ErrorMessage = "Error ao obter conjunto de palavras, verifique sua internet e tente novamente mais tarde. Código de Erro: {}"
    LevelName = "Nível {}"
    Start = "Iniciar"
    Stop = "Parar"
    Stoping = "Parando"
    InvalidLevelError = "Nível inválido"
    SelectBrowser = "Selecionar Navegador"
    Executables = "Executáveis"
    UpdateMessage = "Pesquisa Bing obteve uma nova atualização, deseja atualizar?"

    @staticmethod
    def get_level_by_str(text: str) -> int:
        return int(text[-1])


del util