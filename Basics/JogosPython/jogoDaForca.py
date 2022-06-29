import random
from signal import pause

def jogar_forca():

    print('***************************')
    print('Bem vindo ao jogo da Forca!')
    print('***************************')

    file = open('forca.txt', 'r')

    palavras = []

    for linha in file:
        linha = linha.strip()
        palavras.append(linha)

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].lower()

    letras_acertadas = ['_' for letra in palavra_secreta]

    tentativas_de_letras = letras_acertadas.__len__()

    enforcado = False

    acertou = False

    chances = palavra_secreta.__len__()

    while(not enforcado and not acertou):

        print('Você tem {} tentativas!'.format(chances))
        
        print(letras_acertadas)
        
        chute = input('Qual letra você deseja chutar: ')
        
        print('***************************')
        
        chute = chute.lower()

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[posicao] = chute
                posicao += 1
                if(''.join(letras_acertadas) == palavra_secreta):
                    print('Parabéns, você ganhou!')
                    print('***************************')
                    print('A palavra secreta era: {}'.format(palavra_secreta).upper())
                    print('***************************')
                    acertou = True
                    break
        else:
            tentativas_de_letras -= 1
            chances -= 1
            if(tentativas_de_letras == 0):
                enforcado = True
                print('***************************')
                print('Você perdeu!')
                print('A palavra secreta era: {}'.format(palavra_secreta).upper())

if(__name__ == '__main__'):
    jogar_forca()