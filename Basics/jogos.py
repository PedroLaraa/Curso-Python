
import jogoDaForca
import jogoDeAdivinhação

print('*******************')
print('Escolha o seu jogo!')
print('*******************')

print('(1) Jogo da Forca | (2) Jogo da Adivinhação')

jogo = int(input('Qual jogo você deseja jogar: '))

if(jogo == 1):
    jogoDaForca.jogar_forca()
elif(jogo == 2):
    jogoDeAdivinhação.jogar_adivinhacao()
else:
    print('Digite uma opção válida!')
    print('************************')
    jogo = int(input('Qual jogo você deseja jogar: '))
