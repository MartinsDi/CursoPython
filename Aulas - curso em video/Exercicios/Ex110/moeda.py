def resumo(n=0, a=10, d=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":<20}\t{moeda(n)}')
    print(f'{"Dobro do preço:":<20}\t{dobro(n)}')
    print(f'{"Metade do preço:":<20}\t{metade(n)}')
    print(f'{a:<3}{"% de aumento:":<17}\t{aumenta(n, a)}')
    print(f'{d:<3}{"% de redução:":<17}\t{diminui(n, d)}')
    print('-' * 30)


def metade(n=0, form=True):
    num = n / 2
    return num if form is False else moeda(num)


def dobro(n=0, form=True):
    num = n * 2
    return num if form is False else moeda(num)


def aumenta(n=0, taxa=0, form=True):
    num = n + (n * taxa / 100)
    return num if form is False else moeda(num)


def diminui(n=0, taxa=0, form=True):
    num = n - (n * taxa / 100)
    return num if form is False else moeda(num)


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
