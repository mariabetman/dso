from campeonato import Campeonato
from tela_campeonato import TelaCampeonato
from equipe import Equipe


class ControladorCampeonatos:
    def __init__(self, controlador_sistema):
        self.__campeonatos = []
        self.__tela_campeonato = TelaCampeonato(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def tela_campeonato(self):
        return self.__tela_campeonato
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def lista_campeonatos(self):
        if len(self.__campeonatos) == 0:
            self.__tela_campeonato.mostra_mensagem('Nenhum Campeonato cadastrado!')
        else:
            self.__tela_campeonato.mostra_mensagem('----- CAMPEONATOS CADASTRADOS -----')
            for campeonato in self.__campeonatos:
                self.__tela_campeonato.mostra_campeonato({'codigo': campeonato.codigo})
        
    def inclui_campeonato(self):
        dados_campeonato = self.tela_campeonato.pega_dados_campeonato()
        campeonato =  Campeonato(int(dados_campeonato['codigo']))

        if not self.pega_campeonato_por_codigo(campeonato.codigo):
            self.__campeonato.append(campeonato)
            self.__tela_campeonato.mostra_mensagem('\nCampeonato cadastrado com sucesso!\n')
        else:
            self.__tela_campeonato.mostra_mensagem('\nATENÇÃO: Campeonato já cadastrado!\n')
    
    def altera_campeonato(self):
        codigo_campeonato =  self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_codigo(codigo_campeonato)
        
        if campeonato:
            novos_dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
            if isinstance(novos_dados_campeonato['nome'], int):
                campeonato.nome = novos_dados_campeonato['nome']
            self.lista_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem('\nATENÇÃO: Campeonato não encontrado!\n')
    
    def exclui_campeonato(self):
        codigo_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_codigo(codigo_campeonato)
        
        if campeonato:
            self.__campeonatos.remove(campeonato)
            self.__tela_campeonato.mostra_mensagem('\nCampeonato excluído com sucesso!\n')
        else:
            self.__tela_campeonato.mostra_mensagem('\nATENÇÃO: Campeonato não encontrado!\n')
        
    def pega_campeonato_por_codigo(self, codigo:int):
        for campeonato in self.__campeonatos:
            if campeonato.codigo == codigo:
                return campeonato
        return None
    
    def adiciona_equipe_no_campeonato(self):
        codigo_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_codigo(codigo_campeonato)
        codigo_equipe = self.__controlador_sistema.controlador_equipes.tela_equipe.seleciona_equipe()
        equipe = self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(codigo_equipe)

        if isinstance(campeonato, Campeonato) and isinstance(equipe, Equipe):
            for equipe_cadastrada in self.__equipes:
                if equipe_cadastrada.codigo == equipe.codigo:
                    self.__tela_campeonato.mostra_mensagem('\nEquipe já adicionada nesse Campeonato!\n')
                    return
            campeonato.adiciona_equipe(equipe)
            self.__tela_campeonato.mostra_mensagem('\nEquipe adicionada com sucesso!\n')
    
    def remove_equipe_do_campeonato(self):
        codigo_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_codigo(codigo_campeonato)
        codigo_equipe = self.__controlador_sistema.controlador_equipes.tela_campeonato.seleciona_equipe()
        equipe = self.__controlador_sistema.controlador_equipes.pega_equipe_por_codigo(codigo_equipe)

        if isinstance(campeonato, Campeonato) and isinstance(equipe, Equipe):
            for equipe_cadastrada in self.__equipes:
                if equipe_cadastrada.codigo == equipe.codigo:
                    campeonato.remove_equipe(equipe)
                    self.__tela_campeonato.mostra_mensagem('\nEquipe removida com sucesso!\n')
    
    def adiciona_partida_no_campeonato(self):
        pass
    
    def remove_partida_do_campeonato(self):
        pass

    def adiciona_gols_artilharia_no_campeonato(self):
        pass
    
    def remove_gols_artilharia_do_campeonato(self):
        pass

    def inicia_campeonato(self):
        pass

    def finaliza_campeonato(self):
        pass

    def gera_relatorio(self):
        pass

    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.inclui_campeonato,
                        '2': self.altera_campeonato,
                        '3': self.lista_campeonatos,
                        '4': self.exclui_campeonato,
                        '5': self.adiciona_equipe_no_campeonato,
                        '6': self.remove_equipe_do_campeonato,
                        '7': self.inicia_campeonato,
                        '8': self.finaliza_campeonato,
                        '9': self.gera_relatorio,
                        '0': self.retorna}
        while True:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
