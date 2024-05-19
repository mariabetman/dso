class TelaArbitro:
    def tela_opcoes(self):
        print('---------- ÁRBITROS ----------')
        print('Escolha a opção')
        print('1 - Incluir Árbitro')
        print('2 - Editar Árbitro')
        print('3 - Listrar Árbitros')
        print('4 - Excluir Árbitro')
        print('0 - Retornar')
        
        opcao = int(input('\nEscolha sua opção: '))
        return opcao
    
    def pega_dados_arbitro(self):
        print('---------- DADOS ÁRBITRO ----------')
        nome = input('Nome: ')
        cpf = input('CPF: ')
        data_nasc = input('Data de Nascimento: ')
        
        return {'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
    def mostra_arbitro(self, dados_arbitro):
        print('Nome do Árbitro: ', dados_arbitro['nome'])
        print('CPF do Árbitro: ', dados_arbitro['cpf'])
        print('Data de Nascimento do Árbitro: ', dados_arbitro['data_nasc'])
        print()
        
    def seleciona_arbitro(self):
        cpf = input('Digite o CPF do Árbitro que deseja selecionar: ')
        return cpf
    
    def mostra_mensagem(self, msg):
        print(msg)
