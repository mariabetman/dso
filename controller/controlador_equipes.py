from model.equipe import Equipe
from view.tela_equipe import TelaEquipe
from model.curso import Curso
from model.aluno import Aluno
from DAOs.equipe_dao import EquipeDAO

from exceptions.opcao_invalida_exception import OpcaoInvalidaException
from exceptions.cadastro_duplicado_exception import CadastroDuplicadoException
from exceptions.tipo_invalido_exception import TipoInvalidoException
from exceptions.cadastro_nao_encontrado_exception import CadastroNaoEncontradoException
from exceptions.aluno_de_curso_diferente_da_equipe_exception import AlunoDeCursoDiferenteDaEquipeException
from exceptions.aluno_jah_cadastrado_na_equipe_exception import AlunoJahCadastradoNaEquipeException
from exceptions.aluno_jah_cadastrado_em_outra_equipe_exception import AlunoJahCadastradoEmOutraEquipeException
from exceptions.erro_inesperado import ErroInesperadoException
class ControladorEquipes:
    def __init__(self, controlador_sistema):
        self.__equipe_DAO = EquipeDAO()
        self.__tela_equipe = TelaEquipe(self)
        self.__controlador_sistema = controlador_sistema
    
    @property
    def equipes(self):
        return self.__equipe_DAO.get_all()
    
    @property
    def tela_equipe(self):
        return self.__tela_equipe
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def lista_equipes(self):
        if len(self.__equipe_DAO.get_all()) == 0:
            self.__tela_equipe.mostra_mensagem('Nenhuma Equipe cadastrada!')
        else:
            self.__tela_equipe.mostra_equipes(self.__equipe_DAO.get_all())

    def inclui_equipe(self):
        dados_equipe = self.__tela_equipe.pega_dados_equipe()
        try:
            if isinstance(dados_equipe['codigo_curso'], int) and isinstance(dados_equipe['nome'], str) and isinstance(dados_equipe['codigo'], int):
                curso = self.__controlador_sistema.controlador_cursos.pega_curso_por_codigo(dados_equipe['codigo_curso'])
                if curso:
                    if not self.pega_equipe_por_codigo(dados_equipe['codigo']):
                        equipe = Equipe(curso, dados_equipe['nome'], dados_equipe['codigo'])
                        self.__equipe_DAO.add(equipe)
                        self.__tela_equipe.mostra_mensagem('Equipe cadastrada com sucesso!')
                    else:
                        raise CadastroDuplicadoException('Equipe')
                else:
                    raise CadastroNaoEncontradoException('Curso')
            else:
                raise TipoInvalidoException()
        except (CadastroDuplicadoException, TipoInvalidoException, CadastroDuplicadoException) as e:
            self.__tela_equipe.mostra_mensagem(str(e))

    def altera_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        
        try:
            if equipe:
                novos_dados_equipe = self.__tela_equipe.pega_dados_equipe(editando=True)
                if isinstance(novos_dados_equipe['nome'], str):
                    equipe.nome = novos_dados_equipe['nome']
                self.__equipe_DAO.update(equipe)
                self.__tela_equipe.mostra_mensagem('Equipe editada com sucesso!')
            else:
                raise CadastroNaoEncontradoException('Equipe')
        except CadastroNaoEncontradoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))       
    
    def exclui_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        try:
            if equipe:
                self.__equipe_DAO.remove(codigo_equipe)
                self.__tela_equipe.mostra_mensagem('Equipe excluída com sucesso!')
            else:
                raise CadastroNaoEncontradoException('Equipe')
        except CadastroNaoEncontradoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))
            
    def pega_equipe_por_codigo(self, codigo:int):
        for equipe in self.__equipe_DAO.get_all():
            if equipe.codigo == codigo:
                return equipe
        return None

    def adiciona_aluno_na_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        matricula_aluno = self.__controlador_sistema.controlador_alunos.tela_aluno.seleciona_aluno()
        aluno = self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)
        try:
            if aluno.curso.codigo != equipe.curso.codigo:
                raise AlunoDeCursoDiferenteDaEquipeException()
            else:
                pass
        except AlunoDeCursoDiferenteDaEquipeException as e:
                self.__tela_equipe.mostra_mensagem(str(e))
                return None
        try:
            for _aluno in equipe.alunos:
                if _aluno.matricula == matricula_aluno:
                    raise AlunoJahCadastradoNaEquipeException(codigo_equipe)
        except AlunoJahCadastradoNaEquipeException as e:
                    self.__tela_equipe.mostra_mensagem(str(e))
                    return None
        try:
            for equipe_existente in self.__equipe_DAO.get_all():
                for _aluno in equipe_existente.alunos:
                    if _aluno.matricula == matricula_aluno:
                        raise AlunoJahCadastradoEmOutraEquipeException(equipe_existente.codigo)
        except AlunoJahCadastradoEmOutraEquipeException as e:
                    self.__tela_equipe.mostra_mensagem(str(e))
                    return None
        try:
            if isinstance(equipe, Equipe) and isinstance(aluno, Aluno):
                equipe.adiciona_aluno(aluno)
                self.__tela_equipe.mostra_mensagem('Aluno adicionado com sucesso!')
                self.__equipe_DAO.update(equipe)
            else:
                raise TipoInvalidoException()
        except TipoInvalidoException:
            self.__tela_equipe.mostra_mensagem(str(e))
            return None
            
    def remove_aluno_da_equipe(self):
        codigo_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_codigo(codigo_equipe)
        matricula_aluno = self.__controlador_sistema.controlador_alunos.tela_aluno.seleciona_aluno()
        aluno = self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)

        try:
            if isinstance(equipe, Equipe) and isinstance(aluno, Aluno):
                for _aluno in equipe.alunos:
                    if _aluno.matricula == matricula_aluno:
                        equipe.remove_aluno(aluno)
                        self.__tela_equipe.mostra_mensagem('Aluno removido com sucesso!')
                        self.__equipe_DAO.update(equipe)
                        return aluno
                raise CadastroNaoEncontradoException('Aluno')
            else:
                raise TipoInvalidoException()
        except (CadastroNaoEncontradoException, TipoInvalidoException) as e:
                self.__tela_equipe.mostra_mensagem(str(e))
                return None
    
    def adiciona_pontos_na_equipe(self, equipe:Equipe, pontos:int):
        try:
            if isinstance(equipe, Equipe) and isinstance(pontos, int):
                equipe.adiciona_pontos(pontos)
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('adicionar pontos.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))

    def remove_pontos_da_equipe(self, equipe:Equipe, pontos:int):
        try:
            if isinstance(equipe, Equipe) and isinstance(pontos, int):
                equipe.remove_pontos(pontos)
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('remover pontos.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))

    def zera_pontos_na_equipe(self, equipe:Equipe):
        try:
            if isinstance(equipe, Equipe):
                equipe.zera_pontos()
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('zerar gols sofridos.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))
    
    def adiciona_gols_marcados_na_equipe(self, equipe:Equipe, gols:int):
        try:
            if isinstance(equipe, Equipe) and isinstance(gols, int):
                equipe.adiciona_gols_marcados(gols)
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('adicionar gols marcados.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))

    def remove_gols_marcados_da_equipe(self, equipe:Equipe, gols:int):
        try:
            if isinstance(equipe, Equipe) and isinstance(gols, int):
                equipe.remove_gols_marcados(gols)
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('remover gols marcados.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))
    
    def zera_gols_marcados_na_equipe(self, equipe:Equipe):
        try:
            if isinstance(equipe, Equipe):
                equipe.zera_gols_marcados()
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('zerar gols sofridos.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))
    
    def adiciona_gols_sofridos_na_equipe(self, equipe:Equipe, gols:int):
        try:
            if isinstance(equipe, Equipe) and isinstance(gols, int):
                equipe.adiciona_gols_sofridos(gols)
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('adicionar gols sofridos')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))

    def remove_gols_sofridos_da_equipe(self, equipe:Equipe, gols:int):
        try:
            if isinstance(equipe, Equipe) and isinstance(gols, int):
                equipe.remove_gols_sofridos(gols)
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('remover gols sofridos.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))
    
    def zera_gols_sofridos_na_equipe(self, equipe:Equipe):
        try:
            if isinstance(equipe, Equipe):
                equipe.zera_gols_sofridos()
                self.__equipe_DAO.update(equipe)
            else:
                raise ErroInesperadoException('zerar gols sofridos.')
        except ErroInesperadoException as e:
            self.__tela_equipe.mostra_mensagem(str(e))
            
    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {'1': self.inclui_equipe,
                        '2': self.altera_equipe,
                        '3': self.lista_equipes,
                        '4': self.exclui_equipe,
                        '5': self.adiciona_aluno_na_equipe,
                        '6': self.remove_aluno_da_equipe,
                        '0': self.retorna}
        
        while True:
            try:
                opcao_escolhida = self.__tela_equipe.tela_opcoes()
                if opcao_escolhida in lista_opcoes:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                else:
                    raise OpcaoInvalidaException()
            except OpcaoInvalidaException as e:
                self.__tela_equipe.mostra_mensagem(str(e))