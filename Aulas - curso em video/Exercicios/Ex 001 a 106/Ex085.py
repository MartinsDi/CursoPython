# 85 - Crie um programa onde o usúario possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e ímpares em ordem crescente.
Lista = [[],[]]

for i in range(1,8):
    num = int(input(f'Digite o {i}º numero: '))
    if num % 2 == 0:
        Lista[0].append(num)
    else:
        Lista[1].append(num)
Lista[0].sort()
Lista[1].sort()
print(f'Os valores pares em ordem crescente são: {Lista[0]}')
print(f'Os numeros ímpares em ordem crescente são: {Lista[1]}')