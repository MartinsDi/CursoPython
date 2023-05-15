# 95 - Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

jogadores = list()
jogador = dict()
gols = list()

while True:
    gols.clear()
    jogador.clear()
    tot = 0
    jogador['nome'] = str(input('Nome: '))
    n = int(input('Quantos jogos? '))
    for i in range(0, n):
        gols.append(int(input(f'Quantos gols no jogo {i + 1}? ')))

    jogador['gols'] = gols.copy()
    for i in gols:
        tot += i
    # jogador['total'] = sum(gols)
    jogador['total'] = tot
    jogadores.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resp in "SN": break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N': break
#print('cod ',end='')
#for i in jogador.keys():
#    print(f'{i:<15}',end='')
print('-=' * 30, f'\n{"cod":3} {"nome":<15}{"gols":<15}{"total":6<0}\n', '-' * 40)
for c, i in enumerate(jogadores):
    print(f'{c:>3} {i["nome"]:<15}{str(i["gols"]):<15}{i["total"]:>6}')
    '''print(f'{c:>3}', end='')
    for d in i.values():
        print(f'{str(d):<15}',end='')'''

while True:
    print('-' * 40)
    resp = int(input('Mostrar dado de qual jogador? (-1 para sair)'))
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[resp]["nome"]}:')
    if resp == -1:
        break
    if resp >= 0 and resp < len(jogadores):
        for c, v in enumerate(jogadores[resp]['gols']):
            print(f'   No jogo {c + 1}, fez {v} gols.')
    else:
        print(f'ERRO! não existe jogador com código {resp}! Tente novamente')
print('<<< VOLTE SEMPRE >>>')