# Jogo De Adivinhação:

import random

def jogar_adivinhacao():

    print('*********************************')
    print('Bem vindo ao jogo da adivinhação!')
    print('*********************************')

    print('(1) Fácil | (2) Médio | (3) Difícil' )

    chances = 0

    pontos = 10

    dificuldade = int(input('Nível de dificuldade: '))

    if(dificuldade == 1):
        chances = 5
    elif(dificuldade == 2):
        chances = 3
    elif(dificuldade == 3):
        chances = 1
    else:
        print('Digite uma opção válida!')
        dificuldade = int(input('Nível de dificuldade: '))

    numero_secreto = int(random.randrange(1, 11)) # Gera um número entre 1 e 10

    for rodada in range(1, chances + 1):

        chute_str = input('Digite um número entre 0 e 10: ')

        chute = int(chute_str)

        acertou = chute == numero_secreto

        maior = chute > numero_secreto

        menor = chute < numero_secreto

        pontos_perdidos = chances

        if(acertou):
            print('Você acertou! Parabéns, ganhou o jogo!')
            print('Total de pontos: {}'.format(pontos))
            print('*********************************')
            break
        else:
            if(chances == 1):
                print('Você perdeu! O número era: {}'.format(numero_secreto))
                print('*********************************')
                break
            elif(menor):
                print('Você errou! Seu chute foi menor que o número')
                pontos = pontos - pontos_perdidos
                chances -= 1
                print('Você tem {} chances'.format(chances))
                print('*********************************')
            elif(maior):
                print('Você errou! Seu chute foi maior que o número')
                pontos = pontos - pontos_perdidos
                chances -= 1
                print('Você tem {} chances'.format(chances))
                print('*********************************')

if(__name__ == '__main__'):
    jogar_adivinhacao()

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