# 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos

soma = 0
media = 0
nomevelho = ""
idadevelho = 0
qtdN = 0

for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    op=str(input('Sexo (M/F): ')).strip().upper()
    soma+=idade
    if op == 'F':
        if idade < 20:
            qtdN += 1
    elif op == 'M':
        if idade > idadevelho:
            idadevelho = idade
            nomevelho = nome
    else:
        print('Opção de sexo invalida')


media = soma/4
print('A media de idade do grupo é de {} anos'.format(media))
print('O homem mais velho se chama {} tem {} anos'.format(nomevelho,idadevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(qtdN))
