# 49 - Refaça o DESAFIO 009, mostre a tabuada de um número que o usuario escolher, só que agora utilizando laço for

num = int(input("Digite um numero para ver sua tabuada: "))

print("A tabuada de {} é: ".format(num))
print("-"*12)
for i in range(1,11):
    print("{} x {:2} = {}".format(num, i, num*i))

print("-"*12)