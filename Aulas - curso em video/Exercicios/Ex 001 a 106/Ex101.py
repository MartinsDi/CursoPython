# 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
# 65 anos opcional

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    frase = f'Com {idade} anos: VOTO '
    if idade < 16:
        frase += 'NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        frase += 'OPCIONAL'
    else:
        frase += 'OBRIGATORIO'
    return frase


print('-'*30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))