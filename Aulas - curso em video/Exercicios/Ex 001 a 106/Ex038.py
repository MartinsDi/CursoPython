# 38 - Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
