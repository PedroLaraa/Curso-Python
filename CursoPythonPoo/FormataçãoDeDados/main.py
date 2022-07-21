from telefonesBr import TelefonesBr

# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"

# email = 'fasfas pedroalveslara@gmail.com.br'

# resposta = re.search(padrao, email)

# print(resposta.group())

# padrao_molde = "(xx)aaaa-wwww"

# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

# texto = 'testando 31992842024 e também este 3192489924'

# resposta_todos_resultados = re.findall(padrao, texto)
# print(resposta_todos_resultados)

# resposta_unica = re.search(padrao, texto)
# print(resposta_unica.group())

telefone = '5531992842024'

telefone_objeto = TelefonesBr(telefone)

print(telefone_objeto)