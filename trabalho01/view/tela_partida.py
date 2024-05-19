class TelaPartida:
    def __init__(self, controlador_partida):
        self.__controlador_partida = controlador_partida

    def tela_opcoes(self):
        print('---------- PARTIDAS ----------')
        print('Escolha a opção')
        print('1 - Incluir Partida')
        print('2 - Editar Partida')
        print('3 - Listrar Partida')
        print('4 - Excluir Partida')
        print('0 - Retornar')
        
        opcao = int(input('\nEscolha sua opção: '))
        return opcao
    
    def pega_dados_partida(self):
        print('---------- DADOS PARTIDA ----------')
        codigo = int(input('Código: '))
        print('---------- CURSOS DISPONÍVEIS ----------')
        curso = controlador_partida.controlador_sistema.controlador_curso.pega_curso_por_codigo(int(input('Código do curso: ')))
        nome = input('Nome: ')
        cpf = input('CPF: ')
        data_nasc = input('Data de Nascimento: ')
        
        return {'matricula': matricula, 'curso': curso, 'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
    def mostra_partida(self, dados_partida):
        print('Matrícula do partida: ', dados_aluno['matricula'])
        print('Curso do Aluno: ', dados_aluno['curso'])
        print('Nome do Aluno: ', dados_aluno['nome'])
        print('CPF do Aluno: ', dados_aluno['cpf'])
        print('Data de Nascimento do Aluno: ', dados_aluno['data_nasc'])
        print('-------------------------------------------------------')
        
    def seleciona_partida(self):
        codigo = input('Digite o código do Partida que deseja selecionar: ')
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)
