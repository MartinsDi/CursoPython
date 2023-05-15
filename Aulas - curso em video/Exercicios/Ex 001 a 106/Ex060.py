# 60 - faça um que leia um numero qualquer e mostre o seu fatorial.
# Ex: 5! = 5*4*3*2*1 = 120
from math import factorial

fat = int(input('Digite um numero para fatorar: '))
cont = 1
while fat > 0:
    print("{} * ".format(fat), end="")
    cont *= fat
    fat-=1
print('\b\b = ',cont)

#versão professor
fat = int(input('Digite um numero para fatorar: '))
cont = fat
f = 1
print('Calculando {}! = '.format(fat),end='')
while cont > 0:
    print('{}'.format(cont),end='')
    print(' x ' if cont > 1 else ' = ',end='')
    f*= cont
    cont -= 1
print('{}'.format(f))