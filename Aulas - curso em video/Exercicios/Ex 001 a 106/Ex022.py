# 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todos as letras maiúsculas
#O nome com todas minusculas
#Quantas letras ao tdo (sem considerar espaços)
#Quantas letras tem o primeiro nome


nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em maiusculas é {}.".format(nome.upper()))
print("Seu nome em minusculas é {}.".format(nome.lower()))
print("O nome tem {} letras".format((len(nome)-nome.count(" "))))


print("O primeiro nome tem {} letras".format(len(nome[0:nome.find(" ")])))
list = nome.split()
print("O primeiro nome tem {} letras.".format(len(list[0])))


print("O primeiro nome tem {} letras.".format(nome.find(" ")))#professor