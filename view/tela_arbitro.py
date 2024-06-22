from datetime import datetime
import PySimpleGUI as psg


class TelaArbitro:
    def __init__(self, controlador_arbitros):
        self.__controlador_arbitros = controlador_arbitros

    def tela_opcoes(self):
        print('\n---------- Árbitros ----------')
        print('1 - Incluir Árbitro')
        print('2 - Editar Árbitro')
        print('3 - Listar Árbitros')
        print('4 - Excluir Árbitro')
        print('0 - Retornar')
        
        opcao = (input('\nEscolha uma opção: '))
        return opcao

    def pega_dados_arbitro(self):
        psg.set_options(font=('Arial Bold', 16))
        layout = [
            [psg.Text('Nome ', size=(15,1)),psg.Input(expand_x=True, key='nome')],
            [psg.Text('CPF ', size=(15,1)), psg.Input(expand_x=True, key='cpf')],
            [psg.Text('Data de Nascimento ', size=(15,1)), psg.Input(expand_x=True, key='data_nasc')],
            [psg.OK(), psg.Cancel()]
        ]
        window = psg.Window('Form', layout, size=(715,207))
        event, values = window.read()
        window.close()
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
        print(f'\n{msg}')
