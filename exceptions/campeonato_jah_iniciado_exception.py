class CampeonatoJahIniciadoException(Exception):
    def __init__(self):
        self.mensagem = "Campeonato já iniciado!"
        super().__init__(self.mensagem)