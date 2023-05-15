nome = input("Qual é o seu nome? ")
print("Prazer em te conhcer {}!".format(nome))
print("Prazer em te conhcer {:20}!".format(nome))
print("Prazer em te conhcer {:>20}!".format(nome))
print("Prazer em te conhcer {:<20}!".format(nome))
print("Prazer em te conhcer {:^20}!".format(nome))
print("Prazer em te conhcer {:=^20}!".format(nome))

n1 = int(input("Um valor: "))
n2 = int(input("Outro vallor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m, d) , end=" ")  #{:.3f} formata para 3 casas depois da virgula, flutuante | , end=" " Não quebra barra \n quebra linha
print("A divisão inteira é {} e a potencia é {}".format(di, e))