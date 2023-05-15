# 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar   Considere US$1,00 == R$3,27

din = float(input("Quanto dinheiro você tem na carteira? R$"))
dol = din/3.27
print("Com R${:.2f} voce pode comprar US${:.2f} ".format(din, dol))