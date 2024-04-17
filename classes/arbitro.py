from pessoa import Pessoa


class Arbitro(Pessoa):
    def __init__(self, nome: str, cpf: int, data_nasc: str):
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(data_nasc, str):
            super().__init__(nome, cpf, data_nasc)
            self.__num_partidas = 0

    @property
    def num_partidas(self):
        return self.__num_partidas

    @num_partidas.setter
    def num_partidas(self, num_partidas: int):
        if isinstance(num_partidas, int):
            self.__num_partidas = num_partidas

    def adicionar_partida(self): # Ver se aqui vale a pena manter um registro das partidas ou somente a quantidade mesmo
        self.__num_partidas += 1

    def desempenho(self):
        return 