# 106 - Faça um mini-sistema que utilize o interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.
'''def linha(str, num):
    cont = len(str) + 4
    print(f'\033[{num}m~'*cont)
    print(f'  {str}')
    print('~' * cont,'\n\033[m')


while True:
    linha('SISTEMA DE AJUDA PyHELP', 42)
    soli = str(input('Função ou Biblioteca > '))
    if soli == 'FIM':
        linha('ATÉ LOGO!',41)
        break
    linha(f'Acessando o manual do comando {soli}',44)
    print(f'\033[7;40m')
    help(soli)
    print(f'\033[m')'''

# Versão do professor
from time import sleep
c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;40m')


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(1)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        título('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)


