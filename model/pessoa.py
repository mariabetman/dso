from abc import ABC, abstractmethod
from datetime import datetime


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, data_nasc: datetime):
        if isinstance(nome, str) and isinstance(cpf, str) and isinstance(data_nasc, datetime):
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
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc: datetime):
        if isinstance(data_nasc, datetime):
            self.__data_nasc = data_nasc
