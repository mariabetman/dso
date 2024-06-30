class PartidasNaoRealizadasException(Exception):
    def __init__(self):
        self.mensagem = "Existem partidas não realizadas em seu campeonato! Finalize todas antes de encerrar o campeonato!"
        super().__init__(self.mensagem)