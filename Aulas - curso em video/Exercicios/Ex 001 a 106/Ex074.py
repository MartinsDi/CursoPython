# 74 - Crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e tambem indiquei o menor e o maior valor que estão na tupla.
from random import randint

'''n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
menor = maior = n1
lista = (n1, n2, n3, n4, n5)
for i in lista:
    if i < menor:
        menor = i
    if i > maior:
        maior = i
    print(f"{i} → ", end='')
print('FIM')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
# print(f'O maior valor sorteado foi {sorted(lista)[-1]}') metodo sorted elimina a necessidade do for
# print(f'O menor valor sorteado foi {sorted(lista)[0]}')'''

list = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10,), randint(1, 10))
print(f'Eu sorteei os valores {list}')
print(f'O maior valor sorteado foi {sorted(list)[-1]}')
print(f'O maior valor sorteado foi {max(list)}')
print(f'O menor valor sorteado foi {sorted(list)[0]}')
print(f'O menor valor sorteado foi {min(list)}')
