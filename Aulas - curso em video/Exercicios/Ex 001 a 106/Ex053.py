# 53 - Crie um programa que leia uma frase qualquer e difa se ela é palindromo, desconsiderando os espaços.
# Ex: apos a sopa / a sacada da casa / a torre da derrota / o lobo ama o bolo / anotaram a dara da maratona

'''frs = str(input('Digite um frase: ')).lower().replace(' ','')
ultimo = len(frs)-1

frase = True
for c in range(0,len(frs)):
    if frs[c] != frs[ultimo]:
        frase = False
    ultimo -= 1

if  frase:
    print('A frase é um palindromo')
else:
    print('A frase NÃO é um palindromo')'''

frase = str(input('Digite um frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
#inverso = ''
inverso = junto[::-1]

#for letra in range(len(junto)-1,-1,-1):
#   inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')