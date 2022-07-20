from collections import defaultdict

# aparicoes = {
#     'Guilherme': 1,
#     'Pedro': 2,
#     'João': 4,
#     'Maria': 1,
# }

# for elemento in aparicoes.keys():
#     valor = aparicoes[elemento]
#     print(elemento, ' - ', valor)

# for chave, valor in aparicoes.items():
#     print(chave, ' - ', valor)

from email.policy import default
from typing import Counter

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

# meu_texto = meu_texto.lower()

# aparicoes = defaultdict(int)

# for palavra in meu_texto.split():
#     aparicoes[palavra] += 1

# print(aparicoes)

print(Counter(meu_texto.split()))

def analisa_frequencia_de_letras(texto):

    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = ([(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()])
    proporcoes = Counter(dict(proporcoes)).most_common(5)

    for caractere, proporcao in proporcoes:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(meu_texto)
