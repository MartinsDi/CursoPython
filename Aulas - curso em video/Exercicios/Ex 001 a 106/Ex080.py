# 80 - Crie um programa onde o usúario possa digitar cinco valores numérios e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numeros = list()

'''for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if len(numeros) == 0 :
        numeros.append(n)
    else:
        for i in range(0,len(numeros)):
            if n < numeros[i]:
                numeros.insert(i,n)
                break
            elif i == len(numeros)-1:
                numeros.append(n)
                break
print(numeros)'''

# Versão professor

for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {numeros}')