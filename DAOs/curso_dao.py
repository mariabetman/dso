from DAOs.dao import DAO
from model.curso import Curso

class CursoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.codigo, int)):
            super().add(curso.codigo, curso)

    def update(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.codigo, int)):
            super().update(curso.codigo, curso)

    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if(isinstance(codigo, int)):
            return super().remove(codigo)