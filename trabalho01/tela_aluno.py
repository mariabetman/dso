class TelaAluno:
    def __init__(self, controlador_aluno):
        self.__controlador_aluno = controlador_aluno

    def tela_opcoes(self):
        print('---------- ALUNOS ----------')
        print('Escolha a opção')
        print('1 - Incluir Aluno')
        print('2 - Editar Aluno')
        print('3 - Listrar Aluno')
        print('4 - Excluir Aluno')
        print('0 - Retornar')
        
        opcao = int(input('\nEscolha sua opção: '))
        return opcao
    
    def pega_dados_aluno(self):
        print('---------- DADOS ALUNO ----------')
        matricula = int(input('Matrícula: '))
        print('---------- CURSOS DISPONÍVEIS ----------')
        curso = self.__controlador_aluno.__controlador_sistema.__controlador_curso.__tela_curso.seleciona_curso()
        nome = input('Nome: ')
        cpf = input('CPF: ')
        data_nasc = input('Data de Nascimento: ')
        
        return {'matricula': matricula, 'curso': curso, 'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
    def mostra_aluno(self, dados_aluno):
        print('Matrícula do Aluno: ', dados_aluno['matricula'])
        print('Curso do Aluno: ', dados_aluno['curso'])
        print('Nome do Aluno: ', dados_aluno['nome'])
        print('CPF do Aluno: ', dados_aluno['cpf'])
        print('Data de Nascimento do Aluno: ', dados_aluno['data_nasc'])
        print('-------------------------------------------------------')
        
    def seleciona_aluno(self):
        cpf = input('Digite o CPF do Aluno que deseja selecionar: ')
        return cpf
    
    def mostra_mensagem(self, msg):
        print(msg)
