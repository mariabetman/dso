from DAOs.dao import DAO
from model.partida import Partida

class PartidaDAO(DAO):
    def __init__(self):
        super().__init__('partidas.pkl')

    def add(self, partida: Partida):
        if((partida is not None) and isinstance(partida, Partida) and isinstance(partida.codigo, int)):
            super().add(partida.codigo, partida)

    def update(self, partida: Partida):
        if((partida is not None) and isinstance(partida, Partida) and isinstance(partida.codigo, int)):
            super().update(partida.codigo, partida)

    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if(isinstance(codigo, int)):
            return super().remove(codigo)