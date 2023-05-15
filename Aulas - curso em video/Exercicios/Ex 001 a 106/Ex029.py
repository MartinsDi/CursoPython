# 29 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custa R$ 7,00 por cada Km acima do limite.

vel = float(input('Qual é a veloidade atual do carro?  '))

if vel > 80:
    print('MULTADO! Excedeu o limite de 80Km/h ')
    m = (vel-80)*7
    print('O valor da multa é de R${:.2f}!'.format(m))

print('Tenha um bom dia! Dirija com segurança')