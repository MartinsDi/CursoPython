# 18 - Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo


import math

Ang = float(input("Digite um angulo qualquer: "))
Rad = math.radians(Ang)
print("O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}".format(Ang, math.sin(Rad), Ang, math.cos(Rad), Ang, math.tan(Rad)))









