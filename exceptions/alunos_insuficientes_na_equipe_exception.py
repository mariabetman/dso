class AlunosInsuficientesNaEquipeException(Exception):
    def __init__(self, quantidade_necessaria):
        self.mensagem = "Alunos insuficientes em pelo menos uma das equipes! Cada equipe deve ter pelo menos {} alunos"
        super().__init__(self.mensagem.format(quantidade_necessaria))