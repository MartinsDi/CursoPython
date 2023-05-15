# 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final. mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# maior e menor podem ter mais de um
numero = list()
for i in range(0, 5):
    numero.append(int(input(f'Digite um valor para a posição {i}: ')))
menor = maior = 0
for i in numero:
    if maior == 0 or maior < i:
        maior = i
    if menor == 0 or menor > i:
        menor = i
print('=-'*30)
print(f'Você digitou os valores {numero}')

print(f'O maior numero é {maior} e foi encontrado nas posições ', end='')
for c, i in enumerate(numero):
    if i == maior:
        print(f"{c}...", end='')

print(f'\nO menor numero é {menor} e foi encontrado nas posições ', end='')
for c, i in enumerate(numero):
    if i == menor:
        print(f"{c}...", end='')
