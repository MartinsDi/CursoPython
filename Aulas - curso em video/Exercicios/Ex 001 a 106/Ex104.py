# 104 - Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor númérico.
# Ex: n = leiaInt('Digite um n')
def leiaInt(frs):
    while True:
        print('-'*30)
        num = input(frs)
        if num.isnumeric():
            return int(num)
            break
        else:
            print('\033[31mERRO! digite um número inteiro valido.\033[m')
'''def leiaInt(msg):#Versão do professor
    ok = False
    valor = 0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! digite um número inteiro valido.\033[m')
        if ok:
            break
    return valor'''

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')