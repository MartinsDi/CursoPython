# 52 - Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo

numPri = int(input('Digite um número: '))
'''primo = True
for i in range(2,numPri):
    if numPri % i == 0:
        primo = False
if primo:
    print('É um numero primo')
else:
    print('Não é um numero primo')'''
tot = 0
for i in range(1,numPri+1):
    if numPri % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i),end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(numPri,tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('É por isso ele NÃO É PRIMO')
