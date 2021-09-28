import forca
import adivinhacao

def escolhe_jogos():
    print('************************************')
    print("Escolhe o seu jogo!")
    print('************************************')

    print('(1)Forca (2)Adivinhação')
    jogo = int(input('Qual jogo?'))

    if(jogo==1):
        print('Jogo da forca!')
        forca.jogar()
    elif(jogo==2):
        print('Jogo de advinhação')
        adivinhacao.jogar()
    else:
        print('Opção invalida')

if(__name__ == "__main__"):
    escolhe_jogos()