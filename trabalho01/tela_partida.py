class TelaPartida:
    def __init__(self, controlador_partidas):
        self.__controlador_partidas = controlador_partidas

    def tela_opcoes(self):
        print('---------- PARTIDAS ----------')
        print('1 - Listar Partidas')
        print('2 - Adicionar gols da partida')
        print('0 - Retornar')
        
        opcao = int(input('\nEscolha sua opção: '))
        return opcao
    
    def pega_gols_partida(self):
        print('---------- GOLS PARTIDA ----------')
        print('---------- *Caso a equipe não tenha feito nenhum gol, por favor digite 0! ----------')
        gols_equipe_casa = int(input('Gols Equipe Casa: '))
        gols_equipe_visitante = int(input('Gols Equipe Visitante: '))
        
        return {'gols_equipe_casa': gols_equipe_casa, 'gols_equipe_visitante': gols_equipe_visitante}
    
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
        self.__controlador_partidas.lista_cursos()
        codigo = input('Digite o código da Partida que deseja selecionar: ')
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)
