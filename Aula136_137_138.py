lista = []
for numero in range(10):
    lista.append(numero)


lista = [
    numero * 2
    for numero in range(10)
]

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.5}
    if produto['preco'] > 10 else
    {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

lista = [
    numero * 2
    for numero in range(10) if numero == 5
]
#antes de for é mapeamento e depois é filtro
print(lista)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)