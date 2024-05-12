from equipe import Equipe


class Partida:
    def __init__(self, codigo:int, equipe_casa:Equipe, equipe_visitante:Equipe):
        self.__codigo = codigo
        self.__data_partida = None
        self.__equipe_casa = equipe_casa
        self.__equipe_visitante = equipe_visitante
        self.__gols_equipe_casa = None
        self.__gols_equipe_visitante = None
        self.__resultado = None #Verificar
        self.__partida_realizada = False
        
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
    
    @property
    def data_partida(self):
        return self.__data_partida

    @data_partida.setter
    def data_partida(self, data_partida):
        if isinstance(data_partida, str):
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
    def gols_equipe_casa(self):
        return self.__gols_equipe_casa

    @gols_equipe_casa.setter
    def gols_equipe_casa(self, gols_equipe_casa):
        if isinstance(gols_equipe_casa, int):
            self.__gols_equipe_casa = gols_equipe_casa
      
    @property      
    def gols_equipe_visitante(self):
        return self.__gols_equipe_visitante

    @gols_equipe_visitante.setter
    def gols_equipe_visitante(self, gols_equipe_visitante):
        if isinstance(gols_equipe_visitante, int):
            self.__gols_equipe_visitante = gols_equipe_visitante
      
    @property      
    def resultado(self):
        return self.__resultado

    @property
    def partida_realizada(self):
        return self.__partida_realizada

    @partida_realizada.setter
    def partida_realizada(self, partida_realizada):
        if isinstance(partida_realizada, bool):
            self.__partida_realizada = partida_realizada
        