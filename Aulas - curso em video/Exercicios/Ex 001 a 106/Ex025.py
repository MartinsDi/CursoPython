# 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input("Digite o nome inteiro: ")).strip()

if "Silva" in nome.title():
    print("O nome tem Silva")
else:
    print("O nome não tem Silva")

print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))