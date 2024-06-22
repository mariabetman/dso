class AlunoDeCursoDiferenteDaEquipeException(Exception):
    def __init__(self):
        self.mensagem = "O aluno e a equipe selecionados precisam ser do mesmo curso"
        super().__init__(self.mensagem)