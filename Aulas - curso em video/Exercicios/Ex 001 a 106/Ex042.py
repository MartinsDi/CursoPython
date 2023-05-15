# 42 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais | - Isósceles: dois lados iguais | Escaleno: todos os lados diferentes

print('-='*20)
print("Analisador de trinagulo")
print('-='*20)

n1 = float(input('Primeiro segmento:'))
n2 = float(input('Segunda segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    if n1 == n2 == n3:
        print('Os segmentos acima PODEM FORMAR um Triângulo EQUILÁTERO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Os segmentos acima PODEM FORMAR um Triângulo ISÓSCELES')
    else:
        #n1 != n2 != n3 != n1
        print('Os segmentos acima PODEM FORMAR um Triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo')
