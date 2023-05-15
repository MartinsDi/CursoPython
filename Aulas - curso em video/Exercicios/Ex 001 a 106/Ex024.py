# 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input("Digite o nome da cidade: ").strip())

cidade = cidade.upper()

list = cidade.split()

if "SANTO" in list[0]:
    print("A cidade começa com SANTO")
else:
    print("A cidade não começa com SANTO")


print(cidade[:5]=="SANTO")#professor