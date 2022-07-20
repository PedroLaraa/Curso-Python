import re

# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"

# email = 'fasfas pedroalveslara@gmail.com.br'

# resposta = re.search(padrao, email)

# print(resposta.group())

padrao_molde = "(xx)aaaa-wwww"

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

texto = 'testando 31992842024 e também este 3192489924'

resposta = re.findall(padrao, texto)

print(resposta)
