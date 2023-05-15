# 55 - Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0

for i in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if menor > peso:
            menor = peso

print('O maior peso lido foi {:.2f}Kg \nO menor peso lido {:.2f}Kg'.format(maior,menor))
