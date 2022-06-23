def jogar_forca():

    print('***************************')
    print('Bem vindo ao jogo da Forca!')
    print('***************************')

    palavra_secreta = 'banana'

    letras_acertadas = ['_']*len(palavra_secreta)

    enforcado = False

    acertou = False

    tentativas_de_letras = letras_acertadas.__len__()

    while(not enforcado and not acertou):
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
            if(tentativas_de_letras == 0):
                enforcado = True
                print('***************************')
                print('Você perdeu!')
                print('A palavra secreta era: {}'.format(palavra_secreta))

if(__name__ == '__main__'):
    jogar_forca()