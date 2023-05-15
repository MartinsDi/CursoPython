# Modulos de 95 a 100
'''def mostraLinha(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-' * 30)


mostraLinha('CURSO EM VIDEO')
mostraLinha('CADASTRO DE FUNCIONÁRIOS')
mostraLinha('ERRO DO SISTEMA')'''
'''def soma(a, b):
    s = a + b
    return s


result = soma(6,5)
print(result)'''
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(b=6, a=8)'''
'''def contador(*num):# " * " é o simbolo de desempacotar  
    print(num)
    soma = 0
    for i in num:
        soma += i
    print(soma)




contador(8,2,4,5,6,7,1,0)'''


'''def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
    print(list)

valores = [7, 2, 5, 0, 4]
dobra(valores)'''
