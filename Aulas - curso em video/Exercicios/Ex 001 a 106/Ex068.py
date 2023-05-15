# 68 - faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)
count = 0

while True:
    num = int(input('Diga um valor: '))
    tipo =''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? (P/I) ')).strip().upper()[0]
    numMaquina = randint(0, 10)
    print('-' * 20)
    resp = num + numMaquina
    print(f'Você jogou {num} e o computador {numMaquina}. Total de {resp} ', end='')

    if resp % 2 == 0:
        print('DEU PAR')
        opf = 'P'
    elif resp % 2 != 0:
        print('DEU ÍMPAR')
        opf = 'I'
    print('-' * 20)

    if tipo == opf:
        print('Você VENCEU!')
        count += 1
    else:
        print('Você PERDEU! ')
        break
print(f'GAME OVER! Você venceu {count} vezes.')


while True:
    num = int(input('Diga um valor: '))
    tipo =''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? (P/I) ')).strip().upper()[0]
    numMaquina = randint(0, 10)
    print('-' * 20)
    resp = num + numMaquina
    print(f'Você jogou {num} e o computador {numMaquina}. Total de {resp} ', end='')
    print('DEU PAR' if resp % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if resp % 2 == 0:
            print('Você VENCEU!')
            count += 1
        else:
            print('Você PERDEU! ')
            break
    if tipo == 'I':
        if resp % 2 == 1:
            print('Você VENCEU!')
            count += 1
        else:
            print('Você PERDEU! ')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! vOCÊ VENCEU {count} vezes.')
