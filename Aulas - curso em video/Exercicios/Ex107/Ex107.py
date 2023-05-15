# 107 - Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções
from Exercicios.Ex107 import moeda as m

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é R${m.metade(p)}')
print(f'O dobro de {p} é R${m.dobro(p)}')
print(f'Aumentando 10%, temos R${m.aumenta(p, 10)}')
print(f'Reduzindo 13%, temos R${m.diminui(p,13)}')


