from datetime import datetime


class TelaAluno:
    def __init__(self, controlador_alunos):
        self.__controlador_alunos = controlador_alunos
        
    def tela_opcoes(self):
        print('---------- ALUNOS ----------')
        print('1 - Incluir Aluno')
        print('2 - Editar Aluno')
        print('3 - Listar Alunos')
        print('4 - Excluir Aluno')
        print('0 - Retornar')
        
        opcao = int(input('\nEscolha uma opção: '))
        return opcao
    
    def pega_dados_aluno(self):
        print('---------- DADOS ALUNO ----------')
        matricula = int(input('Matrícula: '))
        codigo_curso =  self.__controlador_alunos.controlador_sistema.controlador_cursos.tela_curso.seleciona_curso()
        curso = self.__controlador_alunos.controlador_sistema.controlador_cursos.pega_curso_por_codigo(codigo_curso)
        nome = input('Nome do Aluno: ')
        cpf = input('CPF: ')
        data_nasc = datetime.strptime(input('Data de Nascimento no formato DD/MM/AAAA: '), "%d/%m/%Y")
        
        return {'matricula': matricula, 'curso': curso, 'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
    def mostra_aluno(self, dados_aluno):
        print(dados_aluno)
        print('Matrícula do Aluno: ', dados_aluno['matricula'])
        print('Curso do Aluno: ', dados_aluno['curso'])
        print('Nome do Aluno: ', dados_aluno['nome'])
        print('CPF do Aluno: ', dados_aluno['cpf'])
        print('Data de Nascimento do Aluno: ', dados_aluno['data_nasc'])
        print('-------------------------------------------------------')
        
    def seleciona_aluno(self):
        self.__controlador_alunos.lista_alunos()
        cpf = input('Digite o CPF do Aluno que deseja selecionar: ')
        return cpf
    
    def mostra_mensagem(self, msg):
        print(msg)


