# 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

vlr = float(input("Qual o preço do produto: R$"))

#desconto = vlr - (vlr * 5 / 100)

print("O produto que custava R${:.2f} com desconto de 5% fica R${:.2f}".format(vlr, vlr*0.95))

# outra versão

vlr = float(input("Qual o preço do produto: R$"))

print("O produto custava R${:.2f} \nPagando a vista tem desconto de 10% fica R${:.2f}\nParcelando no cartão tem acrescimo de 6% e fica R${}".format(vlr, vlr*0.9, vlr*1.06))

