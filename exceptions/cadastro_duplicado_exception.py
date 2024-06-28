class CadastroDuplicadoException(Exception):
    def __init__(self, identificador):
        self.mensagem = "ERRO! {} já cadastrado(a)"
        super().__init__(self.mensagem.format(identificador))