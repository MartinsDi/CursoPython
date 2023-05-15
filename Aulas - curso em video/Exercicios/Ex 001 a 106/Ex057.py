# - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso estejá errado, peça a digitação novamente até ter uma valor correto.

sex = ' '
while sex not in "FM":
    sex = str(input('Qual é o sexo? (M/F) ')).strip().upper()
    if sex not in "FM":
        print('Opção {} é invalida, redigite'.format(sex))

#versão professor
sex = str(input('Qual é o sexo? (M/F) ')).strip().upper()[0]#pegando a primeira letra
while sex not in "FM":
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sex))