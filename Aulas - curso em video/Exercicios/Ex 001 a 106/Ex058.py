# 58 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10.
# Só que agora o jogo vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

numMaq = randint(0, 100)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

cont = 0
numUsu = -1
while numMaq != numUsu:
    numUsu = int(input('Qual é seu palpite? '))
    cont += 1
    if numMaq == numUsu:
        print('!' * 15)
        print('PARABENS!\nVocê conseguiu acertar em {} tentativas!'.format(cont))
        print('!' * 15)
    elif numUsu < numMaq:
        print('Mais... Tente mais uma vez.')
    elif numUsu > numMaq:
        print('Menos... Tente mais uma vez.')


#Versão professor
acertou = False
while not acertou:
    numUsu = int(input('Qual é seu palpite? '))
    cont += 1
    if numMaq == numUsu:
        acertou = True
    else:
        if numUsu < numMaq:
            print('Mais... Tente mais uma vez.')
        elif numUsu > numMaq:
            print('Menos... Tente mais uma vez.')
print('!' * 15)
print('PARABENS!\nVocê conseguiu acertar em {} tentativas!'.format(cont))
print('!' * 15)
