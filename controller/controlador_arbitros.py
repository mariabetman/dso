from model.arbitro import Arbitro
from view.tela_arbitro import TelaArbitro
from DAOs.arbitro_dao import ArbitroDAO
from datetime import datetime

from exceptions.opcao_invalida_exception import OpcaoInvalidaException
from exceptions.cadastro_duplicado_exception import CadastroDuplicadoException
from exceptions.tipo_invalido_exception import TipoInvalidoException
from exceptions.cadastro_nao_encontrado_exception import CadastroNaoEncontradoException
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
            self.__tela_arbitro.mostra_arbitros(self.__arbitro_dao.get_all())
    
    def inclui_arbitro(self):
        dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
        try:
            if isinstance(dados_arbitro['nome'], str) and isinstance(dados_arbitro['cpf'], str) and isinstance(dados_arbitro['data_nasc'], datetime):
                try:
                    if not self.pega_arbitro_por_cpf(dados_arbitro['cpf']):
                        arbitro = Arbitro(dados_arbitro['nome'], dados_arbitro['cpf'], dados_arbitro['data_nasc'])
                    else:
                        raise CadastroDuplicadoException('CPF')
                except CadastroDuplicadoException as e:
                    self.__tela_arbitro.mostra_mensagem(str(e))
                else:
                    self.__arbitro_dao.add(arbitro)
                    self.__tela_arbitro.mostra_mensagem('Árbitro cadastrado com sucesso!')
        except TipoInvalidoException as e:
            self.__tela_arbitro.mostra_mensagem(str(e))
            
    
    def altera_arbitro(self):
        cpf_arbitro =  self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro) 
        try:
            if arbitro:
                novos_dados_arbitro = self.__tela_arbitro.pega_dados_arbitro(editando=True)
                if isinstance(novos_dados_arbitro['nome'], str):
                    arbitro.nome = novos_dados_arbitro['nome']
                if isinstance(novos_dados_arbitro['data_nasc'], datetime):
                    arbitro.cpf = novos_dados_arbitro['cpf']
                self.__tela_arbitro.mostra_mensagem('Árbitro editado com sucesso!')
            else:
                raise CadastroNaoEncontradoException('Arbitro')
        except CadastroNaoEncontradoException as e:
                    self.__tela_arbitro.mostra_mensagem(str(e)) 
    
    def exclui_arbitro(self):
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)
        try:
            if arbitro:
                self.__arbitro_dao.remove(arbitro.cpf)
                self.__tela_arbitro.mostra_mensagem('Árbitro excluído com sucesso!')
            else:
                raise CadastroNaoEncontradoException('Arbitro')
        except CadastroNaoEncontradoException as e:
                    self.__tela_arbitro.mostra_mensagem(str(e)) 
        
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
            try:
                opcao_escolhida = self.__tela_arbitro.tela_opcoes()
                if opcao_escolhida in lista_opcoes:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                else:
                    raise OpcaoInvalidaException()
            except OpcaoInvalidaException as e:
                self.__tela_arbitro.mostra_mensagem(str(e))