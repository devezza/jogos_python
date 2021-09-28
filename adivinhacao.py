import random

def jogar():
    print('************************************')
    print("Bem vindo ao jogo de Adivinhação!")
    print('************************************')

    numero_secreto = random.randrange(1,100)
    total_tentativas=3
    pontos = 1000

    print("Qual o nível de dificuldade?", numero_secreto)
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input("Defina o nível: "))

    if(nivel==1):
        total_tentativas=20
    elif(nivel==2):
        total_tentativas=10
    else:
        total_tentativas=5

    for rodada in range(1, total_tentativas+1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas))
        chute = input("Digite o seu número entre 1 e 100: ")
        print('Você digitou ', chute)
        chute = int(chute)

        if(chute<1 or chute>100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute
        maior   = chute>numero_secreto


        if(acertou):
            print('Você acertou!')
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o número secreto')
            else:
                print('Você errou! O seu chute foi menor que o número secreto')
        pontos_perdidos = abs(numero_secreto-chute)
        pontos = pontos-pontos_perdidos
        print('_______________________________________________________')
    print(numero_secreto)
    print("Você fez ", pontos,"pontos")

if(__name__ =="__main__"):
    jogar()
