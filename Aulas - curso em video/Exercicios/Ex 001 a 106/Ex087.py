# 87 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
soma = somat = 0

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(num)
        if num % 2 == 0:
            soma += num
    somat += matriz[i][2]
print('-=' * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}] ', end='')
    print()
print('-=' * 30)
print(
    f'A soma dos valores pares é {soma}\nA soma dos valores da terceira coluna é {somat}\nO maior valor da segunda linha é {max(matriz[1])}')
