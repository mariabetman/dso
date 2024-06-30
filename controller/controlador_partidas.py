from datetime import datetime
from model.partida import Partida
from view.tela_partida import TelaPartida
from model.aluno import Aluno
from model.equipe import Equipe
from model.arbitro import Arbitro
from DAOs.partida_dao import PartidaDAO

from exceptions.opcao_invalida_exception import OpcaoInvalidaException
from exceptions.cadastro_duplicado_exception import CadastroDuplicadoException
from exceptions.tipo_invalido_exception import TipoInvalidoException
from exceptions.cadastro_nao_encontrado_exception import CadastroNaoEncontradoException
from exceptions.aluno_de_curso_diferente_da_equipe_exception import AlunoDeCursoDiferenteDaEquipeException
from exceptions.aluno_jah_cadastrado_na_equipe_exception import AlunoJahCadastradoNaEquipeException
from exceptions.erro_inesperado import ErroInesperadoException
from exceptions.partida_realizada_exception import PartidaRealizadaException
class ControladorPartidas:
    def __init__(self, controlador_sistema):
        self.__partida_DAO = PartidaDAO()
        self.__tela_partida = TelaPartida(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def tela_partida(self):
        return self.__tela_partida
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def lista_partidas(self):
        if len(self.__partida_DAO.get_all()) == 0:
            self.__tela_partida.mostra_mensagem('Nenhuma Partida cadastrada!')
        else:
            self.__tela_partida.mostra_mensagem('----- PARTIDAS CADASTRADOS -----')
            for partida in self.__partida_DAO.get_all():
                self.__tela_partida.mostra_partida({'codigo': partida.codigo, 'data_partida': partida.data_partida, 'equipe_casa': partida.equipe_casa.nome, 'equipe_visitante': partida.equipe_visitante.nome, 'arbitro': partida.arbitro.nome, 'gols_equipe_casa': partida.gols_equipe_casa, 'gols_equipe_visitante': partida.gols_equipe_visitante, 'resultado': partida.resultado, 'partida_realizada': partida.partida_realizada})
    
    def inclui_partida(self, dados_partida):
        try:
            if isinstance(dados_partida['codigo'], int) and isinstance(dados_partida['data_partida'], datetime) and isinstance(dados_partida['equipe_casa'], Equipe) and isinstance(dados_partida['equipe_visitante'], Equipe) and isinstance(dados_partida['arbitro'], Arbitro):
                partida =  Partida(dados_partida['codigo'], dados_partida['data_partida'], dados_partida['equipe_casa'], dados_partida['equipe_visitante'], dados_partida['arbitro'])
                if not self.pega_partida_por_codigo(partida.codigo):
                    self.__partida_DAO.add(partida)
                    return partida
            else:
                raise TipoInvalidoException()
        except TipoInvalidoException as e:
            self.__tela_partida.mostra_mensagem(str(e))
            
    def pega_partida_por_codigo(self, codigo:int):
        for partida in self.__partida_DAO.get_all():
            if partida.codigo == codigo:
                return partida
        return None
    
    def adiciona_gols_partida(self):
        codigo_partida = self.__tela_partida.seleciona_partida()
        partida = self.pega_partida_por_codigo(codigo_partida)

        try:
            if not partida:
                raise CadastroNaoEncontradoException('Partida')
        except CadastroNaoEncontradoException as e:
                self.__tela_partida.mostra_mensagem(str(e))
                return

        try:
            if partida.partida_realizada:
                raise PartidaRealizadaException()
        except PartidaRealizadaException as e:
                self.__tela_partida.mostra_mensagem(str(e))
                return

        alunos_equipe_casa = partida.equipe_casa.alunos
        alunos_equipe_visitante = partida.equipe_visitante.alunos
        
        gols_partida = self.__tela_partida.pega_gols_partida(partida)
        
        gols_equipe_casa = gols_partida['gols_equipe_casa']
        artilheiros_equipe_casa = [self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula) for matricula in gols_partida['artilheiros_equipe_casa']]
        gols_equipe_visitante = gols_partida['gols_equipe_visitante']
        artilheiros_equipe_visitante = [self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula) for matricula in gols_partida['artilheiros_equipe_visitante']]

        try:
            if all(isinstance(artilheiro, Aluno) for artilheiro in artilheiros_equipe_casa) and all(isinstance(artilheiro, Aluno) for artilheiro in artilheiros_equipe_visitante):
                partida.gols_equipe_casa = gols_equipe_casa
                partida.artilheiros_equipe_casa = artilheiros_equipe_casa
                partida.gols_equipe_visitante = gols_equipe_visitante
                partida.artilheiros_equipe_visitante = artilheiros_equipe_visitante
                partida.partida_realizada = True
                partida.resultado = f'Equipe Casa {partida.gols_equipe_casa}X{partida.gols_equipe_visitante} Equipe Visitante'
                self.gera_dados_partida(partida)
                self.__partida_DAO.update(partida)
                self.__tela_partida.mostra_mensagem('Gols cadastrados com sucesso!')
            else:
                raise ErroInesperadoException('adicionar gols da partida.')
        except ErroInesperadoException as e:
            self.__tela_partida.mostra_mensagem(str(e))

    def gera_dados_partida(self, partida:Partida):
        if partida.gols_equipe_casa > partida.gols_equipe_visitante:
            equipe_vencedora = partida.equipe_casa
        elif partida.gols_equipe_visitante > partida.gols_equipe_casa:
            equipe_vencedora = partida.equipe_visitante
        else:
            equipe_vencedora = None
        
        if equipe_vencedora:
            self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(equipe_vencedora.codigo).adiciona_pontos(3)
        else:
            self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(partida.equipe_casa.codigo).adiciona_pontos(1)
            self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(partida.equipe_visitante.codigo).adiciona_pontos(1)
        
        self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(partida.equipe_casa.codigo).adiciona_gols_marcados(partida.gols_equipe_casa)
        self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(partida.equipe_casa.codigo).adiciona_gols_sofridos(partida.gols_equipe_visitante)
        self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(partida.equipe_visitante.codigo).adiciona_gols_marcados(partida.gols_equipe_visitante)
        self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(partida.equipe_visitante.codigo).adiciona_gols_sofridos(partida.gols_equipe_casa)

        for aluno in partida.artilheiros_equipe_casa:
            self.controlador_sistema.controlador_alunos.adiciona_gol(aluno.matricula)

        for aluno in partida.artilheiros_equipe_visitante:
            self.controlador_sistema.controlador_alunos.adiciona_gol(aluno.matricula)

    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.lista_partidas,
                        '2': self.adiciona_gols_partida,
                        '0': self.retorna}
        while True:
            try:
                opcao_escolhida = self.__tela_partida.tela_opcoes()
                if opcao_escolhida in lista_opcoes:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                else:
                    raise OpcaoInvalidaException()
            except OpcaoInvalidaException as e:
                self.__tela_partida.mostra_mensagem(str(e))
