# 59 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar / [2] multiplicar / [3] maior / [4] novos números / [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
op = 0
while op !=5:
    print("=-=" * 10)
    print('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        soma = n1 +n2
        print('O resultado de  {:.0f} + {:.0f} é {:.0f}.'.format(n1,n2,soma))
    elif op == 2:
        mult = n1*n2
        print('O resultado de {:.0f} x {:.0f} é {:.0f}.'.format(n1,n2,mult))
    elif op == 3:
        if n1 > n2:
            print('{:.0f} é maior que {:.0f}.'.format(n1,n2))
        elif n1 < n2:
            print("{:.0f} é maior que {:.0f}".format(n2, n1))
        else:
            print('Não tem maior os dois numeros são iguais!')
    elif op == 4:
        n1 = float(input('Redigite o primeiro numero: '))
        n2 = float(input('Redigite o segundo numero: '))
    elif op == 5:
        print('Finalizando programa...')
        sleep(0.5)
    else:
        print('Opção inválida. Tente novamente')
    sleep(0.5)

print('Fim do programa! Volte sempre!')