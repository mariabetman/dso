class ErroInesperadoException(Exception):
    def __init__(self, erro):
        self.mensagem = "Erro ao {}"
        super().__init__(self.mensagem.format(erro))