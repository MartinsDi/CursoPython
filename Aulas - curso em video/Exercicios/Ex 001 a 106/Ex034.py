# 34 - Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento pe de 15%.

salario = float(input('Qual é o salario do funcionário? R$'))

if salario >1250:
    salNovo = salario * 1.1
else:
    salNovo = salario * 1.15

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,salNovo))
