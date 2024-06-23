import PySimpleGUI as psg


class TelaSistema:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        layout = [
            [psg.Text('Bem-vindo ao sistema de gerenciamento de campeonato universitário!')],
            [psg.Text('---------- MENU PRINCIPAL ----------')],
            [psg.Text('*Apenas inicie o Campeonato após criar as Equipes que irão participar!!!')],
            [psg.Text('Escolha uma opção')],
            [psg.Text('1 - Menu de Cursos')],
            [psg.Text('2 - Menu de Alunos')],
            [psg.Text('3 - Menu de Equipes')],
            [psg.Text('4 - Menu de Árbitros')],
            [psg.Text('5 - Iniciar Campeonato')],
            [psg.Text('6 - Finalizar Campeonato')],
            [psg.Text('0 - Encerrar Programa')],
            [psg.Input(key='OPCAO', size=(10, 1), do_not_clear=False, focus=True)],
            [psg.Button('Confirmar', bind_return_key=True)]
        ]

        window = psg.Window('Tela Sistema', layout)
        event, values = window.read()

        if event == psg.WIN_CLOSED:
            window.close()
            self.__controlador_sistema.abre_tela()
        else:
            opcao = values['OPCAO']
            window.close()
            return opcao
        
    def mostra_mensagem(self, msg):
        psg.popup(msg)
