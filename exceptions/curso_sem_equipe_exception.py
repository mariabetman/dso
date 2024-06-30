class CursoSemEquipeException(Exception):
    def __init__(self, codigo):
        self.mensagem = "O curso com código {} não possui equipe!"
        super().__init__(self.mensagem.format(codigo))