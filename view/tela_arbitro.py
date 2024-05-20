from datetime import datetime


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
    
    def pega_dados_arbitro(self, editando=False):
        print('---------- DADOS ÁRBITRO ----------')
        nome = input('Nome: ')
        if not editando:
            cpf = input('CPF: ')
        else:
            cpf = None
        try:
            data_nasc = datetime.strptime(input('Data de Nascimento no formato DD/MM/AAAA: '), "%d/%m/%Y")
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            return self.__controlador_arbitros.abre_tela()
        
        return {'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
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
