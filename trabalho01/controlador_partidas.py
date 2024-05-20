from partida import Partida
from tela_partida import TelaPartida


class ControladorPartidas:
    def __init__(self, controlador_sistema):
        self.__partidas = []
        self.__tela_partida = TelaPartida(self)
        self.__controlador_sistema = controlador_sistema
        
    def pega_partida_por_codigo(self, codigo:int):
        for partida in self.__partidas:
            if partida.codigo == codigo:
                return partida
        return "Não existe partida com esse código cadastrado"
    
    def listar_partidas(self):
        for partida in self.__partidas:
            self.__tela_curso.mostra_partida({'codigo': curso.codigo, 'data_partida': curso.data_partida, 'equipe_casa': curso.equipe_casa, 'equipe_visitante': curso.equipe_visitante, 'arbitro': curso.arbitro, 'gols_equipe_casa': curso.gols_equipe_casa, 'gols_equipe_visitante': curso.gols_equipe_visitante, 'resultado': curso.resultado, 'partida_realizada': curso.partida_realizada})
    
    def incluir_partida(self):
        dados_partida = self.tela_curso.pega_dados_partida()
        partida =  partida(dados_partida['codigo'], dados_partida['data_partida'], dados_partida['equipe_casa'], dados_partida['equipe_visitante'], dados_partida['arbitro'], dados_partida['gols_equipe_casa'], dados_partida['gols_equipe_visitante'], dados_partida['resultado'], dados_partida['partida_realizada'])
        if not self.pega_partida_por_codigo(partida.codigo):
            self.__partidas.append(partida)
        else:
            self.__tela_partida.mostra_mensagem('ATENÇÃO: Partida já cadastrado!')
    
    def alterar_partida(self):
        self.listar_partidas()
        codigo_partida =  self.__tela_partida.seleciona_partida()
        partida = self.pega_partida_por_codigo(codigo_partida)
        
        if partida:
            novos_dados_partida = self.__tela_partida.pega_dados_partida()
            if isinstance(novos_dados_partida['codigo'], int):
                partida.codigo = novos_dados_partida['codigo']
            if isinstance(novos_dados_partida['data_partida'], str):
                partida.data_partida = novos_dados_partida['data_partida']
            if isinstance(novos_dados_partida['equipe_casa'], str):
                partida.equipe_casa = novos_dados_partida['equipe_casa']
            if isinstance(novos_dados_partida['equipe_visitante'], str):
                partida.equipe_visitante = novos_dados_partida['equipe_visitante']
            if isinstance(novos_dados_partida['arbitro'], str):
                partida.arbitro = novos_dados_partida['arbitro']
            if isinstance(novos_dados_partida['gols_equipe_casa'], str):
                partida.gols_equipe_casa = novos_dados_partida['gols_equipe_casa']
            if isinstance(novos_dados_partida['gols_equipe_visitante'], str):
                partida.gols_equipe_visitante = novos_dados_partida['gols_equipe_visitante']
            if isinstance(novos_dados_partida['resultado'], str):
                partida.resultado = novos_dados_partida['resultado']
            if isinstance(novos_dados_partida['partida_realizada'], str):
                partida.partida_realizada = novos_dados_partida['partida_realizada']
            self.listar_partidas()
        else:
            self.__tela_partida.mostra_mensagem('ATENÇÃO: Partida não encontrado!')
    
    def excluir_partida(self):
        self.listar_partidas()
        codigo_partida = self.__tela_partida.seleciona_partida()
        partida = self.pega_partida_por_codigo(codigo_partida)
        
        if partida:
            self.__partidas.remove(partida)
            self.listar_partidas()
        else:
            self.__tela_partida.mostra_mensagem('ATENÇÃO: p=Partida não encontrado!')
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.incluir_partida,
                        '2': self.alterar_partida,
                        '3': self.listar_partidas,
                        '4': self.excluir_partida,
                        '0': self.retornar}
        
        while True:
            lista_opcoes[self.__tela_partida.tela_opcoes()]()
