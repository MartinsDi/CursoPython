# 92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date, datetime
datetime.now().year
date.today().year
anoAt = date.today().year
trab = dict()
trab['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
trab['idade'] = anoAt - nascimento
trab['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trab['CTPS'] != 0:
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salario'] = float(input('Salario: R$ '))
    trab['aposentadoria'] = (trab['contratação']+35) - nascimento
print('-='*40)
for k, v in trab.items():
    print(f'{k} tem o valor {v}')
