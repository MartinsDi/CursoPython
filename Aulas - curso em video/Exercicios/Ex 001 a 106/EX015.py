# 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
VlrKm = km * 0.15
VlrDia = 60 * dias

print("-"*33)
print("Km: {:7} - Valor R${:>11.2f}\nDias: {:5} - Valor R${:>11.2f}".format(km,VlrKm,dias,VlrDia))
print("Valor total R${:>19.2f}".format(VlrDia+VlrKm))
print("-"*33)