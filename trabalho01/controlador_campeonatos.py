from datetime import datetime, timedelta
from random import random
from campeonato import Campeonato
from tela_campeonato import TelaCampeonato
from equipe import Equipe
from partida import Partida

class ControladorCampeonatos:
    def __init__(self, controlador_sistema):
        self.__campeonato = None
        self.__tela_campeonato = TelaCampeonato(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
        
    def inclui_campeonato(self, codigo:int , equipes):
        campeonato = Campeonato(codigo, equipes)
        self.__campeonato = campeonato
        self.__tela_campeonato.mostra_mensagem('\nCampeonato cadastrado com sucesso!\n')
        self.cria_partidas_do_campeonato()
    
    def cria_partidas_do_campeonato(self):
        if self.__campeonato and len(self.__campeonato.equipes) > 1:
            equipes = self.__campeonato.equipes
            num_equipes = len(equipes)
            partidas_geradas = []

            for i in range(num_equipes):
                for j in range(i + 1, num_equipes):
                    data_aleatoria = datetime.now() + timedelta(days=random.randint(1, 30))
                    arbitro_aleatorio = random.choice(self.__controlador_sistema.controlador_arbitros.arbitros)
                    partida = Partida(
                        codigo = len(partidas_geradas) + 1,
                        data_partida = data_aleatoria,
                        equipe_casa = equipes[i],
                        equipe_visitante = equipes[j],
                        arbitro = arbitro_aleatorio
                    )
                    self.__campeonato.adiciona_partida(partida)

            self.__tela_campeonato.mostra_mensagem('\nPartidas geradas com sucesso!\n')
        else:
            self.__tela_campeonato.mostra_mensagem('\nNão há equipes suficientes no campeonato para gerar partidas.\n')
            self.__retorna()

    def finaliza_campeonato(self):
        todas_partidas_realizadas = True
        for partida in self.__campeonato.partidas:
            if not partida.partida_realizada:
                todas_partidas_realizadas = False

        if todas_partidas_realizadas:
            self.gera_relatorio(self.__campeonato)
            self.__controlador_sistema.tela.mostra_mensagem('\nCampeonato finalizado com sucesso!\n')
            self.__controlador_sistema.encerra_sistema()
        else:
            self.__tela_campeonato.mostra_mensagem('\nAinda faltam partidas a serem realizadas!\n')
            self.retorna()

    def gera_relatorio(self):
        campeonato = self.__campeonato

        equipes = campeonato.equipes
        jogadores = {aluno for equipe in equipes for aluno in equipe.jogadores}
        equipes_ordenadas = sorted(equipes, key=lambda e: (e.pontos, e.gols_marcados), reverse=True)

        ganhadores = equipes_ordenadas[:3]
        mais_gols_marcados = max(equipes, key=lambda e: e.gols_marcados)
        mais_gols_sofridos = max(equipes, key=lambda e: e.gols_sofridos)
        artilheiros = sorted(jogadores, key=lambda j: j.gols, reverse=True)[:3]

        relatorio = f"""
        Relatório do Campeonato:
        
        1º Lugar: {ganhadores[0].nome} com {ganhadores[0].pontos} pontos e {ganhadores[0].gols_marcados}
        2º Lugar: {ganhadores[1].nome} com {ganhadores[1].pontos} pontos e {ganhadores[1].gols_marcados}
        3º Lugar: {ganhadores[2].nome} com {ganhadores[2].pontos} pontos e {ganhadores[2].gols_marcados}

        Equipe com mais gols marcados: {mais_gols_marcados.nome} com {mais_gols_marcados.gols_marcados} gols
        Equipe que levou mais gols: {mais_gols_sofridos.nome} com {mais_gols_sofridos.gols_sofridos} gols

        Jogadores com mais gols marcados:
        1. {artilheiros[0].nome} com {artilheiros[0].gols} gols
        2. {artilheiros[1].nome} com {artilheiros[1].gols} gols
        3. {artilheiros[2].nome} com {artilheiros[2].gols} gols
        """
        self.__tela_campeonato.mostra_mensagem(relatorio)

    def retorna(self):
        self.__controlador_sistema.abre_tela()
