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
    
    def pega_gols_partida(self, partida:Partida):
        print('---------- GOLS PARTIDA ----------')
        print('---------- *Caso a equipe não tenha feito nenhum gol, por favor digite 0! ----------')
        try:
            gols_equipe_casa = int(input('Gols Equipe Casa: '))
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            return self.__controlador_partidas.abre_tela()
        artilheiros_equipe_casa = []

        for i in range(gols_equipe_casa):
            print(f'Selecione o Artilheiro do {i+1}º gol da Equipe Casa!')
            self.__controlador_partidas.controlador_sistema.controlador_equipes.mostra_alunos_equipe(partida.equipe_casa.codigo)
            matricula_artilheiro_gol = self.__controlador_partidas.controlador_sistema.controlador_alunos.tela_aluno.seleciona_aluno()
            artilheiro_gol = self.__controlador_partidas.controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_artilheiro_gol)
            artilheiros_equipe_casa.append(artilheiro_gol)
        
        try:
            gols_equipe_visitante = int(input('Gols Equipe Visitante: '))
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            return self.__controlador_partidas.abre_tela()
        artilheiros_equipe_visitante = []

        for i in range(gols_equipe_visitante):
            print(f'Selecione o Artilheiro do {i+1}º gol da Equipe Visitante!')
            self.__controlador_partidas.controlador_sistema.controlador_equipes.mostra_alunos_equipe(partida.equipe_visitante.codigo)
            matricula_artilheiro_gol = self.__controlador_partidas.controlador_sistema.controlador_alunos.tela_aluno.seleciona_aluno()
            artilheiro_gol = self.__controlador_partidas.controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_artilheiro_gol)
            artilheiros_equipe_casa.append(artilheiro_gol)
        
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
