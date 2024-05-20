from datetime import datetime


class TelaAluno:
    def __init__(self, controlador_alunos):
        self.__controlador_alunos = controlador_alunos
        
    def tela_opcoes(self):
        print('\n---------- ALUNOS ----------')
        print('1 - Incluir Aluno')
        print('2 - Editar Aluno')
        print('3 - Listar Alunos')
        print('4 - Excluir Aluno')
        print('0 - Retornar')
        
        opcao = (input('\nEscolha uma opção: '))
        return opcao
    
    def pega_dados_aluno(self, editando=False):
        print('---------- DADOS ALUNO ----------')
        if not editando:
            cpf = input('CPF: ')
            matricula = int(input('Matrícula: '))
            codigo_curso =  self.__controlador_alunos.controlador_sistema.controlador_cursos.tela_curso.seleciona_curso()
            curso = self.__controlador_alunos.controlador_sistema.controlador_cursos.pega_curso_por_codigo(codigo_curso)
        else:
            cpf = None
            matricula = None
            curso = None
        nome = input('Nome do Aluno: ')
        data_nasc = datetime.strptime(input('Data de Nascimento no formato DD/MM/AAAA: '), "%d/%m/%Y")
        
        return {'matricula': matricula, 'curso': curso, 'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
    def mostra_aluno(self, dados_aluno):
        print('Matrícula do Aluno: ', dados_aluno['matricula'])
        print('Curso: ', dados_aluno['curso'])
        print('Nome: ', dados_aluno['nome'])
        print('CPF: ', dados_aluno['cpf'])
        print('Data de Nascimento: ', dados_aluno['data_nasc'])
        print('-------------------------------------------------------')
        
    def seleciona_aluno(self):
        matricula = int(input('Digite a matrícula do Aluno que deseja selecionar: '))
        return matricula
    
    def mostra_mensagem(self, msg):
        print(f'\n{msg}\n')
