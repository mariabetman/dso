from DAOs.dao import DAO
from model.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.matricula, int)):
            super().add(aluno.matricula, aluno)

    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.matricula, int)):
            super().update(aluno.matricula, aluno)

    def get(self, matricula: int):
        if isinstance(matricula, int):
            return super().get(matricula)

    def remove(self, matricula: int):
        if(isinstance(matricula, int)):
            return super().remove(matricula)
        
