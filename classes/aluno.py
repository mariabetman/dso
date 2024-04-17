from pessoa import Pessoa
from curso import Curso
from universidade import Universidade


class Aluno(Pessoa):
    def __init__(self, universidade: Universidade, curso: Curso, matricula: int, nome: str, cpf: int, data_nasc: str):
        if isinstance(universidade, Universidade) and isinstance(curso, Curso) and isinstance(matricula, int) and isinstance(nome, str) and isinstance(cpf, int) and isinstance(data_nasc, str):
            super().__init__(nome, cpf, data_nasc)
            self.__universidade = universidade
            self.__curso = curso
            self.__matricula = matricula

    @property
    def universidade(self):
        return self.__universidade

    @universidade.setter
    def universidade(self, universidade):
        if isinstance(universidade, Universidade):
            self.__universidade = universidade

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, int):
            self.__matricula = matricula

    def desempenho(self):
        return 