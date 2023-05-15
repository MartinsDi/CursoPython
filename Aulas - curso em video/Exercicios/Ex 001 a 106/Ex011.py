# 11 - Faça um programa que leia a largura e altura de parede em metros , calcule a sua área e a quatidade de tinta
# necessaria para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m2.

b = float(input("Digite a largura: "))
a = float(input("Digite a altura: "))
ar = b*a

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(b,a,ar))
print("Para pintar essa parede, você precisará de {:.1f}l de pintar.".format(ar/2))
