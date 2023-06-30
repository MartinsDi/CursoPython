with open('Dados.txt', 'r') as aq:
    dado = aq.readlines()
permissao = 53

def Listas():
    listas = []


    for linha in dado:
        l1 = linha.rstrip('\n')
        #listas.append(l1.split('\t'))
        listas.append(l1.split(' '))

    return listas


