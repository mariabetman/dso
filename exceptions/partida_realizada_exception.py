class PartidaRealizadaException(Exception):
    def __init__(self):
        self.mensagem = "Partida já realizada!"
        super().__init__(self.mensagem)