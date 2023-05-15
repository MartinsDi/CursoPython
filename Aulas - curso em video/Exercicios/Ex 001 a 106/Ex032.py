# 32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano // 1 % 100 == 0 and ano % 400 != 0:
        print('{} não é ano BISSEXTO'.format(ano))
    else:
        print('{} é ano BISSEXTO'.format(ano))

else:
    print('{} não é ano BISSEXTO'.format(ano))

'''if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    print('{} não é ano BISSEXTO'.format(ano))
else:
    print('{} é ano BISSEXTO'.format(ano))'''
#versão do professor