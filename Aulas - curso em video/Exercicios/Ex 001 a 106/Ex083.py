# 83 - Crie um programa onde o usúario digite uma expressão qualquer que use parênteces.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
pd = 0

exp = str(input('Digite uma expressão: '))

'''for i in exp:
    if i in '(':
        pd += 1
    eliif i == ')' and pd > 0:
        pd -= 1
    elif i == ')' and pd == 0:
        print('Sua expressão está errada!')
        break
if pd == 0:
    print('Sua expressão está valida!')'''


#Versão do professor

pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')