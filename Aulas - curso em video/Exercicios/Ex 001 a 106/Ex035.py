# 35 - Desenvolva um programa que leia o comprimento de tres restas e diga ao usuario se elas podem ou não formar um triangulo
print('-='*20)
print("Analisador de trinagulo")
print('-='*20)

n1 = float(input('Primeiro segmento:'))
n2 = float(input('Segunda segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    if n1 == n2 == n3:
        print('Os segmentos acima PODEM FORMAR um Triângulo Equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Os segmentos acima PODEM FORMAR um Triângulo Isósceles')
    else:
        print('Os segmentos acima PODEM FORMAR um Triângulo Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo')
