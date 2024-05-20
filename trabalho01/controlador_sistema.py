from random import randint
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
        self.__controlador_cursos = ControladorCursos(self)
        self.__controlador_alunos = ControladorAlunos(self)
        self.__controlador_equipes = ControladorEquipes(self)
        self.__controlador_arbitros = ControladorArbitros(self)
        self.__controlador_campeonatos = ControladorCampeonatos(self)
        self.__controlador_partidas = ControladorPartidas(self)

    @property
    def controlador_cursos(self):
        return self.__controlador_cursos
    
    @property
    def controlador_alunos(self):
        return self.__controlador_alunos
    
    @property
    def controlador_equipes(self):
        return self.__controlador_equipes
    
    @property
    def controlador_arbitros(self):
        return self.__controlador_arbitros

    @property
    def controlador_campeonatos(self):
        return self.__controlador_campeonatos
    
    @property
    def controlador_partidas(self):
        return self.__controlador_partidas

    def inicializa_sistema(self):
        self.__tela_sistema.mostra_mensagem('Bem-vindo ao sistema de gerenciamento de campeonato universitário!')
        self.abre_tela()

    def abre_tela_curso(self):
        return self.__controlador_cursos.abre_tela()
    
    def abre_tela_aluno(self):
        return self.__controlador_alunos.abre_tela()
    
    def abre_tela_equipe(self):
        return self.__controlador_equipes.abre_tela()
    
    def abre_tela_arbitro(self):
        return self.__controlador_arbitros.abre_tela()
    
    def abre_tela_partida(self):
        return self.__controlador_partidas.abre_tela()
    
    def inicia_campeonato(self):
        codigo_aleatorio = randint(1, 100)
        equipes = self.__controlador_equipes.equipes
        self.__controlador_campeonatos.inclui_campeonato(codigo_aleatorio, equipes)
        return self.__tela_sistema.mostra_mensagem('\nCampeonato iniciado com sucesso! As partidas foram geradas e agora só basta adicionar os resultados!\n')
    
    def finaliza_campeonato(self):
        return self.__controlador_campeonatos.finaliza_campeonato()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mensagem('Até logo!')
        exit(0)

    def abre_tela(self):
        lista_opcoes = {'1': self.abre_tela_curso, '2': self.abre_tela_aluno, '3': self.abre_tela_equipe,
                        '4': self.abre_tela_arbitro, '5': self.inicia_campeonato, '6': self.finaliza_campeonato, '0': self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_sistema.mostra_mensagem('ERRO: Opção inválida!\n')

if __name__ == '__main__':
    ctrl = ControladorSistema()
    print(ctrl.controlador_cursos)
    print(ctrl.controlador_cursos.controlador_sistema)
    print(ctrl.controlador_cursos.controlador_sistema.controlador_cursos)
    print(ctrl.controlador_cursos.controlador_sistema.controlador_cursos.controlador_sistema)
