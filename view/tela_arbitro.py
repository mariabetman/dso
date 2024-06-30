import PySimpleGUI as psg
from datetime import datetime


class TelaArbitro:
    def __init__(self, controlador_arbitros):
        self.__controlador_arbitros = controlador_arbitros

    def tela_opcoes(self):
        layout = [
            [psg.Text('---------- Árbitros ----------')],
            [psg.Text('Escolha uma opção')],
            [psg.Text('1 - Incluir Árbitro')],
            [psg.Text('2 - Editar Árbitro')],
            [psg.Text('3 - Listar Árbitros')],
            [psg.Text('4 - Excluir Árbitro')],
            [psg.Text('0 - Retornar')],
            [psg.Input(key='OPCAO', size=(10, 1), do_not_clear=False, focus=True)],
            [psg.Button('Ok', bind_return_key=True), psg.Button('Voltar', bind_return_key=True)]
        ]

        window = psg.Window('Tela Árbitro', layout)
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == 'Voltar':
            window.close()
            return '0'
        else:
            opcao = values['OPCAO']
            window.close()
            return opcao

    def pega_dados_arbitro(self, editando=False):
        if not editando:
            layout = [
                [psg.Text('Preencha os dados do árbitro')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome', focus=True)],
                [psg.Text('CPF: ', size=(15,1)), psg.Input(expand_x=True, key='cpf')],
                [psg.Text('Data de Nascimento (DD/MM/AAAA) ', size=(15,1)), psg.Input(expand_x=True, key='data_nasc')],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
            ]
        else:
            layout = [
                [psg.Text('Preencha os dados do árbitro')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome', focus=True)],
                [psg.Text('Data de Nascimento (DD/MM/AAAA) ', size=(15,1)), psg.Input(expand_x=True, key='data_nasc')],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
            ]

        window = psg.Window('Formulário Árbitro', layout, size=(715,207))
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            self.__controlador_arbitros.abre_tela()
            return None
        else:
            nome = values['nome']
            if not editando:
                cpf = values['cpf']
            else:
                cpf = None
            try:
                data_nasc = datetime.strptime(values['data_nasc'], "%d/%m/%Y")
            except ValueError:
                window.close()
                self.mostra_mensagem('\nDigite um valor válido para a data de nascimento!\n')
                self.__controlador_arbitros.abre_tela()
                return None

            window.close()
            return {'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
            
    def mostra_arbitro(self, arbitros):
        layout = [
            [psg.Text('Árbitros cadastrados')],
            [psg.Multiline(default_text='', size=(60, 15), key='LISTA_ARBITROS', disabled=True)],
            [psg.Button('Fechar', bind_return_key=True)]
        ]

        window = psg.Window('Lista de Árbitros', layout, finalize=True)

        lista_arbitros = ""
        for arbitro in arbitros:
            lista_arbitros += f"Nome: {arbitro.nome}\n"
            lista_arbitros += f"CPF: {arbitro.cpf}\n"
            lista_arbitros += f"Data de Nascimento: {arbitro.data_nasc.strftime('%d/%m/%Y')}\n"
            lista_arbitros += "-" * 40 + "\n"

        window['LISTA_ARBITROS'].update(lista_arbitros)

        while True:
            event = window.read()
            if event == psg.WIN_CLOSED or event == 'Fechar':
                window.close()
                self.__controlador_arbitros.abre_tela()
            
    def seleciona_arbitro(self):
        self.__controlador_arbitros.lista_arbitros()
        
        layout = [
            [psg.Text('Digite o CPF do Árbitro que deseja selecionar:')],
            [psg.Input(key='cpf', focus=True)],
            [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
        ]
        
        window = psg.Window('Seleciona Árbitro', layout, finalize=True)
        
        event, values = window.read()

        if event == psg.WIN_CLOSED  or event == 'Cancelar':
            window.close()
            self.__controlador_arbitros.abre_tela()
            return None
        else:
            cpf = values['cpf']
            window.close()
            self.__controlador_arbitros.abre_tela()
            return cpf
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)
