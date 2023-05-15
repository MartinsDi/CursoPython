# 50 - Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, descondidere-o

soma = 0
count = 0

for i in range(1,7):
    num = int(input("Digite o {}º numero: ".format(i)))
    if num % 2 == 0:
        soma += num
        count += 1

print('Você informou {} números PARES e a soma foi {}'.format(count,soma))