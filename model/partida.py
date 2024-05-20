from datetime import datetime
from model.aluno import Aluno
from model.equipe import Equipe
from model.arbitro import Arbitro


class Partida:
    def __init__(self, codigo:int, data_partida:datetime, equipe_casa:Equipe, equipe_visitante:Equipe, arbitro:Arbitro):
        self.__codigo = codigo
        self.__data_partida = data_partida
        self.__equipe_casa = equipe_casa
        self.__equipe_visitante = equipe_visitante
        self.__arbitro = arbitro
        self.__gols_equipe_casa = None
        self.__artilheiros_equipe_casa = None
        self.__gols_equipe_visitante = None
        self.__artilheiros_equipe_visitante = None
        self.__resultado = None
        self.__partida_realizada = False
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def data_partida(self):
        return self.__data_partida

    @data_partida.setter
    def data_partida(self, data_partida):
        if isinstance(data_partida, datetime):
            self.__data_partida = data_partida
    
    @property        
    def equipe_casa(self):
        return self.__equipe_casa

    @equipe_casa.setter
    def equipe_casa(self, equipe_casa):
        if isinstance(equipe_casa, Equipe):
            self.__equipe_casa = equipe_casa
    
    @property      
    def equipe_visitante(self):
        return self.__equipe_visitante

    @equipe_visitante.setter
    def equipe_visitante(self, equipe_visitante):
        if isinstance(equipe_visitante, Equipe):
            self.__equipe_visitante = equipe_visitante
    
    @property      
    def arbitro(self):
        return self.__arbitro

    @arbitro.setter
    def arbitro(self, arbitro):
        if isinstance(arbitro, Arbitro):
            self.__arbitro = arbitro
    
    @property     
    def gols_equipe_casa(self):
        return self.__gols_equipe_casa

    @gols_equipe_casa.setter
    def gols_equipe_casa(self, gols_equipe_casa):
        if isinstance(gols_equipe_casa, int):
            self.__gols_equipe_casa = gols_equipe_casa
      
    @property     
    def artilheiros_equipe_casa(self):
        return self.__artilheiros_equipe_casa

    @artilheiros_equipe_casa.setter
    def artilheiros_equipe_casa(self, artilheiros_equipe_casa):
        if all(isinstance(artilheiro, Aluno) for artilheiro in artilheiros_equipe_casa):
            self.__artilheiros_equipe_casa = artilheiros_equipe_casa

    @property      
    def gols_equipe_visitante(self):
        return self.__gols_equipe_visitante

    @gols_equipe_visitante.setter
    def gols_equipe_visitante(self, gols_equipe_visitante):
        if isinstance(gols_equipe_visitante, int):
            self.__gols_equipe_visitante = gols_equipe_visitante
    
    @property     
    def artilheiros_equipe_visitante(self):
        return self.__artilheiros_equipe_visitante

    @artilheiros_equipe_visitante.setter
    def artilheiros_equipe_visitante(self, artilheiros_equipe_visitante):
        if all(isinstance(artilheiro, Aluno) for artilheiro in artilheiros_equipe_visitante):
            self.__artilheiros_equipe_visitante = artilheiros_equipe_visitante
      
    @property      
    def resultado(self):
        return self.__resultado
    
    @resultado.setter     
    def resultado(self, resultado):
        if isinstance(resultado, str):
            self.__resultado = resultado

    @property
    def partida_realizada(self):
        return self.__partida_realizada

    @partida_realizada.setter
    def partida_realizada(self, partida_realizada):
        if isinstance(partida_realizada, bool):
            self.__partida_realizada = partida_realizada
        