# 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
def ficha(nome='<desconhecido>', gols=0):#Versão do professor
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


def ficha(nome='<desconhecido>', gols=0):
    if nome != str:
        nome = '<desconhecido>'
    if gols != int:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('-' * 30)
n = str(input('Nome do jogador: '))
g = input('Número de Gols: ')
print(ficha(n, g))

#Versão do professor
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)