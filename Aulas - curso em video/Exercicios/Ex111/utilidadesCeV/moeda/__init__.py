def resumo(n, a, d):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(n)}')
    print(f'{"Dobro do preço:":<20}{dobro(n)}')
    print(f'{"Metade do preço:":<20}{metade(n)}')
    print(f'{a:>3}{"% de aumento:":<17}{aumenta(n,a)}')
    print(f'{d:>3}{"% de redução:":<17}{diminui(n,d)}')
    print('-' * 30)

def metade(n=0, form=True):
    num = n / 2
    return num if form is False else moeda(num)


def dobro(n=0, form=True):
    num = n * 2
    return num if form is False else moeda(num)


def aumenta(n=0, taxa =0, form=True):
    num = n + (n * taxa / 100)
    return num if form is False else moeda(num)


def diminui(n=0, taxa=0, form=True):
    num = n - (n * taxa / 100)
    return num if form is False else moeda(num)

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
