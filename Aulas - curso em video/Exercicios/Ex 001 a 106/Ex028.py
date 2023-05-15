# 28 - Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 peça para o usuário tentar descobbrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o úsuarui venceu ou perdeu.

from random import randint
from time import sleep

numMaq = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
numUsu = int(input('Em que número eu pensei? '))
print('\nPROCESSANDO...\n')
sleep(2)

if numMaq == numUsu:
    print('\n!' * 15)
    print('PARABENS!\nVocê Conseguiu me vencer!')
    print('!' * 15)
else:
    print('Você perdeu!\nEu pensei no numero {} e não no {}!\nNão foi dessa vez'.format(numMaq, numUsu))
