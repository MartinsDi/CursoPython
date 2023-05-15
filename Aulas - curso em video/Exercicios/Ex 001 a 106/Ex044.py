# 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto | Á vista no cartão: 5% de desconto | em até 2x no cartão: preço normal | 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('MANNYS BURGER'))
valor = float(input('Valor da compra: R$'))
print('FORMAS DE PAGAMENTO\n[1] á vista dinheiro/cheque\n[2] Á vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
op = int(input('Qual é a opção: '))

if op == 1:
    valorAtual = valor * 0.9
elif op == 2:
    valorAtual = valor * 0.95
elif op == 3:
    valorAtual = valor
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(valorAtual/2))
elif op == 4:
    parc = int(input('Quantas parcelas? '))
    valorAtual = valor * 1.2
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc, valorAtual / parc))
else:
    valorAtual = valor
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(valor,valorAtual))
