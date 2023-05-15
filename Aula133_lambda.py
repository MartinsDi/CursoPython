"""lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista.sort(key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

for item in l2:
    print(item)


def executa(função, *args):
    return função(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


print(
    executa(lambda x, y: x + y, 2, 3)
)

duplica = executa(
    lambda m: lambda n: n * m, 2)

print(duplica(3))

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
#lambda iteravel: função, variaveis(opcional)"""

lista = [1,3,5,7,9,11,13,15,17,19]


conta = list(map(lambda x: x * 10, lista))
print(conta)

for i in conta:
    lista = lambda x: x * 3.3568
    resp = lista(i)
    print(resp)

soma =  lambda x: x + 10
multiplica = lambda x, y: x * y

print(soma(5))