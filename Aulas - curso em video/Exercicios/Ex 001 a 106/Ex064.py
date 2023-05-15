# 64 - Crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuario digitar o valor 999.
# que é a condição de para, No final mostre quantos foram digitados e qual foi a soma entre eles, desconsiderando o 999
soma = 0
count = 0
num = 0
while num != 999:
    num = int(input('Digite um numero: (999 p/ encerrar) '))
    if num == 999:break
    soma += num
    count +=1

print('A soma dos {} numeros informados da {}.'.format(count,soma))
print('Você digitou {} números e a soma entre eles foi {}.'.format(count,soma))

#Versão professor
num = int(input('Digite um numero: (999 p/ encerrar) '))
while num != 999:
    soma += num
    count +=1
    num = int(input('Digite um numero: (999 p/ encerrar) '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(count,soma))