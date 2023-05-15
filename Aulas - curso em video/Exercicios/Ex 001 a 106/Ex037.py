# 37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

'''=	Coloca o sinal na posição mais à esquerda
b	Converte o valor em binário equivalente
o	Converte o valor para o formato octal
x	Converte o valor para o formato Hex
d	Converte o valor dado em decimal
E	Formato científico, com um E em maiúsculas
X	Converte o valor para o formato Hex em maiúsculas'''

num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')
op = int(input('Sua opção: '))

if op == 1:
    #conv = bin(num) #converte em binario mas acrescenta 0b no incio da string
    #conv = {0:b}.format(num)
    #conv = format(num, "b") #as duas com format converte mas sem o 0b
    print('O valor {} convertido em BINÁRIO é {}.'.format(num, format(num,"b")))
elif op == 2:
    #conv = oct(num)
    print('O valor {} convertido em OCTAL é {}.'.format(num, format(num,"o")))
elif op == 3:
    #conv = hex(num)
    print('O valor {} convertido em HEXADECIMAL é {}.'.format(num, format(num, "x")))
else:
    print('Opção invalida. Tente novamente')
