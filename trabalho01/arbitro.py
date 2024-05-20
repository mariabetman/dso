from pessoa import Pessoa
from datetime import datetime


class Arbitro(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nasc:datetime):
        if isinstance(nome, str) and isinstance(cpf, str) and isinstance(data_nasc, datetime):
            super().__init__(nome, cpf, data_nasc)
            self.__num_partidas = 0

    @property
    def num_partidas(self):
        return self.__num_partidas

    def adiciona_partida(self):
        self.__num_partidas += 1
    
    def remove_partida(self):
        self.__num_partidas -= 1
