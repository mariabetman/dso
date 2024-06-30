from model.equipe import Equipe
from view.tela_equipe import TelaEquipe
from model.curso import Curso
from model.aluno import Aluno
from DAOs.equipe_dao import EquipeDAO

from exceptions.opcao_invalida_exception import OpcaoInvalidaException
class ControladorEquipes:
    def __init__(self, controlador_sistema):
        self.__equipe_DAO = EquipeDAO()
        self.__tela_equipe = TelaEquipe(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def equipes(self):
        return self.__equipe_DAO.get_all()
    
    @property
    def tela_equipe(self):
        return self.__tela_equipe
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def lista_equipes(self):
        if len(self.__equipe_DAO.get_all()) == 0:
            self.__tela_equipe.mostra_mensagem('Nenhuma Equipe cadastrada!')
        else:
            self.mostra_alunos_equipe(self.__equipe_DAO.get_all())

    def inclui_equipe(self):
        dados_equipe = self.__tela_equipe.pega_dados_equipe()
        if isinstance(dados_equipe['codigo_curso'], int) and isinstance(dados_equipe['nome'], str) and isinstance(dados_equipe['codigo'], int):
            curso = self.__controlador_sistema.controlador_cursos.pega_curso_por_codigo(dados_equipe['codigo_curso'])
            if curso:
                if not self.pega_equipe_por_codigo(dados_equipe['codigo']):
                    equipe = Equipe(dados_equipe['curso'], dados_equipe['nome'], dados_equipe['codigo'])
                    self.__equipe_DAO.add(equipe)
                    self.__tela_equipe.mostra_mensagem('Equipe cadastrada com sucesso!')
                else:
                    self.__tela_equipe.mostra_mensagem('ATENÇÃO: Equipe já cadastrada!')
            else:
                self.__tela_equipe.mostra_mensagem('ATENÇÃO: Código do curso inválido!')
        else:
            self.__tela_equipe.mostra_mensagem('ATENÇÃO: Algo de errado ocorreu durante o cadastro! Tente novamente!')
    
    def altera_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        
        if equipe:
            novos_dados_equipe = self.__tela_equipe.pega_dados_equipe(editando=True)
            if isinstance(novos_dados_equipe['nome'], str):
                equipe.nome = novos_dados_equipe['nome']
            self.__equipe_DAO.update()
            self.lista_equipes()
        else:
            self.__tela_equipe.mostra_mensagem('ATENÇÃO: Equipe não encontrada!')
    
    def exclui_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        
        if equipe:
            self.__equipe_DAO.remove(equipe)
            self.__tela_equipe.mostra_mensagem('Equipe excluída com sucesso!')
        else:
            self.__tela_equipe.mostra_mensagem('ATENÇÃO: Equipe não encontrada!')
        
    def pega_equipe_por_codigo(self, codigo:int):
        for equipe in self.__equipe_DAO.get_all():
            if equipe.codigo == codigo:
                return equipe
        return None
    
    def mostra_alunos_equipe(self, codigo_equipe=None):
        if not codigo_equipe:
            codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        self.controlador_sistema.controlador_alunos.tela_aluno.mostra_alunos(equipe.alunos)

    def adiciona_aluno_na_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        self.__controlador_sistema.controlador_alunos.lista_alunos()
        matricula_aluno = self.__controlador_sistema.controlador_alunos.tela_aluno.seleciona_aluno()
        aluno = self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)

        if aluno.curso.codigo != equipe.curso.codigo:
            self.__tela_equipe.mostra_mensagem('ATENÇÃO: O Aluno deve ser do mesmo curso que a Equipe!')
            return None
        for _aluno in equipe.alunos:
            if _aluno.matricula == matricula_aluno:
                self.__tela_equipe.mostra_mensagem('ATENÇÃO: O Aluno já está cadastrado na equipe!')
                return None
        for equipe_existente in self.__equipe_DAO.get_all():
            for _aluno in equipe_existente.alunos:
                if _aluno.matricula == matricula_aluno:
                    self.__tela_equipe.mostra_mensagem('ATENÇÃO: O Aluno já está cadastrado em outra equipe!')
                    return None
        if isinstance(equipe, Equipe) and isinstance(aluno, Aluno):
            equipe.adiciona_aluno(aluno)
            self.__tela_equipe.mostra_mensagem('Aluno adicionado com sucesso!')
            self.__equipe_DAO.update(equipe)
        else:
            self.__tela_equipe.mostra_mensagem('ERRO: Um erro aconteceu ao tentar cadastrar o aluno na equipe!')
            

    def remove_aluno_da_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        self.mostra_alunos_equipe(codigo_equipe)
        matricula_aluno = self.__controlador_sistema.controlador_alunos.tela_aluno.seleciona_aluno()
        aluno = self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)

        if isinstance(equipe, Equipe) and isinstance(aluno, Aluno):
            for _aluno in equipe.alunos:
                if _aluno.matricula == matricula_aluno:
                    equipe.remove_aluno(aluno)
                    self.__tela_equipe.mostra_mensagem('Aluno removido com sucesso!')
                    self.__equipe_DAO.update(equipe)
                    return Aluno
            self.tela_equipe.mostra_mensagem('ERRO: Aluno não encontrado!')
            return None
    
    def adiciona_pontos_na_equipe(self, equipe:Equipe, pontos:int):
        if isinstance(equipe, Equipe) and isinstance(pontos, int):
            equipe.adiciona_pontos(pontos)
            self.__equipe_DAO.update(equipe)

    def remove_pontos_da_equipe(self, equipe:Equipe, pontos:int):
        if isinstance(equipe, Equipe) and isinstance(pontos, int):
            equipe.remove_pontos(pontos)
            self.__equipe_DAO.update(equipe)
    
    def adiciona_gols_marcados_na_equipe(self, equipe:Equipe, gols:int):
        if isinstance(equipe, Equipe) and isinstance(gols, int):
            equipe.adiciona_gols_marcados(gols)
            self.__equipe_DAO.update(equipe)

    def remove_gols_marcados_da_equipe(self, equipe:Equipe, gols:int):
        if isinstance(equipe, Equipe) and isinstance(gols, int):
            equipe.remove_gols_marcados(gols)
            self.__equipe_DAO.update(equipe)
    
    def adiciona_gols_sofridos_na_equipe(self, equipe:Equipe, gols:int):
        if isinstance(equipe, Equipe) and isinstance(gols, int):
            equipe.adiciona_gols_sofridos(gols)
            self.__equipe_DAO.update(equipe)

    def remove_gols_sofridos_da_equipe(self, equipe:Equipe, gols:int):
        if isinstance(equipe, Equipe) and isinstance(gols, int):
            equipe.remove_gols_sofridos(gols)
            self.__equipe_DAO.update(equipe)
            
    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.inclui_equipe,
                        '2': self.altera_equipe,
                        '3': self.lista_equipes,
                        '4': self.exclui_equipe,
                        '5': self.adiciona_aluno_na_equipe,
                        '6': self.remove_aluno_da_equipe,
                        '7': self.mostra_alunos_equipe,
                        '0': self.retorna}
        
        while True:
            try:
                opcao_escolhida = self.__tela_equipe.tela_opcoes()
                if opcao_escolhida in lista_opcoes:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                else:
                    raise OpcaoInvalidaException()
            except OpcaoInvalidaException as e:
                self.__tela_equipe.mostra_mensagem(str(e))