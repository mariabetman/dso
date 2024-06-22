from DAOs.dao import DAO
from model.equipe import Equipe

class EquipeDAO(DAO):
    def __init__(self):
        super().__init__('equipes.pkl')

    def add(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance(equipe.codigo, int)):
            super().add(equipe.codigo, equipe)

    def update(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance(equipe.codigo, int)):
            super().update(equipe.codigo, equipe)

    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if(isinstance(codigo, int)):
            return super().remove(codigo)