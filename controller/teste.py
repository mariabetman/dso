class CadastroNaoEncontradoException(Exception):
    def __init__(self, classe):
        self.mensagem = "{} não encontrado"
        super().__init__(self.mensagem.format(classe))

lista = [1, 2, 3, 0, 3, 4]


def teste(lista):
    for i in lista:
        try:
            if 1/i:
                print(1/i)
            else:
                raise ZeroDivisionError()
        except ZeroDivisionError as e:
            print(str(e))
            return False

print(teste(lista))


for i in range(10):
    if i % 2 == 0:
        print(i)
    else:
        pass