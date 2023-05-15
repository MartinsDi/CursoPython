# 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia(list):
    print('Sorteando 5 valores da lista: ',end='')
    for i in range(0,5):
        num = randint(1,10)
        print(num,end=' ')
        list.append(num)
        sleep(0.5)
    print('PRONTO!')
    somaPar(list)


def somaPar(list):
    soma = 0
    for i in list:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {list}, temos {soma}')


números = list()
sorteia(números)
print(números)
