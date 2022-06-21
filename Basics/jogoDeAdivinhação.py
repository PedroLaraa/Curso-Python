# Jogo De Adivinhação:

print('*********************************')
print('Bem vindo ao jogo da adivinhação!')
print('*********************************')

chances = 3

numero_secreto = 42

while(chances > 0):

    chute_str = input('Digite um número: ')

    chute = int(chute_str)

    acertou = chute == numero_secreto

    maior = chute > numero_secreto

    menor = chute < numero_secreto

    if(acertou):
        print('Você acertou! Parabéns, ganhou o jogo!')
        break
    else:
        if(maior):
            print('Você errou! Seu chute foi maior que o número')
            chances -= 1
            print('Você tem {} chances'.format(chances))
        elif(menor):
            print('Você errou! Seu chute foi menor que o número')
            chances -= 1
            print('Você tem {} chances'.format(chances))
        elif(chances == 0):
            print('Você perdeu!')

# Correção de erros propostos pelo professor:

# minha_idade = 26
# idade_namorado = 25
# if(minha_idade == idade_namorado):
#     print('temos idades iguais')
# else:
#     print('temos idades diferentes')

# numero1 = 10
# numero2 = 10
# if(numero1 == numero2):
#     print("São números iguais")

# O código não funciona devido os tipos de dados diferentes...

# idade1 = 10 Int
# idade2 = "20" Str
# print(idade1 + idade2)

# usuario = input("Informe o usuário do sistema!")

# if(usuario == "Flávio"):
#     print("Seja bem-vindo Flávio!")
# elif(usuario == "Douglas"):
#     print("Seja bem-vindo Douglas!")
# elif(usuario == "Nico"):
#     print("Seja bem-vindo Nico")
# else:
#     print("Usuário não identificado!")