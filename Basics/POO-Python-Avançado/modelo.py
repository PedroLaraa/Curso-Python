
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def dados_do_programa(self):
        return f'Nome: {self._nome} | Ano: {self._ano} | Likes: {self._likes}'

    @property
    def likes(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self._ano} | Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = str(duracao) + ' minutos'
    
    def imprime(self):
        print(f'Nome: {self._nome} | Ano: {self._ano} | Duração: {self._duracao} | Likes: {self._likes}')

class Serie(Programa): 
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = str(temporadas) + ' temporadas'

    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self._ano} | Temporadas: {self._temporadas} | Likes: {self._likes}'

class Playlist:

    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    @property
    def listagem_da_playlist(self):
        return self._programas

    @property
    def tamanho_da_playlist(self):
        return len(self._programas)

# CRIAÇÃO DOS OBJETOS:

vingadores = Filme('vingadores - guerra infinita', 2018, 160)

strangerThings = Serie('stranger things', 2016, 4)

tmep = Filme('todo mundo em panico', 2001, 100)

demolidor = Serie('demolidor', 2016, 3)

# MANIPULAÇÃO DOS OBJETOS (LIKES):

strangerThings.likes
strangerThings.likes

vingadores.likes
vingadores.likes
vingadores.likes

tmep.likes

demolidor.likes
demolidor.likes
demolidor.likes

# EXIBIÇÃO DOS OBJETOS:

# vingadores.dados_do_programa

# strangerThings.dados_do_programa

# ALTERAÇÃO DOS OBJETOS:

# strangerThings.dados_do_programa = ['vingadores - guerra infinita', '2011', '1']

# strangerThings.dados_do_programa

# ARMAZENAMENTO DOS OBJETOS:

filmes_e_series = [vingadores, strangerThings, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.listage:
    print(programa)

