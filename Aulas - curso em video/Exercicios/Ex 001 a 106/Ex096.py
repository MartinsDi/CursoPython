# 96 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno
def área(l, c):
    ar = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {ar:.1f}m²')


print(' Controle de Terrenos\n','-'*20)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
área(larg,compr)