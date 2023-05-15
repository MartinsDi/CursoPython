# 23 - Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex: Digite um numero: 1834
#Unidade: 4
#dezena: 3
#centendas:8
#Milhar: 1

ns = int(input("Digite um numero entre 0 e 9999: "))
n = str(ns)
#print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(ns[3],ns[2],ns[1],ns[0]))


ml = ns // 1000
ns = ns % 1000
ct = ns // 100
ns = ns % 100
dz = ns // 10
ns = ns % 10
un = ns // 1

print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(un,dz,ct,ml))

#Versão do professor
u = ns // 1 % 10
d = ns // 10 % 10
c = ns // 100 % 10
m = ns // 1000 % 10

print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(u,d,c,m))
