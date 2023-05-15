# 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

vetor = []

vetor.append(input("Primeiro aluno: "))
vetor.append(input("Segundo aluno: "))
vetor.append(input("Terceiro Aluno: "))
vetor.append(input("Quarto aluno: "))

random.shuffle(vetor)

print("A ordem de aprensetação será {}".format(vetor))
print("A ordem de aprensetação será {}, {}, {} e {}".format(vetor[0],vetor[1],vetor[2],vetor[3]))



