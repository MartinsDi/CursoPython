''''pessoa = []
pessoas = [['Maria',25]]

pessoa.append('Victor')
pessoa.append(25)
pessoas.append(pessoa.copy())
pessoa.clear()
pessoa.append('Diego')
pessoa.append(25)
pessoas.append(pessoa.copy())


print(pessoas)'''
#teste = list()
galera = list()
dado = list()

'''teste.append('Gustavo')
teste.append(40)

galera.append(teste.copy())

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste.copy())
print(galera)'''
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado.copy())
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')