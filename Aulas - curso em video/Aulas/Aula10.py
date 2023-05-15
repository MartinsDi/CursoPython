'''tempo = int(input("Quantos anos tem seu carro: "))
if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho")


print("Carro novo"if tempo <= 3 else "Carro velho." )'''

'''nome = str(input("Qual é o seu nome? ")).strip()

if nome == 'Diego':
    print("Que nome lindo você tem! ")
else:
    print("Seu nome é tão normal!")

print("Bom dia, {}!".format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi {:.2f}!'.format(m))

if m >= 6.0:
    print('Sua média foi boa, parabens!')
else:
    print('Sua média foi ruim, estude mais!')


