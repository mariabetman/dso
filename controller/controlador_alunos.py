from model.aluno import Aluno
from view.tela_aluno import TelaAluno
from model.curso import Curso
from datetime import datetime
from DAOs.aluno_dao import AlunoDAO


class ControladorAlunos:
    def __init__(self, controlador_sistema):
        self.__aluno_DAO = AlunoDAO()
        self.__tela_aluno = TelaAluno(self)
        self.__controlador_sistema = controlador_sistema
        
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
            self.__tela_aluno.mostra_mensagem('----- ALUNOS CADASTRADOS -----')
            for aluno in self.__aluno_DAO.get_all():
                self.__tela_aluno.mostra_aluno({'matricula': aluno.matricula, 'curso': aluno.curso.nome, 'nome': aluno.nome, 'cpf': aluno.cpf, 'data_nasc': aluno.data_nasc})
    
    def inclui_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        if isinstance(dados_aluno['matricula'], int) and isinstance(dados_aluno['curso'], Curso) and isinstance(dados_aluno['nome'], str) and isinstance(dados_aluno['cpf'], str) and isinstance(dados_aluno['data_nasc'], datetime):
            aluno =  Aluno(dados_aluno['matricula'], dados_aluno['curso'], dados_aluno['nome'], dados_aluno['cpf'], dados_aluno['data_nasc'])
            if not self.pega_aluno_por_matricula(aluno.matricula):
                self.__aluno_DAO.add(aluno)
                self.__tela_aluno.mostra_mensagem('Aluno cadastrado com sucesso!')
            else:
                self.__tela_aluno.mostra_mensagem('ATENÇÃO: Aluno já cadastrado!')
        else:
            self.__tela_aluno.mostra_mensagem('ATENÇÃO: Algo de errado ocorreu durante o cadastro! Tente novamente!')
        
    def altera_aluno(self):
        self.lista_alunos()
        matricula =  self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)
        
        if aluno:
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno(editando=True)
            if isinstance(novos_dados_aluno['nome'], str):
                aluno.nome = novos_dados_aluno['nome']
            if isinstance(novos_dados_aluno['data_nasc'], datetime):
                aluno.data_nasc = novos_dados_aluno['data_nasc']
            self.__aluno_DAO.update(aluno)
            self.lista_alunos()
        else:
            self.__tela_aluno.mostra_mensagem('ATENÇÃO: Aluno não encontrado!')
    
    def exclui_aluno(self):
        self.lista_alunos()
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)
        
        if aluno:
            self.__aluno_DAO.remove(aluno.matricula)
            self.__tela_aluno.mostra_mensagem('Aluno excluído com sucesso!')
        else:
            self.__tela_aluno.mostra_mensagem('ATENÇÃO: Aluno não encontrado!')

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
    
    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.inclui_aluno,
                        '2': self.altera_aluno,
                        '3': self.lista_alunos,
                        '4': self.exclui_aluno,
                        '0': self.retorna}
        
        while True:
            opcao_escolhida = self.__tela_aluno.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_aluno.mostra_mensagem('ERRO: Opção inválida!\n')
