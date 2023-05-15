# 88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo cadastrado tudo em uma lista composta.
from random import randint
from time import sleep
jogos = []
palpite = []
print('-'*30,f'\n{"JOGA NA MEGA SENA":^30}\n','-'*30)
num = int(input('Quantos jogos quer que eu sorteie? '))
print('-='*3,f'SORTEANDO {num} JOGOS','=-'*3)
for i in range(0,num):
    for j in range(0,6):
        while True:
            n = randint(1,60)
            if n not in palpite:
                palpite.append(n)
                break
    palpite.sort()
    jogos.append(palpite.copy())
    palpite.clear()
for c, i in enumerate(jogos):
    print(f'Jogo {c+1}: {i}')
    sleep(0.5)
print('-='*5,'< BOA SORTE! >','=-'*5)