from curso import Curso


class Universidade:
    def __init__(self, nome: str, sigla: str):
        if isinstance(nome, str) and isinstance(sigla, str):
            self.__nome = nome
            self.__sigla = sigla
            self.__cursos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla

    @sigla.setter
    def sigla(self, sigla: str):
        if isinstance(sigla, ):
            self.__sigla = sigla

    @property
    def cursos(self):
        return self.__cursos

    @cursos.setter
    def cursos(self, cursos: list):
        if isinstance(cursos, list):
            self.__cursos = cursos

    def adicionar_curso(self, codigo: int, nome: str):
        if isinstance(codigo, int) and isinstance(nome, str):
            for curso in self.__cursos:
                if curso.codigo == codigo:
                    return
            self.__cursos.append(Curso(codigo, nome))

    def remover_curso(self, codigo: int):
        if isinstance(codigo, int):
            for curso in self.__cursos:
                if curso.codigo == codigo:
                    self.__cursos.remove(curso)




