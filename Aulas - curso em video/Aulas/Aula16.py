# Tuplas são IMUTAVEIS
# Aceita diversos tipos de dados ao mesmo tempo
# () tuplas [] Lista {} dicionario
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[-1])  # mostra o ultimo termo, -2 o penultimo assim em diante

for pos, i in enumerate(lanche):
    print(i)

lanche[3] = "Lasanha"

print(sorted(lanche))  # sorted ordena sem alterar a tupla

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))  # Vai contar quantos 5 tem na tupla
print(c.index(8))# vai mostrar a posição do numero
print(c.index(2, 4))# vai mostrar a posição do numero 2 a partir da 4 posição
pessoa = ("Diego", 26, 'M', 137)
del(lanche) # Irá deletar a tuplas, metodo del() apaga qualquer dado