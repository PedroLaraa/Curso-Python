
class Filme: 

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = str(duracao) + ' minutos'
        self.__likes = 0

    @property
    def dados_do_filme(self):
        print(f'Nome: {self.__nome} | Ano: {self.__ano} | Duração: {self.__duracao} | Likes: {self.__likes}')

    @property
    def likes(self):
        self.__likes += 1

class Serie: 

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = str(temporadas) + ' temporadas'
        self.__likes = 0

    @property
    def dados_da_serie(self):
        print(f'Nome: {self.__nome} | Ano: {self.__ano} | Duração: {self.__temporadas} | Likes: {self.__likes}')

    @dados_da_serie.setter
    def dados_da_serie(self, values):
        self.__nome = values[0].title()
        self.__ano = values[1]
        self.__temporadas = str(values[2]) + ' temporadas'
        self.__likes = self.__likes

    @property
    def likes(self):
        self.__likes += 1

# CRIAÇÃO DOS OBJETOS:

vingadores = Filme('vingadores - guerra infinita', 2018, 160)

strangerThings = Serie('stranger things', 2016, 4)

# MANIPULAÇÃO DOS OBJETOS (LIKES):

strangerThings.likes
strangerThings.likes

vingadores.likes
vingadores.likes
vingadores.likes

# EXIBIÇÃO DOS OBJETOS:

vingadores.dados_do_filme

strangerThings.dados_da_serie

# ALTERAÇÃO DOS OBJETOS:

strangerThings.dados_da_serie = ['vingadores - guerra infinita', '2011', '1']

strangerThings.dados_da_serie