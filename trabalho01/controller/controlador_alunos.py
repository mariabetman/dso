from model.aluno import Aluno
from view.tela_aluno import TelaAluno


class ControladorAluno:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno(self)
        self.__controlador_sistema = controlador_sistema
        
    def pega_aluno_por_cpf(self, cpf:str):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                return aluno
        return "Não existe aluno com esse cpf cadastrado"
    
    def listar_alunos(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostra_aluno({'matricula': matricula, 'codigo_curso': codigo_curso, 'nome': aluno.nome, 'cpf': aluno.cpf, 'data_nasc': aluno.data_nasc})
    
    def incluir_aluno(self):
        dados_aluno = self.tela_aluno.pega_dados_aluno()
        aluno =  Aluno(int(dados_aluno['matricula']), dados_aluno['curso'], dados_aluno['nome'], dados_aluno['cpf'], dados_aluno['data_nasc'])
        if not self.pega_aluno_por_cpf(aluno.cpf):
            self.__alunos.append(aluno)
        else:
            self.__tela_aluno.mostra_mensagem('ATENÇÃO: Aluno já cadastrado!')
    
    def alterar_aluno(self):
        self.listar_alunos()
        cpf_aluno =  self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_cpf(cpf_aluno)
        
        if aluno:
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            if isinstance(matricula, int):
                aluno.matricula = novos_dados_aluno['matricula']
            if isinstance(curso, Curso):
                aluno.curso = novos_dados_aluno['curso']
            if isinstance(nome, str):
                aluno.nome = novos_dados_aluno['nome']
            if isinstance(cpf, str):
                aluno.cpf = novos_dados_aluno['cpf']
            if isinstance(data_nasc, str):
                aluno.data_nasc = novos_dados_aluno['data_nasc']
            self.listar_alunos()
        else:
            self.__tela_aluno.mostra_mensagem('ATENÇÃO: Aluno não encontrado!')
    
    def excluir_aluno(self):
        self.listar_alunos()
        cpf_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_cpf(cpf_aluno)
        
        if aluno:
            self.__alunos.remove(aluno)
            self.listar_alunos()
        else:
            self.__tela_aluno.mostra_mensagem('ATENÇÃO: Aluno não encontrado!')
    
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
