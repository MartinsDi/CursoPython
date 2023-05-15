# 19 - Um professoe quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

vetor = []

vetor.append(input('Primeiro aluno: '))
vetor.append(input('Segundo aluno: '))
vetor.append(input('Terceiro aluno: '))
vetor.append(input('Quarto aluno: '))
int = random.randint(0,3)

print("O aluno escoljido foi {}!".format(vetor[int]))

print("O aluno escoljido foi {}!".format(random.choice(vetor)))