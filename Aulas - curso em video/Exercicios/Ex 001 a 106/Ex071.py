# 71 - Crie um programa que simule o funcionamenteo de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print("=" * 40)
print(f'{"MANNY INTERNATIONAL BANK":^40}')
print("=" * 40)
#c50 = c20 = c10 = c1 = 0
num = int(input('Que valor você quer sacar? R$'))
'''while True:
    while True:
        if num - 50 >= 0:
            c50 += 1
            num -= 50
        else:
            break
    while True:
        if num - 20 >= 0:
            c20 += 1
            num -= 20
        else:
            break
    while True:
        if num - 10 >= 0:
            c10 += 1
            num -= 10
        else:
            break
    while True:
        if num - 1 >= 0:
            c1 += 1
            num -= 1
        else:
            break
    break'''
'''c50 = num // 50
num %= 50
c20 = num // 20
num %= 20
c10 = num // 10
c1 = num % 10'''

'''
print(f'Total de {c50} cédulas de R$50' if c50 > 0 else "\b")
print(f'Total de {c20} cédulas de R$20'if c20 > 0 else "\b")
print(f'Total de {c10} cédulas de R$10'if c10 > 0 else "\b")
print(f'Total de {c1} cédulas de R$1'if c1 > 0 else "\b")
print('='*40)
print('Volte sempre ao MANNY INTERNATIONAL BANK! Tenha um bom dia!')'''
total = num
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.0f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*40)
print('Volte sempre ao MANNY INTERNATIONAL BANK! Tenha um bom dia!')