from datetime import datetime, timedelta
from random import randint, choice
from model.campeonato import Campeonato
from view.tela_campeonato import TelaCampeonato
from model.partida import Partida

class ControladorCampeonatos:
    def __init__(self, controlador_sistema):
        self.__campeonato = None
        self.__tela_campeonato = TelaCampeonato(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
        
    def inclui_campeonato(self, codigo:int , equipes):
        if self.__campeonato:
            self.__tela_campeonato.mostra_mensagem('\nCampeonato já iniciado!\n')
            self.retorna()
        else:
            cursos_com_equipes = {curso.codigo: False for curso in self.__controlador_sistema.controlador_cursos.cursos}
        
            for equipe in equipes:
                if len(equipe.alunos) < 11:
                    self.__tela_campeonato.mostra_mensagem('\nUma ou mais equipes têm menos de 11 alunos. Campeonato não pode ser iniciado!\n')
                    self.retorna()
                    return

                if equipe.curso.codigo in cursos_com_equipes:
                    cursos_com_equipes[equipe.curso.codigo] = True
            
            for curso_codigo, tem_equipe in cursos_com_equipes.items():
                if not tem_equipe:
                    self.__tela_campeonato.mostra_mensagem(f'\nCurso com código {curso_codigo} não possui equipe. Campeonato não pode ser iniciado!\n')
                    self.retorna()
                    return

            if len(self.controlador_sistema.controlador_arbitros.arbitros) == 0:
                self.__tela_campeonato.mostra_mensagem(f'\nAdicione pelo menos um árbitro antes de iniciar o campeonato!\n')
                self.retorna()
                return
            
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
                    data_aleatoria = datetime.now() + timedelta(days=randint(1, 30))
                    arbitro_aleatorio = choice(self.__controlador_sistema.controlador_arbitros.arbitros)
                    dados_partida =  {'codigo': len(partidas_geradas) + 1, 'data_partida': data_aleatoria, 'equipe_casa': equipes[i], 'equipe_visitante': equipes[j], 'arbitro': arbitro_aleatorio}
                    partida = self.__controlador_sistema.controlador_partidas.inclui_partida(dados_partida)
                    self.adiciona_partida_campeonato(partida)
                    partidas_geradas.append(partida)

            self.__tela_campeonato.mostra_mensagem('\nPartidas geradas com sucesso!\n')
            self.__controlador_sistema.controlador_partidas.abre_tela()
        else:
            self.__tela_campeonato.mostra_mensagem('\nNão há equipes suficientes no campeonato para gerar partidas.\n')
            self.retorna()

    def adiciona_partida_campeonato(self, partida):
        if isinstance(partida, Partida):
            self.__campeonato.adiciona_partida(partida)

    def finaliza_campeonato(self):
        if not self.__campeonato:
            self.__tela_campeonato.mostra_mensagem('\nO campeonato ainda não foi iniciado!.\n')
            self.retorna()
        else:
            todas_partidas_realizadas = True
            for partida in self.__campeonato.partidas:
                if not partida.partida_realizada:
                    todas_partidas_realizadas = False

            if todas_partidas_realizadas:
                self.gera_relatorio()
                self.__tela_campeonato.mostra_mensagem('\nCampeonato finalizado com sucesso!\n')
                self.__controlador_sistema.encerra_sistema()
            else:
                self.__tela_campeonato.mostra_mensagem('\nAinda faltam partidas a serem realizadas!\n')
                self.retorna()

    def gera_relatorio(self):
        campeonato = self.__campeonato

        equipes = campeonato.equipes
        jogadores = {aluno for equipe in equipes for aluno in equipe.alunos}
        equipes_ordenadas = sorted(equipes, key=lambda e: (e.pontos, e.gols_marcados), reverse=True)

        ganhadores = equipes_ordenadas[:3]
        mais_gols_marcados = max(equipes, key=lambda e: e.gols_marcados)
        mais_gols_sofridos = max(equipes, key=lambda e: e.gols_sofridos)
        artilheiros = sorted(jogadores, key=lambda j: j.num_gols, reverse=True)[:3]

        relatorio = "\nRelatório do Campeonato:\n"
    
        if ganhadores:
            relatorio += f"\n1º Lugar: {ganhadores[0].nome} com {ganhadores[0].pontos} pontos e {ganhadores[0].gols_marcados} gols"
            relatorio += f"\n2º Lugar: {ganhadores[1].nome} com {ganhadores[1].pontos} pontos e {ganhadores[1].gols_marcados} gols"
            if len(ganhadores) > 2:
                relatorio += f"\n3º Lugar: {ganhadores[2].nome} com {ganhadores[2].pontos} pontos e {ganhadores[2].gols_marcados} gols"
        
        relatorio += f"\n\nEquipe com mais gols marcados: {mais_gols_marcados.nome} com {mais_gols_marcados.gols_marcados} gols"
        relatorio += f"\nEquipe que levou mais gols: {mais_gols_sofridos.nome} com {mais_gols_sofridos.gols_sofridos} gols"

        relatorio += "\n\nJogadores com mais gols marcados:"
        if artilheiros:
            relatorio += f"\n1. {artilheiros[0].nome} com {artilheiros[0].num_gols} gols"
            if len(artilheiros) > 1:
                relatorio += f"\n2. {artilheiros[1].nome} com {artilheiros[1].num_gols} gols"
            if len(artilheiros) > 2:
                relatorio += f"\n3. {artilheiros[2].nome} com {artilheiros[2].num_gols} gols"
        else:
            relatorio += "\nNenhum jogador marcou gols."

        self.__tela_campeonato.mostra_mensagem(relatorio)

    def retorna(self):
        self.__controlador_sistema.abre_tela()
