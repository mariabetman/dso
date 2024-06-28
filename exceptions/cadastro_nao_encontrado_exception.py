class CadastroNaoEncontradoException(Exception):
    def __init__(self, classe):
        self.mensagem = "{} não encontrado"
        super().__init__(self.mensagem.format(classe))