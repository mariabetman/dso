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
            [psg.Text('5 - Adicionar Aluno na Equipe')],
            [psg.Text('6 - Remover Aluno da Equipe')],
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
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar')]
            ]
        else:
            layout = [
                [psg.Text('Preencha os dados da equipe')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome', focus=True)],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar')]
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
    
    def mostra_equipes(self, equipes):
        layout = [
            [psg.Text('Equipes cadastradas')],
            [psg.Multiline(default_text='', size=(60, 15), key='LISTA_EQUIPES', disabled=True)],
            [psg.Button('Fechar', bind_return_key=True)]
        ]

        window = psg.Window('Lista de Equipes', layout, finalize=True)

        lista_equipes = ""
        for equipe in equipes:
            lista_equipes += f"Código: {equipe.codigo}\n"
            lista_equipes += f"Curso: {equipe.curso.nome}\n"
            lista_equipes += f"Nome: {equipe.nome}\n"
            for aluno in equipe.alunos:
                lista_equipes += f"  - Matrícula: {aluno.matricula}, Nome: {aluno.nome}\n"
            lista_equipes += "-" * 40 + "\n"

        window['LISTA_EQUIPES'].update(lista_equipes)

        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED or event == 'Fechar':
                window.close()
                self.__controlador_equipes.abre_tela()
                return
        
    def seleciona_equipe(self):
        layout = [
            [psg.Text('Digite o código da Equipe que deseja selecionar:')],
            [psg.Input(key='codigo', focus=True)],
            [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar')]
        ]
        
        window = psg.Window('Seleciona Equipe', layout, finalize=True)
        
        event, values = window.read()

        if event == psg.WIN_CLOSED  or event == 'Cancelar':
            window.close()
            self.__controlador_equipes.abre_tela()
            return None
        else:
            try:
                codigo = int(values['codigo'])
                window.close()
                return codigo
            except ValueError:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                window.close()
                self.__controlador_alunos.abre_tela()
                return None
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)


