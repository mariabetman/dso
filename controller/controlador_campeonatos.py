from datetime import datetime, timedelta
from random import randint, choice
from model.campeonato import Campeonato
from view.tela_campeonato import TelaCampeonato
from model.partida import Partida


from exceptions.erro_inesperado import ErroInesperadoException
from exceptions.campeonato_jah_iniciado_exception import CampeonatoJahIniciadoException
from exceptions.alunos_insuficientes_na_equipe_exception import AlunosInsuficientesNaEquipeException
from exceptions.curso_sem_equipe_exception import CursoSemEquipeException
from exceptions.nenhum_arbitro_cadastrado_exception import NenhumArbitroCadastradoException
from exceptions.equipes_insuficientes_exception import EquipesInsuficientesNaEquipeException
from exceptions.campeonato_nao_iniciado_exception import CampeonatoNaoIniciadoException
from exceptions.partidas_nao_realizadas_exception import PartidasNaoRealizadasException
class ControladorCampeonatos:
    def __init__(self, controlador_sistema):
        self.__campeonato = None
        self.__tela_campeonato = TelaCampeonato(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
        
    def inclui_campeonato(self, codigo:int , equipes):
        quantidade_necessaria_alunos = 11
        try:
            if self.__campeonato:
                raise CampeonatoJahIniciadoException()
            else:
                cursos_com_equipes = {curso.codigo: False for curso in self.__controlador_sistema.controlador_cursos.cursos}
            
                for equipe in equipes:
                    if len(equipe.alunos) < quantidade_necessaria_alunos:
                        raise AlunosInsuficientesNaEquipeException(quantidade_necessaria_alunos)

                    if equipe.curso.codigo in cursos_com_equipes:
                        cursos_com_equipes[equipe.curso.codigo] = True
                
                for curso_codigo, tem_equipe in cursos_com_equipes.items():
                    if not tem_equipe:
                        raise CursoSemEquipeException(curso_codigo)

                if len(self.controlador_sistema.controlador_arbitros.arbitros) == 0:
                    raise NenhumArbitroCadastradoException()
                
                campeonato = Campeonato(codigo, equipes)
                self.__campeonato = campeonato
                self.__tela_campeonato.mostra_mensagem('\nCampeonato cadastrado com sucesso!\n')
                self.cria_partidas_do_campeonato()
        except (CampeonatoJahIniciadoException, AlunosInsuficientesNaEquipeException, CursoSemEquipeException, NenhumArbitroCadastradoException) as e:
            self.__tela_campeonato.mostra_mensagem(str(e))
            return self.retorna()
        
    def cria_partidas_do_campeonato(self):
        try:
            if self.__campeonato and len(self.__campeonato.equipes) > 1:
                equipes = list(self.__controlador_sistema.controlador_equipes.equipes)
            else:
                raise EquipesInsuficientesNaEquipeException()
        except EquipesInsuficientesNaEquipeException as e:
                self.__tela_campeonato.mostra_mensagem(str(e))
                return self.retorna()
        else:
            num_equipes = len(equipes)
            partidas_geradas = []

            for i in range(num_equipes):
                for j in range(i + 1, num_equipes):
                    data_aleatoria = datetime.now() + timedelta(days=randint(1, 30))
                    arbitros_lista = list(self.__controlador_sistema.controlador_arbitros.arbitros)
                    arbitro_aleatorio = choice(arbitros_lista)
                    dados_partida =  {'codigo': len(partidas_geradas) + 1, 'data_partida': data_aleatoria, 'equipe_casa': equipes[i], 'equipe_visitante': equipes[j], 'arbitro': arbitro_aleatorio}
                    partida = self.__controlador_sistema.controlador_partidas.inclui_partida(dados_partida)
                    self.adiciona_partida_campeonato(partida)
                    partidas_geradas.append(partida)

            self.__tela_campeonato.mostra_mensagem('\nPartidas geradas com sucesso!\n')
            self.__controlador_sistema.controlador_partidas.abre_tela()

    def adiciona_partida_campeonato(self, partida):
        try:
            if isinstance(partida, Partida):
                self.__campeonato.adiciona_partida(partida)
            else:
                raise ErroInesperadoException('adicionar partida no campeonato.')
        except ErroInesperadoException as e:
            self.__tela_campeonato.mostra_mensagem(str(e))

    def finaliza_campeonato(self):
        try:
            if not self.__campeonato:
                raise CampeonatoNaoIniciadoException()
            else:
                todas_partidas_realizadas = True
                for partida in self.__campeonato.partidas:
                    if not partida.partida_realizada:
                        todas_partidas_realizadas = False

                if todas_partidas_realizadas:
                    self.gera_relatorio()
                    partidas = list(self.__controlador_sistema.controlador_partidas.partidas)
                    for partida in partidas:
                        self.__controlador_sistema.controlador_partidas.exclui_partida(partida.codigo)
                    for equipe in self.__controlador_sistema.controlador_equipes.equipes:
                        self.__controlador_sistema.controlador_equipes.zera_pontos_na_equipe(equipe)
                        self.__controlador_sistema.controlador_equipes.zera_gols_marcados_na_equipe(equipe)
                        self.__controlador_sistema.controlador_equipes.zera_gols_sofridos_na_equipe(equipe)
                    for aluno in self.__controlador_sistema.controlador_alunos.alunos:
                        self.__controlador_sistema.controlador_alunos.zera_gols(aluno.matricula)
                    self.__tela_campeonato.mostra_mensagem('\nCampeonato finalizado com sucesso!\n')
                    self.__controlador_sistema.encerra_sistema()
                else:
                    raise PartidasNaoRealizadasException()
                    
        except (CampeonatoNaoIniciadoException, PartidasNaoRealizadasException) as e:
            self.__tela_campeonato.mostra_mensagem(str(e))
            return self.retorna()

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
