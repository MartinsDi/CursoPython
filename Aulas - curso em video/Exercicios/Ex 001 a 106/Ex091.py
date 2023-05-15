# 91 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter # professor
jogo = dict()
jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)
'''jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)
        }'''
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
print('-=' * 20)
print('   ==RANKING DOS JOGADORES ==')
for n, i in enumerate(sorted(jogo, key=jogo.get, reverse=True)):
    print(f'    {n + 1}º lugar: {i} com {jogo[i]}.')
    sleep(0.5)
#versão professor
print('-'*50)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #itemgetter se colocasse 0 iria selecionar os nome
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)