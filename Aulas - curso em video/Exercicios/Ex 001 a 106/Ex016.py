# 16 - Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite numero: 6.127
# O numero 6.127 tem a parte inteira 6.
from math import trunc

num = float(input("Digite um numero Real: "))
print("O numero {} tem a parte inteira {}.".format(num, trunc(num)))
print("O numero {} tem a parte inteira {}.".format(num, int(num)))
print("O numero {} tem a parte inteira {:.0f}.".format(num, num//1))
