# 81 - Crie um programa que vai ler vários números e colocar em uma lista. Despois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':break
    if resp == 'N': break
print('-='*30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'Foram digitadas {numeros.count(5)} vezes o valor 5!')
else:
    print('O valor 5 não foi encontrado na lista!')