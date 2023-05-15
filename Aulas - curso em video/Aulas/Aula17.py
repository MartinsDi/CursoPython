'''lanche = ['Hamburguer','Suco','Pizza','Sorvete']
lanche.append('Cookie')
lanche.insert(0,'Cachorro quente')
print(lanche)
#del lanche[3]
#lanche.pop(3) # del e pop remove pelo indice
#lanche.remove('Pizza') # remove remove pelo conteudo
print(lanche)
resp = lanche.pop()
print(lanche)
print(resp)
if 'Pizza' in lanche:# contorna o erro de remover algo que não esteja na lista
    lanche.remove('Pizza')
valores = list(range(4,11))# vai popular a lista em ordem com os numeros de 4 a 10, é obrigatorio usar list
valores = [8,2,5,4,9,3,0]
valores.sort() # ordena a lista
valores.sort(reverse=True) # ordena a lista ao contrario
valores.reverse()#inverte a lista sem fazer nenhuma ordenação
valores.clear() # Zera a lista
valores.copy()
print(valores)'''
'''valores = [5,9,4]
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''
a = [2,3,4,7]
b = a
c = a.copy()
b[2] = 8
c[1] = 5
print(f'Lista a {a}')
print(f'Lista b {b}')
print(f'Lista c {c}')