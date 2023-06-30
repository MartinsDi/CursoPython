with open('Dados.txt', 'r') as aq:
    dado = aq.readlines()

listas = []
permissao = 53

for linha in dado:
    l1 = linha.rstrip('\n')
    listas.append(l1.split('\t'))

print(listas)