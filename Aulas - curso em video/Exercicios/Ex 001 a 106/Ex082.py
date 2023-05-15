# 82 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final mostre o conteúdo das três listas geradads

par = impar = False

numeros = list()

while True:
    numeros.append(int(input('Digite um numero: ')))
    while True:
        resp = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':break
    if resp == 'N': break

for i in numeros:
    if i % 2 == 0:
        par = True
    if i % 2 == 1:
        impar = True
print('-='*30)
print(f'Os valores digitados são {numeros}')
numeros.sort()
if par:
    par = list()
    for i in numeros:
        if i % 2 == 0:
            par.append(i)
    print(f'A lista de valores pares são {par}')
else:
    print('Não foi digitado nenhum número par.')
if impar:
    impar = list()
    for i in numeros:
        if i % 2 == 1:
            impar.append(i)
    print(f'A lista de valores ímpares são {impar}')
else:
    print('Não foi digitado nenhum número ímpar')