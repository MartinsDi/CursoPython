# 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

lista = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o último numero: ')))
# lista = (n1, n2, n3, n4)
print(f'Você digitou os valores {lista}')
num9 = lista.count(9)
print(f'O valor 9 pareceu {num9} vezes')

num3 = 0
for i in lista:
    if i == 3:
        num3 = lista.index(3)
if num3 <= 0:
    print('O valor 3 não foi digitado em nunhuma posição.')
else:
    print(f'O valor 3 pareceu na {num3 + 1}ª posição')

'''if 3 in lista: #Essas 4 linhas substitui da linha 15 a 22
    print(f'O valor 3 pareceu na {num3 + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nunhuma posição.')'''

numP = 0
for i in lista:
    if i % 2 == 0:
        if numP == 0:
            print('Os valores pares digitados foram: ', end='')
        print(f'{i} ', end='')
        numP += 1
if numP == 0:
    print('Não foi digitado nenhum número par')
