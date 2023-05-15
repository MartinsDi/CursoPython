# 93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. o programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será quardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
tot = 0
jogador['nome'] = str(input('Nome: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, n):
    gols.append(int(input(f'Quantos gols no jogo {i}? ')))
jogador['gols'] = gols

#jogador['total'] = sum(gols)
for i in gols:
    tot += i
jogador['total'] = tot
print('-=' * 40)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')

for c, v in enumerate(jogador['gols']):
    print(f'   → Na partida {c}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
