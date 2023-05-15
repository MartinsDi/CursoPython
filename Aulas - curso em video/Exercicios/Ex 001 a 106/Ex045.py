# 45 - Crie um programa que faça o computador jogar Jokenpô com você

from random import choice , randint
from time import sleep


list = ('PEDRA', 'PAPEL', 'TESOURA')
print('-='*20)
print('\033[33mVAMOS JOGAR JOKENPÔ\033[m')
print('-='*20)

print('Suas opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\n')
escolha = int(input('Qual é a sua jogada? '))

computador = randint(0, 2)
maquina = choice(list)
usuario = list[escolha]

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-='*15)
print('COMPUTADOR ESCOLHEU {}\nVOCE ESCOLHEU {}'.format(list[computador],list[escolha]))
print('-='*15)


'''if maquina == usuario:
    print("EMPATE")
elif usuario == 'pedra':
    if maquina == 'papel':
        print('Você perdeu')
    else:
        print('Parabens! Você ganhou')
elif usuario == 'papel':
    if maquina == 'tesoura':
        print('Você perdeu')
    else:
        print('Parabens! Você ganhou')
else:
    if maquina == 'pedra':
        print('Você perdeu')
    else:
        print('Parabens! Você ganhou')'''

if computador == escolha:
    print('EMPATE')
else:
    if computador == 0:
        if escolha == 1:
            print('JOGADOR VENCE')
        elif escolha == 2:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')
    elif computador == 1:
        if escolha == 0:
            print('COMPUTADOR VENCE')
        elif escolha == 2:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')
    elif computador == 2:
        if escolha == 0:
            print('JOGADOR VENCE')
        elif escolha == 1:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')


