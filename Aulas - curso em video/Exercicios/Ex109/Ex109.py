# 109 - Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por ele vai ser ou não formatado pela função moeda() desenvolvida no DESAFIO 108

from Exercicios.Ex109 import moeda as m

p = float(input('Digite o preço: R$ '))
print(f'A metade de {m.moeda(p)} é {m.metade(p)}')
print(f'O dobro de {m.moeda(p)} é {m.dobro(p)}')
print(f'Aumentando 10%, temos {m.aumenta(p, 10)}')
print(f'Reduzindo 13%, temos {m.diminui(p,13)}')