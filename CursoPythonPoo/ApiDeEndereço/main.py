import requests

from acesso_cep import BuscaEndereco

cep = 32900000

objeto_cep = BuscaEndereco(cep)

print(objeto_cep)

# r = requests.get('https://viacep.com.br/ws/{}/json/'.format(objeto_cep))

# print(r.json())
