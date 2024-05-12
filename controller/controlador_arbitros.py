from model.arbitro import Arbitro
from view.tela_arbitro import TelaArbitro


class ControladorArbitro:
    def __init__(self, controlador_sistema):
        self.__arbitros = []
        self.__tela_arbitro = TelaArbitro()
        self.__controlador_sistema = controlador_sistema
        
    def pega_arbitro_por_cpf(self, cpf:int): ### cpf deveria ser str, não int
        for arbitro in self.__arbitros:
            if arbitro.cpf == cpf:
                return arbitro
        return None
    
    def incluir_arbitro(self):
        dados_arbitro = TelaArbitro.pega_dados_arbitro()
        arbitro = Arbitro(dados_arbitro['nome'], dados_arbitro['cpf'], dados_arbitro['data_nasc'])
        if not self.pega_arbitro_por_cpf(arbitro.cpf):
            self.__arbitros.append(arbitro)
        else:
            self.__tela_arbitro.mostra_mensagem('ATENÇÃO: Árbitro já cadastrado!')
    
    def alterar_arbitro(self):
        self.listar_arbitros()
        cpf_arbitro =  self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        
        if arbitro:
            novos_dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
            arbitro.nome = novos_dados_arbitro['nome']
            arbitro.cpf = novos_dados_arbitro['cpf']
            arbitro.data_nasc = novos_dados_arbitro['data_nasc']
            self.listar_arbitros()
        else:
            self.__tela_arbitro.mostra_mensagem('ATENÇÃO: Árbitro não encontrado!')
    
    def listar_arbitros(self):
        for arbitro in self.__arbitros:
            self.__tela_arbitro.mostra_arbitro({'nome': arbitro.nome, 'cpf': arbitro.cpf, 'data_nasc': arbitro.data_nasc})
    
    def excluir_arbitro(self):
        self.listar_arbitros()
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        
        if arbitro:
            self.__arbitros.remove(arbitro)
            self.listar_arbitros()
        else:
            self.__tela_arbitro.mostra_mensagem('ATENÇÃO: Árbitro não encontrado!')
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_arbitro,
                        2: self.alterar_arbitro,
                        3: self.listar_arbitros,
                        4: self.excluir_arbitro,
                        0: self.retornar}
        
        while True:
            lista_opcoes[self.__tela_arbitro.tela_opcoes()]()
        