from aluno import Aluno
from equipe import Equipe
from partida import Partida


class Campeonato:
    def __init__(self, codigo:int):
        if isinstance(codigo, int):
            self.__codigo = codigo
            self.__equipes = []
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

    def adiciona_gol_artilharia(self, gols:int, aluno:Aluno):
        if self.__artilharia[aluno]:
            gols_atuais = self.__artilharia[aluno]
            self.__artilharia[aluno] = self.__artilharia[aluno] + gols
        else:
            self.__artilharia[aluno] = gols
    
    def remove_gol_artilharia(self, gols:int, aluno:Aluno):
        if self.__artilharia[aluno]:
            gols_atuais = self.__artilharia[aluno]
            self.__artilharia[aluno] = self.__artilharia[aluno] - gols
