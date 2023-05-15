# 6 - Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num = float (input("Digite um numero: "))
print("O dobro é {}\nO triplo é {} \nA raiz quadrada é {:.2f}".format(num*2, num*3, num**(1/2)))