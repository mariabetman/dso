class TelaSistema:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        print('---------- MENU PRINCIPAL ----------')
        print('*Apenas inicie o Campeonato após criar as Equipes que irão participar!!!')
        print('Escolha a opção')
        print('1 - Menu de Cursos')
        print('2 - Menu de Alunos')
        print('3 - Menu de Equipes')
        print('4 - Menu de Árbitros')
        print('5 - Iniciar Campeonato')
        print('6 - Finalizar Campeonato')
        print('0 - Encerrar Programa')

        opcao = int(input('\nEscolha sua opção: '))
        return opcao
        
    def mostra_mensagem(self, msg):
        print(msg)
