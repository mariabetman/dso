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
        if not editando:
            layout = [
                [psg.Text('Preencha os dados da equipe')],
                [psg.Text('Código: ', size=(15,1)),psg.Input(expand_x=True, key='codigo', focus=True)],
                [psg.Text('Código do Curso: ', size=(15,1)),psg.Input(expand_x=True, key='codigo_curso')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome')],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
            ]
        else:
            layout = [
                [psg.Text('Preencha os dados da equipe')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome', focus=True)],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
            ]

        window = psg.Window('Formulário Equipe', layout, size=(715,207))
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            self.__controlador_equipes.abre_tela()
            return None
        else:
            if not editando:
                try:
                    codigo = int(values['codigo'])
                except ValueError:
                    window.close()
                    self.mostra_mensagem('\nDigite um valor válido para o código!\n')
                    self.__controlador_equipes.abre_tela()
                    return None
                try:
                    codigo_curso = int(values['codigo_curso'])
                except ValueError:
                    window.close()
                    self.mostra_mensagem('\nDigite um valor válido para o código do curso!\n')
                    self.__controlador_equipes.abre_tela()
                    return None
            else:
                codigo = None
                codigo_curso = None
            nome = values['nome']
            
            window.close()
            return {'codigo': codigo, 'codigo_curso': codigo_curso, 'nome': nome}
    
    def mostra_equipe(self, equipes):
        layout = [
            [psg.Text('Equipes cadastradas')],
            [psg.Multiline(default_text='', size=(60, 15), key='LISTA_EQUIPES', disabled=True)],
            [psg.Button('Fechar', bind_return_key=True)]
        ]

        window = psg.Window('Lista de Equipes', layout, finalize=True)

        lista_equipes = ""
        for equipe in equipes:
            lista_equipes += f"Matrícula: {equipe.matricula}\n"
            lista_equipes += f"Curso: {equipe.curso.nome}\n"
            lista_equipes += f"Nome: {equipe.nome}\n"
            lista_equipes += "-" * 40 + "\n"

        window['LISTA_EQUIPES'].update(lista_equipes)

        while True:
            event = window.read()
            if event == psg.WIN_CLOSED or event == 'Fechar':
                window.close()
                self.__controlador_equipes.abre_tela()
        
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


