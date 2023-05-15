# 39 -  Faça um programa que leio o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sex = str(input('Digite seu sexo: (M/F) ')).strip().upper()
if sex == 'M':
    ano = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

    if idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        print('Seu alistamento será em {}'.format(atual + saldo))
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE')
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(atual - saldo))
else:
    print('Alistamento não obrigatorio!')