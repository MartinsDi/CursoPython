# 73 - Crie uma tupla ppreenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de futebol, na ordem de colocação. depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabeça está o time da Chapecoense.
nfl = ('Rams', 'Bengals', 'Chiefs', '49ers', 'Packers', 'Buccaneers', 'Titans', 'Bills', 'Cowboys', 'Cardinals', 'Raiders',
'Patriots', 'Steelers', 'Eagles', 'Saints', 'Chargers', 'Colts', 'Dolphins', 'Ravens', 'Browns', 'Vikings',
'Commanders', 'Seahawks', 'Broncos', 'Falcons', 'Bears', 'Panthers', 'Giants', 'Jets', 'Texans', 'lions', 'Jaguars')
count = 0
print('-'*52)
print(f'{"Lista de Times da NFL":^52}')
print('-'*52)
for i in nfl:
    print(f'{i:^10} - ', end='')
    count += 1
    if count == 4:
        print('\b\b')
        count = 0
print('-'*52)
print(f'Os 5 primeiros são {nfl[0:5]}')
print('-'*52)
print(f'Os 4 ultimos são {nfl[-4:]}')
print('-'*52)
print(f'Os times em ordem alfabética: {sorted(nfl)}')
print('-'*52)
print(f'Os Cardinals estão na {nfl.index("Cardinals")+1}ª posição')