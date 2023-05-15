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
