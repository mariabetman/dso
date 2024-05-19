from curso import Curso
from aluno import Aluno


class Equipe:
    def __init__(self, curso: Curso, nome:str, codigo:int):
        if isinstance(curso, Curso) and isinstance(nome, str) and isinstance(codigo, int):
            self.__curso = curso
            self.__alunos = []
            self.__nome = nome
            self.__codigo = codigo
            self.__pontos = 0
            self.__gols_marcados = 0
            self.__gols_sofridos = 0

    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    @property
    def alunos(self):
        return self.__alunos
    
    def adiciona_aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)
    
    def remove_aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.remove(aluno)

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
             
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
          
    @property
    def pontos(self):
        return self.__pontos
    
    def adiciona_pontos(self, pontos:int):
        if isinstance(pontos, int):
            self.__pontos += pontos
    
    def remove_pontos(self, pontos:int):
        if isinstance(pontos, int):
            self.__pontos -= pontos
            
    @property
    def gols_marcados(self):
        return self.__gols_marcados
    
    def adiciona_gols_marcados(self, gols:int):
        if isinstance(gols, int):
            self.__gols_marcados += gols
    
    def remove_gols_marcados(self, gols:int):
        if isinstance(gols, int):
            self.__gols_marcados -= gols
            
    @property
    def gols_sofridos(self):
        return self.__gols_sofridos
    
    def adiciona_gols_sofridos(self, gols:int):
        if isinstance(gols, int):
            self.__gols_sofridos += gols
    
    def remove_gols_sofridos(self, gols:int):
        if isinstance(gols, int):
            self.__gols_sofridos -= gols
