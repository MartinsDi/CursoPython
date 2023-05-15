# 31 - Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km e R$ 0,45 para viagens mais longas

dist =  float(input('Qual a distancia da viagem? '))

if dist <= 200:
    vl = dist * 0.5
    print('O valor da passagem é de R${:.2f}'.format(vl))
else:
    vl = dist *0.45
    print('O valor da passagem é de R${:.2f}'.format(vl))


preço = dist * 0.5 if dist <= 200 else dist * 0.45
