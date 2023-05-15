# 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.


num = int(input('Me diga um número qualquer: '))

if num%2 == 0:
    print("O numero {} é PAR!".format(num))
else:
    print('O numero {} é IMPAR!'.format(num))