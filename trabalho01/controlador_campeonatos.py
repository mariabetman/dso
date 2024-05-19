from tela_campeonato import TelaCampeonato
from campeonato import Campeonato


class ControladorCampeonatos:
    def __init__(self, controlador_sistema):
        self.__campeonatos = []
        self.__tela_campeonato = TelaCampeonato(self)
        self.__controlador_sistema = controlador_sistema
    
    def lista_campeonatos(self):
        for campeonato in self.__campeonatos:
            self.__tela_campeonato.mostra_campeonato({'codigo': campeonato.codigo, 'equipes': campeonato.equipes, 'partidas': campeonato.partidas, 'artilharia': campeonato.artilharia})
    ##Verificar
        
    def adiciona_campeonato(self):
        dados_campeonato = self.tela_campeonato.pega_dados_campeonato()
        campeonato =  Campeonato(int(dados_campeonato['codigo']))
        if not self.pega_campeonato_por_codigo(campeonato.codigo):
            self.__campeonato.append(campeonato)
        else:
            self.__tela_campeonato.mostra_mensagem('ATENÇÃO: Campeonato já cadastrado!')
    
    def remove_campeonato(self):
        self.listar_campeonatos()
        codigo_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_codigo(codigo_campeonato)
        
        if campeonato:
            self.__campeonatos.remove(campeonato)
            self.listar_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem('ATENÇÃO: Campeonato não encontrado!')
        
    def pega_campeonato_por_codigo(self, codigo:int):
        for campeonato in self.__campeonatos:
            if campeonato.codigo == codigo:
                return campeonato
        return "Não existe campeonato com esse código cadastrado"
    
    def altera_campeonato(self):
        self.lista.campeonatos()
        codigo_campeonato =  self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_codigo(codigo_campeonato)
        
        if campeonato:
            novos_dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
            if isinstance(novos_dados_campeonato['codigo'], int):
                campeonato.codigo = novos_dados_campeonato['codigo']
            self.lista_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem('ATENÇÃO: Campeonato não encontrado!')
    
    def adiciona_equipe_no_campeonato(self):
        campeonato = self.__tela_campeonato.seleciona_campeonato()
        equipe_nova = self.__controlador_sistema.tela_equipe.seleciona_equipe()
        if equipe_nova:
            campeonato.adiciona_equipe(equipe_nova)
    
    def remove_equipe_do_campeonato(self):
        campeonato = self.__tela_campeonato.seleciona_campeonato()
        equipe_a_ser_removida = self.__controlador_sistema.tela_equipe.seleciona_equipe()
        if equipe_a_ser_removida:
            campeonato.remove_equipe(equipe_a_ser_removida)
    
    def adiciona_partida_no_campeonato(self):
        campeonato = self.__tela_campeonato.seleciona_campeonato()
        partida_nova = self.__controlador_sistema.tela_equipe.seleciona_equipe()
        if equipe_nova:
            campeonato.adiciona_equipe(equipe_nova)
    
    def remove_partida_do_campeonato(self):
        partida_a_ser_removida = self.__controlador_sistema.tela_partida.seleciona_partida()
        if partida_a_ser_removida:
            self.__partidas.remove(partida_a_ser_removida)
    
    def adiciona_equipe_no_campeonato(self):
        equipe_nova = self.__controlador_sistema.tela_equipe.seleciona_equipe()
        if equipe_nova:
            self.__equipes.append(equipe_nova)
    
    def remove_equipe_no_campeonato(self):
        equipe_a_ser_removida = self.__controlador_sistema.tela_equipe.seleciona_equipe()
        if equipe_a_ser_removida:
            self.__equipes.remove(equipe_a_ser_removida)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_aluno,
                        2: self.alterar_aluno,
                        3: self.listar_alunos,
                        4: self.excluir_aluno,
                        0: self.retornar}
        
        while True:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
