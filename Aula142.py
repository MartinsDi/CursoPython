# isinstace - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'}
]

for i in lista:
    if isinstance(i, set):
        i.add(5)
        print(i, isinstance(i, set))

    if isinstance(i, str):
        print(i.upper(), isinstance(i ,str))

    if isinstance(i, (int, float)):
        print(i, i*2)