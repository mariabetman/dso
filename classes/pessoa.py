from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: int, data_nasc: str):
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(data_nasc, str):
            self.__nome = nome
            self.__cpf = cpf
            self.__data_nasc = data_nasc

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc: str):
        if isinstance(data_nasc, str):
            self.__data_nasc = data_nasc

    @abstractmethod 
    def desempenho(self): # para aluno: gols e partidas; para árbitro: partidas. Ver se isso faz sentido... ou colocar um método "papel" (aluno ou árbitro)?
        pass

