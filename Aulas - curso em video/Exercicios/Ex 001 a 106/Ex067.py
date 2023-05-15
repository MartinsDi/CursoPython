# 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input("Quer ver a tauada de qual valor? "))
    print("-"*30)
    if num < 0:
        break
    for i in range(1,11):
        print(f"{num} x {i:2} = {num * i:2}")

    print("-"*30)
print('PROGRAMA TABUADA ENCERRADO! Volte sempre.')