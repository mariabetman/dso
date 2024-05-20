class TelaCurso:
    def __init__(self, controlador_cursos):
        self.__controlador_cursos = controlador_cursos

    def tela_opcoes(self):
        print('\n---------- Cursos ----------')
        print('1 - Incluir Curso')
        print('2 - Editar Curso')
        print('3 - Listar Cursos')
        print('4 - Excluir Curso')
        print('0 - Retornar')
        
        opcao = (input('\nEscolha uma opção: '))
        return opcao
    
    def pega_dados_curso(self, editando=False):
        print('\n---------- DADOS CURSO ----------')
        if not editando:
            try:
                codigo = int(input('Código: '))
            except:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                return self.__controlador_cursos.abre_tela()
        else:
            codigo = None
        nome = input('Nome: ')
        
        return {'codigo': codigo, 'nome': nome}
    
    def mostra_curso(self, dados_curso):
        '''print('Código do Curso: ', dados_curso['codigo'])
        print('Nome do Curso: ', dados_curso['nome'])
        print()'''
        print(f"{dados_curso['codigo']} - {dados_curso['nome']}")
        
    def seleciona_curso(self):
        self.__controlador_cursos.lista_cursos()
        try:
            codigo = int(input('Digite o código do curso que deseja selecionar: '))
            return codigo
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            return self.__controlador_cursos.abre_tela()
    
    def mostra_mensagem(self, msg):
        print(f'\n{msg}')
