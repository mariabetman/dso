import PySimpleGUI as psg
from model.partida import Partida


class TelaPartida:
    def __init__(self, controlador_partidas):
        self.__controlador_partidas = controlador_partidas

    def tela_opcoes(self):
        layout = [
            [psg.Text('---------- Partidas ----------')],
            [psg.Text('Escolha uma opção')],
            [psg.Text('1 - Incluir Partida')],
            [psg.Text('2 - Editar Partida')],
            [psg.Text('3 - Listar Partidas')],
            [psg.Text('4 - Excluir Partida')],
            [psg.Text('0 - Retornar')],
            [psg.Input(key='OPCAO', size=(10, 1), do_not_clear=False, focus=True)],
            [psg.Button('Confirmar', bind_return_key=True)]
        ]

        window = psg.Window('Tela Partida', layout)
        event, values = window.read()

        if event == psg.WIN_CLOSED:
            window.close()
            return '0'
        else:
            opcao = values['OPCAO']
            window.close()
            return opcao
        
    def pega_gols_partida(self, partida):
        layout = [
            [psg.Text('---------- GOLS PARTIDA ----------')],
            [psg.Text('---------- *Caso a equipe não tenha feito nenhum gol, por favor digite 0! ----------')],
            [psg.Text('Gols Equipe Casa: '), psg.Input(key='gols_equipe_casa', focus=True)],
            [psg.Text('Gols Equipe Visitante: '), psg.Input(key='gols_equipe_visitante')],
            [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
        ]

        window = psg.Window('Gols da Partida', layout)
        event, values = window.read()

        if event == 'Cancelar' or event == psg.WIN_CLOSED:
            window.close()
            self.__controlador_partidas.abre_tela()
            return None
        
        try:
            gols_equipe_casa = int(values['gols_equipe_casa'])
            gols_equipe_visitante = int(values['gols_equipe_visitante'])
        except ValueError:
            self.mostra_mensagem('Digite um valor válido!')
            window.close()
            self.__controlador_partidas.abre_tela()
            return None

        artilheiros_equipe_casa = []
        alunos_equipe_casa = partida.equipe_casa.alunos 
        for i in range(gols_equipe_casa):
            layout = [
                [psg.Text(f'Selecione o Artilheiro do {i+1}º gol da Equipe Casa!')],
                [psg.Listbox(values=[f"{aluno.matricula} - {aluno.nome}" for aluno in alunos_equipe_casa], size=(30, 6), key='matricula_artilheiro', select_mode='single')],
                [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
            ]

            artilheiro_window = psg.Window('Seleciona Artilheiro', layout)
            artilheiro_event, artilheiro_values = artilheiro_window.read()

            if artilheiro_event == 'Cancelar' or artilheiro_event == psg.WIN_CLOSED:
                artilheiro_window.close()
                self.__controlador_partidas.abre_tela()
                return None
            
            matricula_artilheiro_gol = artilheiro_values['matricula_artilheiro'][0].split(" - ")[0]
            artilheiros_equipe_casa.append(matricula_artilheiro_gol)
            artilheiro_window.close()

        artilheiros_equipe_visitante = []
        alunos_equipe_visitante = partida.equipe_casa.alunos 
        for i in range(gols_equipe_visitante):
            layout = [
                [psg.Text(f'Selecione o Artilheiro do {i+1}º gol da Equipe Visitante!')],
                [psg.Listbox(values=[f"{aluno.matricula} - {aluno.nome}" for aluno in alunos_equipe_visitante], size=(30, 6), key='matricula_artilheiro', select_mode='single')],
                [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
            ]

            artilheiro_window = psg.Window('Seleciona Artilheiro', layout)
            artilheiro_event, artilheiro_values = artilheiro_window.read()

            if artilheiro_event == 'Cancelar' or artilheiro_event == psg.WIN_CLOSED:
                artilheiro_window.close()
                self.__controlador_partidas.abre_tela()
                return None
            
            matricula_artilheiro_gol = artilheiro_values['matricula_artilheiro'][0].split(" - ")[0]
            artilheiros_equipe_visitante.append(matricula_artilheiro_gol)
            artilheiro_window.close()
        
        self.__controlador_partidas.abre_tela()
        return {
            'gols_equipe_casa': gols_equipe_casa,
            'artilheiros_equipe_casa': artilheiros_equipe_casa,
            'gols_equipe_visitante': gols_equipe_visitante,
            'artilheiros_equipe_visitante': artilheiros_equipe_visitante
        }

    def mostra_partida(self, dados_partida):
        print('Código da partida: ', dados_partida['codigo'])
        print('Data da partida: ', dados_partida['data_partida'])
        print('Equipe Casa: ', dados_partida['equipe_casa'])
        print('Equipe Visitante: ', dados_partida['equipe_visitante'])
        print('Árbitro da Partida: ', dados_partida['arbitro'])
        print('Partida Realizada?: ', dados_partida['partida_realizada'])
        if dados_partida['partida_realizada']:
            print('Gols da Equipe Casa: ', dados_partida['gols_equipe_casa'])
            print('Gols da Equipe Visitante: ', dados_partida['gols_equipe_visitante'])
            print('Resultado da Partida: ', dados_partida['resultado'])
        print('-------------------------------------------------------')
        
    def seleciona_partida(self):
        self.__controlador_partidas.lista_partidas()
        try:
            codigo = int(input('Digite o código da Partida que deseja selecionar: '))
            return codigo
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            return self.__controlador_partidas.abre_tela()
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)
