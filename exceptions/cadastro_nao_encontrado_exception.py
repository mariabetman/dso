class CadastroNaoEncontradoException(Exception):
    def __init__(self, classe):
        self.mensagem = "{} não encontrado(a)"
        super().__init__(self.mensagem.format(classe))