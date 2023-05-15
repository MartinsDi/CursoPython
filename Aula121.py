import copy
pessoa = {
    'nome' : 'Diego',
    'sobrenome' : 'Oliveira',
    'idade' : 28,
    'altura' : 1.83,
    'endereço' : [
        {'rua' : 'tal rua', 'numero': 0},
        {'rua' : 'outra rua', 'numero': 6}
    ]
}


print(pessoa, type(pessoa))
print(pessoa['nome'],pessoa['sobrenome'])

del pessoa['sobrenome']
pessoa['CPF'] = '000.000.000-00'
pessoa['data de nascimento'] = '04/09/1995'

if pessoa.get('sobrenome') is None:
    print('!existe')
else:
    print(pessoa['sobrenome'])


print(pessoa.__len__()) # == len(pessoa)
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)

pessoa.setdefault('telefone', None) # Coloca algum valor como padrão , caso a chave exista vai retornar o valor da chave caso não tenha retorna o valor definido

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2]
}

d2 = copy.deepcopy(d1) #metodo .copy() irá copiar todos os dados imutaveis mas os dados mutaveis serão simplesmente apontados

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)