def metade(n=0):
    num = n / 2
    return num


def dobro(n=0):
    num = n * 2
    return num


def aumenta(n=0, taxa=0):
    num = n + (n * taxa / 100)
    return num


def diminui(n=0, taxa=0):
    num = n - (n * taxa / 100)
    return num


'''def moeda(n):
    return f'R${n:.2f}'''


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
