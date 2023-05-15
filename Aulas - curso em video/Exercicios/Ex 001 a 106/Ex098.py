# 98 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if fim > inicio:
        for i in range(inicio, fim + 1, passo):
            print(f'{i} ', end='',
                  flush=True)  # flush=True está em redundancia em corrigir o sleep, sem flush funciona normalmente
            sleep(0.5)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fin = int(input('Final:  '))
pas = int(input('Passo:  '))
contador(ini, fin, pas)
