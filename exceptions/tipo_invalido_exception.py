class TipoInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "ERRO: O tipo de um dos campos é inválido!"
        super().__init__(self.mensagem)