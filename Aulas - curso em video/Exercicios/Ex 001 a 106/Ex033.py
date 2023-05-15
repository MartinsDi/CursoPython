# 33 - Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor.]

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    if n2 < n3:
        print('{} é o maior e {} é o menor.'.format(n1,n2))
    else:
        print('{} é o maior e {} é o menor.'.format(n1, n3))
elif n2 >n1 and n2 > n3:
    if n1 < n3:
        print('{} é o maior e {} é o menor.'.format(n2, n1))
    else:
        print('{} é o maior e {} é o menor.'.format(n2, n3))
else:
    if n1 < n2:
        print('{} é o maior e {} é o menor.'.format(n3, n1))
    else:
        print('{} é o maior e {} é o menor.'.format(n3, n2))


menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))
