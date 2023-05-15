# 69 - Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pessoaMaior = homens = muMenor = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    while True:
        idade = int(input('Idade: '))
        if  type(idade) == int: break
    while True:
        sexo = str(input('Sexo: (M/F) ')).strip().upper()[0]
        if sexo in 'MF': break
    print('-' * 20)
    if idade >= 18:
        pessoaMaior +=1
    if sexo == 'M':
        homens += 1
    #if sexo == 'F' and idade < 20:
        #muMenor += 1
    else:
        if idade < 20:
            muMenor += 1
    while True:
        resp = str(input('Que continuar? (S/N)')).strip().upper()[0]
        if  resp in 'SN': break
    if resp == 'N': break
print(f'{"FIM DO PROGRAMA":=^40}')

print(f'Total de pessoas com mais de 18 anos: {pessoaMaior} ')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {muMenor} mulheres com menos de 20 anos.')