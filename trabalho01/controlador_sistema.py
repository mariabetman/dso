from controlador_alunos import ControladorAlunos
from controlador_arbitros import ControladorArbitros
from controlador_campeonatos import ControladorCampeonatos
from controlador_cursos import ControladorCursos
from controlador_equipes import ControladorEquipes
from controlador_partidas import ControladorPartidas

from tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_alunos = ControladorAlunos(self)
        self.__controlador_cursos = ControladorCursos(self)
        self.__controlador_arbitros = ControladorArbitros(self)
        self.__controlador_equipes = ControladorEquipes(self)
        self.__controlador_campeonatos = ControladorCampeonatos(self)
        self.__controlador_partidas = ControladorPartidas(self)
        self.__tela_sistema = TelaSistema(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela_curso(self):
        self.__controlador_cursos.abre_tela()
    
    def abre_tela_aluno(self):
        self.__controlador_alunos.abre_tela()
    
    def abre_tela_equipe(self):
        self.__controlador_equipes.abre_tela()

    def abre_tela_arbitro(self):
        self.__controlador_arbitros.abre_tela()

    def abre_tela_campeonato(self):
        self.__controlador_campeonatos.abre_tela()
    
    def abre_tela_partida(self):
        self.__controlador_partidas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.abre_tela_curso, 2: self.abre_tela_aluno, 3: self.abre_tela_equipe,
                        4: self.abre_tela_arbitro, 5: self.abre_tela_campeonato, 6: self.abre_tela_partida, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

if __name__ == '__main__':
    print(1)
