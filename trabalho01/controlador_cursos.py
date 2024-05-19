from curso import Curso
from tela_curso import TelaCurso


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__tela_curso = TelaCurso()
        self.__controlador_sistema = controlador_sistema
        
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def pega_curso_por_codigo(self, codigo:int):
        for curso in self.__cursos:
            if curso.codigo == codigo:
                return curso
        return None
    
    def listar_cursos(self):
        if len(self.__cursos) == 0:
            self.__tela_curso.mostra_mensagem('Nenhum curso cadastrado!')
        else:
            self.__tela_curso.mostra_mensagem('----- CURSOS CADASTRADOS -----')
            for curso in self.__cursos:
                self.__tela_curso.mostra_curso({'codigo': curso.codigo, 'nome': curso.nome})
                
    
    def incluir_curso(self):
        dados_curso = self.__tela_curso.pega_dados_curso()
        curso =  Curso(dados_curso['codigo'], dados_curso['nome'])
        if not self.pega_curso_por_codigo(curso.codigo):
            self.__cursos.append(curso)
            self.__tela_curso.mostra_mensagem('\nCurso cadastrado com sucesso!\n')
        else:
            self.__tela_curso.mostra_mensagem('\nATENÇÃO: Curso já cadastrado!\n')
            
        
    
    def alterar_curso(self):
        self.listar_cursos()
        codigo_curso =  self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo_curso)
        
        if curso:
            novos_dados_curso = self.__tela_curso.pega_dados_curso()
            if isinstance(novos_dados_curso['codigo'], int):
                curso.codigo = novos_dados_curso['codigo']
            if isinstance(novos_dados_curso['nome'], str):
                curso.nome = novos_dados_curso['nome']
            self.listar_cursos()
        else:
            self.__tela_curso.mostra_mensagem('\nATENÇÃO: Curso não encontrado!\n')
    
    def excluir_curso(self):
        self.listar_cursos()
        codigo_curso = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_codigo(codigo_curso)
        
        if curso:
            self.__cursos.remove(curso)
            self.__tela_curso.mostra_mensagem('\nCurso excluído com sucesso!\n')
        else:
            self.__tela_curso.mostra_mensagem('\nATENÇÃO: Curso não encontrado!\n')
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_curso,
                        2: self.alterar_curso,
                        3: self.listar_cursos,
                        4: self.excluir_curso,
                        0: self.retornar}
        
        while True:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()

if __name__ == '__main__':
    ctrl = ControladorCurso(123)
    ctrl.listar_cursos()
    ctrl.incluir_curso()
    ctrl.incluir_curso()
    ctrl.listar_cursos()