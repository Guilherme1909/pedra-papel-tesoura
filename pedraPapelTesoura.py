from random import randint
import time


def menu():
    print('1. Pedra \n2. Papel \n3. Tesoura\n')


def vencedor(jogador, computador):
    if jogador == computador:
        print('Empate!\n')
        return False
    if (jogador == 0 and computador == 1) or (jogador == 2 and computador == 0) or (jogador == 1 and computador == 2):
        print('Computador venceu!')
        return True
    if (jogador == 1 and computador == 0) or (jogador == 0 and computador == 2) or (jogador == 2 and computador == 1):
        print('Você venceu!')
        return True


def main():
    jogadas = ['pedra', 'papel', 'tesoura']

    acabou = False
    while acabou is False:
        menu()
        p1 = int(input('Qual sua escolha? '))
        while p1 < 1 or p1 > 3:
            print('Jogada inválida! Insira um valor correspondente às opções!')
            p1 = int(input('Qual sua escolha? '))

        pc = randint(0, 2)

        print("Pedra, papel ou tesoura...!")
        time.sleep(1.5)
        print(f'{jogadas[p1-1].upper()} x {jogadas[pc].upper()}\n')

        acabou = vencedor(p1-1, pc)


main()
