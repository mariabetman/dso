class CampeonatoNaoIniciadoException(Exception):
    def __init__(self):
        self.mensagem = "Campeonato não iniciado!"
        super().__init__(self.mensagem)