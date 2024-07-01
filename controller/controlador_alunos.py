from model.aluno import Aluno
from view.tela_aluno import TelaAluno
from model.curso import Curso
from datetime import datetime
from DAOs.aluno_dao import AlunoDAO

from exceptions.opcao_invalida_exception import OpcaoInvalidaException
from exceptions.cadastro_duplicado_exception import CadastroDuplicadoException
from exceptions.tipo_invalido_exception import TipoInvalidoException
from exceptions.cadastro_nao_encontrado_exception import CadastroNaoEncontradoException
class ControladorAlunos:
    def __init__(self, controlador_sistema):
        self.__aluno_DAO = AlunoDAO()
        self.__tela_aluno = TelaAluno(self)
        self.__controlador_sistema = controlador_sistema
        
    @property
    def alunos(self):
        return self.__aluno_DAO.get_all()
    
    @property
    def tela_aluno(self):
        return self.__tela_aluno
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def lista_alunos(self):
        if len(self.__aluno_DAO.get_all()) == 0:
            self.__tela_aluno.mostra_mensagem('Nenhum aluno cadastrado!')
        else:
            self.__tela_aluno.mostra_alunos(self.__aluno_DAO.get_all())
    
    def inclui_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        try:
            if isinstance(dados_aluno['matricula'], int) and isinstance(dados_aluno['codigo_curso'], int) and isinstance(dados_aluno['nome'], str) and isinstance(dados_aluno['cpf'], str) and isinstance(dados_aluno['data_nasc'], datetime):
                curso = self.__controlador_sistema.controlador_cursos.pega_curso_por_codigo(dados_aluno['codigo_curso'])
                if curso:
                    if not self.pega_aluno_por_matricula(dados_aluno['matricula']):
                        aluno =  Aluno(dados_aluno['matricula'], curso, dados_aluno['nome'], dados_aluno['cpf'], dados_aluno['data_nasc'])
                        self.__aluno_DAO.add(aluno)
                        self.__tela_aluno.mostra_mensagem('Aluno cadastrado com sucesso!')
                    else:
                        raise CadastroDuplicadoException('Aluno(a)')
                else:
                    raise CadastroNaoEncontradoException('Curso')
            else:
                raise TipoInvalidoException()
        except (CadastroNaoEncontradoException, CadastroDuplicadoException, TipoInvalidoException) as e:
            self.__tela_aluno.mostra_mensagem(str(e))

        
    def altera_aluno(self):
        matricula =  self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)
        
        try:
            if aluno:
                novos_dados_aluno = self.__tela_aluno.pega_dados_aluno(editando=True)
                if isinstance(novos_dados_aluno['nome'], str):
                    aluno.nome = novos_dados_aluno['nome']
                if isinstance(novos_dados_aluno['data_nasc'], datetime):
                    aluno.data_nasc = novos_dados_aluno['data_nasc']
                self.__aluno_DAO.update(aluno)
                self.__tela_aluno.mostra_mensagem('Aluno editado com sucesso!')
            else:
                raise CadastroNaoEncontradoException('Aluno(a)')
        except CadastroNaoEncontradoException as e:
            self.__tela_aluno.mostra_mensagem(str(e))
    
    def exclui_aluno(self):
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)
        try:
            if aluno:
                self.__aluno_DAO.remove(matricula)
                self.__tela_aluno.mostra_mensagem('Aluno excluído com sucesso!')
            else:
                raise CadastroNaoEncontradoException('Aluno(a)')
        except CadastroNaoEncontradoException as e:
            self.__tela_aluno.mostra_mensagem(str(e))

    def pega_aluno_por_matricula(self, matricula:int):
        for aluno in self.__aluno_DAO.get_all():
            if aluno.matricula == matricula:
                return aluno
        return None

    def adiciona_gol(self, matricula:int):
        aluno = self.pega_aluno_por_matricula(matricula)
        if aluno:
            aluno.adiciona_gol()
            self.__aluno_DAO.update(aluno)
    
    def remove_gol(self, matricula:int):
        aluno = self.pega_aluno_por_matricula(matricula)
        if aluno:
            aluno.remove_gol()
            self.__aluno_DAO.update(aluno)

    def zera_gols(self, matricula:int):
        aluno = self.pega_aluno_por_matricula(matricula)
        if aluno:
            aluno.zera_gols()
            self.__aluno_DAO.update(aluno)
    
    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.inclui_aluno,
                        '2': self.altera_aluno,
                        '3': self.lista_alunos,
                        '4': self.exclui_aluno,
                        '0': self.retorna}
        
        while True:
            try:
                opcao_escolhida = self.__tela_aluno.tela_opcoes()
                if opcao_escolhida in lista_opcoes:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                else:
                    raise OpcaoInvalidaException()
            except OpcaoInvalidaException as e:
                self.__tela_aluno.mostra_mensagem(str(e))

