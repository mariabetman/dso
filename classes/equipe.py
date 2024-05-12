from curso import Curso


class Equipe:
    def __init__(self, curso: Curso, nome:str, codigo:int):
        if isinstance(curso, Curso) and isinstance(nome, str) and isinstance(codigo, int):
            self.__curso = curso
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
    
    @pontos.setter
    def pontos(self, pontos):
        if isinstance(pontos, int):
            self.__pontos = pontos
            
    @property
    def gols_marcados(self):
        return self.__gols_marcados
    
    @gols_marcados.setter
    def gols_marcados(self, gols_marcados):
        if isinstance(gols_marcados, int):
            self.__gols_marcados = gols_marcados
            
    @property
    def gols_sofridos(self):
        return self.__gols_sofridos
    
    @gols_sofridos.setter
    def gols_sofridos(self, gols_sofridos):
        if isinstance(gols_sofridos, int):
            self.__gols_sofridos = gols_sofridos
            
