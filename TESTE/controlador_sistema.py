from controlador_alunos import ControladorAluno
from controlador_arbitros import ControladorArbitro
from controlador_campeonato import ControladorCampeonato
from controlador_cursos import ControladorCurso
from controlador_equipes import ControladorEquipe
from controlador_partidas import ControladorPartida

from tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_cursos = ControladorCurso(self)
        self.__controlador_alunos = ControladorAluno(self)
        self.__controlador_equipes = ControladorEquipe(self)
        self.__controlador_arbitros = ControladorArbitro(self)
        self.__controlador_campeonatos = ControladorCampeonato(self)
        self.__controlador_partidas = ControladorPartida(self)

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos

    @property
    def controlador_cursos(self):
        return self.__controlador_cursos

    def inicializa_sistema(self):
        self.abre_tela()

    def tela_cursos(self):
        return self.__controlador_cursos.abre_tela()
    
    def tela_alunos(self):
        return self.__controlador_alunos.abre_tela()
    
    def tela_equipes(self):
        return self.__controlador_equipes.abre_tela()
    
    def tela_arbitros(self):
        return self.__controlador_arbitros.abre_tela()
    
    def tela_campeonatos(self):
        return self.__controlador_campeonatos.abre_tela()
    
    def tela_partidas(self):
        return self.__controlador_partidas.abre_tela()

    def encerrar_programa():
        return quit()
         

    def abre_tela(self):
        lista_opcoes = {
            1: self.tela_cursos,
            2: self.tela_alunos,
            3: self.tela_equipes,
            4: self.tela_arbitros,
            5: self.tela_campeonatos,
            6: self.tela_partidas,
            0: self.encerrar_programa
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

if __name__ == '__main__':
    ctrl = ControladorSistema()
    print(ctrl.controlador_cursos)
    print(ctrl.controlador_cursos.controlador_sistema)
    print(ctrl.controlador_cursos.controlador_sistema.controlador_cursos)
    print(ctrl.controlador_cursos.controlador_sistema.controlador_cursos.controlador_sistema)