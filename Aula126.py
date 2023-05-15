lista = (1,2,2,2,3,5,4,8,1)
st = {'Luiz'}
st.add(3) #permite a adição de um item de cada vez
st.update(("Olá mundo", 1,2,3)) #pemite a adição de varios items dentro de um interavel
st.clear() #limpa o set
st.discard('Olá mundo') # exclui o item especificado
#s1 = set(lista)
#s2={5,6,7,8,9,10,1}
s1 = {1,2}
s2 = {2,3}



print( s1 | s2) #união dos dois sets
print( s1 & s2) #intersecção, itens presentes nos dois
print( s1 - s2) #diferença, itens presentes apenas no set da esquerda
print( s1 ^ s2) #diferença simetrica, itens que não estão em ambos
