# 48 - Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se ecnontram no intervalo de 1 até 500.

soma = 0
count = 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            #print(i, end= ' ')
            count +=1
            soma += i

#print(soma, end=" ")

'''for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        count += 1
        soma += i'''
print('A soma de todos os {} valores solicitados é {}'.format(count,soma))

