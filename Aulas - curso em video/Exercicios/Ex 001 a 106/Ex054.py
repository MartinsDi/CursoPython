# 54 - Crie um programa que leia o ano de nascinemtno de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
anoAt = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    anoNasc = int(input('Em que ano a {}ª nasceu: '.format(i)))
    idade = anoAt - anoNasc
    if  idade < 18:
        menor += 1
    else:
        maior += 1

#print('{} pessoas ainda não atingiram a maioridade e {} já são maiores'.format(menor,maior))
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
