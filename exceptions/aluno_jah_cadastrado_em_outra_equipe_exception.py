class AlunoJahCadastradoEmOutraEquipeException(Exception):
    def __init__(self, codigo):
        self.mensagem = "O aluno já está cadastrado na equipe de código {}"
        super().__init__(self.mensagem.format(codigo))