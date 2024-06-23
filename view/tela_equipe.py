import PySimpleGUI as psg


class TelaEquipe:
    def __init__(self, controlador_equipes):
        self.__controlador_equipes = controlador_equipes
        
    def tela_opcoes(self):
        layout = [
            [psg.Text('---------- Equipes ----------')],
            [psg.Text('Escolha uma opção')],
            [psg.Text('1 - Incluir Equipe')],
            [psg.Text('2 - Editar Equipe')],
            [psg.Text('3 - Listar Equipes')],
            [psg.Text('4 - Excluir Equipe')],
            [psg.Text('0 - Retornar')],
            [psg.Input(key='OPCAO', size=(10, 1), do_not_clear=False, focus=True)],
            [psg.Button('Confirmar', bind_return_key=True)]
        ]

        window = psg.Window('Tela Equipe', layout)
        event, values = window.read()

        if event == psg.WIN_CLOSED:
            window.close()
            return '0'
        else:
            opcao = values['OPCAO']
            window.close()
            return opcao
    
    def pega_dados_equipe(self, editando=False):
        print('---------- DADOS EQUIPE ----------')
        if not editando:
            try:
                codigo = int(input('Código: '))
            except:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                return self.__controlador_equipes.abre_tela()
            try:
                codigo_curso = int(input('Código do curso: '))
            except:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                return self.__controlador_equipes.abre_tela()     
        else:
            codigo = None
            codigo_curso = None 
        nome = input('Nome da Equipe: ')
        return {'codigo_curso': codigo_curso, 'nome': nome, 'codigo': codigo}
    
    def mostra_equipe(self, dados_equipe):
        print(f"{dados_equipe['codigo']} - {dados_equipe['nome']} - {dados_equipe['curso']}")
        print('-------------------------------------------------------')
        
    def seleciona_equipe(self):
        self.__controlador_equipes.lista_equipes()
        try:
            codigo = int(input('Digite o Código da Equipe que deseja selecionar: '))
            return codigo
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            return self.__controlador_equipes.abre_tela()
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)


