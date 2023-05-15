# 79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente.

numero = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numero:
        numero.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while True:
        resp = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*30)
numero.sort()
print(f'Você digitou os valores {numero}')