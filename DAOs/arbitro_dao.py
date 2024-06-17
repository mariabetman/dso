from DAOs.dao import DAO
from model.arbitro import Arbitro

#cada entidade terá uma classe dessa, implementação bem simples.
class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitros.pkl')

    def add(self, arbitro: Arbitro):
        if((arbitro is not None) and isinstance(arbitro, Arbitro) and isinstance(arbitro.cpf, str)):
            super().add(arbitro.cpf, arbitro)

    def update(self, arbitro: Arbitro):
        if((arbitro is not None) and isinstance(arbitro, Arbitro) and isinstance(arbitro.cpf, str)):
            super().update(arbitro.cpf, arbitro)

    def get(self, cpf:str):
        if isinstance(str, str):
            return super().get(cpf)

    def remove(self, cpf):
        if(isinstance(cpf, str)):
            print('if do dao arbitro')
            return super().remove(cpf)