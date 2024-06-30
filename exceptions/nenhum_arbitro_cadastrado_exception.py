class NenhumArbitroCadastradoException(Exception):
    def __init__(self):
        self.mensagem = "Pelo menos um árbitro deve estar cadastrado para iniciar o campeonato!"
        super().__init__(self.mensagem)