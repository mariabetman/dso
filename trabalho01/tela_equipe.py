

class TelaEquipe:
    def __init__(self, controlador_equipe):
        self.__controlador_equipe = controlador_equipe
        
    def tela_opcoes(self):
        print('---------- EQUIPES ----------')
        print('1 - Incluir Equipe')
        print('2 - Editar Equipe')
        print('3 - Listar Equipe')
        print('4 - Excluir Equipe')
        print('5 - Adicionar Aluno na Equipe')
        print('6 - Remover Aluno da Equipe')
        print('0 - Retornar')
        
        opcao = (input('\nEscolha uma opção: '))
        return opcao
    
    def pega_dados_equipe(self):
        print('---------- DADOS EQUIPE ----------')
        codigo_curso =  self.__controlador_equipe.controlador_sistema.controlador_cursos.tela_curso.seleciona_curso()
        curso = self.__controlador_equipe.controlador_sistema.controlador_cursos.pega_curso_por_codigo(codigo_curso)
        nome = input('Nome da Equipe: ')
        codigo = int(input('Código: '))
        
        return {'curso': curso, 'nome': nome, 'codigo': codigo}
    
    def mostra_equipe(self, dados_equipe):
        print(dados_equipe)
        print('Curso da Equipe: ', dados_equipe['curso'])
        print('Nome da Equipe: ', dados_equipe['nome'])
        print('Código da Equipe: ', dados_equipe['codigo'])
        print('-------------------------------------------------------')
        
    def seleciona_equipe(self):
        self.__controlador_equipe.lista_equipes()
        codigo = int(input('Digite o Código da Equipe que deseja selecionar: '))
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)


