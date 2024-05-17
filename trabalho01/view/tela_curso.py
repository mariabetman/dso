class TelaCurso:
    def __init__(self, controlador_curso):
        self.__controlador_curso = controlador_curso

    def tela_opcoes(self):
        print('---------- Cursos ----------')
        print('Escolha a opção')
        print('1 - Incluir Curso')
        print('2 - Editar Curso')
        print('3 - Listrar Curso')
        print('4 - Excluir Curso')
        print('0 - Retornar')
        
        opcao = int(input('\nEscolha sua opção: '))
        return opcao
    
    def pega_dados_curso(self):
        print('---------- DADOS CURSO ----------')
        codigo = int(input('Código: '))
        nome = input('Nome: ')
        
        return {'codigo': codigo, 'nome': nome}
    
    def mostra_curso(self, dados_curso):
        print('Código do Curso: ', dados_curso['codigo'])
        print('Nome do Curso: ', dados_curso['nome'])
        print('-------------------------------------------------------')
        
    def seleciona_curso(self):
        codigo = input('Digite o código do Curso que deseja selecionar: ')
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)
