# 108 - Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado
from Exercicios.Ex108 import moeda as m

p = float(input('Digite o preço: R$ '))
print(f'A metade de {m.moeda(p)} é {m.moeda(m.metade(p))}')
print(f'O dobro de {m.moeda(p)} é {m.moeda(m.dobro(p))}')
print(f'Aumentando 10%, temos {m.moeda(m.aumenta(p, 10))}')
print(f'Reduzindo 13%, temos {m.moeda(m.diminui(p,13))}')