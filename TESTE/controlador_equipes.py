from equipe import Equipe
from tela_equipe import TelaEquipe
from controlador_alunos import ControladorAluno


class ControladorEquipe:
    def __init__(self, controlador_sistema):
        self.__equipes = []
        self.__tela_equipe = TelaEquipe()
        self.__controlador_sistema = controlador_sistema
        
    def pega_equipe_por_codigo(self, codigo: int):
        for equipe in self.__equipes:
            if equipe.codigo == codigo:
                return equipe
        return None
    
    def add_equipe(self):
        dados_equipe = TelaEquipe.pega_dados_equipe()
        equipe = Equipe(dados_equipe['curso'], dados_equipe['nome'], dados_equipe['codigo'])
        if not self.pega_equipe_por_codigo(equipe.codigo):
            self.__equipes.append(equipe)
        else:
            self.__tela_equipe.mostra_mensagem('ATENÇÃO: Equipe já cadastrada!')

    def altera_equipe(self):
        self.listar_arbitros()
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        
        if equipe:
            novos_dados_equipe = self.__tela_equipe.pega_dados_equipe()
            equipe.nome = novos_dados_equipe['nome']
            equipe.curso = novos_dados_equipe['curso']
            self.listar_arbitros()
        else:
            self.__tela_equipe.mostra_mensagem('ATENÇÃO: Equipe não encontrada!')
    
    def lista_equipes(self):
        for equipe in self.__equipes:
            self.__tela_equipe.mostra_equipe({'codigo': equipe.codigo, 'nome': equipe.nome, 'curso': equipe.curso})
    
    def exclui_equipe(self):
        self.lista_equipes()
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        
        if equipe:
            self.__equipes.remove(equipe)
            self.lista_equipes
        else:
            self.__tela_equipe.mostra_mensagem('ATENÇÃO: Equipe não encontrada!')
            
    def add_aluno_na_equipe(self):
        self.__controlador_sistema.controlador_aluno
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.add_equipe,
                        2: self.altera_equipe,
                        3: self.lista_equipes,
                        4: self.exclui_equipe,
                        0: self.retornar}
        
        while True:
            lista_opcoes[self.__tela_equipe.tela_opcoes()]()