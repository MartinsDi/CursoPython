# 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

'''cadastro = []
aluno = []
nota = []
media = 0
while True:
    aluno.append(str(input('Nome: ')).strip().title())
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota.copy())
    cadastro.append(aluno.copy())
    nota.clear()
    aluno.clear()
    while True:
        resp  = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*50)
print(f'{"No.":4}{"NOME":10}{"MÉDIA":6.1f}')
print('-'*20)
for c , i in enumerate(cadastro):
   media = (i[1][0] + i[1][1]) / 2
   print(f'{c:<4}{i[0]:10}{media:>6}')
while True:
    print('-'*20)
    ind = int(input('Mostrar notas de qual aluno? (-1 interrompe): '))
    if ind == -1:
        break
    if ind < len(cadastro):
        print(f'Notas de {cadastro[ind][0]} são {cadastro[ind][1]}')
    else:
        print('Indice invalido! Tente novamente!')
print('PROGRAMA FINALIZADO')'''''
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2] , media])
    resp = str(input('Quer continuar? (S/N) ')).upper()
    if resp in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (-1 interrompe) '))
    if opc == -1:
        print('FINALIZANDO...')
        break
    if opc < len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')