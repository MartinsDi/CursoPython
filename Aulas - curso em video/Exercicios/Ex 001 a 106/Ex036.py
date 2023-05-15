# 36 - Escreva um programa para aprovar empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.

valorCasa = float(input('Valor da casa? R$'))
salario = float(input('Salario do comprador ? R$'))
tempo = int(input('Quantos anos de financiamento? '))
mensal = valorCasa / (tempo * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valorCasa, tempo,mensal))

if mensal <= salario*0.3:
    print('\033[32mAPROVADO\033[m')
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('\033[31mNEGADO\033[m')