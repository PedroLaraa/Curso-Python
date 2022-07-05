
import re

endereco = 'Rua osório da Silva Couto, número 296, padre eustáquio, Igarapé, MG, 32900-000'

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(f'CEP: {cep}')
