# 66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos númentos foram digitados e qual foi a soma entre ele (desconsideran o flag)
soma = count = 0
while True:
    num = int(input('Digite um numero: (999 p/ encerrar) '))
    if num == 999: break
    soma += num
    count += 1
print(f'Você digitou {count} números e a soma entre eles foi {soma}.')