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
            [psg.Button('Confirmar', bind_return_key=True)]
        ]

        window = psg.Window('Tela Árbitro', layout)
        event, values = window.read()

        if event == psg.WIN_CLOSED:
            window.close()
            return '0'
        else:
            opcao = values['OPCAO']
            window.close()
            return opcao

    def pega_dados_arbitro(self):
        layout = [
            [psg.Text('Preencha os dados do árbitro')],
            [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome', focus=True)],
            [psg.Text('CPF: ', size=(15,1)), psg.Input(expand_x=True, key='cpf')],
            [psg.Text('Data de Nascimento ', size=(15,1)), psg.Input(expand_x=True, key='data_nasc')],
            [psg.Button('Adicionar', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
        ]

        window = psg.Window('Formulário Árbitro', layout, size=(715,207))
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            self.__controlador_arbitros.abre_tela()
        else:
            window.close()
            ##Falta verificar a dat de nascimento
            return {'nome': values['nome'], 'cpf': values['cpf'], 'data_nasc': datetime.strptime(values['data_nasc'],  "%d/%m/%Y")}

    def mostra_arbitro(self, dados_arbitro):
        print('Nome do Árbitro: ', dados_arbitro['nome'])
        print('CPF do Árbitro: ', dados_arbitro['cpf'])
        print('Data de Nascimento do Árbitro: ', dados_arbitro['data_nasc'])
        print()
        
    def seleciona_arbitro(self):
        self.__controlador_arbitros.lista_arbitros()
        cpf = input('Digite o CPF do Árbitro que deseja selecionar: ')
        return cpf
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)
