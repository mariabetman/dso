from model.curso import Curso
from view.tela_curso import TelaCurso
from DAOs.curso_dao import CursoDAO

from exceptions.opcao_invalida_exception import OpcaoInvalidaException
from exceptions.cadastro_duplicado_exception import CadastroDuplicadoException
from exceptions.tipo_invalido_exception import TipoInvalidoException
from exceptions.cadastro_nao_encontrado_exception import CadastroNaoEncontradoException

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
        try:
            if isinstance(dados_curso['codigo'], int) and isinstance(dados_curso['nome'], str):
                if not self.pega_curso_por_codigo(dados_curso['codigo']):
                    curso =  Curso(dados_curso['codigo'], dados_curso['nome'])
                    self.__curso_DAO.add(curso)
                    self.__tela_curso.mostra_mensagem('Curso cadastrado com sucesso!')
                else:
                    raise CadastroDuplicadoException('Curso')       
            else:
                raise TipoInvalidoException()
        except (CadastroDuplicadoException, TipoInvalidoException) as e:
            self.__tela_curso.mostra_mensagem(str(e))
    
    def altera_curso(self):
        codigo_curso =  self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo_curso)
        try:
            if curso:
                novos_dados_curso = self.__tela_curso.pega_dados_curso(editando=True)
                if isinstance(novos_dados_curso['nome'], str):
                    curso.nome = novos_dados_curso['nome']
                self.__curso_DAO.update(curso)
                self.lista_cursos()
            else:
                raise CadastroNaoEncontradoException('Curso')
        except CadastroNaoEncontradoException as e:
            self.__tela_curso.mostra_mensagem(str(e))
    
    def exclui_curso(self):
        codigo_curso = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo_curso)
        try:
            if curso:
                self.__curso_DAO.remove(curso)
                self.__tela_curso.mostra_mensagem('Curso excluído com sucesso!')
            else:
                raise CadastroNaoEncontradoException('Curso')
        except CadastroNaoEncontradoException as e:
            self.__tela_curso.mostra_mensagem(str(e))
    
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
            try:
                opcao_escolhida = self.__tela_curso.tela_opcoes()
                if opcao_escolhida in lista_opcoes:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                else:
                    raise OpcaoInvalidaException()
            except OpcaoInvalidaException as e:
                self.__tela_curso.mostra_mensagem(str(e))