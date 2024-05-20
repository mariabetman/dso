from pessoa import Pessoa
from curso import Curso
from datetime import datetime


class Aluno(Pessoa):
    def __init__(self, matricula: int, curso: Curso, nome: str, cpf: str, data_nasc: datetime):
        if isinstance(curso, Curso) and isinstance(matricula, int) and isinstance(nome, str) and isinstance(cpf, str) and isinstance(data_nasc, datetime):
            super().__init__(nome, cpf, data_nasc)
            self.__matricula = matricula
            self.__curso = curso
            self.__num_gols = 0
          
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula:int):
        if isinstance(matricula, int):
            self.__matricula = matricula
    
    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso:Curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    @property
    def num_gols(self):
        return self.__num_gols

    def adiciona_gols(self):
        self.__num_gols += 1
    
    def remove_gols(self):
        self.__num_gols -= 1
