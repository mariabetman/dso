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
            [psg.Button('Ok', bind_return_key=True)]
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
        if not editando:
            layout = [
                [psg.Text('Preencha os dados do aluno')],
                [psg.Text('Matrícula: ', size=(15,1)),psg.Input(expand_x=True, key='matricula', focus=True)],
                [psg.Text('Código do Curso: ', size=(15,1)),psg.Input(expand_x=True, key='codigo_curso')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome')],
                [psg.Text('CPF: ', size=(15,1)), psg.Input(expand_x=True, key='cpf')],
                [psg.Text('Data de Nascimento (DD/MM/AAAA) ', size=(15,1)), psg.Input(expand_x=True, key='data_nasc')],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar')]
            ]
        else:
            layout = [
                [psg.Text('Preencha os dados do aluno')],
                [psg.Text('Nome: ', size=(15,1)),psg.Input(expand_x=True, key='nome', focus=True)],
                [psg.Text('Data de Nascimento (DD/MM/AAAA) ', size=(15,1)), psg.Input(expand_x=True, key='data_nasc')],
                [psg.Button('Enviar', bind_return_key=True), psg.Button('Cancelar')]
            ]

        window = psg.Window('Formulário Aluno', layout, size=(715,207))
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            self.__controlador_alunos.abre_tela()
            return None
        else:
            if not editando:
                try:
                    matricula = int(values['matricula'])
                except ValueError:
                    window.close()
                    self.mostra_mensagem('\nDigite um valor válido para a matrícula!\n')
                    self.__controlador_alunos.abre_tela()
                    return None
                try:
                    codigo_curso = int(values['codigo_curso'])
                except ValueError:
                    window.close()
                    self.mostra_mensagem('\nDigite um valor válido para o código do curso!\n')
                    self.__controlador_alunos.abre_tela()
                    return None
                cpf = values['cpf']
            else:
                matricula = None
                codigo_curso = None
                cpf = None
            nome = values['nome']
            try:
                data_nasc = datetime.strptime(values['data_nasc'], "%d/%m/%Y")
            except ValueError:
                window.close()
                self.mostra_mensagem('\nDigite um valor válido para a data de nascimento!\n')
                self.__controlador_alunos.abre_tela()
                return None
            
            window.close()
            return {'matricula': matricula, 'codigo_curso': codigo_curso, 'nome': nome, 'cpf': cpf, 'data_nasc': data_nasc}
    
    def mostra_alunos(self, alunos):
        layout = [
            [psg.Text('Alunos cadastrados')],
            [psg.Multiline(default_text='', size=(60, 15), key='LISTA_ALUNOS', disabled=True)],
            [psg.Button('Fechar', bind_return_key=True)]
        ]

        window = psg.Window('Lista de Alunos', layout, finalize=True)

        lista_alunos = ""
        for aluno in alunos:
            lista_alunos += f"Matrícula: {aluno.matricula}\n"
            lista_alunos += f"Curso: {aluno.curso.nome}\n"
            lista_alunos += f"Nome: {aluno.nome}\n"
            lista_alunos += f"CPF: {aluno.cpf}\n"
            lista_alunos += f"Data de Nascimento: {aluno.data_nasc.strftime('%d/%m/%Y')}\n"
            lista_alunos += "-" * 40 + "\n"

        window['LISTA_ALUNOS'].update(lista_alunos)

        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED or event == 'Fechar':
                window.close()
                self.__controlador_alunos.abre_tela()
                return
        
    def seleciona_aluno(self):
        layout = [
            [psg.Text('Digite a matrícula do Aluno que deseja selecionar:')],
            [psg.Input(key='matricula', focus=True)],
            [psg.Button('Ok', bind_return_key=True), psg.Button('Cancelar')]
        ]
        
        window = psg.Window('Seleciona Aluno', layout, finalize=True)
        
        event, values = window.read()

        if event == psg.WIN_CLOSED  or event == 'Cancelar':
            window.close()
            self.__controlador_alunos.abre_tela()
            return None
        else:
            try:
                matricula = int(values['matricula'])
                window.close()
                return matricula
            except:
                self.mostra_mensagem('\nDigite um valor válido!\n')
                window.close()
                self.__controlador_alunos.abre_tela()
                return None
    
    def mostra_mensagem(self, msg):
        psg.popup(msg)
