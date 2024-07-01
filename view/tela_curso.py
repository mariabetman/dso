import PySimpleGUI as psg


class TelaCurso:
    def __init__(self, controlador_cursos):
        self.__controlador_cursos = controlador_cursos

    def tela_opcoes(self):
        layout = [
            [psg.Text('---------- Cursos ----------')],
            [psg.Text('Escolha uma opção')],
            [psg.Text('1 - Incluir Curso')],
            [psg.Text('2 - Editar Curso')],
            [psg.Text('3 - Listar Cursos')],
            [psg.Text('4 - Excluir Curso')],
            [psg.Text('0 - Retornar')],
            [psg.Input(key='OPCAO', size=(10, 1), do_not_clear=False, focus=True)],
            [psg.Button('Confirmar', bind_return_key=True)]
        ]

        window = psg.Window('Tela Curso', layout)
        event, values = window.read()

        if event == psg.WIN_CLOSED:
            window.close()
            return '0'
        else:
            opcao = values['OPCAO']
            window.close()
            return opcao

    def pega_dados_curso(self, editando=False):
        if not editando:
            layout = [
                [psg.Text('Preencha os dados do curso')],
                [psg.Text('Código: ', size=(15,1)),psg.Input(expand_x=True, key='codigo', focus=True)],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome')],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar')]
            ]
        else:
            layout = [
                [psg.Text('Preencha os dados do curso')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome', focus=True)],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar')]
            ]

        window = psg.Window('Formulário Curso', layout, size=(715,207))
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            self.__controlador_cursos.abre_tela()
            return None
        else:
            if not editando:
                try:
                    codigo = int(values['codigo'])
                except ValueError:
                    window.close()
                    self.mostra_mensagem('\nDigite um valor válido para o código!\n')
                    self.__controlador_cursos.abre_tela()
                    return None
            else:
                codigo = None
            nome = values['nome']
            
            window.close()
            return {'codigo': codigo, 'nome': nome}
    
    def mostra_cursos(self, cursos):
        layout = [
            [psg.Text('Cursos cadastrados')],
            [psg.Multiline(default_text='', size=(60, 15), key='LISTA_CURSOS', disabled=True)],
            [psg.Button('Fechar', bind_return_key=True)]
        ]

        window = psg.Window('Lista de Cursos', layout, finalize=True)

        lista_cursos = ""
        for curso in cursos:
            lista_cursos += f"Código: {curso.codigo}\n"
            lista_cursos += f"Nome: {curso.nome}\n"
            lista_cursos += "-" * 40 + "\n"

        window['LISTA_CURSOS'].update(lista_cursos)

        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED or event == 'Fechar':
                window.close()
                self.__controlador_cursos.abre_tela()
                return
        
    def seleciona_curso(self):
        layout = [
            [psg.Text('Digite o código do Curso que deseja selecionar:')],
            [psg.Input(key='codigo', focus=True)],
            [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar')]
        ]
        
        window = psg.Window('Seleciona Curso', layout, finalize=True)
        
        event, values = window.read()
        if event == psg.WIN_CLOSED  or event == 'Cancelar':
            window.close()
            self.__controlador_cursos.abre_tela()
            return None
        elif event == 'Ok':
            try:
                codigo = int(values['codigo'])
                window.close()
                return codigo
            except:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                window.close()
                self.__controlador_cursos.abre_tela()
                return None
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)
