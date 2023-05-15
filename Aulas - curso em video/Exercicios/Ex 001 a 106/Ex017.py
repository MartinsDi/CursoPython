# 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt, hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

hp = (co**2 + ca**2)**(1/2)

print('O comprimento da hipotenusa é {:.2f}.'.format(hp))
print('O comprimento da hipotenusa é {:.2f}.'.format(hypot(co,ca)))
