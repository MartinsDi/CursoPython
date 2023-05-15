# 63 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))

prim = 0
seg = 1
terc = 0
cont = 0
while n > cont:
    if cont == 0:
        print( '0 → ',end='')
        cont+=1
    if cont == 1:
        print('1 → ', end='')
        cont += 1
    terc = prim + seg
    print(terc,' → ',end='')
    prim = seg
    seg = terc
    cont+=1
print('FIM')

t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1,t2, end=''))
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(" → {}".format(t3),end='')
    cont+=1
    t1 = t2
    t2 = t3

print('→ FIM')
print('~'*30)
