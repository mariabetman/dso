import PySimpleGUI as psg
from model.partida import Partida


class TelaPartida:
    def __init__(self, controlador_partidas):
        self.__controlador_partidas = controlador_partidas

    def tela_opcoes(self):
        layout = [
            [psg.Text('---------- Partidas ----------')],
            [psg.Text('Escolha uma opção')],
            [psg.Text('1 - Listar Partidas')],
            [psg.Text('2 - Adicionar gols Partida')],
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
            [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar')]
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
            window.close()
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
                [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar')]
            ]

            artilheiro_window = psg.Window('Seleciona Artilheiro', layout)
            artilheiro_event, artilheiro_values = artilheiro_window.read()

            if artilheiro_event == 'Cancelar' or artilheiro_event == psg.WIN_CLOSED:
                artilheiro_window.close()
                self.__controlador_partidas.abre_tela()
                return None
            
            matricula_artilheiro_gol = int(artilheiro_values['matricula_artilheiro'][0].split(" - ")[0])
            artilheiros_equipe_casa.append(matricula_artilheiro_gol)
            artilheiro_window.close()

        artilheiros_equipe_visitante = []
        alunos_equipe_visitante = partida.equipe_visitante.alunos 
        for i in range(gols_equipe_visitante):
            layout = [
                [psg.Text(f'Selecione o Artilheiro do {i+1}º gol da Equipe Visitante!')],
                [psg.Listbox(values=[f"{aluno.matricula} - {aluno.nome}" for aluno in alunos_equipe_visitante], size=(30, 6), key='matricula_artilheiro', select_mode='single')],
                [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar')]
            ]

            artilheiro_window = psg.Window('Seleciona Artilheiro', layout)
            artilheiro_event, artilheiro_values = artilheiro_window.read()

            if artilheiro_event == 'Cancelar' or artilheiro_event == psg.WIN_CLOSED:
                artilheiro_window.close()
                self.__controlador_partidas.abre_tela()
                return None
            
            matricula_artilheiro_gol = int(artilheiro_values['matricula_artilheiro'][0].split(" - ")[0])
            artilheiros_equipe_visitante.append(matricula_artilheiro_gol)
            artilheiro_window.close()
        
        return {
            'gols_equipe_casa': gols_equipe_casa,
            'artilheiros_equipe_casa': artilheiros_equipe_casa,
            'gols_equipe_visitante': gols_equipe_visitante,
            'artilheiros_equipe_visitante': artilheiros_equipe_visitante
        }

    def mostra_partidas(self, partidas):
        layout = [
            [psg.Text('Partidas cadastradas')],
            [psg.Multiline(default_text='', size=(60, 15), key='LISTA_PARTIDAS', disabled=True)],
            [psg.Button('Fechar', bind_return_key=True)]
        ]

        window = psg.Window('Lista de Partidas', layout, finalize=True)

        lista_partidas = ""
        for partida in partidas:
            lista_partidas += f"Código: {partida.codigo}\n"
            lista_partidas += f"Data da partida: {partida.data_partida.strftime('%d/%m/%Y')}\n"
            lista_partidas += f"Equipe Casa: {partida.equipe_casa.nome}\n"
            lista_partidas += f"Equipe Visitante: {partida.equipe_visitante.nome}\n"
            lista_partidas += f"Árbitro: {partida.arbitro.nome}\n"
            lista_partidas += f"Partida realizada: {'Sim' if partida.partida_realizada else 'Não'}\n"
            lista_partidas += f"Gols equipe casa: {partida.gols_equipe_casa if partida.gols_equipe_casa else '-'}\n"
            lista_partidas += f"Gols equipe visitante: {partida.gols_equipe_visitante if partida.gols_equipe_visitante else '-'}\n"
    
            if partida.partida_realizada:
                lista_partidas += "Artilheiros equipe casa:\n"
                for artilheiro in partida.artilheiros_equipe_casa:
                    lista_partidas += f" - {artilheiro.nome}\n"
                lista_partidas += "Artilheiros equipe visitante:\n"
                for artilheiro in partida.artilheiros_equipe_visitante:
                    lista_partidas += f" - {artilheiro.nome}\n"
            lista_partidas += "-" * 40 + "\n"

        window['LISTA_PARTIDAS'].update(lista_partidas)

        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED or event == 'Fechar':
                window.close()
                self.__controlador_partidas.abre_tela()
                return
        
    def seleciona_partida(self):
        layout = [
            [psg.Text('Digite o códgio da Partida que deseja selecionar:')],
            [psg.Input(key='codigo', focus=True)],
            [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar', bind_return_key=True)]
        ]
        
        window = psg.Window('Seleciona Partida', layout, finalize=True)
        
        event, values = window.read()

        if event == psg.WIN_CLOSED  or event == 'Cancelar':
            window.close()
            self.__controlador_partidas.abre_tela()
            return None
        else:
            try:
                codigo = int(values['codigo'])
                window.close()
                return codigo
            except ValueError:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                window.close()
                self.__controlador_partidas.abre_tela()
                return None
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)
