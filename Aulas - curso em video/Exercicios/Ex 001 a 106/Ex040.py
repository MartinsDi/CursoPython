# 40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado / - Média entre 5.0 e 6.9: RECUPERAÇÃO / - Média 7.0 ou superior: APPROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))
if media < 5.0:
    print('O aluno está \033[31mREPROVADO\033[m')
elif media < 7:
    #7 > media >= 5
    print('O aluno está em \033[33mRECUPERAÇÃO\033[m')
else:
    print('O aluno está \033[32mAPROVADO\033[m')