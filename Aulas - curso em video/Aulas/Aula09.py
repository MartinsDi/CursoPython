frase = "Curso em Video Python"
#No fatiamento a ultima posição é sempre ignorada pelo python

frase[9] #Mostra caracter na posição 9
frase[9:13] #Mostas os caracteres da pisição 9 a posição 12
frase[9:21:2] #Mostra os caracteres da posição 9 a 21 pulando 2 posições | VdoPto
frase[:5] #Como não foi definido a posição de inicio automaticamente inicia na posição zero
frase[15:] #como não foi definido aa posição final automaticamente sera feito até o final da string
frase[9::3]

len(frase) #len() é o metodo length
frase.count('o') # faz a contagem de quantas vezes o caracter aparece
frase.count("o",0,13) # faz a contagem dos caracteres da posição 0 a posição 12
frase.find('deo') # ira informar a primeira vez que foi encontrada a parte da string e mostrata aonde inicia

frase.rfind()

'Curso' in frase #retorna um boolean

# transformação

frase.replace('Python','Android') # Ira porcurar a palavra Python e substituir por Android
frase.upper()#Deixa a frase inteira em maiusculo
frase.lower()#Deixa a frase inteira em minusculo
frase.capitalize()#Ira manter o primeiro caracter em maiusculo e minisculo o restante da string
frase.title()#ira converter o primeiro caracter de cada palavra em maiusculo
frase.strip()#remove os espaços inuteis antes da string e apos a string
frase.rstrip()#remove somente os espaços finais
frase.lstrip()#remove somente os espaços iniciais

#Divisão

frase.split()#

#Junção

'-'.join(frase)