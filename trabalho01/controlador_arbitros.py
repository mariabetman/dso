from arbitro import Arbitro
from tela_arbitro import TelaArbitro
from datetime import datetime


class ControladorArbitros:
    def __init__(self, controlador_sistema):
        self.__arbitros = []
        self.__tela_arbitro = TelaArbitro(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def tela_arbitro(self):
        return self.__tela_arbitro
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def lista_arbitros(self):
        if len(self.__arbitros) == 0:
            self.__tela_arbitro.mostra_mensagem('Nenhum árbitro cadastrado!')
        else:
            self.__tela_arbitro.mostra_mensagem('----- ÁRBITROS CADASTRADOS -----')
            for arbitro in self.__arbitros:
                self.__tela_arbitro.mostra_arbitro({'nome': arbitro.nome, 'cpf': arbitro.cpf, 'data_nasc': arbitro.data_nasc})
    
    def inclui_arbitro(self):
        dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
        arbitro = Arbitro(dados_arbitro['nome'], dados_arbitro['cpf'], dados_arbitro['data_nasc'])
        if not self.pega_arbitro_por_cpf(arbitro.cpf):
            self.__arbitros.append(arbitro)
            self.__tela_arbitro.mostra_mensagem('\nÁrbitro cadastrado com sucesso!\n')
        else:
            self.__tela_arbitro.mostra_mensagem('\nATENÇÃO: Árbitro já cadastrado!\n')
    
    def altera_arbitro(self):
        cpf_arbitro =  self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        
        if arbitro:
            novos_dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
            if isinstance(novos_dados_arbitro['nome'], str):
                arbitro.nome = novos_dados_arbitro['nome']
            if isinstance(novos_dados_arbitro['cpf'], str):
                arbitro.cpf = novos_dados_arbitro['cpf']
            if isinstance(novos_dados_arbitro['data_nasc'], datetime):
                arbitro.cpf = novos_dados_arbitro['cpf']
            self.lista_arbitros()
        else:
            self.__tela_arbitro.mostra_mensagem('\nATENÇÃO: Árbitro não encontrado!\n')
    
    def exclui_arbitro(self):
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        
        if arbitro:
            self.__arbitros.remove(arbitro)
            self.__tela_arbitro.mostra_mensagem('\nÁrbitro excluído com sucesso!\n')
        else:
            self.__tela_arbitro.mostra_mensagem('\nATENÇÃO: Árbitro não encontrado!\n')
        
    def pega_arbitro_por_cpf(self, cpf:str):
        for arbitro in self.__arbitros:
            if arbitro.cpf == cpf:
                return arbitro
        return None
    
    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.inclui_arbitro,
                        '2': self.altera_arbitro,
                        '3': self.lista_arbitros,
                        '4': self.exclui_arbitro,
                        '0': self.retorna}
        
        while True:
            lista_opcoes[self.__tela_arbitro.tela_opcoes()]()