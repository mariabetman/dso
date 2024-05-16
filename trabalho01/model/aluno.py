from pessoa import Pessoa
from curso import Curso



class Aluno(Pessoa):
    def __init__(self, matricula: int, curso: Curso, nome: str, cpf: str, data_nasc: str):
        if isinstance(curso, Curso) and isinstance(matricula, int) and isinstance(nome, str) and isinstance(cpf, str) and isinstance(data_nasc, str):
            super().__init__(nome, cpf, data_nasc)
            self.__matricula = matricula
            self.__curso = curso
            self.__num_gols = 0
            
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, int):
            self.__matricula = matricula
    
    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    @property
    def num_gols(self):
        return self.__num_gols

    @num_gols.setter
    def num_gols(self, num_gols):
        if isinstance(num_gols, int):
            self.__num_gols = num_gols
