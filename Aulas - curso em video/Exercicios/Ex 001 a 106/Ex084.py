# 84 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pessadas.
# C) Uma listagem com as pessoas mais leves.
lista = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')).strip().title())
    pessoa.append(float(input('Peso: ')))
    if maior == 0 or pessoa[1] > maior:
        maior = pessoa[1]
    if menor == 0 or pessoa[1] < menor:
        menor = pessoa[1]
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=' * 30)

print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O maior peso é {maior:.2f}Kg. Peso de ', end='')
for i in lista:
    if i[1] == maior:
        print(f'{i[0]}...', end='')

print(f'\nO menor peso é {menor:.2f}Kg. Peso de ', end='')
for i in lista:
    if i[1] == menor:
        print(f'{i[0]}...', end='')
