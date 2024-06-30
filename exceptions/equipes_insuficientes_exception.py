class EquipesInsuficientesNaEquipeException(Exception):
    def __init__(self, quantidade_necessaria):
        self.mensagem = "O campeonato deve ter pelo menos duas equipes!"
        super().__init__(self.mensagem)