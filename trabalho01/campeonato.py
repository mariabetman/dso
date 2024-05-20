from equipe import Equipe
from partida import Partida


class Campeonato:
    def __init__(self, codigo:int, equipes):
            if isinstance(codigo, int) and all(isinstance(equipe, Equipe) for equipe in equipes):
                self.__codigo = codigo
                self.__equipes = equipes
                self.__partidas = []
                self.__campeonato_iniciado = False
            
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
    
    def adiciona_equipe(self, equipe:Equipe):
        self.__equipes.append(equipe)
    
    def remove_equipe(self, equipe:Equipe):
        self.__equipes.remove(equipe)
            
    @property
    def partidas(self):
        return self.__partidas

    def adiciona_partida(self, partida:Partida):
        self.__partidas.append(partida)
    
    def remove_partida(self, partida:Partida):
        self.__partidas.remove(partida)
            
    @property
    def artilharia(self):
        return self.__artilharia
    
    @property
    def campeonato_iniciado(self):
        return self.__campeonato_iniciado
    
    @campeonato_iniciado.setter
    def campeonato_iniciado(self, campeonato_iniciado:bool):
        if isinstance(campeonato_iniciado, bool):
            self.__campeonato_iniciado = campeonato_iniciado
