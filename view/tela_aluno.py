import PySimpleGUI as psg
from datetime import datetime


class TelaAluno:
    def __init__(self, controlador_alunos):
        self.__controlador_alunos = controlador_alunos
        
    def tela_opcoes(self):
        layout = [
            [psg.Text('---------- Alunos ----------')],
            [psg.Text('Escolha uma opção')],
            [psg.Text('1 - Incluir Aluno')],
            [psg.Text('2 - Editar Aluno')],
            [psg.Text('3 - Listar Alunos')],
            [psg.Text('4 - Excluir Aluno')],
            [psg.Text('0 - Retornar')],
            [psg.Input(key='OPCAO', size=(10, 1), do_not_clear=False, focus=True)],
            [psg.Button('Confirmar', bind_return_key=True)]
        ]

        window = psg.Window('Tela Aluno', layout)
        event, values = window.read()

        if event == psg.WIN_CLOSED:
            window.close()
            return '0'
        else:
            opcao = values['OPCAO']
            window.close()
            return opcao
    
    def pega_dados_aluno(self, editando=False):
        print('---------- DADOS ALUNO ----------')
        if not editando:
            cpf = input('CPF: ')
            try:
                matricula = int(input('Matrícula: '))
            except:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                self.__controlador_alunos.abre_tela()
            try:
                codigo_curso = int(input('Código do curso: '))
            except:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                self.__controlador_alunos.abre_tela()
        else:
            cpf = None
            matricula = None
            curso = None
        nome = input('Nome do Aluno: ')
        try:
            data_nasc = datetime.strptime(input('Data de Nascimento no formato DD/MM/AAAA: '), "%d/%m/%Y")
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            return self.__controlador_alunos.abre_tela()
        
        return {'matricula': matricula, 'curso': curso, 'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
    def mostra_aluno(self, dados_aluno):
        print('Matrícula do Aluno: ', dados_aluno['matricula'])
        print('Curso: ', dados_aluno['curso'])
        print('Nome: ', dados_aluno['nome'])
        print('CPF: ', dados_aluno['cpf'])
        print('Data de Nascimento: ', dados_aluno['data_nasc'])
        print('-------------------------------------------------------')
        
    def seleciona_aluno(self):
        try:
            matricula = int(input('Digite a matrícula do Aluno que deseja selecionar: '))
            return matricula
        except:
            self.mostra_mensagem('\nDigite um valor válido!\n')
            self.__controlador_alunos.abre_tela()
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)
