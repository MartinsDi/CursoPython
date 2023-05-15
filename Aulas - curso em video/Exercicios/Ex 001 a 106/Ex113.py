# 113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leia Float() com a mesma funcionalidade.
def leiaInt(frs):
    while True:
        try:
            num = int(input(frs))
        except (ValueError, TypeError):
            print('\033[31mERRO! digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse numero\033[m')
            return 0
        else:
            return num


def leiaFloat(frs):
    while True:
        try:
            num = float(input(frs))
        except(ValueError, TypeError):
            print('\033[31mERRO! digite um número real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num

i = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real doi {r}')
