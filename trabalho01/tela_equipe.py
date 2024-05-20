class TelaEquipe:
    def __init__(self, controlador_equipes):
        self.__controlador_equipes = controlador_equipes
        
    def tela_opcoes(self):
        print('\n---------- EQUIPES ----------')
        print('1 - Incluir Equipe')
        print('2 - Editar Equipe')
        print('3 - Listar Equipes')
        print('4 - Excluir Equipe')
        print('5 - Adicionar Aluno na Equipe')
        print('6 - Remover Aluno da Equipe')
        print('7 - Listar Alunos da Equipe')
        print('0 - Retornar')
        
        opcao = (input('\nEscolha uma opção: '))
        return opcao
    
    def pega_dados_equipe(self, editando=False):
        print('---------- DADOS EQUIPE ----------')
        if not editando:
            codigo = int(input('Código: '))
            codigo_curso =  self.__controlador_equipes.controlador_sistema.controlador_cursos.tela_curso.seleciona_curso()
            curso = self.__controlador_equipes.controlador_sistema.controlador_cursos.pega_curso_por_codigo(codigo_curso)      
        else:
            codigo = None
            curso = None 
        nome = input('Nome da Equipe: ')
        return {'curso': curso, 'nome': nome, 'codigo': codigo}
    
    def mostra_equipe(self, dados_equipe):
        print(f"{dados_equipe['codigo']} - {dados_equipe['nome']} - {dados_equipe['curso']}")
        print('-------------------------------------------------------')
        
    def seleciona_equipe(self):
        self.__controlador_equipes.lista_equipes()
        codigo = int(input('Digite o Código da Equipe que deseja selecionar: '))
        return codigo
    
    def mostra_mensagem(self, msg):
        print(f'\n{msg}')


