class OpcaoInvalidaException(Exception):
    def __init__(self):
        self.mensagem = "Opção inválida! Selecione uma das opções disponíveis."
        super().__init__(self.mensagem)