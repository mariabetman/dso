from model.arbitro import Arbitro
from view.tela_arbitro import TelaArbitro
from DAOs.arbitro_dao import ArbitroDAO
from datetime import datetime


class ControladorArbitros:
    def __init__(self, controlador_sistema):
        self.__arbitro_dao = ArbitroDAO()
        self.__tela_arbitro = TelaArbitro(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def arbitros(self):
        return self.__arbitro_dao.get_all()
    
    @property
    def tela_arbitro(self):
        return self.__tela_arbitro
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def lista_arbitros(self):
        if len(self.__arbitro_dao.get_all()) == 0:
            self.__tela_arbitro.mostra_mensagem('Nenhum árbitro cadastrado!')
        else:
            self.__tela_arbitro.mostra_mensagem('----- ÁRBITROS CADASTRADOS -----')
            for arbitro in self.__arbitro_dao.get_all():
                self.__tela_arbitro.mostra_arbitro({'nome': arbitro.nome, 'cpf': arbitro.cpf, 'data_nasc': arbitro.data_nasc})
    
    def inclui_arbitro(self):
        dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
        if isinstance(dados_arbitro['nome'], str) and isinstance(dados_arbitro['cpf'], str) and isinstance(dados_arbitro['data_nasc'], datetime):
            if not self.pega_arbitro_por_cpf(dados_arbitro['cpf']):
                arbitro = Arbitro(dados_arbitro['nome'], dados_arbitro['cpf'], dados_arbitro['data_nasc'])
                self.__arbitro_dao.add(arbitro)
                self.__tela_arbitro.mostra_mensagem('Árbitro cadastrado com sucesso!')
            else:
                self.__tela_arbitro.mostra_mensagem('ATENÇÃO: Árbitro já cadastrado!')
        else:
            self.__tela_arbitro.mostra_mensagem('ATENÇÃO: Algo de errado ocorreu durante o cadastro! Tente novamente!')
    
    def altera_arbitro(self):
        cpf_arbitro =  self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        
        if arbitro:
            novos_dados_arbitro = self.__tela_arbitro.pega_dados_arbitro(editando=True)
            if isinstance(novos_dados_arbitro['nome'], str):
                arbitro.nome = novos_dados_arbitro['nome']
            if isinstance(novos_dados_arbitro['data_nasc'], datetime):
                arbitro.cpf = novos_dados_arbitro['cpf']
            self.__tela_arbitro.mostra_mensagem('Árbitro editado com sucesso!')
        else:
            self.__tela_arbitro.mostra_mensagem('ATENÇÃO: Árbitro não encontrado!')
    
    def exclui_arbitro(self):
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        
        if arbitro:
            self.__arbitro_dao.remove(arbitro.cpf)
            self.__tela_arbitro.mostra_mensagem('Árbitro excluído com sucesso!')
        else:
            self.__tela_arbitro.mostra_mensagem('ATENÇÃO: Árbitro não encontrado!')
        
    def pega_arbitro_por_cpf(self, cpf:str):
        for arbitro in self.__arbitro_dao.get_all():
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
            opcao_escolhida = self.__tela_arbitro.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_arbitro.mostra_mensagem('ERRO: Opção inválida!\n')
