# 99 - Faça um programa que tenha uma função chama maior(), que recaba vários pâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*num):
    maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in num:
        print(i, end=' ')
        sleep(0.3)
        if i > maior:
            maior = i
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 5, 3, 4, 6, 8, 2, 0)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
