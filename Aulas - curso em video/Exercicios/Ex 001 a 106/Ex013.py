# 13 - Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

sal = float(input("Qual o salário do funcionário? R$"))
# novo = sal + (sal * 15 / 100)
print("Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(sal, sal * 1.15))
