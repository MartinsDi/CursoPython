# 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.]
# Ex: Ana Maria de Souza
# primeiro = Ana
# Último = Souza

nome = str(input("Digite seu nome completo: ")).title().strip()

print("Muito prazer em te conhecer! ")
print("Nome: {}.\nprimeiro = {}.\núltimo = {}.\n".format(nome, nome[:nome.find(" ")],nome[nome.rfind(" "):]))

list = nome.split()

print("Nome: {}.\nprimeiro = {}.\núltimo = {}.".format(nome, list[0], list[len(list)-1]))

