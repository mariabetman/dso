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
        psg.popup(msg)
