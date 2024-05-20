from partida import Partida
from tela_partida import TelaPartida


class ControladorPartidas:
    def __init__(self, controlador_sistema):
        self.__partidas = []
        self.__tela_partida = TelaPartida(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def tela_partida(self):
        return self.__tela_partida
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def lista_partidas(self):
        for partida in self.__partidas:
            self.__tela_partida.mostra_partida({'codigo': partida.codigo, 'data_partida': partida.data_partida, 'equipe_casa': partida.equipe_casa, 'equipe_visitante': partida.equipe_visitante, 'arbitro': partida.arbitro, 'gols_equipe_casa': partida.gols_equipe_casa, 'gols_equipe_visitante': partida.gols_equipe_visitante, 'resultado': partida.resultado, 'partida_realizada': partida.partida_realizada})
    
    def inclui_partida(self, dados_partida):
        partida =  partida(dados_partida['codigo'], dados_partida['data_partida'], dados_partida['equipe_casa'], dados_partida['equipe_visitante'], dados_partida['arbitro'])
        if not self.pega_partida_por_codigo(partida.codigo):
            self.__partidas.append(partida)
        
    def pega_partida_por_codigo(self, codigo:int):
        for partida in self.__partidas:
            if partida.codigo == codigo:
                return partida
        return "Não existe partida com esse código cadastrado"
    
    def adiciona_gols_partida(self):
        partida = self.__tela_partida.seleciona_partida()
        gols_partida = self.tela_partida.pega_gols_partida()
        gols_equipe_casa = gols_partida['gols_equipe_casa']
        gols_equipe_visitante = gols_partida['gols_equipe_visitante']

        if isinstance(gols_equipe_casa, int) and isinstance(gols_equipe_visitante, int):
            partida.gols_equipe_casa(gols_equipe_casa)
            partida.gols_equipe_visitante(gols_equipe_visitante)
            partida.partida_realizada(True)
            partida.resultado('Equipe Casa {gols_equipe_casa}X{gols_equipe_visitante} Equipe Visitante')
        
    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.lista_partidas,
                        '2': self.adiciona_gols_partida,
                        '0': self.retorna}
        while True:
            opcao_escolhida = self.__tela_partida.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_partida.mostra_mensagem('ERRO: Opção inválida!\n')

