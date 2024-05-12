from partida import Partida
from equipe import Equipe
from curso import Curso


class Campeonato:
    def __init__(self, codigo:int, equipes:list[Equipe]):
        if isinstance(codigo, int) and all(isinstance(equipe, Equipe) for equipe in equipes):
            self.__codigo = codigo
            self.__equipes = equipes
            self.__partidas = []
            self.__artilharia = {}
            
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
            
    @property
    def equipes(self):
        return self.__equipes

    @equipes.setter
    def equipes(self, equipes):
        if all(isinstance(equipe, Equipe) for equipe in equipes):
            self.__equipes = equipes
            
    @property
    def partidas(self):
        return self.__partidas

    @partidas.setter
    def partidas(self, partidas):
        if all(isinstance(partida, Partida) for partida in partidas):
            self.__partidas = partidas
            
    @property
    def artilharia(self):
        return self.__artilharia