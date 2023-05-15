# 94 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média

pessoa = dict()
pessoas = list()
media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        s = str(input('Sexo: (M/F) ')).strip().upper()[0]
        if s in 'MF':
            pessoa['sexo'] = s
            break
        print('ERRO! por favor, digite apenas M ou F.')
    while True:
        i = int(input('Idade: '))
        if int == type(i):
            pessoa['idade'] = i
            media += i
            break
        print('Opção invalida')
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? (S/N)')).strip().upper()[0]
        if resp in 'SN':break
        print('ERRO! Resposta invalida, só S ou N ')
    if resp == 'N':
        break
print('-='*40)
print(f'- O grupo tem {len(pessoas)} pessoas.')
#for i in pessoas:
 #   media += i['idade']
media = media / len(pessoas)
print(f'- A média de idade é de {media:5.2f} anos.')

print('- As mulheres cadastradas foram: ',end='')
for f in pessoas:
    if f['sexo'] == 'F':
        print(f'{f["nome"]}... ',end='')
print('\nLista das pessoas que estão acima da média: \n')
for i in pessoas:
    if i['idade']>= media:
        for k, v in i.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<< ENCERRADO >>>')