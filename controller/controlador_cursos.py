from model.curso import Curso
from view.tela_curso import TelaCurso
from DAOs.curso_dao import CursoDAO


class ControladorCursos:
    def __init__(self, controlador_sistema):
        self.__curso_DAO = CursoDAO()
        self.__tela_curso = TelaCurso(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def cursos(self):
        return self.__curso_DAO.get_all()

    @property
    def tela_curso(self):
        return self.__tela_curso
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def lista_cursos(self):
        if len(self.__curso_DAO.get_all()) == 0:
            self.__tela_curso.mostra_mensagem('Nenhum curso cadastrado!')
        else:
            self.__tela_curso.mostra_mensagem('----- CURSOS CADASTRADOS -----')
            for curso in self.__curso_DAO.get_all():
                self.__tela_curso.mostra_curso({'codigo': curso.codigo, 'nome': curso.nome})
    
    def inclui_curso(self):
        dados_curso = self.__tela_curso.pega_dados_curso()
        if isinstance(dados_curso['codigo'], int) and isinstance(dados_curso['nome'], str):
            if not self.pega_curso_por_codigo(dados_curso['codigo']):
                curso =  Curso(dados_curso['codigo'], dados_curso['nome'])
                self.__curso_DAO.add(curso)
                self.__tela_curso.mostra_mensagem('Curso cadastrado com sucesso!')
            else:
                self.__tela_curso.mostra_mensagem('\nATENÇÃO: Curso já cadastrado!\n')
        else:
            self.__tela_curso.mostra_mensagem('ATENÇÃO: Algo de errado ocorreu durante o cadastro! Tente novamente!')
    
    def altera_curso(self):
        codigo_curso =  self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo_curso)
        
        if curso:
            novos_dados_curso = self.__tela_curso.pega_dados_curso(editando=True)
            if isinstance(novos_dados_curso['nome'], str):
                curso.nome = novos_dados_curso['nome']
            self.__curso_DAO.update(curso)
            self.lista_cursos()
        else:
            self.__tela_curso.mostra_mensagem('ATENÇÃO: Curso não encontrado!')
    
    def exclui_curso(self):
        codigo_curso = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo_curso)
        
        if curso:
            self.__curso_DAO.remove(curso)
            self.__tela_curso.mostra_mensagem('Curso excluído com sucesso!')
        else:
            self.__tela_curso.mostra_mensagem('ATENÇÃO: Curso não encontrado!')
    
    def pega_curso_por_codigo(self, codigo:int):
        for curso in self.__curso_DAO.get_all():
            if curso.codigo == codigo:
                return curso
        return None
    
    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.inclui_curso,
                        '2': self.altera_curso,
                        '3': self.lista_cursos,
                        '4': self.exclui_curso,
                        '0': self.retorna}
        
        while True:
            opcao_escolhida = self.__tela_curso.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_curso.mostra_mensagem('ERRO: Opção inválida!')
