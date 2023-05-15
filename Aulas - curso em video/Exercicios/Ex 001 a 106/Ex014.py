# 14 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

gc = float(input("Informe a temperatura em ºC: "))
gf = gc * 9 / 5 + 32
print("A temperatura de {}ºC corresponde a {}ºf.".format(gc, gf))
