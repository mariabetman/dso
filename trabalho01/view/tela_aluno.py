class TelaAluno:
    def __init__(self, controlador_aluno):
        self.__controlador_aluno = controlador_aluno

    def tela_opcoes(self):
        print('---------- ÁRBITROS ----------')
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
        curso = controlador_aluno.controlador_sistema.controlador_curso.pega_curso_por_codigo(int(input('Código do curso: ')))
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
