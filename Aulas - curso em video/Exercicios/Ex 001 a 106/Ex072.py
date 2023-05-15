# 72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclaado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}')
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
        if resp == 'N':
            break
    print('Tente novamente. ',end='')
